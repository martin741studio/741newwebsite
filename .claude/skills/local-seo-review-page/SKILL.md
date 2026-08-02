---
name: local-seo-review-page
description: >
  Build a prospect Local-SEO review/audit deliverable end-to-end — research → Local Falcon
  Maps scan → Drive analysis sheet → personalised review landing page (German "du" style with
  Maps-grid + Loom video) → deploy. Use for any new LOCAL business prospect (physical location /
  Google Business Profile), e.g. a practice, Treuhand, clinic, salon. Trigger on "review page for
  <name>", "audit page", "make the review page", or when Martin drops a LinkedIn/contact card of a
  prospect. For ONLINE / no-GBP / English prospects use the organic variant at the bottom.
---

# Local-SEO Review Page — repeatable SOP

**This is a fast (~2–3 min once data is in hand), multiple-times-per-week process. Follow it in order; do not re-derive.** Two source memories back this: `local-seo-sheet-workflow` and `review-page-fast-workflow`.

## Inputs (grab from the LinkedIn/contact card)
Business name · contact **first name** (for "Hallo <Vorname>,") · city/region · website (or email domain) · LinkedIn URL. **Never** put personal data (mobile, birthday) on the page or in the sheet.

## Step 1 — Research & VERIFY (never let the generator invent metrics)
- `searchForLocalFalconBusinessLocation {term, proximity:"<city>, <country>"}` → confirms the **GBP** and returns `place_id, lat, lng, rating, reviews, categories, phone, address`. **No GBP found → switch to the organic variant (bottom).**
- Verify the site with one curl (try http AND https — old sites often fail SSL):
  ```bash
  html=$(curl -sSL <url>); \
  printf '%s' "$html" | grep -oiE "<title>[^<]*</title>"; \
  printf '%s' "$html" | grep -oiE '<meta[^>]+name="description"[^>]*>'; \
  echo "H1:$(printf '%s' "$html"|grep -ociE '<h1') schema:$(printf '%s' "$html"|grep -ociE 'ld\+json') viewport:$(printf '%s' "$html"|grep -ociE 'name=.viewport')"; \
  printf '%s' "$html" | grep -oE "G-[A-Z0-9]{10}|GTM-[A-Z0-9]{6,}|UA-[0-9-]+"; \
  printf '%s' "$html" | grep -oiE 'jimdo|wix|wordpress|squarespace|webflow|generator" content="[^"]*"'
  ```
  Check HTTPS validity (`curl -sSI https://…`), TTFB (`curl -w "%{time_starttransfer}"`), sitemap, favicon. Record **only verified** facts. Common real findings: no H1, no schema, dead UA / no GA4, no HTTPS, default favicon, old CMS (Jimdo `---.html` URLs = Jimdo).
- `WebSearch "<name> <city>"` for competitors + context.

## Step 2 — Local Falcon Maps scan (CONFIRM credits with Martin first)
- Save the business: `saveLocalFalconBusinessLocationToAccount` (must be saved before a scan).
- **Ask Martin to OK the scan + confirm the keyword** (e.g. "Treuhänder <Stadt>", "Steuerberater <Region>"). Then `runLocalFalconScan {placeId, keyword, lat, lng, gridSize:"9", radius:2, measurement:"km", platform:"google"}`. It returns "submitted" → **poll** `listLocalFalconScanReports {placeId}` (do NOT re-run — that burns credits).
- `getLocalFalconReport {reportKey, fieldmask:"report_key,keyword,arp,atrp,solv,found_in,unique_competitors,image,heatmap,insights.solv_competitors.total,rankings.by_solv"}` → grab `arp/solv`, top competitors, and the grid **image**.
- Download the grid image → convert to WebP → save at `04_site/public/review-assets/<slug>/scan.webp` for the page's `.maps-vs-section`.

## Step 3 — Drive analysis sheet (Chrome UI only — no Sheets API here)
- Create prospect folder: `create_file {mimeType:'application/vnd.google-apps.folder', parentId:'1WS-FQ-W0D_CeYN0tpM2Va1Jl_U0ynoxi', title:'<Name>'}`.
- Copy blanko master into it: `copy_file {fileId:'1WTsonTvVZKcnxCVgnGIMxrGG5QSPxC1Ra-WPq06Bk5M', parentId:<folder>, title:'Local SEO Analyse – <Name>'}`.
- Open the copy at `#gid=1653072650` (Analyse tab) in claude-in-chrome (Martin = martin.stylectric@googlemail.com).
- Layout: meta C4/E4,C5/E5,C6/E6 · §1 r10-16 · §2 GBP r20-39 · §3 Website/Technik r43-64 · §4 Citations r68-75 · §5 Keywords r79-84 · §6 Competitors r88-90 (+r91 Ads) · §7 Maßnahmen r95-100 (C=Priorität Hoch/Mittel/Niedrig). Status dropdown OK/Fehlt/Teilweise/n/a; **leave blank = "live prüfen"** (only verified findings get a status).
- **Sheet-fill gotchas (deadly):** ① after opening, wait ≥5s, screenshot, click the "You're signed in as…" **OK** popup (it silently eats keystrokes), then type ONE cell + screenshot-verify before batching. ② Navigate with the **Name box** (click ~[50,127], type ref, Enter) — **never arrow keys** (they concatenate). ③ `Enter` moves down only AFTER a typed value; never Enter-skip a blank cell (Name-box-jump instead). ④ **No blank lines in a typed block** (`\n\n` is swallowed → whole column desyncs) — split into contiguous Name-box-anchored blocks. ⑤ Autocomplete extends a typed prefix that matches an existing column entry — type a distinct full string. ⑥ Leading `+` → `#ERROR!` formula (write phone as `0xx …`). ⑦ `Ø` / em-dash break; regular umlauts + en-dash `–` are fine.

## Step 4 — Review page (the FAST part)
- **ALWAYS `cp 04_site/review/claudia-hauser/index.html` as the base.** It is the canonical, mobile-perfect skeleton. **NEVER base it on `praxis-suriya`/`gusborn` (older — they lack the `.maps-vs-section`) and NEVER hand-roll the maps-vs section, the target grid, the scorecard, or the wording — copying a wrong base + inventing sections is exactly what makes it look off and burns Martin's time (learned the hard way 2026-07-30, Bechtel).**
- claudia-hauser is **data-driven**: `window.PROSPECT_DATA = {…}` holds companyName, contactName, city, branch, loomUrl, loomDuration, mapsRankDesktop, focusKeyword, currentReviewsCount, currentRating, mobileSpeedScore, personalMessageGreeting, authorName, positives[], opportunities[], criticalIssues[], gbpAudit/websiteAudit/citationAudit [{title,status:good|warning|critical,desc}], competitors[{name,rank,reviews,category,advantage}], keywords[{keyword,region,volume,currentRank}], quickWins[{title,desc}], growthMetrics{currentRank,targetRank,callsIncrease,routesIncrease,leadsIncrease,trustLabel}, roadmap[{step,action,priority,effort}]. A render script `.map()`s these into element IDs. **To swap: read the file, replace the whole object (brace-count to `};\n  </script>`) via `json.dumps(dict, ensure_ascii=False, indent=2)`, then `json.loads`-validate.** (Barbara-Brunner lesson: never string-`.replace()` inside PROSPECT_DATA.)
- Then fix the **hardcoded** bits (NOT in PROSPECT_DATA): the static H1 fallback ("Hallo <Vorname>,<br>wir haben…" — crawlers run no JS), hero subheadline city, the hero Maps-card `href` (query + query_place_id) & website-card `href`+badge, the `.maps-vs-section` (date, N Messpunkte, radius, keyword, left `<img src="/review-assets/<slug>/scan-grid.webp">` + caption "X von Y Punkten…", right target SVG, impact chips), the Loom `<iframe>`, and the 3 static `<p>` in `.letter-body`. Keep `{{> header_de}}/footer_de/consent}}`. German "du" throughout.
- **Maps scan section is EXACTLY claudia's:** light `#f7f6f2` bg, LEFT card badge "● Heute – echter Scan" + the real scan WebP, RIGHT card badge "● Das Ziel – so kann es aussehen" + a numbered green target SVG whose grid density matches the scan (49→7×7, 81→9×9 — generate circles programmatically, colors #136c2e/#2e8b34/#4d9a3f/#7aa83f, center highlighted w/ lemon stroke, label "Ziel-Szenario (Simulation)"). Save the LF grid PNG→WebP as `review-assets/<slug>/scan-grid.webp`.
- **Loom:** if Martin gave `…/share/<id>`, embed `https://www.loom.com/embed/<id>` in the video-responsive iframe. If not, placeholder + TODO — **never invent a video**.
- **Client-proof wall (social proof — standard since 2026-07-30, Martin "very important, as proof"):** the claudia-hauser skeleton now carries a `<section class="section-proof">` right before the Final CTA — our real client roster as `.wc` cards (avatar/initials + green rank-change line "▲ Platz 17 → 4 · „keyword""), heading "Ist der Sprung in die Top 3 realistisch? Für diese Betriebe war er es." So `cp claudia-hauser` includes it automatically. CSS is **self-contained + scoped under `.section-proof`** (explicit hex, no dependency on page tokens) so it drops into any page. Cards are lifted verbatim from `pages/growth-plan-de.html`'s `<div class="wall">`; avatars live at `/review-assets/people/*.jpg`, proof screenshots at `/review-assets/proof/*.jpg` (already deployed). To retrofit pages: DE cards come from `pages/growth-plan-de.html`'s `<div class="wall">`; the **EN version is the one already on the Bali Google-Ads LPs** — `pages/bali-local-seo.html` `<div class="wall">` (heading "The businesses we have worked with", "▲ Rank 17 → 2 · …"). Injection scripts: `/tmp/build_proof.py` (DE) and `/tmp/build_proof_en.py` (EN, extracts the Bali wall) — both inject CSS before `</style>` + section before the Final-CTA/footer marker. English review pages (e.g. house-of-eluma) get the EN wall; German pages the DE wall.
- **OG tags** in `<head>` (og:type/title/description/url + twitter:card; og:image = the scan WebP).
- **Verify at 375px before deploy (hard rule):** `document.documentElement.scrollWidth === innerWidth` (no h-overflow), headline visibly bigger than subheadline, navbar not overlapping hero.

## Step 5 — Deploy & verify
`npm run build` then `npm run deploy` (incremental FTP). Confirm live: `curl -sSL https://741.studio/review/<slug>/ | grep -E "<h1|<title>|og:url"` → 1 H1 with the real first name, correct title/OG.

## Step 6 — (optional) Mail
Send the prospect their page link (Ich-form, Martin's voice) or notify `mdrendel@icloud.com` per the run's instruction.

---
## VARIANT — online / no-GBP / English prospect (e.g. House of Eluma)
`searchForLocalFalconBusinessLocation` returns nothing for them → pivot to an **English organic/website audit**: in the SHEET mark §2 GBP + §4 local-citation rows `n/a`; core = §3 Website/Technik + §5 keywords + §6 ORGANIC competitors. On the PAGE `cp praxis-suriya`, swap `{{> header_de}}`→`{{> header}}` & `footer_de`→`footer`, English "Hi <Name>," style, **drop the Maps-scan** (there is none), reframe the 4 audit tabs to Website·On-Page·Analytics·Authority. Example: `04_site/review/house-of-eluma/`.
