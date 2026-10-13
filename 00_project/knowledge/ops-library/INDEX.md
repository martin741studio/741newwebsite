# Ops library — morning grill and daily client command

## Purpose

Lean research base for the 741 workflow "morning grill and daily client command". Each morning an agent scans the last 1–2 days, asks Martin sharp questions (urgency, owner, human vs agent, goals/KPIs/leading indicators, gaps), turns answers into today's plan per client, and logs done/open/tomorrow per client in the evening. Goal: fewer decisions for Martin.

- Fetch date: 2026-10-13
- Freshness rule: only sources published on or after 2026-07-13. Official docs are living pages and count as current on their fetch date. Every publish date below was checked on the page or in page metadata.
- Derived files: `_derived/rules.md` (40 IF/THEN rules) and `_derived/claude-tooling-facts.md` (verified tool limits).
- Source files hold short extracts in own words with at most one short quote. No full third-party texts and no raw transcripts are stored. Full copies of most official docs already exist in `00_project/knowledge/workflow-library/official-docs/`.

## Sources (23)

### Official docs (6)

| id | title | org | type | publish date | URL | local file | why it matters |
|---|---|---|---|---|---|---|---|
| O1 | Automate work with routines | Anthropic | official doc | living, fetched 2026-10-11 | https://code.claude.com/docs/en/routines | sources/O1-routines-cloud.md | Only Claude Code option that runs with the Mac off; 1 h minimum. No approvals. |
| O2 | Desktop scheduled tasks + /loop | Anthropic | official docs | living, fetched 2026-10-11 | https://code.claude.com/docs/en/desktop-scheduled-tasks , https://code.claude.com/docs/en/scheduled-tasks | sources/O2-local-scheduling-desktop-and-loop.md | Local runs with repo access. Skipped when asleep. Catch-up rules. |
| O3 | /goal, cross-session messaging, agent view | Anthropic | official docs | living, fetched 2026-10-11 / 2026-10-13 | https://code.claude.com/docs/en/goal , .../cross-session-messaging , .../agent-view | sources/O3-goal-crosssession-agentview.md | Keep a log pass running. Hand results between sessions. One screen of "waiting on you". |
| O4 | Remote Control, mobile, push, channels | Anthropic | official docs | living, fetched 2026-10-13 | https://code.claude.com/docs/en/remote-control , .../mobile , .../channels | sources/O4-remote-control-mobile-push-channels.md | Answer the grill from the phone. Push rules. Mac must stay on. |
| O5 | Claude Code Projects | Anthropic | official doc | living, fetched 2026-10-11 | https://code.claude.com/docs/en/claude-projects | sources/O5-claude-code-projects.md | Coordinator + threads + "Waiting on you". Possible per-client home. |
| O6 | Cowork cloud move, scheduled tasks, Dispatch | Anthropic | official help articles | living, fetched 2026-10-13 / 2026-10-11 | https://support.claude.com/en/articles/15520349 , /13854387 , /13947068 | sources/O6-cowork-cloud-scheduled-tasks-dispatch.md | Since 6 Oct new Cowork tasks run in cloud. Dispatch closed to new users. |

### Articles and write-ups (13)

| id | title | author/org | type | publish date | URL | local file | why it matters |
|---|---|---|---|---|---|---|---|
| A01 | My Morning Is 29 Decisions and a Walk Queue | Dan Willoughby | founder essay | 2026-08-27 | https://danrwilloughby.substack.com/p/my-morning-is-29-decisions-and-a | sources/A01-willoughby-29-decisions-walk-queue.md | Best model for decision cards, compressed answers, binding "park". |
| A02 | The Approval Queue Is the Product | Manish Lad | practitioner essay | 2026-10-06 | https://manishlad.substack.com/p/the-approval-queue-is-the-product | sources/A02-lad-approval-queue-is-the-product.md | Queue + away-log. Auto / notify / wait routing. One-minute cards. |
| A03 | Agency on Claude Code (README) | Veobit | agency case write-up (GitHub README) | 2026-09-29 (repo created, last push 2026-09-30) | https://github.com/Veobit/agency-on-claude-code | sources/A03-veobit-agency-on-claude-code.md | Local-services agency run on Claude Code: owner gate, autonomy ladder, pulse log. |
| A04 | I Built an AI Chief of Staff That Clocks In at 7:07 AM | Jyothi Venkat | build log | 2026-07-15 | https://jyothiwrites.substack.com/p/i-built-an-ai-chief-of-staff-that | sources/A04-venkat-ai-chief-of-staff-707.md | Ranking by standing priorities. Yesterday's memory feeds today. |
| A05 | One Daily Briefing Agent. 3 Very Different Ways to Build It | Pavel Jiranek | article | 2026-08-23 | https://thehybridleader.substack.com/p/one-daily-briefing-agent-3-very-different-ways-to-build-it | sources/A05-jiranek-daily-briefing-agent-3-ways.md | TODAY/FIXED/WATCH/NEXT layout. Start simple. |
| A06 | Gate Fatigue: When AI Approval Stops Working | FullStack Labs (A. Vanamali) | industry article | 2026-10-01 | https://www.fullstack.com/labs/resources/blog/gate-fatigue-when-human-approval-stops-meaning-anything | sources/A06-fullstack-gate-fatigue.md | Why too many approvals fail. Signals to watch. |
| A07 | Human-in-the-Loop AI Agents: Approval Workflows | PrompTessor | guide | 2026-10-06 (metadata) | https://promptessor.com/blog/human-in-the-loop-ai-agents | sources/A07-promptessor-hitl-approval-workflows.md | Approve/modify/reject/escalate. Approval expiry. |
| A08 | AI Agents Push Humans Out of the Loop | Mitchell, Ghosh, Passi | research position paper | 2026-08-24 | https://arxiv.org/abs/2608.23642 | sources/A08-mitchell-agents-push-humans-out-of-loop.md | Oversight skills decay. Keep real hands-on checks. |
| A09 | Your AI Agent Needs a Queue, Not a Chat Box | Shilpa Mitra | technical article | 2026-08-27 | https://webafterai.substack.com/p/your-ai-agent-needs-a-queue-not-a | sources/A09-mitra-agent-needs-a-queue.md | Durable, idempotent state for cards and logs. |
| A10 | KPI Scorecard: The Weekly 5 to 15 Number Template | Andreas Pettersson (Leaders ADAPT) | guide | 2026-10-01 | https://www.leadersadapt.com/weekly-scorecard/ | sources/A10-leadersadapt-weekly-scorecard.md | One owner per number. Leading indicators; 3-weeks-red rule. |
| A11 | Four Check-In Questions Worth Asking (And One to Drop) | Steven Macdonald (OKRs Tool) | article | 2026-08-04 | https://www.okrstool.com/blog/check-in-questions | sources/A11-okrstool-check-in-questions.md | Four weekly questions + 1–5 confidence. |
| A12 | The GTD Weekly Review: A 6-Step Protocol | Nishant Kapoor (Nerd Productivity) | guide | 2026-07-22 (metadata) | https://nerdproductivity.com/gtd-weekly-review/ | sources/A12-nerdproductivity-gtd-weekly-review.md | Weekly reset. Three rocks per week. |
| A13 | Level 10 Meeting | EOS Worldwide | official method page (undated, living) | none shown, counted at fetch 2026-10-13 — **flagged exception** | https://www.eosworldwide.com/level-10-meeting | sources/A13-eos-level-10-meeting.md | L10 agenda, 7-day to-dos, IDS. |

### Videos (4, all 5,000+ views, uploaded after 2026-07-13)

| id | title | channel | type | upload date | views | URL | local file | why it matters |
|---|---|---|---|---|---|---|---|---|
| V1 | I Made Claude My Personal Assistant (Full Build) | Systems Made Better | YouTube tutorial | 2026-09-25 | 47,472 | https://www.youtube.com/watch?v=3ZT0upsICHk | sources/V1-systemsmadebetter-claude-personal-assistant.md | Brief → approval tags → separate executor → captain's log. |
| V2 | Build Your Claude Command Center In 15 Minutes | AI Founders | YouTube tutorial | 2026-09-14 | 120,948 | https://www.youtube.com/watch?v=CBHUn7DFhkQ | sources/V2-aifounders-claude-command-center.md | "Would I act differently?" filter. Source map. Visibility check. |
| V3 | Turn Claude Code Into Your AI Operating System (4 Layers) | Pav Rusovs / Automation Orbit | YouTube walkthrough | 2026-09-22 (search listing) | 95,881–234,407 (scrapers disagree) | https://www.youtube.com/watch?v=Zs3faMCDYNs | sources/V3-rusovs-ai-operating-system-4-layers.md | Routines registry, run records, "agent never marks done", draft-only server agent. |
| V4 | Claude Is Moving to the Cloud (Here's What Breaks) | Mansel Scheffel | YouTube explainer | 2026-10-05 | 74,189 | https://www.youtube.com/watch?v=Mr-8DdrZDjo | sources/V4-scheffel-claude-moving-to-cloud.md | What breaks for local files and skills after 6 Oct. |

## Coverage by topic

- Topic 1 (operators running priorities with agents): A01, A03, A04, A05, V1, V2, V3.
- Topic 2 (decision fatigue, decision queues, human-in-the-loop): A01, A02, A06, A07, A08, A09.
- Topic 3 (operating rhythms): A10, A11, A12, A13.
- Topic 4 (Claude-native tooling): O1–O6, V4.

## Gaps and honest notes

- **EOS Level 10:** no fresh (after 2026-07-13) third-party source with substance. A13 is the undated official EOS page, used as a living-doc exception and flagged. Fresh pages found were updated before the cut-off (Spinach: 2026-07-11).
- **Decision-fatigue research:** the fresh items are practitioner pieces plus one position paper (A08). Stronger studies found were too old (Stack Overflow blog 2026-05-21, Thoughtworks 2026-06-05) and were dropped.
- **End-of-day log:** no fresh source dedicated to an evening shutdown log. The rules draw on A02 (away-log), V1 (captain's log), V3 (run records), A12.
- **DACH / German-language agency sources:** none searched in depth. None included.
- **OKR check-in:** only A11 is fresh. Other OKR guides had no visible date and were dropped.
- **Dropped as too old (checked dates):** chiefofstaff.network "I'm a Chief of Staff. So I Built Myself One." (2026-07-08), playingaws Cowork + routines (2026-07-09), anothercodingblog daily brief with routines (2026-04-25), linas.substack routines guide (2026-04-29), digitalapplied HITL escalation (2026-06-07), BlitzMetrics 18 scheduled tasks for agencies (2026-03-28), Mercury leading vs lagging (updated 2026-04-23), Asian Efficiency GTD review (updated 2026-07-12), cc-gtd GitHub (last push 2026-07-06).
- **Unverified claims kept out of rules:** A11's "43% lift" from weekly check-ins (vendor figure, no source checked).
- **Tool notes:** `yt-dlp` is not installed on this Mac, so YouTube discovery used the Apify actor `streamers/youtube-scraper` (upload-date filter "month", sorted by views). Transcripts came from `johnvc/YoutubeTranscripts` (dataset `bC8FIf44JlT9gFC2P`). The Firecrawl account reported low credits during this run.
- **Product state:** Routines, agent view, channels and Projects are in research preview or beta. Re-check `claude-tooling-facts.md` against the live docs before building.
