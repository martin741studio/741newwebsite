# Hand-run — one real task solved by hand (2026-10-15)

## Task A: regenerate two goal-sheet entries from Supabase by hand, diff against the current file

Picked Praxis Suriya (portal client) and Taxi-Zentrale Nürnberg (not a portal client) because they sit on opposite sides of the design question.

**Suriya — queried Supabase directly:**
- `clients`: status = `active`, mode `program`, lang `de`. Matches `goals.json`.
- `work_phases` where `status='current'`: `P4` (Aufbau). Matches `goals.json` `"phase": "P4"` exactly.
- `work_goals`: one row, `title` = "Top 3 in the Maps grid for the 5 tracked keywords (Martin 2026-10-13)", matches `quarter_goal` verbatim. `baseline`/`target`/`due_on`/`metric_key` are all NULL — so the detailed `goal_numbers[]` sub-array in the JSON (baseline text, target "top 3", due 2026-12-01) is NOT yet in Supabase. A pure generator would currently drop this detail unless (a) it is backfilled once, or (b) the generator keeps falling back to the overlay for `goal_numbers` until backfilled.
- `access_grants` (status != 'erteilt'): Search Console `ausstehend`, Website/Hosting `angefragt` — these map closely to 2 of the 4 lines in `goals.json`'s `blockers[]`, but not all 4 (e.g. "No big change without backup and her OK" is a client rule, not an access row).
- `work_items` with `status='waiting'`: one row, `waiting_on='martin'` — maps to the one `waiting_for` entry in the JSON (`who: client`, read via `access_grants`, not `work_items`, in this case — the two tables cover different halves of "waiting").

**Context I had to supply by hand that a script cannot invent:** the alias-matching logic (goals.json's `aliases: ["suriya","coralie"]` has no Supabase equivalent — `clients.name` is the only name field); which `access_grants` rows count as "blockers" vs. which blockers are free text with no structured home (domain 404, GTM access-type issues already closed); the mapping from `work_phases.code` to the human phase label used across all 7 consumer scripts.

**Taxi-Zentrale Nürnberg — queried `clients` for a matching row: none exists.** Confirmed: Supabase `public.clients` has exactly 10 rows (Bali Healing, Johni Jaya Motor, Kamil Böyük, Maria Brasse, Naturheilpraxis Daniela Dumann, Praxis Hüwel, Praxis Suriya, Rabenmütter Shop, STÜRZL Steuerstrafrecht, Testpraxis Musterstadt). Taxi-Zentrale, Marcel Rosenbach, me&you/Pauspapier and Tacheles are not portal clients and never will be (Joomla client, sales prospect, partner engagement, closed white-label work). This is the concrete proof that "goals.json = 100% generated from Supabase" cannot be the design — a fixed overlay for non-portal entities is required, not optional.

## Task B: trace one client's NAP across every system that claims to hold it (the reconciliation addendum)

Picked STÜRZL Steuerstrafrecht's address because memory already flagged a move (13.10.2026).
1. Queried Supabase `locations`: `street = "Wiesenhüttenstraße 17"`, row `created_at = 2026-10-01`, never updated.
2. Read the Drive Source-of-Truth-Sheet (`10JISY6H71F_pIX8KzGhrTucDvWXfv2WYh4-M3E72SqY`) via the Drive MCP: tab "11 Citations & NAP" header literally reads "Soll-Adresse: Untermainkai 26, 60329 Frankfurt (Vorschlag, Go offen)" as of 08.10.2026.
3. Checked memory `anja-stuerzl-client.md`: GBP profile moved to Untermainkai 26 on 13.10.2026 with Martin's go, address called "kanonische NAP" — but the same memory entry says the live website and schema still showed Wiesenhüttenstraße 17 as of 13.10 evening.
4. Result: 4 systems, 2 values, nobody pushing the confirmed value into the other systems. Supabase `locations` (the row the portal and any future citation/report automation would read) is the stalest of the four.

**Context I had to supply by hand:** the Drive MCP's `read_file_content` only returned merged header rows per tab, not the actual per-directory rows under "11 Citations & NAP" — I had to recognize that limitation and look instead for the header's embedded "Soll-Adresse" note, and separately cross-check memory for the GBP move date, since no single tool gave the full picture. A real reconciliation script needs the Google Sheets API (service-account), not the Drive MCP, to read actual cell values — this was not obvious before testing it.
