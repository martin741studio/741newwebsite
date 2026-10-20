# Demand: Manuela Stetter (agent A, 2026-10-14)

Evidence files are in `evidence/`. Volumes are Google Ads monthly searches, Germany (2276), language de. Cost: 0,1498 USD (cap 0,30).

## 1. Her real services (site menu, `/leistungen/`, `/naturheilkunde/`, `/coaching/`)
Frauenheilkunde and Hormone, Menstruationsbeschwerden, PMS, Wechseljahre, Kinderwunsch, Endometriose, PCO, Hormonspeicheltest, Ernährungsberatung, Coaching, Kurse.

## 2. Volume table (evidence: `dfs-volumes-ads.json`)
| Term | Searches per month |
|---|---|
| heilpraktiker landshut | 320 |
| heilpraktikerin landshut | 320 |
| naturheilpraxis landshut | 10 |
| heilpraktiker essenbach | 20 |
| heilpraktiker dingolfing | 70 |
| kinderwunsch heilpraktiker | 480 |
| hormonspeicheltest | 210 |
| hormonspeicheltest kosten | 40 |
| heilpraktiker kosten | 880 |
| menstruationsbeschwerden naturheilkunde | 10 |
| pms naturheilkunde | 20 |
| frauenheilkunde naturheilkunde | Google gibt keine Zahl heraus |
| wechseljahre heilpraktiker landshut | Google gibt keine Zahl heraus |
| hormone heilpraktiker landshut | Google gibt keine Zahl heraus |

Merged variants (never add up): "heilpraktiker landshut" and "heilpraktikerin landshut" are one demand. Google shows 320 for each. Count it as 320, not 640. The two SERPs share 7 unique URLs (18 and 20 unique organic URLs) (`dfs-serp-1.json`, `dfs-serp-2.json`).
No women's-health term with a town has a number. This is a data limit, not proof of zero demand.

## 3. Gap keyword
**heilpraktikerin landshut: 320 searches per month (merged with "heilpraktiker landshut").**
- Town in keyword: Landshut. Scan centre = Landshut centre (48.5372, 12.1522).
- Her site is not in the organic top 20 for "heilpraktikerin landshut" (`dfs-serp-2.json`, 20 organic hits) and not for "heilpraktiker landshut" (`dfs-serp-1.json`).
- Caveat 1: this is the provider term, not her women's-health focus. No women's-health term with a town reaches 30 searches (see table).
- Caveat 2: Essenbach is about 12 km from the Landshut centre. A 7x7 grid with radius 5 km around Landshut will probably not cover her practice. Orchestrator and agent D must decide: radius, or a second scan.
- Other options: "kinderwunsch heilpraktiker" 480 (no town, no SERP checked). "heilpraktiker dingolfing" 70 (town, SERP not checked, no paid call made).

## 4. Competitor provider URLs (no directories), from `dfs-serp-1.json` and `dfs-serp-2.json`
- https://heilpraktikerin-silviahensel.de/ (Altdorf bei Landshut, TCM)
- https://www.praxis-funktionsmedizin.de/
- https://naturheilpraxis-eigl.de/therapien-fuer-kinder/
- https://www.heilpraxis-muehleninsel.de/leistungen/
- https://www.heilpraxis-muehleninsel.de/diagnostik/
- https://www.naturheilpraxis-andrea-stig.de/
- https://www.heilpraktiker-bieringer.de/ueber-mich/
- https://www.maluweber.de/
- https://eike-seibert.de/akupunktur-und-coaching-in-landshut/
- https://natuerlichgsund.de/therapie-angebot.html
- https://www.knau-coaching-therapie.de/

Excluded: jameda, doctolib, doctify, doctena, theralupa, aerzte.de, dastelefonbuch, pflegesuche, osteopathie.de, erleben.landshut.de, branchen-info.net, silvamed.de (clinic group).
Page-length check candidates for agent B: the first 6 URLs.

## 5. Name searches (Landshut coordinates, depth 10)
- "manuela stetter heilpraktikerin" (`dfs-serp-name.json`): her site is #1. Jameda is #2, Theralupa #3, GoLocal #4, werkenntdenbesten #5, ablefy #6, 11880 #7. SERP shows knowledge_graph, google_reviews and third_party_reviews.
- "naturheilpraxis stetter" (`dfs-serp-name2.json`): her blog `/blog/` is #2 (rank_absolute 3). First hit is an unrelated Osteopathie page. Facebook page is #7. SERP shows knowledge_graph and google_reviews.
- Finding: she is easy to find by name. She is not found by town and service.

## 6. Spam links (evidence: `dfs-backlinks-summary.json`, `dfs-refdomains-spam.json`)
- Summary: 67 backlinks, 39 referring domains (38 main domains), 13 nofollow domains, domain rank 127, profile spam score 41.
- **Spam: 20 of 39 linking domains have a backlink spam score of 60 or more.** Each has 1 or 2 links.
- Examples: bestnz-poker-casinoslot.com (70), betwinnermirror.com (70), m98ufa.com (75), kernelpanicpodcast.com (70).

## 7. Blockers
None. No 40101 status. Cost split: volumes 0,09 USD, 4 SERPs 0,0110 USD, backlinks 0,0488 USD.
