# Trigger tests — video-edit (step 4.1, fresh sessions)

Run 2026-10-27, 4 fresh subagents (no context of this build), each given one message and asked only to state which skill it would invoke, not to execute anything.

| # | Input | Expected | Result | Pass |
|---|---|---|---|---|
| 1 | "/video-edit — here's my raw clip [file], here's the reference [link], make it a 9:16 reel..." | video-edit | video-edit | ✅ |
| 2 | "cut this talking-head footage down like that TikTok I sent you, I want it punchy for Instagram." | video-edit | video-edit | ✅ |
| 3 | "write today's captions from our dump, usual format." | NOT video-edit (captions) | captions | ✅ |
| 4 | "give the client some video content ideas for next month." | NOT video-edit (content-format-board) | content-format-board | ✅ |

4/4 correct.

## Observation (not a blocker)
Agent 1 noted the `video-edit` line in its available-skills listing had no description text next to it (name only), so its match rested on the literal "/video-edit" string rather than the frontmatter description. Checked: `marketing-grill` and `sales-pitch` — both also built via workflow-create — show the same way (bare name, no description) in this session's own skills listing, while older skills like `captions` show full descriptions. This looks like a harness indexing lag for recently-created project skills, not a defect in this skill's frontmatter (the description text itself is present and correctly formed in SKILL.md, matching the working skills' format byte-for-byte in structure). Expected to resolve once this skill has been through a normal session restart/re-index, same as its sibling skills. Not fixed here — nothing in `video-edit`'s own files is wrong.
