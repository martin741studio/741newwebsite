# Functional test (step 4.2) — fresh session, skill active, 2026-10-24

Task: "Build a content format board for Little Frenchie Bali." Run by a fresh subagent session that read SKILL.md and followed steps 1–8, stopping before step 9 (Martin's go). Output: `00_project/assets/little-frenchie-bali/content-format-board/2026-10-24/board.md` (6 ideas) + `_run.json` + `research-calls.jsonl`.

Result: `BOARD PASSED · 6 ideas · 0 failures` after two verify loops (first blocked on the banned phrase "one shot" and em-dashes in headings; second on slop 4/5 for "at the end of the day"; two small rewrites, no cleanse needed). 8 research calls (6 search, 2 scrape), 2 with 0 relevant hits, both reported as such in the board. ~43 tool calls, ~219k tokens.

## Where it stalled, guessed, or asked — and the skill patch for each
| # | Finding (step) | Patch (same session, 2026-10-24) |
| --- | --- | --- |
| 1 | Step 3: no readiness answers or on-camera person on file; skill wanted to ask | Expected behaviour: wrote OPEN QUESTION and continued (Martin's decision). No change. |
| 2 | Step 4: `hits` meaning unclear (raw vs relevant) | `log_research_calls.py` docstring + SKILL.md: hits = relevant results (category AND area) |
| 3 | Step 4: oversize page (81k chars) could not be read; agent grepped the saved file | SKILL.md step 4: save, grep for client name + keyword, log the count; else log unreadable; never summarize an unread page |
| 4 | Step 4: competitor threads rule needs a URL; files had domains only; agent guessed and skipped | SKILL.md: "competitor post URL (not just a domain)" |
| 5 | Step 7: slop lint treats heading dash + next line as one sentence | Idea headings now `### Idea N: <label>`; labels and template markers use commas/colons, no em-dashes; verifier warns on dashes |
| 6 | Step 8: banned-term check flagged plain English "one shot" | "one shot" (space) removed from the banned list; hyphenated "one-shot" stays banned |
| 7 | Input files conflict (intake.md DE/2276 vs intake.json ID/2360; prospect.json claim vs competitor table) | SKILL.md step 2: use the file with the raw table, do not repeat the claim, list the conflict in the reply |
| 8 | No STE check was run | `verify_board.py` now WARNs on sentences over 20 words; SKILL.md step 7 states the STE rules |
| 9 | Idea 4 differentiator and Idea 6 drive time not in the files | Expected: marked OPEN QUESTION / "owner checks". No change. |

Re-verified after the patches: `BOARD PASSED · 6 ideas · 0 failures`, slop 5/5, no WARN.
