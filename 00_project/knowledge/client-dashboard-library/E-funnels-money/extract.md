# Area E: Funnels, cost and return

Date: 2026-10-13. Scope: D05-D11, D36-D37, D41-D43. Language: English. Quotes: none longer than 15 words.
Rules from the brief apply: gaps show as gaps, no estimates, no tool names in client material, plain words.

## 1. Sources

All pages fetched 2026-10-13 with Firecrawl. Screenshots are in `refs/`.

| id | name | URL | fetched | type | status | screenshot |
|---|---|---|---|---|---|---|
| E01 | Pipedrive, Insights deal conversion report | https://support.pipedrive.com/en/article/insights-reports-deal-conversion | 2026-10-13 | product docs (pipeline funnel) | current (page updated 2026-09-02) | `refs/01-pipedrive-funnel-conversion.png` (chart image from the doc) |
| E02 | lemlist, Understand reports overview | https://help.lemlist.com/en/articles/8964490-understand-reports-overview | 2026-10-13 | product docs (outreach funnel) | current (live help page) | `refs/02-lemlist-reports-overview.png` (Lead funnel overview widget) |
| E03 | Moz, Spam Score help | https://moz.com/help/link-explorer/link-building/spam-score | 2026-10-13 | product docs (backlink quality) | current (live help page) | `refs/03-moz-spam-score.png` (Spam Score breakdown panel) |
| E04 | Atlassian, Complete guide to funnel charts | https://www.atlassian.com/data/charts/funnel-chart-complete-guide | 2026-10-13 | chart guidance | evergreen | `refs/04-atlassian-funnel-guide.png` (funnel with stage percentages) |
| E05 | Dataslayer, Marketing dashboard best practices | https://www.dataslayer.ai/blog/marketing-dashboard-best-practices-2025 | 2026-10-13 | dashboard guidance + ads template | current (page says updated April 2026) | `refs/05-dataslayer-ppc-dashboard.png` (ads cards, some cells say "No data") |
| E06 | Fuselab, Data visualization best practices | https://fuselabcreative.com/data-visualization-best-practices/ | 2026-10-13 | chart guidance (gaps, uncertainty) | current (updated 2026-09-10) | `refs/06-fuselab-chart-rebuild.png` (before and after bar chart) |
| E07 | Instantly, Analytics and Report | https://help.instantly.ai/en/articles/6602310-analytics | 2026-10-13 | product docs (outreach cards) | current (page says updated this week) | `refs/07-instantly-campaign-analytics.png` (metric cards, show/hide menu) |
| E08 | Ahrefs, Free Backlink Checker | https://ahrefs.com/backlink-checker | 2026-10-13 | live product page (backlink numbers) | current | `refs/08-ahrefs-backlink-checker.png` (page top only, weak visual) |
| E09 | Google Ads Help, Understand your conversion tracking data | https://support.google.com/google-ads/answer/6270625?hl=en | 2026-10-13 | product docs (cost per result, value per cost) | current | `refs/09-google-ads-conversion-columns.png` (page top only, text page) |
| E10 | Meta Business Help, About columns presets in Ads Manager | https://www.facebook.com/business/help/181580096038351 | 2026-10-13 | product docs (messaging results) | evergreen (live, but text has a 2023 note) | `refs/10-meta-ads-columns.png` (page top only, text page) |
| E11 | storytelling with data, What is a Sankey diagram | https://www.storytellingwithdata.com/blog/what-is-a-sankey-diagram | 2026-10-13 | chart guidance (Sankey) | evergreen (published 2023, edited 2024-11) | `refs/11-storytelling-sankey.png` (page top only) |

Blocked pages: none. Not covered in this run: Semrush and HubSpot views (HubSpot connector needs login), Smartlead and LinkedIn tools (only a search excerpt seen, no page scrape). Screenshots 08 to 11 show the page top, not a chart. Use E01, E02, E03, E04, E05, E06 and E07 for visual reference.

## 2. Findings per reference (one line each, exact element)

- E01: The funnel report draws one column per pipeline stage, puts a percentage badge between neighbouring columns, and writes a headline "Win rate is 87%" above the chart.
- E01: A text line under the headline says how many deals must enter to win one. This is a plain-words reading of the funnel.
- E01: A table sits under the chart with a Summary tab per stage. The chart is the first read, the table is the proof.
- E02: The "Lead funnel overview" widget lists six rows (Contacted, Delivered, Opened, Clicked or accepted, Replied, Interested). Each row shows a count and a share of contacted in brackets. A thin progress bar sits under it.
- E02: The docs split "Total activities" (every event counts) from "Lead funnel" (each lead counts once). Our funnel must say which one it counts.
- E02: A report only counts leads first contacted inside the chosen date range. The same rule fits our weekly or monthly outreach counts.
- E02: A widget with no matching data shows an empty state, and the docs tell the user to change the filter. Gaps are named, not zero-filled.
- E02: Reports can be shared by public link, with no login. This fits a client view.
- E03: Spam Score has three plain bands: Low 1-30, Medium 31-60, High 61-100. A "Spam Score Breakdown" panel shows the share of linking sites per band.
- E03: Moz says a high score does not prove a site is bad. It is a prompt to check the site. Our wording must say "check", not "toxic".
- E03: A double dash means "not rated yet", not zero. It updates every quarter and has no history.
- E04: Use a bar-style funnel, not a triangle. Triangle areas mislead. Show at least three stages.
- E04: Show the raw count and the share of the first stage. Add stage-to-stage percentages so nobody must calculate the drop.
- E04: A plain bar chart is often better than a funnel shape. Stacked bar fits a two-stage case.
- E05: Cost per lead is the "hero" number, large, top-centre. Four small visuals support it. Limit a page to 5-7 visuals.
- E05: Every number gets context: last period, goal, or a gap to goal. Use "Cost Per Lead", not "CPL".
- E05: Show a "last updated" time on every data block. Flag a day with zero spend as "possible missing data".
- E05: Ads template: each platform is one row of five small cards. Cells without data say "No data" in place of a zero.
- E06: Missing data: break the line or mark the gap. Connecting across a gap claims a value that never existed.
- E06: A partial current period needs one of three marks: shaded, labelled "in progress", or left out.
- E06: Before and after rebuild: axis from zero, values on bars, no legend, grey bars with one accent colour on the answer.
- E06: Part-to-whole: a stacked bar or a table with a percentage column beats a pie chart.
- E07: Metric cards (Sequence started, Reply rate, Positive reply rate, Opportunities) with a gear menu to show or hide each card.
- E07: "Opportunities" carry a money value; "Conversions" show cash collected as a second value. Money sits as a second line, not a new card.
- E07: A progress percentage counts a lead only after the whole sequence ends. It does not rise per step. Define "done" on the card.
- E08: The free backlink view opens with four numbers: referring domains, backlinks, a site strength score and a rank. Link type and platform come after.
- E08: Broken links are a separate tool, not part of the headline numbers. Same for us: broken links are a detail, not a headline.
- E09: "Cost / conv." is total cost divided by conversions. "Conv. value / cost" is the return on spend. Value per conversion only works when a value is entered.
- E09: A dash, not a zero, shows when conversion types cannot be added. The docs say this protects accuracy.
- E09: Conversions are counted at the click date, and reports can lag 24-48 hours. Our cost per result needs a "numbers up to" date.
- E10: Column presets named "Messaging engagement" and "Traffic" show cost per result and messaging conversations started. This is Meta's own name for the WhatsApp-type result.
- E10: The default view has "Results" and "Cost per result" next to "Amount spent". The pair spend plus result plus unit cost is the standard.
- E11: Sankey fits progress through stages with branches. It is a poor fit when there is no flow, or when readers must compare exact values.
- E11: Too many nodes overwhelm the reader. Our funnels have one path and five steps, so a Sankey adds nothing.

## 3. Patterns

### P1. Step funnel with percentage between steps
Source: E01, E04. Three to five bars in a row, equal spacing, bars aligned to one baseline. A small badge between bars shows the share that moved on. Headline above: one plain sentence.
Use when: 3 to 5 steps, one path, counts above about 30 at the first step (WhatsApp clicks to booked jobs once bookings exist).
Avoid when: first step has fewer than about 20 events, or steps have branches. Small counts make percentages jump (`unverified` limit, my judgement).

### P2. Step rows with a count, a share and a thin bar
Source: E02, E07. One row per step. The label sits left. Count and share sit right. A thin bar goes below. Works in one column at 390 px.
Use when: outreach funnels with 5 to 6 steps and a big first number, such as 149 requests to 0 live links.
Avoid when: bar lengths hide small counts (9 offers next to 149 requests). Print the count in text next to the bar.

### P3. One big "cost per result" number with context
Source: E05, E09. One large number, a label in plain words ("Cost per WhatsApp click"), a second line with the period, a third line with last period or the formula.
Use when: the result is tracked and the period has at least a few results.
Avoid when: the result count is zero or tracking is off. Show a gap card (P5). Avoid when the number is a mean of very few events: print "based on 14 clicks".

### P4. Spend and result pair
Source: E09, E10, E05. Two or three tiles in a fixed order: Spent, Result count, Cost per result. Currency shows once, on the spend tile and in the unit line.
Use when: ads run (D37). Keep IDR as the account currency. Show EUR only with a stated rate and date, otherwise leave it out (`unverified`: no reference found on currency display for small advertisers).
Avoid when: ads are paused and no spend exists. Show the status card (P8) with the last period.

### P5. "What we know / what we do not know yet" split
Source: E06, E09, E03, E05. Two blocks side by side or stacked. Left block: tracked facts with a "numbers up to" date. Right block: the missing item as a card with a dash, one line on why, and one action ("Tell us your booked jobs"). No estimate, no grey zero.
Use when: bookings are not tracked (D08, D09, D10). The gap itself is the call to action.
Avoid when: the item is zero for real. A tracked zero says "0 so far, tracking active since 12 Oct".

### P6. Quality as plain word with share of sites
Source: E03. Three bands with plain words, for example "Fine / Look at / Risky", a stacked bar of the share of linking sites per band, and one line: "We check each Look-at site by hand".
Use when: D42 has a quality score per site.
Avoid when: the score is missing (show "not rated yet"). Avoid the word "toxic" and any raw 0-100 number as the headline.

### P7. Cost basis as a visible sum
Source: E09 formula, own synthesis. One line: "741 fee + ad spend = total cost. Total cost / booked jobs = cost per booked job." Numbers sit under each term.
Use when: D10 and D11 are both known. It shows the client how the number is built.
Avoid when: Martin does not want the fee shown. Memory rule: no invoice or fee talk unless asked. Needs a decision.

### P8. Status pill with a reason line
Source: E05 (colour only for exceptions), E06 (colour keeps one meaning). Pill (Running / Paused / Needs you), one reason line, date of last change.
Use when: D36. One colour rule for the whole portal: green = fine, amber = waiting on someone, red = broken, grey = not tracked.
Avoid when: paused for a planned reason. Say who paused and why, so red does not scare.

### P9. Bar over Sankey
Source: E04, E11. Keep funnels as bars. Use a Sankey only for branching flows with many nodes. Our funnels do not branch, so skip it.

## 4. Recommendation per data point

| ID | Best form | Alternative 1 | Alternative 2 | Risk |
|---|---|---|---|---|
| D05 WhatsApp clicks | Big number for the period with 8 small weekly bars (P3 light) | Row in a step funnel (P1) | Daily line in the trend area | A click is not a chat. Label it "clicks on the WhatsApp button". |
| D06 Form leads | Count with the last three leads listed under it | Step in the funnel | Number in a "Leads" tile with a source split | Tracking off shows as 0. Show "not connected yet" (P5). |
| D07 Leads added by hand | Count labelled "added by you" next to D06, one add button | Single combined "Leads" number with a split line | Small list only | Low use. Empty looks like zero demand. Mark as "no entries yet". |
| D08 Booked jobs | Count the client ticks, with a "Tell us" button and a date of last update | Funnel step that stays dashed until data exists (P1 + P5) | Checklist of leads with a "booked" tick | Silence is not zero. Never show 0 without "tracking active since". |
| D09 Value per booked job | Money number only after at least one booked job with a value | Range from the client's own entries (min to max, no model) | Hidden until D08 exists | Client may not share it. Never fill with an average from us. |
| D10 Cost per booked job | One big number (P3) with "based on N jobs" and the sum under it (P7) | Gap card with the missing item named (P5) | Cost per WhatsApp click as the stand-in, clearly labelled as a different result | One or two jobs give a wild number. Show N. Never compare it with a benchmark we cannot source. |
| D11 Cost basis | Visible sum line (P7) | Stacked bar fee vs ad spend per month | Small footnote under D10 | Showing the fee is Martin's call. Fee talk only on request (memory). |
| D36 Ad status | Status pill with reason and date (P8) | Banner at the top of the ads section only when paused | Dot in the section title | A red pill for a planned pause. State the reason in words. |
| D37 Spend, clicks, WhatsApp clicks, cost per click, cost per result | Spend and result pair (P4) with the unit cost large | Week-by-week small bars for spend and result, side by side | Plain table of the same four numbers under "Show the numbers" | Mixed currency. Two units (IDR and EUR) in one view confuse. Pick one and label it. |
| D41 Outreach funnel | Step rows with a count, a share and a thin bar (P2) | Step funnel with arrows (P1) | Five step cards with one plain line each | 0 live links reads as failure. Show the next step and the date of the last send. Define what "requests" and "messages" count (`unverified`: the exact meaning of each step). |
| D42 Backlink quality | Four number tiles (links, sites linking, broken, rated risky) with plain words, plus a band bar (P6) | Single "Link health" word with a one-line reason | Table behind a toggle | Raw spam score and DA are jargon. Rated-risky wording must say "check", not "toxic". |
| D43 Listings live x of y | Segmented progress bar "12 of 44 live" with states (live, waiting, we need you) | Checklist grouped by state | Single fraction tile | The y total changes when we add sites. Show the date of the count. |

## 5. Layouts for decision cards

Example numbers come from the brief (Bali Healing): spend IDR 571,785, 61 clicks, 14 WhatsApp clicks, IDR 40,842 per WhatsApp click. Cost per click is not in the brief. If used, compute it: 571,785 / 61, about IDR 9,374 (derived, check before use). Booked jobs: not tracked.

### Ads and cost section

**Layout A: Money line, then the gap**
- Row 1: status pill (P8) and "numbers up to 12 Oct".
- Row 2: three tiles: Spent (IDR 571,785), WhatsApp clicks (14), Cost per WhatsApp click (IDR 40,842), with the sum line under the tiles (P4).
- Row 3: weekly bars, spend and clicks side by side.
- Row 4: gap card "Booked jobs: not tracked yet. Tell us each booked job." (P5).
- Mobile 390: tiles stack in one column, bars shrink to a row of 8 bars.
- Good for: one clear story, least risk. Weak spot: no step view.

**Layout B: Funnel first**
- Row 1: status pill and date.
- Row 2: step funnel: Clicks (61) to WhatsApp clicks (14) to Form leads (not connected) to Booked jobs (not tracked). Percentage badge between known steps. Dashed bars for unknown steps (P1 + P5).
- Row 3: cost under each known step: cost per click, cost per WhatsApp click.
- Row 4: "Show the numbers" table.
- Mobile 390: switch to step rows (P2).
- Good for: shows where the chain breaks, and why bookings matter. Weak spot: dashed steps can look unfinished to the owner.

**Layout C: One number first, details hidden**
- Hero card: one big number "IDR 40,842 per WhatsApp click", one sentence, status pill.
- Under it: a single line "Booked jobs: not tracked yet" with one button.
- Below: collapsed section "Show the numbers" with spend, clicks, cost per click and the weekly table.
- Mobile 390: same, already one column.
- Good for: owners who do not read charts, five-second test (E05, E06). Weak spot: hides spend by default, the owner may want the money first.

### Backlinks section

**Layout A: Step rows plus health tiles**
- Block 1: five step rows. Each has a count, a share of requests and a thin bar: 149 requests, 38 messages, 14 in conversation, 9 offers, 0 links live (P2). A one-line plain sentence above: "Of 149 requests, 9 became offers. No link is live yet."
- Block 2: four tiles for the links we already have: links, sites linking, broken, rated risky (P6). If none are rated: "not rated yet".
- Mobile 390: rows are already one column; tiles go two by two.
- Good for: full detail with the least drawing. Weak spot: long on a phone.

**Layout B: Step cards with arrows, one health word**
- Block 1: five cards in a row, each with the count, a one-line plain meaning and a small arrow with the share to the next card (P1 as cards). Last card says "0 live. Next: 9 offers to close."
- Block 2: one "Link health" word (Fine / Look at / Risky) with a one-line reason and a link to the table.
- Mobile 390: cards become a vertical list with a down arrow.
- Good for: owner reads it like a story. Weak spot: cards take more room than rows, and one word hides detail.

## 6. Open items for the decision round
- Fee display (P7): Martin decides. Default in all layouts: not shown.
- Currency: show IDR only, or IDR plus EUR with a stated rate and date. No reference found.
- Meaning of "requests" and "messages" in D41 (`unverified`).
- Zero rule: a tracked zero reads "0 so far, tracking since <date>". An untracked item shows a dash and a reason.
