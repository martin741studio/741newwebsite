# Agent Job Library — how to give a 741 agent a job description, a scope, a gate and a weekly review

Built 2026-11-03 for the workflow `agent-job-descriptions` (build folder `00_project/workflow-builds/agent-job-descriptions/`). Freshness rule: sources younger than 3 months; re-fetch after 6 weeks. Next refresh due: 2026-12-15. Internal library. Never name video or creator sources in client material.

How to use:
1. `grep -ril <term> 00_project/knowledge/agent-job-library/` and read hits in this order: `_derived/` → vendor docs (03–06, 09) → practitioner essays (10, 11) → the video (01).
2. Derived layer: `_derived/agent-job-descriptions-rules.md` (IF/THEN with one source per line), `_derived/agent-job-descriptions-questions.md` (what to ask Martin, what is already answered), `_derived/roster-2026-11-03.md` (the agents that exist today).
3. The skill body greps this library at run time; it never carries the knowledge itself.

## Sources

| # | File | Type | Date | What it gives | Status |
|---|---|---|---|---|---|
| 01 | `sources/01-tyler-phillips-hire-ai-like-an-employee-transcript.md` | video transcript, Martin's input | 2026-11-01 | the 7-part job block, Friday review, task→skill→routine loop | local, full transcript |
| 02 | `sources/02-tyler-phillips-channel-x-and-hire-doc.md` | creator context | 2026-11-03 | nothing beyond 01; HIRE doc not public; X not readable | local |
| 03 | `sources/03-openai-private-intelligence-agent-actions.md` | vendor page | 2026-10-30 | four boundary fields: data access, tools, permitted actions, required approvals | local |
| 04 | `sources/04-grok-bot-docs-work-bots-jobs-skills-routines.md` | vendor docs | 2026-11-02 cache | split criterion for roles, 5-part reviewable result, trust ladder, missing-source rule | local |
| 05 | `sources/05-grok-bot-security-approvals-auto-review.md` | vendor docs | 2026-11-02 cache | three enforcement layers; narrow ask-first rules; approval scope | local |
| 06 | `sources/06-openai-practical-guide-building-agents.md` | vendor guide | 2026-01-15 | tool risk rating (4 factors), two human-intervention triggers, edge cases | local |
| 07 | `sources/07-crewai-role-goal-backstory.md` | framework docs | 2026 | goal with success criterion, expected output, caps, delegation flag | local |
| 08 | `sources/08-anthropic-building-effective-agent-automations.md` | engineering blog | 2026 | preferences vs state, bookmarks, ledger, unreadable ≠ nothing new, proposals | pointer to workflow-library copy |
| 09 | `sources/09-claude-code-docs-enforcement-layers.md` | official docs | living | enforcement ladder: CLAUDE.md < rules < skill < hook < subagent tools | pointer to workflow-library copies |
| 10 | `sources/10-matthews-wong-agent-harness-engineering.md` | practitioner essay, 20 refs | 2026-10-18 | self-grading bias, judge by what landed, duplicated policy drifts, stale-rule audit | local |
| 11 | `sources/11-incresco-claude-code-harness-guide.md` | practitioner guide | 2026-10-11 | rule ladder, brief fields, verification table, "twice → rung" | local |
| 12 | `sources/12-x-trend-ai-job-architectures-and-12-block-system-UNVERIFIED.md` | secondary claim | — | not locatable; recorded as unverified | open: Martin may drop the post in |
| 13 | `sources/13-741-internal-control-mechanisms.md` | internal inventory | 2026-11-03 | go-gate, slop gate, night shift, morning grill, registry, scheduled tasks, memory layers | local |

Still to export: nothing required. Optional: Tyler Phillips' X posts (x.com unreadable from here) and the "12-block" post if Martin has it.

## What the video gets right, what it misses (one-paragraph verdict)
Right: the vocabulary (title, duties, locked tools, approval on send/spend/delete/publish, weekly review, promote a good day to a skill and a routine). Missing: enforcement (every "do not" is prose), evidence (the review is self-graded; 10 shows that grader is biased), a manager definition, a roster, change control for the description itself, and the missing-source rule. Sources 03–11 supply each of those; 13 shows 741 already owns the enforcement and manager layers and must not build them twice.
