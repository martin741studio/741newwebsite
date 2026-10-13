# Extract: 03 Work data model, rules for the client work view of 741 Studio

Scope: data model and storage for work items, delegation, provenance and outcomes in the client portal of 741 Studio (Supabase/Postgres, RLS per client).
Sources: 16 files in `sources/`. Fetch date: 2026-10-13. Dated sources: 2026-07-16 to 2026-09-11. All other sources are living docs.
Today the portal has a fixed 13-week `tasks` table (client_id, week, title, owner 741/kunde, done) and an `activity_log` feed. The rules below replace that model step by step.

## A. Work items and structure

1. **Use one work-item table with a type column.**
Asana keeps tasks, milestones and approvals in one Task object with a subtype field. Use the types task, deliverable, milestone, approval and decision. A milestone marks a date and has no start date.
Sources: asana-tasks-api, github-sub-issues. Strength: official doc

2. **Build the hierarchy with a parent_id, not with fixed weeks.**
GitHub gives each issue one parent and many sub-issues. Keep `week` only as a planning field on the item. A deliverable can then hold its tasks, and a milestone can hold its deliverables.
Sources: github-sub-issues, asana-tasks-api. Strength: 2+ sources

3. **Compute progress from child items. Do not type it by hand.**
GitHub returns total, completed and percent_completed for the children of each issue. Calculate these values in a view. Then the number in the portal always matches the real items.
Sources: github-sub-issues. Strength: official doc

4. **Store dependencies as rows in an edge table.**
GitHub and Asana store "blocked by" and "dependents" as relations between two items, not as text. Use one row per pair (blocker, blocked). A view can then show what blocks each item.
Sources: github-issue-dependencies, asana-tasks-api. Strength: 2+ sources

5. **Give approvals their own result values.**
Asana approvals use pending, approved, changes_requested and rejected. Only pending counts as open. Use this set for every client sign-off, for example a text draft or a page design.
Sources: asana-tasks-api. Strength: official doc

## B. Status state machine

6. **Map every status to a small fixed category set.**
Use four categories. Planned and active hold open work. Done and failed hold closed work. Schema.org uses the same four-part core for actions. Linear also groups custom statuses under fixed types such as "started".
Sources: schema-org-action, linear-agent-best-practices. Strength: 2+ sources

7. **Keep "blocked" and "waiting on client" as active statuses with a reason field.**
Linear has an awaitingInput state when an agent needs a human answer. Store the reason and the actor who must act. Then the portal can list all items that wait on the client.
Sources: linear-agent-interaction. Strength: 1 source

8. **Separate "done" from "verified".**
Jira keeps agent output private until a human reviews and shares it. Asana records completed_by and completed_at. Store done_by, done_at, verified_by and verified_at as four separate fields.
Sources: atlassian-jira-agents-work-items, asana-tasks-api. Strength: 2+ sources

9. **Let only a human set "verified" or "approved".**
An agent can set an item to "needs review". A human then sets the final state. This rule follows the review step in Jira and the triage rule in Linear.
Sources: atlassian-jira-agents-work-items, linear-agent-best-practices. Strength: 2+ sources

10. **Store a close reason next to the final status.**
Asana stores rejected and changes_requested as results. MADR stores rejected, deprecated and superseded. Use one `resolution` field, for example completed, canceled, duplicate or replaced.
Sources: asana-tasks-api, madr-template. Strength: 2+ sources

11. **Derive the state of an agent run from its last event.**
Linear sets the session state from the last activity of the agent. A session with no activity for 30 minutes becomes stale. Use the same rule for agent runs in the portal.
Sources: linear-agent-interaction, linear-agent-best-practices. Strength: official doc

## C. Ownership, delegation and agents

12. **Give every work item one accountable human.**
In Linear the human stays on the issue when an agent gets the work. In Jira the person who triggers the agent controls it. The accountable person is Martin or a team member, never an agent.
Sources: linear-agents-in-linear, atlassian-jira-agents-work-items. Strength: 2+ sources

13. **Store the doer in a separate delegate field.**
Linear has Issue.delegate next to the assignee. The delegate can be a team member, an agent, a script or the client. Then the portal can filter "work done by agents" without a second list.
Sources: linear-agents-in-linear, linear-agent-best-practices. Strength: 2+ sources

14. **Use one actor table for humans, agents, scripts and clients.**
Linear treats agents as workspace users. Schema.org uses an agent and participant field on each action. One actor table with a `kind` column lets every field point to any doer.
Sources: linear-agents-in-linear, schema-org-action. Strength: 2+ sources

15. **Record each handoff as an event row. Do not overwrite the old owner.**
Linear opens a new session on each delegation. Jira starts an agent on a workflow transition. Write one event with from_actor, to_actor, instructions and time.
Sources: linear-agent-interaction, atlassian-jira-agents-work-items. Strength: 2+ sources

16. **Agents draft. Humans publish to the client.**
Jira shows agent output only to the trigger person until that person shares it. Linear keeps automation-delegated issues in triage for a human. Mark agent output as internal until a human releases it.
Sources: atlassian-jira-agents-work-items, linear-agent-best-practices. Strength: 2+ sources

17. **Limit each agent to a defined scope.**
Linear admins choose the teams that each agent can access. Jira admins switch on each agent per surface. Store the allowed clients and allowed actions on each agent actor.
Sources: linear-agents-in-linear, atlassian-jira-agents-work-items. Strength: 2+ sources

## D. Evidence, outcomes and decisions

18. **Store links as typed rows with a label, a URL and a kind.**
Linear stores external links as label and URL pairs, and each URL is unique. Schema.org separates the object, the instrument and the result of an action. Use kinds such as page, file, screenshot, report and run.
Sources: linear-agent-interaction, schema-org-action. Strength: 2+ sources

19. **Mark each link as "used" or "produced".**
AgentTrails shows that a flat log hides which step used or made which artifact. Two edge types (used, produced) make the evidence chain visible. A third type, "proves", links evidence to an outcome.
Sources: agenttrails-provenance, novafabric-run-evidence. Strength: 2+ sources

20. **Link each agent run to its work item and its trace IDs.**
OpenTelemetry models an agent run as invoke_agent and execute_tool spans. Store trace_id and conversation_id on the run row. Do not copy the full trace into the portal.
Sources: otel-genai-conventions-2026-status, novafabric-run-evidence. Strength: 2+ sources

21. **Keep prompts and raw model text out of the shared tables.**
OpenTelemetry does not capture prompt and output text by default because of privacy. Store a short human-readable summary and a link to the raw log. Keep raw logs in internal storage only.
Sources: otel-genai-conventions-2026-status. Strength: 1 source

22. **Store a content hash for evidence that a client can dispute.**
NovaFabric seals each run with hashes and a signature. A small agency needs less. A SHA-256 hash and a capture time on each screenshot or report file are enough.
Sources: novafabric-run-evidence. Strength: 1 source

23. **Store outcomes as separate records with a metric, a before value and an after value.**
Schema.org keeps the result of an action apart from the action. An outcome row links to the work items that caused it and to a client goal. It also records who checked the numbers.
Sources: schema-org-action, asana-tasks-api. Strength: 2+ sources

24. **Write decisions as fixed records with a status and a "superseded by" link.**
MADR stores context, options, outcome, consequences and confirmation. It also names the decision-makers. It lists the people it consulted and the people it informed. Do not edit an accepted decision. Write a new one that supersedes it.
Sources: madr-template. Strength: official doc

## E. Storage, audit, sync and security

25. **Keep current state in normal tables plus one append-only event table. Do not use full event sourcing.**
Linear rebuilds agent history from fixed activities, not from editable comments. The event table gives the audit trail. The normal tables give fast reads for the portal.
Sources: linear-agent-best-practices, linear-agent-interaction. Strength: 2+ sources

26. **Make every producer write with an idempotency key and an upsert.**
Build the key from source, event type and source event ID. Postgres ON CONFLICT gives an atomic insert or update, also under concurrency. Put a unique constraint on the key.
Sources: datamagnet-webhook-idempotency, postgresql-insert-on-conflict. Strength: 2+ sources

27. **Give each row from an outside system a stable external_source and external_id.**
Asana stores an external gid per task, and tools address the task by that ID. Use a unique pair (external_source, external_id). A script can then run twice and change nothing.
Sources: asana-tasks-api, datamagnet-webhook-idempotency. Strength: 2+ sources

28. **Enable RLS on every table and write one policy per operation.**
Revoke default grants. Name the role in each policy. Index client_id and wrap auth.uid() in a select. Keep roles in app_metadata, not in user_metadata.
Sources: supabase-rls. Strength: official doc

29. **Put internal-only fields in a separate table. Do not use column grants.**
Supabase does not recommend column privileges for most users, and they break "select *". Store internal notes, cost and risk in a side table with an admin-only policy. Expose client views only with security_invoker = true.
Sources: supabase-column-level-security, supabase-rls. Strength: 2+ sources

30. **Run agents and scripts on the server key, and test every policy.**
The secret key bypasses RLS, so it must stay on the server. Agents must still write the actor and the idempotency key on each row. Write pgTAP tests for allowed and denied access per role.
Sources: supabase-rls. Strength: official doc

## F. Draft schema sketch

Proposal only. Names and key columns, no SQL. `client_id` is on every client table for RLS.

| Table | Key columns | Notes |
|---|---|---|
| `actor` | id, kind (admin, team, agent, script, client), display_name, owner_actor_id, allowed_clients, active | One table for all doers (rules 13, 14, 17). Agents point to a human owner. |
| `goal` | id, client_id, title, metric_key, baseline, target, due_on, owner_actor_id, visibility | Client goal or KPI (rule 23). |
| `work_item` | id, client_id, type, parent_id, goal_id, title, status, status_category, status_reason, resolution, accountable_actor_id, delegate_actor_id, waiting_on_actor_id, week, due_on, done_by, done_at, verified_by, verified_at, visibility, external_source, external_id, created_by, created_at, updated_at | Replaces `tasks` (rules 1 to 13, 27). Old owner 741/kunde maps to accountable and delegate. |
| `work_item_internal` | work_item_id, internal_notes, effort, cost, risk | Admin-only side table (rule 29). |
| `work_item_dependency` | blocker_id, blocked_id, created_by, created_at | Edge table (rule 4). |
| `work_event` | id (sequence), client_id, work_item_id, actor_id, event_type, from_status, to_status, from_actor_id, to_actor_id, payload, idempotency_key (unique), run_id, occurred_at | Append-only log for status changes, handoffs and comments (rules 15, 25, 26). Replaces `activity_log`. |
| `agent_run` | id, client_id, work_item_id, agent_actor_id, delegated_by, state, summary, trace_id, conversation_id, started_at, ended_at | One row per agent session (rules 11, 20, 21). |
| `evidence_link` | id, client_id, work_item_id, run_id, outcome_id, decision_id, kind, relation (used, produced, proves), label, url, content_hash, captured_at, visibility, created_by | Sources and proof (rules 18, 19, 22). |
| `outcome` | id, client_id, goal_id, work_item_id, summary, metric_key, value_before, value_after, measured_at, verified_by, visibility | What the work achieved (rule 23). |
| `decision` | id, client_id, number, title, status, context, options, outcome, consequences, decided_by, consulted, informed, supersedes_id, decided_at, work_item_id | Decision record (rule 24). |
| `client_work_view` | view with security_invoker = true | Client-safe columns only (rule 29). |

## Gaps and warnings

- No dated source after 2026-07-13 compares event sourcing with CRUD. All found articles were older and were dropped. Rule 25 rests on product docs and on inference.
- No current official source covers RACI. MADR "consulted" and "informed" is the closest match.
- No source covers PSA models for time, budget or billing. Area 03 does not include time tracking.
- The Linear doc on status categories returned 404. Rule 6 uses schema.org and the Linear agent guide instead.
- The OpenTelemetry GenAI conventions are still at Development status, with no tagged release. Attribute names can change. Store only trace IDs.
- The Linear agent APIs are a Developer Preview. Asana agent assignment is early access. Jira agent credits start on 3 December 2026.
- AgentTrails and NovaFabric are research prototypes. Use their ideas (edges, hashes), not their full systems.
- The Asana Tasks page was too large to read in full. The assignee and custom_fields parts were not checked.
- Dropped for date: Dash0 OTel guide (only "last updated" date), kontext.security (published 2026-05-09), appmaster audit article (2025), Asana agent forum post (2026-05-28), Jira agents announcement (2026-04-27), GitHub issue fields GA (2026-07-02), hidekazu ADR guide (2026-05-08), winningwithai checklist (dates conflict), webhook-architecture.com (no date).
- Supabase now calls the service role key the "secret key". Check key names in the portal code before a change.
