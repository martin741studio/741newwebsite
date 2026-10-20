# Inventory — what the client sees and what data exists

Date: 2026-10-13. Sources: live portal `clients.741.studio` (admin view of Bali Healing, code read from `_src/portal-live.html`), report folders `/r/<hash>/`, `tracking-metric-catalog.json`, `balihealing-seo-roadmap.html`.
Screenshots: scratchpad of the session (roadmap top, status table, tracks, AI table, portal admin view).

## 1. Portal parts (client view)

Tabs for a client in program mode: Übersicht · Entscheidungen (if on) · Sichtbarkeit (if citations) · Berichte · Anfragen (if on) · Kontakte (if on).

| ID | Part | Shows today | Source |
|---|---|---|---|
| P1 | Welcome + tabs | name, sub text, tab row with count pills | `renderClientTabs` |
| P2 | Week video | one Loom per programme week, global | `week_videos` |
| P3 | Onboarding | 6 steps, progress bar, DPA signature | `onboarding_steps`, `avv_signatures` |
| P4 | 90-day programme | chips W1–W13, task list of the current week | `tasks` (template copy) |
| P5 | Access | 7 platforms, status, invite mail, how-to | `access_grants` |
| P6 | Support chat | message history, WhatsApp emergency button | `messages` |
| P7 | Activity feed | counter "actions this week" + dated lines | `activity_log` |
| P8 | Materials | file upload | `materials` |
| P9 | Reports | flat list: title, period, date, Open | `client_reports` |
| P10 | Page change requests | list, empty | `page_change_requests` |
| P11 | Entscheidungen | variants, deadline, record | approval tables |
| P12 | Sichtbarkeit | directory listings x/y live | `client_citations` |
| P13 | Anfragen | lead list (staging, 0 rows) | `leads` |
| P14 | Kontakte | contact list (Hüwel only) | `client_stack.contacts` |
| P15 | Kundenarbeit | work items, owner, proof (admin first) | `work_*` |
| P16 | Ergebnisse | designed, not installed | tracking tables (new) |

## 2. Report page blocks (hand-built HTML per client, 14 types seen)

| ID | Block | Example | Data shape |
|---|---|---|---|
| R1 | Status header: 4 KPI cards | Bali roadmap: clicks 599, position 10.8, WhatsApp 313, Ads paused | 4 numbers + context line |
| R2 | Blocker table | 5 rows: blocker, effect, fix, who | table |
| R3 | Request status table | 7 rows, status pill, next step | table |
| R4 | What we built | 3 rows | table |
| R5 | Four-week plan | 4 rows: week, what, who | table |
| R6 | Decisions needed | 6 rows | table |
| R7 | Roadmap track items | 12 items: why, outcome, timing, owner, findings | card + text |
| R8 | Backlink data | magazines, directories, reclaim list, toxic links | tables + prose |
| R9 | GBP audit | 23 services, categories, opening date | list |
| R10 | Map grid report | Wellness 18 keywords, Beauty 14, share-of-local-voice %, grid images behind a toggle | table + images |
| R11 | Contact tracking | 6 months: calls, website clicks, directions, WhatsApp | table |
| R12 | AI visibility | 16 keywords x 3 platforms, % + word (strong/mid/weak) | table |
| R13 | Reviews, schema, tracking, internal links, competitor benchmark | prose + tables | mixed |
| R14 | Other page types | Google Ads weekly report, week-1 baseline (15 sections), site tree plan, text drafts per page, preview pages, GBP recommendation, positioning | mixed |

## 3. Data points (by the question the client asks)

Cadence: D = daily pull, W = weekly, M = monthly, Q = quarterly, E = event. "Cat." = metric id in `tracking-metric-catalog.json` where one exists.

### Q1 — Do I get more enquiries and customers?
| ID | Data point | Cat. | Unit | Cadence | Shown today |
|---|---|---|---|---|---|
| D01 | Phone calls from Google profile | M01 | count/week | D→W | R11 table |
| D02 | Website clicks from Google profile | M02 | count/week | D→W | R11 table |
| D03 | Direction requests | M03 | count/week | D→W | R11 table |
| D04 | Profile views (impressions) | M04 | count/week | D→W | not shown |
| D05 | WhatsApp clicks from the site | GA4 | count/day | D | R1 card, R11 table |
| D06 | Form leads | M05 | count/week | E | P13 (empty) |
| D07 | Leads the client adds by hand | M06 | count/week | E | not shown |
| D08 | Booked jobs (client ticks) | M08 | count/month | E | not shown |
| D09 | Value per booked job | M09 | EUR/month | M | not shown |
| D10 | Cost per booked job | M11 | EUR | M | not shown |
| D11 | Cost basis: 741 fee + ad spend | M10 | EUR/month | M | not shown |

### Q2 — Am I easier to find?
| ID | Data point | Cat. | Unit | Cadence | Shown today |
|---|---|---|---|---|---|
| D12 | Share of the map where I show in top 3, per keyword | M13 | % | M | R10 table |
| D13 | Average rank on the map per keyword | M14 | rank | M | R10 table |
| D14 | Grid image per keyword (7x7 points) | M15 | image | M | R10 behind toggle |
| D15 | Competitors on the same keyword | M16 | table | M | R13 two rows |
| D16 | Google Search clicks (28 days) | M21 | count | W | R1 card |
| D17 | Google Search average position | M21 | rank | W | R1 card |
| D18 | Top search queries and pages | M22 | table | M | R13 prose |
| D19 | Keyword rank in normal results | M23 | rank | M | not shown |
| D20 | Share in AI answers (ChatGPT, Gemini, Google AI) | M30 | % x 3 | Q | R12 table |
| D21 | Search demand per month for my topics | M33 | count | Q | R7 prose |

### Q3 — Do people trust me?
| ID | Data point | Cat. | Unit | Cadence | Shown today |
|---|---|---|---|---|---|
| D22 | Review count and rating | M17 | count, stars | D | R13 prose |
| D23 | New reviews per month (velocity) | M18 | count | M | R13 prose |
| D24 | Review gap to the local leader | M19 | count | M | R13 table |
| D25 | Unanswered reviews | M20 | count | D | R1 blocker row |

### Q4 — What does 741 do, what is stuck, what do you need from me?
| ID | Data point | Unit | Shown today |
|---|---|---|---|
| D26 | Programme week and phase | week of 13 | P4 chips |
| D27 | Work items: open, doing, to check, done, owner, proof | list | P15 |
| D28 | Blockers with effect, fix, owner | list | R2 table |
| D29 | Client requests and status | list | R3 table |
| D30 | Decisions needed from the client | list | R6 table, P11 |
| D31 | Next four weeks | list | R5 table |
| D32 | Onboarding steps | 6 steps | P3 |
| D33 | Platform access status | 7 platforms | P5 |
| D34 | Last update from 741 (days) | days | not shown |
| D35 | Early warnings (profile changed, site down, reviews drop) | alert | not shown |

### Q5 — What does my ad money do?
| ID | Data point | Unit | Shown today |
|---|---|---|---|
| D36 | Ad status (running, paused, why) | status | R1 card |
| D37 | Spend, clicks, WhatsApp clicks, cost per click, cost per WhatsApp click | IDR / EUR | R14 weekly report, R1 text |

### Q6 — What is the plan?
| ID | Data point | Unit | Shown today |
|---|---|---|---|
| D38 | Roadmap tracks and their state | 12 items | R7 |
| D39 | Site structure (35 pages, two paths) | tree | R14 |
| D40 | Content plan (45 topics, 19 priority) | list | R4 |
| D41 | Backlinks: outreach funnel (requests, replies, offers, live links) | funnel | R7 prose |
| D42 | Backlink quality: links, domains, broken, spam | numbers | R8 |
| D43 | Directory listings live x of y | count | P12 |
| D44 | Page text drafts and previews for approval | pages | R14 |

### Q7 — Is the site and profile healthy?
| ID | Data point | Unit | Shown today |
|---|---|---|---|
| D45 | Site up/down, tracking tag present | status | not shown |
| D46 | Profile change watch (name, category, hours) | diff | not shown |
| D47 | Profile verification state | status | not shown |
| D48 | Schema, internal links, GBP completeness | pass/fail | R9, R13 |
| D49 | Visibility score vs ranked clinics (45 of 100) | score | R4 one line |

## 4. Problems with evidence (13.10.2026)

| # | Problem | Evidence |
|---|---|---|
| 1 | The Overview shows no result number. | Admin view of Bali: video, onboarding, access, chat, feed, materials. No KPI. |
| 2 | Contradicting state. | "Onboarding 1 of 6 steps" next to "Week 5 of 13". |
| 3 | Mixed language. | German buttons ("Speichern", "Offen") next to English titles. |
| 4 | Dead feed. | "0 actions this week"; lines from 19.08. |
| 5 | Flat report list, wrong dates. | Roadmap shows "Status 13 Oct 2026 · live tracking · 23.09." |
| 6 | Report is a wall. | 10,529 px, 22,758 characters, 12 tables, no chart. |
| 7 | Numbers sit in tables that need a chart. | 6-month contact table, 16x3 AI table, 18 grid keywords as rows. |
| 8 | Words the client cannot read. | SoLV, SAIV, NAP, DA, ARP, PBN, reclaim, entity. |
| 9 | Several jobs in one page. | Status, plan, scans, tracking, AI, backlinks, competitors. |
| 10 | Internal text on the client page. | "per SQL/Claude als Report verknüpfen". |
| 11 | Stale footer. | "v2, reviewed 23 Sep 2026" under a v3 page. |
| 12 | Colour carries no meaning. | Status pills in grey/amber/green without a rule. |

## 5. Open
- Which data points we show at all (49 listed; the client should see far fewer on the first screen).
- One visual form per data point.
- Where each point lives: first screen, results tab, report, or hidden.
- Order and naming of tabs.
