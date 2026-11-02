# case02

Source: one ATT&CK procedure example line. ATT&CK files it under technique(s): T1003.001.

<!-- MITRE ATT&CK procedure example (https://attack.mitre.org), © The MITRE Corporation, reproduced under the ATT&CK Terms of Use. -->

---

Olympic Destroyer (S0365) contains a module that tries to obtain credentials from LSASS, similar to Mimikatz (S0002). These credentials are used with PsExec (S0029) and Windows Management Instrumentation (T1047) to help the malware propagate itself across a network.[Talos Olympic Destroyer 2018]
