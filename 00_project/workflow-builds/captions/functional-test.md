# 4.2 Functional test (fresh session, skill active, 2026-10-19)

Fresh Sonnet subagent, `/captions` with the sample dump pasted, date `2026-10-19-ft`, stop at the checkpoint, no Drive write.

## Result
- 24 blocks. Validator: `24 blocks checked`, `PASS` in 1 round. Slop lint: `score 5/5  CLEAN` in 1 round. No cleanse needed.
- Tool calls: 3 (Skill, 2 Bash). No ToolSearch, no Drive, no questions.
- Output kept in `runs/functional-test/` (captions.md, beats.md, dump.md, _run.json).
- Every number in the captions is in the dump. No invented fact. Hook "We live here on 2,500 euros a month."

## Where the skill was unclear (agent's report) and the patch
| # | Finding | Patch (same day) |
|---|---|---|
| 1 | "laut" and "nie wieder montag" have two readings. No rule for unclear words. Agent wanted to ask Martin. | story-rules section 7: plain reading, "?" in beats.md, open words listed at the checkpoint card. SKILL.md step 7 shows them. |
| 2 | The example hook says "We live in Bali", the dump says "hier". The rule "no location the dump lacks" conflicts with the example. Agent wrote "here". | The hand run was wrong. Example and hand run now say "We live here". New rule: examples are shapes, never text to copy. |
| 3 | "Our visa ends" is an inference (dump: visa agent, Verlängerung, läuft 4.11. ab). | story-rules section 7: supported inference is fine, unsupported is an added fact. |
| 4 | Present tense "Celine has two client calls" reads oddly. | story-rules section 7: past for today's events, present for states, future for plans. |
| 5 | The b-roll wish fits no part of the 4-part shape. | story-rules section 7: note beats go right before the close line, or are dropped. |
| 6 | "1.5 to 2.5 blocks per dump line" and the validator's 12 to 60 are two numbers for one limit. | story-rules section 7: validator = hard limit, the ratio = guide. |

## Verdict
The skill ran end to end without a stall. All 6 findings are patched in `references/story-rules.md` and `SKILL.md` (homeostasis rule: corrections become skill edits, never one-off prompt patches).
