# Data readiness — Bali Healing pilot (13.10.2026)

Read-only check. Free reads only: Search Console, GA4, Local Falcon (LF) reports, portal selects. No scans, no paid calls. Values come from files or live reads on 13.10. `unverified` = not checked. NHC = Natural Health Center profile. Beauty = Beauty Clinic profile.

## 1. Table

| D-ID | Page needs | Real source | Readable today | Latest value (date) | History | Gap or risk |
|---|---|---|---|---|---|---|
| D01–D03 | Calls, website clicks, directions, both profiles | LF MCP `getLocalFalconGbpPerformanceMetrics`, one place ID per profile | yes | NHC Sep: 21 calls, 224 clicks, 230 directions. Oct 1–13: 8 / 67 / 105. Beauty Sep: 2 / 59 / 97 | Daily, 378 days read (from 2025-10-01; older not tested) | We store nothing. Last 2–3 days fill late (see e). Roadmap table shows NHC only; its Sep row is stale |
| D04 | Profile views | Same tool, default metrics (4 impression types, maps and search) | yes | NHC 10–26 Sep: 3,261 | Daily, same range | Sum four metrics. No "views" total from Google |
| D05 | WhatsApp clicks | GA4 property 428850764, event `contact_whatsapp`, service account | yes | Aug 321, Sep 313, Oct 1–13: 123 | Daily 2 Aug–13 Oct (73 days) | Before 2 Aug not tracked. Counts the click, not the chat. Memory note "service account cannot read this property" is stale |
| D06–D07 | Form leads, hand-added leads | Portal `leads`, `site_form_submissions` | yes, empty | 0 rows | None | No form path on the Wix site. GA4 shows `generate_lead` 34 and `form_submit` 1 since 1 Aug; meaning `unverified` |
| D08–D11 | Booked jobs, value, cost per job | None. Only the client knows | no | — | None | Booked jobs live in WhatsApp Business. Cost basis = ad spend only (decision 6) |
| D12–D13 | Top-3 share and average rank per keyword | 80 files `assets/audit/balihealing/2026-10-11-kickoff/evidence/falcon-report-*.json`; live `getLocalFalconReport` | yes | ozone therapy 38.78% / ARP 3.78 (12 Oct); naturopath 71.43% / 2.98 (10 Oct); acupuncture bali 2.04% / 13.52; skin tag removal bali 0.00% / 5.00 (1 of 49 spots); iv drip therapy bali 0.00% / 21.00 (0 of 49) | Only "ozone therapy" has a same-setting series: 21 Sep 57.14, 28 Sep 53.06, 5 Oct 34.69, 12 Oct 38.78. Others: 1 scan | Three scan settings mixed: 9x9 5 mi (2 Jun), 7x7 3 km (Aug–22 Sep), 7x7 5 mi (from 23 Sep). Beauty: 13 of 14 keywords 0.00%. 49 credits per scan; 261 package credits left on 11 Oct, cycle ends 19 Oct |
| D14 | Grid, 49 points per keyword | LF `getLocalFalconReport` with fieldmask `data_points` | yes | 49 points read for 3 reports | Not stored | See (a) |
| D15 | Competitors per keyword | `places` block in each scan file (name, reviews, rating, categories, top-3 share, ARP) | yes | iv drip scan 10 Oct: 58 competitors | Per scan only | `competitors.json` holds 6 hand-picked. No quarter diff |
| D16–D18 | Search clicks, position, queries | Search Console, service account is full user on `https://www.balihealing.com/` (checked 13.10.); `scripts/gsc-client-export.mjs` | yes | Clicks Jul 653, Aug 609, Sep 599, 1–10 Oct 191. 28 days to 8 Oct: 554 clicks, position 11.4 (Chrome read 11.10.) | Daily 1 Jan–10 Oct (283 rows). 90-day queries and pages stored in `assets/balihealing/content-pool/03-demand/` | 3-day lag. URL-prefix property only. Brand queries lead ("bali healing" 234 of 874 query clicks, 90 days). Query rows 874 vs page rows 1,838 (hidden queries) |
| D19 | Rank in normal results | No scheduled tracker. DataForSEO `ranked_keywords` file 11 Oct (paid, not re-run). GSC position per query is free | partly | GSC position 11.4 | One snapshot | Not a true rank per keyword. Name it "average position in Google Search" |
| D20 | Share in AI answers | LF AI scans: 48 reports dated 23 Sep (16 keywords x ChatGPT, Gemini, AI Mode) in the LF index | yes | Platform means in roadmap: ChatGPT 55.6%, AI Mode 36.8%, Gemini 26.5% | One run | 9 samples per cell (see b). Portal `visibility_prompts`: 0 rows for Bali |
| D21 | Search demand | `evidence/search-volume-2026-10-11.json` (DataForSEO, 25 terms) | file yes; refresh paid | iv drip bali 1,300; iv drip canggu 390; acupuncture bali 260; ozone therapy bali 210; skin tag removal bali 40 | One snapshot, 11 Oct | 9 of 25 terms return null. Null = no data, not zero demand |
| D22–D23, D25 | Review count, rating, new per month, unanswered | LF `listLocalFalconGbpReviews`, both profiles | yes | NHC 100 reviews, 4.7; 21 unanswered, 79 with reply. Beauty 10, 5.0; 2 unanswered | Dated reviews back to 2016. NHC new in 2026: Jan 7, Feb 2, Jun 1, Jul 2, Sep 3, other months 0 | Roadmap says "no replies": wrong. It read the newest 7. The 8 newest are all unanswered (latest 29 Sep) |
| D24 | Gap to local leader | `places.reviews` in scan files. Blood Ozone Bali: 118 (Aug), 125 (21 Sep), 128 (5 Oct scan) | partly | Leader 128; target 2x = 256 | Snapshots per scan | Leader differs per keyword. Beauty leader not read (`unverified`) |
| D26–D27, D30 | Programme week, work items, decisions | Portal (`tasks`, `work_items`, `approval_items`) | yes | 44 tasks, 2 done. 8 work items (2 waiting, 2 to check, 4 planned; updated 13.10.). 7 approval items, all draft | Live state | Week 5 starts 14.09 per `status-2026-10-13/task-cleanup-draft.md`; not in DB (`unverified`). Onboarding 1 of 6 done |
| D28–D29 | Blockers, client requests | Only hand-built tables in `status-2026-10-13/build_roadmap_v3.py` | no | 5 blockers, 7 requests (13 Oct) | None | No table. Needs a store |
| D34 | Last update from 741 | `client_reports` last row 23 Sep; `activity_log` last row 19 Aug | partly | 20 days by report row | — | Roadmap v3 went live 13 Oct under the old row. Table says "stale", page is fresh |
| D35 | Early warnings | None | no | — | — | Rules decided (round 5, #20). No engine. Tracking module not installed |
| D36–D37 | Ad status, spend, clicks, WhatsApp clicks, cost per click (IDR) | Chrome read of Google Ads UI, file `evidence/ads-read-2026-10-13.json`. GA4 link confirms totals | needs access (browser login; no API developer token) | Paused since 1 Oct. 6–12 Oct: 0 clicks. All time: 685 impressions, 61 clicks, IDR 571,785, 14 WhatsApp conversions, IDR 40,842 each, CPC IDR 9,374 | All-time plus text snapshots (10 Aug, 19 Aug). Billing: Aug 297,191, Sep 338,784, Oct 10,133 | No weekly series. Billing is 13.0% above campaign cost (646,108 vs 571,785; tax inferred). GA4 ad metrics repeat the campaign total per session: do not sum. Skin tag campaign: 2 drafts, unpublished |
| D41 | Backlink funnel | Drive sheet "Bali Healing CRM - 741 Studio" (state 12.10.). Not read today | needs access | 149 requests, 38 accepted, 38 messaged, 14 in talk, 9 offers, 0 live | Since 25 Sep; no snapshots | `morning-grill/2026-10-13/send-pack.md` flags 38 accepted vs 38 messaged as maybe different groups |
| D42 | Backlink quality | DataForSEO backlinks summary, 3 snapshots | file yes; refresh paid | 11 Oct: 1,034 links, 1,001 domains, 25 broken, spam score 51 | 7 Sep 66 / 44 / 27. 23 Sep 73 / 50 / 25. 11 Oct 1,034 / 1,001 / 25 | 14x jump in 3 weeks from a spam push; competitors show about 1,000 too. Tiles would show noise. Roadmap says rank 104, file says 101 |
| D43 | Listings live | Portal `client_citations` | yes, empty | 0 rows. 5 directories found, none listed | None | Citation module not set up for Bali |
| D49 | 45 of 100 | `run.json` field `score_total` | yes | 45, coverage 90% (13 Oct, Go-B) | 1 run (46 on 11 Oct, before the Ads field changed) | See (c) |

## 2. Answers

**(a) 49 point values or only images?** Not in our files. All 80 `falcon-report-*.json` hold only `arp`, `atrp`, `solv`, `found_in` and `places`. No `data_points` key exists. The roadmap shows LF-hosted images (`lf-static-v2.localfalcon.com/image/<key>`). LF still returns the 49 values on request, free. I read 3 reports on 13.10. Each point has `found`, `rank`, lat, lng and a top-5 list. Fix: save `data_points` at every scan. How long LF keeps old reports is `unverified`. `scripts/render_falcon_grid.py` rebuilds a grid image from the points.

**(b) AI sample size per cell.** 9. The AI scans use a 3x3 grid (`grid_size` 3, 48 reports, all dated 23 Sep). Audit field B12.01 says "3x3 grid with 9 points". Every share is a multiple of 11.11% (1 of 9). It is one run, one answer per point. One step equals 11 points. One cell, Gemini "ozone therapy bali" at 12.50%, equals 1 of 8. Why it has 8 is `unverified`. Show "5 of 9 spots" with the date. Show no trend before 3 runs.

**(c) How the 45 is calculated.** Weighted mean of audit block scores. Source: `audit-workflow/scripts/score.py`, `run.json`. Weights: B05 profile and rankings (25 points of weight), B06 live technical check (15), B10 profile quality (15), B11 competitor benchmark (15), B07 off-page (10), B13 risk (10), B12 AI (5), B04 geography (5). A block score is the mean of field colours (critical fields count 3). A block under 70% coverage drops out. B04 (50%) dropped, so weights sum to 95. Result: 4,280 / 95 = 45.05, shown as 45. Coverage 90% is the weighted share of fields with data. Field colours are set by the agent. It is not a comparison with ranked clinics. Only B11 (15%) benchmarks competitors, score 68. The design idea "rank 7 of 20" has no data. Roadmap line "measured against the clinics that rank above you" is wrong. Name it "Profile and site readiness".

**(d) ARP rule.** Not-found spots are skipped. ARP = mean rank over spots where the profile shows in the top 20. ATRP counts a not-found spot as 21. I recomputed from 49 points: ozone 5 Oct, 42 found, ARP 3.83, ATRP 6.29 (both match the files). Skin tag 10 Oct: 1 found at rank 5, ARP 5.00, ATRP 20.67. Acupuncture 10 Oct: 21 found, max rank 20, ARP 13.52, ATRP 17.80. ARP 21.00 means "found nowhere" (placeholder). Risk: ARP flatters thin presence ("5.00" from 1 spot). Show "spots found" beside rank, or use ATRP.

**(e) Zero website clicks 15–23 Sep.** Data delay, not a real break. Evidence read 13.10.: (1) LF now returns 4, 8, 14, 9, 7, 5, 8, 9, 4 = 68 website clicks for NHC on those days, and 13 call clicks. (2) Search Console clicks were 29, 23, 14, 24, 22, 14, 21, 22, 20 per day. (3) GA4 organic sessions were 14–27 per day. (4) WhatsApp clicks were 9, 6, 3, 17, 11, 13, 7, 13, 13. (5) Full Sep now shows 224 website clicks. The roadmap table showed 104 for 1–23 Sep. The nine days alone now hold 68. Limit: I cannot see what Google showed on 23 Sep. Action: remove the "flatline" text from the roadmap, refresh the Sep row, mark the last 3 days "still filling".

## 3. Pilot readiness

**Ready now (6)**
1. D01–D04 Google profile actions. Next: pull and store monthly rows. Owner: agent.
2. D05 WhatsApp clicks. Next: store daily rows from GA4. Owner: agent.
3. D16–D18 Search Console. Next: store daily and monthly rows. Owner: agent.
4. D22–D23, D25 Reviews. Next: store monthly counts and unanswered. Owner: agent.
5. D12–D13, D15 latest scan values and competitors. Next: copy into the store. Owner: agent.
6. D26–D27, D30 portal state. Next: read at render time. Owner: Dinakar.

**Needs a small fix (12)**
1. D14 49 points. Next: save `data_points` at each scan. Owner: agent.
2. D12–D13 history. Next: lock one setting (7x7, 5 mi) and keep weekly "ozone therapy". 49 credits per added scan, Martin's go. Owner: Martin.
3. D24 leader history. Next: save leader review count at each scan. Owner: agent.
4. D20 AI cells. Next: show "x of 9 spots" with date. Repeat the run in 4 weeks. Owner: agent.
5. D19 rank. Next: use Search Console position and rename it. Owner: agent.
6. D21 demand. Next: store the snapshot. Show "no data" for null terms. Owner: agent.
7. D36–D37 ads history. Next: export weekly rows Aug–Sep from the Ads UI via Chrome. Show spend without tax. Owner: agent.
8. D41 funnel. Next: read the CRM sheet, store a weekly count, confirm 38 vs 38. Owner: agent, Martin confirms.
9. D42 backlink quality. Next: define "rated risky" so the spam push does not show as growth. Owner: Martin decides, agent applies.
10. D43 listings. Next: create Bali rows when the first listing goes out. Owner: agent.
11. D49 score. Next: rename and fix the roadmap sentence. Owner: agent.
12. D28–D29, D34. Next: add two small tables and a "last update" date set at publish. Owner: Dinakar.

**Blocked (3)**
1. D06–D11 leads, booked jobs, value, cost. No lead path on the Wix site. Booked jobs only in the client's WhatsApp Business. Next: ask Peggy and Pasha for a monthly booked-job count in the portal. Owner: Martin.
2. D36–D37 automatic ad feed. The account is paused (verification open since 1 Oct) and no API developer token exists. Next: finish client verification. Apply for the token. Owner: Martin.
3. D35 early warnings. No engine. The tracking module is not installed. Next: build after the store exists. Owner: Dinakar.
