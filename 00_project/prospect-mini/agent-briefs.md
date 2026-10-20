# Agent briefs for the parallel prospect run (v2.1, 2026-10-12)

Only agent O uses Claude in Chrome. Every other agent queues browser jobs in `prospects/<slug>/browser-queue.jsonl` (format: workflow section 1b) and waits for the result file.

The orchestrator (main chat) copies one brief per agent, fills `<slug>`, `<website>`, `<city>` and the other fields from `intake.md`, and starts the agents. Order and dependencies: `prospect-mini-workflow.md` section 1b. Every brief ends with the same handover rule.

Paths: working folder `/Users/martindrendel/741website/00_project`. Prospect folder `prospects/<slug>/`. Images `../04_site/public/review-assets/<slug>/`.

**Handover rule (append to every brief):**
> Write only the files named in this brief. Never use Claude in Chrome yourself (only agent O does); queue a browser job instead. At the end, update your entry in `prospects/<slug>/run-state.json` (status `done` or `failed`, outputs, blockers). In your `.md` file, give every finding with its evidence file name. Do not run a new Local Falcon scan, do not deploy, do not send messages. Reply with: status, files written, cost, blockers.

---

## A Demand (level 1, no Chrome, cheaper model)

> You are agent A (demand) for the prospect review page `<slug>` (<business>, <city>, <branch>). Read `prospects/<slug>/intake.md`.
> 1. One volume call with 10 to 14 terms: 3–4 "provider + city" terms (also the female form, e.g. "heilpraktikerin <city>"), 3–4 service terms from the prospect's real menu, 2–3 question/cost terms ("<service> kosten"), 1–2 neighbouring towns. Command: `python3 prospect-mini/scripts/dfs.py prospects/<slug> keywords_data/google_ads/search_volume/live '[{"keywords":[...],"location_code":<2276|2040|2756>,"language_code":"de"}]' volumes-ads`. Never Labs.
> 2. Two SERP calls for the 2 main services: endpoint `serp/google/organic/live/regular`, `"location_coordinate":"<lat>,<lng>"` of the town centre, `depth` 20. Note: this endpoint lists `local_pack` in `item_types` but returns no map-pack items. Do not claim map-pack positions; the scan decides.
> 3. Name searches (2–3, `depth` 10): "<brand> <city>", "<business name as on Google>". Skip the person's name if it is not the business name.
> 4. Spam links: `backlinks/summary/live` and `backlinks/referring_domains/live` with `"filters":["backlinks_spam_score",">=",60]`.
> 5. A task status `40101` costs money and returns nothing: retry once, then skip and note it.
> Write `prospects/<slug>/demand.md`: table of volumes (no number = "Google gibt keine Zahl heraus"), the gap keyword proposal (real main service, has demand, own site not in the organic top 20), competitor provider URLs (no directories) for the page-length check, name-search findings, spam count (x of y linking domains).

## B Site (level 1, no Chrome, cheaper model)

> You are agent B (site) for `<slug>`, website `<website>`.
> 1. `python3 prospect-mini/scripts/collect_site.py prospects/<slug> <website>` (run in the background; about 2 minutes).
> 2. curl checks: `href="tel:` on home, contact and one service page; `http://` → `https://`; contact form on the contact page (not only on home); duplicate pages (same title and word count, e.g. `/` and `/<name>/`).
> 3. Read the price page if there is one: list every price with its service (for the calculator).
> 4. Health branch: list sentences on the prospect's site that name serious diseases or sound like a healing promise (quote them). They become one neutral "Werberecht" row, never a claim of illegality.
> 5. Second pass, after agent A wrote `demand.md`: `python3 content-pool-skill/scripts/page_metrics.py --out prospects/<slug>/evidence/comp-pages.json --lang de <competitor URLs>` in the background. Report the mean word count and each competitor heading. Say what the data shows; the prospect's pages can be longer (lesson 4).
> Write `prospects/<slug>/site-findings.md`.

## C Homepage (level 1, no Chrome: queues `home_shot`)

> You are agent C (homepage) for `<slug>`, website `<website>`, form of address on the site: `<Sie|du>`.
> 1. If the orchestrator did not queue it yet, append a `home_shot` job for `<website>` to `browser-queue.jsonl`. While it runs, do steps 2 and 3.
> 2. Download the real logo and a real photo of the person and the practice. Use `curl -L` (some site builders redirect image URLs, e.g. cm4all `uproc.php` → `/.cm4all/mediadb/<file>`; `evidence/home-images.txt` from the operator lists the URLs). Crop empty margins from the logo. Open every image before use.
> 3. Build `prospects/<slug>/draft/index.html` from the model `prospects/ana-violeta-fredel/draft/index.html`: headline = service + city and it follows the page's main advice, subline = situation + help, stars, button + reassurance, trust row, the prospect's own colours and form of address. Health: no healing or success promise.
> 4. Draft screenshot with headless Chrome (our own page, no cookie banner): `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --virtual-time-budget=5000 --window-size=1440,838 --screenshot=<file> http://localhost:8975/<slug>/draft/index.html` → `evidence/home-draft-1440.jpg` and `review-assets/<slug>/startseite-entwurf.webp` (cwebp). Save 2–3 strip photos as `review-assets/<slug>/foto-*.webp`.
> 5. When `evidence/home-today-1440.jpg` exists: crop to 1440 wide, save `review-assets/<slug>/startseite-heute.webp`, score it with `knowledge/cro-library/_derived/scorecard.md` (22 points, evidence line for every 0 or 1) → `evidence/scorecard-today.md`.
> 6. Write `prospects/<slug>/homepage.md` (score, the 5-second test answers: Was? Wo? Warum du? Wie zum Termin? Wer?).

## D Scan (level 1 and 2, no Chrome; the panel is an operator job)

> You are agent D (scan) for `<slug>`, place `<business>`, `<city>`.
> **Part 1 (level 1):**
> 1. Find the place_id: `audit-workflow/scripts/lf_client.py searchForLocalFalconBusinessLocation '{"term":"<business>","proximity":"<city>"}'`.
> 2. Search existing scans (0 credits): `python3 prospect-mini/scripts/find_scan.py "<name or place_id>"`. Write `scan-search.md`: usable scan yes/no (recent + keyword fits the gap rule).
> 3. Wait for `demand.md` from agent A (the gap keyword). The Google panel is the operator's job `maps_panel`; read `evidence/google-panel-<date>.md` when you need review counts.
> **Part 2 (level 2, standing G1 go: the keyword passes the gap rule; otherwise stop and set `waiting_gate`):**
> 5. New scan only: `saveLocalFalconBusinessLocationToAccount '{"platform":"google","placeId":"<id>"}'`, then `runLocalFalconScan` with `gridSize "7"`, `radius 5`, `measurement "km"`, centre = the town the keyword names. Never retry. Add a ledger line with `"credits": 49`.
> 6. `getLocalFalconReport` → `evidence/falcon-report-<key>.json`. Download the image, save `review-assets/<slug>/scan-grid.webp`, and LOOK at it.
> 7. Write `competitors.md`: own SoLV (top 3 at x of 49), found_in, rank at the centre point, the top 4 competitors with German category, reviews, share, distance to the centre. Every sentence must match the image.

## E Writer (level 3, main model)

> You are agent E (writer) for `<slug>`. Read `intake.md`, `demand.md`, `site-findings.md`, `homepage.md`, `scan-search.md`, `competitors.md`, `evidence/google-panel-*.md`, and the model `prospects/catja-grieshaber/prospect.json` (every field). Read the rules: `prospect-mini-workflow.md` steps 7 and 8, `assets/brand/martin-guide/README.md`, `prompts/direct-response-copy-prompts.md`.
> Write `prospects/<slug>/prospect.json` with all sections and the `headlines` block (no dashes in headlines). Hero short (Martin 2026-10-12): headline max 14 words, subline in the H1 max 28, paragraph max 35; validate.py fails above that. Plain language, "du", every number from the findings, `sources` filled. Calculator: `val` from the prospect's price page and a multiple of 50 from 100. Proof cases from `prospect-mini/case-library.json` by branch and main gap. Martin guide: 5 texts, max 2 sentences each. Health: no healing promise, no protected titles she does not hold.

## F Fact check (level 5, fresh agent, main model)

> You are a strict fact checker. You did not write the page. Read ONLY `prospects/<slug>/prospect.json`, every file in `prospects/<slug>/evidence/`, the scan image, and `prospects/<slug>/draft/index.html`. You may curl the prospect's own pages cited in `sources`. For every number and claim: SUPPORTED (file + value), UNSUPPORTED, or WRONG. Also flag healing promises, protected titles, jargon, and claims the map image contradicts. Compute counts yourself. Write `evidence/fact-check.md` (table + "Must fix" list). Do not edit other files.

## G Visual (level 5, no Chrome: queues `mobile_check`)

> You are agent G (visual check) for `http://localhost:3000/review/<slug>/` (dev server `site-dev`).
> 1. Append a `mobile_check` job to `browser-queue.jsonl` (the operator checks 375×812 iframes: scrollWidth ≤ 375, H1 bigger than the text, no broken images — the empty `.rvw-lb` lightbox image is fine —, badge not under the menu, proof toggle, zoom). Never use headless Chrome for mobile: it renders wider than 375 px and crops.
> 2. Desktop: full-page screenshot with headless Chrome: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --virtual-time-budget=8000 --window-size=1500,13200 --screenshot=<file> <url>` → `evidence/page-desktop-1500.jpg`.
> 3. Look at every section of the desktop image: wrong numbers on sliders (slider steps round values), empty slots, cut text, images that do not load.
> 4. When `evidence/mobile-check.md` exists, add its result. Write `evidence/visual-check.md`.

## O Browser operator (levels 0–5, the only Chrome user, cheaper model)

> You are agent O, the only agent that uses Claude in Chrome (never the built-in browser). Load the Chrome tools in one ToolSearch call. Create your own tab group with `tabs_context_mcp` / `tabs_create_mcp`.
> Work the jobs in `prospects/<slug>/browser-queue.jsonl` (in a batch: all prospects, oldest `at` first), one at a time. For each job: set `status` to `running`, do it, write the `out` file, set `done`. On a Chrome error: wait 10 seconds, open a fresh tab, retry once; then set `failed` with the reason and go to the next job.
> - `maps_search`: search "<business> <city>"; a match needs the same website AND phone. Write name, address, CID/coordinates.
> - `linkedin_chat`: open the profile, click Message, read the whole thread (scroll up), close the chat window. Never type, never click a suggested reply. Write the thread with dates.
> - `maps_panel`: name (h1), category, rating, review count, age of every visible review ("vor x Jahren"), count of "Antwort vom Inhaber", "Wird auch oft gesucht" list. Do not claim "unclaimed" unless the panel shows it.
> - `home_shot`: window 1440 wide, open the site, click the decline button of the cookie banner (non-essential off), screenshot with `save_to_disk`, copy it to `evidence/home-today-1440.jpg`; list all image URLs (`document.images` + CSS backgrounds) in `evidence/home-images.txt`.
> - `mobile_check`: in a localhost:3000 tab, replace the body with three 375×812 iframes of the page (top, map, competitor table), set all images to eager, measure and screenshot → `evidence/page-mobile-375.jpg` + `evidence/mobile-check.md`.
> When the queue is empty and the orchestrator says the run is done, close all your tabs.
