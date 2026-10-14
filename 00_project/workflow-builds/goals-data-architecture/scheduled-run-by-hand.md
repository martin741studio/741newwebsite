# Scheduled-run step, run by hand (2026-10-15)

Step 3c of the morning-grill run (regenerate the goal sheet) and the NAP reconciliation, run once by hand with the framework python, output read below. The full 06:13 scheduled run is not triggered by hand here (it writes grill snapshots and cards); its first real run is read the next morning.

First attempt failed with CERTIFICATE_VERIFY_FAILED in sb.py (shared Supabase login). Fixed in sb.py (certifi CA bundle, both copies) and rerun below.

## generate_goals.py (real write, idempotent)
```
WARNING: Johni Jaya Motor: overlay status_override='restart' overrides Supabase clients.status='active' (expected — Supabase has no matching state)
written /Users/martindrendel/741website/00_project/morning-grill-goals.json · 13 clients · 0 archive-log lines · 1 warnings
exit=0
```

## reconcile_drive.py (NAP, Stürzl)
```
[
 {
  "client": "STÜRZL Steuerstrafrecht",
  "field": "address",
  "flag": "disagreement",
  "supabase_locations_street": "Wiesenhüttenstraße 17, 60329 Frankfurt am Main",
  "drive_soll_adresse": "Untermainkai 26, 60329 Frankfurt",
  "drive_soll_note": "Vorschlag, Go offen"
 }
]

1 flagged item(s) out of 1 checked — never auto-resolved, needs a grill card.
exit=0
```
