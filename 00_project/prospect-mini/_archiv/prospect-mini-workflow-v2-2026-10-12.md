# Prospect Mini Workflow v2 (review page for a new prospect)

Status: v2 of 2026-10-12. It replaces v1, which describes the first test run with Catja Grieshaber and Claudia Tiemann. v1 is in `prospect-mini/_archiv/`. Owner: Martin. Runner: Claude Code in this repo.

Trigger: Martin sends a name, a website and a Google Maps link, or says "review page for <name>". This workflow is the standard for LOCAL prospects with a Google profile (Martin, 2026-10-12: "Stürzl v2 is the new review-page standard"). Online prospects without a Google profile still use the organic variant at the end of the skill `local-seo-review-page`.

## 0. Goal and done

One small run collects only the data that the review page needs. It does not run the five big client workflows: Content Pool, Maps Audit, Un-Burning, CRO Homepage and Maps Playbook. The page shows a slim version of each of them: what clients search, the phone-rings levers, and the first screen of the homepage.

**Done means all of these are true:**

1. `validate.py` shows 0 errors.
2. The fact check in step 9 found no number without a source.
3. Desktop at 1500 px and mobile at 375 px were checked with screenshots. Nothing scrolls sideways, all images load, and the headline is bigger than the text.
4. The cost ledger is at or below 0,30 USD, and the scan credits stay within what Martin approved.
5. Martin has the message draft and the link.
6. `_run.json` is written, so the run shows in the overview Excel.
7. The page is live after Martin's go, and every URL returns 200.

Targets per prospect: 0,15 to 0,30 USD on DataForSEO, 0 or 49 Local Falcon credits, about 45 minutes of agent time.

## 1. Gates (Martin decides, the agent stops and asks)

| Gate | When | What Martin approves |
| --- | --- | --- |
| G1 Scan | Only if no usable scan exists | 1 new 7×7 scan (49 credits) per prospect. In a batch, ask once for all new scans with keyword, city and credits |
| G2 Page | After step 10 | The finished page on localhost plus the screenshots, and the message draft |
| G3 Deploy | After G2 | Upload of the new paths only |
| G4 Old page | If an older review page for this prospect exists | Redirect the old page to the new one, or take it offline |

Without a "go", the agent does not run a new scan, does not upload, and does not send anything. It sends no messages at all. Martin sends them himself.

## 2. Page sections and their data

The page order is fixed (Martin's decisions, section 7). Each row lists the data the section needs.

| Page section | What it shows | Source | Cost |
| --- | --- | --- | --- |
| Hero | greeting headline with a finding, short text, video (or placeholder), button "Zeig mir meinen Markt", Martin "hello". No fact cards | headline step, Loom URL | 0 |
| Map | real scan image next to the target grid (simulation), caption, Martin "point" | Local Falcon, 1 scan 7×7 (reuse if one exists) | 0 or 49 credits |
| Proof (right under the map) | headline, 4 compact result cards, Martin "celebrate", one button that opens the cases and further results | `prospect-mini/case-library.json` | 0 |
| Step 1: What clients search | search volumes (questions vs. provider searches), terms without data, length of own vs. competitor pages, 6 new content items, Martin "think" | DataForSEO volumes + SERP, page measurement | about 0,10 USD |
| Step 2: Phone rings | own Google entry vs. 4 competitors (category, reviews, share of map), 6 entry changes, 4 clean-up numbers, good news, Martin "insight" | Falcon report, name searches, spam links | about 0,06 USD |
| Step 3: Homepage | today's first screen next to a draft of the first screen (zoom on tap), score today on the 22-point list, target 36+ of 44, 5-second test | Chrome screenshot, HTML draft | 0 |
| Calculator | unpaid (map and search) and Google ads separately, real volumes and real price per click | step 1 data | 0 |
| Website check (piano) | 4 strips with 2 to 5 points (Passt, Ausbaufähig, Dringend), photos from the prospect | site check | 0 |
| Quick wins, roadmap | 6 quick wins, 5 roadmap rows | derived from the findings | 0 |
| "Deine Ausgangslage auf einen Blick" | 4 fact cards, before the final CTA | Google panel, site check, scan | 0 |
| Final CTA | button and closing sentence | fixed text | 0 |

## 3. Run steps

Working folder: `00_project`. Prospect folder: `prospects/<slug>/` with `evidence/`, `draft/`, `cost_ledger.jsonl`, `prospect.json`, `_run.json`.

### Step 0: Readiness check (free, about 5 minutes)

Collect and write into `prospects/<slug>/intake.md`:

- Name, website, Google Maps link, and the Loom URL if it already exists.
- **Channel and context.** Where does the conversation with the prospect happen (LinkedIn, WhatsApp, e-mail)? What was already said? Read the existing chat if Martin points to it. The message in step 11 must continue that conversation.
- **Branch class:** health (HWG rules, protected titles), law (no success promises, professional rules), trade, or other. The class sets the limits in steps 6 and 9.
- **Country:** DE 2276, AT 2040 or CH 2756 for DataForSEO.
- **Form of address on the prospect's own site** (Sie or du). The page always uses "du" to the prospect. The homepage draft uses the prospect's own form.
- **Google profile exists?** Open the Maps link. If there is no profile, stop and use the organic variant.
- **Site reachable?** If the site blocks us, Martin switches on a German VPN or sends a screenshot. If the site is dead, search for name, service and company to check whether the prospect can be found at all.
- **Old review page?** Search `04_site/review/` for the name. If one exists, read it. Old pages can contain wrong claims (lesson 7). Plan gate G4.

### Step 1: Demand and gap keyword (paid, about 0,10 USD)

Do this BEFORE any scan. The data picks the scan keyword.

- 1 volume call: 10 to 14 terms from the branch template (section 6) plus the prospect's real services. Use only `keywords_data/google_ads/search_volume/live`, never Labs (lesson 1).
- 2 SERP calls for the 2 main services, depth 20, with the city centre or the scan centre as the coordinate. Read the map pack in the answer: is the prospect in the top 3?
- **Gap keyword rule:** the keyword names the prospect's real main service (never a neighbouring service with more volume). It has search demand, and the prospect is NOT in the map top 3 for it. If no keyword fits all three, take the real main service and say so.

All calls go through `prospect-mini/scripts/dfs.py` (ledger, cap 0,30 USD). If you see "IP not whitelisted", give Martin the IP from `curl https://api.ipify.org`.

### Step 2: Map scan (0 or 49 credits)

- Search existing reports first with `listLocalFalconScanReports` (0 credits). Reuse a scan when it is recent and its keyword fits the gap rule.
- If no usable scan exists, ask for gate G1 (keyword, city, 49 credits). Then run 1 scan 7×7. Never retry a scan, because it is queued.
- Read the report with `getLocalFalconReport` (0 credits): own entry, top competitors with categories, reviews and share of map. Save it to `evidence/`.
- Save the map image to `04_site/public/review-assets/<slug>/scan-grid.webp` and look at the image yourself. Every sentence about the map must match the picture.

### Step 3: Google panel (Chrome, free)

Open `https://www.google.com/maps/place/?q=place_id:<id>&hl=de`. Note the rating, the review count, the category, the visible owner replies and the age of the newest reviews. Falcon review counts can show 0, which means no data. The panel decides (lesson 2).

### Step 4: Name searches and links (paid, about 0,06 USD)

- 2 to 3 name searches: does the prospect's own website appear for its own name? Are there two different names in use (lesson 5)?
- `backlinks/summary/live` plus `backlinks/referring_domains/live` with the filter `["backlinks_spam_score",">=",60]`.

### Step 5: Site check (free)

- `python3 prospect-mini/scripts/collect_site.py prospects/<slug> <url>`.
- Check by hand with curl: phone links (`href="tel:`), http to https, the homepage text.
- Competitor page lengths: `python3 content-pool-skill/scripts/page_metrics.py --out prospects/<slug>/evidence/comp-pages.json --lang de <urls>` on the top 5 provider pages per service. Skip directories.

### Step 6: Homepage (free)

- Screenshot of today's first screen in Chrome at 1440 px wide. Crop the browser bar (lesson 6). Save it as `startseite-heute.webp`.
- Score today against `knowledge/cro-library/_derived/scorecard.md` (22 points).
- Build the draft of the first screen as HTML in `prospects/<slug>/draft/`, with the prospect's real logo and photo:
  - headline = service + city;
  - subline = situation + help;
  - stars, button + reassurance, and a trust row;
  - the prospect's own Sie or du.
  - Use real logos only, never placeholders, and no GPT images, because they garble text.
- Serve the draft with the launch config `prospect-drafts` (port 8975). Take a screenshot and save it as `startseite-entwurf.webp`. Save strip photos from the prospect's site as `foto-*.webp`. Open every image before you use it.
- Branch limits: health means no healing or success promise, and protected titles only if the prospect holds them. Law means no success promise.

### Step 7: Write `prospect.json`

- Copy `prospects/catja-grieshaber/prospect.json` as the model. It shows every field.
- Write all text in plain language, with no tool names and no SEO terms. Use "du" to the prospect.
- **Every number comes from `evidence/` and is listed in `sources`.** A missing volume is "Google gibt keine Zahl heraus", never "0".
- Choose the proof cases from `case-library.json` by branch and by the prospect's main gap.
- Martin guide: one text per placement (`guide.hello`, `point`, `think`, `insight`, `celebrate`). Martin speaks in first person, with at most 2 short sentences. Rules: `assets/brand/martin-guide/README.md`.

### Step 8: Headlines (standard since 2026-10-12)

Run the hero and section headlines through `00_project/prompts/direct-response-copy-prompts.md`. Each headline states a finding with a real number, not a label: outcome + benefit + time frame + proof, with no dashes. Write the picks into `prospect.json` under `headlines`. Model: `prospects/catja-grieshaber/headlines-2026-10-12.md`. The button stays "Zeig mir meinen Markt".

### Step 9: Build, validate, fact check

1. Build: `python3 prospect-mini/scripts/build_page.py prospects/<slug>` writes `04_site/review/<slug>/index.html`. Never hand-edit that file. Change `prospect.json` and rebuild.
2. Validate: `python3 prospect-mini/scripts/validate.py prospects/<slug>`. It must show 0 errors. It checks jargon, text from other prospects, missing images, empty slots, sources, "0" volumes, protected titles, and the length of the Martin guide texts. It also writes `_run.json`.
3. **Fact check with a fresh subagent.** It reads only `prospect.json`, `evidence/` and the scan image. It lists every number or claim on the page that has no source, or that the evidence does not support. Fix every item, then rebuild and validate again.

### Step 10: Visual check

Use the dev server `site-dev` (port 3000) and Claude in Chrome. Check `/review/<slug>/` at 1500 px and in a 375 px iframe:

- nothing scrolls sideways;
- the headline is bigger than the text;
- all images load;
- the gap below the fixed menu fits;
- the image zoom opens on click;
- the proof toggle opens.

Save both screenshots to `evidence/`.

### Step 11: Message draft and gate G2

Write the message for the channel from step 0. It continues the existing conversation and uses "du" in 3 to 4 sentences. It contains one real number and only the review link with `https://`, never a booking link. If the Loom URL is not there yet, write it so the link can be added later.

Send Martin the local link, the two screenshots and the draft, then wait for G2.

### Step 12: Deploy (gate G3)

1. `npm run build` in the repo root.
2. Upload only the new paths: `node 00_project/prospect-mini/scripts/upload_only.mjs review/<slug> review-assets/<slug>`. The first deploy with the Martin guide also needs `review-assets/martin-guide`.
3. Check every URL with curl: status 200 and a plausible size.
4. If an old page exists, do gate G4 now.
5. Set `_run.json` to `fertig, Freigabe offen`. The overview Excel updates itself.

### Step 13: Loom and final message

When Martin sends the Loom URL:

1. Set `loom_url` in `prospect.json`.
2. Rebuild and validate.
3. Deploy again after a short go.
4. Give Martin the final message with the link.

When Martin says the page is approved, run `workflow_registry.py approve --client "<Name>" --workflow prospect`.

## 4. Batch mode (several prospects at once)

1. Run step 0 for all prospects first. Report blockers in one list: no Google profile, site blocked, old page found.
2. Run steps 1 and 4 for all prospects. Then ask gate G1 once for all new scans.
3. Run steps 2 to 9 per prospect, in parallel with one subagent each. Each subagent writes only in its own prospect folder.
4. Show Martin one status table: prospect, gap keyword, scan new or reused, cost, validate result, fact check result, local link.
5. Ask G2 and G3 once for the whole batch. Martin can exclude single pages.

## 5. Where everything lives

```
00_project/prospects/<slug>/
  intake.md            step 0 answers (channel, branch, country, form of address, blockers)
  prospect.json        all page text and numbers, 1:1 with the page sections
  evidence/            Falcon report, DataForSEO answers, site check, screenshots, archive copies, fact check
  draft/               HTML draft of the first screen + logo/photo
  cost_ledger.jsonl    every paid call with USD
  _run.json            status for the overview Excel (written by validate.py)
00_project/prospect-mini/
  template.html        made from anja-stuerzl-v2 by scripts/make_template.py (slots + Martin guide)
  case-library.json    proof cases (facts from case studies and the proof wall only)
  branch-templates.json  volume terms and standard Google-entry changes per branch (to build, section 8)
  scripts/             collect_site.py, dfs.py, build_page.py, validate.py, make_template.py, upload_only.mjs
  NEW-CHAT-BRIEF.md    short brief for a chat that only builds review pages
  _archiv/             v1 of this document and of validate.py
04_site/review/<slug>/index.html               generated, never hand-edited
04_site/public/review-assets/<slug>/           page images
04_site/public/review-assets/martin-guide/     character poses + CSS/JS (shared)
```

## 6. Branch templates (volume terms and Google-entry changes)

Until `branch-templates.json` exists, use these rules:

- **Volume terms (10 to 14):** 3 to 4 "provider + city" terms for the real main services, 3 to 4 question terms ("was hilft bei …", "kosten …"), 2 to 3 symptom or problem terms, and 1 to 2 neighbouring-city terms. Health: no diagnosis promises in the terms that are shown.
- **Google-entry changes (6):** pick from the Maps playbook catalogue `00_project/maps-playbook-*` and `gbp-visibility-blueprint.md`. Use primary category, secondary categories, services list, description, photos, and review requests plus replies. Choose the 6 with the biggest gap in the Falcon report.

## 7. Decisions (Martin, 2026-10-12)

- Stürzl v2 is the new review-page standard.
- Plain language for non-technical readers. No "Pool", H1, SoLV, Schema, NAP or Sitemap without a translation.
- Video in the hero, a light design, and one CTA, "Zeig mir meinen Markt".
- No service videos and no "Die wichtigsten Funde" block.
- Website check as the piano element.
- Proof tailored to the prospect: 4 to 5 cases with start state and changes, plus 5 short results.
- The calculator shows unpaid and Google ads separately, with the real price per click.
- No AI-visibility line. Spam-link counter: yes.
- Homepage step is essential: today's first screen next to a draft of the first 5 seconds. The draft is HTML with the real logo and photo.
- Martin guide character: hello, point, think, insight, celebrate. Max 1 per section, about 5 per page.
- Hero: no fact cards. The map follows directly. The 4 fact cards move to "Deine Ausgangslage auf einen Blick" before the final CTA. On mobile: headline and text, then the video, then the button. The gap below the fixed menu adapts to its real height.
- Homepage images open large on click or tap.
- Proof sits right under the map: headline, 4 compact result cards, Martin "celebrate", one button that opens the detailed cases. No proof block at the bottom.

## 8. Lessons

1. DataForSEO Labs `keyword_overview` returns no volumes for health terms. Use only the Google Ads source. Many health terms still have no number: the page says "Google gibt keine Zahl heraus", never "0".
2. Reuse an existing Falcon scan when it is recent and fits. Falcon review counts can be 0 = no data; the Google panel decides.
3. Check categories and titles for legal limits: "Psychotherapeut" is a protected title, so never recommend it to a Heilpraktikerin.
4. The length comparison can go either way. Say what the data shows.
5. Name searches find real problems: two different names in use, or the own site missing for its own name.
6. Crop the browser bar from screenshots that Martin sends (it shows his extensions).
7. Old review pages can contain wrong claims. Always read the scan image again. Replace the old page (gate G4).
8. (v2) Pick the scan keyword from cheap demand and map-pack data first. A scan for the wrong keyword wastes 49 credits.
9. (v2) Upload only new paths with `upload_only.mjs`. The old `upload.js` went into a stray `public_html` folder and new folders never went live.

## 9. Open points

- Build `prospect-mini/branch-templates.json` from the rules in section 6 (health, law, trade).
- Message templates per channel (LinkedIn, WhatsApp, e-mail) with examples from the first sends.
- Follow-up after sending: when, and through which channel? Martin decides.
- Skill packaging as `/prospect-page <name>` after 3 more runs with this v2.
- The stray `/public_html` folder on the server: delete after Martin's go.

## Registry: automatic (2026-10-12)

The workflow id is `prospect`. `validate.py` writes `prospects/<slug>/_run.json`, and the registry sync reads `00_project/prospects/` after every turn. Approval stays manual (`approve --workflow prospect`).

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. On prospect pages: hello at the top, point at the map, celebrate at proof, think at open data, insight at the biggest lever. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
