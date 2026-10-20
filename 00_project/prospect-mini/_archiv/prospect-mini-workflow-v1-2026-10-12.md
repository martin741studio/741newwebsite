# Prospect Mini Workflow (as run, v1)

Status: first test run done on 2026-10-12 (Catja Grieshaber, Claudia Tiemann). Both pages are live. This document describes the workflow as it ran. Martin wants to define it further.

## 1. Goal

One small run collects only the data that the new review page needs. It does not run the five big workflows (Content Pool, Maps Audit, Un-Burning, CRO Homepage, Maps Playbook). Those stay for paying clients.

Reference page: `04_site/review/anja-stuerzl-v2/` (built from the full Stürzl data). Result pages: `https://741.studio/review/catja-grieshaber-v2/` and `https://741.studio/review/claudia-tiemann-v2/`.

Cost per prospect in the test: about 0,19 USD DataForSEO, 0 Local Falcon credits (both scans existed). With a new scan: plus 49 credits (7×7). Without the wasted Labs call (see Lessons): about 0,17 USD.

## 2. Page sections and their data

| Page section | What it shows | Source | Cost |
| --- | --- | --- | --- |
| Hero | greeting, one-line finding, 4 cards, video (or placeholder), CTA "Zeig mir meinen Markt", Martin "hello" | Google Maps panel (Chrome), Falcon report, site check | 0 |
| Map | real scan image + target grid (simulation), caption, Martin "point" | Local Falcon, 1 scan 7×7 (reuse if one exists) | 0 or 49 credits |
| Step 1: What clients search | search volumes (questions vs. provider searches), terms without data, length of own vs. competitor pages, 6 new content items, Martin "think" | DataForSEO `keywords_data/google_ads/search_volume/live` (1 task), `serp/google/organic/live/regular` (2 tasks), page measurement | ~0,10 USD |
| Step 2: Phone rings | own Google entry vs. 4 competitors (category, reviews, share of map), 6 entry changes, 4 clean-up numbers, good news, Martin "insight" | Falcon report of the same scan, name searches (2–3 SERP tasks), spam links (`backlinks/summary` + `backlinks/referring_domains` with spam filter ≥ 60) | ~0,06 USD |
| Step 3: Homepage | today's first screen vs. draft of the first screen, score today (22-point list), target 36+/44, 5-question test | screenshot (Chrome), HTML draft with the prospect's logo + photo, screenshot of the draft | 0 |
| Calculator | organic (map + search) and Google ads separately, real volumes + real price per click | Step 1 data | 0 |
| Website check (piano) | 4 strips × 2–5 points (Passt / Ausbaufähig / Dringend), photos from the prospect | site check | 0 |
| Quick wins, roadmap | 6 quick wins, 5 roadmap rows | derived from the findings | 0 |
| Proof (under the map, folded) | 4 compact result cards visible; behind a toggle: 4 cases with start state + changes, 5 short results; chosen by branch and main gap; Martin "celebrate" | `prospect-mini/case-library.json` | 0 |

## 3. Run steps

1. **Input from Martin:** name, website, Google Maps link. Optional: Loom URL.
2. **Find the scan.** Search the Local Falcon reports for the place (`listLocalFalconScanReports`, 0 credits). If none exists: pick the keyword that shows the gap (not the win), then run 1 scan 7×7.
3. **Read the Falcon report** (`getLocalFalconReport`, 0 credits): own entry, top competitors with categories and reviews. Save to `evidence/`.
4. **Google Maps panel (Chrome):** rating, review count, category, visible owner replies, age of the newest visible reviews.
5. **Site check (free):** `prospect-mini/scripts/collect_site.py <dir> <url>`: title, headline, description, words, phone links, form, tracking, structured data, sitemap, dead links, https, server time, page list + per-page metrics.
   - If the site blocks us (Cloudflare): Martin switches on a German VPN, or sends a screenshot. Page facts can come from the Internet Archive (CDX API, `id_` URLs). State the date of the copy on the page.
6. **DataForSEO (paid, ledger + cap 0,30 USD):** `prospect-mini/scripts/dfs.py <dir> <endpoint> <payload> <name>`:
   - 1 × search volume (Google Ads source, 10–14 terms, country code),
   - 2 × SERP for the main services (top 20, scan centre as coordinate),
   - 2–3 × name searches (does the own website appear?),
   - 1 × backlinks summary + 1 × spam domains.
7. **Competitor page lengths:** `content-pool-skill/scripts/page_metrics.py` on the top 5 provider pages per service (skip directories).
8. **Homepage:**
   - Screenshot of today's first screen (Chrome, 1440 px wide, without browser bar).
   - Score today against `knowledge/cro-library/_derived/scorecard.md` (22 points).
   - Build the draft of the first screen as HTML in `prospects/<slug>/draft/` with the prospect's real logo and photo: headline = service + city, subline = situation + help, stars, button + reassurance, trust row. Same Sie/du form as the prospect's own site. Health: no healing promise, protected titles only if held.
   - Serve it with the launch config `prospect-drafts` (port 8975), screenshot in Chrome.
9. **Write `prospects/<slug>/prospect.json`.** All text in plain language (no tool names, no SEO terms). "du" to the prospect. Every number from `evidence/`, listed in `sources`. Martin guide: one text per placement (`guide.hello`, `point`, `think`, `insight`, `celebrate`).
10. **Build:** `prospect-mini/scripts/build_page.py prospects/<slug>` → `04_site/review/<slug>/index.html`. Images to `04_site/public/review-assets/<slug>/` (scan-grid, startseite-heute, startseite-entwurf, strip photos).
11. **Check:** `prospect-mini/scripts/validate.py prospects/<slug>` (jargon, foreign text, missing images, slots). Then desktop + 375 px in Chrome (iframe test): no sideways scroll, headline bigger than subline, all images load.
12. **Message draft** for Martin (du, no booking link, only the review link).
13. **Deploy after Martin's go:** `npm run build`, then upload. Check every URL with curl (200 + size). Fixed on 2026-10-12: `upload.js` changed into a stray `public_html` folder inside the web root, so new folders never went live. Now it stays in the FTP root when an `index.html` is there.

## 4. Where everything lives

```
00_project/prospects/<slug>/
  prospect.json        all page text and numbers, 1:1 with the page sections
  evidence/            Falcon report, DataForSEO answers, site check, screenshots, archive copies
  draft/               HTML draft of the first screen + logo/photo
  cost_ledger.jsonl    every paid call with USD
00_project/prospect-mini/
  template.html        made from anja-stuerzl-v2 by scripts/make_template.py (9 slots + Martin guide CSS/JS)
  case-library.json    proof cases (only facts from case studies and the proof wall)
  scripts/             collect_site.py, dfs.py, build_page.py, validate.py, make_template.py
04_site/review/<slug>/index.html               generated, never hand-edited
04_site/public/review-assets/<slug>/           page images
04_site/public/review-assets/martin-guide/     character poses + CSS/JS (shared)
```

## 5. Decisions (Martin, 2026-10-12)

- Stürzl v2 is the new review-page standard.
- Plain language for non-technical readers. No "Pool", H1, SoLV, Schema, NAP, Sitemap without a translation.
- Video in the hero, light design, one CTA "Zeig mir meinen Markt".
- No service videos, no "Die wichtigsten Funde" block.
- Website check as the piano element.
- Proof tailored to the prospect: 4–5 cases with start state and changes + 5 short results.
- Calculator shows organic and Google ads separately, with the real price per click.
- No AI-visibility line. Spam-link counter: yes.
- Homepage step is essential: today's first screen next to a draft of how it should look in the first 5 seconds. Draft as HTML with the real logo and photo (GPT images garble text).
- Martin guide character: hello, point, think, insight, celebrate; max 1 per section, about 5 per page.
- Hero (12.10., second round): no fact cards in the hero; the map follows directly. The 4 fact cards move to the bottom ("Deine Ausgangslage auf einen Blick", before the final CTA). On mobile: headline and text, then the video, then the button. The gap below the fixed menu adapts to its real height.
- Homepage images (today and draft) open large on click or tap.
- Proof moves up, right under the map: headline, 4 compact result cards (always visible), Martin "celebrate", and one button "So haben wir es gemacht – N Fälle ansehen" that opens the detailed cases and further results. No proof block at the bottom.

## 6. Lessons from the test run

1. DataForSEO Labs `keyword_overview` returns no volumes for health terms. Use only the Google Ads source. Many health terms still have no number; the page says "Google gibt keine Zahl heraus", never "0".
2. Reuse an existing Falcon scan when it is recent. The review counts in Falcon can be 0 = no data; check the Google panel when it matters.
3. Check categories for legal limits: "Psychotherapeut" is a protected title, so never recommend it to a Heilpraktikerin.
4. The length comparison can go either way. For Catja the gap was the homepage (26 words), not the service pages. For Claudia the content was a strength. Say what the data shows.
5. Name searches find real problems: two different names (Catja), the own site missing for its own name (Claudia).
6. Crop the browser bar from screenshots that Martin sends (it shows his extensions).
7. Old review pages can contain wrong claims (Claudia's old page said "Platz 2–5 around the practice"; the scan shows 20+ there). Always read the scan image again.

## 7. Open points to define

- Which keyword to scan when no scan exists (rule: gap, not win; one scan only).
- How many terms for the volume call per branch.
- A fixed list of standard Google-entry changes per branch (health, law, trade).
- Loom: Martin records after the page is live, then I set `loom_url` and rebuild.
- Message template per channel (LinkedIn, WhatsApp, e-mail).
- Skill packaging (`/prospect-page <name>`).
