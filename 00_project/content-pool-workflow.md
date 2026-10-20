# Content Pool Workflow

Status: v1 draft. Date: 2026-10-11. Owner: Martin. Tested once, on the Dumann dry run (existing site, health client, HWG).
Skill draft: `00_project/content-pool-skill/`. Not installed. Data model: `00_project/content-pool-data-model.md`. Schema: `00_project/content-pool-item.schema.json`.

**Contents**
0. Purpose and outcome · 1. Where it plugs in · 2. Hard rules · 3. Trigger and inputs · 4. Storage · 5. The four pillars · 6. Steps · 7. Scoring · 8. Competitor set · 9. Demand signals and cost · 10. Compliance · 11. Existing-site mode · 12. Output · 13. Lessons from the Dumann dry run · 14. Known gaps · 15. Sitemap step (checkpoint 2) · 16. Scripts

---

## 0. Purpose and outcome

The workflow turns real search demand and competitor data into the **content pool**: a ranked list of what goes on a client website. The site must mainly show the client's own services and data. The pool adds the content that makes the site findable and well converting. The goal is that the client has the best chance to out-rank the local competitors and to convert the visitors it gets.

The pool has four pillars: (1) location, (2) main service, (3) brand, (4) authority. Homepage items get full detail. Items for other pages get one line and a page tag.

**Done (all must be true):**
1. `scripts/validate_pool.py` passes with 0 errors.
2. Every item has proof: a raw data file and a reference. Every number comes from a script, not from typing.
3. Every item passed the fit test against the client's real service list.
4. Every health item has an HWG flag (or BRAO flag for lawyers). Blocked items are cut.
5. Every competitor that could not be read is listed as unreadable. None is read as "nothing found".
6. The HTML report was checked in a rendered screenshot, desktop and narrow.
7. Paid spend is at or under the cap and is reported.
8. Martin said "go" on the draft pool.

## 1. Where it plugs in

The pool is its own step. Martin can run it alone. CRO Step 1 can also call it, before it collects its own data.

| Existing workflow | What the pool does | Change in that document |
| --- | --- | --- |
| `cro-homepage-workflow.md` Step 1 | The pool replaces rows 1.5 (keywords) and 1.6 (rankings). Rows 1.1 to 1.4 and 1.7 to 1.11 stay. The pool reuses the scrape and GBP data from `02-data/dataset.md` when they exist. | **Applied 2026-10-11:** new row 1.0 "run or reuse the content pool (not older than 30 days)". Rows 1.5 and 1.6 point to the pool. |
| `cro-homepage-workflow.md` rule 7 ("No competitors are analysed") | The pool analyses competitors for content and proof, not for design. | **Applied 2026-10-11:** rule 7 reads "Competitors are analysed only through the content pool". Rule 6 allows the pool's client form as a draft. |
| `cro-homepage-workflow.md` Steps 2 and 3 | Diagnosis uses the pool to rank gaps. Copy writes the top homepage items. | **Applied 2026-10-11:** Step 2 and Step 3 read `pool-top.md`. |
| CRO P0 blueprint (10 rows) | The pool never removes a row. It ranks what goes into each row. | None. |
| `website-struktur-master-prompt.md` (exists in worktree `admiring-nightingale-f0f882`, not on `main`) | The sitemap step (section 15) follows its rules and takes the pool as data. The portal client report (its steps 8 to 10) can be built later from `sitetree.json`. | None. Bring the master prompt to `main`. |
| `page-content-qa-checklist.md` gate A0 | Competitor reads follow A0: retry failed fetches, verify numbers, count words by script, benchmark floor of 70 % of the competitor median. | None. |
| `seo-page-optimizer` | A later page run reads the pool items of that page as its data package. | Optional input. |
| `backlink-dach` | Authority link targets go to it as a list. | None. |

## 2. Hard rules

1. **Real data only.** No guessed fact, price, volume or credential. A gap carries `[FEHLT]`. A claim in text must match a number in the data (check by script or by tokens).
2. **Fit first.** The keyword must match a service the client really offers (memory `keyword-must-match-service`). Competitor keywords that fail the test are cut and logged. They are never a target.
3. **Strategy before pages.** Start from who the client serves and what already works, then what the market shows. Use proven concepts. Do not invent new methods (memory `never-reinvent-the-wheel`).
4. **Volume "no data" is not zero demand.** Build the autocomplete tree and read People Also Ask before you drop a topic.
5. **Do not copy competitors.** Competitors show what visitors expect (table stakes) and where the gap is. They are not text sources.
6. **No scaled copy.** A place page needs demand, a catchment signal and unique local facts. All three. Otherwise the place is named in text only.
7. **Health clients.** HWG mode: no healing promises, no disease lists, no before/after, no fear wording. Lawyers: BRAO and UWG (see CRO rule 10).
8. **Never send, publish or change a live site.** The pool only writes local files. The client form is a draft until Martin says "go".
9. **Paid data stays under the cap** (default 5 USD). Local Falcon scans stay out unless Martin says "go".
10. **No method sources and no tool names in client material.** The method is called "741 Content-Pool-Raster". Replies and working files are STE. Client text is normal German with "du".

## 3. Trigger and inputs

Trigger: `/content-pool <client>` or a phrase such as "Content-Pool für <Name>". Do not use it for page copy (`seo-page-optimizer`), the CRO prototype (`cro-homepage`), the sitetree (structure playbook), or a single practitioner page (`behandler-seite`).

Martin gives: client name, URL (or "new site"), city, GBP link, mode (new or existing), industry mode (HWG, BRAO or none), cost cap (default 5 USD). The agent asks once, in one line, if one is missing.

## 4. Storage

Local: `00_project/assets/<slug>/content-pool/` (layout in the data model, section 2). Drive: `Local SEO/<Client>/Content Pool/` (report and sitemap as PDF, HTML and xlsx, `pool.json`, raw-data zip, `_status.md`; old versions to `_archiv/`). Stage with `scripts/stage_drive.py`. Upload with the CRO browser method (JS click on "File upload", then `file_upload` on the file input; about 10 MB per call). Check the Drive listing against `_drive/MANIFEST.json`. Dumann: folder id `1wVxMLaJDgt6CoOiU6XPba1Q1MJqszPHP` (uploaded 2026-10-11, 17 files). At run start read `_status.md` and continue at the step named as next.

## 5. The four pillars

| | Location | Main service | Brand | Authority |
| --- | --- | --- | --- | --- |
| **Question it answers** | Where does the client work, and why should a local searcher choose her? | What exactly does the client do, for whom, at what price, how does the first visit go? | Who is she, what is different, how does she sound? | Why should the visitor and Google trust her? |
| **Client input (from the client)** | Address, access, catchment, second places, one name everywhere | Service list, exclusions, ideal client, prices, first-visit steps | Story, method, voice, audiences | Credentials, roles, memberships, reviews, quotes with consent, photos |
| **Added from outside** | Place demand, local pack, competitor place coverage, schema types | Questions (PAA, autocomplete), cost topics, seasonal peaks, competitor depth | How competitors present themselves (only to find the difference) | Competitor proof elements, review counts, directories on page 1 |
| **Main sources** | NAP record, GBP, DataForSEO volume, SERP local pack, competitor sitemaps | Live site, `dataset.md`, autocomplete, PAA, DataForSEO, Trends | `brand.md`, client form, SERP of the niche | Live site, GBP, SERP local pack, client form |
| **Typical items** | Hero with city, location block, places in text, schema, name consistency | Service cards and pages, question sets, prices, first visit, FAQ | Positioning, method in 3 sentences, story, audience split | Qualifications block, roles, proof strip, patient quotes, link targets |
| **Stays out** | Place pages without proof, place swapping | Services the client does not offer. Competitor-only keywords. Disease-based claims | Invented positioning, claims the client did not give | Unproven titles, invented numbers, quotes without consent |

## 6. Steps

Copy this list into `_status.md` and tick it off. The agent runs steps 0 to 8 without asking. It stops at a failed gate, at the cost cap, and at the checkpoint.

- [ ] **Step 0 Readiness.** Check inputs. Create the folder. Test DataForSEO access and balance. Test GSC access with `scripts/gsc-client-export.mjs` on the `www` and the non-`www` property (the property type matters). A 403 on all: ask Martin to add `reporting-bot@studio-apis-503306.iam.gserviceaccount.com`, or read the Performance table in Chrome with a Google account that has access (try `authuser=0,1,2` in the URL). Set the cap.
- [ ] **Step 1 Client baseline → `01-client/client-baseline.md`.** Services, places, brand, proof, prices, audiences, own rankings, `[FEHLT]` list. Reuse the CRO `dataset.md` and `brand.md` when they exist. Existing site: crawl the sitemap and measure the home page and key pages. If `[FEHLT]` items block pillars: write the German client form (`client-form-<slug>-de.md`) as a draft.
- [ ] **Step 2 Seeds.** Seeds come from the real services × core place × neighbour places × question words. Check each seed against the service list. Write the seed list with the volume call.
- [ ] **Step 3 Competitor set → `02-competitors/`.** SERP for 6 to 10 key searches (local pack, organic, PAA, AI overview). Choose the set (section 8). Measure pages with `scripts/page_metrics.py`. Crawl sitemaps with `scripts/site_urls.py`. Gate A0: retry failed fetches (HTTP, headless Chrome, Firecrawl). Report the rest as unreadable.
- [ ] **Step 4 Demand → `03-demand/`.** Volume calls, autocomplete tree (`scripts/autocomplete_tree.py`), PAA from the SERPs, ranked keywords of own and competitor domains, Trends for seasonal terms, GSC if available, review language, optional AI-answer prompts by hand.
- [ ] **Step 5 Candidates → `04-pool/candidates.json`.** The agent writes the judgment per item: pillar, audience, page tag, section, fit, fit reason, conversion, effort, HWG flag, search patterns, `[FEHLT]`. No number is typed here.
- [ ] **Step 6 Build → `04-pool/pool.json`.** Run `scripts/build_pool.py`. It adds all numbers, scores, priority and live status. Write `04-pool/summary.json` (findings, pillar text, decisions for Martin).
- [ ] **Step 7 Validate.** Run `scripts/validate_pool.py`. Fix until 0 errors. Check each typed claim in `summary.json` and in `cover_note` fields against `pool.json`.
- [ ] **Step 8 Report.** Run `scripts/render_report.py`. Open the HTML in Chrome. Check desktop and narrow width and one opened card. Fix until the check passes.
- [ ] **CHECKPOINT: Martin reads the draft pool and says "go".** He decides the adjacent items and the split of audiences. Changes: only named items are revised.
- [ ] **Step 9 Hand off.** Upload to Drive (report, xlsx, `pool.json`, `_status.md`). Write `04-pool/pool-top.md` (homepage items by CRO row, as input for CRO Step 3). Give Martin the Drive link, the screenshot and the draft client form message. Append the run to the lessons list in section 13.

## 7. Scoring

Full formula and rules R-S1 to R-S6: `content-pool-data-model.md` section 4. In short: `0.30 demand + 0.25 gap + 0.25 fit + 0.15 conversion + 0.05 effort`. A at 75 or more, B at 55 or more. Fit 1 is never A. Fit 0 is cut. The priority never removes a CRO P0 row.

Judgment inputs (fit, conversion, effort) stay with the agent. Every other number comes from the data. Martin can change a judgment value in `candidates.json` and rebuild.

## 8. Competitor set

| Tier | Who | How chosen | Used for |
| --- | --- | --- | --- |
| local | Practice sites of the same trade in the client's city | Maps top 3 (SERP local pack) and organic top 5 of the main local search, portals removed | Gap, table stakes, benchmark |
| niche | Practice sites for the client's special method | SERP of the "method + trade + city" search | Gap in the niche |
| topic | 2 to 3 national topic sites | SERP of the topic search ("method medicine", "costs") | Depth of education content |
| portal | Directories and booking platforms (doctolib, jameda, …) | Seen on page 1 | **Not competitors.** They become link targets |

Per page we measure: words, H1 to H3, schema types, FAQ, price, rating, phone link, form, booking hint, places named, credential words, sitemap URLs. The benchmark is the median of local homepages (not service pages). The floor is 70 % of that median (gate A0). "Better than the competitors" means: more complete on the table-stakes blocks, a real answer to the unmet topics, and stronger proof.

## 9. Demand signals and cost

| Signal | Tool | Cost (Dumann run) |
| --- | --- | --- |
| Search volume | DataForSEO `keywords_data/google_ads/search_volume/live` | 0.09 USD per call of up to 1,000 terms |
| SERP, local pack, PAA, AI overview | DataForSEO `serp/google/organic/live/advanced` | 0.002 to 0.0035 USD per search |
| Competitor ranked keywords | DataForSEO `dataforseo_labs/google/ranked_keywords/live` | 0.013 to 0.03 USD per domain (limit 150) |
| Trends | DataForSEO `keywords_data/google_trends/explore/live` | 0.011 USD |
| Autocomplete tree | Google suggest, free | 0 |
| Own queries | GSC via service account (`scripts/gsc-client-export.mjs`, then `scripts/gsc_to_tsv.py`), or the Performance table read in Chrome (500 rows per page, `get_page_text`) | 0 |
| Review language | GBP reviews | 0 |
| AI-answer prompts | Chrome, by hand, optional | 0 |

Dumann run total: 0.38 USD for 22 paid calls (2 volume, 11 SERP, 8 ranked-keyword, 1 Trends). The cap is 5 USD. `scripts/dfs.py` logs every call in `spend.jsonl` and stops at the cap. Avoid `keyword_ideas/live` (expands too broadly). Trends: terms in one graph are relative to the biggest term. Small terms read as 0 to 1. Ask for a small term alone.

## 10. Compliance

- Every item has `compliance.mode` and `flag`. Review items carry a note with the rule.
- HWG: no healing promises, no disease lists, no before/after, no fear wording. Education about a method is allowed. Complaint-based topics are `review` at best and `adjacent` when the client does not clearly offer them.
- A `block` item is cut. A cut item needs a `decision_note`.
- Lawyers: BRAO § 43b, BORA § 6, UWG. Title claims need proof.

## 11. Existing-site mode

Same steps. Step 1 also crawls the own sitemap and measures the key own pages. Step 6 adds `live_status` per item. The check is coarse: an own page needs its own URL (event, product and blog URLs do not count). A heading or card on another page is `weak`. FAQ sets are never `present` without a manual read. The report says "Auto check. Confirm by hand."

## 12. Output

`05-report/content-pool-report.html`: findings first, one card per pillar, the homepage map (CRO rows), items for other pages, detail per pillar (filter, open cards with numbers and raw data links), cut items, decisions for Martin, open client facts, raw data. `05-report/content-pool.xlsx`: sheets Pool, Keywords, Competitors, Needs client (formatted, filters, frozen header).

## 13. Lessons from the Dumann dry run (2026-10-11)

1. A client can have two audiences (practice and school). None of the 63 known rankings was a patient search. They were for training, lexicon pages and single method terms. The `audience` field and an early split decision fix this.
2. The biggest competitor keywords were for services the client does not offer (Colon-Hydro 6,600, HPU 5,400). The fit gate cuts them. Without it, the pool would target the wrong topics.
3. National head terms inflate demand ("darmsanierung" 18,100). Rule R-S1.
4. The volume tool returned no data for real local searches ("heilpraktiker charlottenburg"). Autocomplete confirmed them.
5. Competitors that most local sites have (prices, first visit, FAQ) are expected content. Rule R-S2.
6. A gap with no demand is not an opportunity. Rule R-S3.
7. One measured page per competitor is not enough for a service topic. The sitemap check shows if a page exists.
8. Some sites need a headless Chrome read, and one site blocked every method. It stays "unreadable" and the related claim carries a caveat.
9. I typed "3 von 13" in a note. The data said 3 of 12. Notes must not hold numbers that the script can compute. Check typed claims.
10. Portals dominate page 1. They are link targets, not competitors.
11. The live-site check matched event pages. The URL exclusion rule fixed it. Keep a human check.
12. The first scoring gave 28 items priority A. The thresholds and rules R-S1 to R-S4 brought it to 10.
13. GSC returned 403 for the service account. Martin's own Google account had access, so the tables were read in Chrome first. Later Martin added the service account, and the export worked for the `www` property only. Both sources matched within about 4 %. The client's own queries confirmed real demand for Schilddrüse and Aderlass (already near the top) and showed that fasting searches land on a course page far from page 1. Rule R-S5 scores this signal. Use `scripts/gsc_to_tsv.py` to turn the export into the evidence files.
14. Chrome could not post the table to a local server (the browser waits for a local-network permission). Use `get_page_text` after setting 500 rows per page. Tool output is cut at about 1,000 characters for `javascript_tool`.

## 14. Known gaps (v1)

- AI-answer prompts are not automated and were not run.
- Review language uses only the reviews that Google shows without login.
- The catchment area and the neighbour places come from search data, not from the client yet.
- Local Falcon scans are not part of the run. Existing reports are read for the baseline.
- `live_status` is a coarse automatic check.
- Tested on three runs: two health practices (Dumann, Hüwel; HWG) and one law firm (Stürzl; BRAO). Not tested: a new site without a live site, a second run for the same client.
- Skill trigger tests and the with/without baseline are not run yet.

15. (Stürzl run, law firm) The site had no `sitemap.xml`. `site_urls.py` now crawls internal links as a fallback and stores up to 5,000 URLs. A first version cut the list at 600 and would have missed pages of large sites.
16. (Stürzl) For a law firm almost every service is table stakes and the client offers almost all of them. All scores sat between 60 and 74 and no item reached A. Rule R-S6 takes the best quarter (total of 65 or more) as A when fewer than 5 items reach A. The gap is depth and structure, not topics, and the report must say so.
17. (Stürzl) The search tool returned "invalid field location_name" for a German city name, and an empty result with cost 0. Use `location_code` for cities (Frankfurt am Main 1004363). A result with 0 items is an error, not "no results".
18. (Stürzl) `zsh` does not split an unquoted variable into words. Pass long domain lists with command substitution, or from a file.
19. (Stürzl) Before any redirect proposal, compare the texts (5-word shingles). Three Selbstanzeige pages shared 97 % and 74 % of their phrases. A fourth page on the same topic shared only 31 %. In the Dumann run a Course schema showed that a "duplicate" was a training page.
20. (Stürzl) A page template can add an H1 to every page ("Leistungen"). The finding "2×H1" then means one template fix, not 17 content fixes.
21. (Stürzl) Client-specific text (reasons, "not built") must live in the data file (`tree.json`), not in the renderer. A hard-coded Dumann sentence would have appeared in a law-firm report.

22. (Hüwel run, relaunched site) Search Console data then mixes the old and the new site, and new URLs have no history. The sitemap report shows one note for the whole report (`meta.gsc_note` in `tree.json`) and no "not listed" line per page. DataForSEO knew only 2 own keywords after the relaunch: GSC is the real signal.
23. (Hüwel) A reference page with direct claims of effect may serve as a structure example only. The compliance note says so. A past warning of the client (here 2018) belongs in every compliance note of the run.
24. (Hüwel) Tokens in `summary.json` are not shared: `{words:ST-nn}` works in the sitemap reasons only. A token that the renderer does not know stays as literal text in the report. Check the rendered HTML for braces.
25. (Hüwel) Queries in other languages or typos give a misleading "best position" (an English query at position 1.0). Do not quote a best position for a pattern group. Quote impressions.
26. (Hüwel) macOS has no `timeout` command, and a headless Chrome screenshot can hang. Run it in the background with its own `--user-data-dir` and a kill loop.
27. (Hüwel) Static sites use slugs that end in `.html`. Rule S4 accepts a slash or `.html` at the end. The place rule in the sitemap check reads `meta.places` of the pool, not fixed names.

## 15. Sitemap step (checkpoint 2)

Martin's decision (2026-10-11): after the pool is approved, the next step is the sitemap, built from the pool. The CRO workflow takes only the pool. It does not need the sitemap. The CRO file was changed on 2026-10-11 (row 1.0, rows 1.5 and 1.6, rules 6 and 7, Steps 2 and 3). The sitemap is saved as its own output in the content-pool folder.

The sitemap step does not collect the pool data again. It follows the rules of `website-struktur-master-prompt.md` (three sources, origin per node, status values, catchment levels) and uses `pool.json` as its demand and proof data.

| Step | What | Output |
| --- | --- | --- |
| 10 Inputs | Pool items with page tag. Live sitemap (`site_urls.json`). Own page measures for the real service URLs (`page_metrics.py`). GSC pages (3 months). Backlink summary of the client and 3 competitors. Client content (`dataset.md`). Programme modules (M2, M5, M6, M8, M10, Pflicht) | `05-sitetree/own-metrics.json`, `gsc-pages-90d.tsv` |
| 11 Tree | The agent writes `05-sitetree/tree.json`: nodes with parent, title, status, origin, module, job, path or slug, keyword, `pool_tag` or `pool_items`, `needs_client`. Also redirect proposals and the four catchment levels. Check every redirect idea by reading the target page (a Course page is not a duplicate) | `tree.json` |
| 12 Build and check | `scripts/build_sitetree.py` adds GSC, words, volumes and pool items per node, checks rules S1 to S8, counts the KPIs, renders the HTML and xlsx | `sitetree.json`, `05-report/content-pool-sitetree.html`, `.xlsx` |
| **CHECKPOINT 2** | Martin reads the sitemap and says "go". Then the client report in the portal can be built from `sitetree.json` (master prompt steps 8 to 10). That report is not part of this step | |

Rules (the script enforces them): S1 each node has an origin and a status. S2 "Neu" needs an origin in client content or in the programme. A topic from search data only is "Vorschlag". S3 "Bleibt" and "Überarbeiten" need a URL in the live sitemap. S4 new slugs are lower case. A place in a slug needs a place item in the pool. S5 each pool item with priority A or B and a page tag is on a node. S6 no cut item on a node. S7 KPI counts equal the nodes. S8 no duplicate path.

Lessons from the Dumann sitemap:
1. A Course schema on a page showed that a "duplicate" was a training page. The redirect idea was wrong and was removed. Read the target page before any redirect proposal.
2. The strongest patient page (`/schilddrüse`, 40 clicks) names "Mikroimmuntherapie" and "Schilddrüsenspezialist". Neither is in the client's service list. Protect the URL, and clear the claims with the client first.
3. The domain has more referring domains (148) than two of three competitors. Links are not the gap. Reviews and local presence are. Always measure before you write the "why".
4. The service pages are long (446 to 2,638 words). The work is a text rework, not a rebuild. Only the homepage and the practitioner page are thin.
5. GSC hides rare queries. For Dumann the query rows add up to 113 clicks, the page rows to 375. Use the query file for demand and the page file for traffic per URL. Do not mix the totals.

## 16. Scripts (in `00_project/content-pool-skill/scripts/`)

| Script | Job |
| --- | --- |
| `dfs.py` | One DataForSEO call with a spend log and a cap |
| `page_metrics.py` | Measure pages. HTTP, then headless Chrome. Reports unreadable pages |
| `site_urls.py` | Read sitemaps. Without a sitemap it crawls internal links (depth 3, up to 200 pages) |
| `autocomplete_tree.py` | Google autocomplete tree with question words |
| `build_pool.py` | Join judgment and data. Compute numbers, scores, priority, live status |
| `validate_pool.py` | Schema, raw-number match, rules, spend. Exit 1 on error |
| `gsc_to_tsv.py` | Turn the GSC export into the evidence files for the pool and the sitemap |
| `render_report.py` | HTML report and xlsx |
| `stage_drive.py` | Stage the Drive upload: flat names, PDFs, raw-data zip, manifest |
| `build_sitetree.py` | Sitemap step: build from `tree.json`, check rules S1 to S8, render HTML and xlsx |

## Registry entry (2026-10-11)

Every run of this workflow is recorded in the workflow registry. The Excel `~/Desktop/Workflow-Uebersicht.xlsx` shows per client whether the workflow ran, its state, the last run, Martin's approval and the folder links.
- At the start or end of a run: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py upsert --client "<client>" --workflow pool --status "in Arbeit|Trockenlauf|fertig, Freigabe offen" --local <folder> --drive <url> --result <file>`
- When Martin approves the result: `python3 /Users/martindrendel/741website/00_project/workflow-registry/workflow_registry.py approve --client "<client>" --workflow pool` in the same turn, then tell Martin the sheet was updated. A hook reminds Claude when a message sounds like an approval.
Workflow id: `pool` (Content Pool).

## Registry: automatic (2026-10-11)

The overview Excel `~/Desktop/Workflow-Uebersicht.xlsx` updates itself. A Stop hook runs `workflow_registry.py sync --quiet` after every turn. You do not call `upsert` for normal progress. Write one line per step into `00_project/assets/<client>/content-pool/_status.md` (date at the start of the line). When `05-report/content-pool-report.html` exists and the Drive upload is logged in `_drive/_status.md`, `sync` shows fertig, Freigabe offen.
For any other file layout, write `_run.json` in the run folder (schema in `00_project/workflow-registry/README.md`). Only the approval stays manual: when Martin approves a result, run `approve` in the same turn and say that the Excel is updated.

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. In this workflow: in the client version of the pool report and the sitemap: present at each pillar, point at the A priorities, think at client questions. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
