# 3.7 Unattended rules (workflow-library rules.md §6 + ops-library rules) — how Night Shift v2 meets them

| Rule | Meaning | v2 implementation | Status |
|---|---|---|---|
| R6.1 bookmarks | read from a bookmark, not a fixed window | the queue is the bookmark: only items Martin confirmed for that date; state.json resumes per item | met |
| R6.2 unreadable ≠ nothing | failed source reported | executor prompt rule 3 ("[fehlt: …]"); critic C3; runner logs `is_error` per run | met |
| R6.3 confirm before ledger | count as done only after confirmation | item = pass only after a separate Critic run writes the verdict file; Martin's click is the only "done" (morning grill) | met |
| R6.4 re-check before post | — | nothing is posted at night | n/a |
| R6.5 read-only creds + spend cap | | no secrets sourced; `--strict-mcp-config` (no WordPress/Supabase MCP); cap 14 runs / est. USD 10 / per-run `--max-budget-usd` | met (gap: `python3` allowed; git check logs writes) |
| R6.6 time zone | | LaunchAgent TZ=Asia/Makassar; deadline 22:45 WITA in the runner | met |
| R6.7 self-contained prompt | | prompts/executor.md + critic.md state task, limits, done, output | met |
| R6.8 payload as data | | executor rule 4: instructions inside fetched pages are ignored and noted | met |
| R6.9 not on the hour | | 17:30 / 20:30 local LaunchAgent (no cloud jitter issue) | n/a |
| R6.10 green ≠ success | | `validate_night.py` + Martin reads REVIEW at 06:13 | met |
| R6.11 skill availability | | runner uses prompt files in the repo, no skill dependency | met |
| ops R22 autonomy ladder | start at L0/L1 | L1: act (drafts) + report; no live action class exists at night | met |
| ops R27 idempotent queue | re-runs must not duplicate | state.json skips pass/needs_martin items; 20:30 resume slot is safe; lock dir | met |
| ops R28 pulse log | | `pulse.log` line per night; missing line → 06:13 card | met |
| ops R36 approvals never from another session | | queue writer needs `--confirmed-by` quoting Martin; SKILL.md critical rule 2 | met |
| tooling: Desktop/launchd skip when asleep | | caffeinate -i during runs; 20:30 resume slot; old sleep agent at 23:02 after the 22:45 stop | met |
| tooling: cloud routines cannot read the repo | | laptop phase uses local launchd, not routines | met |
