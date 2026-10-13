# Client work view: brief (grill-me, 2026-10-13)

Status: research started on 13.10. (4 outside areas plus an inventory of our own data). There is no design yet and nothing is built.

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

## Research (in progress)
Library: `00_project/knowledge/client-work-library/`
1. `01-agency-task-delegation-ux/`
2. `02-ai-agent-work-visibility/`
3. `03-work-data-model/`
4. `04-dashboard-visualization/`
5. `research/05-inventory-741.md` (where our data lives today)

## Security fix (13.10., Martin's go)
The inventory found that the `report_feedback` SELECT policy was `using (true)`. So every logged-in client could read the feedback of all 5 clients (351 rows). Migration `report_feedback_select_own_only` changed it to `is_admin() or client_id = my_client_id()`. Tested: the test client sees 0 foreign rows, Suriya sees her 57 rows and 0 foreign rows, admin and delivery see 351. The report pages only insert (anon), so they still work. Open point: anon INSERT accepts any `client_id` (`with check true`). Harden this when the report feedback moves into the new task model.
