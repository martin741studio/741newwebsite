# Client work view: brief (grill-me, 2026-10-13)

Status: research done on 13.10. (64 sources in 4 areas, plus an inventory of our own data). A data model proposal and a clickable prototype exist. Nothing is built in the portal. The design check with Martin is next.

## Job
For each client, show in one place:
- the task list,
- the delegation list (owner: Martin, team, AI agent or client),
- links to where the sources and proof are,
- what was worked out (the outcome).

The view goes from data gathering to clear next steps. AI does most of the work, and Martin and the team support it. Today the portal has only a fixed 13-week task list per client, which is not enough. The view needs proper visuals and proper data storage.

## Decisions (Martin, 2026-10-13)
| Topic | Decision |
| --- | --- |
| Users and order | Step 1: admin (Martin) sees all clients. Step 2: each team member sees only their own tasks. Step 3: the client sees a cleaned-up view (done, next, what we need from you, results with proof). Internal notes and agent noise stay hidden from the client. |
| 13-week list | The 13 weeks stay, but only as phases or milestones. Real tasks with owners, sources and results sit below them. Progress comes from the real tasks. |
| Team place | The team works in the portal: "my tasks" with due date, handoff note and source links. They tick "done" with a proof link. |
| Outcome of a task | All four: a proof link (live URL, screenshot, report, Drive file, chat or run), the result in client words, the effect on a goal number (measured later), and time and cost (who spent how long, agent cost per run). |

## Inputs we reuse
- Morning Grill: decision cards, plan per client with owner, Command Center tab (`00_project/morning-grill-workflow.md`, `00_project/knowledge/ops-library/`).
- Client approval: approval items, decision log, "ready for live" list, Martin's go (`00_project/client-approval-workflow/`).
- Tracking: metric catalog, goal numbers, source links (`00_project/tracking-workflow.md`).
- Workflow registry: `_run.json` for each run, overview Excel.

## Coordination
- The Morning Grill chat builds a thin v0 "Tasks" tab from its plan. It creates no new task tables until this design proposes the data model (confirmed by that chat on 13.10.).
- Its tables: `grill_snapshots` (id, run_date, mode, created_at, data jsonb) and `grill_answers` (id, card_id, run_date, option incl. `own`, note, answered_by, answered_at). Both are admin-only through RLS.
- Its tasks today live only in the snapshot JSON as `data.tasks[]`: id, owner (Martin | agent | Dinakar | Tantri | Gayo | external), status (open | in_progress | waiting | drafted | done), client, title, card, source_card, link (file path), session (chat id), next, due. The file for each run is `00_project/assets/morning-grill/<date>/tasks.json`. Team tasks exist only as drafts (`team-tasks-drafts.md`, rule D22).
- Hand-over: send the schema proposal to the Morning Grill chat. Its grill then writes into the new task model instead of `tasks.json`. These fields map one to one to a task row plus an owner and a source link.

## Research (done 13.10.)
Library: `00_project/knowledge/client-work-library/`
1. `01-agency-task-delegation-ux/`
2. `02-ai-agent-work-visibility/`
3. `03-work-data-model/`
4. `04-dashboard-visualization/`
5. `research/05-inventory-741.md` (where our data lives today)

## Security fix (13.10., Martin's go)
The inventory found that the `report_feedback` SELECT policy was `using (true)`. So every logged-in client could read the feedback of all 5 clients (351 rows). Migration `report_feedback_select_own_only` changed it to `is_admin() or client_id = my_client_id()`. Tested: the test client sees 0 foreign rows, Suriya sees her 57 rows and 0 foreign rows, admin and delivery see 351. The report pages only insert (anon), so they still work. Open point: anon INSERT accepts any `client_id` (`with check true`). Harden this when the report feedback moves into the new task model.

## Changes from the research (2026-10-13, for Martin's design check)
Library: `00_project/knowledge/client-work-library/INDEX.md`. Rule numbers below are area-rule, for example 02-8.
1. **Two people fields per task.** "Accountable" is always a person (Martin or the team). "Doer" can be a person, an agent, Google or the client (01-7, 02-2, 03-12, 03-13).
2. **An agent never sets "done".** It sets "needs check". A person sets "done", and only with a proof link (02-8, 03-9, 04-21, 04-24).
3. **One list, many views.** Admin, team, client and Command Center read the same rows. There are no copies (01-25, 04-9).
4. **Exceptions first.** The start screen shows 5 counters and at most 12 rows. Clients that need nothing are one collapsed line. The activity feed moves to its own area (04-1, 04-5).
5. **Health per client = word + colour + reason + owner + next action.** Signals propose the colour, and Martin confirms it weekly. "No data" is its own state, never green (01-18, 01-20, 04-2).
6. **"Waiting on client" is its own lane with age.** In the client view the same lane is "What we need from you", with the effect of a delay (01-15, 04-13, 04-23).
7. **Client view = 4 blocks.** Where we stand, what is next, what we need from you, who to ask. Results with proof come below. Internal notes, hours and agent steps stay hidden (04-12, 04-14).
8. **Outcomes are their own records.** Each has the result in client words, a before and after value, "confirmed" or "assumed", proof, and time and cost. Missing time is shown as "not recorded", never estimated (02-11, 03-23).
9. **Current state in tables plus one append-only log.** Every producer (grill, sessions, registry, night shift, approvals) writes with a unique key, so repeated runs change nothing (03-25 to 03-27).
10. **Hidden work becomes visible.** 98 report change requests and 8 access help requests go into an "intake" lane. Dinakar and Tantri need portal accounts for "My tasks" (inventory).

## Design (prototype 13.10.)
- Data model: `data-model.md` (10 tables, status set, producers, security, migration path).
- Prototype: `prototype/index.html` (run: launch config `work-view-proto`, port 8988). Real data from 13.10.: Morning Grill tasks t01–t23, portal counts.
  - **Heute (admin):** 5 counters (waits for you 8, check 4, team waits for you 2, waits for client or Google 4, agents working 3), "do first" list (max 12), clients with health bands.
  - **Kunde (Praxis Suriya):** quarter goal and goal numbers, phases P0–P6 (the 13 weeks become milestones), one task list with filters Martin / Team / Agent / Kunde, results with proof, "waits on Coralie" with age, decisions, client rules, history.
  - **Meine Aufgaben (team):** own tasks across all clients, handoff note, "done means", documents, "report done" only with a proof link.
  - **Kundenansicht (Coralie):** 4 blocks, results with proof, max. 2 Martin figures (hello, point). Slop check 5/5.
- Tested in Chrome at 1440 px and 390 px (no horizontal scroll). Rules tested: "done" without proof is blocked, and the team cannot report done without a link.
- Screenshots: `prototype/screenshots/` (8).
