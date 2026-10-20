# B — Local map visibility and AI visibility: extract

Date: 2026-10-13. Area B of the client dashboard redesign.
Data points: D12, D13, D14, D15, D19, D20, D21, D49 (IDs from `00_project/client-dashboard-redesign/01-inventory.md`).
Screenshots are in `refs/`. They are for internal decisions only. They never go into client files.
In client files, call the framework "741 Dashboard-Raster". Do not name tools or sources.
Rule for quotes: no source text over 15 words. Most lines below are paraphrase.

## 0. Short answer

1. The 18-keyword table is the wrong form. Two live products use a keyword list with one small heat thumbnail, one number, one arrow and one sparkline per row (B05, B03). That form fits 18 rows. Group the rows, because the UK statistics office advises at most 12 panels (B15).
2. "Share of voice" means three different things across tools. SoLV is the share of grid points in the top 3 (B01). Semrush "Share of Voice" is a weighted rank metric (B03). Ahrefs, Peec and Otterly use it for the share of AI answers that name the brand (B07, B10, B16). Do not show this term to a clinic owner. Use one sentence with a count: "top 3 on 31 of 49 spots".
3. The best client-facing report I found is a public demo (B06). It gives a word for the average rank, a counted top-3 score ("34 of 37 spots"), a tooltip that explains the score, a compass view ("North / South / East / West"), a recommendation card and a competitor table.
4. AI answers change on every run (B08). One check is not a number. Show how many answers sit behind each percentage. No reference shows a 16 keywords x 3 platforms matrix. That layout is our own design (`unverified` that none exists).

## 1. Sources

Fetch date for every row: 2026-10-13. "Core" = used for a pattern. "Support" = definitions or guidance.
Status: `current` = live product page or doc fetched today, or post under 3 months old. `evergreen` = principle, or post over 3 months old.

| ID | Name | URL | Type | Status | Use | Screenshot |
|---|---|---|---|---|---|---|
| B01 | Local Falcon — Scan Report | https://www.localfalcon.com/report-types/scan-report | product page | current | core | `refs/01-localfalcon-scan-report.png` |
| B02 | BrightLocal — Local Search Grid | https://www.brightlocal.com/local-seo-tools/rankings/local-search-grid/ | product page (page dated 2026-07-28) | current | core | `refs/02-brightlocal-local-search-grid.png` |
| B03 | Semrush — Keyword report in Map Rank Tracker | https://www.semrush.com/kb/1484-keyword-report-in-map-rank-tracker | docs (published 2025-01-20, live) | current | core | `refs/03-semrush-map-rank-keyword-report.png` |
| B04 | Whitespark — Local Ranking Grids | https://whitespark.ca/local-ranking-grids/ | product page | current | core | `refs/04-whitespark-local-ranking-grids.png` |
| B05 | Whitespark — live public share view (demo location) | https://grid.localdata.tools/share/location/05241b96-b2dd-44ae-b385-e7a123d41e2a | public demo, scans dated 2026-10-05 | current | core | `refs/05-whitespark-live-demo-share.png` |
| B06 | EmbedMyReviews — public client report (demo scan, data from Dec 2025) | https://demo.app.embedmyreviews.com/scans/1ffcf206-b2a5-45f5-8b49-4b4f2fddcfd9/report | public demo | current (demo data old) | core | `refs/06-embedmyreviews-client-report.png` |
| B07 | Peec AI — AI visibility | https://peec.ai/product/ai-visibility | product page | current | core | `refs/07-peec-ai-visibility.png` |
| B08 | Local Falcon — AI search visibility | https://www.localfalcon.com/features/ai-search-visibility | product page | current | core | `refs/08-localfalcon-ai-visibility.png` |
| B09 | Local Falcon — Trend Report | https://www.localfalcon.com/report-types/trend-report | product page | current | support | `refs/09-localfalcon-trend-report.png` |
| B10 | Ahrefs — Brand Radar | https://ahrefs.com/brand-radar | product page | current | support | `refs/10-ahrefs-brand-radar.png` |
| B11 | Semrush — Getting started with the AI Visibility Toolkit | https://www.semrush.com/kb/1496-getting-started-with-ai-visibility-toolkit | docs (live) | current | core | `refs/11-semrush-ai-visibility-toolkit.png` (page header only) |
| B12 | UK Government Analysis Function — colours in charts | https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/ | guidance | evergreen | support | `refs/12-gov-uk-analysis-function-colours.png` (page header only) |
| B13 | Local Falcon — Competitor Report | https://www.localfalcon.com/report-types/competitor-report | product page | current | support | `refs/13-localfalcon-competitor-report.png` |
| B14 | GBPPromote — Local Falcon review 2026 (updated 2026-09-10) | https://gbppromote.com/local-falcon-review/ | blog post by a vendor of a competing product | current, bias noted | support | `refs/14-gbppromote-local-falcon-review.png` (page header only) |
| B15 | ONS Service Manual — small multiple charts | https://service-manual.ons.gov.uk/data-visualisation/chart-types/small-multiple-charts | guidance | evergreen | core | `refs/15-ons-small-multiple-charts.png` (page header only) |
| B16 | Otterly — "What can you learn from the insights on brand reports?" (dated 2026-10-05) | https://help.otterly.ai/insights-on-brand-reports | docs | current | core | `refs/16-otterly-brand-report-insights.png` (page header only) |
| B17 | Profound — How to track brand visibility in AI search (2026-01-26) | https://www.tryprofound.com/blog/how-to-track-your-visibility-in-ai-search | vendor blog | evergreen (over 3 months) | support | `refs/17-profound-track-ai-visibility.png` (page header only) |
| B18 | Local Viking — GeoGrid tracking | https://localviking.com/geogrid-visibility-tracking | product page | current | support | `refs/18-localviking-geogrid-tracking.png` |
| B19 | AgencyAnalytics — local rank tracker (2026-06-09) | https://agencyanalytics.com/blog/local-rank-tracker | vendor blog | evergreen (over 3 months) | support | `refs/19-agencyanalytics-local-rank-tracker.png` |

Also read for definitions, no own screenshot:
- Local Falcon KB32 "What is SoLV" (scraped), https://www.localfalcon.com/knowledge-base/kb32-what-is-solv
- Local Falcon KB72 "How to read a scan report" (search excerpt only, page updated 2025-12-29), https://www.localfalcon.com/knowledge-base/kb72-how-to-read-a-scan-report
- Semrush KB1399 Map Rank Tracker (scraped), https://www.semrush.com/kb/1399-map-rank-tracker
- Semrush API doc for Map Rank Tracker (scraped, long file), https://developer.semrush.com/api/v4/local/map-rank-tracker/
- Semrush product page https://www.semrush.com/map-rank-tracker/ (scraped; screenshot showed only the hero, so I dropped it)

Blocked or weak:
- No page was blocked.
- Peec: the page text showed a bot check, but the page and screenshot loaded. Facts come from the FAQ text and the demo strip.
- Local Viking: I did not see a client report. I only read the product page. A Reddit comment in a search excerpt says it shows desktop results only. That is `unverified`.
- Not fetched: Semrush KB1594 (AI metrics), Otterly KPI definitions, Ahrefs methodology post.
- Screenshots B11, B12, B14, B15, B16, B17 show the page header, not the chart. The facts come from the page text.

## 2. Findings per reference (one line each)

- B01: The "Geo-Grid Scan Explorer" is a map with one coloured pin per grid point. The pin carries the rank number inside it.
- B01: The metric block lists SoLV and SAIV together. ARP excludes spots at rank 20 or lower. ATRP includes every spot.
- B01: "OSoLV" shows how far the business is from the best competitor's SoLV. This is a "gap to the leader" number.
- B01 / KB32: A worked SoLV example uses decimals (18.37). That is false precision for a clinic owner. Round to whole numbers.
- B02: The grid pins are coloured dots with the rank number inside. The legend is a small chip in the map corner with 4 bands: 1-3, 4-10, 11-20, over 20. It has no words and the type is tiny.
- B02: "Then vs Now" puts any two grids side by side. This is the before/after pair.
- B02: A competitor grid can sit beside your own grid for the same keyword and period.
- B02: The FAQ calls the grid a weather map for rankings and calls 5x5 the sweet spot. Our 7x7 (49 spots) is fine.
- B03: The "Keywords" tab shows one row per keyword. Each row has Avg. Rank with a sparkline and a change figure, Share of Voice with a sparkline, and four split values.
- B03: The four split values are Good (rank 1-3), Average (4-10), Poor (11-20) and Out of Top 20 (KB1399). This is a rank distribution. It replaces ARP as the main story.
- B03: A date drop-down switches between scan dates. "Mini heatmaps" show a strip of past heatmaps for one keyword.
- B03: Semrush "Share of Voice" is a weighted rank metric, not the share of top-3 spots. Same words, other formula (KB1399, API doc).
- B03 product page: The competitor list marks the own business with a "You" tag and shows Avg Rank, rating and review count per business.
- B04: "Versus mode" compares two grids side by side. The two grids can be a competitor or your own past scan.
- B04: A live white-label share link and a one-click screenshot are offered for client reports. "Plot competitor locations" shows where rivals sit on the map.
- B04: The hero preview shows a green-to-orange gradient behind rank numbers. Header stats read 74%, 3.9 and 92% with no words attached.
- B05: Each keyword row has a coloured thumbnail of the grid, the last scan date, a Visibility Score, an arrow with a change figure and a sparkline. A filter box sits on top. This is the best small-multiples row I found.
- B05: The share view needs no login. Header facts list grid size, distance, total points and keyword count.
- B06: A word label "Excellent" sits next to the average rank (2.1) on a green square. This turns a rank number into a verdict.
- B06: A "Visibility Score" bar has a "How is this calculated?" info icon. The tooltip says top 3 counts high, 4-10 moderate, 11+ low. The page lists click-rate estimates per position (`unverified` as data).
- B06: Counts replace percentages: 34 spots in the top 3, 37 in the top 10, 0 not found, "based on 37 search locations".
- B06: "Geographic Strength" shows North, South, East and West as four percentages with change figures. Owners read compass directions easily.
- B06: A "Recommendations" card gives a sentence in plain words, such as keep up reviews.
- B06: The competitor table has a "Threat" column. It is the share of spots where the rival beats you, with Major / Moderate / Low bands. The idea is good. The word is too harsh for a clinic.
- B06: A date strip, a play button and a speed control step through scans. This is a time-lapse of the grid.
- B07: A strip shows Visibility 60.4% (+4.5), Sentiment 95, Position #1 and SoV 16% (-1.1). These are demo numbers.
- B07: A multi-line chart plots one line per brand over time. The own brand has a "You" tag.
- B07: The FAQ defines visibility as the percentage of AI answers that mention the brand. It splits results per AI engine.
- B08: In Local Falcon each grid point is one AI answer sample. A report holds 9 to 441 samples because the same question gets different answers each time.
- B08: The report adds SAIV, sentiment, a "Buyer Persuasion Score" and a "Brand Phrases" list. The hero image shows found (green 1) versus not found (red) pins.
- B08: The page says AI visibility is inclusion or exclusion, not a rank. There is no position 1-20 in an AI answer.
- B09: The Trend Report plots ARP, ATRP and SoLV against the top five competitors. It offers bar, line, animated map and CSV. It needs two or more scans with the same settings.
- B10: Ahrefs defines "AI Share of Voice" as the share of AI responses in a topic set that mention or cite the brand versus competitors. Another meaning of the same words.
- B10: "Estimated Impressions" weights each prompt by the search volume behind it. This is the link between D21 and D20.
- B10: The tracked platforms are AI Overviews, AI Mode, ChatGPT, Perplexity, Gemini, Copilot and, for custom prompts, Claude. KPI tiles carry a big number and a small caption.
- B11: The Visibility Overview gives an "AI Visibility Score" from 0 to 100 and a "Distribution by LLM" module. This is the per-platform split.
- B11: A "Share of Voice vs. Sentiment" chart compares brands. Prompt tracking gives Visibility and Average Position per platform (ChatGPT Search, Google AI Mode, Gemini), shown next to normal Google rankings.
- B12: Colour must not be the only way to carry meaning (WCAG 1.4.1). Graphics need 3:1 contrast, text 4.5:1. Label directly instead of using a legend. The page states about 8% of men are colour blind.
- B12: Do not write "the green line" in body text. The reader may not see green.
- B13: The competitor list shows the whole local field, ordered by ATRP, with ARP and SoLV per business. A pin-level view shows the search results at each point.
- B14: A vendor says SoLV is the metric to report to a client. The sample sentence says "top 3 across 62 percent of the area, up from 38". This supports the plain-count form. Bias: the vendor sells a rival tool.
- B14: A single scan is a snapshot. A scheduled series is a trend line. Colours: green top 3, then yellow, orange, red.
- B15: Every panel uses the same scale on both axes. Use at most 12 panels. Order panels in a logical way. Add a reference line (such as an average) to every panel. Put annotations on the first panel only.
- B15: Comparing inside one panel is easier than across panels. Panels reduce the reliance on colour.
- B16: Every KPI is paired with a signal and a next step. Example: low coverage means check the prompts first. Our "what this means" line copies this idea.
- B16: A "Brand Visibility Index" quadrant has three zones: Leaders, Niche, Low Conversion. This is a 2x2 map. It is too abstract for clinic owners.
- B16: The page says day-to-day numbers move and the trend matters. This supports a "no real change" state.
- B17: A "Visibility Rankings by Topic" board marks where the brand leads and where it needs work. "Previous period" and "Compare competitors" are toggles.
- B17: A claim about overlap with Google's sources is a vendor claim. `unverified`, not used.
- B18: Grids are stored per location and can export as a time-lapse GIF. The site calls this proof for client retention. Each pin opens the competitors at that point.
- B19: Hover on a rank shows the ranking page, the time of the data and a link to a stored search screenshot. This is a "proof" link for each number. It also splits map results from normal results.
- B19: Tags decide which keywords the client sees and which stay internal.

## 3. Patterns

### P1 — Grid heatmap with a plain-word legend
- What: One map, 49 dots (7x7). Each dot shows the rank number inside. Colour follows 4 bands: 1-3, 4-10, 11-20, 20+. (B01, B02, B06)
- Add: a legend with words, set above the map, not in the corner. Example: "Top 3 = people see you first". Mark the office position.
- Use for: the one hero keyword, and the detail view of any keyword.
- Avoid: 18 big maps stacked. Avoid colour as the only code (B12). Keep the numbers in the dots. Avoid dark red over most of the map, because it scares non-data readers. A single-colour scale is an option to test (our idea, not from a source).
- Note: The proximity effect is real (B02). Ranks fall with distance from the office. Add one line to say so.

### P2 — Small multiples: keyword rows with a thumbnail
- What: One row per keyword. Parts: keyword, mini heat thumbnail, one number, arrow, sparkline. (B05, B03)
- Rules: same scale in every row (B15). Order by a logical rule, such as "needs work first". Max 12 rows per block (B15), so split 18 keywords into themes or 9 + 9.
- Use for: D12 and D14 across many keywords.
- Avoid: a thumbnail without a number (too small to read). Avoid sparklines when there are fewer than 4 scans. Show "first scan" instead.

### P3 — Best 5 / worst 5 (and "close to top 3")
- What: Three short lists: "You win here" (top 3 on most spots), "Close" (rank 4-10), "Missing" (not in top 20). Each list shows at most 5 keywords.
- Source: our own derivation. Related ideas are the lead / needs-work marks in B17 and the signal-to-action pairs in B16.
- Use for: the first screen when there are more than 8 keywords.
- Avoid: showing only the best 5. Show both ends. The brief says gaps show as gaps. Put a link "all 18" under the lists.

### P4 — Change arrow with a baseline and a "no real change" state
- What: One arrow per number: change since last month. A second, quieter arrow or text: change since the first scan. (B03, B05, B06, B02 "Then vs Now")
- Use for: D12, D13, D19, D20, D49.
- Avoid: arrows for tiny moves. AI answers vary per run (B08, B16). Set a rule for "no real change". The threshold is our decision (`unverified` — no source gives one).
- Option: a before/after pair of grids or a time-lapse (B04, B09, B18). Do not autoplay on mobile.

### P5 — Competitor leaderboard with the client row pinned
- What: Top 5 competitors for one keyword. The client row is always visible with a "You" tag, even at rank 9. Columns: name, top-3 share, rating. Add the review count in small type. (B03, B06, B13)
- Use for: D15 on one chosen keyword. Use a drop-down for the keyword.
- Avoid: 15 rows of strangers (B06 shows 15). Avoid the word "Threat". Use "beats you on X of 49 spots". Avoid showing a chain that is not a real peer without a note.

### P6 — Distribution bar (where on the map you appear)
- What: One stacked bar per keyword: Top 3 / 4-10 / 11-20 / not in top 20. (B03 "Good / Average / Poor / Out of Top 20", B06 counts)
- Use for: D12 and D13 together. The bar shows the whole picture in one line and replaces the average rank.
- Avoid: more than 4 bands. Avoid red-heavy colour. Add the numbers on the bar or on hover.

### P7 — AI visibility as a heat strip (keywords x 3 platforms)
- What: Rows are keywords. Columns are ChatGPT, Gemini, Google AI mode. Each cell shows the value as text and as a 3-step fill. A headline shows the total as a count: "named in X of Y answers". (B07 per-engine split, B11 "Distribution by LLM", B08 samples)
- Use for: D20. This is our own design for 16 x 3.
- Must have: the number of answers per cell, and a "not tested" state. AI answers vary per run (B08).
- Avoid: a line chart with 48 lines. Avoid a single average over the three platforms. Avoid the word "rank" or "position" (B08: AI has inclusion, not a rank). Avoid "recommends": a mention is not a recommendation.

### P8 — One plain-word line under each block: what it means, what we do
- What: A one-sentence reading plus one action by 741. (B16 signal-to-action, B06 "Recommendations", B02 and B01 AI analysis)
- Use for: every block in the section.
- Avoid: text from a tool with no human check. Avoid long advice. One fact, one next step. A person checks it before it goes live.

## 4. Plain-language names

Recommended option is marked with *. Each option has a label and a one-line help text. Keep the same word on every page.
All numbers in the help texts are examples.

### SoLV (share of the map where you are in the top 3)
| # | English label | English help text | German label | German help text |
|---|---|---|---|---|
| 1* | Top-3 coverage | "In 31 of 49 spots around you, you are one of the first 3 results." | Top-3-Abdeckung | "An 31 von 49 Punkten im Umkreis steht der Eintrag unter den ersten 3 Treffern." |
| 2 | Map visibility | "How much of your area shows you in the first 3 results." | Sichtbarkeit auf der Karte | "Auf wie viel Prozent des Gebiets der Eintrag unter den ersten 3 steht." |
| 3 | Found-first share | "The share of your area where people see you first." | Anteil „zuerst gefunden“ | "Der Anteil des Gebiets, in dem der Eintrag zuerst auftaucht." |

Notes:
- Option 1 has a count form ("31 of 49") that avoids the % sign. This follows the plain sentence in B14 and the counts in B06.
- Do not use "share of voice". Three tools use it with three meanings (B01, B03, B10).

### ARP (average rank on the map)
| # | English label | English help text | German label | German help text |
|---|---|---|---|---|
| 1* | Typical position | "In most spots you appear around place 6 in the list." | Typische Platzierung | "An den meisten Punkten steht der Eintrag etwa auf Platz 6." |
| 2 | Average place in results | "Your average place on the map list. Lower is better." | Durchschnittsplatz in den Treffern | "Der mittlere Platz in der Kartenliste. Niedriger ist besser." |
| 3 | Where you usually rank | "The place you usually hold when people search nearby." | Üblicher Platz | "Der Platz, den der Eintrag bei Suchen in der Nähe meist hat." |

Notes:
- Tools differ. Local Falcon ARP skips spots at rank 20 or lower (B01). Semrush counts 21 for those spots (KB1399). Which one our data uses is `unverified`. Write the rule in a footnote.
- Lower is better. Say so in the help text.
- Keep it secondary. A good ARP can sit next to a low top-3 coverage.

### SAIV (share of AI voice)
| # | English label | English help text | German label | German help text |
|---|---|---|---|---|
| 1* | Named in AI answers | "In 19 of 48 AI answers we checked, your practice was named." | In KI-Antworten genannt | "In 19 von 48 geprüften KI-Antworten wurde die Praxis genannt." |
| 2 | AI mention rate | "How often ChatGPT, Gemini and Google AI mention you." | KI-Erwähnungsquote | "Wie oft ChatGPT, Gemini und Google KI den Eintrag erwähnen." |
| 3 | AI visibility | "Whether AI tools bring your name up when people ask." | Sichtbarkeit in KI-Antworten | "Ob KI-Werkzeuge den Namen nennen, wenn Menschen fragen." |

Notes:
- "Named" is safer than "recommended". A mention is not a recommendation (B08 has a separate score for persuasion).
- The "x of y" form needs a sample count per cell. Whether our D20 data stores one is `unverified`.
- Use "practice" or "clinic" per client type. Do not hard-code it.

## 5. Recommendation per data point

Each row: best form, 2 alternatives, one risk.

| ID | Best form | Alternative 1 | Alternative 2 | Risk |
|---|---|---|---|---|
| D12 Top-3 share per keyword | One big plain count ("31 of 49 spots") with a change arrow, plus a P6 distribution bar. Per keyword, the same in a P2 row. | Ring gauge with the % in the centre | Plain % with a word label ("Strong / Building / Weak") | Top 3 is the only win. A rank-4 spot counts as zero, so a good result can look like 0%. Decimals add false precision (B01 KB32 uses them). Round to whole numbers. |
| D13 Average rank on the map | Small secondary stat "Typical position: 6" in the detail view only. | Fold into the P6 bar and drop the number | Show as a line over time in the detail view | Two definitions exist (skip rank 20+ or count it as 21). Lower is better and readers forget it. The first screen must not lead with this number. |
| D14 7x7 grid image | P1: one hero grid, large, with numbers in the dots and a words legend. Other keywords as P2 thumbnails that open the full grid. Always visible, not behind a toggle. | Before/after pair (B02, B04) | Time-lapse slider (B06, B09, B18) | Grid settings must stay fixed. Trend views only work for scans with the same settings (B09). If we only hold an image and not the 49 values, we cannot draw numbers in the dots. Whether we hold the values is `unverified`. Show the radius, which is also unknown here. |
| D15 Competitors per keyword | P5: top-5 leaderboard for one chosen keyword, client row pinned with "You". One line: "X beats you on N of 49 spots". | Two grids side by side: you and the top rival (B04, B02) | Bar chart of top-3 share for the top 5 | The competitor set changes between scans. The biggest names may not be real peers. A "Threat" label hurts trust. Public names are fine, but check the tone. |
| D19 Normal search rank | A second small column in the keyword row: "Normal results: #7, up 2". Label it apart from the map. | Dot plot of web rank per keyword in the detail view | Separate "Google results" tab | Two ranks for one keyword confuse. Use two clear names: "On the map" and "In normal results". Rank depends on where and how the search runs. Map and web results are separate things (B19). |
| D20 Share in AI answers | P7 heat strip, 16 x 3, values as text, plus a count headline. | Three small bars, one per platform (average), with the keyword list one click away | Per-platform big number with a trend line (B07 style) | AI answers vary per run (B08). Without a sample count the % can mislead. Small moves are noise (B16). "Named" does not mean "recommended". |
| D21 Monthly search demand | A small bar or 3-dot level ("high / medium / low") inside each keyword row. | Sort the keyword list by demand | Show demand as a number only in the detail view | Volumes are estimates. Small local markets can be thin or empty (`unverified` for Bali). A missing value must show as a gap, never as 0. AI prompt volume is not the same as search volume (B10). |
| D49 Visibility score vs ranked clinics (45 of 100) | One number with a dot strip: all ranked clinics as dots on a 0-100 bar, "You" highlighted, plus "rank 7 of 20". | P5-style leaderboard of clinics | Number plus a word band ("Building") | The method of the 45 is `unverified` in the inventory. It needs a one-line how-to-read and a fixed formula. A score out of 100 reads like a school grade. A second "score" next to SoLV causes confusion (B06 also uses this word). Use only one score on the page. |

## 6. Three layouts for "Am I easier to find?"

Common rules for all three:
- First line is one sentence with a count and a change. Example: "On the map you are in the top 3 on 31 of 49 spots, up from 22 in September."
- Every block has a P8 line: what it means, what we do.
- Same words on every page: "On the map", "In normal results", "In AI answers".
- Mobile 390: one column. Desktop 1440: two columns at most.

### Layout A — "One answer, then proof" (recommended)
Reading order, top to bottom:
1. Headline sentence + 3 tiles: On the map (D12), In normal results (D19, plain), In AI answers (D20). Each tile has a count and an arrow.
2. Hero grid, large (D14), with a before/after switch.
3. Keywords: "You win here / Close / Missing" lists (P3), then "all 18" as P2 rows.
4. Competitors for the hero keyword (D15, P5).
5. AI strip (D20, P7) and the clinic score (D49).
- Pros: tells one story. Works on a phone. Best for a non-data owner. Gaps show as lists.
- Cons: the page is long. AI sits low.

### Layout B — "Three lanes"
Three cards side by side (stacked on mobile): On the map | In normal results | In AI answers.
Each card: one big number, one arrow, one mini visual (distribution bar / rank dot / three platform bars), one P8 line, a "details" link.
D14, D15, D21 and D49 live in the detail pages.
- Pros: fast scan. Maps to the three kinds of data. Easy to keep the layout stable across clients.
- Cons: three numbers with three units invite wrong comparison. The grid image hides behind a click, which repeats the old problem.

### Layout C — "The keyword list is the page"
Top: headline sentence + D49 clinic score.
Below: one list of all keywords as P2 rows, in blocks of 9. Each row has a thumbnail (D14), a distribution bar (D12), the web rank (D19), 3 AI dots (D20), a demand bar (D21) and an arrow.
Click a row: a drawer opens with the big grid, the competitor board (D15) and history.
- Pros: everything for one keyword sits in one place. Scales to 18 and 14 keywords. Easy to see which keyword to fix.
- Cons: the densest layout. On mobile many columns drop. If thumbnails and bars do not carry the weight, it looks like the old table.

Suggested decision card: A as the page, with C as the "all keywords" view behind it, and B as a summary card on the Overview tab. Martin decides.

## 7. Open points and risks

- Data check before design: do we hold the 49 point values per keyword, or only the grid image? If only the image, P1 cannot draw numbers in the dots. `unverified`.
- Data check: how many AI answers sit behind each D20 percentage? `unverified`.
- Data check: how is D49 (45 of 100) calculated? `unverified`.
- Data check: which ARP rule does our scan data use? `unverified`.
- Colour: green / yellow / orange / red is the market standard (B01, B02, B14). Red-heavy maps may scare a clinic owner. Test a calmer scale in the prototype.
- Naming: tool names stay out of client files. This file is internal.
- Hold the "no real change" threshold for arrows as an open decision for Martin.
