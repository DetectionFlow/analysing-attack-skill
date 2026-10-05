"""Generate the analysing-attack skill resources from MITRE ATT&CK STIX data.

    uv run generate.py           # compress new or changed techniques, rewrite resources and zip
    uv run generate.py --all     # recompress every technique
    uv run generate.py --check   # verify committed files against STIX and the cache (no LLM calls)

To move to a new ATT&CK release: bump ATTACK_VERSION, add it to RELEASES, add a row to the
Version Timeline in attack_version_changelog.md, then run this script.
"""

import argparse
import hashlib
import io
import json
import re
import sys
import zipfile
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from pathlib import Path

import anthropic
import requests
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError

ATTACK_VERSION = "19.2"
STIX_URL = (
    "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/"
    f"enterprise-attack/enterprise-attack-{ATTACK_VERSION}.json"
)

# Release dates. An object is attributed to the first release on or after its creation date.
RELEASES = {
    "15": "2024-04-23",
    "15.1": "2024-05-02",
    "16": "2024-10-31",
    "16.1": "2024-11-12",
    "17": "2025-04-22",
    "17.1": "2025-05-06",
    "18": "2025-10-28",
    "18.1": "2025-11-13",
    "19": "2026-04-28",
    "19.1": "2026-05-12",
    "19.2": "2026-08-05",
}
CHANGELOG_SINCE = "2023-11-16"  # v14.1 release: the changelog covers everything after it

MODEL = "claude-opus-5-5"
EFFORT = "medium"
BATCH_SIZE = 10
MAX_ATTEMPTS = 3
WORKERS = 4

ROOT = Path(__file__).parent
SKILL_DIR = ROOT / "analysing-attack-skill"
TECHNIQUES_PATH = SKILL_DIR / "resources" / "attack_techniques.md"
KEYWORDS_PATH = SKILL_DIR / "resources" / "attack_keywords.idx"
CHANGELOG_PATH = SKILL_DIR / "resources" / "attack_version_changelog.md"
SKILL_PATH = SKILL_DIR / "SKILL.md"
README_PATH = ROOT / "README.md"
ZIP_PATH = ROOT / "analysing-attack-skill.zip"
CACHE_PATH = ROOT / "technique_cache.json"
DATA_PATH = ROOT / "data" / f"enterprise-attack-v{ATTACK_VERSION}.json"

TACTIC_ABBR = {
    "reconnaissance": "REC",
    "resource-development": "RD",
    "initial-access": "IA",
    "execution": "EX",
    "persistence": "PE",
    "privilege-escalation": "PRV",
    "stealth": "ST",
    "defense-impairment": "DIM",
    "credential-access": "CA",
    "discovery": "DIS",
    "lateral-movement": "LM",
    "collection": "COL",
    "command-and-control": "C2",
    "exfiltration": "EXF",
    "impact": "IMP",
}
TACTIC_LEGEND = (
    "REC=Reconnaissance, RD=Resource Development, IA=Initial Access, EX=Execution, PE=Persistence, "
    "PRV=Privilege Escalation, ST=Stealth, DIM=Defense Impairment, CA=Credential Access, DIS=Discovery, "
    "LM=Lateral Movement, COL=Collection, C2=Command and Control, EXF=Exfiltration, IMP=Impact"
)

SYSTEM_PROMPT = """You compress MITRE ATT&CK technique descriptions into a compact reference for AI agents.

The agents map behaviour seen in threat intelligence reports, detection rules and incident data to technique IDs. They find candidates by grepping a keyword index built from your keywords, then read your description to confirm the match. So keywords must be the concrete strings that actually show up in that source material, and descriptions must say what distinguishes each technique from its neighbours.

For every technique in the input return:

keywords: 3 to 10 terms an analyst would search for: file names and paths, process and tool names, command-line flags, API calls, registry keys, protocols, event sources. Prefer terms specific to this technique. Skip generic security vocabulary (adversary, malicious, attack) and ubiquitous terms (such as powershell) unless the technique is specifically about them. Each keyword is plain text with no commas or pipe characters.

description: a single sentence of at most 40 words (20 to 35 is ideal) that starts with an action verb and states what technically happens and what makes it distinct. No filler, no citations, no pipe characters or line breaks.

Sub-technique names are given as "Parent: Sub-technique". Return every input ID exactly once."""

TECHNIQUE_ID = re.compile(r"T\d{4}(?:\.\d{3})?")


class Compressed(BaseModel):
    id: str
    keywords: list[str]
    description: str


class CompressedBatch(BaseModel):
    techniques: list[Compressed]


# --- STIX ---------------------------------------------------------------------------------------


def load_stix() -> list[dict]:
    if not DATA_PATH.exists():
        print(f"Downloading ATT&CK v{ATTACK_VERSION}...")
        response = requests.get(STIX_URL, timeout=300)
        response.raise_for_status()
        response.json()["objects"]  # fail here rather than cache a bad payload
        DATA_PATH.parent.mkdir(exist_ok=True)
        DATA_PATH.write_bytes(response.content)
    return json.loads(DATA_PATH.read_text())["objects"]


def attack_id(obj: dict) -> str:
    return next(r["external_id"] for r in obj["external_references"] if r.get("source_name") == "mitre-attack")


def is_active(obj: dict) -> bool:
    return not obj.get("revoked") and not obj.get("x_mitre_deprecated")


def sort_key(technique_id: str) -> tuple[int, int]:
    parent, _, sub = technique_id[1:].partition(".")
    return int(parent), int(sub or 0)


def release_of(date: str) -> str:
    """Version of the first release on or after an ISO date."""
    return next((v for v, released in RELEASES.items() if date[:10] <= released), "unreleased")


def load_techniques(objects: list[dict]) -> dict[str, dict]:
    """Active Enterprise techniques keyed by ID, in ID order. Sub-techniques are named 'Parent: Sub'."""
    patterns = {attack_id(o): o for o in objects if o["type"] == "attack-pattern" and is_active(o)}
    techniques = {}
    for tid in sorted(patterns, key=sort_key):
        obj = patterns[tid]
        parent = patterns.get(tid.split(".")[0]) if "." in tid else None
        techniques[tid] = {
            "id": tid,
            "name": f"{parent['name']}: {obj['name']}" if parent else obj["name"],
            "description": obj.get("description", ""),
            "tactics": [
                TACTIC_ABBR[p["phase_name"]]
                for p in obj.get("kill_chain_phases", [])
                if p["kill_chain_name"] == "mitre-attack"
            ],
            "platforms": obj.get("x_mitre_platforms", []),
            "created": obj["created"],
        }
    return techniques


# --- Compression --------------------------------------------------------------------------------


def source_hash(technique: dict) -> str:
    """Hash of everything the model sees, so a row is recompressed only when its source changes."""
    return hashlib.sha256(f"{technique['name']}\n{technique['description']}".encode()).hexdigest()[:16]


def problems(keywords: list[str], description: str) -> list[str]:
    found = []
    if not 3 <= len(keywords) <= 10:
        found.append(f"{len(keywords)} keywords, need 3 to 10")
    for kw in keywords:
        if not kw.strip() or any(c in kw for c in "|,\n"):
            found.append(f"keyword {kw!r} is empty or contains a comma, pipe or line break")
    words = len(description.split())
    if not 1 <= words <= 40:
        found.append(f"description is {words} words, need at most 40")
    if any(c in description for c in "|\n"):
        found.append("description contains a pipe or line break")
    return found


def is_stale(technique: dict, cache: dict) -> bool:
    entry = cache.get(technique["id"])
    return (
        entry is None
        or entry["source"] != source_hash(technique)
        or bool(problems(entry["keywords"], entry["description"]))
    )


def compress_batch(client: anthropic.Anthropic, rejected: dict[str, str], batch: list[dict]) -> dict[str, dict]:
    """Compress one batch. Returns cache entries for the items that came back valid."""
    label = f"{batch[0]['id']}..{batch[-1]['id']}"
    payload = [
        {"id": t["id"], "name": t["name"], "description": t["description"]}
        | ({"previous_attempt_rejected": rejected[t["id"]]} if t["id"] in rejected else {})
        for t in batch
    ]
    try:
        response = client.beta.messages.parse(
            model=MODEL,
            max_tokens=16000,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": f"Compress these {len(batch)} techniques:\n\n{json.dumps(payload, indent=1)}",
                }
            ],
            output_config={"effort": EFFORT},
            output_format=CompressedBatch,
            # Safety classifiers can decline security content; let the API re-run it on a fallback model.
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        )
    except (anthropic.RateLimitError, anthropic.InternalServerError, anthropic.APIConnectionError) as e:
        print(f"  {label}: {type(e).__name__}, will retry")
        return {}
    except ValidationError:
        print(f"  {label}: response did not match the schema, will retry")
        return {}
    if response.stop_reason != "end_turn" or response.parsed_output is None:
        print(f"  {label}: stopped with {response.stop_reason}, will retry")
        return {}

    by_id = {t["id"]: t for t in batch}
    accepted = {}
    for item in response.parsed_output.techniques:
        keywords = [kw.strip() for kw in item.keywords]
        description = item.description.strip()
        if item.id not in by_id or item.id in accepted:
            continue
        if found := problems(keywords, description):
            rejected[item.id] = "; ".join(found)
            continue
        accepted[item.id] = {
            "source": source_hash(by_id[item.id]),
            "keywords": keywords,
            "description": description,
        }
    usage = response.usage
    print(f"  {label}: {len(accepted)}/{len(batch)} ok ({usage.input_tokens} in, {usage.output_tokens} out)")
    return accepted


def compress(pending: list[dict], cache: dict) -> None:
    """Compress techniques into the cache, retrying missing or invalid items. Exits if any remain."""
    client = anthropic.Anthropic()
    rejected: dict[str, str] = {}
    done: set[str] = set()
    for attempt in range(1, MAX_ATTEMPTS + 1):
        if not pending:
            return
        print(f"Compressing {len(pending)} techniques with {MODEL} (attempt {attempt}/{MAX_ATTEMPTS})")
        batches = [pending[i : i + BATCH_SIZE] for i in range(0, len(pending), BATCH_SIZE)]
        with ThreadPoolExecutor(WORKERS) as pool:
            for accepted in pool.map(partial(compress_batch, client, rejected), batches):
                cache.update(accepted)
                save_cache(cache)
                done.update(accepted)
        pending = [t for t in pending if t["id"] not in done]
    if pending:
        details = "\n".join(f"  {t['id']}: {rejected.get(t['id'], 'no valid response')}" for t in pending)
        sys.exit(f"Failed to compress {len(pending)} techniques after {MAX_ATTEMPTS} attempts:\n{details}")


def save_cache(cache: dict) -> None:
    ordered = {tid: cache[tid] for tid in sorted(cache, key=sort_key)}
    CACHE_PATH.write_text(json.dumps(ordered, indent=1, ensure_ascii=False) + "\n")


# --- Rendering ----------------------------------------------------------------------------------


def render_techniques(techniques: dict[str, dict], cache: dict) -> str:
    lines = [
        f"# ATT&CK-LLM | Enterprise | v{ATTACK_VERSION}",
        f"# Tactics: {TACTIC_LEGEND}",
        f"# Techniques (inc. sub-techniques): {len(techniques)}",
        "",
        "|ID|Tactics|Name|Keywords|Description|Platforms|",
        "|---|---|---|---|---|---|",
    ]
    for tid, t in techniques.items():
        entry = cache[tid]
        lines.append(
            f"|{tid}|{','.join(t['tactics'])}|{t['name']}|{','.join(entry['keywords'])}"
            f"|{entry['description']}|{','.join(t['platforms'])}|"
        )
    return "\n".join(lines) + "\n"


def render_keywords(techniques: dict[str, dict], cache: dict) -> str:
    index: dict[str, list[str]] = {}
    for tid in techniques:
        for kw in cache[tid]["keywords"]:
            ids = index.setdefault(kw.lower(), [])
            if tid not in ids:
                ids.append(tid)
    lines = [
        f"# ATT&CK Keyword Index | Enterprise | v{ATTACK_VERSION}",
        "# Format: keyword:technique_ids (IDs follow the last colon)",
        '# Usage: grep -i "keyword" attack_keywords.idx',
    ]
    lines += [f"{kw}:{','.join(ids)}" for kw, ids in sorted(index.items())]
    return "\n".join(lines) + "\n"


def changelog_blocks(objects: list[dict], techniques: dict[str, dict]) -> dict[str, str]:
    """The changelog sections that are derived from STIX rather than written by hand."""
    by_stix_id = {o["id"]: o for o in objects}

    revoked = []
    for rel in objects:
        if rel["type"] != "relationship" or rel["relationship_type"] != "revoked-by":
            continue
        old, new = by_stix_id.get(rel["source_ref"]), by_stix_id.get(rel["target_ref"])
        if old and new and old["type"] == "attack-pattern" and rel["created"][:10] > CHANGELOG_SINCE:
            revoked.append((attack_id(old), old["name"], attack_id(new), new["name"], release_of(rel["created"])))
    revoked.sort(key=lambda row: sort_key(row[0]))

    new = [t for t in techniques.values() if t["created"][:10] > CHANGELOG_SINCE]

    changes = [
        "### Revoked or Merged",
        "",
        "| Old ID | Old Name | New ID | New Name | Version |",
        "|---|---|---|---|---|",
    ]
    changes += [f"| {a} | {b} | {c} | {d} | v{v} |" for a, b, c, d, v in revoked]
    changes += ["", "### New", "", "| ID | Name | Version |", "|---|---|---|"]
    changes += [f"| {t['id']} | {t['name']} | v{release_of(t['created'])} |" for t in new]

    groups: dict[str, list[str]] = {}
    for o in objects:
        if o["type"] == "intrusion-set" and is_active(o) and o["created"][:10] > CHANGELOG_SINCE:
            groups.setdefault(release_of(o["created"]), []).append(f"{attack_id(o)} {o['name']}")
    group_lines = [f"**v{v}:** {', '.join(sorted(groups[v]))}" for v in reversed(RELEASES) if v in groups]

    def count(*types: str) -> int:
        return sum(1 for o in objects if o["type"] in types and is_active(o))

    subs = sum(1 for tid in techniques if "." in tid)
    stats = (
        f"## Stats (v{ATTACK_VERSION})\n\n"
        f"Enterprise: {count('x-mitre-tactic')} tactics, {len(techniques) - subs} techniques, {subs} sub-techniques"
        f" | Groups: {count('intrusion-set')} | Software: {count('malware', 'tool')} | Campaigns: {count('campaign')}"
    )
    return {"technique-changes": "\n".join(changes), "groups": "\n\n".join(group_lines), "stats": stats}


def sub_once(pattern: str, replacement: str | Callable, text: str, path: Path, flags: int = 0) -> str:
    text, n = re.subn(pattern, replacement, text, flags=flags)
    if n != 1:
        sys.exit(f"{path.name}: expected exactly one match for {pattern!r}, found {n}")
    return text


def render_changelog(blocks: dict[str, str]) -> str:
    text = CHANGELOG_PATH.read_text()
    text = sub_once(r"(# ATT&CK Version Changes \(v15→v)[\d.]+(?=\))", rf"\g<1>{ATTACK_VERSION}", text, CHANGELOG_PATH)
    for name, body in blocks.items():
        pattern = rf"(<!-- generated:{name} -->\n).*?(<!-- /generated:{name} -->)"
        text = sub_once(pattern, lambda m: f"{m[1]}{body}\n{m[2]}", text, CHANGELOG_PATH, re.S)
    return text


def render_skill() -> str:
    text = SKILL_PATH.read_text()
    text = sub_once(r"(Contains information on v)[\d.]+(?= \(latest\))", rf"\g<1>{ATTACK_VERSION}", text, SKILL_PATH)
    return sub_once(r"(Reference for v15->v)[\d.]+(?= changes)", rf"\g<1>{ATTACK_VERSION}", text, SKILL_PATH)


def render_readme() -> str:
    return sub_once(r"(all ATT&CK v)[\d.]+(?= )", rf"\g<1>{ATTACK_VERSION}", README_PATH.read_text(), README_PATH)


def render_zip(files: dict[Path, str]) -> bytes:
    """A byte-for-byte reproducible zip of the skill folder."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SKILL_DIR.rglob("*")):
            if path.is_file() and path.name != ".DS_Store":
                info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                archive.writestr(info, files[path] if path in files else path.read_bytes())
    return buffer.getvalue()


# --- Validation ---------------------------------------------------------------------------------


def reference_errors(objects: list[dict], techniques: dict[str, dict], files: dict[Path, str]) -> list[str]:
    """Check the hand-written parts of the skill against the STIX data."""
    errors = []
    known = {attack_id(o) for o in objects if o["type"] == "attack-pattern"}
    for tid in sorted(set(TECHNIQUE_ID.findall(files[SKILL_PATH])) - techniques.keys(), key=sort_key):
        errors.append(f"SKILL.md cites {tid}, which is not an active technique in v{ATTACK_VERSION}")
    for tid in sorted(set(TECHNIQUE_ID.findall(files[CHANGELOG_PATH])) - known, key=sort_key):
        errors.append(f"attack_version_changelog.md cites {tid}, which does not exist in Enterprise ATT&CK")
    if f"| v{ATTACK_VERSION} |" not in files[CHANGELOG_PATH]:
        errors.append(f"attack_version_changelog.md has no Version Timeline row for v{ATTACK_VERSION}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--all", action="store_true", help="recompress every technique")
    parser.add_argument("--check", action="store_true", help="verify committed files without calling the model")
    args = parser.parse_args()
    if ATTACK_VERSION not in RELEASES:
        sys.exit(f"Add v{ATTACK_VERSION} and its release date to RELEASES")

    objects = load_stix()
    techniques = load_techniques(objects)
    cache = json.loads(CACHE_PATH.read_text()) if CACHE_PATH.exists() else {}
    stale = list(techniques.values()) if args.all else [t for t in techniques.values() if is_stale(t, cache)]

    if args.check:
        if stale:
            sys.exit(f"{len(stale)} techniques need compressing, e.g. {stale[0]['id']}. Run: uv run generate.py")
    else:
        load_dotenv()
        compress(stale, cache)
        cache = {tid: entry for tid, entry in cache.items() if tid in techniques}
        save_cache(cache)

    files = {
        TECHNIQUES_PATH: render_techniques(techniques, cache),
        KEYWORDS_PATH: render_keywords(techniques, cache),
        CHANGELOG_PATH: render_changelog(changelog_blocks(objects, techniques)),
        SKILL_PATH: render_skill(),
        README_PATH: render_readme(),
    }
    errors = reference_errors(objects, techniques, files)
    archive = render_zip(files)

    if args.check:
        errors += [f"{p.relative_to(ROOT)} is out of date" for p, text in files.items() if p.read_text() != text]
        if not ZIP_PATH.exists() or ZIP_PATH.read_bytes() != archive:
            errors.append(f"{ZIP_PATH.name} is out of date")
    if errors:
        sys.exit("\n".join(errors))
    if args.check:
        print(f"OK: {len(techniques)} techniques, ATT&CK v{ATTACK_VERSION}")
        return

    for path, text in files.items():
        path.write_text(text)
    ZIP_PATH.write_bytes(archive)
    print(f"Wrote {len(techniques)} techniques for ATT&CK v{ATTACK_VERSION}")


if __name__ == "__main__":
    main()
