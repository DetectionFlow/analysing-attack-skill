# ATT&CK Version Changes (v15→v19.1)

Quick reference for deprecated, renamed, and new technique IDs. Use when analysing older reports or validating mappings.

## Technique ID Changes

| Old ID | Status | New ID | Name | Version |
|--------|--------|--------|------|---------|
| T1574.002 | MERGED | T1574.001 | DLL Side-Loading → DLL | v17 |
| T1453 | UN-DEPRECATED | T1453 | Abuse Accessibility Features (Mobile) | v18 |
| T1204.003 | NEW | — | User Execution: Malicious Copy and Paste | v17 |
| T1585.004 | NEW | — | Email Bombing | v17 |
| T1656.002 | NEW | — | Email Spoofing | v17 |
| T1656 | REVOKED | T1684.001 | Impersonation → sub of new T1684 Social Engineering | v19 |
| T1562 (+subs) | REVOKED | T1685 (+subs) | Impair Defenses → Disable or Modify Tools | v19 |
| T1682 | NEW | — | Query Public AI Services | v19 |
| T1683 | NEW | — | Generate Content | v19 |
| T1684 | NEW | — | Social Engineering (parent, 2 subs) | v19 |
| T1685 | NEW | — | Disable or Modify Tools (parent, 6 subs) | v19 |
| T1686 | NEW | — | Disable or Modify System Firewall (parent, 3 subs) | v19 |
| T1688 | NEW | — | Safe Mode Boot | v19 |

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

**T1562 → T1685 crosswalk:** T1562 (Impair Defenses) parent and sub-techniques were revoked. Old T1562.* IDs in legacy detections will break. Map to new IDs under T1685 (Disable or Modify Tools) or T1686 (Disable or Modify System Firewall).

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

**v19 Notable Groups:** MirrorFace, VOID MANTICORE (Enterprise) + 5 new Mobile groups

**v17 Notable Groups:** G1045 Salt Typhoon (PRC), G1044 APT42 (Iran), G1041 Sea Turtle (Türkiye), G1043 BlackByte 2.0

## Version Timeline

| Ver | Date | Key Change |
|-----|------|------------|
| v19.1 | May 2026 | Current - minor fixes on v19 |
| v19 | Apr 2026 | Defense Evasion split → Stealth + Defense Impairment; AI/social-engineering techniques; ICS sub-techniques |
| v18.1 | Oct 2025 | v18 minor fixes |
| v18 | Oct 2025 | Detection model overhaul (Data Sources deprecated) |
| v17 | Apr 2025 | ESXi platform, DLL technique merge |
| v16 | Oct 2024 | Cloud platform refactor, ICS sub-techniques |
| v15 | Apr 2024 | Analytics → Splunk-style, ICS cross-mapping |

## Stats (v19.1)

Enterprise: 15 tactics, 222 techniques, 475 sub-techniques | Groups: 172+ | Software: 900+ | Campaigns: 50+