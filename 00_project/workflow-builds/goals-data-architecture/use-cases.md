# Use cases — goals-data-architecture

## UC1 — Morning grill run regenerates the goal sheet fresh
**Trigger:** the scheduled grill run (06:13 / 17:00 WITA) reaches its scan step, or Martin asks "regenerate the goal sheet" / "why does Taxi-Zentrale still show active".
**Steps:** `generate_goals.py` (new) reads `clients`, `programs`, `work_phases` (current row), `work_goals` from Supabase (read-only) for portal clients → loads the small hand-kept overlay file for non-portal entities (Taxi-Zentrale, Marcel Rosenbach, me&you/Pauspapier, Tacheles, leads) and for fields Supabase does not model yet (aliases, chat id, client_rules, free-text blockers/waiting_for, next_workflow, notes) → merges (Supabase wins for portal clients' status/phase/goal fields, overlay fills the rest) → diffs against the previous generated file and appends any status/phase transition to an archive log → writes `morning-grill-goals.json` with a header comment marking it generated.
**Tools:** Supabase MCP (`execute_sql`, read-only), local script, file write.
**Result:** `status`/`phase`/`quarter_goal` can never silently stay stale the way Taxi-Zentrale's "active" did — they are read fresh every run, not hand-edited. The 7 existing consumer scripts (`scan.py`, `build_cards.py`, `publish_tasks.py`, `validate_brief.py`, `build_night_queue.py`, `status_report.py`, `render_command_center.py`) need zero changes — they still read `morning-grill-goals.json` the same shape as today.

## UC2 — Martin states a goal number verbally in the grill chat
**Trigger:** "target for Suriya is top 3 by December 1" / any verbal goal confirmation during a grill round.
**Steps:** Claude writes directly into Supabase `work_goals` (insert or update the `baseline`/`target`/`due_on`/`metric_key`/`status` columns — currently NULL for all 9 rows except `title`), not into the JSON file.
**Tools:** Supabase MCP `execute_sql` (write, with Martin's go per the existing grill-decision rule).
**Result:** the next scheduled regeneration (UC1) picks the number up automatically. Closes the exact gap Martin named: "a verbal goal target never got written to the file."

## UC3 — Non-portal engagement needs tracking (no Supabase row exists)
**Trigger:** a new sales prospect, partner, or off-portal engagement (like Marcel Rosenbach or Taxi-Zentrale) needs a status line in the grill.
**Steps:** added to the small overlay file by hand (or via an AskUserQuestion-confirmed grill answer), never through the Supabase generator path, because no `clients` row exists for these.
**Tools:** manual edit / grill card.
**Result:** leads and off-portal clients keep working without forcing portal onboarding on entities that will never have one.

## UC4 — Reconciliation pass flags a Drive-vs-Supabase disagreement (folded in 2026-10-15)
**Trigger:** weekly scan step, or Martin asks "check <client>'s address/NAP everywhere".
**Steps:** `reconcile_drive.py` (new) reads the client's Drive Source-of-Truth-Sheet tab "11 Citations & NAP" (via the Google Sheets API — the generic Drive MCP only returns header snippets, confirmed by testing) → reads Supabase `locations` + `client_master_data` for the same client → diffs NAP field by field → where they disagree, emits a decision card (not an auto-fix) into the existing grill card pipeline: "Supabase says X, Drive says Y, which is current?" → Martin answers; Claude updates only the side he names.
**Tools:** Google Sheets API (service account, same stack as the existing `00_project/assets/stuerzl/sheet/*.mjs` scripts), Supabase MCP (read for the diff; write only after Martin's per-item go), the existing grill card pipeline (`build_cards.py`).
**Result:** real, verified case during this research — Stürzl's address is "Wiesenhüttenstraße 17" in Supabase `locations` (unchanged since 01.10) but "Untermainkai 26" in the Drive sheet and the live GBP profile (moved 13.10 with Martin's go) — gets caught and surfaced as a card instead of staying silently wrong.
