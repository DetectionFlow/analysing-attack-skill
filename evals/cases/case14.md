# case14

Source: a CTI report (markdown).

<!-- Written for this evaluation (synthetic, uses retired IDs on purpose). -->

---

## Technical analysis (2019)

The intrusion began with a spearphishing attachment (T1193): a Word document whose macro ran PowerShell (T1086) to fetch a second stage. The loader copied itself to %APPDATA% and added a Run key under HKCU\Software\Microsoft\Windows\CurrentVersion\Run (T1060) for persistence. It then cleared the Security and System event logs with wevtutil cl (T1070.001) and disabled Windows Defender with Set-MpPreference (T1562.001). Its C2 beaconed over TCP 443 using a commonly used port (T1043), and the actors used RDP (T1076) to reach the file server.
