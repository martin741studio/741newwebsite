# Decisions — agent-job-descriptions

Martin's gos, with date and his words.

(none yet — Checkpoint 1 pending)

## 2026-11-03 — Checkpoint 1, round 1 (4 AskUserQuestion cards)
- 0.0 inputs: "Confirm all 4 (Recommended)" — Job, surface, cadence, hard limits confirmed as in `inputs-grill.md`.
- First agents: Martin wrote his own answer: "Now we need to create a new job description and I want you to grill me on that because what we definitely need is power development. The web developer does execution work for our SEO clients. I guess you need to grill me on that. To keep in the backlog as well is social media manager/strategist". Reading: the first job description is for a NEW agent, a web developer that executes for the SEO clients (read "power development" as web development); a second new agent "social media manager/strategist" goes to the backlog. The existing unattended agents (A1–A5) are not rejected; they follow after the web developer.
- Where it lives: "At its rung per agent type (Recommended)" — scheduled: header in task SKILL.md / runner prompt; chats: `.claude/rules/agents/<id>.md` with `paths:`; roster + memory pointer; source of truth `agent-jobs/<id>.md`; validator checks copies.
- Gate mapping: "Two named lists per agent, no new hook (Recommended)" — hook-enforced list + card-enforced list; card shows the exact change, Go option carries "Go", same turn.

## 2026-11-03 — Checkpoint 1, round 2 (4 cards)
- Web Developer = "A Claude agent session (Recommended)": one standing chat that builds and fixes pages in the client CMS and deploys only per card Go; humans stay as they are.
- Scope: all four — page builds from approved prototypes, on-page SEO fixes, technical fixes, tracking and conversions.
- Manager + review: "Martin via morning grill, Friday review card (Recommended)": one card per agent in the Friday 06:13 grill; Martin grades A–F in one sentence.
- Language: "English STE, German for client-facing fields (Recommended)".
- Backlog agent (Martin, round 1): Social media manager/strategist.

## 2026-11-03 — Checkpoint 1, round 3 (4 cards)
- Sites: "Suriya, Hüwel, Stürzl, Bali Healing (Recommended)" — start narrow, extend per Go.
- Trigger: "Handoff from client chats + grill plan (Recommended)" — tasks arrive in the agent's inbox folder (client, page, spec, done-definition); no self-invented work.
- Risk list beyond send/spend/delete/publish: Martin picked ONLY "Supabase writes and portal tables". Client-visible changes, Ads changes and automation edits were NOT picked as card-enforced items in this list; the existing memory rules for them (`no-website-changes-without-go`, `ads-changes-need-reasoned-go`) stay in force as house rules and are cited in the template as such.
- Done means: "Staging + both screenshots + QA list + swap plan (Recommended)".

## 2026-11-03 — Checkpoint 1 (Design go)
GATE PASSED (cp1) shown in full. Card answer: "Go, build the skill (Recommended)" — confirmed. Proceeding to Step 3.

## 2026-11-03 — Checkpoint 2 (Ship go)
GATE PASSED (cp2) shown in full, scorecard 96.7 %. Card answer: "Go, register, commit, document, install (Recommended)" — confirmed. Proceeding to Step 5. Placing `webdev.md` into `.claude/rules/agents/` stays a separate card after the install.

## 2026-11-03 — after install
- Place webdev: "Go, place it now (Recommended)" — placed at `.claude/rules/agents/webdev.md`, roster active, `_run.json` written.
- Friday hook-in: "Yes, send the task to the Morning Grill session (Recommended)" — task sent to the Morning Grill session; it edits its own skill with its own Go.

## 2026-11-03 — Run 2: Sales Director (write mode, 2 card rounds)
- Active today (Martin's words): "we have Gayo and one or two other people who are actually reaching out via LinkedIn DM. (I think it could be an idea to also have scheduled LinkedIn posting in it, just to get more views.) Then we sent the review pages Loom, plus the videos that are already analysed, over there, and people who are interested book a call" + LinkedIn (own seat), review pages + Loom, booking sequence + pitch calls. Cold email, HubSpot reactivation, affiliates, Meta lead magnet = dormant.
- Owns: "Overview + weekly brief + proposals + light research (Recommended)".
- Research: "Weekly, 60-minute cap, one source per week (Recommended)".
- Pipeline SoT: "CRM sheet Pipeline tab + prospects folders (Recommended)".
- LI posting: "Yes, as a posting calendar with proposals (Recommended)" — post text via /741-post or /personal-post per Go.
- Outreach team: "Reads their numbers, one team line per week, no messages to them (Recommended)".
- Goal number: "Booked calls per week (Recommended)" — target set on the first Friday review.
- Cadence: "Monday pipeline brief as a grill card + Friday review (Recommended)".

- Place sales-director: "Go, place it now (Recommended)" — placed at `.claude/rules/agents/sales-director.md`, roster active.
