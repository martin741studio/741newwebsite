# Drive Source-of-Truth sheet update (2026-10-15)

Go: Martin, relayed via the orchestrator ("yes, update the Drive Source-of-Truth sheet too ... Untermainkai 26").
Sheet: STÜRZL Steuerstrafrecht — Requirement Sheets (Source of Truth), tab "11 Citations & NAP".
Scope: only the NAP header and the Frankfurt Google-Unternehmensprofil row. The other listings (website, anwalt.de, 11880, Creditreform, Cylex, Infobel) are out of scope per Martin and were not changed.

| Cell | Before | After |
| --- | --- | --- |
| A1 | "... Soll-Adresse: Untermainkai 26, 60329 Frankfurt (Vorschlag, Go offen)" | "... Soll-Adresse: Untermainkai 26, 60329 Frankfurt am Main (bestätigt 15.10.2026, passt zu Supabase und Google-Profil)" |
| D4 | "Wiesenhüttenstraße 17, 60329 Frankfurt am Main" | "Untermainkai 26, 60329 Frankfurt am Main" |
| F4 | "alt (Umzug 05.10.)" | "korrekt nach Umzug (13.10.2026)" |
| G4 | "Adresse auf Untermainkai 26 ändern (nach Go), Kategorien, Leistungen" | "Kategorien, Leistungen offen (Adresse erledigt 15.10.)" |

Backup of the range before the write: drive-nap-before.json (same folder).
Write method: Sheets API, service account reporting-bot, RAW values, batchUpdate. 4 cells updated, read back and verified.

Reconciliation after the write (reconcile_drive.py):
```
[
 {
  "client": "STÜRZL Steuerstrafrecht",
  "field": "address",
  "flag": "ok",
  "note": "Supabase locations matches the Drive Soll-Adresse"
 }
]
0 flagged item(s) out of 1 checked — never auto-resolved, needs a grill card.
```
