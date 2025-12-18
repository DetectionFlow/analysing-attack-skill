---
name: analysing-attack
description: Analyse Mitre ATT&CK tactics, techniques and sub-techniques. Use when performing analysis of threat detections, threat models, security risks or cyber threat intelligence
---

# Analysing ATT&CK Tactics and Techniques

## Overview

This document provides best practices and resources for use when mapping ATT&CK tactics and techniques to threat detections, threat models, security risks or cyber threat intelligence.

Contains information on v18.1 (latest) version of Mitre ATT&CK

## Available Resources

Resources folder contains LLM optimised and token-efficient content. Read whole file for broad context or grep for specfic keywords or IDs. Use index files for quick reference keyword searches.

Tactics are abreviated: REC=Reconnaissance, RD=Resource Development, IA=Initial Access, EX=Execution, PE=Persistence, PRV=Privilege Escalation, DE=Defense Evasion, CA=Credential Access, DIS=Discovery, LM=Lateral Movement, COL=Collection, C2=Command and Control, EXF=Exfiltration, IMP=Impact

### Searching Examples

**By keyword (recommended for discovery)**:
```grep -i "cron\|bash\|/proc/\|cryptocurrency" resources/attack_keywords.idx```

**By technique ID (for validation)**:
```grep "T1053" resources/attack_techniques.md```

**By tactic abbreviation (find all persistance techniques)**:
```grep "PE" resources/attack_techniques.md```


### Resource Files

**ATT&CK Technique Keyword Index**: Index file for quick keyword searching to identify suitable ATT&CK IDs for further research. Sorted alphabetically and fomatted as keyword:technique_ids (comma seperated when multiple). See -> [resources/attack_keywords.idx](resources/attack_keywords.idx)

**ATT&CK Technique List**: Markdown table containing ATT&CK ID, name, keywords, description and platforms. Sorted by ID. Use when researching techniques, valdiating IDs, searching for up-to-date descriptions or filtering by platform. See -> [resources/attack_techniques.md](resources/attack_techniques.md)

**ATT&CK Version Changelog**: Reference for v15→v18.1 changes including deprecated techniques, renamed platforms, and the v18 detection model overhaul. Use when analysing older reports or understanding structural changes. See -> [resources/attack_version_changelog.md](resources/attack_version_changelog.md)

## Best Practice

Use your judgment alongside these guidelines to generate high-quality ATT&CK analysis.

- Do not assume your knowledge is 100% complete or up to date. Use the resources provided
- Search broadly for keywords, quickly identify techniques, then perform deeper research
- Think about the specific procedure being performed and consider the attacker (or defender) intent before determining appropriate tactic, technique or sub-technique
- Some techniques are part of multiple tactics (for ex. T1078 Valid Accounts) and may appear different in each tactic
- Other techniques are similar but distinct depending on tactic (for ex. T1213.003 and T1593.003 are both Code Respositories)
- Multiple technique IDs may be identified for a single procedure or control. This is normal.
- Map to the most specific sub-technique when possible
- Avoid mapping techniques that are a very minor side effect

### When Analysing CTI Reports

- Read the whole report thourouly
- Screenshots contain valuable intelligence, ensure they are processed
- Download appendixes, IOC lists or STIX files for complete information
- Break down actions to granular procedures for mapping to techniques
- Think about attacker objectives. What did they take that action? What did they hope to achieve?
- Avoid infering techniques that are not contained in the report

### When Analysing Detections

- Detection logic may detect multiple techniques, map all that are applicable
- Analyse detection log sources and fields, these can help determine distinct tactic or techniques
