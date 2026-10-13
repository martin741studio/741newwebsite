# 4.3 Baseline — v1 (laptop, 20 nights 15.09.–12.10.) vs v2 (13.10.)

| Measure | v1 (from reporting/night-shift/LOG.md) | v2 night 13.10. |
|---|---|---|
| Work source | LLM planner over portal tasks + client feedback | Martin's confirmed queue (script planner) |
| Items per night | 6 planned, ~5 pass | 4 queued, 3 pass, 1 needs_martin |
| Useful new work | low: same 5 feedback items re-run 8 nights in a row (processed-feedback.json never written) | 4 new items, all from today's evening log |
| Run counter | wrong (undercount; "15/14" on 12.10.) | exact: 10 runs = 10 log lines |
| Cost visible | no (text output) | yes: USD 4.23 (`total_cost_usd`) |
| Planner/loop bugs | `len(plan.json)` bug, Critic sometimes skipped, Reviewer crash | none seen; Critic always paired; reviewer is a script |
| Repeat blocker | Rabenmütter blocker 10 nights | n/a (queue only holds what Martin confirmed) |
| Safety | `acceptEdits`, project allow-list (Write/Edit/curl allowed), MCP servers loaded | `dontAsk`, user settings only, Write/Edit only under reporting/night-shift/**, curl/ftp/ssh/git push/rm denied, no MCP; git write check 0 violations |
| Martin's corrections | not read by anyone (grill O6) | 1 link swap, 1 premise correction; 4 cards answered in one check-in |
| Duration | up to 3 h (20:00–22:59) | 20 min (20:30–20:50) |
