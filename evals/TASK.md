# ATT&CK mapping task

The prompt given to each model. Replace SKILL_DIR with the skill folder under test and CASES_DIR with `evals/cases`.

---

You are testing an agent skill for mapping text to MITRE ATT&CK v20 Enterprise technique IDs.

The skill is in SKILL_DIR. Read SKILL_DIR/SKILL.md first and follow it, using the resource files under SKILL_DIR/resources with grep or by reading them.

Map each case file in CASES_DIR (case01.md to case16.md). For each case, list every ATT&CK technique or sub-technique ID that the case text shows was performed (for detection rules: the behaviour the rule detects; for Atomic tests: what the test performs; for reports: everything the attacker did).

Strict rules:
- Use only SKILL_DIR, CASES_DIR and your own knowledge. Do NOT open, list or search any other files or directories, or the web. This is a blind test.
- Do not write or modify any files.
- Work through all 16 cases.

Final answer: only a JSON object, no prose before or after, in this shape:
{"case01": {"techniques": ["T1059.001", "T1105"], "note": "one short line"}, "case02": {...}, ...}
