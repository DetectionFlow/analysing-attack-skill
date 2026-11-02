# Skill evaluation

A small blind test of how well models map text to ATT&CK v20 technique IDs with this skill. Each model gets the same 16 cases and the prompt in [TASK.md](TASK.md), runs once with one version of the skill, and returns technique IDs. [score.py](score.py) compares the answers with [gold.json](gold.json) on exact IDs.

| Cases | Kind |
|---|---|
| 5 | Sigma detection rules |
| 4 | Atomic Red Team tests |
| 5 | ATT&CK procedure example lines (the filed technique is given) |
| 2 | Synthetic probes that use retired IDs (T1086, T1089, T1043, T1562.001 and more) |

The gold labels come from a hand-reviewed procedure gold set: every technique the behaviour implements, plus the technique ATT&CK files the line under. The two probes were written for this test. Optional IDs in a probe's gold are neither credited nor penalised.

## Run it

1. Give a model the prompt in TASK.md, with SKILL_DIR set to the skill folder under test.
2. Save its JSON answer as `results/<model>_<label>.json`.
3. Run `python evals/score.py`. It uses only the standard library.

## Results (2026-11-02)

`before` is the skill at commit 49eed78 and `after` is the version that added this folder. Each model ran once per version.

| Model | F1 before → after | Wrong extra techniques | Correct (of 53) |
|---|---|---|---|
| Claude Sonnet 5.5 | 0.80 → 0.84 | 13 → 6 | 44 → 43 |
| Gemini 4 Argon | 0.73 → 0.77 | 31 → 23 | 48 → 48 |
| Grok 4.7 | 0.72 → 0.76 | 22 → 19 | 42 → 44 |
| Muse Wonder | 0.73 → 0.76 | 19 → 12 | 41 → 40 |
| GPT-6.1 Sol | 0.77 → 0.78 | 22 → 19 | 47 → 46 |

Most of the gain is fewer techniques added without evidence. No model returned a retired ID with either version.

Two CTI-report cases were also used in the original run, but they're left out here because the reports are copyrighted. With them included the trend was the same: wrong extras fell from 201 to 148 across all models, and correct ones went from 373 to 370.

## Limits

- 16 cases and one run per model, so treat the results as a direction, not a benchmark.
- The command-line hints in SKILL.md (PowerShell, WMI and services) came from the same gold set these cases were drawn from. Test them on other cases before relying on them.
- Some gold answers are debatable. For example, `setspn -q` is labelled T1087.002, and most models choose T1558.003.

## Third-party content

The cases quote third-party material, each marked at the top of its file:

- **Sigma rules:** from [SigmaHQ](https://github.com/SigmaHQ/sigma), under the [Detection Rule License 1.1](https://github.com/SigmaHQ/Detection-Rule-License). Authors are kept in each rule.
- **Atomic Red Team tests:** from [Red Canary](https://github.com/redcanaryco/atomic-red-team), MIT License.
- **ATT&CK procedure lines:** © The MITRE Corporation, reproduced under the [ATT&CK Terms of Use](https://attack.mitre.org/resources/legal-and-branding/terms-of-use/).
