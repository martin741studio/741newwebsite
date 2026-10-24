# Trigger tests (step 4.1) — fresh sessions, 2026-10-24

Method: three fresh subagent sessions, each read only the `description` frontmatter of every skill under `.claude/skills/` and named the one skill it would invoke. No task executed. The new skill's listing appeared in the session's skill list after the build (confirmed in this session's environment update).

| # | Scenario | Message | Picked | Result |
| --- | --- | --- | --- | --- |
| 1 | Obvious | "Build a content format board for Little Frenchie Bali." | `content-format-board` | PASS |
| 2 | Paraphrase | "What video content should we pitch Little Frenchie with — give me some format ideas for the call." | `content-format-board` | PASS |
| 3a | Negative | "Write the homepage copy for Little Frenchie." | `cro-homepage` (runner-up `seo-page-optimizer`) | PASS (not this skill) |
| 3b | Negative | "What keywords should Little Frenchie's blog target?" | `content-pool` | PASS (not this skill) |
| 3c | Negative | "Write a LinkedIn post about my own take on Bali restaurants." | `personal-posts` | PASS (not this skill) |
| 3d | Negative | "Make a before/after Local Falcon story for Little Frenchie." | none (story-automation / social-visuals exist as memories + scripts, not as a skill dir) | PASS (not this skill) |

Observations: 3a routed to `cro-homepage` rather than `content-writing` because `content-writing` is installed under `~/.claude/skills/` (personal), not in the project folder the test read — the test's scope, not a description problem. No description change needed (Rule R4.8). Over-trigger risk checked: the four neighbours did not pull toward this skill.
