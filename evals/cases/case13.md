# case13

Source: one ATT&CK procedure example line. ATT&CK files it under technique(s): T1053.005.

<!-- MITRE ATT&CK procedure example (https://attack.mitre.org), © The MITRE Corporation, reproduced under the ATT&CK Terms of Use. -->

---

Kimsuky (G0094) has downloaded additional malware with scheduled tasks.[KISA Operation Muzabi][NaumaanProofpoint_GlobalClickFix_April2025] Kimsuky (G0094) has established persistence by creating a scheduled task named “ChromeUpdateTaskMachine” through the PowerShell cmdlet `Register-ScheduleTask` which was set to execute another PowerShell script once, then five minutes after its creation and periodically repeat every 30 minutes.[Securonix Kimsuky February 2025] Kimsuky (G0094) has also set scheduled tasks that run periodically using the PT1M repetition pattern leveraging naming conventions of Anti-Virus software to include "AhnlabUpdate".[Gen Digital Kimsuky HTTPTroy October 2025]
