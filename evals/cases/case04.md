# case04

Source: a Sigma detection rule (YAML).

<!-- Written for this evaluation (synthetic, uses retired IDs on purpose). -->

---

title: Disable Windows Defender via PowerShell
status: experimental
description: Detects PowerShell disabling Defender real-time monitoring
tags:
    - attack.defense_evasion
    - attack.t1089
    - attack.execution
    - attack.t1086
logsource:
    product: windows
    category: process_creation
detection:
    selection:
        Image|endswith: '\\powershell.exe'
        CommandLine|contains: 'Set-MpPreference -DisableRealtimeMonitoring $true'
    condition: selection
level: high
