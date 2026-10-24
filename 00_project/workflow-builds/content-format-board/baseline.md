# Baseline comparison (step 4.3) — with vs. without the skill, same task, 2026-10-24

Task in both runs: a short-video idea board for the prospect Little Frenchie (Pererenan/Canggu) for a 741 pitch, using the existing prospect folder and live web research. Both ran as fresh subagent sessions. The baseline was forbidden to open `.claude/skills/` or the build folder.

| Measure | Without skill (baseline) | With skill |
| --- | --- | --- |
| Output | `scratchpad/baseline-board.md`, 247 lines, 12 ideas, 9 sections of its own design | `assets/little-frenchie-bali/content-format-board/2026-10-24/board.md`, 110 lines, 6 ideas, the fixed 7-section template |
| Format knowledge | Ad-hoc web guides found during the run (a restaurant-marketing guide, three short-video blogs) | The verified 4-format taxonomy + the notebook's hook/retention/loop/length rules, per idea |
| Per-idea execution detail | Varies per idea; no fixed hook/second-line/length/ending/quality fields | All 8 fields on every idea (opening line, opening image, proof line, shot list, length, loop ending, quality bar) |
| Finding before formats | Starts with an idea summary | §1 states the real gap first (strong reviews, absent from the public conversation) |
| Open questions | 12 OPEN QUESTIONs, mixed into the ideas | 3 readiness answers + on-camera person + 4 fact checks, in fixed places (§2, §3, §7) |
| Method-name / tool-name leakage | 0 banned terms (scan passed) | 0 banned terms (verifier enforced) |
| Slop lint | 4/5 ("needs a cleanse") — not run by the agent | 5/5, enforced by `verify_board.py` |
| Promise language | none found | none, verifier enforced |
| Telemetry | none | `_run.json` (registry schema) + `research-calls.jsonl` |
| Research calls | 11 (8 search, 3 scrape) | 8 (6 search, 2 scrape), 2 zero-hit queries reported |
| Tool calls / tokens | ~19 calls, ~170k tokens | ~43 calls, ~219k tokens |
| Corrections needed before Martin could see it | Slop cleanse; restructure to a fixed shape; strip unsourced "proven" claims | None; two verify-loop fixes done inside the run |

Reading: the skill costs about 2× the tool calls and 30 % more tokens, and buys a verified format base, a fixed client-safe structure, an enforced slop and leak gate, telemetry, and zero post-run corrections. The baseline's extra ideas (12 vs 6) came from unverified web guides and would need a rewrite before a pitch. Rule R1.6 targets met: triggers on both phrasings, 0 failed API calls, 0 Martin corrections in the skill run.
