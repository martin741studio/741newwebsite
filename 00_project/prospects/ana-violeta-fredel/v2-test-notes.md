# v2 test notes: Ana Violeta Fredel (2026-10-12)

One line per step: what worked, what was unclear or wrong, what I had to guess, time and cost.

| Step | Worked | Unclear / wrong / guessed | Time | Cost |
| --- | --- | --- | --- | --- |
| Read-in | Brief "v2 changes" block on top is good. Workflow doc is clear on order and gates. | Brief section 5 and workflow step 8 say "put headlines into prospect.json → headlines", but the model `catja-grieshaber/prospect.json` has no `headlines` key; they are only in `prospect-headlines.json` (variant file with slug `-headlines`). Unclear: main file or variant file? | 10 min | 0 |
| 0 Readiness | Site reachable (200, no block). Old page check by grep: 0 hits. Profile found by Chrome Maps search, matched by website + phone. | No Maps link given: the doc has no sub-step "find the profile yourself" and no rule for "certain match". The doc says "read the existing chat if Martin points to it"; here Martin did not point, but the chat was decisive (she said "ja gerne" to a VIDEO on 11.10.). Proposal: always open the chat in step 0. Martin's choice after asking: delivery = "page now, Loom later". | 12 min | 0 |
| 0 → G0? | I asked Martin 4 questions after step 1 (scan keyword + centre, delivery, focus service, G0). | Martin: no fixed G0; ask only when blocked. But 3 of the 4 questions were real blockers that the doc does not answer: grid centre (city vs. practice when the practice is outside town), delivery when the chat promised a video, focus service for generalists with 7+ therapies. | 3 min | 0 |
| 1 Demand | Volume call 14 terms worked in one go (0,09 USD). | "provider + city" terms for a small town: 2 of 3 had data, "naturheilpraxis merzig" none. Branch template still missing (doc section 9), so term choice is a guess. | 4 min | 0,09 |
| 1 SERP | SERP "heilpraktiker merzig" ok (organic top 20: her site not in it). | (a) `item_types` lists `local_pack`, but the items contain NO local_pack entry at depth 20, so "is the prospect in the map top 3?" cannot be read from this call. The doc assumes it can. (b) SERP "infusionstherapie merzig" failed with task 40101 "Internal SE Server Error" and still cost 0,002 USD. No retry rule in the doc. (c) The doc does not give the `location_coordinate` format; I copied it from Catja's evidence file. | 6 min | 0,0055 |
| 2 Scan search | No scan for her among 360 reports. | `listLocalFalconScanReports` pages with `nextToken` (camelCase), but the answer field is `next_token`; my first loop used the wrong name and looped on page 1. `listAllLocalFalconLocations` ignores its `query`. Proposal: a script `find_scan.py <name|place_id>` in prospect-mini/scripts. | 8 min | 0 |
| 2 Scan run (G1) | Martin's go: "heilpraktiker merzig", centre Merzig, 7×7, 5 km. | `runLocalFalconScan` fails with "location hasn't been added to your saved locations" until you call `saveLocalFalconBusinessLocationToAccount`. Not in the doc. Radius (5 km) is also not in the doc; I copied Catja's. Place ID came from `searchForLocalFalconBusinessLocation`, not from the Google panel (the panel only shows the CID). | 4 min | 49 credits |
| 3 Google panel | Chrome panel read: 5,0 / 6, ages, 0 owner replies, 5 "also searched" practices. | The place_id link format `?q=place_id:<id>` works only after you know the place_id, which came from Local Falcon, not from the panel. Local Falcon says `claimed: false`, the panel shows no claim prompt: unverifiable, so not used. Falcon name "Naturheilpraxis Ana Fredel" ≠ panel name "ana-vital Naturheilpraxis": not used as a "two names" claim, because only the panel is the truth. | 6 min | 0 |
| 4 Name + links | 3 name searches + 2 backlink calls ran first time. Real finding: "ana-vital merzig" does not show her site in the first 9 results. Spam: 21 of 39 linking domains. | Name searches need `depth` 10 only (0,002 USD each); the doc does not say a depth. "ana violeta fredel" gave only other people: useless, skip in future when the name is not the business name. | 4 min | 0,055 |
| 5 Site check | collect_site.py ran fine in the background (~2 min). | page_metrics.py on 5 competitor sites ran > 2 min (1 site timed out) and blocked the shell; run it in the background. Doc does not say that `timeout` does not exist on macOS. Lesson 4 proved true: her pages are LONGER than the competitors' (652 vs. mean 266), so the "depth" block had to be turned around (big numbers: 652 good, 0 bad). The template has no "your text is longer" variant; the bars/colours worked by setting tone. | 8 min | 0 |
| 6 Homepage | Chrome screenshot, cookie banner declined, 22-point score 5/44, HTML draft with her logo, portrait and room photo, served on 8975. | (a) cm4all images: `uproc.php/.../picture-1200` gives a 301 to `/.cm4all/mediadb/<file>`; curl without `-L` saves empty files. (b) Her logo PNG has wide empty margins: had to crop. (c) Her portrait on the site is only 198×254 px: usable only small. (d) The Chrome screenshot is 1456 px wide (window chrome), not 1440; doc says 1440. (e) Scorecard: no rule what to do when the PROSPECT's own site breaks HWG (item 22 = 0); I put it as a neutral "Werberecht" warning in the website check, not as a claim of illegality. | 15 min | 0 |
| 7 prospect.json | Copying Catja's model worked; every section filled. | (a) Calculator: slider `val` has step 50 from min 100, so 270 € showed as 250 € on the page. Nothing warns. I changed the value to a real 250 € combination. Proposal: validate.py checks calc values against slider steps. (b) case-library has no Heilpraktiker case with a "location outside town" gap; picked by branch. (c) The prices on her Kosten page made the calculator value real; the doc should say "use the prospect's own price page for `val`". | 15 min | 0 |
| 8 Headlines | Wrote hero + 12 section headlines from the findings, no dashes. | The headline file (10 variants etc.) costs time; for one run I wrote the picks directly into `prospect.json → headlines` (the doc says so), but the brief's model keeps them in a separate variant file. Decide one place. | 6 min | 0 |
| 9 Build + validate | Build ok, validate 0 errors on first run. | 2 "Sie" warnings are false positives: the template's "Sie bringen Anfragen sofort" / "Sie brauchen ein paar Monate" (plural "they"). They appear on every page; validate should ignore these template sentences. | 2 min | 0 |
| 10 Visual check | Desktop 1500: no sideways scroll, H1 56 px vs text 20 px, 5 guide callouts, proof toggle opens 4 cases, zoom opens. Mobile 375 in a Chrome iframe: order headline → text → video → button, badge free of the menu, table scrolls in its own box (same as Catja). | (a) Headless Chrome `--window-size=375,...` renders wider than 375 and crops: invalid for mobile. Use the iframe method only (doc is right, but say "never headless for mobile"). (b) A full-page desktop screenshot via headless Chrome at 1500 works well and is better proof than the viewport shot. (c) The empty `<img>` in the lightbox (`.rvw-lb`) looks like a broken image to a naive check. | 10 min | 0 |
| 11 Message | Draft continues the chat ("ja gerne" to a video). | Martin chose "page now, Loom later". The doc has no rule for the case "chat promised a video, video not yet there"; two messages now (page now, Loom later). | 3 min | 0 |

## Totals

- Agent time: about 80 minutes (doc target: 45). Extra time went to: finding the scan paging, the saved-location error, cm4all image redirects, the mobile screenshot method.
- Cost: 0,1523 USD DataForSEO (cap 0,30), 49 Local Falcon credits (G1 go by Martin).

## Change proposals (not applied; Martin decides)

### Workflow doc (`prospect-mini-workflow.md`)

1. Step 0: always open the LinkedIn/WhatsApp chat, even if Martin does not point to it. Here the chat changed the deliverable (she said yes to a VIDEO).
2. Step 0: add "no Maps link: find the profile via Chrome Maps search; a certain match = same website AND same phone".
3. Step 1: the map-pack check cannot come from `serp/google/organic/live/regular` (it lists `local_pack` in `item_types` but returns no items). Use `serp/google/organic/live/advanced` for the 2 service SERPs, or drop the "top 3" part of the gap rule before the scan and say "the scan decides".
4. Step 1: add the `location_coordinate` format (`"lat,lng"`) and a rule for SERP error 40101: retry once, then skip and note it.
5. Step 1/2: add a rule for the grid centre when the practice is outside the town: centre on the town the keyword names (Martin's choice here).
6. Step 2: write the 3 Local Falcon calls in order: `searchForLocalFalconBusinessLocation` (place_id) → `saveLocalFalconBusinessLocationToAccount` → `runLocalFalconScan` (radius 5 km for towns). Without the save call the scan fails.
7. Step 5: "run page_metrics.py in the background; 1 slow site can block it for > 2 min".
8. Step 6: "Chrome screenshot width is about 1456 px; crop to 1440". "cm4all sites: image URLs redirect to `/.cm4all/mediadb/<file>`, use `curl -L`".
9. Step 6/9: rule for a prospect whose own site breaks HWG: mention it neutrally as "Werberecht" in the website check, never as "illegal".
10. Step 7: "`calc.val` comes from the prospect's price page; it must be a multiple of 50 from 100".
11. Step 10: "mobile only via the 375 px iframe in Chrome; headless Chrome cannot render 375 px". Full-page desktop proof via headless Chrome is fine.
12. Step 11: add the case "the chat promised a video": two messages (page now, Loom later) or one message after the Loom.
13. Section 1 (gates): Martin decided "no fixed G0, ask only when blocked". Add one line: "blocked" includes grid centre, delivery form when the chat promised something, and focus service for generalists.

### Brief (`NEW-CHAT-BRIEF.md`)

14. Section 5 says headlines go into `prospect.json → headlines`, but the Catja model keeps them in `prospect-headlines.json`. Pick one (proposal: main `prospect.json`; the variant file only for A/B tests).
15. Add the three Local Falcon calls (proposal 6) to section 4 step 1.

### Scripts

16. New `prospect-mini/scripts/find_scan.py <name|place_id>`: pages `listLocalFalconScanReports` with `nextToken` (the answer field is `next_token`) and prints matching scans. `listAllLocalFalconLocations` ignores its `query` filter.
17. `validate.py`: ignore the two template sentences "Sie bringen Anfragen sofort" and "Sie brauchen ein paar Monate" in the "Sie" check (false positive on every page).
18. `validate.py`: warn when a calc value is not on its slider step (val, vol, budget, cpc).
19. `validate.py` or `dfs.py`: flag SERP tasks with `task_status != 20000` (they still cost money and leave an empty evidence file).
20. `collect_site.py`: also report duplicate pages (same title + same word count, here `/` and `/ana-vital/`) and whether `/Kontakt/` has a form (today it checks only the homepage, which led to a false "no form" risk).

### Parallel agents (Martin's request 12.10., during the run)

21. Split the run by dependency level. 0 Intake (orchestrator: website, place_id + coordinates, chat, branch, Sie/du, old page) → 1 three agents in parallel: A Demand (volumes, 2 SERPs, name searches, spam links), B Site (collect_site, curl checks, price page, HWG text), C Homepage (screenshot, score, images, draft) → G1 (needs only A) → 2 Scan + panel + competitor table (+ competitor page lengths in the background) → 3 Writer (prospect.json + headlines) → 4 Build + validate → 5 Fact check ∥ visual check → 6 Message + G2. Critical path: intake → A → G1 → scan → writer → build → fact check. Expected wall time about 40–45 min instead of about 80.
22. Handover file `prospects/<slug>/run-state.json`: one entry per step (status, output files, blockers). Each agent writes its line when it finishes; any agent or a new chat continues from the last finished step.
23. Chrome is shared: give each parallel agent its own tab, or run the Chrome steps (panel, chat, homepage screenshot, visual check) one after the other.
24. G1 is the biggest wait. Option for Martin: a standing rule "no scan exists + keyword passes the gap rule → run it (max 49 credits)"; Martin then sees the keyword only in the status table.

Note 12.10.: Martin approved during the run to write the parallel-agent setup into the workflow ("get that written down also in the workflow"). Done: workflow v2.1 section 1b + batch mode, `prospect-mini/agent-briefs.md`, brief v2.1 block. v2 copies in `prospect-mini/_archiv/`. Proposals 1–20 are still NOT applied.

| 9.3 Fact check | Fresh agent checked 116 claims in ~7 min, found 22 "must fix" items: 0 HWG issues, map image matches the data. All 22 fixed, rebuilt, validate 0 errors; short re-check by a 2nd fresh agent. | The fact check was the most valuable step of the run. Biggest catches: (1) "heilpraktiker merzig" + "heilpraktikerin merzig" have identical volume/CPC/competition = Google merges them, so adding them counts twice (proposal 25: dfs.py or validate flags identical rows); (2) claims that went one step further than the data ("Google zeigt dich fast nur in Silwingen", "Praxen vor dir sind als Heilpraktiker eingeordnet"); (3) our own draft headline did not follow our own main advice. The fact checker cannot see `case-library.json` by design, so proof claims always come back "unsupported": allow it to read the library (proposal 26). | 15 min | 0 |

## Decisions after the run (Martin, 12.10.2026)

- G2 + G3 go: page deployed, 7 URLs 200 (https://741.studio/review/ana-violeta-fredel/). Loom still open.
- All 26 proposals approved. Applied: workflow v2.1 (sections 1, 1b, steps 0–11, lessons 10–11), brief, agent briefs; scripts 16–20 + 25 by a background agent.
- New: standing G1 go (proposal 24), ONE browser operator with a job queue (Martin: the Chrome extension breaks with many agents), target 10 minutes per page (workflow section 1c, proposals 27–31: intake.py, draft_prospect.py, factcheck.py, draft_home.py, batch first). 27–30 are not built yet.
