# ATT&CK Version Changes (v15→v20)

Quick reference for deprecated, renamed, and new technique IDs. Use when analysing older reports or validating mappings.

## Technique ID Changes

<!-- generated:technique-changes -->
### Revoked or Merged

| Old ID | Old Name | New ID | New Name | Version |
|---|---|---|---|---|
| T1070.001 | Clear Windows Event Logs | T1685.005 | Clear Windows Event Logs | v19 |
| T1070.002 | Clear Linux or Mac System Logs | T1685.006 | Clear Linux or Mac System Logs | v19 |
| T1562 | Impair Defenses | T1685 | Disable or Modify Tools | v19 |
| T1562.001 | Disable or Modify Tools | T1685 | Disable or Modify Tools | v19 |
| T1562.002 | Disable Windows Event Logging | T1685.001 | Disable or Modify Windows Event Log | v19 |
| T1562.003 | Impair Command History Logging | T1690 | Prevent Command History Logging | v19 |
| T1562.004 | Disable or Modify System Firewall | T1686 | Disable or Modify System Firewall | v19 |
| T1562.006 | Indicator Blocking | T1685 | Disable or Modify Tools | v19 |
| T1562.007 | Disable or Modify Cloud Firewall | T1686.001 | Cloud Firewall | v19 |
| T1562.008 | Disable or Modify Cloud Logs | T1685.002 | Disable or Modify Cloud Log | v19 |
| T1562.009 | Safe Mode Boot | T1688 | Safe Mode Boot | v19 |
| T1562.010 | Downgrade Attack | T1689 | Downgrade Attack | v19 |
| T1562.011 | Spoof Security Alerting | T1685.003 | Modify or Spoof Tool UI | v19 |
| T1562.012 | Disable or Modify Linux Audit System | T1685.004 | Disable or Modify Linux Audit System Log | v19 |
| T1562.013 | Disable or Modify Network Device Firewall | T1686.002 | Network Device Firewall | v19 |
| T1574.002 | DLL Side-Loading | T1574.001 | DLL | v17 |
| T1656 | Impersonation | T1684.001 | Impersonation | v19 |
| T1672 | Email Spoofing | T1684.002 | Email Spoofing | v19 |

### New

| ID | Name | Version |
|---|---|---|
| T1027.013 | Obfuscated Files or Information: Encrypted/Encoded File | v15 |
| T1027.014 | Obfuscated Files or Information: Polymorphic Code | v16 |
| T1027.015 | Obfuscated Files or Information: Compression | v17 |
| T1027.016 | Obfuscated Files or Information: Junk Code Insertion | v17 |
| T1027.017 | Obfuscated Files or Information: SVG Smuggling | v17 |
| T1027.018 | Obfuscated Files or Information: Invisible Unicode | v19 |
| T1036.010 | Masquerading: Masquerade Account Name | v16 |
| T1036.011 | Masquerading: Overwrite Process Arguments | v17 |
| T1036.012 | Masquerading: Browser Fingerprint | v18 |
| T1059.010 | Command and Scripting Interpreter: AutoHotKey & AutoIT | v15 |
| T1059.011 | Command and Scripting Interpreter: Lua | v16 |
| T1059.012 | Command and Scripting Interpreter: Hypervisor CLI | v17 |
| T1059.013 | Command and Scripting Interpreter: Container CLI/API | v18 |
| T1070.010 | Indicator Removal: Relocate Malware | v16 |
| T1071.005 | Application Layer Protocol: Publish/Subscribe Protocols | v16 |
| T1098.007 | Account Manipulation: Additional Local or Domain Groups | v16 |
| T1127.002 | Trusted Developer Utilities Proxy Execution: ClickOnce | v16 |
| T1127.003 | Trusted Developer Utilities Proxy Execution: JamPlus | v17 |
| T1176.001 | Software Extensions: Browser Extensions | v17 |
| T1176.002 | Software Extensions: IDE Extensions | v17 |
| T1204.004 | User Execution: Malicious Copy and Paste | v17 |
| T1204.005 | User Execution: Malicious Library | v18 |
| T1213.004 | Data from Information Repositories: Customer Relationship Management Software | v16 |
| T1213.005 | Data from Information Repositories: Messaging Applications | v16 |
| T1213.006 | Data from Information Repositories: Databases | v18 |
| T1216.002 | System Script Proxy Execution: SyncAppvPublishingServer | v15 |
| T1218.015 | System Binary Proxy Execution: Electron Applications | v15 |
| T1219.001 | Remote Access Tools: IDE Tunneling | v17 |
| T1219.002 | Remote Access Tools: Remote Desktop Software | v17 |
| T1219.003 | Remote Access Tools: Remote Access Hardware | v17 |
| T1480.002 | Execution Guardrails: Mutual Exclusion | v16 |
| T1485.001 | Data Destruction: Lifecycle-Triggered Deletion | v16 |
| T1496.001 | Resource Hijacking: Compute Hijacking | v16 |
| T1496.002 | Resource Hijacking: Bandwidth Hijacking | v16 |
| T1496.003 | Resource Hijacking: SMS Pumping | v16 |
| T1496.004 | Resource Hijacking: Cloud Service Hijacking | v16 |
| T1505.006 | Server Software Component: vSphere Installation Bundles | v17 |
| T1518.002 | Software Discovery: Backup Software Discovery | v18 |
| T1543.005 | Create or Modify System Process: Container Service | v15 |
| T1546.017 | Event Triggered Execution: Udev Rules | v16 |
| T1546.018 | Event Triggered Execution: Python Startup Hooks | v18 |
| T1548.006 | Abuse Elevation Control Mechanism: TCC Manipulation | v15 |
| T1556.009 | Modify Authentication Process: Conditional Access Policies | v15 |
| T1557.004 | Adversary-in-the-Middle: Evil Twin | v16 |
| T1558.005 | Steal or Forge Kerberos Tickets: Ccache Files | v16 |
| T1564.012 | Hide Artifacts: File/Path Exclusions | v15 |
| T1564.013 | Hide Artifacts: Bind Mounts | v17 |
| T1564.014 | Hide Artifacts: Extended Attributes | v17 |
| T1569.003 | System Services: Systemctl | v17 |
| T1574.014 | Hijack Execution Flow: AppDomainManager | v15 |
| T1584.008 | Compromise Infrastructure: Network Devices | v15 |
| T1588.007 | Obtain Capabilities: Artificial Intelligence | v15 |
| T1608.007 | Stage Capabilities: AI Result Poisoning | v20 |
| T1665 | Hide Infrastructure | v15 |
| T1666 | Modify Cloud Resource Hierarchy | v16 |
| T1667 | Email Bombing | v17 |
| T1668 | Exclusive Control | v17 |
| T1669 | Wi-Fi Networks | v17 |
| T1671 | Cloud Application Integration | v17 |
| T1673 | Virtual Machine Discovery | v17 |
| T1674 | Input Injection | v17 |
| T1675 | ESXi Administration Command | v17 |
| T1677 | Poisoned Pipeline Execution | v18 |
| T1678 | Delay Execution | v18 |
| T1679 | Selective Exclusion | v18 |
| T1680 | Local Storage Discovery | v18 |
| T1681 | Search Threat Vendor Data | v18 |
| T1682 | Query Public AI Services | v19 |
| T1683 | Generate Content | v19 |
| T1683.001 | Generate Content: Written Content | v19 |
| T1683.002 | Generate Content: Audio-Visual Content | v19 |
| T1684 | Social Engineering | v19 |
| T1684.001 | Social Engineering: Impersonation | v19 |
| T1684.002 | Social Engineering: Email Spoofing | v19 |
| T1685 | Disable or Modify Tools | v19 |
| T1685.001 | Disable or Modify Tools: Disable or Modify Windows Event Log | v19 |
| T1685.002 | Disable or Modify Tools: Disable or Modify Cloud Log | v19 |
| T1685.003 | Disable or Modify Tools: Modify or Spoof Tool UI | v19 |
| T1685.004 | Disable or Modify Tools: Disable or Modify Linux Audit System Log | v19 |
| T1685.005 | Disable or Modify Tools: Clear Windows Event Logs | v19 |
| T1685.006 | Disable or Modify Tools: Clear Linux or Mac System Logs | v19 |
| T1685.007 | Disable or Modify Tools: Impair Autonomous Defenses | v20 |
| T1686 | Disable or Modify System Firewall | v19 |
| T1686.001 | Disable or Modify System Firewall: Cloud Firewall | v19 |
| T1686.002 | Disable or Modify System Firewall: Network Device Firewall | v19 |
| T1686.003 | Disable or Modify System Firewall: Windows Host Firewall | v19 |
| T1687 | Exploitation for Defense Impairment | v19 |
| T1688 | Safe Mode Boot | v19 |
| T1689 | Downgrade Attack | v19 |
| T1690 | Prevent Command History Logging | v19 |
| T1696 | Anti-Automation Evasion | v20 |
| T1696.001 | Anti-Automation Evasion: Automate CAPTCHA Completion | v20 |
| T1696.002 | Anti-Automation Evasion: Avoid CAPTCHA | v20 |
| T1697 | Steal Application Specific Passwords | v20 |
| T1698 | Indirect Prompt Injection | v20 |
| T1699 | Direct Prompt Injection | v20 |
| T1700 | AI-Enabled Exfiltration | v20 |
<!-- /generated:technique-changes -->

## Retired Technique IDs

Every revoked or deprecated Enterprise technique ID, from any release. A revoked ID maps to its live replacement; a deprecated ID has none. Check any ID that is not in attack_techniques.md here: older reports and detection rules still cite them.

<!-- generated:retired -->
|Old ID|Old Name|Status|Live ID|Live Name|
|---|---|---|---|---|
|T1002|Data Compressed|revoked|T1560|Archive Collected Data|
|T1004|Winlogon Helper DLL|revoked|T1547.004|Boot or Logon Autostart Execution: Winlogon Helper DLL|
|T1009|Binary Padding|revoked|T1027.001|Obfuscated Files or Information: Binary Padding|
|T1013|Port Monitors|revoked|T1547.010|Boot or Logon Autostart Execution: Port Monitors|
|T1015|Accessibility Features|revoked|T1546.008|Event Triggered Execution: Accessibility Features|
|T1017|Application Deployment Software|revoked|T1072|Software Deployment Tools|
|T1019|System Firmware|revoked|T1542.001|Pre-OS Boot: System Firmware|
|T1022|Data Encrypted|revoked|T1560|Archive Collected Data|
|T1023|Shortcut Modification|revoked|T1547.009|Boot or Logon Autostart Execution: Shortcut Modification|
|T1024|Custom Cryptographic Protocol|revoked|T1573|Encrypted Channel|
|T1026|Multiband Communication|deprecated|—|no replacement: map the behaviour itself|
|T1028|Windows Remote Management|revoked|T1021.006|Remote Services: Windows Remote Management|
|T1031|Modify Existing Service|revoked|T1543.003|Create or Modify System Process: Windows Service|
|T1032|Standard Cryptographic Protocol|revoked|T1573|Encrypted Channel|
|T1034|Path Interception|deprecated|—|no replacement: map the behaviour itself|
|T1035|Service Execution|revoked|T1569.002|System Services: Service Execution|
|T1038|DLL Search Order Hijacking|revoked|T1574.001|Hijack Execution Flow: DLL|
|T1042|Change Default File Association|revoked|T1546.001|Event Triggered Execution: Change Default File Association|
|T1043|Commonly Used Port|deprecated|—|no replacement: map the behaviour itself|
|T1044|File System Permissions Weakness|revoked|T1574.010|Hijack Execution Flow: Services File Permissions Weakness|
|T1045|Software Packing|revoked|T1027.002|Obfuscated Files or Information: Software Packing|
|T1050|New Service|revoked|T1543.003|Create or Modify System Process: Windows Service|
|T1051|Shared Webroot|deprecated|—|no replacement: map the behaviour itself|
|T1053.001|At (Linux)|revoked|T1053.002|Scheduled Task/Job: At|
|T1053.004|Launchd|deprecated|—|no replacement: map the behaviour itself|
|T1054|Indicator Blocking|revoked|T1685|Disable or Modify Tools|
|T1058|Service Registry Permissions Weakness|revoked|T1574.011|Hijack Execution Flow: Services Registry Permissions Weakness|
|T1060|Registry Run Keys / Startup Folder|revoked|T1547.001|Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder|
|T1061|Graphical User Interface|deprecated|—|no replacement: map the behaviour itself|
|T1062|Hypervisor|deprecated|—|no replacement: map the behaviour itself|
|T1063|Security Software Discovery|revoked|T1518.001|Software Discovery: Security Software Discovery|
|T1064|Scripting|deprecated|—|no replacement: map the behaviour itself|
|T1065|Uncommonly Used Port|revoked|T1571|Non-Standard Port|
|T1066|Indicator Removal from Tools|revoked|T1027.005|Obfuscated Files or Information: Indicator Removal from Tools|
|T1067|Bootkit|revoked|T1542.003|Pre-OS Boot: Bootkit|
|T1070.001|Clear Windows Event Logs|revoked|T1685.005|Disable or Modify Tools: Clear Windows Event Logs|
|T1070.002|Clear Linux or Mac System Logs|revoked|T1685.006|Disable or Modify Tools: Clear Linux or Mac System Logs|
|T1073|DLL Side-Loading|revoked|T1574.001|Hijack Execution Flow: DLL|
|T1075|Pass the Hash|revoked|T1550.002|Use Alternate Authentication Material: Pass the Hash|
|T1076|Remote Desktop Protocol|revoked|T1021.001|Remote Services: Remote Desktop Protocol|
|T1077|Windows Admin Shares|revoked|T1021.002|Remote Services: SMB/Windows Admin Shares|
|T1079|Multilayer Encryption|revoked|T1573|Encrypted Channel|
|T1081|Credentials in Files|revoked|T1552.001|Unsecured Credentials: Credentials In Files|
|T1084|Windows Management Instrumentation Event Subscription|revoked|T1546.003|Event Triggered Execution: Windows Management Instrumentation Event Subscription|
|T1085|Rundll32|revoked|T1218.011|System Binary Proxy Execution: Rundll32|
|T1086|PowerShell|revoked|T1059.001|Command and Scripting Interpreter: PowerShell|
|T1088|Bypass User Account Control|revoked|T1548.002|Abuse Elevation Control Mechanism: Bypass User Account Control|
|T1089|Disabling Security Tools|revoked|T1685|Disable or Modify Tools|
|T1093|Process Hollowing|revoked|T1055.012|Process Injection: Process Hollowing|
|T1094|Custom Command and Control Protocol|revoked|T1095|Non-Application Layer Protocol|
|T1096|NTFS File Attributes|revoked|T1564.004|Hide Artifacts: NTFS File Attributes|
|T1097|Pass the Ticket|revoked|T1550.003|Use Alternate Authentication Material: Pass the Ticket|
|T1099|Timestomp|revoked|T1070.006|Indicator Removal: Timestomp|
|T1100|Web Shell|revoked|T1505.003|Server Software Component: Web Shell|
|T1101|Security Support Provider|revoked|T1547.005|Boot or Logon Autostart Execution: Security Support Provider|
|T1103|AppInit DLLs|revoked|T1546.010|Event Triggered Execution: AppInit DLLs|
|T1107|File Deletion|revoked|T1070.004|Indicator Removal: File Deletion|
|T1108|Redundant Access|deprecated|—|no replacement: map the behaviour itself|
|T1109|Component Firmware|revoked|T1542.002|Pre-OS Boot: Component Firmware|
|T1116|Code Signing|revoked|T1553.002|Subvert Trust Controls: Code Signing|
|T1117|Regsvr32|revoked|T1218.010|System Binary Proxy Execution: Regsvr32|
|T1118|InstallUtil|revoked|T1218.004|System Binary Proxy Execution: InstallUtil|
|T1121|Regsvcs/Regasm|revoked|T1218.009|System Binary Proxy Execution: Regsvcs/Regasm|
|T1122|Component Object Model Hijacking|revoked|T1546.015|Event Triggered Execution: Component Object Model Hijacking|
|T1126|Network Share Connection Removal|revoked|T1070.005|Indicator Removal: Network Share Connection Removal|
|T1128|Netsh Helper DLL|revoked|T1546.007|Event Triggered Execution: Netsh Helper DLL|
|T1130|Install Root Certificate|revoked|T1553.004|Subvert Trust Controls: Install Root Certificate|
|T1131|Authentication Package|revoked|T1547.002|Boot or Logon Autostart Execution: Authentication Package|
|T1138|Application Shimming|revoked|T1546.011|Event Triggered Execution: Application Shimming|
|T1139|Bash History|revoked|T1552.003|Unsecured Credentials: Shell History|
|T1141|Input Prompt|revoked|T1056.002|Input Capture: GUI Input Capture|
|T1142|Keychain|revoked|T1555.001|Credentials from Password Stores: Keychain|
|T1143|Hidden Window|revoked|T1564.003|Hide Artifacts: Hidden Window|
|T1144|Gatekeeper Bypass|revoked|T1553.001|Subvert Trust Controls: Gatekeeper Bypass|
|T1145|Private Keys|revoked|T1552.004|Unsecured Credentials: Private Keys|
|T1146|Clear Command History|revoked|T1070.003|Indicator Removal: Clear Command History|
|T1147|Hidden Users|revoked|T1564.002|Hide Artifacts: Hidden Users|
|T1148|HISTCONTROL|revoked|T1690|Prevent Command History Logging|
|T1149|LC_MAIN Hijacking|deprecated|—|no replacement: map the behaviour itself|
|T1150|Plist Modification|revoked|T1647|Plist File Modification|
|T1151|Space after Filename|revoked|T1036.006|Masquerading: Space after Filename|
|T1152|Launchctl|revoked|T1569.001|System Services: Launchctl|
|T1153|Source|deprecated|—|no replacement: map the behaviour itself|
|T1154|Trap|revoked|T1546.005|Event Triggered Execution: Trap|
|T1155|AppleScript|revoked|T1059.002|Command and Scripting Interpreter: AppleScript|
|T1156|Malicious Shell Modification|revoked|T1546.004|Event Triggered Execution: Unix Shell Configuration Modification|
|T1157|Dylib Hijacking|revoked|T1574.004|Hijack Execution Flow: Dylib Hijacking|
|T1158|Hidden Files and Directories|revoked|T1564.001|Hide Artifacts: Hidden Files and Directories|
|T1159|Launch Agent|revoked|T1543.001|Create or Modify System Process: Launch Agent|
|T1160|Launch Daemon|revoked|T1543.004|Create or Modify System Process: Launch Daemon|
|T1161|LC_LOAD_DYLIB Addition|revoked|T1546.006|Event Triggered Execution: LC_LOAD_DYLIB Addition|
|T1162|Login Item|revoked|T1647|Plist File Modification|
|T1163|Rc.common|revoked|T1037.004|Boot or Logon Initialization Scripts: RC Scripts|
|T1164|Re-opened Applications|revoked|T1547.007|Boot or Logon Autostart Execution: Re-opened Applications|
|T1165|Startup Items|revoked|T1037.005|Boot or Logon Initialization Scripts: Startup Items|
|T1166|Setuid and Setgid|revoked|T1548.001|Abuse Elevation Control Mechanism: Setuid and Setgid|
|T1167|Securityd Memory|revoked|T1555.002|Credentials from Password Stores: Securityd Memory|
|T1168|Local Job Scheduling|revoked|T1053|Scheduled Task/Job|
|T1169|Sudo|revoked|T1548.003|Abuse Elevation Control Mechanism: Sudo and Sudo Caching|
|T1170|Mshta|revoked|T1218.005|System Binary Proxy Execution: Mshta|
|T1171|LLMNR/NBT-NS Poisoning and Relay|revoked|T1557.001|Adversary-in-the-Middle: Name Resolution Poisoning and SMB Relay|
|T1172|Domain Fronting|revoked|T1090.004|Proxy: Domain Fronting|
|T1173|Dynamic Data Exchange|revoked|T1559.002|Inter-Process Communication: Dynamic Data Exchange|
|T1174|Password Filter DLL|revoked|T1556.002|Modify Authentication Process: Password Filter DLL|
|T1175|Component Object Model and Distributed COM|deprecated|—|no replacement: map the behaviour itself|
|T1177|LSASS Driver|revoked|T1547.008|Boot or Logon Autostart Execution: LSASS Driver|
|T1178|SID-History Injection|revoked|T1134.005|Access Token Manipulation: SID-History Injection|
|T1179|Hooking|revoked|T1056.004|Input Capture: Credential API Hooking|
|T1180|Screensaver|revoked|T1546.002|Event Triggered Execution: Screensaver|
|T1181|Extra Window Memory Injection|revoked|T1055.011|Process Injection: Extra Window Memory Injection|
|T1182|AppCert DLLs|revoked|T1546.009|Event Triggered Execution: AppCert DLLs|
|T1183|Image File Execution Options Injection|revoked|T1546.012|Event Triggered Execution: Image File Execution Options Injection|
|T1184|SSH Hijacking|revoked|T1563.001|Remote Service Session Hijacking: SSH Hijacking|
|T1186|Process Doppelgänging|revoked|T1055.013|Process Injection: Process Doppelgänging|
|T1188|Multi-hop Proxy|revoked|T1090.003|Proxy: Multi-hop Proxy|
|T1191|CMSTP|revoked|T1218.003|System Binary Proxy Execution: CMSTP|
|T1192|Spearphishing Link|revoked|T1566.002|Phishing: Spearphishing Link|
|T1193|Spearphishing Attachment|revoked|T1566.001|Phishing: Spearphishing Attachment|
|T1194|Spearphishing via Service|revoked|T1566.003|Phishing: Spearphishing via Service|
|T1196|Control Panel Items|revoked|T1218.002|System Binary Proxy Execution: Control Panel|
|T1198|SIP and Trust Provider Hijacking|revoked|T1553.003|Subvert Trust Controls: SIP and Trust Provider Hijacking|
|T1206|Sudo Caching|revoked|T1548.003|Abuse Elevation Control Mechanism: Sudo and Sudo Caching|
|T1208|Kerberoasting|revoked|T1558.003|Steal or Forge Kerberos Tickets: Kerberoasting|
|T1209|Time Providers|revoked|T1547.003|Boot or Logon Autostart Execution: Time Providers|
|T1214|Credentials in Registry|revoked|T1552.002|Unsecured Credentials: Credentials in Registry|
|T1215|Kernel Modules and Extensions|revoked|T1547.006|Boot or Logon Autostart Execution: Kernel Modules and Extensions|
|T1223|Compiled HTML File|revoked|T1218.001|System Binary Proxy Execution: Compiled HTML File|
|T1483|Domain Generation Algorithms|revoked|T1568.002|Dynamic Resolution: Domain Generation Algorithms|
|T1487|Disk Structure Wipe|revoked|T1561.002|Disk Wipe: Disk Structure Wipe|
|T1488|Disk Content Wipe|revoked|T1561.001|Disk Wipe: Disk Content Wipe|
|T1492|Stored Data Manipulation|revoked|T1565.001|Data Manipulation: Stored Data Manipulation|
|T1493|Transmitted Data Manipulation|revoked|T1565.002|Data Manipulation: Transmitted Data Manipulation|
|T1494|Runtime Data Manipulation|revoked|T1565.003|Data Manipulation: Runtime Data Manipulation|
|T1500|Compile After Delivery|revoked|T1027.004|Obfuscated Files or Information: Compile After Delivery|
|T1501|Systemd Service|revoked|T1543.002|Create or Modify System Process: Systemd Service|
|T1502|Parent PID Spoofing|revoked|T1134.004|Access Token Manipulation: Parent PID Spoofing|
|T1503|Credentials from Web Browsers|revoked|T1555.003|Credentials from Password Stores: Credentials from Web Browsers|
|T1504|PowerShell Profile|revoked|T1546.013|Event Triggered Execution: PowerShell Profile|
|T1506|Web Session Cookie|revoked|T1550.004|Use Alternate Authentication Material: Web Session Cookie|
|T1514|Elevated Execution with Prompt|revoked|T1548.004|Abuse Elevation Control Mechanism: Elevated Execution with Prompt|
|T1519|Emond|revoked|T1546.014|Event Triggered Execution: Emond|
|T1522|Cloud Instance Metadata API|revoked|T1552.005|Unsecured Credentials: Cloud Instance Metadata API|
|T1527|Application Access Token|revoked|T1550.001|Use Alternate Authentication Material: Application Access Token|
|T1536|Revert Cloud Instance|revoked|T1578.004|Modify Cloud Compute Infrastructure: Revert Cloud Instance|
|T1547.011|Plist Modification|revoked|T1647|Plist File Modification|
|T1562|Impair Defenses|revoked|T1685|Disable or Modify Tools|
|T1562.001|Disable or Modify Tools|revoked|T1685|Disable or Modify Tools|
|T1562.002|Disable Windows Event Logging|revoked|T1685.001|Disable or Modify Tools: Disable or Modify Windows Event Log|
|T1562.003|Impair Command History Logging|revoked|T1690|Prevent Command History Logging|
|T1562.004|Disable or Modify System Firewall|revoked|T1686|Disable or Modify System Firewall|
|T1562.006|Indicator Blocking|revoked|T1685|Disable or Modify Tools|
|T1562.007|Disable or Modify Cloud Firewall|revoked|T1686.001|Disable or Modify System Firewall: Cloud Firewall|
|T1562.008|Disable or Modify Cloud Logs|revoked|T1685.002|Disable or Modify Tools: Disable or Modify Cloud Log|
|T1562.009|Safe Mode Boot|revoked|T1688|Safe Mode Boot|
|T1562.010|Downgrade Attack|revoked|T1689|Downgrade Attack|
|T1562.011|Spoof Security Alerting|revoked|T1685.003|Disable or Modify Tools: Modify or Spoof Tool UI|
|T1562.012|Disable or Modify Linux Audit System|revoked|T1685.004|Disable or Modify Tools: Disable or Modify Linux Audit System Log|
|T1562.013|Disable or Modify Network Device Firewall|revoked|T1686.002|Disable or Modify System Firewall: Network Device Firewall|
|T1574.002|DLL Side-Loading|revoked|T1574.001|Hijack Execution Flow: DLL|
|T1656|Impersonation|revoked|T1684.001|Social Engineering: Impersonation|
|T1672|Email Spoofing|revoked|T1684.002|Social Engineering: Email Spoofing|
<!-- /generated:retired -->

## Platform Changes

| Old Platform | New Platform | Version |
|--------------|--------------|---------|
| Azure AD | Identity Provider | v16 |
| Office 365 | Office Suite | v16 |
| Google Workspace | Office Suite | v16 |
| Network | Network Devices | v17 |
| — | ESXi (new) | v17 |

## Defense Evasion Split (v19)

**CRITICAL:** v19 retired the Defense Evasion tactic. Pre-v19 mappings tagged `defense-evasion` / `DE` will not load cleanly against v19 data.

| Deprecated | Replaced By |
|------------|-------------|
| Defense Evasion (TA0005) | **Stealth (TA0005, reused ID)** + **Defense Impairment (TA0112, new)** |

**TA0005 ID reuse gotcha:** TA0005 still exists, but now means *Stealth*, not *Defense Evasion*. Anything keying off the numeric ID (rules, dashboards, ATT&CK Navigator layers) will silently mis-label.

**Where old DE techniques landed:**
- Most → **Stealth (ST)** — concealment, blending in (obfuscation, masquerading, indicator removal)
- Several → **Defense Impairment (DIM)** — disabling/degrading defences (firewall mods, log clearing, tool disabling)
- A few → **Lateral Movement, Privilege Escalation, Execution** — reassigned where they fit better

Some techniques are now mapped to **both** ST and DIM (intent isn't always clean). Compressed rows reflect this: `ST,DIM`.

**T1562 crosswalk:** T1562 (Impair Defenses) parent and sub-techniques were revoked. Old T1562.* IDs in legacy detections will break. Map each to its new ID using the Revoked or Merged table above.

**Authoritative crosswalk:** https://attack.mitre.org/resources/updates/updates-april-2026/ — use this when remapping pre-v19 detections.

## Detection Model Change (v18)

**CRITICAL:** v18 fundamentally changed how detections are documented.

| Deprecated | Replaced By |
|------------|-------------|
| Data Sources | Detection Strategies |
| Detection notes (free text) | Analytics (1,739 structured rules) |

**New mapping chain:** Technique → Detection Strategy → Analytics → Data Components → Log Sources

**When analysing pre-v18 content:** Data Source references map to Detection Strategies. Analytics format changed from CAR pseudocode (pre-v15) → Splunk-style queries (v15-v17) → structured Analytics objects (v18).

## New Coverage Areas (v17-v20)

**v20:** AI and LLM abuse — prompt injection (T1698 Indirect, T1699 Direct), AI-enabled exfiltration via agent tool connections (T1700), AI result poisoning (T1608.007), impairing LLM-assisted defences (T1685.007); CAPTCHA evasion (T1696); application specific password theft (T1697); PowerShell (T1059.001) now also Linux/macOS, SSH (T1021.004) now also Windows

**v19:** AI services abuse (T1682 Query Public AI Services, T1683 Generate Content), unified Social Engineering parent (T1684), Safe Mode Boot evasion (T1688), ICS sub-techniques (first-class), Mobile Detection Strategies (initial)

**v18:** CI/CD pipelines, Kubernetes, cloud databases, ransomware prep behaviours, Signal/WhatsApp linked-devices abuse, supply chain attacks

**v17:** ESXi hypervisor (34 adapted + 4 new techniques), ClickFix-style attacks, email-based social engineering

## New Groups

<!-- generated:groups -->
**v20:** G1058 The Gentlemen, G1059 NIMBUS MANTICORE

**v19.2:** G1056 TeamPCP, G1057 ShinyHunters

**v19:** G1054 MirrorFace, G1055 VOID MANTICORE

**v18:** G1048 UNC3886, G1049 AppleJeus, G1050 Water Galura, G1051 Medusa Group, G1052 Contagious Interview, G1053 Storm-0501

**v17:** G1041 Sea Turtle, G1042 RedEcho, G1043 BlackByte, G1044 APT42, G1045 Salt Typhoon, G1046 Storm-1811, G1047 Velvet Ant

**v16:** G1030 Agrius, G1031 Saint Bear, G1032 INC Ransom, G1033 Star Blizzard, G1034 Daggerfly, G1035 Winter Vivern, G1036 Moonstone Sleet, G1037 TA577, G1038 TA578, G1039 RedCurl, G1040 Play

**v15:** G1020 Mustard Tempest, G1021 Cinnamon Tempest, G1022 ToddyCat, G1023 APT5, G1024 Akira, G1026 Malteiro, G1028 APT-C-23
<!-- /generated:groups -->

## Version Timeline

| Ver | Date | Key Change |
|-----|------|------------|
| v20 | Oct 2026 | Current - AI/LLM techniques (prompt injection, AI-enabled exfiltration, AI result poisoning); no revocations |
| v19.2 | Aug 2026 | No technique changes; new groups and software only |
| v19.1 | May 2026 | v19 minor fixes |
| v19 | Apr 2026 | Defense Evasion split → Stealth + Defense Impairment; AI/social-engineering techniques; ICS sub-techniques |
| v18.1 | Nov 2025 | v18 minor fixes |
| v18 | Oct 2025 | Detection model overhaul (Data Sources deprecated) |
| v17 | Apr 2025 | ESXi platform, DLL technique merge |
| v16 | Oct 2024 | Cloud platform refactor, ICS sub-techniques |
| v15 | Apr 2024 | Analytics → Splunk-style, ICS cross-mapping |

<!-- generated:stats -->
## Stats (v20)

Enterprise: 15 tactics, 227 techniques, 479 sub-techniques | Groups: 178 | Software: 842 | Campaigns: 57
<!-- /generated:stats -->
