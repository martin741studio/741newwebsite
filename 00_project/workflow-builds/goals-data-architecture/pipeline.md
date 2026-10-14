# Pipeline — goals-data-architecture

## Shape
Multi-MCP coordination (`patterns.md` §4.2): Phase 1 Supabase (read), Phase 2 local overlay file (read), Phase 3 merge + write, Phase 4 (reconciliation, folded in) Drive Sheets API (read) + Supabase (read) + grill card (decide). Extends `workflow_registry.py`'s proven sync shape: explicit source wins where it has data, detected/overlay fills gaps, only raises status, never silently downgrades an approved/archived entry, atomic file write (`tmp` + `os.replace`), one source of truth per field — never two writers for the same field.

## Phase A — Goal-sheet generation (every grill run)
1. **Read Supabase** (`clients`, `programs`, `work_phases` where `status='current'`, `work_goals`) — script, read-only.
2. **Read the overlay** `00_project/morning-grill-goals-overlay.json` (new, small) — holds: non-portal entities in full (Taxi-Zentrale, Marcel, me&you, Tacheles, leads), plus per-portal-client fields Supabase does not model (`aliases`, `chat`, `client_rules`, `next_workflow`, `notes`, free-text `blockers`/`waiting_for` not covered by `access_grants`/`work_items`).
3. **Merge** — script, fixed precedence: for a portal client, Supabase wins on `status`, `phase` (from `work_phases.code`), `quarter_goal` (from `work_goals.title`), and `goal_numbers` fields that are populated; the overlay fills anything Supabase has NULL or does not model. For a non-portal entity, the overlay is the entire entry.
4. **Diff against the previous generated file** — script. Every status/phase transition gets one line in `00_project/morning-grill-goals-archive-log.md` (date, client, old → new, source). Nothing is removed from view silently; a client moving to `done`/`archived` still shows, logged, same as `workflow_registry.py`'s rule.
5. **Flag, don't fix, overlay-vs-Supabase contradictions** (e.g. overlay status `restart`, a 741-only state Supabase has no column for) — printed as a warning, never auto-resolved.
6. **Write** `morning-grill-goals.json` with a header comment: "generated <timestamp>; edit Supabase (goal numbers, status, phase) or the overlay (everything else) — never this file by hand."
7. Downstream: `scan.py`, `build_cards.py`, `publish_tasks.py`, `validate_brief.py`, `build_night_queue.py`, `status_report.py`, `render_command_center.py` keep reading the same file shape — zero changes needed there.

**Checkpoint:** none inside Phase A itself (fully automated, read-only on Supabase) — this is cp1/cp2 of the workflow build, not a per-run Martin gate.

## Phase B — Goal-number capture (whenever Martin states a number)
1. Claude writes directly to Supabase `work_goals` (`baseline`/`target`/`due_on`/`metric_key`/`status`), the same existing-pattern write the grill already does elsewhere (`approval_items`, `grill_snapshots`).
2. Next Phase A run picks it up automatically.

**Checkpoint:** normal grill-chat confirmation (Martin's own words = the go), not a separate gate.

## Phase C — Reconciliation pass (folded into this build, 2026-10-15 scope update)
1. **Read the Drive Source-of-Truth-Sheet** for a client that has one, via the **Google Sheets API** (service account — the Drive MCP only returns header/structure snippets per tab, confirmed by testing on Stürzl's sheet; it cannot read row-level NAP values).
2. **Read Supabase** `locations` + `client_master_data` for the same client — read-only.
3. **Diff field by field.** Start with NAP (name/address/phone) only — the highest-leverage field, and the one both systems already model structurally. Widen to other fields (pricing, contract terms from the Contracts folder) only after this slice works (R1.3: one hard task first).
4. **Where they disagree:** emit one decision card into the existing grill card pipeline (`build_cards.py`'s shape, same as `release-decisions-from-chat.md`'s pattern) — states both values with their dates, asks which is current. Never auto-resolves.
5. **Where only one side has a value:** flag as "missing in X", not an auto-fill.
6. **Where no Drive sheet exists yet for a client:** flag as "no Source-of-Truth-Sheet" rather than silently skipping — surfaces the rollout gap (today only Stürzl has one).
7. **Write nothing** to either system until Martin answers the card naming the correct value; then one targeted update to the side he names.

**Cadence:** weekly scan step (new scan source, next free `S` id in `scan.py`'s numbering) plus on-demand ("check <client>'s NAP everywhere"). Not every grill run — ~10 clients × several fields is too noisy daily, and Drive Sheets API calls are the slow part.

**Checkpoint:** every disagreement is a Martin-answered card; no automatic writes. This phase is itself gated at cp2 (build) behind the same checkpoint-1 go as Phase A — one design, two slices, because the brief said do not build it standalone later.

## Degrees of freedom (R1.7)
| Step | Freedom | Why |
| --- | --- | --- |
| Supabase reads (Phase A.1, C.2) | Script, zero | Fixed SQL, must be exact |
| Overlay merge precedence (A.3) | Script, zero | Explicit precedence table above, no judgment calls |
| Archive-log diff + write (A.4) | Script, zero | Deterministic diff, same as `workflow_registry.py` |
| Overlay-vs-Supabase contradiction flagging (A.5) | Script detects, human decides | Script never auto-resolves; Martin's call via a card if it matters |
| One-time backfill of `work_goals.baseline/target/due_on` from today's JSON | Human-gated, medium freedom | Data entry needs judgment (which JSON value is still true); done by hand with Martin's go per client, not scripted |
| New Supabase columns for `aliases`/`client_rules` (schema change) | Zero freedom, blocked | Requires an explicit migration + Martin's go; open question for cp1, not assumed |
| Drive Sheets API read + NAP diff (C.1–C.3) | Script, zero | Fixed field comparison |
| Which value is correct (C.4) | Human only | Never automated — matches `release-decisions-from-chat.md` hard rule |
| Widening reconciliation beyond NAP | Future, not this build | Explicitly scoped down to one field first (R1.3) |
