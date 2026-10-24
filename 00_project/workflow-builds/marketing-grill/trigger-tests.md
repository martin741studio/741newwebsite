# Trigger tests (Step 4.1) — fresh subagent sessions, 2026-10-25

Method (same as `content-format-board`'s build): fresh Explore subagents, each reading ONLY the frontmatter `description` of every skill under `.claude/skills/*/SKILL.md`, naming the single skill it would invoke. No task executed.

| # | Scenario | Message | Picked | Result |
| --- | --- | --- | --- | --- |
| 1 | Obvious | "marketing grill" | `marketing-grill` | PASS |
| 2 | Paraphrase | "I don't know if I should be doing cold email or LinkedIn outreach right now, help me figure out 741's lead gen." | `marketing-grill` | PASS |
| 3 | Negative | "write a LinkedIn post for 741 about our new pricing." | `personal-posts` (explicitly confirmed `marketing-grill` wrong) | PASS (not this skill) |
| 3b | Negative | "build the content board for Praxis Suriya" | `content-format-board` (explicitly confirmed `marketing-grill` wrong) | PASS (not this skill) |
| 3c | Negative | "prep me for my call with Katharina Kisser" | `sales-call-prep` (explicitly confirmed `marketing-grill` wrong) | PASS (not this skill) |

Observations: all 5/5 passed on the first draft of the description — no `description` change needed (Rule R4.8). The negative cases confirm the description's "Do NOT use for" list (personal-posts, content-format-board, sales-call-prep/booking-sequence) is doing real work, not just decorative text.
