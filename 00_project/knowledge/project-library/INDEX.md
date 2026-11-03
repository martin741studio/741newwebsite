# Project Library — knowledge base of the 741 Project Manager agent

Built 2026-11-03 for the agent `project-manager` (description `00_project/agent-jobs/project-manager.md`). Freshness: external sources younger than 3 months, re-check after 6 weeks; next refresh due 2026-12-15. Internal library. Never name a framework (RACI, Kanban, DRI) or a guru in anything a client, team member or partner sees; call the method "741 Work-Raster" internally if it needs a name.

How to use:
1. `grep -ril <term> 00_project/knowledge/project-library/` and read hits in this order: `_derived/` → `sources/04` (the real 741 model, always fresh) → `sources/20` (Hormozi team/ops) → external notes 01–03.
2. Derived layer: `_derived/project-manager-rules.md` (P1–P6, 27 rules, one source each), `_derived/project-manager-questions.md` (8 answered by Martin's cards, 1 open, 2 later).
3. The client-work library (`../client-work-library/`, 64 sources) and the Hormozi library (`../hormozi-library/`) stay where they are; this library points at them and distils the project-management part.

## Sources
| # | File | Type | What it gives |
|---|---|---|---|
| 01 | `sources/01-wip-limits-and-flow-small-teams.md` | external, 4 sources | WIP = people+1, pull not push, Little's Law |
| 02 | `sources/02-single-owner-accountability-raci-dri.md` | external, 3 sources | one accountable owner per task, five things the owner must give |
| 03 | `sources/03-agency-weekly-loop-and-client-health.md` | external, 2 sources | one status place, weekly loop, client-health early-warning numbers |
| 04 | `sources/04-741-work-item-model-and-client-work-library.md` | internal + 120-rule extract | the real `work_items` status machine, what is live vs. only designed, 2 real gaps |
| 20 | `sources/20-hormozi-team-and-operations-extract.md` | extract of 10 Hormozi files | delegation, document-demonstrate-duplicate, constraint theory, ramp time, leader ratio |

Still to export: nothing required.

## What is already live vs. what the agent must build on
Live (from source 04): the `work_items`/`work_events`/`work_evidence` tables, 21 actors seeded, the proof-before-done trigger, the morning grill writing into work_items, the Kundenarbeit admin counters. Designed but not built: team portal logins, the client-facing four-block view, the decision-task URL exemption. The Project Manager works on top of the live tables and proposes the designed-but-missing pieces as cards, never builds them itself.
