# Demand: Thorsten Schmidt (agent A, 2026-10-31)

Status: DONE. Location code 2276 (Germany), language de. SERP position: Troisdorf centre, 50.8158,7.1550.
Source: DataForSEO `keywords_data/google_ads/search_volume/live` (no Labs). Evidence: `evidence/dfs-*.json`.
Cost: 0.1522 USD (ledger). Cap: 0.30 USD.

## 1. Search volumes (Google Ads, per month, Germany)

Evidence: `evidence/dfs-volumes-ads.json`. The volume is for Germany. Google does not give a city figure.

| Term | Volume | CPC (EUR) | Competition |
| --- | --- | --- | --- |
| steuerberater kosten | 5.400 | 2,93 | low |
| steuerberater bonn | 1.300 | 1,90 | low |
| steuerberater siegburg | 390 | 1,42 | low |
| steuerberater troisdorf | 320 | 1,76 | low |
| rechtsanwalt troisdorf | 210 | 6,08 | medium |
| fachanwalt steuerrecht köln | 110 | 32,28 | high |
| unternehmensnachfolge steuerberater | 50 | 3,97 | medium |
| immobiliensteuerrecht | 40 | 1,17 | high |
| rechtsanwalt steuerrecht bonn | 10 | 13,33 | medium |
| steuerberater rechtsanwalt troisdorf | Google gibt keine Zahl heraus | - | - |
| steuerberater für unternehmer troisdorf | Google gibt keine Zahl heraus | - | - |
| umstrukturierung gmbh steuerberater | Google gibt keine Zahl heraus | - | - |
| unternehmenskauf anwalt | Google gibt keine Zahl heraus | - | - |
| steuerberater und rechtsanwalt in einer person | Google gibt keine Zahl heraus | - | - |

No two terms have identical data, so no term is merged (lesson 10).
Reading: People search the plain provider term with the town ("steuerberater troisdorf", 320). The combined offer ("steuerberater rechtsanwalt", the interdisciplinary mix) and all deal-type terms (Umstrukturierung, Unternehmenskauf) have no figure. "steuerberater kosten" (5.400) is a question term without a town.

## 2. SERP: is the own site in the organic top 20?

Evidence: `evidence/dfs-serp-steuerberater-troisdorf.json`, `evidence/dfs-serp-rechtsanwalt-troisdorf.json`. Depth 20.

| Keyword | kanzlei-schmidt.online in top 20? | `item_types` | `local_pack` listed? |
| --- | --- | --- | --- |
| steuerberater troisdorf | NO (not in 20 organic results) | ai_overview, local_pack, organic | yes (listed only, no map-pack items returned) |
| rechtsanwalt troisdorf | NO (not in 20 organic results) | ai_overview, local_pack, organic, related_searches | yes (listed only, no map-pack items returned) |

No map-pack claim is made. The scan decides the map ranking. Because the prospect has no Google entry, no scan of his own entry is possible.
"rechtsanwalt steuerrecht troisdorf" was not used: the volumes show "rechtsanwalt troisdorf" (210) as the second strongest real service term, and "rechtsanwalt steuerrecht bonn" has only 10.

## 3. Gap keyword proposal

**Proposal: "steuerberater troisdorf"** — 320 searches per month, CPC 1,76 EUR, competition low. Own SERP position: not in the organic top 20.

Rule check (workflow step 1):

| Condition | Result |
| --- | --- |
| Names the real main service (Steuerberatung is the first service on his site) | PASS |
| Has search demand (320 per month) | PASS |
| Own site not in the organic top 20 | PASS |
| **Gap rule overall** | **PASS** |

Notes:
- Variant: the prospect has no Google entry (`intake.md`). The page uses the no-GBP variant (hide_grid, hide_step2). The gap keyword drives the organic story. A Local Falcon scan of his own entry is not possible.
- Grid centre, if agent D wants a market scan of competitors: Troisdorf centre. This is for the orchestrator to decide; no scan was run.
- Second choice: "rechtsanwalt troisdorf" (210, CPC 6,08). Also not in the top 20. Its SERP is mostly directories (anwalt.de, Gelbe Seiten), so it gives less comparable competitor pages.
- The interdisciplinary offer (RA + StB) has no measured demand. Do not claim demand for it.

## 4. Competitor provider URLs (no directories) for the page-length check

Only the hostname and path from the SERP breadcrumb are visible for results that Google wraps in a redirect. Full URLs were not returned for those, so the home URL is given.

"steuerberater troisdorf" (SERP rank in organic order):
- https://www.steuerkanzlei-nrw.de/ (rank 1, Steuerberatungskanzlei Krauthäuser)
- https://www.steuerberaterin-leineweber.de/ (rank 3, Steuerberaterin Rosi Leineweber)
- https://datax-gmbh.de/erstellung-von-jahresabschluessen/ (rank 6, full URL known; rank 4 is a page of the same site)
- https://www.stb-saelker.de/ (rank 10)
- https://www.schaefer-stb.de/team (rank 13, Steuerberaterkanzlei Wolfgang N. Schäfer; breadcrumb path /team)
- https://www.hess-steuerberater.de/kontakt/ (rank 18, full URL known; use the home page for page length)
- https://www.lohnsteuerhilfe-troisdorf.net/ (rank 9; Lohnsteuerhilfeverein, not a Steuerberater; use only if a 7th page is needed)

"rechtsanwalt troisdorf" (provider sites only):
- http://grey-grundhoff.de/kontakt (rank 3)
- https://www.strafverteidiger-guelpen.de/ (rank 6, Strafrecht; far from the prospect's field)
- https://www.rechtsanwalt-fritz.eu/familienrecht-troisdorf (rank 13, Familienrecht)
- https://www.rechtsanwaeltecharl.de/uebersicht (rank 15, Arbeitsrecht und Familienrecht)

Best match for the prospect's field: the six Steuerberater sites above. The law sites cover other fields (Straf-, Familien-, Arbeitsrecht).
Left out as directories or lists: dasoertliche.de, dastelefonbuch.de, gelbeseiten.de, anwalt.de, anwalt24.de, koeln.de, troisdorf.city, steuerberaterscout.de, aktuell-verein.de, facebook.com, blitzeranwalt.com.

## 5. Name searches (depth 10)

Evidence: `evidence/dfs-name-kanzlei-schmidt.json`, `evidence/dfs-name-thorsten-schmidt.json`. The second call returned task status 40101 once (0,002 USD, no data); the retry worked.

| Search | kanzlei-schmidt.online in top 10? | What ranks instead |
| --- | --- | --- |
| "kanzlei schmidt troisdorf" | NO | dasoertliche.de (Roth Klaus-Jochen Rechtsanwalt), anwalt.de, rechtecheck.de (Steuerrecht Troisdorf), steuerberaterfinden.net, meinestadt.de (Helga Schmidt Steuerberaterin, Troisdorf 53842), mapquest.com, scheidung-troisdorf.muessigundklein.de. `item_types`: ai_overview, organic, google_reviews, knowledge_graph |
| "thorsten schmidt steuerberater rechtsanwalt troisdorf" | NO | steuerberater.de and steuerberaterscout.de (Hans-Christoph Schmidt, Hennef), linklisten24.com, rocketreach.co (Torsten Schmidt), rechtecheck.de (Kanzlei Schmidt, Rüsing & Partner, Münster), meinestadt.de (Carsten Schmidt, Schenefeld). `item_types`: organic, local_pack |

Finding: the site does not appear for its own firm name or for the full name with both titles. No other web site called "Kanzlei Schmidt" ranks in Troisdorf. The results are directories and other people named Schmidt. A different firm in the same town is listed: Helga Schmidt, Steuerberaterin, Troisdorf (via meinestadt.de). No claim about a Knowledge Panel for the prospect is made.
Note: the first attempt of the "steuerberater troisdorf" SERP call ran into the client timeout and wrote no ledger line. The retry was billed once in the ledger. If DataForSEO also billed the first attempt, the true cost is at most 0,0035 USD higher.

## 6. Spam links for kanzlei-schmidt.online

Evidence: `evidence/dfs-bl-summary.json`, `evidence/dfs-bl-spam-refdomains.json`.

- Backlinks: 69. Referring domains: 52 (47 main domains). Domain rank: 0. Broken backlinks: 0.
- Summary field `backlinks_spam_score`: 52 (this value is the summary's spam score, not a count).
- **Referring domains with spam score 60 or higher: 32 of 52** (62 percent). Score range 60 to 75.
- Examples: bestnz-poker-casinoslot.com (70), betwinnermirror.com (70), m98ufa.com (75), kernelpanicpodcast.com (70), clifflisting.com (65), australianwebdirectory.shop (70).
- The spam domains link from casino, directory and unrelated blog sites. They carry no local relevance.
- Use only as a clean-up number ("32 von 52 verweisende Domains mit Spam-Score ab 60"). It is a DataForSEO score, not a Google penalty. Do not claim a ranking cause.
