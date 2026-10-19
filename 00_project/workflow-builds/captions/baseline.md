# 4.3 Baseline: with vs without the captions skill (2026-10-19)

Same sample dump, two fresh Sonnet sessions. "Without" got the task in plain words (English, we-voice, short lines) and was told not to look at the skill or the build folder.

| | Without skill (baseline) | With skill (functional test) |
|---|---|---|
| Tool calls | 1 | 3 (Skill, intake, validator + lint) |
| Tokens | 108,892 | 118,477 (+9 %, the skill text and the references) |
| Blocks | 20 | 24 |
| Added facts (not in the dump) | 3 clear inventions: "It sits by the sea", "No Monday dread here", "We film it next time". Plus 4 assumed units or readings the agent listed itself. | 0. Two supported inferences ("Our visa ends", "6 am"), both marked by the agent. |
| Format violations | Blocks 9 and 18 have 3 to 4 lines. No line limit, no word limit, no character limit applied. | 0. Validator PASS, 24 blocks, max 12 words, max 2 lines, max 42 chars. |
| Number check | By eye only | Script: every number in the dump |
| Slop lint | Not run | 5/5 in 1 round |
| Questions it wanted to ask | 8 (format limits, meaning of "laut", units, privacy of the budget, the hook) | 3 (meaning of "laut", "Bali" in the example, the b-roll note); all three became skill rules the same day |
| Where the output went | Scratchpad text file, no record | Run folder with dump.md, beats.md, captions.md, _run.json |
| Corrections Martin would have to make | At least 3 invented lines to delete, 2 blocks to split, units to check | The open "?" words at the checkpoint card |

Result: the skill costs 2 more tool calls and 9 % more tokens. It removes all 3 invented facts and all format violations, adds a number check and a slop gate, and keeps a record per day. The baseline agent asked for exactly what the skill fixes: format limits, a rule for unclear words, and a numbers check.
