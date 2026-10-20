# Morning Grill + Daily Client Command (workflow `morning`)

Version 0.2 · 2026-10-13 · Status: DESIGN APPROVED by Martin (checkpoint 1, 2026-10-13). Dry run done (read only). Nothing is installed or scheduled. No portal change. Nothing is sent.
Owner: Martin. Runner: Claude Code Desktop, repo `/Users/martindrendel/741website`. Time zone: **WITA (UTC+8)** for every date and time in this file.
Language: STE. Chat name: `⚙️🧭 Morning Grill`.
Related: research `00_project/knowledge/ops-library/` (rules R1–R40 = `_derived/rules.md`), coverage `00_project/morning-grill-coverage-map.md`, architecture `00_project/workflow-architecture.md`, goal sheet `00_project/morning-grill-goals.json`.

## Contents
0. Job and done · 1. Decisions from the grill · 2. Daily rhythm · 3. Data sources and bookmarks · 4. Morning scan · 5. Decision queue · 6. Question bank · 7. Client goal sheet · 8. Human / agent routing · 9. Plan of the day · 10. Evening log · 11. Weekly and quarterly hooks · 12. Storage · 13. Automation and safety · 14. Success measures · 15. Hard rules · 16. Open points

---

## 0. Job and done

Job in one sentence (R1): **cut Martin's daily decisions to the few that only he can take, and make sure nothing for any client is forgotten.**

Done for one day means all of these are true:
- The brief existed before Martin opened the chat (or the fallback built it in under 3 minutes).
- Martin answered the cards in 10 minutes or less.
- Every active client has a line: today, fixed, watch, next.
- Every human task has an owner, inputs and a due date. Every agent task has a start command.
- At 17:00 the evening log draft exists. Martin confirmed it, or the next grill shows it first.

## 1. Decisions from the grill (2026-10-13)

| # | Topic | Decision |
|---|---|---|
| D1 | Backlinks | **Revised 2026-10-13:** keep both workflows (different outcomes). Citations = consistent listings; Backlink DACH = authority links (pillars B–E), ≥ 8 new referring domains in 90 days. Border: niche directories (jameda, Doctolib, theralupa …) belong to `citations`. The maps playbook only tracks O01–O20. Backlink doc + link library copied from worktree `great-easley-4f6970` to `main`. |
| D2 | Place and length | Desktop chat `⚙️🧭 Morning Grill`, 10 minutes. |
| D3 | Shape | One ranked queue for all clients and 741. Target max 7 cards. |
| D4 | First view | Martin's decisions only. Everything else is below. |
| D5 | Brief time | Pre-built at 06:00 WITA. Fallback: built when Martin opens the chat. |
| D6 | Defaults (no card) | Drafts and read-only scans; team tasks from the approved plan; portal task status to "needs review" (never "done"). |
| D7 | Not a default | Data spend outside a running workflow, anything external, money, launches, live-site changes, client messages. |
| D8 | Handoff to humans | Portal task with all inputs + a ready WhatsApp line for Martin to forward. Portal writes need GO-PORTAL first. Until then the task is a draft in `plan.md`. |
| D9 | Answer format | Clickable cards in chat (AskUserQuestion, 4 per round). Short string `1a 2p 3b` also works. |
| D10 | Goals | Filled for all active clients in this session (see §7 and the goal sheet). |
| D11 | Default numbers | Tracking set. Results: calls, web clicks, routes, real leads, reviews, Maps grid rank. Leading: 741 tasks done per week, pages live, citations live, review asks sent. |
| D12 | Lookback | Since last grill, one bookmark per source. Monday covers the weekend. Failed source = "unreadable". |
| D13 | Evening log | Agent drafts at 17:00 WITA, Martin confirms. "Log the day" runs it at any time. |
| D14 | 741 level | One line every day. A full 741 card every Monday. |
| D15 | Output | Chat + one-page HTML brief (side panel). Portal tab later. |
| D16 | Success | "Nothing forgotten" (§14). |
| D17 | Client status | Active: Suriya, Hüwel, Stürzl, Dumann, Brasse, Bali Healing (now Kunde), Rabenmütter, Johni Jaya Motor (restart), Kamil (reports overdue), me&you/Pauspapier, Marcel (new sales opportunity). Done: Tacheles. |
| D19 | Grill's own open points | Every open point of a workflow becomes a card in the queue. Never a prose list at the end of a report (Martin 2026-10-13). |
| D20 | Install | Skill install + trigger tests + baseline approved 2026-10-13. |
| D21 | Schedule | Desktop tasks 06:00 / 17:00 only after the tests pass; the first 3 runs are opened and read. |
| D22 | Portal tasks | One week as drafts in plan.md, then the agent writes portal tasks from the approved plan. |
| D23 | Start dates | Decided client by client, one walk-queue item each (Suriya, Hüwel, Stürzl). |
| D24 | Grill flow | Three parts in chat: 1 status report (where we are, what moved, what runs, what is stuck + why + who waits), 2 walk queue + decision cards, 3 what happens now (who, when Martin hears back). Martin 2026-10-13: "I get informed through the grill". |
| D25 | Report depth | Clients with movement, a blocker or a card get 3–4 lines; quiet clients one line (`status_report.py`). |
| D26 | Evening report | The 17:00 run also reports in chat in the same style, then one confirm card. |
| D27 | Command Center page | One page `00_project/assets/morning-grill/command-center.html`, rebuilt after every scan, grill answer and evening log. Tabs: Decisions (cards in the client-approval style, 741 recommends, click → answer line), Clients (goal, program week, roadmap P0–P6 with registry workflow status, open now, next steps, goal numbers), Agents & waiting. Martin 2026-10-13: "I have no idea where we are" from chat alone. |
| D28 | Command Center home | Portal admin view on staging (answers saved in Supabase). Portal write order (Martin 13.10.): Freigabe-Dashboard → outreach numbers per client → Command Center. The local page stays in use until then. |
| D29 | Admin panel build | Command Center as an admin-only tab on clients.741.studio, data from an admin-only Supabase snapshot table, clicks saved to `grill_answers`. Plan: `00_project/morning-grill-portal-plan.md` (not built). |
| D30 | Admin tab on staging | Built and tested 13.10. (tables, RLS, tab, answer pull). Live upload and the snapshot write in the scheduled runs wait for separate gos. Log: `morning-grill-portal-plan.md` §8. |
| D31 | Live + run write | Tab is LIVE since 13.10. (backup `index-2026-10-13-before-command-center.html`). The 06:13 and 17:00 runs pull answers first and publish one snapshot at the end (Martin's go 13.10.). |
| D32 | Own answer + change answer | Added 13.10. by the Freigabe chat after Martin's review: every card has "Write own answer" (grill_answers option `own`, text required, DB constraint `own_needs_text`) and decided cards can be reopened (latest answer wins). `pull_answers.py` turns `own` into the decision text. Verified by this chat: repo source reproduces live byte for byte, JS valid, constraint present. |
| D33 | No walk list, only cards | Martin 13.10. (via the Freigabe chat): "We can just put up the decision so I can click easily through." Every click item is a decision card (type 'Your click'): Done / Agent or team does it / Not today with reason (park) / own answer. Real decisions in the list get real options (start dates, Go-C). Live 13.10. Snapshot field `walk` stays empty. `pull_answers.py` writes all answers into the ledger with client, headline and option text. |
| D34 | Tasks tab | Martin 13.10. (via the Freigabe chat): "how do we actually list the task that needs to be done as a result of that?" → tab 'Tasks' in the Command Center: one line per resulting task with owner, status, client, source card, link; click-card tasks follow the card status. Source: `<run>/tasks.json` (written in step 9). Team tasks stay drafts for the first week (`team-tasks-drafts.md`). Live 13.10. |
| D35 | One task system | The Freigabe chat designs the per-client task and delegation model (`00_project/client-work-visibility/`, research `knowledge/client-work-library/`). The Tasks tab stays a thin v0 on `tasks.json` inside the snapshot; no task table is created by this workflow. When its schema exists, the grill writes into it and the tab switches over. Tables of this workflow: only `grill_snapshots`, `grill_answers`. |
| D36 | Task model | The Freigabe chat built the task model (tables `work_*`: work_items, work_actors, work_evidence, work_events, work_client_health …, RLS admin all / delivery read) on 13.10. with Martin's go; my 23 tasks were imported (source 'grill', source_id '<date>/tNN'). The Tasks tab now reads `work_items` (fallback: snapshot). `publish_tasks.py` writes my tasks idempotently (rules in the SKILL). Scheduled runs do NOT write tasks until Martin says go (the card was dismissed 13.10.); only the one snapshot row stays approved. |
| D37 | Night queue | Requested by the Night Shift chat (spec 00_project/night-shift-server-workflow.md §3, §14); Martin's go 13.10.: the 17:00 run adds the card 'Night queue <date>' (≤ 8 night-suitable agent tasks), writes only his ticked items to `reporting/night-shift/queue/<date>.json` with `build_night_queue.py` (validates classes, limits, inputs, confirmed_by). NO ANSWER = NO FILE = no night run (the 17:30 read-only fallback of the spec is NOT used). The 06:13 run shows `REVIEW.md` results as release cards (S6). |
| D18 | Leads | In the daily 741 line. A lead gets a card only when a follow-up is due or older than 7 days. |
| D38 | WhatsApp + email scan | Martin 14.10.: the grill reads his local WhatsApp (Mac app) and Airmail (all accounts, unified inbox) for a summary, prepared answers and prepared actions, routed to the right chat. WhatsApp: business chats only (clients, team, prospects), no personal/family chats. No connector exists for either, so access is via computer-use (one-time grant per app), reading the screen. Voice notes are transcribed only if the audio file can be found on disk (`whisper --model small`); screen-reading alone gives no audio. Runs ONLY in the interactive grill with Martin present — never in the 06:00/17:00 scheduled task. See S14, S15. |

## 2. Daily rhythm

```
05:50  (existing) nothing — standup still runs at 08:05; the scan calls the standup RPC itself
06:00  M0 SCAN      Desktop scheduled task, read only → scan.json, cards.json, brief.html
any    M1 GRILL     Martin opens ⚙️🧭 Morning Grill → brief link → card rounds (≤ 2 rounds of 4)
+10m   M2 PLAN      answers → plan.md per client + task drafts + WhatsApp lines + agent starts
day    M3 RUN       agents and team work; client chats as usual
17:00  E1 LOG       Desktop scheduled task → evening-log draft per client
any    E2 CONFIRM   Martin confirms or fixes the log (one card) → tomorrow's open list
Mon    W1           741 card + weekly review cards (parked cards, defaults proposals, stale to-dos)
Qtr    Q1           hand-over to the tracking war room; goals reset
```

If the Mac slept at 06:00, Desktop runs one catch-up on wake (R33). If the catch-up starts after 12:00, it builds a short brief: fires and decisions only (R8).

## 3. Data sources and bookmarks

Rule: each source has a bookmark in `state/bookmarks.json` (R6.1 of the workflow library). A read error is written as `unreadable` with the error text. It is never "nothing new" (R6.2). Before a new source feeds the brief, the agent shows one real record from it (R5).

| id | Source | How it is read | What it gives | Source of truth for |
|---|---|---|---|---|
| S1 | Session list | `list_sessions` (titles, `lastActivityAt`, worktree, group) | Which client and workflow chats moved | chat activity |
| S2 | Chat transcripts | Subagent per moved chat reads the transcript tail since the bookmark (`~/.claude/projects/*/*.jsonl`, `export_transcript`) and returns ≤ 8 lines: done, open, waiting-for, promises to client | What we actually did | work done in chats |
| S3 | Registry | `00_project/workflow-registry/registry.json` | Runs, status, "fertig, Freigabe offen" | workflow runs and approvals |
| S4 | Git, all worktrees | `git log --since=<bookmark>` in main and each `.claude/worktrees/*` | Commits per area | committed work |
| S5 | Portal standup | RPC `daily_standup()` via `reporting/daily-standup.sh` logic, read only | Program week, onboarding, missing access, help requests, unread messages, overdue tasks | program, tasks, client messages |
| S6 | Night shift | `reporting/night-shift/<date>/REVIEW.md` | Drafts waiting for review, repeat blockers | overnight drafts |
| S7 | Citations | `client_citations` (planned > 14 days), `listing_emails` (handled = false) | Stuck listings, verify links | listings |
| S8 | Tracking | Early warnings from the tracking workflow (when built); until then Local Falcon MCP GBP reads only on Monday | Calls, clicks, routes, reviews | proof numbers |
| S9 | Memory | Client memory files changed since the bookmark | New rules, client facts | client rules |
| S10 | Calendar | Google Calendar MCP, today and tomorrow | Calls and deadlines today | meetings |
| S11 | Yesterday | `<yesterday>/evening-log.md`, `state/cards.json` | Carry-over, open and parked cards (R7) | commitments |
| S13 | Deadline sweep | `scan.py read_deadlines()` over ALL memory files | Dated deadlines without a done note | open deadlines |
| S12 | 741 level | `00_project/revenue-model-100k.md`, prospects `_run.json`, lead memory files | Pipeline line, follow-ups due | agency numbers |
| S14 | WhatsApp (Mac app) | **Interactive grill only, Martin present.** computer-use opens WhatsApp.app (one-time access grant), reads business chats only (clients, team, prospects — no personal/family chats). Voice notes: locate the media file on disk and transcribe with `whisper --model small` (memory `audio-transcription-fast`); screen-reading alone cannot transcribe audio. | Summary per chat, prepared answers (drafts), prepared actions, routed to the client's chat or team drafts | client/team WhatsApp messages |
| S15 | Email (Airmail, all accounts, unified inbox) | **Interactive grill only, Martin present.** computer-use opens Airmail's unified inbox (all connected accounts). Business-relevant mail; same drafting and routing rules as S14. | Summary, prepared answers, prepared actions | email |
| S16 | Outreach & Sales board | Supabase `741-portal` project (`galjmtozcgxcwtzkzbpi`): `outreach_accounts` joined to `daily_report_accounts`/`daily_reports` — per LinkedIn account requests_sent, accepted, pitched, follow_ups, replies, interested, last report day | Per-account LinkedIn numbers, judged (which account works, which is stalled, which never reports) | outreach/sales activity, added 2026-10-20 (Martin: "needs to be checked once a day, every time") |

Decided 2026-10-14 (D38, see decisions table): S14/S15 never run in the unattended 06:00/17:00 scheduled task — personal data, no one watching. They run only when Martin says "grill me" (or asks directly) and are present in the chat.
Decided 2026-10-20: S16 runs every grill (morning and evening, scheduled or interactive) — it is read-only Supabase data, no personal-data restriction. A stalled account (sent but not pitched/replied for 2+ days) or a never-reported account becomes a judgment card.

## 4. Morning scan (M0)

Steps, all read only:
1. Read `preferences.md` (Martin's standing priorities and defaults; the agent cannot edit it) (R3.7 of the workflow library).
2. Read bookmarks. Read S1–S12. Write `scan.json` with one block per client plus a 741 block. Each fact carries its source id and a link.
3. Run the detectors (§6). Each hit becomes a card candidate or a brief line.
4. Rank card candidates (§5.3). Keep max 7. Batch related ones. Move the rest to "below the line".
5. Render `brief.html` (template `templates/morning-grill-brief.html`) and `brief.md`.
6. Validate with `scripts/validate_brief.py`: every card has options, a recommendation, a deadline and an evidence link; no card older than 3 days without a decision or park reason; every active client has a line. Fix until it passes.
7. Write `_run.json`, the pulse line in `state/pulse.log`, and move the bookmarks.

## 5. Decision queue

### 5.1 Decision card format (R9)

```json
{"id": "2026-10-13-suriya-01", "client": "Praxis Suriya", "type": "decide|approve|define|route|park-check",
 "headline": "plain words: what, why now, what the answer unlocks",
 "evidence": ["link or path", "source id"],
 "options": {"a": "...", "b": "...", "c": "..."}, "recommended": "a", "why": "one line",
 "deadline": "2026-10-14", "created": "2026-10-13", "status": "open|decided|parked|expired",
 "answer": null, "park_reason": null, "then": "what the agent does after each option"}
```

A card that has no recommendation, uses jargon, or takes more than about 1 minute goes back to the agent (R9, R10).

### 5.2 Answers
- Martin clicks the options (AskUserQuestion, 4 per round, max 2 rounds). Or he types `1a 2p 3b`.
- `p` = park. A park needs a reason. The card returns only when the reason changes (R12).
- If the answer conflicts with the record, the agent says so with evidence and keeps the card open (R13).
- Every answer is written to `state/cards.json` and `<date>/decisions.md` before the agent acts.

### 5.2a Walk queue (R24, added after the dry run)
Some items are not decisions. They are 1–5 minute clicks that only Martin can do (Wix Publish, Airmailer send, Search Console "Add user", "which drafts did you send?"). They go to a separate **walk queue** with checkboxes. They do not count against the 7 cards. A judgment card becomes a walk item when it has the field `walk` (one line: what, where, minutes).

### 5.3 Ranking (standing priorities in `preferences.md`)
1. Fire: lost access, angry or worried client, broken site or tracking, legal or HWG risk.
2. Money and contract: start dates, payments, renewals, new offers (e.g. Marcel).
3. Client deadline within 3 days or a promise made to a client.
4. Approval waiting more than 3 days (registry "fertig, Freigabe offen").
5. Goal gap: missing goal field, leading number red.
6. Pipeline follow-up due.
7. Internal 741 work.

Inside one level: older first. More than 7 candidates: the extra ones go "below the line" with one line each, and the Monday review proposes defaults for repeated types (R15, R16).

## 6. Question bank with conditions

Martin's 9 questions become detectors. The agent asks a question only when its condition is true. It never asks what a file already answers.

| Q | Martin's question | Condition that creates a card or a line | Card type |
|---|---|---|---|
| Q1 | Who has urgency? | Any priority-1 to -3 fact (§5.3) | rank only, no own card |
| Q2 | Human needed, who must work on it? | Next step of a client is a human task type (§8) and has no owner | route |
| Q3 | What must be done, who can do it, what must be prepared? | Human task lacks an input (access, text, photo, approval, budget) | define |
| Q4 | Can the agent do it alone? | Task type is "agent alone" in §8 → no card, runs as default. Type unknown → card | route |
| Q5 | What activities lead to the result? | Client phase has a next workflow in `workflow-architecture.md` §3 whose gate is open | brief line "next" |
| Q6 | Is everything defined (goal, KPI, measurement)? | A goal-sheet field is `null` or older than 90 days | define |
| Q7 | Are we aligned (client or 741)? | A client message, chat or memory file contradicts the goal sheet or the plan (e.g. Suriya's new hard rules), or a client is silent > 14 days | decide |
| Q8 | Do we hit the goals and KPIs? | Monday only: a weekly number misses its threshold | brief line; card when red 2 weeks |
| Q9 | What are the leading factors? | A number is red 3 weeks in a row → question goal and measure (R18) | decide |

Extra detectors from the coverage map:
- Q10 Approval queue: registry run in "fertig, Freigabe offen" > 3 days → approve card (batch by client).
- Q11 Night shift: REVIEW item unread > 1 day, or the same blocker 3 times → card.
- Q12 Stale task: portal task overdue > 7 days without a card → card ("done, re-plan, drop").
- Q13 Status conflict: two sources disagree (e.g. program start 14.08. vs 03.09.) → define card, once.
- Q14 Unhandled client message or help request > 1 day → priority 1.

## 7. Client goal sheet

File: `00_project/morning-grill-goals.json`. One block per client. The agent fills numbers from baselines and marks them `proposed`. Martin confirms each number with one card (Q6). A number is never invented: no baseline means the field stays `null` and a define card asks for the source.

Fields: `client`, `registry_name`, `status` (active / restart / paused / done / lead), `grill` (daily / monday), `phase` (P0–P6 from the architecture map), `program_start`, `program_end`, `quarter_goal` (text), `goal_numbers` [{metric, baseline, target, due, source, status proposed|confirmed}], `leading` [{metric, weekly_threshold, owner}], `next_milestone`, `blockers`, `waiting_for` [{who: client|team|google|martin, what, since}], `client_rules`, `chat` (session id), `next_workflow`.

## 8. Human / agent routing

| Task type | Who | Handoff |
|---|---|---|
| Scans, audits, pool, page specs, copy drafts, report drafts, prototypes, review pages | Agent alone (default D6) | Start command in `plan.md`; result in the evening log |
| CMS implementation (Elementor, WordPress, Shopify), page publish after Martin's go | Dinakar (Tantri as second) | Portal task + WhatsApp line |
| Citations group A, listing verify links, data entry | Tantri | Portal task + WhatsApp line |
| Outreach, LinkedIn follow-ups, prospect lists | Gayo | Portal task (team area) + WhatsApp line |
| Client calls, client messages, Loom, money, approvals, live-site go, offers | Martin | Card or walk queue (R24) |
| Logins, group B listings, review asks, photos, texts from the client | Client | Message draft for Martin (never sent by the agent) |

Rules: the agent never marks a task "done" (R26). A new automation starts at level L0, propose only (R22). Stürzl-facing lists name no people; they use "von euch" / "741" (memory `feedback-no-named-task-owners`).

## 9. Plan of the day (M2)

`<date>/plan.md`, one block per client: **Today** (task, owner, inputs ready yes/no, due) · **Agent starts** (exact chat sentence or slash command, e.g. `/content-write Stürzl <page>`) · **Waiting for** · **Message drafts** (```text blocks, slop-checked 5/5, never sent by the agent).
Agent work that Martin approved in the grill can start as new sessions from the grill chat (memory `start-chats-directly-no-offer-card`: `start_session` user_asked, `use_worktree: false`) or continue in the existing client chat (SendMessage to its session id).

## 10. Evening log (E1, E2)

Draft at 17:00 WITA from the same sources, since the morning bookmark. Per client: **Done** (with link) · **Open** (with owner) · **Tomorrow** (first action) · **Blockers / waiting for** · plus "What agents did while you were away". Martin confirms with one card: confirm / fix lines / add. Unconfirmed logs show first in the next brief. File: `<date>/evening-log.md`; one line per client is also appended to `logs/<client-slug>.md` (running client history).

## 11. Weekly and quarterly hooks

- **Monday** (in the morning grill, +10 minutes): 741 card (revenue vs `revenue-model-100k.md`, pipeline, capacity, 3 priorities of the week); scorecard per client against the goal sheet; parked cards review; repeated answers → default proposals (R15); to-dos older than 2 weeks → done / re-plan / drop (R30).
- **Tracking**: the tracking workflow's weekly card (draft Monday, release Wednesday 12:00) and its red alerts enter the queue as priority 1 (red) or a brief line (yellow).
- **Quarter**: the grill hands each client's goal sheet and decision log to the tracking war room. The war room's decisions (date, decision, owner, due, metric, review date) come back as goal-sheet updates.

## 12. Storage

```
00_project/assets/morning-grill/
  preferences.md                  # Martin's standing priorities + defaults (read only for the agent)
  state/bookmarks.json  cards.json  pulse.log
  logs/<client-slug>.md           # one line per day per client
  <YYYY-MM-DD>/scan.json  brief.md  brief.html  decisions.md  plan.md  evening-log.md  _run.json
00_project/morning-grill-goals.json   # goal sheet (later: portal table, needs GO-DB)
00_project/morning-grill-skill/       # skill draft (not installed)
```
`_run.json`: `{"client": "741 Studio (intern)", "workflow": "morning", ...}` per day, so the overview Excel shows each day.

## 13. Automation and safety

- Two **Desktop scheduled tasks** (local files needed, R33): 06:00 scan, 17:00 log draft. Setting "keep computer awake". Not cloud routines: they cannot read the local repo (R32).
- Before the first unattended run: automation-build layers from `00_project/automation-workflow.md` (L0 propose only; read-only credentials; spend cap 0 € in the scan; pulse log; time zone in the prompt; open and read the first 3 runs, R6.10).
- The scan never writes to the portal, Supabase, Drive, a client site, or a message channel.
- Cost cap: one scan run ≤ 1 subagent per moved chat, max 12 subagents; Haiku or Sonnet for transcript summaries.

## 14. Success measures (after 2 weeks)

**Nothing forgotten** (Martin's pick): no overdue portal task, open approval, unanswered client message or help request older than 7 days without a card. Checked by `scripts/validate_brief.py --audit` every Monday.
Side measures (logged, not gates): minutes from open to last card; cards per day; parked cards; clients with no logged step in 7 days.

## 15. Hard rules

1. Read only in the scan. Every write outside `00_project/assets/morning-grill/` needs a card or an approved plan line. Exception (Martin 2026-10-13): `publish_snapshot.py` inserts ONE row per run into the admin-only table `grill_snapshots`; `pull_answers.py` reads `grill_answers`.
2. Never send a message, never publish, never spend. Message drafts in ```text blocks, slop-checked 5/5.
3. Never mark a task "done". Never invent a number; `null` + define card instead.
4. Failed source = "unreadable" in the brief.
5. STE in the brief and the cards. German client names stay as they are.
6. No Martin guide in the brief (internal deliverable, not client-facing).

## 16. Dry run 2026-10-13 (read only) — lessons

Run folder `00_project/assets/morning-grill/2026-10-13-dryrun/`. 11 of 12 sources read (S8 tracking not built). 37 chats had work since the bookmark. 22 card candidates → 7 cards, 4 walk items, 11 below the line. `validate_brief.py` PASS. Screenshots `brief-desktop.png`, `brief-mobile.png` (375 px).
- L1 The queue is too broad on day 1 (22 candidates). The walk queue took 4 out. The Monday review must turn repeated types into defaults (R15).
- L2 Many client drafts have no visible send status (WhatsApp is not readable). The "which drafts did you send?" walk item is needed every day until a send log exists.
- L3 The portal shows "last activity" weeks old for clients with daily chat work (Suriya: 21.09.). S2 (chat summaries) is the real activity source.
- L4 Suriya already ranks 1 at all 49 grid points for one keyword. A goal can be met on day 1; goals need all 5 keywords.
- L5 Citations: Suriya 28 unhandled verify emails, Suriya 25 and Hüwel 29 planned > 14 days, Dumann 85 planned + 4 inconsistent. Nobody saw these before.
- L6 Headless Chrome lays out at 500 px minimum; the mobile check renders the brief in a 375 px frame.
- L7 Baseline (fresh session without the skill) found 3 old memory deadlines the scan missed (cold-email Abmahnung 23.09., Bali advertiser verification 01.10., Taxi .htaccess risk). New source **S13 deadline sweep**: all memory files, dated deadline phrases in [today−60, today+3] without a done note. Urgent ones (legal, verification) become priority-1 cards; invoice and payment hits are never shown unasked (memory `feedback-no-invoice-talk`).
- L8 Trigger tests: plan mode blocks the Skill tool; test with `--allowedTools "Skill" "Read"`. `disable-model-invocation` removed so "Was steht heute an" works.

## 17. Open points

- O1 GO-PORTAL: approved with a one-week draft period (D22).
- O2 Start date conflicts: Suriya 14.08. vs 03.09.; Hüwel 16.08. vs 25.08.; Stürzl none.
- O3 Registry fixes: DONE 2026-10-13 (Bali = Kunde; Tacheles, Kamil, Rabenmütter, Johni added).
- O4 Backlink: no merge (D1 revised). Doc and library are on `main` now. Skill tests open (own chat).
- O5 Standup: `letzte_aktivitaet` reads only the portal; the grill's evening log could write a portal activity line later (GO-PORTAL).
- O6 Night shift: nobody reads REVIEW.md; the grill now shows it (Q11).
