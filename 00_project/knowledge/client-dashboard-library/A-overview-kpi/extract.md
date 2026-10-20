# Area A — Overview, first screen, KPI cards

Fetch date: 2026-10-13. Scope: D01–D05, D16–D17, D26, D34, D35, D10–D11 (see `client-dashboard-redesign/01-inventory.md`).
Rule for this file: no source is quoted with more than 15 words. A claim that I could not check is marked `unverified`. "741 judgement" means my own design view. It is not from a source.

## 1. Sources

All screenshots show the top of the page at 1920 x 1080. They show help pages and marketing pages. They do not show logged-in product screens (login wall). See section 7 for gaps.

| ID | Name | URL | Type | Status | Screenshot |
|---|---|---|---|---|---|
| S01 | NN/g — Dashboards: charts and graphs easier to understand | https://www.nngroup.com/articles/dashboards-preattentive/ | design guidance | evergreen (no date seen) | `refs/01-nngroup-dashboards-preattentive.png` |
| S02 | AgencyAnalytics — Smart Dashboards | https://agencyanalytics.com/features/smart-dashboards | agency product page | current (live page, undated) | `refs/02-agencyanalytics-smart-dashboards.png` |
| S03 | Google — Business Profile performance and insights (help) | https://support.google.com/business/answer/9918094?hl=en-GB | official docs | current (live page, undated) | `refs/03-google-business-profile-performance-help.png` |
| S04 | Shopify dev docs — Metrics card | https://shopify.dev/docs/api/app-home/latest/patterns/compositions/metrics-card | design-system pattern | current (live docs, undated) | `refs/04-shopify-metrics-card.png` |
| S05 | Google — GA4 About the Home page (help) | https://support.google.com/analytics/answer/11197963?hl=en | official docs | current (live page, undated) | `refs/05-ga4-home-page-help.png` |
| S06 | AgencyAnalytics — home page (client roll-up table) | https://agencyanalytics.com/ | agency product page | current (live page, undated) | `refs/06-agencyanalytics-home-rollup-table.png` |
| S07 | BrightLocal — How to do effective local SEO reporting | https://www.brightlocal.com/learn/local-seo-reporting/ | local SEO guide | current (page modified 2026-10-02, first posted 2021) | `refs/07-brightlocal-local-seo-reporting.png` |
| S08 | Databox — KPI dashboard examples | https://databox.com/dashboard-examples/kpi | template gallery | current (modified 2026-09-24) | `refs/08-databox-kpi-dashboard-examples.png` |
| S09 | Stripe Support — Dashboard home page charts | https://support.stripe.com/questions/dashboard-home-page-charts-for-business-insights | official docs | current (modified 2026-05-11) | `refs/09-stripe-dashboard-home-help.png` |
| S10 | 925Studios — Stripe Dashboard design breakdown | https://www.925studios.co/blog/stripe-dashboard-design-breakdown | third-party analysis (opinion) | current (published 2026-03-27, older than 3 months) | `refs/10-925studios-stripe-dashboard-breakdown.png` |
| S11 | Windsor.ai — Data Studio SEO report template (Search Console) | https://windsor.ai/data-studio-seo-reporting-template/ | report template | current (updated 2026-10-08) | `refs/11-windsor-looker-studio-gsc-template.png` |
| S12 | The Data School — Relative vs absolute change | https://dataschool.com/misrepresenting-data/relative-vs-absolute-change/ | data literacy | evergreen | `refs/12-dataschool-relative-vs-absolute-change.png` |
| S13 | AgencyAnalytics — Anomaly detection | https://agencyanalytics.com/features/anomaly-detection | agency product page | current (live page, undated) | `refs/13-agencyanalytics-anomaly-detection.png` |
| S14 | Sterling Sky — Business Profile Performance report explained | https://www.sterlingsky.ca/interpret-google-business-profile-performance/ | local SEO guide | current (published 2026-09-27) | `refs/14-sterlingsky-gbp-performance-caveats.png` |

Count: 14 sources, 14 screenshots.

## 2. Findings per reference

One line each. The exact element is in bold.

- S01 — Bar and line charts work best on a dashboard. They use length and 2D position. Avoid **gauge**, **donut** and pie. Do not use colour to show size. Use colour for groups only.
- S02 — The **Goals widget** gives a progress indicator towards a client target. This is the closest pattern to "week 5 of 13" (goal progress). The page also says a live dashboard can be shared by link.
- S03 — The **Performance view** lists interactions, calls, directions, website clicks, messages, bookings, views and searches. It has a **date range selector**. Data exists only for verified profiles.
- S04 — The **metrics card** has three parts: a **label**, one **value** and a **change badge** (up, flat, down, with a tone). Cards sit in a **grid** that is side by side on large screens and stacked on small screens. The docs say to add trend badges only when a past comparison adds context.
- S05 — The GA4 **Home overview card** shows a **trendline** per metric. It compares the last 7 days with the 7 days before. An **Insights** block below shows unusual changes in plain text.
- S06 — The AgencyAnalytics client list has a **Status pill** (Active / Trial) and a **Trend column** with a small green delta chip per client. One row answers "is this client fine?".
- S07 — Lead with results that map to real actions (calls, direction requests). Do not lead with domain authority or bounce rate. Say where a rank gain sits in the plan, so a small gain still has meaning.
- S08 — The page is a gallery of KPI templates. I could not extract element details from it. No finding is taken from S08.
- S09 — The Stripe **Home charts** can be customised. They have a **date range dropdown** and a separate **comparison range dropdown**.
- S10 — Opinion piece. It says the Stripe home screen shows the previous period in **smaller text under each main number**. It says colour is only for status. It says an **empty state** should give the next step. Treat as `unverified` against the live product.
- S11 — Four **scorecards** (clicks, impressions, average position, CTR). The first three carry a **previous-period change**. Below sits one **line chart** (clicks and average position) and a device **donut**. The report keeps 16 months of data.
- S12 — A percent change on a small base looks large. A percent change on a large base looks small. Show the absolute number and the percent together.
- S13 — Flags show up as marks on **line and area charts** and in an **in-app inbox**. Users are told when a data feed stops. This is the "tell the client before they ask" pattern.
- S14 — A **call** in the Google view is a tap on the Call button, not a proven call. **Directions** are adjusted for repeat taps and spam. **Website clicks** are not leads. **Views** can count one person more than once across devices.

## 3. Patterns for the first screen

### P1 — Three question cards, not a metric wall
- What: three cards. Each card is one client question in plain words ("Do I get more enquiries?"). Each card holds one number, one absolute change and one sentence.
- When: always on the first screen. Matches the 10-second test in the brief.
- Avoid: more than 4 cards in the top row. Avoid card titles with jargon such as "SoLV" or "ARP". (Basis: S04, S07; 741 judgement on the count.)

### P2 — Number, then change in absolute terms
- What: show "+6 vs last 4 weeks" first. Add the percent only when the base is large.
- When: every count card (D01–D05, D16).
- Avoid: "+300%" on a base of 2. Do not sort the card by the most dramatic figure. (Basis: S12, S04.)

### P3 — One fixed comparison rule
- What: compare the last 4 full weeks with the 4 full weeks before. Print the rule on the card ("29 Sep – 26 Oct vs 1 Sep – 28 Sep"). Mark a running week as "so far".
- When: all cards. GA4 uses 7 days against 7 days (S05). Stripe lets the user pick the range (S09).
- Avoid: a partial month next to a full month. Avoid a user-set range on the first screen. A client does not need that control. (741 judgement.)

### P4 — Bars for counts, line for position, no gauges
- What: weekly counts use small **bars** (12 weeks). Average position uses a **line** with a flipped axis. Progress uses a **segment bar**.
- When: any card with a time series.
- Avoid: gauge, donut, 3D. Avoid colour as a size code. (Basis: S01. S11 shows a donut for devices; do not copy it.)

### P5 — So-what sentence under each number
- What: one short sentence written by 741: what the number means and what we do next. Example form: "More people tapped Call. We keep the phone number on every page."
- When: every top card. A person writes it, or a fixed template fills it. A person checks it each week.
- Avoid: claims about cause that we cannot prove. Avoid generated praise. If the number fell, say so and say why, or say "we are checking". (Basis: S07, S05 insights block; 741 judgement on process.)

### P6 — Colour means status only, with one written rule
- What: green = on track. Amber = needs attention. Red = broken or at risk. Grey = no data. Everything else is neutral.
- When: pills, banners, delta chips.
- Avoid: green for "number went down" on lower-is-better data such as rank. Colour carries no meaning today (brief problem 12). (Basis: S10 `unverified`, S01.)

### P7 — Status strip and warning banner
- What: one slim strip at the top: "Week 5 of 13 · Last update from 741: 2 days ago". A **warning banner** appears only when a warning is open. It names the issue, the owner and the next step. No banner means one calm "All clear" line or nothing.
- When: always for the strip. The banner only on D35 events.
- Avoid: a permanent red zone. Avoid warnings with no owner. (Basis: S13, S02 goal widget.)

### P8 — Honest gap state with an action
- What: a missing value shows "No data yet" in grey with the reason and the action ("Tick your booked jobs to see cost per job"). Add a freshness stamp ("Data to 11 Oct").
- When: D08–D11, a new client, a feed that failed, a partial week.
- Avoid: a zero where data is missing. Avoid an estimate. This is a hard rule in the brief. (Basis: S10 `unverified`, S13.)

## 4. Recommendation per data point

Form = best visual form. Alt = two alternatives. Risk = the main trap. Data notes use the "count per week, small numbers, partial month, gaps" cases.

### D01 — Phone calls from the Google profile
- Form: **card with a 4-week total, absolute change and a 12-week bar strip.** The running week is hatched and marked "so far". Label: "Taps on Call".
- Alt 1: sparkline of weekly counts. Alt 2: number and change only, no chart, when most weeks are 0–2.
- Risk: the figure is button taps, not proven calls (S03, S14). Do not write "calls received". Also: a percent on 3 calls is noise (S12).

### D02 — Website clicks from the Google profile
- Form: **same card family as D01**, same bars. Label: "Visits to your website from Google".
- Alt 1: one combined "Contact actions" card with a split bar (calls, website, directions, WhatsApp). Alt 2: number only.
- Risk: clicks are not leads (S14). The card must not sit under a title like "Enquiries" unless the sentence says what it counts.

### D03 — Direction requests
- Form: **same card family, bars.** Label: "Asked for directions".
- Alt 1: fold into the combined "Contact actions" card. Alt 2: hide when the practice is online-only (value 0 for months).
- Risk: Google adjusts this count for repeat taps and spam (S03, S14), so it can change after the fact. A permanent zero looks like failure for an online-only client.

### D04 — Profile views (impressions)
- Form: **not a top card.** Show as one grey line inside the results tab: "Profile views: X (4 weeks)".
- Alt 1: weekly line on the results page. Alt 2: a small "reach" figure under the enquiries card, no chart.
- Risk: views are a reach figure. They can rise while enquiries stay flat. The same person can count more than once (S14). On the first screen it makes the story look better than it is.

### D05 — WhatsApp clicks from the site (daily)
- Form: **card with weekly bars built from the daily data**, plus an **annotation marker** on the weeks when ads were paused or restarted (D36). Label: "Taps on WhatsApp".
- Alt 1: 28-day line on daily data (use only above ~10 per day). Alt 2: number only with a "ads on / ads off" split.
- Risk: a tap is not a started chat (`unverified` for the Bali tag setup). A fall after "Ads paused" is not an SEO fall. Without the marker the client reads it wrong. Daily bars on small counts are spiky.

### D16 — Google Search clicks (28 days)
- Form: **card with the 28-day total, absolute change vs the 28 days before, and one line chart with the earlier period as a dashed line.** Same layout as S11.
- Alt 1: weekly bars. Alt 2: number and change only.
- Risk: Search Console lags by a few days (`unverified` for exact days). Mark "Data to <date>". The total mixes brand and non-brand searches, so growth may not mean new customers.

### D17 — Google Search average position
- Form: **plain-word band plus number**: "Page 2 (10.8)". Below it, one small line chart with the axis flipped so better is up.
- Alt 1: bar of "searches in top 3 / top 10 / beyond" (needs D18 or D19 data). Alt 2: number with an arrow that points to better or worse in words.
- Risk: the average hides what moves. A fall in the number is good news, so an "up" arrow and a "down" number clash (see P6). A new page that ranks poorly can pull the average down while the work succeeds.

### D26 — Programme week and phase
- Form: **segment bar of 13 segments** with the current one filled, and the phase name: "Week 5 of 13 · Build". It sits in the status strip (P7).
- Alt 1: compact 13 chips (today's P4 chips, smaller). Alt 2: text only.
- Risk: it must come from one source. Today onboarding says "1 of 6" while the week says 5 (brief problem 2). If the programme pauses or runs long, 13 segments become false.

### D34 — Last update from 741 (days)
- Form: **line in the status strip**: "Last update from 741: 2 days ago" plus the headline of that update. Click opens the entry.
- Alt 1: freshness stamp on each card ("Data to 11 Oct"). Alt 2: latest item from the activity feed pinned at the top.
- Risk: after 7 days with no update the line shows neglect. Use a rule: after 7 days it turns amber and 741 gets an internal task. Keep the work-update stamp apart from the data stamp. They are two different facts.

### D35 — Early warnings
- Form: **warning banner** under the status strip, only when open (P7). Each item has: what changed, what it may cost, owner, next step.
- Alt 1: a coloured dot on the matching card. Alt 2: a short "Watch list" card with 0–3 rows.
- Risk: false alarms. They train the client to ignore the banner. Use a fixed trigger list (profile edit, site down, review drop). Each trigger needs a named owner. Do not alert on normal weekly noise on small counts.

### D10 — Cost per booked job
- Form: **single number card with the base shown**: "€X per booked job · based on N jobs · month so far". If D08 or D11 is missing, show the gap state (P8) with the action.
- Alt 1: quarterly figure instead of monthly. Alt 2: a small table (cost, jobs, cost per job) per month.
- Risk: one or two booked jobs make the figure swing. A partial month makes it look too high. Show only for full months, or print "so far". Never fill a gap with an estimate.

### D11 — Cost basis (741 fee + ad spend)
- Form: **one-line equation under D10**: "€ fee + € ads = € total ÷ N jobs". Hidden until the client opens the D10 card.
- Alt 1: stacked bar per month (fee, ads). Alt 2: table in the results tab.
- Risk: it can read as invoice talk. Martin's memory rule says to discuss invoices and instalments only when asked (`feedback-no-invoice-talk`). Decide whether the fee part shows at all. This needs a Martin card.

## 5. Three first-screen layouts

Same data, three orders. Phone order is in each line. Use these as options for a decision card.

### Layout A — "Three questions"
Order, top to bottom:
1. Status strip: name, "Week 5 of 13", last update from 741 (D26, D34).
2. Warning banner, only if open (D35).
3. Three cards in a row (stacked on phone): **Enquiries** (D01+D02+D03+D05 as one total with a small split and 12-week bars), **Found on Google** (D16 number + D17 band), **741 at work** (last update headline, 2–3 done items).
4. "What we need from you" card (decisions, access, unanswered reviews). Each row has one button.
5. Link: "See all results".

Strong: maps 1:1 to the three questions in the brief. Weak: the first card merges four metrics, which hides one weak metric. Phone: strip, banner, cards in the order above, then "what we need".

### Layout B — "One sentence, one chart"
Order, top to bottom:
1. Status strip (D26, D34) and warning banner (D35).
2. One headline sentence in large type: "48 enquiry actions in the last 4 weeks. That is 6 more than before."
3. One large 12-week bar chart of all contact actions, with annotation markers (ads paused, site change).
4. Four small chips under the chart: calls, website, directions, WhatsApp, each with an absolute change.
5. Two side blocks: "741 this week" and "Needed from you".
6. Search clicks and position (D16, D17) as one compact row at the bottom.

Strong: the story is told in 5 seconds, and the chart is the hero. Weak: the sentence needs a weekly human check. Few big cards means less detail. Phone: sentence, chart, chips (2x2), blocks.

### Layout C — "Needs you first"
Order, top to bottom:
1. Status strip (D26, D34).
2. **Needs you** card: count of open items with the first two named (decision, access, unanswered reviews).
3. Warning banner (D35), if open.
4. Slim KPI strip of four numbers with absolute change: enquiry actions, search clicks, position band, cost per booked job or its gap state (D10).
5. 13-week programme timeline with this week marked.
6. Link to results and reports.

Strong: it clears blockers first and suits clients that open the portal to act. Weak: the results sit lower, so a good month is less visible. It fits weeks with small counts. Phone: needs-you card first, strip of 2x2 numbers, timeline.

## 6. Notes for the decision card

- A and B put results first. C puts the client's action first.
- All three use P2, P3, P6 and P8. Those four patterns do not depend on layout.
- Open items for Martin: show D11 or not (invoice rule), and who writes the P5 sentence each week.

## 7. Gaps and skipped pages

- No live product screens were captured for Google Business Profile, GA4, Stripe, Linear or Vercel. Help and docs pages were used instead. The product screens sit behind a login. Statements about layout come from text on those pages.
- Linear and Vercel overview pages: not researched. No reliable public page found in the time used. `unverified`.
- Whitespark, Semrush client reports, Swydo, DashThis, Looker Studio gallery: no usable client-report view found in search results. Skipped. Windsor (S11) stands in for the Looker Studio template.
- Databox (S08): the page gave no element detail. It stays in the table for the record. No finding relies on it.
- AgencyAnalytics Goal and Budget tracking page: the extract had no element detail. I did not keep a screenshot. The Goals widget claim in S02 comes from the Smart Dashboards page text.
- The "so-what sentence" pattern (P5) has no named single source. S05 (Insights block) and S07 (tie numbers to actions) support it. The weekly human check is 741 judgement.
- The small-number rule (P2, D01–D03) uses S12 for the principle. The "large base" idea and the "~10 per day" limit for D05 are 741 judgement. No source gives those numbers.
