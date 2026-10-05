# ATT&CK Version Changes (v15→v19.2)

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
| T1686 | Disable or Modify System Firewall | v19 |
| T1686.001 | Disable or Modify System Firewall: Cloud Firewall | v19 |
| T1686.002 | Disable or Modify System Firewall: Network Device Firewall | v19 |
| T1686.003 | Disable or Modify System Firewall: Windows Host Firewall | v19 |
| T1687 | Exploitation for Defense Impairment | v19 |
| T1688 | Safe Mode Boot | v19 |
| T1689 | Downgrade Attack | v19 |
| T1690 | Prevent Command History Logging | v19 |
<!-- /generated:technique-changes -->

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

## New Coverage Areas (v17-v19)

**v19:** AI services abuse (T1682 Query Public AI Services, T1683 Generate Content), unified Social Engineering parent (T1684), Safe Mode Boot evasion (T1688), ICS sub-techniques (first-class), Mobile Detection Strategies (initial)

**v18:** CI/CD pipelines, Kubernetes, cloud databases, ransomware prep behaviours, Signal/WhatsApp linked-devices abuse, supply chain attacks

**v17:** ESXi hypervisor (34 adapted + 4 new techniques), ClickFix-style attacks, email-based social engineering

## New Groups

<!-- generated:groups -->
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
| v19.2 | Aug 2026 | Current - no technique changes; new groups and software only |
| v19.1 | May 2026 | v19 minor fixes |
| v19 | Apr 2026 | Defense Evasion split → Stealth + Defense Impairment; AI/social-engineering techniques; ICS sub-techniques |
| v18.1 | Nov 2025 | v18 minor fixes |
| v18 | Oct 2025 | Detection model overhaul (Data Sources deprecated) |
| v17 | Apr 2025 | ESXi platform, DLL technique merge |
| v16 | Oct 2024 | Cloud platform refactor, ICS sub-techniques |
| v15 | Apr 2024 | Analytics → Splunk-style, ICS cross-mapping |

<!-- generated:stats -->
## Stats (v19.2)

Enterprise: 15 tactics, 222 techniques, 475 sub-techniques | Groups: 176 | Software: 825 | Campaigns: 56
<!-- /generated:stats -->
