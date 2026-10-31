# Demand: Claudia Breuer (agent A, 2026-10-31)

Cost: 0.1491 USD (cap 0.30). Evidence: `cost_ledger.jsonl`. All files are in `evidence/`.
Note: the first two calls (2026-10-31 15:03) failed with task status 40207 (IP not whitelisted). They cost 0 USD. After Martin whitelisted the IP, all calls worked.
Location: Germany (2276), language de. SERP centre: 50.6958612,7.1589297 (Bad Godesberg).

## 1. Search volume (Google Ads, per month, Germany)

Source: `evidence/dfs-volumes-ads.json` (endpoint keywords_data/google_ads/search_volume/live, 0.09 USD). Google Ads does not report local volume below city level.

| Term | Volume | CPC (EUR) | Competition |
| --- | --- | --- | --- |
| psychotherapie bonn | 2900 | 3.03 | MEDIUM (44) |
| paartherapie bonn | 880 | 1.95 | MEDIUM (36) |
| heilpraktiker psychotherapie kosten | 590 | 3.06 | HIGH (71) |
| psychotherapie kosten selbstzahler | 390 | 1.98 | LOW (31) |
| lebensberatung bonn | 30 | 1.42 | MEDIUM (34) |
| heilpraktiker psychotherapie bonn | Google gibt keine Zahl heraus | - | - |
| heilpraktikerin psychotherapie bonn | Google gibt keine Zahl heraus | - | - |
| psychotherapeut bonn | Google gibt keine Zahl heraus | - | - |
| psychotherapie bad godesberg | Google gibt keine Zahl heraus | - | - |
| angst therapie bonn | Google gibt keine Zahl heraus | - | - |
| burnout therapie bonn | Google gibt keine Zahl heraus | - | - |
| psychotherapie ohne wartezeit bonn | Google gibt keine Zahl heraus | - | - |
| psychotherapie siegburg | Google gibt keine Zahl heraus | - | - |
| psychotherapie königswinter | Google gibt keine Zahl heraus | - | - |

- 9 of 14 terms have no number. This does not mean zero searches. It means Google gives no figure.
- "heilpraktiker psychotherapie bonn" and "heilpraktikerin psychotherapie bonn" both have no number, so no merge case.
- The two cost terms are not local (no town in the term). They show interest in self-pay therapy in general.
- I replaced "trauerbegleitung bonn" and "gesprächstherapie bonn" with "angst therapie bonn" and "burnout therapie bonn". Her site offers Stress, Erschöpfung, Ängste, Lebenskrisen (page /behandlungsfelder). It does not offer the first two.

## 2. Own site in the organic top 20?

Source: `evidence/dfs-serp-hp-psychotherapie-bonn.json` and `evidence/dfs-serp-psychotherapie-bonn.json` (depth 20, 0.0035 USD each). The endpoint lists `local_pack` in item_types but returns no map-pack items. This file makes no map-pack claim. The scan decides.

| Search | Own site breuer-psychotherapie.de in organic top 20? |
| --- | --- |
| psychotherapie bonn | No. The domain does not appear in positions 1 to 20. |
| heilpraktiker psychotherapie bonn | No. The domain does not appear in positions 1 to 20. |

Positions 1 to 5 for "psychotherapie bonn": valeara.de, privatpraxis-psychotherapie-bonn.de, therapie.de, psychotherapie-schlottner.de, therapie-schumacher.de.
Positions 1 to 5 for "heilpraktiker psychotherapie bonn": deutsche-heilpraktikerschule.de, doctolib.de, praxis-august-renner.de, psychotherapie-sprick.de, zurueck-in-dein-leben.de.

## 3. Gap keyword proposal

**Proposal: "psychotherapie bonn"** - volume 2900 per month, CPC 3.03 EUR, own site not in the organic top 20 (SERP position: none in top 20).
Grid centre: Bonn centre (the keyword names Bonn). The practice is in Bad Godesberg, which is part of Bonn. Radius 5 km.

Gap rule check:
1. Names her real main service: PASS. She is Heilpraktikerin für Psychotherapie. The home page says she works "im Bereich Psychotherapie" (source: https://www.breuer-psychotherapie.de/). "Psychotherapie" is her service. "paartherapie bonn" (880) is not chosen: it is a neighbouring service (she sells "Paargespräch" at 120 EUR, not "Paartherapie").
2. Has search demand: PASS. 2900 per month (`evidence/dfs-volumes-ads.json`).
3. Own site not in the organic top 20: PASS (`evidence/dfs-serp-psychotherapie-bonn.json`).

**The gap rule PASSES for "psychotherapie bonn".**

Caveat for the writer: the more exact term "heilpraktiker psychotherapie bonn" also has no own-site position in the top 20, but Google gives no volume for it. It fails rule 2 on data. Most results for "psychotherapie bonn" are Kassen-psychotherapists and clinics. A Heilpraktikerin competes for the same words but with a different offer (no Kassenleistung, short waits). The HWG rule applies: no protected title ("Psychotherapeutin" is protected for approved psychotherapists). Do not write that she is a "Psychotherapeutin".

## 4. Competitor provider URLs for the page-length check (no directories, no schools)

Source: breadcrumb field in the two SERP files. Google rewrote some organic URLs to google.com/goto links. The real domain is in `breadcrumb`.

From "psychotherapie bonn" (`evidence/dfs-serp-psychotherapie-bonn.json`):
- https://www.privatpraxis-psychotherapie-bonn.de/therapeuten/ (position 2)
- http://psychotherapie-schlottner.de (position 4)
- https://therapie-schumacher.de (position 5)
- https://www.psychotherapie-gippert.de (position 6)
- https://www.raasch-psychotherapie.de (position 8)
- https://www.pmp-schoepf.de (position 9)

From "heilpraktiker psychotherapie bonn" (`evidence/dfs-serp-hp-psychotherapie-bonn.json`):
- https://praxis-august-renner.de/ (position 3)
- https://www.psychotherapie-sprick.de/ (position 4)
- https://www.zurueck-in-dein-leben.de (position 5)
- https://www.heilpraktiker-bonn.de (position 6)
- https://www.karinstuehn.de (position 8)
- https://www.psychotherapie-zaehr.de (position 10)

Left out: valeara.de (clinic), doctolib.de, therapie.de, gelbeseiten.de, jameda.de (directories), deutsche-heilpraktikerschule.de, holler-heilpraktikerschule.de, therapie-ausbildungen.de (schools).

## 5. Name searches

Source: `evidence/dfs-name-breuer-psychotherapie-bonn.json` and `evidence/dfs-name-claudia-breuer-hp.json` (depth 10, 0.002 USD each).

- "breuer psychotherapie bonn": her own domain breuer-psychotherapie.de is NOT in the 9 organic results. Results are other practices (praxis-bonn.com), directories (therapie.de, arzt-auskunft.de, doctena.de) and a person "Babette Breuer" (doctena) and "Nora Breuer" (Köln).
- "Claudia Breuer Heilpraktikerin für Psychotherapie": her own domain is NOT in the 8 organic results. Results are other people with similar names (Karla Breuer, Claudia Kerp, Klara Breuer, Claudia Bräuer) on doctolib.de, arzt-auskunft.de, jameda.de and facebook.com.
- Finding: someone who searches her brand name or her full name does not find her site on page 1. The result is mixed with other Breuer therapists. (Search done with the Bad Godesberg location. Results can differ by user.)

## 6. Spam links

Source: `evidence/dfs-bl-summary.json` (0.024 USD) and `evidence/dfs-bl-refdomains-spam.json` (filter backlinks_spam_score >= 60, 0.024 USD).

- Target www.breuer-psychotherapie.de: 52 backlinks from 18 referring domains. Domain spam score in the summary: 2.
- Referring domains with backlinks_spam_score >= 60: **0 of 18**.
- Finding: no spam-link problem. The page should not claim one. The spam counter shows 0 of 18.
