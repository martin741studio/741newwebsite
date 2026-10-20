# Brief — Client dashboard and report redesign

Date: 2026-10-13. Owner: Martin. Status: design approved (28 decisions + checkpoint). Staging built for Bali (see decisions.md). Live release, feed refresh job and German labels are open.

## Job
Rework how the client portal (clients.741.studio) and the report pages (`/r/<hash>/*.html`) present data.
Trigger: Martin looked at `balihealing-seo-roadmap.html` and said the dashboard is confusing and does not visualise what we want to show.

## What Martin wants (his words, shortened)
1. Go through every data point we want to show a client.
2. Check everything in the live portal and the report pages.
3. Find an ideal reference for how to visualise each point.
4. Put each choice in a decision tree (grill-me cards, same way as the Stürzl run).
5. Rework after that. Nothing is built before the decisions.

## Hard rules
- Questions to Martin only as AskUserQuestion cards. Recommended option first.
- No portal change on live without Martin's go. Staging first.
- Every number needs a source link or a source line. Gaps show as gaps, never as estimates.
- No tool names in client material (no BrightLocal, Falcon, Moz names). Use plain words.
- The client reads in the client language (`clients.lang`). Bali Healing = English.
- Never name method sources. Use "741 Dashboard-Raster" in client files.

## Already designed (do not redo, integrate)
| Module | Folder | State |
|---|---|---|
| Ergebnisse (proof tracking, 34 metrics) | `00_project/tracking-workflow.md`, `tracking-metric-catalog.json`, `assets/tracking-workflow/prototype/` | design go 12.10., pilot Suriya, not installed |
| Kundenarbeit (task list, owner, proof) | `00_project/client-work-visibility/` | live in portal, client view pilot Bali (EN) next |
| Entscheidungen (client picks from 2–3 variants) | `00_project/client-approval-workflow/` | live in portal |
| Morning Grill tasks | `00_project/morning-grill-workflow.md` | writes into work items |

The redesign is the layer above these four: one structure, one visual language, one place for each number.

## Problems seen (13.10.2026, Bali Healing)
Details with evidence are in `01-inventory.md` section 4.
- Overview tab shows no result number at all. It shows onboarding, a generic 90-day list, access settings.
- Onboarding says "1 of 6 steps" while the programme is in week 5.
- Mixed German and English labels in one screen.
- Activity feed shows "0 actions this week" and two entries from 19.08.
- Report list is flat. The newest roadmap carries the date 23.09. in the list but "status 13 Oct" inside.
- The roadmap report is 10,500 px tall, has 12 tables, 2 SVGs, zero charts. It mixes status, plan, grid scans, contact tracking and AI visibility.
- Jargon without translation: SoLV, SAIV, NAP, DA, ARP, PBN, reclaim.
- Internal text visible to clients: "Neuen Report hochladen: Datei in Materialien hochladen, dann per SQL/Claude als Report verknüpfen."

## Process (741 Workflow-Raster)
1. Inventory (done): `01-inventory.md`.
2. Research: references per visualisation family into `00_project/knowledge/client-dashboard-library/`.
3. Decision tree: grill-me rounds, one area per round, max 4 cards per round, recommendation first.
4. Design checkpoint: clickable prototype, desktop 1440 and mobile 390, real Bali data.
5. Build on staging, test, Martin's go for live.
6. Roll the report template out to all clients.

## Pilot
Bali Healing (English, program mode, has the worst report). Second check: Praxis Suriya (German, tracking pilot).
