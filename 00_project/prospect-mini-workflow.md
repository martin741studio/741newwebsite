# Prospect Mini Workflow v2.1 (review page for a new prospect)

Status: v2.1 of 2026-10-12. v2.1 adds the parallel agent run (section 1b) after the Fredel test run: one serial run took about 80 minutes. v2 and v1 are in `prospect-mini/_archiv/`. Owner: Martin. Runner: Claude Code in this repo.

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

Targets per prospect: 0,15 to 0,30 USD on DataForSEO, 0 or 49 Local Falcon credits, **10 minutes of wall time** (section 1c; one serial agent took about 80 minutes).

## 1. Gates (Martin decides, the agent stops and asks)

| Gate | When | What Martin approves |
| --- | --- | --- |
| G1 Scan | Only if no usable scan exists | **Standing go (Martin, 2026-10-12):** if no usable scan exists and the keyword passes the gap rule, agent D runs 1 new 7×7 scan (max 49 credits) without asking. Martin sees keyword, centre and credits in the status table. Ask only if the keyword does not pass the gap rule or more than 49 credits are needed |
| G2 Page | After step 10 | The finished page on localhost plus the screenshots, and the message draft |
| G3 Deploy | After G2 | Upload of the new paths only |
| G4 Old page | If an older review page for this prospect exists | Redirect the old page to the new one, or take it offline |

Without a "go", the agent does not upload and does not send anything (the scan has the standing go above). It sends no messages at all. Martin sends them himself.

There is no fixed question round before the run (Martin, 2026-10-12). Ask Martin only when you are blocked. Blocked includes: the grid centre is unclear (practice outside the town), the chat promised something the page cannot deliver yet (for example a video), or a generalist has no clear focus service.

## 1b. Parallel run: one agent per activity (v2.1, Martin 2026-10-12)

Martin (2026-10-12): "For each activity, an agent, so it's easily done." A serial run took about 80 minutes (Fredel test). Most steps do not depend on each other. The main chat is the **orchestrator**. It does the intake, starts the agents, asks the gates, builds and reports. The agents do the activities. The ready-to-use agent briefs are in `prospect-mini/agent-briefs.md`.

### Dependency levels

| Level | Agent | Activity (steps) | Needs before start | Writes | Chrome | Target time |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Orchestrator | Step 0 intake: website, place_id + coordinates (`find_scan.py --place`), branch, country, Sie/du, old page. Starts `run-state.json` and `browser-queue.jsonl` | Name + website | `intake.md`, `run-state.json` | no (queues jobs) | 3 min |
| 0–5 | **O Browser operator** | The ONLY agent that uses Claude in Chrome. Works the browser queue in order: Maps search (if no link), LinkedIn chat, Google panel, homepage screenshot, later the 375 px check | Jobs in `browser-queue.jsonl` | the output file named in each job | yes (the only one) | 1–2 min per job |
| 1 | **A Demand** | Steps 1 + 4: volumes, 2 service SERPs, name searches, spam links. Proposes the gap keyword and lists competitor URLs | `intake.md` | `evidence/dfs-*.json`, `demand.md` | no | 10 min |
| 1 | **B Site** | Step 5 (own site): `collect_site.py`, curl checks, price page, HWG text check, duplicate pages, contact form | `intake.md` | `evidence/site*.json`, `site-findings.md` | no | 10 min |
| 1 | **C Homepage** | Step 6: 22-point score, logo + photos, HTML draft, draft screenshot (headless), strip photos | `intake.md` + operator job `home-shot` | `draft/`, `evidence/scorecard-today.md`, `review-assets/<slug>/startseite-*.webp`, `foto-*.webp` | no (queues `home-shot`) | 10 min |
| 1 | **D Scan** | Step 2, part 1: search existing scans (0 credits) | `intake.md` (place_id) | `scan-search.md` | no (panel = operator job) | 2 min |
| G1 | Agent D | Standing go: run the scan if the keyword passes the gap rule. Ask Martin only if it does not | A (`demand.md`) + D (`scan-search.md`) | — | — | 0 min |
| 2 | **D Scan + panel** | Step 2, part 2: save location, run the scan, read the report, map image, competitor table | G1 go (or a reused scan) | `evidence/falcon-report-<key>.json`, `review-assets/<slug>/scan-grid.webp`, `competitors.md` | no | 5–10 min |
| 2 | **B Site** (2nd pass, background) | Competitor page lengths with `page_metrics.py` | A (`demand.md` competitor URLs) | `evidence/comp-pages.json` | no | 3 min |
| 3 | **E Writer** | Steps 7 + 8: `prospect.json` + headlines | All level 1 and 2 outputs | `prospect.json` | no | 20 min |
| 4 | Orchestrator | Step 9.1–9.2: build + validate (0 errors) | E | `04_site/review/<slug>/index.html`, `_run.json` | no | 2 min |
| 5 | **F Fact check** (fresh) | Step 9.3: every number against `evidence/` | Build | `evidence/fact-check.md` | no | 10 min |
| 5 | **G Visual** | Step 10: 1500 px full page (headless), reads the operator's 375 px result, looks at every section | Build + operator job `mobile-check` | `evidence/page-desktop-1500.jpg`, `evidence/visual-check.md` | no (queues `mobile-check`) | 5 min |
| 6 | Orchestrator | Fix F's findings, rebuild, validate. Step 11 message draft. Gate G2 | F + G | `message-draft.md` | no | 5 min |

**Critical path:** intake → A → D (scan, standing G1) → E → build → F. Agents B, C and O run beside it and never block it. Start O, A, B, C and D (part 1) in ONE message, right after the intake.

### Rules for all agents

1. **One activity per agent.** Each agent writes only its own files in `prospects/<slug>/` and `04_site/public/review-assets/<slug>/`. Two agents never write the same file.
2. **Handover file.** At the end, each agent writes its entry into `prospects/<slug>/run-state.json` (see below) and lists its findings in its own `.md` file. The next agent reads the files, not the chat.
3. **One browser operator (Martin, 2026-10-12).** The Chrome extension breaks when too many agents use it at the same time. So only agent O uses Claude in Chrome. Every other agent writes a job into `prospects/<slug>/browser-queue.jsonl` and continues with other work until the result file exists. Screenshots of our own pages (draft, full desktop page) use headless Chrome, not the extension. Never use the built-in browser.
4. **Paid calls only through `dfs.py`** (one ledger, one cap of 0,30 USD per prospect). Only agent A and the orchestrator make DataForSEO calls.
5. **Gates stay with the orchestrator.** No agent runs a new scan, deploys or sends a message. Agent D stops after part 1 and waits for G1.
6. **Facts, not opinions.** Every finding in an agent's `.md` file names its evidence file. Agent E uses only these findings.
7. **Cheaper model** for A, B and D (mechanical work). E and F use the main model.
8. **Long commands in the background** (for example `page_metrics.py`, which can take more than 2 minutes).

### Browser queue (`browser-queue.jsonl`)

One job per line. Agents append jobs; agent O works them in order, one at a time, in its own tab group, and closes the tabs at the end. In a batch, one operator serves all prospects (one queue file per prospect; O works them in the order of the jobs' `at` time).

```json
{"id": "panel", "slug": "ana-violeta-fredel", "type": "maps_panel", "url": "https://www.google.com/maps/place/?q=place_id:<id>&hl=de", "out": "evidence/google-panel-<date>.md", "by": "orchestrator", "at": "2026-10-12T08:56", "status": "queued"}
```

| Job type | Who queues | When | What O does | Output |
| --- | --- | --- | --- | --- |
| `maps_search` | Orchestrator | Intake, only if no Maps link | Search "<business> <city>", match website + phone | `evidence/maps-match.md` |
| `linkedin_chat` | Orchestrator | Intake | Open the profile → Message, read the thread, close it without typing | `evidence/chat-<date>.md` |
| `maps_panel` | Orchestrator | Intake | Rating, reviews, category, review ages, owner replies, "also searched" | `evidence/google-panel-<date>.md` |
| `home_shot` | Agent C (or orchestrator at intake) | Level 1 | 1440 window, decline non-essential cookies, first-screen screenshot, list image URLs | `evidence/home-today-1440.jpg`, `evidence/home-images.txt` |
| `mobile_check` | Agent G (or orchestrator after build) | Level 5 | 375×812 iframes: scrollWidth, H1 vs. text, broken images, badge under the menu, proof toggle, zoom | `evidence/page-mobile-375.jpg`, `evidence/mobile-check.md` |

O sets `status` to `running`, then `done` or `failed` (with the reason). If Chrome fails, O waits 10 seconds, opens a fresh tab and retries the job once. A failed job blocks only the step that needs it, never the whole run. The orchestrator queues all intake jobs and `home_shot` in its first message, so O starts at minute 0.

### `run-state.json` (handover)

```json
{
  "slug": "ana-violeta-fredel",
  "steps": {
    "intake":   {"agent": "orchestrator", "status": "done", "at": "2026-10-12T08:56", "outputs": ["intake.md"], "blockers": []},
    "demand":   {"agent": "A", "status": "done", "outputs": ["demand.md", "evidence/dfs-volumes-ads.json"], "blockers": []},
    "site":     {"agent": "B", "status": "running"},
    "homepage": {"agent": "C", "status": "waiting", "blockers": ["site blocks our IP: Martin VPN"]},
    "scan":     {"agent": "D", "status": "waiting_gate", "gate": "G1"}
  }
}
```

Status values: `waiting`, `running`, `waiting_gate`, `done`, `failed`. A new chat reads `run-state.json` first and continues with the first step that is not `done`.

## 1c. Target: 10 minutes per page (Martin, 2026-10-12)

The Fredel test run took about 80 minutes with one serial agent. Sections 1b (parallel agents, one browser operator, standing G1) bring one page to about 15 minutes. For 10 minutes, the slow LLM steps must become script steps. The agents then only check and write words.

### Timeline for one page (wall time)

| Minute | Orchestrator | O Browser | A Demand | B Site | C Homepage | D Scan | E Writer | F / G |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0–2 | `intake.py`: place_id, scans, old page, site, Sie/du; queues browser jobs; starts all agents | chat, panel, home shot | volumes, SERPs, names, spam | collect_site, prices, HWG text | logo, photos, `draft_home.py` | find_scan | — | — |
| 2–3 | — | home shot done | `demand.md`: gap keyword | competitor URLs → page lengths (bg) | draft screenshot (headless) | scan starts (standing G1) | `draft_prospect.py` fills numbers, tables, sources from the findings | — |
| 3–6 | — | idle | done | done | score today | scan queued at Local Falcon (about 3 min) | writes words for every section except map and competitors | — |
| 6–8 | — | — | — | — | done | report, image, `competitors.md` | adds map, competitor table, hero, guide, headlines | — |
| 8–9 | build + validate | mobile check | — | — | — | — | done | `factcheck.py` + fresh agent on the claims only; desktop shot |
| 9–10 | fixes, rebuild, message, status table | done | | | | | | done |

### What must exist for 10 minutes (proposals 27–31)

Scripts 27–30 are **built** (2026-10-12) in `prospect-mini/scripts/`. They share the evidence readers in `evidence_lib.py`. Tested on Ana Fredel and Catja Grieshaber with copies in a scratch folder; the real files were not changed.

27. **Built: `intake.py`.** Place_id and existing scans (`find_scan.py`), old review page (grep), site reachable, Sie/du count, country from the domain, writes `intake.md`, `intake.json`, `run-state.json` and the first `browser-queue.jsonl` jobs (`maps_search` only without a place, `linkedin_chat`, `maps_panel`, `home_shot`).
    - Command: `python3 prospect-mini/scripts/intake.py "<name>" <website> [maps-link] --business "<name on Google>" --city <city> --linkedin <url>`
    - Cost: a Maps link with a place_id costs 0 credits. Without it, ONE place search runs (2 Local Falcon credits per hit). `--no-place` skips it. The scan list is free.
    - Run time: 29–30 s (the free scan list pages through about 360 reports).
28. **Built: `draft_prospect.py`.** Skeleton `prospect.json` from the evidence files (Falcon report, volumes, name SERPs, spam links, `site.json`, `comp-pages.json`, panel, scorecard) and `intake.json`. Fills all numbers, the competitor table, cards, cleanup numbers, check rows, calc values on their slider steps (read from `calc()` in `build_page.py`), proof cases by branch, and the full `sources` block. Text that needs a writer gets "TODO: <hint + fact>". Also writes `evidence/draft-facts.json` (derived counts: 2/49, mean words, distances, H1 counts).
    - Command: `python3 prospect-mini/scripts/draft_prospect.py <slug>` (stops if `prospect.json` exists; use `--out <file>` or `--force`).
    - `validate.py` now fails on every "TODO" in `prospect.json`. The skeleton builds with `build_page.py`.
    - Run time: under 0,1 s. Ana check: table, shares, reviews, calc (110 / 0,7 / 250), cleanup (21 / 39, 9 Treffer, 0 / 6) match the hand-built file.
29. **Built: `factcheck.py`.** Every number must appear in an evidence or findings file (1.900 = 1900, 4,1 % = 4.08 rounded); derived counts count as evidence. Merged keyword variants (rows shown twice, numbers equal to their sum). Count claims ("Drei der vier", "2 von 49") against the derived pairs: MISMATCH when the total exists with another count. Sentences with "alle", "nur", "die meisten", "immer", "überall" go to the fresh agent. Writes `evidence/factcheck-auto.md`, exit 1 on WRONG or MISMATCH.
    - Command: `python3 prospect-mini/scripts/factcheck.py <slug> [--json <file>]`
    - The fresh agent F reads `factcheck-auto.md` first and checks only the "For the fresh agent" table plus the map image.
    - Test on the Fredel first-draft numbers: finds both known errors (220 = 110 + 110 merged variant in `demand_note` and `calc.vol`; "Drei der vier" = MISMATCH, evidence 2/4). The final Ana file: 0 WRONG, 0 MISMATCH.
    - Run time: 0,1–0,2 s.
30. **Built: `draft_home.py`.** `draft/index.html` on the Ana model: logo (margins cropped), portrait, room photo (cm4all image URLs resolved to the original file; more pages are read when the homepage has fewer than 3 photos), brand colours from the site CSS (social widget colours ignored), Sie/du and ich/wir as on the site, headline "Ihr(e) <service> in <city>", stars + review count, phone, address, trust row. Writes `draft/draft-home.json` with the choices.
    - Command: `python3 prospect-mini/scripts/draft_home.py <slug> [--service "Heilpraktikerin"] [--out <dir>] [--force]`
    - Agent C checks: right pictures, female or male form (the script uses the form the site uses; `--service` overrides), headline follows the page's main advice, no healing promise. Then the headless screenshot.
    - Run time: 16–22 s (image downloads).
31. **Batch first.** In a batch of 5, intake runs for all, then one operator, one demand agent and one scan agent serve all 5. Expected: about 20–25 minutes for 5 pages, so 4–5 minutes per page. Not built yet (a process rule, no script).

### Honest estimate

| Setup | One page | Per page in a batch of 5 |
| --- | --- | --- |
| v2 serial (Fredel test) | about 80 min | — |
| v2.1 (section 1b, no new scripts) | about 15 min | about 8 min |
| v2.1 + scripts 27–30 | about 10 min | about 4–5 min |

The fixed floor is the Local Falcon scan (about 3 minutes in the queue) plus build and checks (about 2 minutes). A reused scan saves the 3 minutes.

### Measured: first run with scripts 27–30 (Christian Rüther, `christian-ruether-v2`, 2026-10-12)

| Step | Start | End | Time |
| --- | --- | --- | --- |
| `intake.py` | 10:01:01 | 10:01:33 | 32 s |
| O operator (maps search + panel, chat, home shot) | 10:02:04 | 10:04:35 | 2,5 min |
| A Demand | 10:02:15 | 10:04:10 | 2 min |
| D Scan part 1 / scan at Local Falcon | 10:02:40 / 10:05:06 | 10:04:30 / 10:08:11 | 2 min / 3 min |
| B Site | 10:02:22 | 10:07:32 | 5 min |
| C Homepage (`draft_home.py` 9 s + 9 hand fixes) | 10:02:34 | 10:07:01 | 4,5 min |
| E Writer (`draft_prospect.py`, 93 TODOs) | 10:07:53 | 10:13:40 | 6 min |
| F Fact check ∥ G Visual | 10:14:28 | 10:19:21 | 5 min |
| Fixes, build, validate, `factcheck.py` | — | 10:20:02 | 1 min |

**Total: 19 minutes** (serial v2: about 80). Cost: 0,1577 USD, 51 credits. One Chrome user, no Chrome error.
Next steps to 10 minutes: start E right after A, D and O (do not wait for B and C; about 3 min saved); E and F are the longest blocks (fixes to the skeleton rows applied after this run); batch mode (proposal 31) for several prospects.

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
- **No Maps link?** Search Google Maps in Chrome for "<business> <city>" and the person's name. A certain match needs the same website AND the same phone number. Get the place_id with `python3 prospect-mini/scripts/find_scan.py "<business>" --place --proximity "<city>"` (it also lists existing scans). The place search costs 2 Local Falcon credits per hit. In the script test it returned 0 hits 5 times; if so, call `searchForLocalFalconBusinessLocation` through `audit-workflow/scripts/lf_client.py` with the name exactly as on Google (worked in the Fredel run).
- **Channel and context.** Where does the conversation with the prospect happen (LinkedIn, WhatsApp, e-mail)? What was already said? Always open the existing chat (LinkedIn: profile → Message, read only), even if Martin does not point to it. The chat can change the deliverable: in the Fredel run she had said yes to a video. The message in step 11 must continue that conversation.
- **Branch class:** health (HWG rules, protected titles), law (no success promises, professional rules), trade, or other. The class sets the limits in steps 6 and 9.
- **Country:** DE 2276, AT 2040 or CH 2756 for DataForSEO.
- **Form of address on the prospect's own site** (Sie or du). The page always uses "du" to the prospect. The homepage draft uses the prospect's own form.
- **Google profile exists?** Open the Maps link. If there is no profile, stop and use the organic variant.
- **Site reachable?** If the site blocks us, Martin switches on a German VPN or sends a screenshot. If the site is dead, search for name, service and company to check whether the prospect can be found at all.
- **Old review page?** Search `04_site/review/` for the name. If one exists, read it. Old pages can contain wrong claims (lesson 7). Plan gate G4.

### Step 1: Demand and gap keyword (paid, about 0,10 USD)

Do this BEFORE any scan. The data picks the scan keyword.

- 1 volume call: 10 to 14 terms from the branch template (section 6) plus the prospect's real services. Use only `keywords_data/google_ads/search_volume/live`, never Labs (lesson 1).
- 2 SERP calls for the 2 main services, depth 20, `"location_coordinate":"<lat>,<lng>"` of the town centre. The endpoint `serp/google/organic/live/regular` lists `local_pack` in `item_types` but returns no map-pack items. So the SERP shows only whether the prospect's own site is in the organic top 20. The scan decides the map top 3.
- A task status `40101` ("Internal SE Server Error") still costs money: retry once, then skip and note it.
- Two terms with identical volume, price per click and competition (e.g. "heilpraktiker merzig" and "heilpraktikerin merzig") are merged by Google. Show and count them once (lesson 10).
- **Gap keyword rule:** the keyword names the prospect's real main service (never a neighbouring service with more volume). It has search demand, and the prospect's own site is not in the organic top 20 for it (the scan then confirms the map gap). If no keyword fits all three, take the real main service and say so.
- **Grid centre:** the town that the keyword names (e.g. Merzig centre), also when the practice is outside the town. Radius 5 km for towns.

All calls go through `prospect-mini/scripts/dfs.py` (ledger, cap 0,30 USD). If you see "IP not whitelisted", give Martin the IP from `curl https://api.ipify.org`.

### Step 2: Map scan (0 or 49 credits)

- Search existing reports first with `listLocalFalconScanReports` (0 credits). Reuse a scan when it is recent and its keyword fits the gap rule.
- Search with `python3 prospect-mini/scripts/find_scan.py "<name or place_id>"`. It pages with `nextToken` (the answer field is `next_token`). `listAllLocalFalconLocations` ignores its `query` filter, so do not use it for the search.
- If no usable scan exists, run 1 scan 7×7 under the standing G1 go: first `saveLocalFalconBusinessLocationToAccount` (`{"platform":"google","placeId":"<id>"}`), then `runLocalFalconScan` (`gridSize "7"`, `radius 5`, `measurement "km"`, centre from step 1). Without the save call the scan fails. Never retry a scan, because it is queued. Add a ledger line with `"credits": 49`.
- Read the report with `getLocalFalconReport` (0 credits): own entry, top competitors with categories, reviews and share of map. Save it to `evidence/`.
- Save the map image to `04_site/public/review-assets/<slug>/scan-grid.webp` and look at the image yourself. Every sentence about the map must match the picture.

### Step 3: Google panel (Chrome, free)

Open `https://www.google.com/maps/place/?q=place_id:<id>&hl=de`. Note the rating, the review count, the category, the visible owner replies and the age of the newest reviews. Falcon review counts can show 0, which means no data. The panel decides (lesson 2). Local Falcon's `claimed` field and its business name can differ from the panel: use only what the panel shows.

### Step 4: Name searches and links (paid, about 0,06 USD)

- 2 to 3 name searches (depth 10): does the prospect's own website appear for its own name? Are there two different names in use (lesson 5)? Skip the person's name when it is not the business name.
- `backlinks/summary/live` plus `backlinks/referring_domains/live` with the filter `["backlinks_spam_score",">=",60]`.

### Step 5: Site check (free)

- `python3 prospect-mini/scripts/collect_site.py prospects/<slug> <url>`.
- Check by hand with curl: phone links (`href="tel:`), http to https, the homepage text.
- `collect_site.py` also reports duplicate pages and the form and phone links on the contact page.
- Read the prospect's price page if there is one. The prices feed the calculator (step 7).
- Health: quote sentences on the prospect's site that name serious diseases or sound like a healing promise. On the page they become one neutral "Werberecht" row, never a claim of illegality.
- Competitor page lengths: `python3 content-pool-skill/scripts/page_metrics.py --out prospects/<slug>/evidence/comp-pages.json --lang de <urls>` on the top 5 provider pages per service. Skip directories. Run it in the background: one slow site can block it for more than 2 minutes. On macOS there is no `timeout` command.

### Step 6: Homepage (free)

- Screenshot of today's first screen in Chrome at 1440 px wide. Decline non-essential cookies first. The Chrome screenshot is about 1456 px wide: crop it to 1440. Crop the browser bar (lesson 6). Save it as `startseite-heute.webp`.
- Download images with `curl -L` (site builders redirect image URLs, e.g. cm4all `uproc.php` → `/.cm4all/mediadb/<file>`). Crop empty margins from logos.
- Score today against `knowledge/cro-library/_derived/scorecard.md` (22 points).
- Build the draft of the first screen as HTML in `prospects/<slug>/draft/`, with the prospect's real logo and photo:
  - headline = service + city, and it must follow the page's own main advice (e.g. "Heilpraktikerin in Merzig");
  - subline = situation + help;
  - stars, button + reassurance, and a trust row;
  - the prospect's own Sie or du.
  - Use real logos only, never placeholders, and no GPT images, because they garble text.
- Serve the draft with the launch config `prospect-drafts` (port 8975). Take a screenshot and save it as `startseite-entwurf.webp`. Save strip photos from the prospect's site as `foto-*.webp`. Open every image before you use it.
- Branch limits: health means no healing or success promise, and protected titles only if the prospect holds them. Law means no success promise. Scorecard item 22 = 0 on the prospect's own site goes into the website check as a neutral "Werberecht" row.

### Step 7: Write `prospect.json`

- Copy `prospects/catja-grieshaber/prospect.json` as the model. It shows every field.
- Write all text in plain language, with no tool names and no SEO terms. Use "du" to the prospect.
- **Every number comes from `evidence/` and is listed in `sources`.** A missing volume is "Google gibt keine Zahl heraus", never "0".
- Choose the proof cases from `case-library.json` by branch and by the prospect's main gap.
- Calculator: `val` comes from the prospect's own price page. Every calc value must sit on its slider step (`val` a multiple of 50 from 100, `vol` 10 from 50, `cpc` 0.1). `validate.py` warns otherwise. Label budget, request and booking shares as assumptions.
- Say only what the data shows, never one step further: "top 3 only around X" is not "Google shows you only around X"; "2 of 4" is not "most".
- Martin guide: one text per placement (`guide.hello`, `point`, `think`, `insight`, `celebrate`). Martin speaks in first person, with at most 2 short sentences. Rules: `assets/brand/martin-guide/README.md`.

### Step 8: Headlines (standard since 2026-10-12)

Run the hero and section headlines through `00_project/prompts/direct-response-copy-prompts.md`. Each headline states a finding with a real number, not a label: outcome + benefit + time frame + proof, with no dashes. Write the picks into the main `prospect.json` under `headlines` (one place; a separate variant file only for A/B tests). Model: `prospects/ana-violeta-fredel/prospect.json` → `headlines`. The button stays "Zeig mir meinen Markt".

### Step 9: Build, validate, fact check

1. Build: `python3 prospect-mini/scripts/build_page.py prospects/<slug>` writes `04_site/review/<slug>/index.html`. Never hand-edit that file. Change `prospect.json` and rebuild.
2. Validate: `python3 prospect-mini/scripts/validate.py prospects/<slug>`. It must show 0 errors. It checks jargon, text from other prospects, missing images, empty slots, sources, "0" volumes, protected titles, and the length of the Martin guide texts. It also writes `_run.json`.
3. **Fact check with a fresh subagent.** It reads only `prospect.json`, `evidence/`, the scan image, `draft/index.html` and `prospect-mini/case-library.json` (for the proof claims). It lists every number or claim on the page that has no source, or that the evidence does not support. Fix every item, then rebuild and validate again.

### Step 10: Visual check

Use the dev server `site-dev` (port 3000) and Claude in Chrome. Check `/review/<slug>/` at 1500 px and in a 375 px iframe:

- nothing scrolls sideways;
- the headline is bigger than the text;
- all images load;
- the gap below the fixed menu fits;
- the image zoom opens on click;
- the proof toggle opens.

Desktop proof: a full-page screenshot with headless Chrome (`--headless=new --hide-scrollbars --virtual-time-budget=8000 --window-size=1500,13200 --screenshot=<file> <url>`). Mobile: ONLY the 375 px iframe in Claude in Chrome. Headless Chrome renders wider than 375 px and crops, so its mobile shot is invalid. The empty image in the lightbox (`.rvw-lb`) is not a broken image.

Save both screenshots to `evidence/`.

### Step 11: Message draft and gate G2

Write the message for the channel from step 0. It continues the existing conversation and uses "du" in 3 to 4 sentences. It contains one real number and only the review link with `https://`, never a booking link. If the Loom URL is not there yet, write it so the link can be added later. If the chat promised a video: message 1 sends the page now and says the video follows; message 2 sends the Loom when it is on the page (Martin's choice, 2026-10-12).

Send Martin the local link, the two screenshots and the draft, then wait for G2.

### Step 12: Deploy (gate G3)

1. `npm run build` in the repo root.
2. Upload only the new paths: `node 00_project/prospect-mini/scripts/upload_only.mjs review/<slug> review-assets/<slug>`. The first deploy with the Martin guide also needs `review-assets/martin-guide`.
3. Check every URL with curl: status 200 and a plausible size.
4. If an old page exists, do gate G4 now.
5. Set `_run.json` to `fertig, Freigabe offen`. The overview Excel updates itself.

### Step 13: Loom and final message

When Martin sends the Loom URL:

1. Set `loom_url` in `prospect.json` (embed form `https://www.loom.com/embed/<id>`).
2. **Read the transcript of the video** (Martin, 2026-10-12). Get it from the Loom share page (Claude in Chrome: Transcript tab), or transcribe the audio with whisper `small`. Save it as `evidence/loom-transcript.md`. The message must match what Martin really said in the video: the same findings, the same numbers, the same promises. If the video says something the page does not say, tell Martin.
3. Rebuild and validate.
4. Deploy again after a short go.
5. Give Martin the final message, ready to send **by WhatsApp** (plain text, short paragraphs, no bullets, no booking link, `https://` link to the review page):
   - in the prospect's language and form of address (the language of the chat; German "du" unless the chat says otherwise),
   - it delivers the promise from the chat ("wie versprochen …") and names 1–2 real findings from the video,
   - **it always ends with the email ask** (Martin, 2026-10-12): Martin wants to send the analysis by email as well and asks for the email address. German model: „Ich schicke dir die Analyse auch gern per E-Mail, dann hast du alles an einem Ort. Magst du mir deine E-Mail-Adresse geben? Das wäre super.“
   - **When the prospect gives the email address and Martin has sent the analysis by email** (Martin, 2026-10-13): add the person to the in-house newsletter list (Supabase 741-leads, table `newsletter_contacts`) with `status` = `subscribed` (Martin's decision 13.10.2026), `consent_at` = now, tags `erst-analyse` + `stadt:<city>` + `branche:<branch>`, `source` = `review-page`, and `meta` = review URL, send date, channel, `status_set_by`. First contact: Ana Fredel, 13.10.2026.
   - **Add what the video left out** (Martin, 2026-10-14): from the transcript check, take 1–2 strong page findings that Martin did not mention in the video and add them as a short block („Zwei Punkte, die im Video nicht vorkommen, aber auf der Seite stehen:“ with • bullets), only when they add value.
   - **Never say it is part of a process** (Martin, 2026-10-12): no „Das gehört bei uns zum Ablauf“, no „Workflow“, „Prozess“ or „Standard“ in the message. The ask is a personal offer, nothing more.

When Martin says the page is approved, run `workflow_registry.py approve --client "<Name>" --workflow prospect`.

### Step 14: Call booked → booking sequence (installed 2026-10-14)

When the prospect books a call from the review page or the video (Martin pastes the cal.com booking), run the skill `booking-sequence` (`.claude/skills/booking-sequence/SKILL.md`). It finds this page, makes a small fresh check (free curl + max 3 paid calls, cap 0,30 USD) for something NEW, and writes 3 German WhatsApp messages in Martin's voice: **M1 24 h before the call** (new insight + 5 % traffic example + the 39-min video), **M2 at 08:00 her time on the call day** (insight + success story from `case-library.json`), **M3 30 min before** (meeting link + "am Laptop oder PC, nicht am Handy"). Nothing goes out right after the booking (Martin 14.10.). Output: `prospects/<slug>/whatsapp-sequence.md` with a wa.me link per message, `prospects/<slug>/booking/`, one-time reminders `<slug>-whatsapp-1-24h / -2-morning / -3-30min`. Claude never sends.

## 4. Batch mode (several prospects at once)

1. Orchestrator: step 0 for all prospects first. Report blockers in one list: no Google profile, site blocked, old page found.
2. Level 1 for all prospects at the same time: agents A, B, C and D (part 1) per prospect, all started in one message. Agent A can serve all prospects in one go.
3. Ask gate G1 once for all new scans.
4. Levels 2 to 5 per prospect as in section 1b. Each agent writes only in its own prospect folder.
5. Show Martin one status table: prospect, gap keyword, scan new or reused, cost, validate result, fact check result, local link.
6. Ask G2 and G3 once for the whole batch. Martin can exclude single pages.

## 5. Where everything lives

```
00_project/prospects/<slug>/
  intake.md            step 0 answers (channel, branch, country, form of address, blockers)
  run-state.json       handover: status of each step and agent (section 1b)
  browser-queue.jsonl  browser jobs for agent O, the only Chrome user (section 1b)
  homepage.md          findings of agent C
  demand.md, site-findings.md, scan-search.md, competitors.md   findings of agents A, B, D (each with evidence file names)
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
  agent-briefs.md      ready-to-use briefs for agents A to G (section 1b)
  _archiv/             v1 and v2 of this document and of the brief, v1 of validate.py
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
10. (v2.1) Google merges close variants ("heilpraktiker merzig" / "heilpraktikerin merzig": identical volume, price per click, competition). Adding them double-counts. `validate.py` warns.
11. (v2.1) The prospect's pages can be longer than the competitors'. Then the gap is the main heading, not the length (Fredel: 652 vs. 266 words).

## 9. Open points

- Build `prospect-mini/branch-templates.json` from the rules in section 6 (health, law, trade).
- Message templates per channel (LinkedIn, WhatsApp, e-mail) with examples from the first sends.
- Follow-up after sending: when, and through which channel? Martin decides.
- Skill packaging as `/prospect-page <name>` after 3 more runs with this v2.
- The stray `/public_html` folder on the server: delete after Martin's go.
- `find_scan.py --place` returned 0 hits in tests (12.10.); check the term/proximity format before relying on it.
- Build scripts 27–30 for the 10-minute target (section 1c).

## Registry: automatic (2026-10-12)

The workflow id is `prospect`. `validate.py` writes `prospects/<slug>/_run.json`, and the registry sync reads `00_project/prospects/` after every turn. Approval stays manual (`approve --workflow prospect`).

## Martin guide (2026-10-12)

The 741 character Martin points out the one thing per section the reader must not miss. Rules, poses, markup and the inline helper: `00_project/assets/brand/martin-guide/README.md`. On prospect pages: hello at the top, point at the map, celebrate at proof, think at open data, insight at the biggest lever. Max 1 callout per section, bubble text in first person and plain language, every number with source and date, check desktop and mobile with a screenshot.
