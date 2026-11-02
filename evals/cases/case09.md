# case09

Source: an Atomic Red Team test (YAML).

<!-- Atomic Red Team test (https://github.com/redcanaryco/atomic-red-team), MIT License, Red Canary. -->

---

attack_technique: T1053.005
display_name: 'Scheduled Task/Job: Scheduled Task'
name: Scheduled task Remote
auto_generated_guid: 2e5eac3e-327b-4a88-a0c0-c4057039a8dd
description: |
  Create a task on a remote system.
  Upon successful execution, cmd.exe will create a scheduled task to spawn cmd.exe at 20:10 on a remote endpoint.
supported_platforms:
- windows
input_arguments:
  task_command:
    description: What you want to execute
    type: string
    default: C:\windows\system32\cmd.exe
  time:
    description: What time 24 Hour
    type: string
    default: '20:10'
  target:
    description: Target
    type: string
    default: localhost
  user_name:
    description: 'Username to authenticate with, format: DOMAIN\User'
    type: string
    default: DOMAIN\user
  password:
    description: Password to authenticate with
    type: string
    default: At0micStrong
executor:
  name: command_prompt
  elevation_required: true
  command: |
    SCHTASKS /Create /S localhost /RU DOMAIN\user /RP At0micStrong /TN "Atomic task" /TR "C:\windows\system32\cmd.exe" /SC daily /ST 20:10
  cleanup_command: |
    SCHTASKS /Delete /S localhost /U DOMAIN\user /P At0micStrong /TN "Atomic task" /F >nul 2>&1

