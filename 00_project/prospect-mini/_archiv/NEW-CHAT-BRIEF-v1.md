# Brief for a new chat: build a 741 prospect review page (mini workflow)

Paste this file (or point the new chat to it) to start a session that only builds prospect review pages. State: 2026-10-12.

## 1. What you build

A personal review page at `https://741.studio/review/<slug>/` for a local business that Martin wants to win. It shows the prospect, in plain language, where they stand on Google, why, and what changes. Reference pages (live): `catja-grieshaber-v2`, `claudia-tiemann-v2`. Design source: `anja-stuerzl-v2`.

Page order: Hero (headline, text, video, button "Zeig mir meinen Markt", Martin "hello") → Map (real scan vs. target grid, Martin "point") → Results (4 cards visible, cases behind a toggle, Martin "celebrate") → three steps: (1) what clients search (volumes, page length, 6 new content items, Martin "think"), (2) phone rings (competitor table, 6 Google-entry changes, 4 clean-up numbers, Martin "insight"), (3) homepage (today vs. draft of the first screen, zoom on tap, 5-second test) → calculator (unpaid vs. Google ads) → website check (piano strips) → quick wins → roadmap → "Deine Ausgangslage auf einen Blick" (4 fact cards) → final CTA.

## 2. Input from Martin

Name, website, Google Maps link. Later: Loom URL. Martin may also send a screenshot of the homepage.

## 3. Hard rules

- Read `00_project/prospect-mini-workflow.md` (full spec, decisions, lessons) before the first run.
- Plain language for non-technical readers. Never "Pool", H1, SoLV, Schema, NAP, Sitemap, Backlink, tool names. "du" to the prospect.
- Every number from a real source in `evidence/`, listed in `prospect.json` → `sources`. "Google gibt keine Zahl heraus" is never "0".
- Health prospects: no healing or success promise; never recommend protected titles (e.g. "Psychotherapeut" for a Heilpraktikerin).
- Scan keyword must show the gap, not the win. Reuse an existing Local Falcon scan when there is one (0 credits). New scan only 7×7 (49 credits).
- DataForSEO only through `prospect-mini/scripts/dfs.py` (ledger, cap 0,30 USD). For volumes use only `keywords_data/google_ads/search_volume/live` (Labs gives no health data). The IP whitelist rotates: if you see "IP not whitelisted", give Martin the IP from `curl https://api.ipify.org`.
- Site blocks us (Cloudflare; our IP is Starlink Indonesia): ask Martin to switch on a German VPN or send a screenshot. Page facts can come from archive.org (CDX API, `id_` URLs). Say the date on the page.
- Homepage draft: HTML in `prospects/<slug>/draft/` with the prospect's real logo and photo, same Sie/du as their site. Not GPT images (they garble text). Crop browser bars from Martin's screenshots.
- Martin character: max 1 callout per section, about 5 per page, text in first person, max 2 short sentences, no tool names.
- Never hand-edit `04_site/review/<slug>/index.html`. Change `prospect.json`, rebuild.
- Deploy only after Martin's go. Upload only the new paths (see step 9). Check every URL with curl after the deploy.
- No booking link in outreach messages, only the review link. Emails only as drafts.
- Martin's existing clients and their websites are out of scope here.

## 4. Steps and commands

Working folder: `/Users/martindrendel/741website/00_project`. Prospect folder: `prospects/<slug>/` (`evidence/`, `draft/`).

1. **Scan:** search Falcon reports (`audit-workflow/scripts/lf_client.py`, tool `listLocalFalconScanReports`, 0 credits). If none: pick a gap keyword, run 1 scan. Save the report with `getLocalFalconReport` (fields incl. `image`, `places.*.categories`, `reviews`, `solv`) to `evidence/falcon-report-<key>.json`. The map image goes to `04_site/public/review-assets/<slug>/scan-grid.webp`; always look at the image yourself.
2. **Google panel (Chrome):** `https://www.google.com/maps/place/?q=place_id:<id>&hl=de`: rating, reviews, category, visible owner replies.
3. **Site check:** `python3 prospect-mini/scripts/collect_site.py prospects/<slug> <url>`. Then the important checks by hand with curl: phone links (`href="tel:`), http → https, homepage text.
4. **DataForSEO:** `python3 prospect-mini/scripts/dfs.py prospects/<slug> <endpoint> '<payload>' <name>`. Typical set:
   - volumes: 10–14 terms, `location_code` 2276 DE / 2040 AT / 2756 CH;
   - 2 × SERP for the main services (`location_coordinate` = scan centre, depth 20);
   - 2–3 × name searches;
   - `backlinks/summary/live` + `backlinks/referring_domains/live` with filter `["backlinks_spam_score",">=",60]`.
5. **Competitor page lengths:** `python3 content-pool-skill/scripts/page_metrics.py --out prospects/<slug>/evidence/comp-pages.json --lang de <urls>` (top 5 provider pages, no directories).
6. **Homepage:**
   - Screenshot today (Chrome, 1440 wide) → `review-assets/<slug>/startseite-heute.webp`.
   - Score today with `knowledge/cro-library/_derived/scorecard.md`.
   - Build the draft HTML, serve it with launch config `prospect-drafts` (port 8975), screenshot → `startseite-entwurf.webp`.
   - Strip photos from the prospect site → `foto-*.webp`.
7. **Write `prospects/<slug>/prospect.json`.** Copy `prospects/catja-grieshaber/prospect.json` as the model; it shows every field (meta, guide, hero, grid, system.step1/2/3, calc, check, quick_wins, roadmap, proof, final, sources). Optional: `headlines` (overrides per section) and `assets_slug`. Choose proof cases from `prospect-mini/case-library.json` by branch and main gap.
8. **Build + check:**
   - `python3 prospect-mini/scripts/build_page.py prospects/<slug>`, then `python3 prospect-mini/scripts/validate.py prospects/<slug>` (must show 0 errors).
   - Dev server `site-dev` (port 3000). Check `/review/<slug>/` at 1500 px and in a 375 px iframe: no sideways scroll, headline bigger than the text, all images load, the menu does not cover the badge.
9. **Deploy (after Martin's go):** `npm run build` (repo root), then upload only the new paths: `node 00_project/prospect-mini/scripts/upload_only.mjs review/<slug> review-assets/<slug>` (from the repo root; it uploads to the FTP root, never into `/public_html`). Then curl every URL.
10. **Message draft:** du, 3–4 sentences, one real number, only the review link.

## 5. Headline step (optional, test 2026-10-12)

Run the headlines through `00_project/prompts/direct-response-copy-prompts.md`: outcome + benefit + time frame + proof, real numbers only, no dashes. Put the picks into `prospect.json` → `headlines` (keys: hero_h1, hero_sub, grid_h2, proof_h2, system_h2, step1_h2, step2_h2, step3_h2, calc_h2, check_h2, quickwins_h2, roadmap_h2, final_h2). Example: `prospects/catja-grieshaber/headlines-2026-10-12.md` and `prospect-headlines.json`.

## 6. Done means

Page live (200), `validate.py` 0 errors, desktop + mobile checked with screenshots, cost ledger below 0,30 USD, message draft delivered, Loom placeholder noted if no video yet.
