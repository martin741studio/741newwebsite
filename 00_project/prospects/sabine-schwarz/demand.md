# Demand: Sabine Schwarz (agent A, 2026-10-12)

Title rule: she is "Heilpraktikerin für Psychotherapie" (HPG). Never write "Psychotherapeutin".
Evidence folder: `prospects/sabine-schwarz/evidence/`. Cost: 0.1504 USD (cap 0.30), see `cost_ledger.jsonl`.
Her real menu (curl of the homepage, 2026-10-12): Psychotherapie (HPG) `praxis.html`, Online-Paartherapie `Paar.html`, Coaching / Beratung `online.html`, Alternativmedizin / Energiearbeit (Reiki) `besuch.html`, Seminare, Preise. The page `praxis.html` lists the training "Mobbing-Beratung", "EMDR - Traumatherapie", "Burnout-Beratung". The homepage keywords meta lists "Mobbing Beratung".

## 1. Search volume (Germany, location_code 2276, Google Ads)

Evidence: `evidence/dfs-volumes-ads.json`. Numbers are per month, latest value. Series = last 12 months, oldest first.

| Term | Volume | CPC (EUR) | 12-month series |
|---|---|---|---|
| paartherapie kosten | 1900 | 1.77 | 1600, 1900, 1600, 1900, 1900, 1900, 1900, 2400, 1900, 1900, 1900, 1900 |
| mobbing am arbeitsplatz was tun | 1300 | 1.02 | 880, 880, 1000, 1000, 1000, 1600, 1300, 1300, 1000, 1600, 1300, 1300 |
| heilpraktiker coburg | 260 | 1.92 | 140, 210, 170, 210, 210, 480, 260, 260, 210, 260, 260, 260 |
| paartherapie coburg | 110 | 1.96 | 90, 90, 90, 90, 90, 140, 90, 140, 90, 110, 110, 70 |
| mobbing beratung | 110 | no CPC | 30, 90, 110, 90, 90, 110, 170, 90, 90, 140, 140, 140 |
| reiki coburg | 10 | no CPC | 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 10 |
| heilpraktiker psychotherapie coburg | Google gibt keine Zahl heraus | | |
| heilpraktikerin psychotherapie coburg | Google gibt keine Zahl heraus | | |
| psychotherapie coburg | Google gibt keine Zahl heraus | | |
| mobbing coburg | Google gibt keine Zahl heraus | | |
| traumatherapie coburg | Google gibt keine Zahl heraus | | |
| emdr coburg | Google gibt keine Zahl heraus | | |
| burnout beratung coburg | Google gibt keine Zahl heraus | | |
| psychologische beratung coburg | Google gibt keine Zahl heraus | | |

Merged variants: none. No two terms share the same volume, CPC and monthly series, so nothing is merged and nothing is added up. (The eight terms without a number have no series to compare.)
"Google gibt keine Zahl heraus" means: no demand claim for these terms. Do not write "0 searches".

## 2. Gap keyword (proposal)

**paartherapie coburg, 110 searches per month** (evidence: `dfs-volumes-ads.json`).
- Real main service: yes. She has the page `Paar.html` ("Online-Paartherapie / Beziehungsberatung", H1 "Online-Paarberatung & Paartherapie").
- Has demand: yes, 110 per month, CPC 1.96 EUR, competition MEDIUM.
- Her site is not in the organic top 20: `evidence/dfs-serp-1.json` (query "paartherapie coburg", Coburg centre 50.2586,10.9640, depth 20) lists 20 organic results (absolute positions 8 to 31). `therapie-sasch.com` is not among them. One Instagram post at organic rank 15 (absolute 26) only mentions her web address in its text.
- Scan centre: Coburg (the town the keyword names).
- Check for agent D: her Google profile address is Krebsmühle 5, 96482 Ahorn-Schorkendorf (`intake.md`). Her homepage also lists a second place, Zinkenwehr 5, 96450 Coburg (Studio FRIEDA). The scan can show her far from the Coburg centre. Agent D decides with `google-panel` data.
- The SERP shows 8 paid ads (absolute positions 4 to 7, 19 to 20, 32 to 34, e.g. annaholfeld.de, trustlocal.de, betterhelp.com). Paid competition is present.

Second query: "psychotherapie coburg" (`evidence/dfs-serp-2.json`, depth 20). Her site is not in the top 20 here either, but Google gives no volume number for this term. It is not a demand claim. The results are nearly all directories (jameda, therapie.de, arzt-auskunft).

Other terms with real demand, for the writer: "paartherapie kosten" 1900 (national, matches her Preise section on `Paar.html`), "mobbing am arbeitsplatz was tun" 1300 (national, matches "Mobbing-Beratung"), "heilpraktiker coburg" 260. These terms carry no town in the first two cases. Do not use them as the map-scan keyword.

## 3. Competitor provider URLs for the page-length check (no directories)

Source: `evidence/dfs-serp-1.json`, query "paartherapie coburg".
1. https://praxis-bernklau.de/paartherapie/ (organic 8, absolute 16)
2. https://praxisnoranebel.de/paartherapie/ (organic 11, absolute 22)
3. http://www.eheberatung-coburg.de/eheberatung-ehetherapie.html (organic 4, absolute 12)
4. https://coburg-psychotherapie.de/ (organic 2, absolute 9)
5. https://www.psychotherapie-nuechterlein.de/ (organic 10, absolute 18, homepage, not a Paar page)

Skipped as directories or platforms: therapie.de, doctolib.de, dasoertliche.de, instagram.com. Also skipped: loesungsraum-coburg.de (the ranking pages are "Konditionen" and a "Kontakt" page, not a service page).

## 4. Name searches (Coburg centre, depth 10)

- "therapie sasch" (`evidence/dfs-serp-name.json`): `therapie-sasch.com` is NOT in the 9 organic results. The results are unrelated pages (jameda Psychosomatiker Coburg, doctolib listings from other regions, theralupa, findedeinentherapeuten.de). Google shows the item types `knowledge_graph` and `google_reviews` for this query, but the result file holds no detail for them. Do not claim a panel text from this file. Her brand name alone does not bring up her site in this test. Read as: the brand term "Sasch" is not yet connected to her by Google in this location. Treat as a finding to check, not as proof.
- "sabine schwarz heilpraktikerin coburg" (`evidence/dfs-serp-name2.json`): her site is rank 1 (homepage) and rank 7 (`kontakt.html`). Other hits: therapie.de profile (2), theralupa (3), jameda profile (4), LinkedIn (5), Facebook (6), starofservice (8), heilnetz (9), Instagram (10). Item types include `knowledge_graph`, `google_reviews`, `third_party_reviews`. Google also lists her theralupa title "S. Schwarz Heilprakt. Psychotherapie Coburg u. SASCH ... Paartherapie online in Coburg". The full-name search works. The brand search "therapie sasch" does not.

## 5. Spam links

- Evidence: `evidence/dfs-backlinks-summary.json` and `evidence/dfs-refdomains-spam.json` (target `therapie-sasch.com`, subdomains included, filter `backlinks_spam_score >= 60`).
- Referring domains in total: 1018 (backlinks 1046; referring main domains 1017; domain rank 77; summary spam score 52; only 3 referring domains are nofollow).
- Referring domains with spam score 60 or more: **38 of 1018** (3.7 percent). Spam scores run from 60 to 75.
- Types seen in the list (from the domain names): SEO checker and web2.0 spam domains (e.g. seonix.agency, web20.space, checkerseo.store, dapacheckerpro.site, backlinksboost.info, highdachecker.space with score 75) and a few casino or odd sites (bestnz-poker-casinoslot.com, betwinnermirror.com).
- Caution for the writer: the summary spam score of 52 (whole profile) is a DataForSEO value, not a Google penalty. Do not claim a Google penalty. Say: "38 von 1.018 verlinkenden Domains haben einen hohen Spam-Wert (60 oder mehr)".

## 6. Task status

All six paid calls returned task status 20000. No 40101. No retry needed.
Calls: volumes-ads 0.09, serp-1 0.0035, serp-2 0.0035, serp-name 0.002, serp-name2 0.002, backlinks-summary 0.0240, refdomains-spam 0.0254. Total 0.1504 USD.
