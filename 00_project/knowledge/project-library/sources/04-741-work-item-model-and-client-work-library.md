# Work-item model and client-work library: findings for a Project Manager agent

Read on 2026-11-03. Library fetch date: 2026-10-13.

Files read in full:
- /Users/martindrendel/741website/00_project/knowledge/client-work-library/INDEX.md.
- /Users/martindrendel/741website/00_project/knowledge/client-work-library/01-agency-task-delegation-ux/extract.md (short name: lib-01).
- /Users/martindrendel/741website/00_project/knowledge/client-work-library/02-ai-agent-work-visibility/extract.md (lib-02).
- /Users/martindrendel/741website/00_project/knowledge/client-work-library/03-work-data-model/extract.md (lib-03).
- /Users/martindrendel/741website/00_project/knowledge/client-work-library/04-dashboard-visualization/extract.md (lib-04).
- /Users/martindrendel/741website/00_project/client-work-visibility/brief.md.
- /Users/martindrendel/741website/00_project/client-work-visibility/data-model.md.
- /Users/martindrendel/741website/00_project/client-work-visibility/research/05-inventory-741.md.
- /Users/martindrendel/.claude/projects/-Users-martindrendel-741website/memory/client-work-view.md.

Status key: designed = only in brief.md or data-model.md. built = brief.md or memory says live on 13.10. research = library extract only, not adopted in brief.md or data-model.md. No live state was re-checked on 2026-11-03.

## Status machine and "done"
- **Agents may set only needs_check; a person alone sets done.** Src: brief.md, 'an agent "done" becomes needs_check'. Status: built
- **A row reaches done only with an evidence link that proves the result.** Src: data-model.md, "needs at least one evidence_link with relation proves". Status: built
- Seven statuses cover all work: intake, planned, in_progress, waiting, needs_check, done, dropped. Src: data-model.md, "Status set (one word list everywhere)". Status: designed
- Each status belongs to a fixed category such as planned, active, done or closed. Src: lib-03, "Map every status to a small fixed category set". Status: designed
- Waiting carries the actor who must act and the reason. Src: lib-03, "Store the reason and the actor who must act". Status: designed
- "Needs input" and "needs approval" stay separate states, because an answer and a yes-or-no differ. Src: lib-02, "A question needs an answer, and an action needs a yes or no". Status: research (data-model merges them)
- An agent run turns stale after 30 minutes without activity. Src: lib-03, "A session with no activity for 30 minutes becomes stale". Status: designed
- Done and verified are separate fields, and only a person sets verified. Src: lib-03, "Store done_by, done_at, verified_by and verified_at as four separate fields". Status: designed

## Actors and delegation
- One actor table holds people, agents, scripts and clients, and each agent names a human owner. Src: data-model.md, "One table for every doer". Status: built
- **Every work item has one accountable human, never an agent.** Src: brief.md, '"Accountable" is always a person'. Status: designed
- A separate doer field names a person, an agent, Google or the client. Src: brief.md, '"Doer" can be a person, an agent, Google or the client'. Status: designed
- Each agent actor lists its allowed clients and allowed actions, so its scope stays limited. Src: lib-03, "Store the allowed clients and allowed actions on each agent actor". Status: designed (data-model holds allowed_clients only)
- Each handoff writes one event row, and the old owner stays on record. Src: lib-03, "Record each handoff as an event row". Status: designed
- Agents draft, and humans publish to the client. Src: lib-03, "Agents draft. Humans publish to the client". Status: designed
- Agents never change an owner or a date without a human approval. Src: lib-01, "Do not let agents change owners or dates without approval". Status: research
- The definition of done is written on the task before an agent starts. Src: lib-02, "Write the definition of done on the task before the agent starts". Status: designed
- An agent logs typed steps: action with result, question, final answer and error. Src: lib-02, "Log typed steps: action with result, question, final answer, and error". Status: research

## Waiting, blockers and age
- A blocked task must show who it waits on. Src: lib-01, "A blocked task must show who it waits on". Status: designed
- Dependencies live in an edge table of blocker and blocked rows, not in free text. Src: lib-03, "Store dependencies as rows in an edge table". Status: designed
- Blockers stay visible until they close, and each shows its age in days. Src: lib-04, "Keep blockers visible until they close, and show their age". Status: research
- A health update counts as missing when it is one cycle plus 3 days late. Src: lib-01, 'shows "Update Missing" when the update is one cycle plus 3 days late'. Status: research
- Every waiting or open item shows its age. Src: lib-01, "Show the age of every waiting or open item". Status: designed
- A snooze hides an item until a set date or new activity. Src: lib-01, "Let people snooze an item or set a reminder, with a return date". Status: research

## Evidence and outcomes
- **Outcomes are their own records, with a result in client words and a confirmed or assumed label.** Src: brief.md, "Outcomes are their own records". Status: built (2 Suriya outcome rows; label not re-checked)
- Missing time shows as "not recorded", never as an estimate. Src: brief.md, 'Missing time is shown as "not recorded"'. Status: designed
- Each evidence link has one relation: used, produced or proves. Src: data-model.md, "relation (used, produced, proves)". Status: designed
- Each agent run links to its work item with a stable run ID and trace ID. Src: lib-03, "Link each agent run to its work item and its trace IDs". Status: designed
- Raw prompts and model text stay out of shared tables; the row keeps a summary and a link. Src: lib-03, "Keep prompts and raw model text out of the shared tables". Status: research
- A decision task may close with a label only, without a URL. Src: data-model.md, 'let "Erledigt" submit with a label only'. Status: designed (Martin's call on 14.10; the admin UI still forces a URL)

## Admin view and client health
- The admin start screen shows five counters and at most 12 rows, with exceptions first. Src: brief.md, "The start screen shows 5 counters and at most 12 rows". Status: built
- Clients that need nothing collapse into one line. Src: brief.md, "Clients that need nothing are one collapsed line". Status: built
- All views read the same rows, and no task goes to a second list. Src: lib-04, "Never copy tasks into a second list". Status: built
- Each list on the start screen caps at about 12 items. Src: lib-04, "Show a maximum of about 12 items per list". Status: built
- Each client health shows colour, word and reason, and "No data" is never green. Src: brief.md, '"No data" is its own state, never green'. Status: built
- Client colour comes from rules on signals, not from a person, which differs from lib-01 rule 20. Src: brief.md, "Fully automatic from signals. No manual confirmation". Status: built
- Workload per person is shown against a capacity limit, using real hours. Src: lib-01, "Plan from real hours, not 40 per week". Status: research

## Client view and cadence
- **The client view reads the same rows, filtered. Internal fields sit in an admin-only side table.** Src: data-model.md, "Client view = same rows, filtered". Status: designed
- The client view opens with four blocks: where we are, what is next, what we need from you, who to ask. Src: lib-04, "Show four blocks first: where we are, what is next". Status: designed
- Internal notes, estimates, hours, margins and per-task assignees stay hidden from the client. Src: lib-04, "Hide internal notes, estimates, per-task assignees, hours, margins". Status: designed
- The client gets a link on a fixed weekday, even when nothing changed. Src: lib-04, "Send the client update on a fixed weekday, also when nothing changed". Status: research
- Internal health reviews run weekly, and the results report goes out monthly. Src: lib-04, "Review internal health weekly and send the results report monthly". Status: research (the weekly confirm no longer applies after the automatic colour decision)

## What is live today vs. only designed
- Live (brief.md, 13.10): the work tables, 21 actors, the Morning Grill writing into work_items, and the Kundenarbeit module with admin counters.
- Live (brief.md, 13.10): "Erledigt" without proof is refused, and an agent "done" becomes needs_check.
- Live (brief.md, 13.10): 2 Suriya outcome rows, and an intake lane with 98 change requests and 8 access requests.
- Designed only: the client view (four blocks, Bali Healing English pilot), team logins for Dinakar and Tantri, and the decision-task exemption from the URL.
- Research only: typed agent steps, workload capacity, the weekly internal review, and the snooze and blocker-age rules. None of them appears in data-model.md or brief.md.

## Gaps for a Project Manager (nothing covers this)
- Escalation: no source says who chases a missed due date, or when a waiting item goes to Martin.
- Mixed owner list: no source covers people, agents and the client in one list across all clients (INDEX.md).
- Handover: no source covers a handover note to a trial Upwork partner or a new team member, or a check of their "done".
