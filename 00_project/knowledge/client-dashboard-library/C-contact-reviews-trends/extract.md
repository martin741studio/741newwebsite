# Area C — Contact trends and reviews

Date: 2026-10-13. Scope: D01–D05, D07–D08, D22–D25 (IDs from `00_project/client-dashboard-redesign/01-inventory.md`).
Internal use only. Screenshots are for decision cards. Tool names in this file stay internal. In client files use "741 Dashboard-Raster" and plain words.
Quote limit: no source is quoted. All findings are in our own words.

## 1. Sources

All pages fetched on 2026-10-13. "Current" = live product page or doc. "Evergreen" = design principle or post older than 3 months.

| ID | Name | URL | Fetch date | Type | Status | Screenshot |
|---|---|---|---|---|---|---|
| S01 | Google Business Profile Help: Business Profile performance | https://support.google.com/business/answer/9918094 | 2026-10-13 | Product doc | current | `refs/01-gbp-performance-help.png` |
| S02 | BrightLocal Help: Review Insights in Reputation Manager | https://help.brightlocal.com/hc/en-us/articles/360025096754-How-to-understand-Review-Insights-within-Reputation-Manager | 2026-10-13 | Product doc, sample report image | current | `refs/02-brightlocal-review-insights-help.png` |
| S03 | RevenueCat docs: Charts, incomplete periods | https://www.revenuecat.com/docs/dashboard-and-metrics/charts/charts-feature-incomplete-periods | 2026-10-13 | Product doc | current | `refs/03-revenuecat-incomplete-periods.png` |
| S04 | Datawrapper Academy: how to deal with missing data in line charts | https://www.datawrapper.de/academy/patchy-data | 2026-10-13 | Tool doc (page meta: updated 2026-02-24) | current (doc), principle evergreen | `refs/04-datawrapper-patchy-data.png` |
| S05 | Daydreaming Numbers: time series with an incomplete period (post of 2025-12-02) | https://daydreamingnumbers.com/how-to-show-time-series-data-with-incomplete-period/ | 2026-10-13 | Blog post | evergreen | `refs/05-daydreamingnumbers-incomplete-period.png` |
| S06 | Birdeye Help: Review Reports (article dated 2026-03-20) | https://support.birdeye.com/en/articles/12653724-understanding-birdeye-reports-review-reports | 2026-10-13 | Product doc | current | `refs/06-birdeye-review-reports.png` |
| S07 | Domo Learn: Spark line chart, what it is and when to use it (2026-05-27) | https://www.domo.com/learn/charts/sparkline-chart | 2026-10-13 | Vendor guide | evergreen | `refs/07-domo-sparkline-guide.png` |
| S08 | CDC COVE: Small multiples (updated 2026-01-09) | https://www.cdc.gov/cove/data-visualization-types/small-multiples.html | 2026-10-13 | Public design doc | current | `refs/08-cdc-small-multiples.png` |
| S09 | Vercepta: Features (review monitoring, V-Score, competitor benchmark) | https://vercepta.com/features | 2026-10-13 | Product page | current | `refs/09-vercepta-features-benchmark.png` (cookie banner covers part) |
| S10 | Google Analytics Help: Data freshness | https://support.google.com/analytics/answer/11198161 | 2026-10-13 | Product doc | current | `refs/10-ga4-data-freshness.png` |
| S11 | Datawrapper Academy: what to consider when creating line charts | https://www.datawrapper.de/academy/what-to-consider-when-creating-line-charts | 2026-10-13 | Tool doc (published 2024-06, updated 2026-02) | current (doc), principle evergreen | `refs/11-datawrapper-line-charts.png` |
| S12 | Reintech: Grafana annotations, context for time series | https://reintech.io/blog/grafana-annotations-context-time-series-data | 2026-10-13 | Blog post, no date shown | evergreen | `refs/12-grafana-annotations.png` |

12 sources, 12 screenshots.

### Skipped or not used
- Whitespark Reputation Builder page (`whitespark.ca/reputation-builder/`): fetched in search. It shows the vendor's own review widget, not a dashboard. No screenshot saved.
- Podium and Grade.us: no dashboard doc fetched. One third-party comparison says Grade.us has no competitor module. That is a second-hand claim. `unverified`.
- Sterling Sky page on GBP metrics: seen only as a search excerpt. Not scraped. Its main point (calls = taps on the call button) is covered by S01.
- GBP product UI itself: it needs a login. No live screenshot. S01 is the help page, not the dashboard.
- GA4 trend cards: no public page shows a live card. S10 covers only the data delay. Card layout from GA4: `unverified`.
- No source was blocked by a paywall or bot wall.

## 2. Findings per reference

One line each. Each line names the exact element.

- S01: The "Performance" tab shows Interactions, Views, Directions, Calls and Website clicks with a date range and an "Apply" button.
- S01: "Calls" counts taps on the call button, not answered calls. "Views" counts each person once per day.
- S01: "Directions" is adjusted for repeat taps, cancelled requests and spam. Data exists only for verified profiles.
- S01: WhatsApp is not in the list. WhatsApp clicks must come from our own tracking. "Booking clicks" in S01 apply to hotels only.
- S02: The "Review Summary" shows two tiles: average star rating (big, filled) and total reviews (big, light).
- S02: The "Review Growth" chart is a cumulative area line. Toggle buttons switch between "All Reviews" and "New Reviews". A time dropdown sits beside them.
- S02: The sample report also has a star-rating donut and a review-source donut. Donuts are weak for 5 slices; skip them.
- S03: The doc says charts draw incomplete periods in a different style. The text does not describe the style. Style: `unverified`.
- S03: The doc tells readers to be careful when comparing an unfinished period with finished ones. It also calls an early rise a useful signal.
- S04: Typing "NA" or a dash in the data keeps a gap in the line. A "Connect all points" option closes the gap.
- S04: To show where data is real, use symbols on every point, stepped lines, or dashed lines for assumed parts.
- S05: Five ways for an unfinished period: annotate it, add a labelled estimate, compare like for like, break the line, show all years.
- S05: The post warns that a plain unfinished bar looks like a sudden drop. Omitting it hides an early signal.
- S06: "Review & ratings" has a view "Over time". It shows review count and average rating per period, as line, bar or table.
- S06: That chart adds projected data for the rest of the current month. Projection appears only when the range is longer than one day.
- S06: The "Compare period" menu offers "Previous period". A switch "View aggregated data" makes the chart cumulative.
- S06: The default range is the last 12 months. Response rate and response time have their own "Over time" charts.
- S07: Sparklines are not good with fewer than 5 points per series. 7 to 30 points work best.
- S07: Best pattern: current value, change indicator and sparkline in one cell. Column sparklines suit counts like call volume.
- S07: Gap, zero and connected line mean three different things: not collected, measured zero, assumed continuity.
- S07: Rows that are compared need the same axis. Otherwise a small change looks like a big one.
- S08: Small multiples fit line and bar charts. The doc suggests them for more than 5 series. We use 4 tiles because the scales differ, not because of the count.
- S08: Maximum 3 tiles per row on desktop. Always 1 tile per row on mobile. The legend becomes the tile title. Tooltips sync across tiles.
- S09: The "Battle Scan" compares review growth, sentiment and score with named local competitors.
- S09: The sample card shows two values per metric, for example score "94 / 78" and velocity "+24% / +8%". Which side is "you": `unverified`.
- S09: "V-Score" folds volume, rating, trend and response into one number. We do not copy this. It hides the parts.
- S10: Daily data can take 24 to 48 hours to settle. Numbers for recent days can still change. Some data arrives up to 7 days late.
- S11: Few values at fixed steps (monthly counts): use columns. Continuous change: use lines.
- S11: Add a highlight range where data turns into projection. Add annotations to explain breaks. Use grey for comparison lines.
- S11: Add a zero baseline when values come close to zero.
- S12: An annotation has a time (point or range), a text and tags. It shows as a line or shaded band. Hover opens detail.
- S12: The tag list includes business events such as a campaign or a launch. Automatic creation is better than manual notes.

## 3. Patterns (741 Dashboard-Raster, area C)

### P1 — Partial month
Rule 1: The month in progress is a lighter column with a hatched or outlined fill. Never the full colour.
Rule 2: Label it with the cut-off date, for example "1–13 Oct, so far".
Rule 3: No red, no down arrow, no "−x%" against a full month.
Rule 4: Compare like for like: "1–13 Oct" against "1–13 Sep". Or show no delta at all. (S05 strategy 3, S03 advice.)
Rule 5: No projection for counts below about 300 per month. Small numbers make projections noisy. A projection must carry the word "estimate" and a dotted fill. (S05, S06 shows projection; we choose not to use it by default.)
Rule 6: Mark the last 2 days of daily data as "still counting" for any GA4 number (D05). (S10.)

### P2 — Missing data against zero
Rule 1: Zero means "measured, and it was zero". A column of height 0 with the label "0".
Rule 2: Missing means "no data". Draw no column. Draw a dashed empty slot with the text "not tracked yet" or "not entered". (S04, S07.)
Rule 3: Never connect a line across a gap. Never fill a gap with zero or an average.
Rule 4: Put a marker where tracking starts: "WhatsApp tracking starts Aug". It explains the gap before it. (S12 pattern.)
Rule 5: A total that includes a missing channel carries a footnote: "WhatsApp not tracked before Aug".
Rule 6: Client-entered data (D07, D08) shows "not entered" until the client ticks. It never shows 0 by default.

### P3 — Events on the timeline
Rule 1: One thin vertical marker with a label of 2 to 4 words. For a range, use a light grey band. (S12.)
Rule 2: Maximum 3 markers per chart. More markers are noise.
Rule 3: Event types for clients: tracking started, ads paused or started, profile verified or changed, site change, page launched.
Rule 4: The event list comes from the work log (Kundenarbeit). We do not type markers by hand twice. (S12: automate.)
Rule 5: The September 9-day flatline: if we know the cause (tracking fault), show a grey band "no data recorded". If we do not know the cause, show the band with the text "no change recorded, we are checking". Never state a cause we did not verify.
Rule 6: Annotation text states facts only. No promise that the event caused the change. (S05, S11.)

### P4 — One chart per channel or one combined chart
Rule 1: Use one small tile per channel. Four tiles: calls, website clicks, directions, WhatsApp. (S08, S07.)
Rule 2: Each tile has its own scale. Values run from 9 to 300. One shared axis would flatten the small channels.
Rule 3: Each tile shows the max value on the axis or on the tallest column, so the scale is never hidden.
Rule 4: Show one combined number on top: "contact actions from Google". It is the sum of calls, website clicks and directions. Footnote what it contains. WhatsApp is added only where tracked.
Rule 5: Desktop: 2×2 tiles (the CDC limit of 3 per row holds). Mobile: 1 tile per row. (S08.)
Rule 6: A stacked combined chart is allowed only as a second view for the report page, never on the first screen.

### P5 — How many months to show
Rule 1: Show 6 months as columns. This matches today's table and gives enough shape for small numbers.
Rule 2: Show up to 12 months when 12 full months exist. (S06 default is 12 months.)
Rule 3: Do not use a sparkline for 6 monthly points. S07 asks for 7 or more points. Use mini columns with value labels instead.
Rule 4: A sparkline is allowed if it uses weekly points (about 26 for 6 months).
Rule 5: Bars for counts per period. Lines for cumulative or continuous values such as total review count. (S11, S02.)
Rule 6: Start the axis at zero for every count chart. (S11.)

### P6 — Value, change and shape in one card
Rule 1: Card = plain label, big number, change in words, 6 columns. (S07 pattern.)
Rule 2: One line of definition under the label: "Taps on the Call button in your Google profile." (S01 says calls are taps, not answered calls.)
Rule 3: Change in words: "12 more than last month". No percent for counts under 50.
Rule 4: The card carries one status colour at most. Colour follows a rule, not decoration.

### P7 — Review gap to the local leader
Three forms. Rules for each.
Form A, bar pair (or trio): horizontal bars "You", "Leader", "Target". Target = 2 times the leader (741 programme rule from memory note `program-deliverable-rules`; `unverified` for each client). The gap is one sentence: "You have 44. The leader has 120. The target is 240."
Form B, progress to target: one bar, filled to the share of the target. Label the fill with the count and the target. Good for a headline card.
Form C, velocity line: columns of new reviews per month (S02 "New Reviews" view) plus a dashed line for the pace needed to reach the target. Pace needed = (target − current) ÷ months left. That is our calculation. Label it "needed pace".
Rule 1: Use A or B for the status, C for the pace. A and C together answer "where am I" and "how fast must I go".
Rule 2: Name the leader as "the practice with the most reviews near you". Do not show a competitor name unless Martin approves.
Rule 3: The leader count is a snapshot with a date: "as of 13 Oct".
Rule 4: A cumulative line (S02 "Review Growth") is a fourth option. It needs history for the leader. History availability: `unverified`.

### P8 — Language for non-data people
Rule 1: Title is a question or a plain noun: "Did more people contact you?" Not "Interactions".
Rule 2: One sentence answer above each chart, written from the data. (S01 and AgencyAnalytics-style advice: show few action metrics. The AgencyAnalytics page was a search excerpt only. `unverified`.)
Rule 3: No jargon. Say "tapped Call" not "interaction". Say "people who saw your profile" not "impressions".

## 4. Recommendation per data point

Format: best form; two alternatives; one risk.

### D01 — Phone calls from Google profile
- Best: tile with big number, change in words, 6 monthly columns, current month hatched (P1, P4, P6).
- Alt 1: weekly mini column row (about 26 points) inside the tile.
- Alt 2: one row in a table with a "last 6 months" mini column cell (layout C).
- Risk: S01 says "calls" are taps on the call button. The client may compare with the phone log and doubt the number. Add the definition line.

### D02 — Website clicks from Google profile
- Best: same tile as D01.
- Alt 1: tile row in the table layout.
- Alt 2: number only, with a text line, if the clicks are very low.
- Risk: A profile click is not a site visit in our site analytics. Two numbers for "visits" will clash. Name it "taps on your website link".

### D03 — Direction requests
- Best: same tile as D01.
- Alt 1: table row.
- Alt 2: number card with the sentence "people asked for the route to you".
- Risk: Google adjusts the count for repeat taps and spam (S01). A change in method can shift old numbers. Whether Google restates history: `unverified`. Keep a note "as reported by Google on the pull date".

### D04 — Profile views
- Best: do not show on the first screen. Show as one muted line "People who saw your profile: 1,240" in the detail view.
- Alt 1: one column chart in the report page.
- Alt 2: omit.
- Risk: views are far larger than actions (S01 counts people once per day). Next to calls the ratio looks poor. It can make the client think the work fails.

### D05 — WhatsApp clicks
- Best: tile like D01 with a dashed "not tracked yet" slot before August and a marker "Tracking starts Aug" (P2, P3).
- Alt 1: number card "since tracking started".
- Alt 2: table row with the text "not tracked" in missing cells.
- Risk: three traps at once. Missing looks like zero. The 9-day flatline looks like a fact. The last 2 days are still counting (S10). Handle each with P1 to P3.

### D07 — Leads the client adds by hand
- Best: monthly columns in a "You told us" row under the Google tiles, with a clear label that the client entered the data.
- Alt 1: single count card with an "add lead" button.
- Alt 2: simple list of entries with dates.
- Risk: empty means "not entered", not "zero". Showing 0 punishes the client for not ticking.

### D08 — Booked jobs (client ticks)
- Best: monthly columns next to D07, label "You told us". A sentence links the two: "3 of 12 enquiries became a booked job".
- Alt 1: single number for the month.
- Alt 2: small funnel (belongs to area E).
- Risk: numbers are tiny (0 to 5). One missing month breaks the story. Self-reported data needs the "not entered" state (P2 rule 6).

### D22 — Review count and rating
- Best: two big tiles (rating with stars, total count) and a cumulative line of the count over 12 months. Same pattern as S02.
- Alt 1: tiles only, no line.
- Alt 2: rating split by stars as horizontal bars (not a donut).
- Risk: a rating on few reviews swings. A single 3-star review moves it a lot. Show the count next to the rating always.

### D23 — New reviews per month
- Best: monthly columns, current month hatched, with a dashed "needed pace" line (P7 form C).
- Alt 1: "New Reviews" toggle on the cumulative line (S02).
- Alt 2: one sentence: "6 new reviews in the last 3 months".
- Risk: counts of 0 to 6 are noisy. A hatched current month still reads as a drop if the label is missing (P1).

### D24 — Review gap to the local leader
- Best: bar trio "You, Leader, Target" with a gap sentence (P7 form A), plus form C for the pace.
- Alt 1: single progress bar to the target (form B).
- Alt 2: two cumulative lines over time (needs leader history, `unverified`).
- Risk: the leader count is a snapshot and the leader keeps growing. A 2× target can feel out of reach. State the date and say what pace closes the gap.

### D25 — Unanswered reviews
- Best: one number chip. Zero shows "All reviews answered". More than zero shows the count and a link to the reviews.
- Alt 1: response rate over time (S06 has this as a chart type).
- Alt 2: list of the open reviews with age in days.
- Risk: our memory note `no-review-answering` says 741 does not answer reviews. Showing D25 as a blocker may suggest we owe the reply. Check that note and set the owner (client) before showing. `unverified` for the exact wording of that rule.

## 5. Layouts for decision cards

### Section: "Do I get more enquiries?" (3 layouts)

Data used in all layouts: D01, D02, D03, D05 (Google and WhatsApp), D07, D08 (client entered). D04 is hidden.

#### Layout A — Answer line and four tiles (recommended)
```
Do I get more enquiries?
"142 contact actions in the last 30 days. 12 more than the 30 days before."

[ Calls 38    ] [ Website clicks 71 ]
[ ▂▃▅▆▇▅      ] [ ▃▃▄▅▆▅            ]
[ Directions 33] [ WhatsApp 14       ]
[ ▂▃▄▄▅▄      ] [ ░░ not tracked ▂▅▆ ]

You told us:  Leads 12  ·  Booked jobs 3   (not entered = empty slot)
```
- Best when: the client reads once a week and wants the answer first.
- How it handles our problems: tiles keep scales apart (P4). Hatched current month (P1). Dashed slot for WhatsApp (P2). Markers inside tiles (P3).
- Mobile: 1 tile per row, answer line stays on top.
- Risk: four tiles still hold 24 columns. Keep labels short.

#### Layout B — One total chart plus a small strip
```
Do I get more enquiries?
Stacked columns, 6 months, total contact actions per month
  [ ▇▇▇ ▇▇▇▇ ▇▇▇▇▇ ▇▇▇▇▇▇ ▇▇▇▇▇ ░░░ ]
Below: four small number cards (Calls · Website clicks · Directions · WhatsApp)
You told us: Leads · Booked jobs
```
- Best when: the client only wants one picture of "more or less".
- Risk: stacked columns hide small channels. WhatsApp at 9 next to 300 is invisible. A not-tracked channel changes the stack height and looks like growth. Fine for a report page, weak on the first screen.

#### Layout C — Table with mini columns
```
Channel         This month   Before   Last 6 months   Note
Calls           38           31       ▂▃▅▆▇▅░         
Website clicks  71           64       ▃▃▄▅▆▅░         
Directions      33           30       ▂▃▄▄▅▄░         
WhatsApp        14           —        — — — ▂▅▆░      Tracking starts Aug
Leads (you)     12           9        ▂▂▃▃▄▅
Booked (you)    3            2        ▁▁▂▁▂▃
```
- Best when: the reader likes rows and wants all numbers at once. Good for the report page and for Martin's review.
- How it handles our problems: "—" marks missing. A note column carries events (P3). Mini columns, not sparklines (P5 rule 3).
- Risk: the least visual. A data-shy owner sees a table again. The old table is the reason for this redesign.

Recommendation order: A, C, B. A for the portal first screen. C for the report page.

### Section: "Do people trust me?" (2 layouts)

Data used: D22, D23, D24, D25.

#### Layout T1 — Scoreboard (recommended)
```
Do people trust me?
[ 4.7 ★ ]  [ 44 reviews ]  [ 2 reviews waiting for an answer ]

Reviews compared with the leader
You     ████████░░░░░░░░░░░░░░░░  44
Leader  ██████████████████████░░ 120
Target  ████████████████████████ 240   (2 × leader)
"76 reviews to the leader. 196 to the target."

New reviews per month        needed pace ┄┄┄┄┄┄┄
 ▂ ▁ ▃ ▂ ▅ ░░
```
- Best when: the client needs a clear "where am I and how far is the goal".
- How it handles our problems: partial month hatched (P1). Gap in words (P7). Unanswered as a chip (D25 risk note).
- Risk: the 2× target can feel far away. The bars make the gap very visible. Keep the pace line honest and the tone calm.

#### Layout T2 — Growth line with reference lines
```
Do people trust me?
[ 4.7 ★ ]  [ 44 reviews ]  [ unanswered: 2 ]

Review count over 12 months (line)
   leader: dashed grey line at 120
   target: dashed line at 240
   you:    rising line ending at 44
Below: small columns "new reviews per month"
```
- Best when: the story is growth over time, not the final gap.
- Risk: needs leader count only as a flat line (a snapshot), or leader history (`unverified`). A flat leader line is easy to misread as "the leader stopped growing".

Recommendation order: T1, T2.

## 6. Open points

- The 9-day flatline in September: cause not verified. Ask Martin or check the tracking log before any annotation text.
- The September row is partial. Needs the cut-off date from the data pull ("to 13 Oct" or the real date).
- Whether Google restates history for the Directions count: `unverified`.
- Leader review history: `unverified` whether we can pull it. Without it, only the snapshot forms (P7 A, B) work.
- Target of 2× the leader: taken from the 741 programme rule in memory. Check per client.
- D25 owner: check `no-review-answering` before showing it.
- Live GBP and GA4 card layouts were not seen (login needed). The reference set uses doc pages and the review tools' help pages instead.
- Screenshots 01, 03, 04, 05, 07, 10, 11, 12 are doc or article pages (not all checked one by one). They are proof of the source, not layout models. Layout models: 02 (review summary and growth), 06 (review reports), 08 (small multiples), 09 (competitor card).
