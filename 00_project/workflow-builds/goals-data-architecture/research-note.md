# Research note — goals-data-architecture (2026-10-15)

**Block chosen:** a deterministic script inside the existing `morning-grill` skill (Execution layer, `patterns.md` §2), not a new skill. Reason: this fixes a data-flow bug for an EXISTING consumer (morning-grill's `scan.py`/`build_cards.py`/`render_command_center.py`, 7 scripts read `morning-grill-goals.json` today). R0.5 (deterministic, must-happen-every-time work belongs in a script, not a new skill description); R2.5 (bundle a script, tell Claude to run it, not read it).

**3 relevant rules:**
- R1.8 plan-validate-execute: for the one-time Supabase backfill of goal numbers, write the plan, validate, then execute, then verify — not a direct edit.
- R6.4: re-check every item right before writing; assert or flag a mismatch, never guess/hedge. Applies to overlay-vs-Supabase conflicts.
- R8.x (741-specific): no destructive change without Martin's go at the checkpoint; this applies to the one-time backfill and to any schema change.

**1 pattern:** `patterns.md` §4.2 Multi-MCP coordination (phase 1 Supabase, phase 2 local file, data passed via files) — already proven in `00_project/workflow-registry/workflow_registry.py`'s `sync` function: fcntl lock, atomic save (`tmp` + `os.replace`), explicit-marker vs. detected-heuristic merge, and the rule "only raises status, never downgrades an approved/archived run." This build extends the same shape to `morning-grill-goals.json`.

**Existing assets found (1.4):** no `.claude/skills/` or `~/.claude/skills/` skill already does this. Closest precedent is `workflow_registry.py` (sync pattern, reused not rebuilt). `morning-grill` skill (`~/.claude/skills/morning-grill/`) is the sole consumer of `morning-grill-goals.json` — 7 scripts (`scan.py`, `build_cards.py`, `publish_tasks.py`, `validate_brief.py`, `build_night_queue.py`, `status_report.py`, `render_command_center.py`) read the file for: `status`, `phase`, `quarter_goal`, `goal_numbers[]`, `leading[]`, `blockers[]`, `waiting_for[]`, `client_rules[]`, `aliases[]`, `chat`, `next_workflow`, `next_milestone`, `notes`. `data-brain-project.md` (memory) already locked a much bigger "741 Data Brain" warehouse plan (2026-08-13, not built) — this build is a small, immediate slice of that, not a replacement for it. `client-work-visibility/data-model.md` already proposed a `client_goal` table; Supabase has since shipped it as `work_goals` (9 rows, one per client, title only — baseline/target/due_on columns exist but are NULL).

**Freshness (1.3):** library last refreshed 2026-10-11, today 2026-10-15 — under 6 weeks, no re-fetch needed.

**External grounding (Martin asked for real sources, not invented):** Azure Architecture Center "CQRS pattern" and "Materialized View pattern" (learn.microsoft.com/en-us/azure/architecture/patterns/cqrs, .../materialized-view) describe exactly this split: a write model is the single source of truth, a read model/materialized view is a denormalized, regenerable, read-only cache optimized for display — never hand-edited, always regenerable by replaying the source. IBM and Monte Carlo's data-reconciliation guides describe comparing two systems of record and surfacing mismatches rather than auto-resolving them — this maps directly to the Drive-vs-Supabase addendum (future phase).

**Open questions for Martin (grill-me, see report):** 1) generated-from-Supabase for portal clients + small hand overlay for non-portal entities, or something else; 2) one-time backfill of goal_numbers into `work_goals` — go or not; 3) new Supabase columns for `aliases`/`client_rules` (schema change) — go or keep in the overlay file for now; 4) reconciliation pass scope — start with NAP only (see below) or wider.

**Scope update 2026-10-15 ~07:20 WITA (relayed):** Martin folded the Supabase-vs-Drive reconciliation pass into THIS checkpoint (not a later phase as the original brief said). Researched and designed below, in the same cp1.

**Reconciliation hand-finding (real, verified live during this research, not invented):** STÜRZL Steuerstrafrecht's address exists in 3 places and disagrees right now:
- Supabase `public.locations.street` = "Wiesenhüttenstraße 17" (row created 2026-10-01, never updated).
- Drive Source-of-Truth-Sheet (`10JISY6H71F_pIX8KzGhrTucDvWXfv2WYh4-M3E72SqY`, tab "11 Citations & NAP") header reads "Soll-Adresse: Untermainkai 26, 60329 Frankfurt (Vorschlag, Go offen)" as of 08.10.2026.
- Memory `anja-stuerzl-client.md` records the GBP profile was actually moved to Untermainkai 26 on 13.10.2026 with Martin's go, and the address is "BESTÄTIGT als kanonische NAP, Martin mehrfach 10/2026: nie wieder als 'zu bestätigen' führen" — but also notes the live website and schema still showed Wiesenhüttenstraße 17 as of 13.10. evening.

So: GBP and Drive agree on Untermainkai 26; Supabase `locations` and (per memory) the live website still say Wiesenhüttenstraße 17. Nobody has pushed the confirmed address into Supabase `locations` since the 01.10 row was created. This is exactly the un-reconciled-disagreement problem Martin described, found live, not hypothetical.

**Technical constraint found:** the Drive MCP (`search_files`/`read_file_content`) returns only a structural/header snippet per sheet tab (verified: reading the Stürzl sheet returned merged header rows only, no data rows). It cannot diff cell-level NAP values. A reconciliation pass needs the Google Sheets API (service-account credentials) — the same stack already used by `00_project/assets/stuerzl/sheet/add_audit_0910.mjs` to write cells — not the generic Drive MCP, to read actual row values.
