---
name: analysing-attack
description: Analyse Mitre ATT&CK tactics, techniques and sub-techniques. Use when performing analysis of threat detections, threat models, security risks or cyber threat intelligence
---

# Analysing ATT&CK Tactics and Techniques

## Overview

This document provides best practices and resources for use when mapping ATT&CK tactics and techniques to threat detections, threat models, security risks or cyber threat intelligence.

Contains information on v20 (latest) version of Mitre ATT&CK

## Available Resources

Resources folder contains LLM optimised and token-efficient content. Read whole file for broad context or grep or glob for specfic keywords or IDs. Use index files for quick reference keyword searches.

Tactics are abreviated: REC=Reconnaissance, RD=Resource Development, IA=Initial Access, EX=Execution, PE=Persistence, PRV=Privilege Escalation, ST=Stealth, DIM=Defense Impairment, CA=Credential Access, DIS=Discovery, LM=Lateral Movement, COL=Collection, C2=Command and Control, EXF=Exfiltration, IMP=Impact

### Searching Examples

**By keyword (recommended for discovery)**. Substring search finds variants (`vssadmin` also finds `vssadmin delete shadows`). Technique names are keywords too:
```grep -i "cron\|bash\|/proc/\|cryptocurrency" resources/attack_keywords.idx```

**By technique ID (to validate an ID)**. Anchor it so sub-techniques and keyword mentions do not match:
```grep "^|T1053.005|" resources/attack_techniques.md```

**By tactic abbreviation (all Persistence techniques)**. Match the Tactics column only:
```grep -E "^\|T[0-9.]+\|([A-Z0-9]+,)*PE[,|]" resources/attack_techniques.md```

**Retired IDs**. An ID missing from attack_techniques.md is revoked or deprecated. Look it up:
```grep "^|T1086|" resources/attack_version_changelog.md``` (T1086 is revoked; the table gives its live ID, T1059.001)

### Resource Files

**ATT&CK Technique Keyword Index**: Index file for quick keyword searching to identify suitable ATT&CK IDs for further research. Sorted alphabetically and fomatted as keyword:technique_ids (comma seperated when multiple). See -> [resources/attack_keywords.idx](resources/attack_keywords.idx)

**ATT&CK Technique List**: Markdown table containing ATT&CK ID, name, keywords, description and platforms. Sorted by ID. Sub-technique names are prefixed with their parent ("Parent: Sub-technique"). Use when researching techniques, valdiating IDs, searching for up-to-date descriptions or filtering by platform. See -> [resources/attack_techniques.md](resources/attack_techniques.md)

**ATT&CK Version Changelog**: Every retired (revoked or deprecated) technique ID with its live replacement. Reference for v15->v20 changes including deprecated techniques, renamed platforms, the v18 detection model overhaul, and the v19 Defense Evasion split into Stealth and Defense Impairment. Use when analysing older reports or understanding structural changes. See -> [resources/attack_version_changelog.md](resources/attack_version_changelog.md)

## Best Practice

Use your judgment alongside these guidelines to generate high-quality ATT&CK analysis.

- Do not assume your knowledge is complete or up to date. Your memory of ATT&CK is probably older than v20: Defense Evasion is gone (now Stealth and Defense Impairment), T1562 Impair Defenses and its sub-techniques are revoked (now T1685/T1686/T1688-T1690), T1656 is now T1684.001
- Map only what the supplied text shows. Each technique needs a line, command, field or artefact in the input that demonstrates it. Do not add techniques because they usually accompany others
- Search broadly for keywords, you may need to iterate to find every technique the text shows
- Think about the specific procedure being performed and the attacker (or defender) intent before choosing the tactic, technique or sub-technique
- Some techniques belong to several tactics (for ex. T1078 Valid Accounts); others are similar but distinct by tactic (T1213.003 and T1593.003 are both Code Repositories)
- Map to the most specific sub-technique the text supports; use the parent when the text does not say which sub-technique
- **Validate every final ID** with `grep "^|ID|" resources/attack_techniques.md`. If it is not there, look it up in the changelog's Retired Technique IDs table and use the live ID, or drop it if deprecated

## By Source

### CTI Reports
- Read the whole report, including IOC tables, appendixes, screenshots and linked STIX files
- Break the report into granular procedures and map each one
- Report-supplied technique IDs and tactic names may be from an older ATT&CK version: translate them via the Retired Technique IDs table, never copy them blindly
- Ignore page furniture (navigation, image links, share buttons); it matches keywords by accident
- Finish with a second pass to validate findings and find missed techniques

### Detection Rules (Sigma, EDR, SIEM)
- Tags are the rule author's claim, not ground truth. Check each tag against the logsource and detection logic, and drop tags the logic cannot observe
- Older rules carry retired IDs (`attack.t1086`) and retired tactics (`attack.defense_evasion`): translate them
- Map what the matched process, command line, registry key or event shows. A rule matching only an image name supports less than one matching specific arguments
- Detection logic may cover several techniques; map all the logic supports

### Atomic Red Team Tests
- The technique the test is filed under (`attack_technique`) is a strong prior: include it unless the commands clearly do something else
- Add a technique only for what the executed commands themselves do (the interpreter that runs them, a service they create, a registry key they set)
- Test values (names, paths, accounts) are placeholders, not evidence

### ATT&CK Procedure Examples
- The line is already filed under a technique; include it
- Add other techniques only when the line names a distinct action (a tool run, a file copied, a service used)

## Commonly Missed Techniques

Use these as prompts to check the text, not as automatic additions. Add the technique only if the text shows it.

### Command-Line Indicators
`-windowstyle hidden`|`-w hidden` -> check T1564.003 Hidden Window
`-encodedcommand`|`-enc` -> check T1027.010 Command Obfuscation
`powershell.exe` or PowerShell cmdlets executed -> T1059.001 PowerShell
`cmd.exe /c` -> T1059.003 Windows Command Shell
`wmic`|`Win32_Process`|`Invoke-WmiMethod` -> T1047 Windows Management Instrumentation
`sc create`|new service -> T1543.003 Windows Service; `sc start`|PsExec -> T1569.002 Service Execution

### Network and Infrastructure
Tool or payload downloaded onto the victim -> T1105 Ingress Tool Transfer
Tools copied between victim hosts -> T1570 Lateral Tool Transfer
SSH tunnel|port forward -> T1572 Protocol Tunneling
DDNS|No-IP|FreeDNS -> T1568 Dynamic Resolution
Typosquat|lookalike domain registered -> T1583.001 Domains

### v19/v20 Renames (models often use the old ID)
Disable AV/EDR/security tools -> T1685 (not T1562.001)
Clear Windows event logs -> T1685.005 (not T1070.001)
Disable host firewall -> T1686 / T1686.003 (not T1562.004)
Impersonation in social engineering -> T1684.001 (not T1656)
Safe Mode boot to evade -> T1688 (not T1562.009)
