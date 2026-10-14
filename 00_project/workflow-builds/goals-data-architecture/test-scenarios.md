# Test scenarios — goals-data-architecture (written before the body, per R1.2)

## S1 — Obvious trigger: regenerate from Supabase
**Phrase:** "regenerate morning-grill-goals.json from Supabase" / "warum zeigt Taxi-Zentrale noch active".
**Expected:** `generate_goals.py` runs, logs "goals generated from Supabase (N portal clients), overlay merged (M non-portal entities)". Taxi-Zentrale is NOT pulled from Supabase (no `clients` row exists for it — confirmed: Supabase `clients` has 10 rows, none named Taxi-Zentrale, Marcel Rosenbach, me&you, or Tacheles). Its status comes from the overlay file only, and stays whatever the overlay says until Martin or a grill answer changes the overlay.

## S2 — Paraphrase: drift complaint
**Phrase:** "the goals file is out of sync with Supabase again, fix the drift" / "the goal sheet doesn't match the portal".
**Expected:** same generator step runs. Per R6.4 (assert or flag, never guess), it does NOT silently overwrite a field it cannot verify — it logs each status/phase transition it makes (old → new, with source) to an archive log, and separately lists any field where the overlay and Supabase actively disagree (e.g. overlay says "restart" but Supabase `clients.status` only has "active"/"onboarding" — confirmed live: Supabase has no "restart" state, so Johni Jaya Motor's "restart" status is 741-specific and must stay in the overlay, not be silently dropped).

## S3 — Must-not-trigger: a single verbal goal edit
**Phrase:** "Suriya's target is now top 3 by December 1" (a plain goal statement, no mention of "regenerate", "sync", "architecture", "drift").
**Expected:** this must NOT trigger a full file regeneration run. It triggers the existing, narrower grill goal-capture step: one `UPDATE`/`INSERT` on Supabase `work_goals` (the column is currently NULL for 8 of 9 rows — baseline/target/due_on/metric_key — so this is normal data entry, not a schema change) and a one-line confirmation. The full generator only runs again on its own schedule or on an explicit "regenerate" ask.

## S4 — Reconciliation trigger (added 2026-10-15, folded into this checkpoint)
**Phrase:** "check Stürzl's address everywhere" / the weekly reconciliation scan step.
**Expected:** `reconcile_drive.py` reads the Drive Source-of-Truth-Sheet NAP tab (via Sheets API) and Supabase `locations`/`client_master_data`, finds the real live disagreement (Supabase "Wiesenhüttenstraße 17" vs Drive/GBP "Untermainkai 26"), and emits exactly one decision card naming both values and their dates — it does not pick a winner and does not write to either system before Martin answers the card.

## S5 — Reconciliation must-not-trigger
**Phrase:** "update Stürzl's NAP to Untermainkai 26" (an explicit, already-decided instruction).
**Expected:** this is a direct write instruction, not a reconciliation scan — it should NOT spawn the diff/card pipeline. It goes straight to a Supabase `locations` update (Martin's "go" is already in the sentence), the same as any normal data edit.
