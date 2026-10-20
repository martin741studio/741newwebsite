# Area D: Status, plan, work and decisions

Date: 2026-10-13. Scope: D26–D33, D38–D40, D43, D44 (see `00_project/client-dashboard-redesign/01-inventory.md`).
Fits with: `client-work-visibility` (four blocks for the client: where we stand, what is next, what we need from you, who to ask) and `client-approval-workflow` (decision card with 3 buttons, deadline, "741 empfiehlt").
Screenshots are for internal decisions only. They never go into client files. In client files, say "741 Dashboard-Raster". Never name these sources.
Quotes: none longer than 15 words. All other text is paraphrase.

## 1. Sources

All pages were fetched live on 2026-10-13 with firecrawl (markdown and screenshot). "Current" means a live product page or doc fetched that day. "Evergreen" means the idea is old and stable, or the post is older than 3 months.

| id | Name | URL | Fetched | Type | Status | Screenshot |
|---|---|---|---|---|---|---|
| S01 | Linear Docs: Initiative and project updates | https://linear.app/docs/initiative-and-project-updates | 2026-10-13 | product doc | current | `refs/01-linear-project-updates.png` |
| S02 | Carbon Design System: Status indicators | https://www.carbondesignsystem.com/building-blocks/core/patterns/status-indicators | 2026-10-13 | design system | current | `refs/02-carbon-status-indicators.png` |
| S03 | Shopify dev docs: Setup guide composition | https://shopify.dev/docs/api/app-home/latest/patterns/compositions/setup-guide | 2026-10-13 | design system | current | `refs/03-shopify-setup-guide.png` |
| S04 | GOV.UK Design System: Task list | https://design-system.service.gov.uk/components/task-list/ | 2026-10-13 | design system | current | `refs/04-govuk-task-list.png` |
| S05 | Basecamp: Hill Charts | https://basecamp.com/hill-charts | 2026-10-13 | product page | evergreen (idea is years old, page date unverified) | `refs/05-basecamp-hill-charts.png` |
| S06 | Assembly: client portal for marketing agencies | https://assembly.com/solutions/marketing-agency-client-portal | 2026-10-13 | agency portal vendor page | current | `refs/06-assembly-agency-client-portal.png` |
| S07 | Atlassian Statuspage: Top-level status and incident impact | https://support.atlassian.com/statuspage/docs/top-level-status-and-incident-impact-calculations/ | 2026-10-13 | product doc (page last modified 2025-09-25 per its metadata) | current | `refs/07-atlassian-statuspage-top-level.png` |
| S08 | GitHub Docs: Customizing the roadmap layout | https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout | 2026-10-13 | product doc | current | `refs/08-github-projects-roadmap.png` |
| S09 | Asana Help: Project progress and status updates | https://help.asana.com/s/article/project-progress-and-status-updates | 2026-10-13 | product doc | current | `refs/09-asana-project-status-updates.png` |
| S10 | Forge: New-client welcome packet (post, 2026-06-05) | https://forge.so/blog/new-client-welcome-packet | 2026-10-13 | agency tool blog | evergreen (older than 3 months) | `refs/10-forge-welcome-packet.png` |
| S11 | Linear Docs: Project milestones | https://linear.app/docs/project-milestones | 2026-10-13 | product doc | current | `refs/11-linear-project-milestones.png` |
| S12 | Shopify Polaris: Badge | https://shopify.dev/docs/api/app-home/latest/web-components/feedback-and-status-indicators/badge | 2026-10-13 | design system | current | `refs/12-polaris-badge.png` |
| S13 | Shopify Polaris: Banner | https://shopify.dev/docs/api/app-home/latest/web-components/feedback-and-status-indicators/banner | 2026-10-13 | design system | current | `refs/13-polaris-banner.png` |
| S14 | GOV.UK Design System: Complete multiple tasks | https://design-system.service.gov.uk/patterns/complete-multiple-tasks/ | 2026-10-13 | design system | current | `refs/14-govuk-complete-multiple-tasks.png` |
| S15 | Carbon Design System: Tree view | https://www.carbondesignsystem.com/building-blocks/core/components/tree-view/guidelines | 2026-10-13 | design system | current | `refs/15-carbon-tree-view.png` |
| S16 | Linear Docs: Initiatives (health colours) | https://linear.app/docs/initiatives | 2026-10-13 | product doc | current | `refs/16-linear-initiatives-health.png` |

16 sources, 16 screenshots.

Not fetched or not used:
- Stripe setup checklist: the search returned only third-party noise. No live Stripe page was fetched.
- Vercel deployment status: the search returned only build-error and queue pages. Not fetched.
- SuiteDash, Dubsado, Productized, ClientPortal.io, Notion roadmap: not fetched. S06 and S10 cover the agency-portal idea.
- Basecamp "working with clients": found only as videos. Skipped.
- No page was blocked. The Asana page text showed a blocked tracker script. The content still loaded.
- The screenshots are rendered pages. Several show docs, not the product UI. Look at the linked page for the live widgets.

## 2. Findings per reference

- S01: A project update is one health word (on track, at risk, off track) plus free text. The latest update sits on the project overview, and an Updates tab keeps the history.
- S01: A missed update shows "Update Missing" after one reminder cycle plus 3 days (when the last update was on track). A long silence turns the icon grey. A silent project cannot stay green.
- S01: A "Write with Agent" button drafts the update from recent changes. A person edits and publishes it.
- S16: The initiative list rolls up project health in four colours. Green is on track, yellow is at risk, red is off track, gray is no current update.
- S11: Each milestone shows a completion percentage. A diamond icon marks the milestone in focus. This is a "you are here" marker.
- S02: A status needs at least 3 of 4 signals: colour, shape, symbol, text. Gray means not started or draft. Colour alone fails.
- S02: Icon indicators suit high-attention items. Shape indicators suit dense lists. Use a legend only when a label does not fit.
- S12: Badges use 1–2 word labels in past tense. The same status keeps the same tone everywhere. A large badge shows the main status at the top of a page.
- S13: A banner holds one message or one action. Warning and critical banners need a clear action button. Banners do not queue, so two banners fight each other.
- S07: The top-level status is calculated from the component statuses. One major outage gives a "partial" top status, not a full red. A person can override the impact of an incident.
- S07: Every component has one of five states with a fixed colour. Incident impact has its own scale (none, minor, major, critical).
- S04: Each row has a task name, an optional hint and a status on the right. "Completed" is plain text with no background, so open tasks stand out.
- S04: "Cannot start yet" is grey text and the row is not a link. Red is allowed only for an error state.
- S14: The task page opens at the start and at each return visit. Tasks sit in groups under short headings, in any order. The user can mark a task complete.
- S03: The setup guide has a header with "x out of y steps completed", a dismiss button, a collapse toggle and expandable steps. Each step has one primary button.
- S08: The roadmap view puts items on a timeline from start and target dates. Vertical markers show iterations or milestones. Zoom changes the time span.
- S09: A project has six statuses: on track, at risk, off track, on hold, complete, dropped. The overview shows a dot strip of past statuses.
- S09: A published update freezes. Later edits to a task do not change the old update. This gives a true history.
- S05: A hill chart puts each track on a hill. Uphill means still working out the approach. Downhill means executing. A person sets the dot, not a formula.
- S05: A dot that never moves is a sign that the track is too big. The team splits it.
- S10: A client welcome page has 7 parts. Two matter here: a 30/60/90 timeline and "what we still need from you" (access, assets, decisions).
- S06: The portal layout can show only the most relevant tools. Tasks can be assigned to the client for approvals, content review and asset delivery. This is a vendor claim.
- S15: A tree has branch nodes with a caret and leaf nodes. Use it only for 2 or more levels. For one level use an accordion. For many columns use a data table.
- S15: Every node needs an icon, or no node gets one. Mixed icons break the alignment.

## 3. Patterns

### P1. One-sentence health banner (traffic light)
- Form: one banner on top. Colour, shape, one word, one sentence, one owner or next step. Example: "On track. Week 5 of 13. Next: your OK on the home page text."
- Evidence: S01, S07, S13, S02, S16.
- Rule: the colour is the worst colour below it. The banner also states the count ("1 blocked, 2 need you"). So a red item never hides under a green banner.
- Rule: if 741 posts no update for 10 days, the banner turns grey with "No update since <date>". Source idea: S01 staleness (missed update, then grey). The 10-day limit is a proposal. It assumes a weekly update.
- Use: top of the client page and top of each tab that shows a plan.
- Avoid: two banners at once (S13 has no queue). Avoid banner text longer than one sentence. Avoid a green banner with no reason.

### P2. "Needs you" box on top
- Form: one box above everything else. One card per ask. Each card has one action button. Max 3 cards visible, then "show all".
- Evidence: S13 (one action per banner), S10 (what we need from you), S06 (client tasks), `client-work-visibility` (lane "what we need from you").
- Empty state: "Nothing needed from you now." with the green check. An empty box is good news and must say so.
- Use: always, in the client view.
- Avoid: mixing 741 tasks into it. Avoid a dismiss button on open decisions (S13 says dismiss only if no immediate action is required).

### P3. Phase timeline with "you are here"
- Form: 4–5 phases for the 13 weeks. A marker on the current phase. Text above: "Week 5 of 13". Progress inside a phase comes from real tasks, not from the calendar.
- Evidence: S11 (milestone %, focus marker), S08 (timeline, vertical markers), S10 (30/60/90).
- Fits the decision of 13.10.: the 13 weeks stay as phases, real tasks sit below.
- Use: D26 and D31.
- Avoid: a Gantt bar per task. Avoid exact dates that 741 cannot keep. Avoid a phase list that disagrees with the onboarding count (today: "1 of 6" in week 5).

### P4. Short grouped list for the client, lanes for the team
- Form: three groups: "Needs you", "741 is working on", "Done recently" (collapsed). One row = a verb title, an owner name, a status shape and, when done, a proof link.
- Evidence: S04 and S14 (grouped task list, any order, completed shown plain), S09 (history stays).
- Judgement, `unverified`: no source tests lanes versus lists with non-expert clients. The choice rests on the small item count (about seven items for each client) and on the 4-block decision. Kanban lanes stay in the admin and team views.
- Use: D27, D29.
- Avoid: showing internal notes, hours and agent steps (decision of 13.10.). Avoid "done" without a proof link.

### P5. Checklist with progress that hides when done
- Form: header "x of y done", expandable steps, one primary button per open step. When all are done, the card collapses to one line ("Setup complete") and then leaves the first screen.
- Evidence: S03 (count, dismiss, expand), S04 (status per row), S14 (completion).
- Rule: ticks come from data (signed forms, access grants), not from a manual click. This stops "1 of 6" in week 5.
- Rule: a step that is still open after week 2 turns amber and moves into the "Needs you" box. This is a proposal.
- Use: D32, D33, D43.
- Avoid: showing the same step in two places with two different counts.

### P6. Blocker card with effect and fix
- Form: title in client words; "What it costs you"; "What fixes it"; owner; "Open since <date>". One card per blocker.
- Evidence: S07 (impact comes from the affected parts), S13 (heading, body, action), S04 (red only for a real problem).
- Use: D28. Red only if the effect is real today. Otherwise amber.
- Avoid: a table of 5 rows with 4 columns (today's R2). Avoid wording that blames the client. Avoid an effect with no real data (rule `claims-need-real-data`).

### P7. Decision card with deadline
- Form: title; one line why it matters; options (2–3) with one marked "741 recommends"; deadline date; what happens if silent; three buttons (approve, approve with a small change, request a change).
- Evidence: S13 (single action, buttons), S10 (feedback and approval process with turnaround), plus the existing rules in `client-approval-workflow`.
- Rule from that brief: price, health and legal items always need an active yes. A silent default after 7 days needs written consent. One approver per client.
- Use: D30, D44.
- Avoid: more than 3 cards at once. `unverified` source for the limit; it is a design guess. The approval brief cites decision-fatigue research. I did not re-check it here.

### P8. Site tree as an expandable outline
- Form: levels 1–2 open, deeper levels closed. One status badge per page. A count per branch ("4 of 9 live"). Two top branches for the two paths.
- Evidence: S15 (branch and leaf, caret, same icon on every node), S12 (badge in its own place, same tone for the same status).
- Rule: a closed branch shows the worst status of its children. This extends the selected-state idea in S15. It is my adaptation.
- Use: D39.
- Avoid: a tree for one level (S15 says use an accordion). Avoid extra columns in the tree; switch to a table if you need them.

### P9. Status post with a history strip
- Form: a short post: health word, 2–3 sentences, date, author. Below it, a strip of dots for the last 6 updates. Old posts stay frozen.
- Evidence: S01 (health plus text, Updates tab), S09 (dot strip, frozen updates), S01 (agent drafts, person publishes).
- Use: top of the client page, under the banner. It also gives D34 (last update in days) for free.
- Avoid: an update written by an agent and sent without a human check.

### P10. Three-stage track state
- Form: each of the 12 tracks sits in one of three stages: "Working out", "Doing", "Done". A person sets the stage. A one-line outcome sits under the title.
- Evidence: S05 (uphill and downhill, human-set), S11 (stages of a project).
- Use: D38.
- Avoid: the hill drawing itself for clinic owners. `unverified`: no source tests the hill with non-experts. The three-stage version keeps the idea and drops the abstract chart.

## 4. One colour and word rule (never conflicts)

Basis: S02 (palette meanings, 3 of 4 signals), S16 (green, yellow, red, gray roll-up), S04 (red only for problems, grey for "not yet"), S12 (same tone for the same status), S07 (fixed colour per state, calculated top status).

Two layers. They never share a colour.
- Layer 1, health. Uses colour. Answers: "Is this fine, or does it need someone?"
- Layer 2, progress. Uses shape and plain dark text. Answers: "How far is it?" States: Planned, In progress, To check, Done.

| Colour | Meaning (fixed) | EN words | DE words (proposal) | Shape | Never use for |
|---|---|---|---|---|---|
| Green | Fine. Nobody must act. | On track, Live, Approved | Im Plan, Live, Freigegeben | filled circle with check | missing data; "done" rows in lists (they stay plain, see S04) |
| Amber | Needs attention soon. Someone must act. No harm yet. | Needs you, Waiting, At risk, Due soon | Braucht dich, Wartet, Gefährdet, Bald fällig | triangle | anything that is already hurting |
| Red | Stopped or late. It costs the client now. | Blocked, Off track, Overdue | Blockiert, Hinter Plan, Überfällig | filled octagon | warnings, drops in a number, anything without a real effect |
| Grey | Not started, paused, not needed, or no data. Not a judgement. | Planned, On hold, Not needed, No data yet | Geplant, Pausiert, Nicht nötig, Noch keine Daten | empty circle or dash | anything with data |

Rules:
1. One word, one colour. "Waiting" is always amber. "Planned" is always grey.
2. A colour shows its reason in words next to it. Example: "Amber: 2 access items open for 6 days."
3. "No data" is grey. Never green. Never amber.
4. Show colour, shape and word together (3 of 4 signals, S02). Never colour only.
5. Red is only for real effect today (S04). If in doubt, use amber.
6. The banner colour is the worst child colour. It also shows the count (P1).
7. Done rows are plain text with no colour (S04). Open rows then stand out.
8. These four colours do not appear in charts or in number deltas in any other area. Charts use their own palette. Otherwise a red chart line looks like a "blocked" state.
9. No blue status. Blue stays for links and buttons only.
10. All labels come from one table per language. No mix of German and English in one view (problem 3 in the inventory).

Automatic colour (proposal for Martin). Martin chose "fully automatic from signals" on 13.10. These thresholds are my draft and `unverified`:
- Red: a blocker with an effect today, or a task past its due date.
- Amber: a client action open more than 3 days, or a due date within 7 days, or an update missing. The 3-day mark matches the reminder rule in `client-approval-workflow`.
- Grey: no update for 10 days, or no data.
- Green: none of the above.

## 5. Recommendation per data point

| ID | Best form | Alternative 1 | Alternative 2 | One risk |
|---|---|---|---|---|
| D26: Programme week and phase | P3 phase timeline with "you are here" and "Week 5 of 13" above it | Segmented bar with one phase name | One sentence only ("Week 5 of 13: build phase") | Template phases may not match the real work. Then the marker lies. Take phase progress from real tasks. |
| D27: Work items (open, doing, to check, done, owner, proof) | P4 grouped list: Needs you, 741 is working on, Done recently | Table with filters (admin and team only) | Kanban lanes (admin and team only) | Internal notes or agent noise leak into the client view. Also "done" without proof. |
| D28: Blockers (effect, fix, owner) | P6 blocker card, one per blocker | One row inside "Needs you" if the client owns the fix | Compact 3-column table if there are 4 or more | Red overuse, or wording that blames the client. Effect must use real data. |
| D29: Client requests and status | P4 list with 4 steps: Received, In progress, Ready to check, Done (shape plus word) | Filter "My requests" inside the D27 list | Ticket cards with timestamps | Two lists for one idea (requests and page change requests). Merge them under one filter. |
| D30: Decisions needed | P7 decision card inside the "Needs you" box | One row with a "Decide" link into the Entscheidungen tab | Daily digest mail only | Silent approval after 7 days needs written consent. Price, health and legal need an active yes. |
| D31: Next four weeks | Four week cells on desktop, a stacked list on mobile. 1–3 items each, with an owner chip (741, You, Google) | Mini timeline (S08 style, 4 cells) | Plain list of 4 lines | A date that slips. Show "moved from week 2" and keep grey for planned items. Never edit silently. |
| D32: Onboarding steps | P5 checklist with "x of y", ticks from data, hides when done | Only the open steps as cards in "Needs you" | One line "Setup complete" after week 2 | Contradicting counts ("1 of 6" in week 5). Open steps after week 2 go amber and into "Needs you". |
| D33: Platform access status (7) | One compact list of 7 rows. One badge each: Connected, Needs you, Not needed, Checking. How-to link only on rows that need action. Show "checked on <date>". | Merge into D32 as one step with 7 sub-rows | 7 tiles in a grid | Wrong status after a later revoke. Show the check date. Note: D32 and D33 may overlap (P3 and P5 in the inventory). `unverified`; confirm in the portal code. |
| D38: Roadmap tracks (12) | P10 three-stage groups with one-line outcome per track. Detail opens on click | Roadmap rows on a timeline (S08 style) | Grouped by the client question: more enquiries, easier to find, more trust | 12 items read as a wall. Keep the "findings" text behind the click and in the report. |
| D39: Site structure (35 pages, 2 paths) | P8 expandable outline with a badge per page and a count per branch | Table with rows expandable one level (use when columns are needed) | Static site-map picture for the report and print | Deep levels on a phone. Also two sources for status (tree and D44). Use one source. |
| D40: Content plan (45 topics, 19 priority) | Priority list: the 19 first, the other 26 under "Later". Header "x of 19 live". One badge per topic | Month calendar (S08 style) | Filterable table | Topic names are keywords the client cannot read. Use a plain title and keep the keyword in a hover or detail. |
| D43: Directory listings x of y | Meter "x of y live" with the number in text. Open items collapsed under "show open" | Checklist per directory with a badge | Stacked bar: Live, In review, Not started | The total y changes and reads as a step back. Fix y per quarter. Show "added" items apart. |
| D44: Page drafts for approval | P7 decision card per draft ("Home page text ready, review by <date>") that opens the approval view | Preview link with before and after | Table with one row per page | Many cards at once cause fatigue. Release them in small batches. Run the HWG check before a card goes out. |

## 6. Three layouts: "What 741 does and what you need to do" with a decision card

### Decision card (same in all three layouts)

```
+--------------------------------------------------------------+
| [amber triangle] Needs you          Reply by Fri 16 Oct      |
| Choose the price for a single session                        |
| Why: it sets the price on the page and in the Google profile |
|                                                              |
| (o) 95 EUR  - 741 recommends                                 |
| ( ) 85 EUR                                                   |
|                                                              |
| [Approve]  [Approve with a small change]  [Request a change] |
| If you do not reply: we keep this open and remind you.       |
+--------------------------------------------------------------+
```

- The values are examples. The card mirrors the Suriya price item in `client-approval-workflow`. For price, health and legal items the last line says "we keep this open". Only other items may say "we use our recommendation after 7 days", and only with written consent.
- Labels follow the client language (`clients.lang`). In English: "741 recommends". In German: "741 empfiehlt".
- Buttons come from the approval brief (3 fixed buttons).

### Layout A: two columns "741 does" and "You do"
```
+--------------------------+  +-----------------------------+
| 741 is working on        |  | Needs you (2)               |
|  o Home page text  doing |  |  [decision card]            |
|  o Google profile  doing |  |  [access: Google Ads]       |
|  o Site map        planned|  |                             |
| Done recently (3)  v     |  | Next: week 6               |
+--------------------------+  +-----------------------------+
```
- Good: the split is clear at a glance on a wide screen. Both sides stay the same height.
- Risk: on a phone the order flips. "741 does" comes first unless you force "Needs you" on top. Most people read left to right, so the ask can sit in the second column.
- Fit: needs a second column of width. Works only at 1024 px and wider.

### Layout B: "Needs you" first, then plan, one column (recommended)
```
[banner]  On track. Week 5 of 13. 2 things need you.
+- Needs you (2) -------------------------------------------+
|  [decision card]                                          |
|  [access card]                                            |
+-----------------------------------------------------------+
Phase line:  Setup - Build [you are here] - Grow - Review
741 is working on (3)  list with owner and status
Next four weeks        4 cells
Done recently (3)      collapsed, proof links
Who to ask             name, WhatsApp button
```
- Good: maps 1:1 to the four client blocks already decided (where we stand, what is next, what we need from you, who to ask). The ask is always first, also on a phone. The same stack works at 390 px.
- Risk: it is long. Keep "741 is working on" to 5 rows, and fold the rest.
- Fit: best match for `client-work-visibility` and the live Entscheidungen module.

### Layout C: weekly update post (Linear and Asana style)
```
+-----------------------------------------------------------+
| [green circle] On track           Update of 13 Oct, Martin |
| This week we finished the Google profile text. Next we...  |
|                                                           |
| Done (3)        | Next (3)           | Needs you (2)      |
|  o ...          |  o ...             |  [decision card]   |
| History: o o o o o o   (last 6 updates)                    |
+-----------------------------------------------------------+
```
- Good: it reads like a message from a person. It builds trust and gives a history (P9). It fits the "Ich-Form" voice.
- Risk: it needs a weekly human write-up. If the post is late it turns grey (P1) and the page looks neglected. The "Needs you" column is one of three, so it is the least prominent.
- Fit: good as a second element under the banner in layout B. Weaker as the main layout.

Recommendation (Martin decides): layout B as the frame, with the P9 status post inside the banner area. Layout A as a wide-screen variant is possible later.

## 7. Open points for the grill

1. Colour thresholds in section 4 (3 days, 7 days, 10 days) are drafts.
2. Does the onboarding list (P3 in the portal) overlap with access (P5)? Check the portal code before D32 and D33 are final.
3. German labels in section 4 are proposals. Check the form of address (du or neutral) per client.
4. Test with one real client (Bali, English) whether the three-stage track view (P10) is clear. No source tests it with non-experts.
5. Where do the 12 tracks end and the work items (D27) begin? Without a rule, the same job shows in both lists.
