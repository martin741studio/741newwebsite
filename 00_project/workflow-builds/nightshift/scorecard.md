# 4.5 Scorecard — Night Shift v2 (laptop phase), 2026-10-13 · `_derived/scorecard.md`

| # | Score | Note |
|---|---|---|
| A1 | 2 | runner + skill on local launchd; routines cannot read the repo (patterns §3, tooling facts) |
| A2 | 2 | rules in prompts, procedure in skill, enforcement in CLI permission flags + runner breakers |
| A3 | 1 | skill is model-invoked on purpose ("Nachtschicht" must trigger); its side effects (queue write, STOP) need Martin's card first |
| A4 | n/a | no cloud routine/Cowork |
| B1 | 2 | use-cases.md (3) |
| B2 | 2 | test-scenarios.md written before the runner and skill |
| B3 | 2 | hand-run.md (real evening log → queue card) |
| B4 | 2 | spec §0, §2, §13 |
| B5 | 2 | pipeline.md §2.5 |
| C1 | 2 | WHAT + WHEN + Do NOT use |
| C2 | 2 | night-shift-v2 |
| C3 | 2 | 43 lines, references/ one level |
| C4 | 2 | mode checklists A/B/C |
| C5 | 2 | run.py, review.py, validate_night.py with error handling; caps via env, no magic numbers in prompts |
| C6 | 1 | output files and verdict JSON fixed; no example pairs yet |
| C7 | 2 | one term per concept (queue, item, verdict) |
| C8 | 2 | no MCP at night; scripts and paths listed |
| D1 | 2 | validate_night.py |
| D2 | 1 | FAIL lines go to Martin as cards; no automatic fix loop |
| D3 | 2 | separate Critic per item + validator |
| D4 | 2 | REVIEW.md + validate output quoted |
| D5 | 2 | trigger-tests.md (skill 4/4, runner 6/6, permissions 3/3) |
| D6 | 1 | baseline v1 vs v2 (one night); no with/without-skill token comparison |
| E1 | 2 | prompts self-contained; TZ Asia/Makassar in LaunchAgent; deadline in WITA |
| E2 | 2 | queue per date = bookmark; state resumes per item |
| E3 | 1 | errors logged per run; "unreadable" relies on the prompt rule |
| E4 | n/a | nothing is posted |
| E5 | 1 | no secrets, no MCP, caps; gap: python3 allowed (git write check logs it) |
| E6 | 2 | prompts live in reporting/night-shift-v2/, agents may write only under reporting/night-shift/** |
| E7 | 2 | validate + 21:30 check-in read every item |
| F1 | n/a | internal output; client chats own client messages |
| F2 | 2 | no live change at night; live follow-ups routed to client chats with go |
| F3 | 2 | sources.md per item; critic spot-checks 3 facts |
| F4 | 2 | summaries and replies in STE |
| F5 | 2 | no method sources named |
| F6 | 2 | registry workflow `nightshift` added; _run.json copied to 00_project/assets/night-shift/<date>/ → sync created the run |
| F7 | n/a | no client-facing deliverable |

Total: 57 / 64 → **89.1 %**. Blocking zeros (A, D): **none**.
Decision: ship for the laptop phase (5 clean nights), then server.
