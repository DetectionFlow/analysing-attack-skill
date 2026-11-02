"""Score model answers against evals/gold.json.

    python evals/score.py                   # every file in evals/results
    python evals/score.py path/to/answers.json

An answer file maps case ids to {"techniques": [...]}. A technique counts as correct only on an
exact ID match. IDs listed as optional in the gold are neither credited nor penalised. Any ID that
is not an active technique in resources/attack_techniques.md is also counted as non-live.
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
TECHNIQUES = HERE.parent / "analysing-attack-skill" / "resources" / "attack_techniques.md"


def score(answers: dict, gold: dict, live: set[str]) -> dict[str, Counter]:
    totals: dict[str, Counter] = {"all": Counter()}
    for case, expected in gold.items():
        optional = set(expected.get("optional", []))
        want = set(expected["gold"])
        got = {t.strip().upper() for t in answers.get(case, {}).get("techniques", [])} - optional
        for key in ("all", expected["kind"]):
            c = totals.setdefault(key, Counter())
            c["tp"] += len(got & want)
            c["fp"] += len(got - want)
            c["fn"] += len(want - got)
            c["non_live"] += len(got - live)
            c["missing"] += case not in answers
    return totals


def f1(c: Counter) -> tuple[float, float, float]:
    p = c["tp"] / max(1, c["tp"] + c["fp"])
    r = c["tp"] / max(1, c["tp"] + c["fn"])
    return p, r, 2 * p * r / max(1e-9, p + r)


def main() -> None:
    gold = json.loads((HERE / "gold.json").read_text())
    live = set(re.findall(r"^\|(T\d{4}(?:\.\d{3})?)\|", TECHNIQUES.read_text(), re.M))
    paths = [Path(p) for p in sys.argv[1:]] or sorted((HERE / "results").glob("*.json"))
    print(f"{'answers':32} {'P':>5} {'R':>5} {'F1':>5} {'tp':>4} {'fp':>4} {'fn':>4} non-live")
    for path in paths:
        c = score(json.loads(path.read_text()), gold, live)["all"]
        p, r, f = f1(c)
        missing = f"  ({c['missing']} cases missing)" if c["missing"] else ""
        print(f"{path.stem:32} {p:5.2f} {r:5.2f} {f:5.2f} {c['tp']:4} {c['fp']:4} {c['fn']:4} {c['non_live']:8}{missing}")


if __name__ == "__main__":
    main()
