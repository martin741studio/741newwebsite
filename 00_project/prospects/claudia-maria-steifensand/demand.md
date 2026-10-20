# Demand: Bestattungsinstitut Pinkert und Partner, Riesa (agent A, 2026-10-13)

Source for all numbers: DataForSEO, Germany (2276), language de. Cost total: 0,1501 USD (cap 0,30). See `cost_ledger.jsonl`.
Site menu (curl): Home, Unser Haus, Leistungen, Kontakt. Services on /leistungen/: Erd-, Feuer-, Wald- und Seebestattung, Überführungen, Trauerfeier, Aufbahrung, Träger, Rednerin, Drucksachen, Blumenschmuck, Zeitungsanzeigen, Bestattungsvorsorge-Verträge, Behördengänge.

## 1. Volumes (Google Ads, monthly searches, Germany)
Evidence: `evidence/dfs-volumes-ads.json`

| Keyword | Searches/month | CPC EUR | Note |
|---|---|---|---|
| bestatter riesa | Google gibt keine Zahl heraus | | |
| bestattung riesa | Google gibt keine Zahl heraus | | |
| bestattungshaus riesa | Google gibt keine Zahl heraus | | |
| bestattungsinstitut riesa | 20 | 10,27 | only town term with a number |
| bestatter großenhain | Google gibt keine Zahl heraus | | |
| bestatter strehla | Google gibt keine Zahl heraus | | |
| bestatter oschatz | 50 | 1,35 | neighbour town, 25 km; she is not located there |
| seebestattung | 6.600 | 3,13 | no town |
| baumbestattung | 3.600 | 2,57 | no town; not on her menu (she lists Waldbestattung) |
| waldbestattung | 1.900 | 2,34 | no town; on her menu |
| urnenbestattung | 1.000 | 3,65 | no town |
| bestattungsvorsorge | 2.400 | 3,19 | no town |
| bestattung kosten | 1.900 | 2,32 | no town |
| was kostet eine beerdigung | 4.400 | 1,94 | no town |

Merged variants: "bestatter / bestattung / bestattungshaus / bestattungsinstitut riesa" count as one search intent. Google gives a number only for "bestattungsinstitut riesa" (20). The merged town demand is therefore 20 or more. It is not proven to be 30 or more.
Observation: Google shows 106 results for "bestatter riesa" and 131 for "bestattungsinstitut riesa" (`se_results_count` in the SERP files). The town demand is small. The service terms without a town have large demand but are not local.

## 2. Organic position of her site (depth 20, coordinate 51.3006768,13.3123417)
Evidence: `evidence/dfs-serp-1.json`, `evidence/dfs-serp-2.json`

- "bestatter riesa": her home page is organic position 5 (absolute 9) of 20.
- "bestattungsinstitut riesa": her page /unser-haus/ is organic position 12 (absolute 17). The home page is not listed.
- Both main terms: she is in the top 20. Neither is a gap keyword.
- The endpoint lists `local_pack` in `item_types` but returns no map-pack items. No map-pack position is claimed. The scan decides.

## 3. Gap keyword proposal
Rule: real main service + town, at least 30 searches per month, her site not in the organic top 20.
Result: NO keyword passes the rule with the data in this run.
- "bestatter riesa" and "bestattungsinstitut riesa": she ranks in the top 20 (section 2). Demand is also below 30 or has no number.
- "bestatter oschatz" (50): demand is above 30. But she is not located in Oschatz, so it is not her main service area. Her organic position there was not checked (no SERP call, budget).
- Service terms with demand ("seebestattung", "waldbestattung", "urnenbestattung", "bestattungsvorsorge") have no town in this run. They fail the "WITH the town" rule.
Proposal for the orchestrator (decision for Martin/G1): one more volume call with town + service terms, for example "seebestattung riesa", "feuerbestattung riesa", "urnenbestattung riesa", "waldbestattung riesa", "bestattungsvorsorge riesa", "beerdigung riesa", "trauerfeier riesa", "bestatter meißen". Cost about 0,09 USD. Total would be about 0,24 USD, still under the cap 0,30. I did not run it because the order said one volume call and about 0,15 USD budget.
Until then, the best scan keyword is the main term itself: "bestatter riesa" (she is only rank 5 organic, the map position is unknown). The G1 gap rule does not pass.

## 4. Competitor provider URLs (no directories) for the page-length check
Evidence: `evidence/dfs-serp-1.json`, `evidence/dfs-serp-2.json`, `evidence/dfs-serp-name2.json`
1. https://trauerhilfe-wuensche.de/bestattungen-riesa/ (rank 1 for "bestatter riesa")
2. https://www.bestattungshaus-fritsche.de/ (rank 2)
3. https://riesa.krematorium-meissen.de/agentur-riesa.html (rank 3, Städtisches Bestattungswesen Meißen, agency Riesa)
4. https://www.bestatter-riesa.de/ (3 URLs in "bestatter riesa", 7 URLs in "bestattungsinstitut riesa", ranks 1 and 2 there)
5. https://www.bestatter-riesa.de/bestattungsarten/tree-of-life-baumbestattung (rank 2 for "bestattungsinstitut riesa")
Not providers, excluded: kirche-riesa.de (church), friedhofsverwaltung, krematorium-meissen.de/friedhöfe pages, bestattungen.de, gelbeseiten.de, dasoertliche.de, dastelefonbuch.de, trustlocal.de, bestattungsatlas.de, sellwerk.de, mapquest.com, 11880.com, bestatter-in-deutschland.de, seniorenportal.de, firmenabc.com (all directories or portals).
Possible clone or spam site: https://bestatterriesa.ac.gd/ (rank 15, "Bestatter Riesa"). Not a competitor for the length check.

## 5. Name searches (depth 10)
Evidence: `evidence/dfs-serp-name.json`, `evidence/dfs-serp-name2.json`
- "pinkert und partner riesa": her own site is rank 1 (home page). Then Gelbe Seiten (listing in 01594 Riesa-Oelsitz), bestattungsatlas.de, dastelefonbuch.de, a Facebook post of the web agency CTH, mapquest.com, 11880.com, sellwerk.de. No review or competitor site in the top 8.
- "bestattung pinkert": her own site is NOT in the top 10. Competitors fill the page: trauerhilfe-wuensche.de, bestatter-riesa.de (3 URLs), krematorium-meissen.de, bonitz-pech.de, bestattungshaus-fritsche.de, and others. Only dasoertliche.de "Pinkert in Oelsitz Stadt Riesa" is related to her. Someone who types the short brand name does not find her site.
- Second location: the directory entries show "Riesaer Str. 40, 01594 Riesa-Oelsitz" (Gelbe Seiten, Das Örtliche, dastelefonbuch, seniorenportal). The intake lists a Google profile at Goethestraße 1, 01589 Riesa and a second one in Oelsitz. The name searches confirm that both addresses are in use. The operator job maps_panel must confirm which one is the main site.
- Also seen: the Bestatterinnung Sachsen lists her (bestatterinnung-sachsen.de member page, rank 5 for "bestattungsinstitut riesa"). This is a trust signal for the page.

## 6. Spam links
Evidence: `evidence/dfs-backlinks-summary.json`, `evidence/dfs-refdomains-spam.json`
- Summary: 142 backlinks, 68 referring domains (66 main domains), 20 nofollow domains, 0 broken backlinks, domain rank 114. Average backlink spam score 21. Target spam score 1.
- Referring domains with spam score 60 or higher: 30 of 68 (44 %).
- All 30 have rank 0. Examples: onlyhealthydeals.com (70), bestwebs123.site (75), betwinnermirror.com (70), ufabettererm4.com (70), bestnz-poker-casinoslot.com (70), topbilliondirectory.com (75).
- 28 of the 30 first appeared between 2026-08-03 and 2026-10-12. Two date from 2025-07-30. The recent wave is a pattern of link spam (casino, betting, fake news sites).
- The `refdomains-spam` call returned all 30 on one page (limit 100), so the count is complete.

## 7. Blockers and notes
- No 40101 status. No retry needed. All 6 calls returned 20000.
- Open: gap keyword (section 3).
