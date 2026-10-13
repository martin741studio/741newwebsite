# 05 · Inventory: where the work data of 741 lives today

Status: read-only inventory, 2026-10-13. Nothing was changed, created in the database or sent.
Goal of the design: one view per client with (a) the task list, (b) the delegation list, (c) links to sources and proof, (d) the outcome.
Counts are aggregates. No personal data, no message bodies and no secrets were read. `app_secrets` and `client_credentials` were not opened.

## 1. Summary

1. Portal `tasks` (390 rows) is a fixed 13-week template copy. It has no due date, no proof link, no result and no note.
2. `tasks.owner` has only two values: `741` (315) and `kunde` (75). Team members and AI agents do not exist as owners.
3. Dinakar and Tantri are not in the portal at all. `team_members` holds Gayo, Rias and Farzana (inactive). Defina is a `delivery` profile.
4. The real daily work lives in chat transcripts, git commits and `_run.json` files. The portal does not see it. Suriya shows "last activity 21.09." while the chats show daily work.
5. The Morning Grill `tasks.json` (23 tasks, 13.10.) is the only place with real owners (Martin, Dinakar, Tantri, Gayo, agent, external). It exists for one day only and lives in a local folder and a JSON snapshot.
6. Outcomes (d) are spread over 46 `_run.json` notes, the registry (47 runs), `activity_log` (117 rows, free text) and night-shift `REVIEW.md` files. No source links an outcome to a task.
7. Proof links (c) have no common field. In `registry.json`, the customer list has a Drive link in 6 of 21 rows, the run list in 10 of 47 rows.
8. Client names differ across sources (for example "Naturheilpraxis Daniela Dumann", "Daniela Dumann", "Dumann"). There is no shared client key outside Supabase `clients.id`.
9. Approval data (`approval_items`, `approval_decisions`) is the best-built model (versions, actor, go, due date). Only Suriya (5 items) and the test client use it.
10. A security gap exists: the `report_feedback` SELECT policy is `using=true` for every logged-in user. A client can read the feedback rows of other clients.

## 2. Data sources table

### 2.1 Supabase `741-portal` (galjmtozcgxcwtzkzbpi)

RLS is on for all tables. "Client sees" means the policy `client_id = my_client_id()`.

| Source | What it holds (key columns) | Rows / per client | Who writes | Who sees (RLS) | Freshness | Reuse |
|---|---|---|---|---|---|---|
| `tasks` | 13-week program tasks: `client_id, week, track (A–D or null), module, title, owner (741/kunde), status (offen/erledigt), completed_at, sort` | 390. Hüwel 30/44 done, Suriya 22/44, Dumann 20/44, Brasse 11/44, Rabenmütter 11/30, Johni 9/44, Bali 0/44, Stürzl 0/52, Test 0/44, Kamil 0 | Admin (Martin, scripts). Client can tick only `owner='kunde'` | Client reads own rows. Delivery reads all | Last `completed_at` 2026-10-09 | Yes, as the milestone layer (13 weeks = phases). Not as the real task list |
| `template_tasks` | Template for `tasks`: `week, track, module, title, owner, lang` | 88 (741: 70, kunde: 18) | Admin | Every logged-in user | Static | Yes, as the phase or milestone template |
| `programs` | `client_id, start_date, end_date, status` | 9 (7 running, 2 pending). Kamil has none | Admin | Client own, delivery all | Set at start | Yes (program week). Start dates conflict with memory (see 4) |
| `onboarding_steps` | 6 steps per client: `step_no, title, status, completed_at, kind` | 54 (30 erledigt, 24 offen) | Admin. Client updates own step | Client own | Last 2026-09-25 | Yes (client-owned tasks) |
| `access_grants` | Access per platform: `platform, method, required, status (erteilt/ausstehend/hilfe_angefragt), guide` | 69 (32 / 29 / 8) | Admin. Client marks granted | Client own | Last 2026-10-07 | Yes ("what we need from you") |
| `activity_log` | Free-text work log: `client_id, action, metric, logged_at` | 117. Hüwel 43, Suriya 30, Dumann 16, Brasse 14, Johni 12, Bali 2, others 0 | Admin scripts and chats (manual) | Client own | Last 2026-10-09 | Partly. Good client-facing "done" text. No link to a task, no owner, no proof field |
| `approval_items` | Client decisions: `code, kind, area, title, why, why_source, variants, recommended_key, status, chosen_key, version, due_at, go_at, go_by, risk_class, hwg_checked` | 10 (Suriya 5, Test 5). Status draft 5, ready 2, go 2, change 1 | Admin via RPCs `approval_release/decide/go/undo` | Client own, not draft or withdrawn | 2026-10-13 | Yes. Pattern for task versions, due dates and "go" |
| `approval_decisions` | Decision log: `item_id, item_version, actor_name, kind, action, variant_key, note` | 16 (all test client) | RPC `approval_decide` | Client own, admin and delivery all | 2026-10-13 | Yes. Pattern for an audit trail |
| `client_approval_settings` | Approver, auto-approve consent, digest hour | 2 | Admin | Admin | 13.10. | Yes |
| `page_change_requests` | `page, description, status` | 0 | Admin | Client own | Empty | Probably drop or merge into approvals |
| `client_reports` | Report files: `title, period_label, storage_path` | 33 (Dumann 6, Suriya 6, Bali 5, Hüwel 4, Rabenmütter 4, Brasse 3, Stürzl 2, Kamil 2, Johni 1) | Admin | Client own | Last 2026-10-09 | Yes, as proof links |
| `report_feedback` | Client verdict per report section: `report_slug, section_key, verdict (freigegeben/aenderung), comment, author` | 351 (Brasse 158, Hüwel 70, Suriya 57, Dumann 50, Rabenmütter 16). 98 change requests | Client (anon and authenticated insert) | **All logged-in users (`using=true`)** | Last 2026-10-10 | Yes. 98 change requests are hidden tasks. Fix RLS first |
| `client_citations` | Listing per directory: `directory_id, status, listing_url, submitted_via, last_checked, nap_match` | 273 (planned 170, live 71, submitted 25, inconsistent 4, missing 3). Dumann 90, Hüwel 67, Brasse 57, Suriya 56, Stürzl 3 | Admin, Tantri work, scripts | Client own (RPC `client_set_citation_status`) | Last 2026-10-11 | Yes. `listing_url` is a ready proof link |
| `directories` | 90 directories (citation module) | 90 | Admin | – | Static | Yes (lookup) |
| `listing_emails` | Verify mails from directories: `client_slug, verify_link, handled, confirmed` | 28, all with `client_id` null | Inbox poller `reporting/listings-inbox-poller.mjs` | Admin only | Last 2026-09-15 | Yes, after the client key is filled |
| `scans` | Scan results: `scan_type (maps_service 14, ai_baseline 2, backlinks_manual 1, maps_baseline 1), report_key, data` | 18 (Suriya 10, Stürzl 8) | Scripts | Client own | Last 2026-10-01 | Yes, as proof for goal numbers |
| `visibility_prompts` / `visibility_results` | AI-visibility checks | 5 / 19 | Scripts | Not checked in detail | – | Later (goal numbers) |
| `materials` | Client uploads: `kind, label, storage_path, week` | 25 (Dumann 16, Suriya 9) | Client insert, admin | Client own | Last 2026-08-29 | Yes, as client inputs |
| `messages` | Portal chat client and 741 | 3 | Client and admin | Client own | – | Link only. Not a work source |
| `emails_log` | Sent template mails: `template, subject, sent_at, status` | 25 | Edge functions | Client own | Last 2026-10-12 | Yes, as a send log for client messages |
| `admin_notifications` | Event lines for the admin digest | 439 | Triggers (`queue_step_done`, `queue_grant_change`, `notify_report_feedback` …) | Admin | Current | Yes, as an event feed |
| `client_master_data` | Locked master data (NAP, services, boundaries, open points) | 1 (Suriya) | Admin | Client read only | – | Yes (source of truth per client) |
| `clients` / `profiles` | Customer list (`name, status, mode, lang, stammdaten_sheet_url`). Profiles: role client 9, admin 3 (incl. "Standup Bot"), delivery 1 (Defina) | 10 / 13 | Admin, `provision_client` | – | – | Yes. `clients.id` is the only stable client key |
| `team_members` | Team: `display_name, level, seat, weekly_hours_target, tools, seats` | 3: Gayo (manager), Rias (member), Farzana (inactive) | Manager | Self and manager | – | Yes, but the roster names Dinakar, Tantri and Defina, and they are not in it |
| `daily_plans` / `daily_reports` | Outreach plan and report per member per day: `intent, target_count, targets` / `hours_worked, blockers, progress, next_plan, messages_sent …` | 65 / 58 (Gayo 34/33, Rias 27/23, Farzana 4/2) | Team member via `submit_daily_plan/report` | Self and manager | Last 2026-10-12 | Yes. Pattern for "my tasks" and a done report. Outreach only, not per client |
| `outreach_accounts` (+ members) | LinkedIn accounts: `label, client_label, kind (client 5, 741 3)` | 8 / 8 | Manager | Members of the account | – | Yes, for client outreach work (me&you, Pauspapier) |
| `team_notes` | Notes per member and day | 0 | Manager | – | Empty | Yes (handoff note) |
| `grill_snapshots` | Command Center snapshot: `run_date, mode, data` (keys: cards, clients, tasks, walk, later, agents, waiting, line_741, sources, tiles) | 5, all 2026-10-13 | `publish_snapshot.py` | Admin only | 13.10. | Yes, short term. The `tasks` key is the v0 task list |
| `grill_answers` | Clicks on cards: `card_id, run_date, option, note` | 2 (option `own`) | Admin tab | Admin only | 13.10. | Yes (decision input) |
| `whiteboards` / `whiteboard_items` | Free canvas | 2 / 419 | Admin | Not checked | Last 2026-10-08 | No |
| `leads`, `site_form_submissions`, `subscriptions`, `campaigns`, `assistant_messages`, `daily_*_accounts` | Empty | 0 | – | – | – | Later |
| RPC `daily_standup()` | Per client: program week, onboarding, open access, help requests, open tasks of this week (owner 741 or kunde), overdue tasks | – | – | Admin only | Live | Yes. A ready per-client status query |

### 2.2 Local files and other sources

| Source | Where | What it holds | Who writes | Who sees | Freshness | Reuse |
|---|---|---|---|---|---|---|
| Workflow registry | `00_project/workflow-registry/registry.json` (+ `../cro-registry/registry.json`) | 14 workflows, customer list with `drive` and `local` (21 rows), 47 runs (`client, workflow, page, status, approved, last_run, drive, local, result, note`). Status: in Arbeit 19, freigegeben 12, fertig/Freigabe offen 10, Trockenlauf 5, Archiv 1 | `workflow_registry.py sync` (Stop hook after each turn), `approve` on Martin's word | Martin (local) | Each turn | Yes. Best list of workflow runs and approvals per client |
| `_run.json` per run | 46 files: Stürzl content 30, me&you content 10, Hüwel backlink, Marcel automation, 741 content, Suriya tracking, Morning Grill 2. Plus 6 in `00_project/prospects/` | `client, workflow, status, mode, last_run, page, result, drive, note` | Each workflow at checkpoints | Martin (local) | Per run | Yes. Best "outcome + proof link" record per run. Status words are not always standard (for example "Korrekturrunde fertig, Freigabe offen") |
| Overview Excel | `~/Desktop/Workflow-Uebersicht.xlsx` | Sheets: Übersicht (26 rows; columns Kunde, Typ + 14 workflow columns), Links (96 rows; Kunde, Workflow, Seite oder Lauf, Status, Freigabe von Martin, Letzter Lauf, Ordner Drive, Ordner lokal, Ergebnis, Notiz), Workflows (15 rows), Befehle (14 rows) | Built from the registry | Martin | 13.10. 11:31 | View only. Do not reuse as storage |
| Morning Grill state | `00_project/assets/morning-grill/state/` | `cards.json` (13 cards: 12 decided, 1 parked; fields id, client, priority, type, headline, evidence, options, recommended, deadline, status, answer, then), `bookmarks.json`, `carry-over.md`, `pulse.log`, `answers-cursor.json` | Morning Grill skill | Martin | 13.10. | Yes. Card format = decision record with evidence |
| Morning Grill run | `00_project/assets/morning-grill/2026-10-13/` | `tasks.json` (23 tasks: owner Martin 10, agent 8, external 2, Dinakar 1, Gayo 1, Tantri 1; status open 8, waiting 5, in_progress 4, done 4, drafted 2; fields id, owner, status, client, title, card, link, due), `plan.md` per client, `brief.json` (per client: today, fixed, watch, next, goal, phase, chat id), `snapshot.json`, `team-tasks-drafts.md`, `portal-reply-drafts.md`, `send-pack.md` | Morning Grill skill | Martin, Command Center tab | Daily | Yes. Closest to goals a, b and d. Needs a durable home |
| Client goal sheet | `00_project/morning-grill-goals.json` | One block per customer (12 blocks): status, phase, program dates, goal numbers, leading numbers, waiting_for, next_workflow, chat id | Morning Grill skill, Martin confirms | Martin | 13.10. | Yes (goal and phase per client) |
| Morning Grill spec | `00_project/morning-grill-workflow.md` §3, §8, §10, §12 | Source list S1–S13, routing table (agent, Dinakar, Tantri, Gayo, Martin, client), evening log per client, `logs/<client>.md` history | Spec | – | 13.10. | Yes. Routing table = draft delegation rules. `logs/` is still empty |
| Tracking data model | `00_project/tracking-workflow.md` §12 | Draft tables `tracking_config`, `tracking_metric_values`, `tracking_alerts`, `tracking_cards`, `tracking_decisions`, `tracking_runs` (with `cost_eur`). Not created | Spec | – | 12.10. | Yes. `tracking_decisions` and `tracking_runs` overlap with the task model |
| Client approval brief | `00_project/client-approval-workflow/brief.md` | Client choice rules, decision log fields, "ready for live" list, Martin's go | Spec | – | 13.10. | Yes (client-facing view pattern) |
| Daily standup | `reporting/daily-standup.sh`, `render-standup.py`, `reporting/standup/` | Calls `daily_standup()` and renders text | Script (weekday cron) | Martin | Local output only 2026-08-18. The run may happen elsewhere | Yes (logic). Check where it runs now |
| Night shift | `reporting/night-shift/<date>/` (20 nights since 2026-09-15), `LOG.md` | `plan.json`, `state.json`, `REVIEW.md`, `specs/`, `audits/`, `critic/` per night | `night-shift.sh` (launchd) | Martin (rarely read, spec O6) | 2026-10-12 | Yes. Agent outcomes with pass or "needs_martin" status |
| Chat transcripts | `~/.claude/projects/*/*.jsonl`, session list | Real work done, promises to clients, open points | Claude sessions | Martin | Live | Yes, as raw input (grill S2). Not a store |
| Git log | `main` + `.claude/worktrees/*` | Committed work per area | Sessions | Martin | Live | Yes, as proof links |
| Client asset folders | `00_project/assets/<client>/…` | Workflow outputs, `_status.md` (CRO, pool), reports | Workflows | Martin | Per run | Yes, as proof links |
| Google Drive client folders | Drive (not opened) | Client-facing archive (see 2.3) | Workflows, Martin | Client | – | Yes, as client-facing proof links |
| Memory files | `~/.claude/projects/-Users-martindrendel-741website/memory/` (207 files) | Client facts, rules, status, deadlines | Sessions | Agents | Varies | Input only (grill S9, S13). Not a task store |

### 2.3 Google Drive (from memory files only)

- The client Drive folder is client-facing. Internal team briefings never go there (`internal-briefings-not-in-client-folders.md`).
- Each delivery ends with a direct Drive link (`always-give-drive-link.md`).
- CRO runs keep all final files and `_status.md` in the Drive folder `CRO Homepage`, so a run can continue from Drive (`cro-drive-home-resume.md`).
- Website drafts and text drafts go to the client only as portal links, never as PDF or Google Doc in Drive (`feedback-drafts-link-only.md`, `client-textdraft-delivery.md`).
- Drive is an archive of finished outputs. It does not hold task status.

### 2.4 Memory files with per-client status or plans

- Suriya: `praxis-suriya-client.md`, `suriya-baseline-tracking.md`, `suriya-elementor-dinakar-set.md`, `suriya-ayurveda-massage-page-untouchable.md`, `suriya-conversion-paths-must-stay.md`
- Hüwel: `huewel-client.md`, `huewel-website-live-state.md`, `huewel-site-workflow.md`, `huewel-nap.md`, `huewel-newsletter-build.md`, `huewel-onlyinside-ersatz.md`, `huewel-banerji-subtitles.md`, `huewel-repo-ai-rules.md`
- Stürzl: `anja-stuerzl-client.md`, `stuerzl-source-of-truth-sheet.md`, `stuerzl-backlog-no-implement.md`, `stuerzl-cro-run.md`, `stuerzl-local-falcon-keywords.md`, `stuerzl-kosten-fakten.md`
- Dumann: `dumann-client.md`, `dumann-ueber-mich-page.md`
- Brasse: `maria-brasse-client.md`, `maria-brasse-nap.md`
- Bali Healing: `balihealing-google-ads-setup.md`, `balihealing-local-seo.md`
- Others: `franziska-rabenmuetter-client.md`, `shopify-admin-api-rabenmuetter.md`, `kamil-physio-client.md`, `johnijayamotor-client.md`, `tacheles-client.md`, `marcel-rosenbach-client.md`, `adel-client-cro.md`, `pauspapier-michael-ehlers.md`, `meerblick-klaus-dieter-sachs.md`, `eri-trostl-prospect.md`
- Cross-client: `team-roster.md`, `daily-client-standup.md`, `morning-grill-workflow.md`, `tracking-workflow.md`, `client-approval-workflow.md`, `night-shift-agent.md`, `week1-playbook.md`, `program-deliverable-rules.md`, `prospect-batch-2026-08-04.md`, `session-state-2026-08-06.md` (old)

## 3. Existing producers of tasks and outcomes

| Producer | Produces | Where it writes | Owner model |
|---|---|---|---|
| `provision_client` (RPC) | 44–52 template tasks, 6 onboarding steps, access grants per new client | `tasks`, `onboarding_steps`, `access_grants` | 741 / kunde |
| Portal admin and client clicks | Task ticks, access status, uploads, report verdicts, approval choices | Supabase tables in 2.1 | Admin or client |
| Morning Grill skill (06:00 / 17:00) | Decision cards, plan per client, `tasks.json`, team task drafts, message drafts, snapshot | `00_project/assets/morning-grill/`, `grill_snapshots` | Martin, Dinakar, Tantri, Gayo, agent, external |
| Workflow skills (content writing, CRO homepage, backlink DACH, review page, lockout, tracking, pool, audit) | One run with result, note and status | `_run.json`, `_status.md`, asset folders, Drive | Agent, then Martin approves |
| `workflow_registry.py sync` | Registry rows and the Excel | `registry.json`, `Workflow-Uebersicht.xlsx` | Workflow + client, no person |
| Night shift (`night-shift.sh`) | Page specs and audits from open content tasks, with Critic verdict | `reporting/night-shift/<date>/`, `LOG.md` | Agent, "needs_martin" flag |
| Daily standup (`daily_standup()`) | Per-client status text | `reporting/standup/` | Read only |
| Team daily plan and report (`submit_daily_plan/report`) | Outreach plan and done numbers per member | `daily_plans`, `daily_reports` | Team member |
| Listing inbox poller | Verify mails | `listing_emails` | – |
| Edge functions and triggers | Sent mails, admin events | `emails_log`, `admin_notifications` | System |
| Client chats (Claude sessions) | Most real work and promises | Transcripts, git, `activity_log` (sometimes) | Not recorded |

## 4. Duplicates and conflicts

1. **Client names.** Supabase "Naturheilpraxis Daniela Dumann", registry "Daniela Dumann", goals "Daniela Dumann", folders `dumann`. Kamil appears as "Kamil Böyük", "Kamil Böyük (Physio Anatomie + Kraft)" and "Kamil (Physio Anatomie + Kraft)". me&you is "Meandyou" in the registry and "me&you / Pauspapier" in the goals. Rabenmütter is "Rabenmütter Shop" in Supabase.
2. **Program start dates.** Suriya: portal 2026-09-03, memory 2026-08-14. Hüwel: portal 2026-08-25, memory 2026-08-16. Stürzl: none (spec O2).
3. **Task lists.** Portal `tasks` (template), Morning Grill `tasks.json` and `plan.md`, `team-tasks-drafts.md`, night-shift `plan.json`, and open points in `_run.json` notes. They do not link to each other.
4. **"Done" text.** `activity_log`, `_run.json` notes, registry notes, `brief.json` "fixed", and the planned evening log all hold the same kind of fact.
5. **Status words.** Registry: "in Arbeit / fertig, Freigabe offen / freigegeben". Portal: "offen / erledigt". Grill: "open / waiting / in_progress / done / drafted". Approval: "draft / ready / go / change". Citations: "planned / submitted / live".
6. **Last activity.** `daily_standup()` reads only portal rows. The grill reads chats. Both disagree for active clients (spec L3).
7. **Team list.** `team-roster.md` names Dinakar, Tantri, Gayo and Defina. Supabase `team_members` holds Gayo, Rias and Farzana. Defina is only a `delivery` profile.
8. **Decision logs.** `approval_decisions`, `grill_answers` and `cards.json`, the planned `tracking_decisions`, and `decisions.md` per grill run.
9. **Run data.** The registry, `_run.json`, the planned `tracking_runs` and the Excel all describe runs.

## 5. What is missing for a–d

**(a) Task list**
- A durable task record that is not the template: `client_id`, title, phase or milestone link (the 13 weeks), due date, status, source (card, chat, run, client request, feedback row).
- A path from `report_feedback` "aenderung" (98 rows) and `access_grants` "hilfe_angefragt" (8 rows) into tasks.
- A link from a task to the `_run.json` or workflow run that does it.

**(b) Delegation list**
- An owner field with persons and agents: Martin, Dinakar, Tantri, Gayo, Defina, agent (with workflow id), client.
- Portal accounts and `team_members` rows for Dinakar, Tantri and Defina. Without them, step 2 ("my tasks") cannot work.
- Handoff note, inputs-ready flag and the WhatsApp line (today only in `team-tasks-drafts.md`).
- A rule which owner the client may see. Stürzl-facing lists name no persons.

**(c) Links to sources and proof**
- One `links` structure per task: proof URL, Drive file, git commit, chat id, run folder, report, screenshot.
- Drive links for the rows of the customer list in `registry.json` that have none (15 of 21).
- `client_id` on the 28 `listing_emails` rows.

**(d) Outcome**
- A result field in client words, separate from the internal note.
- A link from the result to a goal number (goal sheet, planned `tracking_metric_values`).
- Time and cost per task and per agent run (only planned in `tracking_runs.cost_eur`).
- A send log for client messages. Drafts exist, but the send status is unknown (spec L2).
- A client-safe view filter: `released` flag, as in `approval_items` and the tracking draft.

**Fix before the build**
- Change the `report_feedback` SELECT policy from `using=true` to own client or admin.
- Pick one client key (`clients.id`) and map the registry, goal sheet and folder names to it.
