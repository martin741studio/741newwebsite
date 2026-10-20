# Client work view: data model proposal (v1, 2026-10-13)

Status: proposal only. Nothing is applied. A migration needs Martin's go.
Basis: `knowledge/client-work-library/03-work-data-model/extract.md` (rules 1–30, sketch F), inventory `research/05-inventory-741.md`, Martin's decisions in `brief.md`.

## Principles
1. **One list for all work.** Tasks, deliverables, milestones and approvals are rows in one `work_item` table. Every view reads this table: admin, team, client and Command Center (rules 01-25, 04-9).
2. **One accountable person and one doer.** `accountable` is always Martin or a team member. `doer` can be a person, an agent, a script or the client (rules 02-2, 03-12, 03-13).
3. **Agent "done" is not done.** An agent can only set `needs_check`. A person sets `done` and links the proof. `verified_by` is always a person (rules 02-8, 03-9, 04-21).
4. **No "done" without proof.** `done` needs at least one `evidence_link` with relation `proves`. Otherwise the row stays `needs_check` (rules 04-24, 02-15).
5. **Current state in tables, history in one append-only log.** We do not use full event sourcing (rule 03-25).
6. **Every producer writes idempotently.** The grill, the night shift, the registry sync and the approval RPCs write with a unique `(source, source_id)` and upsert. A run can repeat and change nothing (rules 03-26, 03-27).
7. **Client view = same rows, filtered.** Internal fields live in an admin-only side table. The client sees a `security_invoker` view (rules 03-29, 04-11, 04-14).

## Tables

| Table | Key columns | Notes |
| --- | --- | --- |
| `actor` | id, kind (`admin`, `team`, `agent`, `script`, `client`), name, user_id (null for agents), owner_actor_id (human owner of an agent), allowed_clients[], active | One table for every doer. Seed: Martin, Dinakar, Tantri, Gayo, Defina, Rias, 741 agents (grill, night shift, chat sessions), one client actor for each client. |
| `client_goal` | id, client_id, title, metric_key, baseline, target, due_on, source_link, status (`proposed`, `agreed`) | From `morning-grill-goals.json`. The quarter goal and the goal numbers. |
| `phase` | id, client_id, code (`P0`–`P6`), label, planned_from, planned_to, status | The 13 weeks become phases or milestones (Martin's decision). Labels come from the architecture map: Prospect, Onboarding, Audit, Un-Burning, Build-up, Content, Proof + Quarter. |
| `work_item` | id, client_id, phase_id, parent_id, goal_id, type (`task`, `deliverable`, `approval`, `client_todo`, `intake`), title, definition_of_done, status, status_reason, waiting_on (`client`, `martin`, `team`, `google`, `external`), accountable_id, doer_id, due_on, next_action, priority, visibility (`internal`, `client`), done_by, done_at, verified_by, verified_at, resolution, source, source_id, created_by, created_at, updated_at | Replaces `tasks` (390 rows become phase or `task` rows with source `template`). Unique `(source, source_id)`. |
| `work_item_internal` | work_item_id, notes, minutes_spent, agent_cost_eur, risk | Admin only. Holds time and cost (Martin's decision on outcome). |
| `work_dependency` | blocker_id, blocked_id | Shows "blocked by" without free text. Example: Dinakar's speed work waits for the WordPress role. |
| `work_event` | id (sequence), client_id, work_item_id, actor_id, type (`created`, `status`, `handoff`, `comment`, `proof`, `decision`), from_status, to_status, from_actor, to_actor, note, run_id, idempotency_key unique, at | Append-only. Replaces `activity_log` for new entries. Client-facing lines carry `visibility = client`. |
| `agent_run` | id, client_id, work_item_id, agent_id, delegated_by, state (`running`, `needs_input`, `needs_approval`, `stale`, `finished`, `failed`), summary, session_ref, started_at, ended_at, cost_eur | One row per chat session or scheduled run. Links to `_run.json` and the chat id. |
| `evidence_link` | id, client_id, work_item_id, run_id, outcome_id, kind (`page`, `file`, `drive`, `screenshot`, `report`, `run`, `chat`, `commit`), relation (`used`, `produced`, `proves`), label, url, captured_at, content_hash, visibility | Sources and proof. One field for what is spread over 5 places today. |
| `outcome` | id, client_id, work_item_id, goal_id, client_text, metric_key, value_before, value_after, measured_at, confirmed (`confirmed`, `assumed`), verified_by, visibility | "What was worked out": a result in client words plus the effect on a goal number. |

**Kept as they are:**
- `approval_items` and `approval_decisions` (the client decision log). Each approval item gets one `work_item` of type `approval`, linked by `source = 'approval'`.
- `client_reports` becomes proof (`evidence_link` kind `report`).
- `report_feedback` change requests and `access_grants` with `hilfe_angefragt` become `intake` and `client_todo` rows.

## Status set (one word list everywhere)
| Status | Category | Who sets it |
| --- | --- | --- |
| `intake` | planned | anyone (new request, not yet triaged) |
| `planned` | planned | Martin or the grill |
| `in_progress` | active | doer |
| `waiting` + `waiting_on` | active | doer (with reason and age) |
| `needs_check` | active | agent or team (draft or result ready) |
| `done` | done | person only, with proof |
| `dropped` | closed | Martin, with reason |

## Producers and how they write
| Producer | Writes | Key |
| --- | --- | --- |
| Morning Grill (step 9) | `work_item` (tasks), `work_event` (handoff), `agent_run` | source `grill`, source_id = task id (for example `2026-10-13/t19`) |
| Chat sessions and agents | `agent_run`, `evidence_link` (produced), status `needs_check` | source `session`, source_id = chat id |
| Workflow registry sync (`_run.json`) | `agent_run`, `evidence_link` (Drive link), `outcome` (draft, `assumed`) | source `registry`, source_id = run id |
| Approval RPCs | `work_item` type `approval` | source `approval`, source_id = item id |
| Night shift | `work_item` (drafts), `evidence_link` | source `nightshift` |
| Team in the portal | status, minutes_spent, proof link | through RPC `work_update` (checks the actor) |
| Client in the portal | `client_todo` done, comments | through RPC (own client only) |

## Security
- RLS on every table, with one policy per operation. A client sees rows with `visibility = 'client'` of their own client only, through the view `client_work_view`.
- A team member sees and updates only rows where they are the accountable person or the doer (`work_update` RPC).
- `work_item_internal`, `agent_run` and `evidence_link` with `visibility = internal` are admin only.
- pgTAP-style tests in the same pattern as `client-approval-workflow/portal/04-rls-tests.sql`. A dry run with rollback comes first.

## Open UX gap (found 14.10. evening, Martin)
The admin task card's "Erledigt" button forces a Nachweis-Link (URL) field before it will submit. The DB does not require a URL: `work_evidence.url` is nullable, and the `work_items_done_proof_check` / `work_items_guard` triggers only need one evidence row with `relation in ('proves','produced')` — `kind`, `relation` and `label` are enough. For decision-type tasks (a date, an A/B choice — nothing to link) the frontend should let "Erledigt" submit with a label only (e.g. "decided live 14.10."), no URL required. Martin's call (14.10.): exempt decision tasks from the link requirement rather than keep forcing one. Not built yet — the admin UI still has the hard requirement; whoever next touches the task-card component should drop it for `type = 'task'` rows without a deliverable link, or add a task subtype distinguishing "decision" from "deliverable".

## Migration path
1. Create the tables and seed `actor` and `phase` from the architecture map.
2. Copy `tasks` into `work_item` (source `template`), with the old `owner 741 → accountable Martin`, `kunde → doer client`. Keep `tasks` read-only until the switch.
3. The Morning Grill writes into `work_item` instead of `tasks.json`.
4. The admin views go live, then "My tasks" for the team, then the client view (Martin's order).
