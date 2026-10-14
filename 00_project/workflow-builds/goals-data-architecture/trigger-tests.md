# Trigger tests (2026-10-15)

This build has no new natural-language trigger — it changes what an already-triggered `morning-grill` run does internally (one deterministic step added before the scan, one on-demand/weekly step added). So "trigger" here means: does the right script fire at the right point, and does a plain goal statement (S3/S5) correctly NOT reach the generator/reconciler. Verified by running the actual scripts fresh (new shell process each time, closest proxy to a fresh session for deterministic tooling) and by reviewing the exact `SKILL.md` wording a future grill session will follow.

## S1 — obvious trigger ("regenerate from Supabase" / "why does Taxi-Zentrale still show active")
Ran fresh: `python3 00_project/morning-grill-skill/scripts/generate_goals.py --check-only`
```
WARNING: Johni Jaya Motor: overlay status_override='restart' overrides Supabase clients.status='active' (expected — Supabase has no matching state)
check-only: 13 clients, 0 changes, 1 warnings. Nothing written.
```
PASS — runs, reads Supabase live, reports Taxi-Zentrale correctly (not a Supabase client, comes from the overlay at status `done`, matching the current file — no false "active").

## S2 — paraphrase ("the goals file is out of sync with Supabase again")
Same script, same entry point — `SKILL.md` step 3c is the only place this runs from, worded generically ("regenerate... before scanning"), so any phrasing that means "check/fix the goal sheet" leads here. PASS by construction (one entry point, not phrase-matched).

## S3 — must-not-trigger ("Suriya's target is now top 3 by December 1")
Reviewed `SKILL.md`: step 3c runs unconditionally as part of the existing scan sequence (already happens every grill run, morning and evening) — it is not something a sentence like this would additionally invoke. A plain goal statement goes to the existing grill judgment step, which already writes to Supabase `work_goals` via the same `execute_sql` pattern the grill uses for `approval_items`/`grill_snapshots` (no new code needed — this was already how the grill makes Supabase writes). PASS — the full `generate_goals.py` regeneration is not re-run outside its one call site.

## S4 — reconciliation trigger ("check Stürzl's address everywhere")
Ran fresh: `/Library/Frameworks/Python.framework/Versions/3.10/bin/python3 00_project/morning-grill-skill/scripts/reconcile_drive.py --client "STÜRZL Steuerstrafrecht"`
```
[
 {
  "client": "STÜRZL Steuerstrafrecht", "field": "address", "flag": "disagreement",
  "supabase_locations_street": "Wiesenhüttenstraße 17, 60329 Frankfurt am Main",
  "drive_soll_adresse": "Untermainkai 26, 60329 Frankfurt",
  "drive_soll_note": "Vorschlag, Go offen"
 }
]
1 flagged item(s) out of 1 checked — never auto-resolved, needs a grill card.
```
PASS — found the real, live disagreement, emitted exactly one flagged item, wrote nothing.

## S5 — reconciliation must-not-trigger ("update Stürzl's NAP to Untermainkai 26" — an explicit instruction)
Reviewed: this phrasing names the target value directly: it is a normal Supabase `locations` update (one `UPDATE` statement), not a call to `reconcile_drive.py`. The reconciliation script is only invoked by name/on-demand or the weekly Monday step — an explicit "update X to Y" sentence has no reason to call a diff tool that compares two sources when the human has already resolved which one is right. PASS by construction.
