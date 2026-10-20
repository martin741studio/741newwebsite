# Demand: Christian Ruether (agent A, 2026-10-12)

Market: Austria, location_code 2040, language de. SERP location: Wien (48.2082,16.3738). No map-pack data: this endpoint returns no map items. No map position is claimed.

## 1. Search volumes (Google Ads, Austria)
Evidence: `evidence/dfs-volumes-ads.json`. Austria returned data for 11 of 13 terms. No call for Germany was needed.
"Google gibt keine Zahl heraus" = no number in the answer. A value of 10 is the lowest value Google shows.

| Keyword | Volume per month | CPC (USD) | Competition |
|---|---|---|---|
| soziokratie | 260 | Google gibt keine Zahl heraus | LOW |
| moderation wien | 50 | 2.41 | MEDIUM |
| organisationsberatung wien | 20 | 5.35 | HIGH |
| konsent moderation | 10 | Google gibt keine Zahl heraus | Google gibt keine Zahl heraus |
| konsent entscheidung | 10 | Google gibt keine Zahl heraus | Google gibt keine Zahl heraus |
| soziokratie 3.0 | 10 | Google gibt keine Zahl heraus | LOW |
| holakratie | 10 | Google gibt keine Zahl heraus | LOW |
| was ist soziokratie | 10 | Google gibt keine Zahl heraus | LOW |
| soziokratie ausbildung | 10 | Google gibt keine Zahl heraus | LOW |
| selbstorganisation unternehmen | 10 | Google gibt keine Zahl heraus | Google gibt keine Zahl heraus |
| new work beratung | 10 | Google gibt keine Zahl heraus | Google gibt keine Zahl heraus |
| soziokratie wien | Google gibt keine Zahl heraus | | |
| soziokratische kreisorganisationsmethode | Google gibt keine Zahl heraus | | |

Findings:
- Only one term has real demand: "soziokratie" with 260 per month (range in 12 months: 140 to 320). Evidence: `dfs-volumes-ads.json`.
- The niche is small. Most terms sit at the Google floor of 10.
- "moderation wien" has 50 per month, with a spike of 210 in the last month of the series. See the SERP note in section 3: this term shows event hosts, not facilitators.

### Merged variants (same volume, same CPC, same monthly series = one Google variant; do not add up)
- "konsent moderation" and "konsent entscheidung": series 0,10,10,10,10,10,10,10,10,10,10,10. One variant: 10 per month in total.
- "was ist soziokratie" and "soziokratie ausbildung": series 10 in all 12 months. One variant: 10 per month in total.

## 2. Gap keyword proposal
**Proposal: "organisationsberatung wien"** (20 per month, CPC 5.35 USD, competition HIGH).
- Service fit: Soziokratie and Holakratie consulting for organisations is his core offer (site menu: Soziokratie Elemente, Fallbeispiele, Begleiter*innen, Termine). Evidence: `dfs-volumes-ads.json`, homepage menu.
- His site is NOT in the organic top 20 for this term. Evidence: `evidence/dfs-serp-4.json` (20 organic results, no soziokratie.org).
- The high CPC shows buyers with commercial intent.
- Risk: the site has no consulting page today. A new page must show "Soziokratie als Organisationsberatung in Wien". The term may need a Wien angle in H1 and title.

Checked and rejected (his site already ranks, so no gap):
- "soziokratie": soziokratie.org is at organic position 1 (page /was-ist-soziokratie/) and position 6 (/elemente/). Evidence: `evidence/dfs-serp-1.json`.
- "konsent moderation": soziokratie.org is at organic position 1 (/konsentmoderation/) and 19. Evidence: `evidence/dfs-serp-3.json`.
- "moderation wien": his site is not in the top 20. But the results are event hosts, TV hosts, job boards and training courses. His KonsenT-Moderation does not match this intent. Do not use as the gap. Evidence: `evidence/dfs-serp-2.json`.
- "soziokratie wien", "soziokratische kreisorganisationsmethode": Google gives no number.

## 3. SERP results (Wien, depth 20, organic only)
- "soziokratie" (`dfs-serp-1.json`): 17 organic results. soziokratie.org at position 1 and 6. Others: soziokratiezentrum.org (4 results), soziokratiezentrum.de (2), thesociocracygroup.ch, dersoziokrat.at, mehr-demokratie.at.
- "moderation wien" (`dfs-serp-2.json`): 20 organic results, soziokratie.org absent. Mix of event hosts, job boards, training courses.
- "konsent moderation" (`dfs-serp-3.json`, extra call): soziokratie.org at position 1 and 19.
- "organisationsberatung wien" (`dfs-serp-4.json`, extra call): soziokratie.org absent.

## 4. Competitor provider URLs for the page-length check (no directories, no Wikipedia)
For the gap keyword "organisationsberatung wien" (source `dfs-serp-4.json`):
1. https://systworks.com/organisationsberatung/ (rank 1)
2. https://www.wonderwerk.com/change-management/ (rank 2)
3. https://diebusinesscoach.at/organisationsentwicklung-changemanagement/ (rank 6)
4. https://www.inspiringleaders.at/de/organisationsentwicklung (rank 19)
5. https://www.janesconsulting.com/beratungsfelder.html (rank 12)

For the Soziokratie topic (source `dfs-serp-1.json`):
1. https://soziokratiezentrum.de/soziokratie-anwenden/unternehmen/
2. https://thesociocracygroup.ch/home/
3. https://dersoziokrat.at/soziokratie/
Excluded as directories or not providers: firmenabc.at, herold.at, wko.at, supervision.at, karriere.at, indeed, linkedin, youtube, amazon.

## 5. Name searches (Wien, depth 10)
- "soziokratie.org" (`dfs-serp-name.json`): soziokratie.org is NOT in the 9 organic results. Results show soziokratiezentrum.org (7 results), sociocracyforall.org, facebook (Soziokratie Bodensee). The domain query does not return his own site. Finding: Google does not match the bare domain name to his site.
- "christian rüther soziokratie" (`dfs-serp-name2.json`): soziokratie.org is at positions 1 (/konsentmoderation/), 2 (PDF vergleich-soziokratie-holakratie) and 6 (/anmeldung/). Other results: wu.ac.at, youtube (2), gewaltfrei.at, soziokratiezentrum.de/.org, christianruether.com.
- Meaning: with his full name the site ranks first. With the domain name only, it does not rank. His brand is the person, not the domain.

## 6. Spam links
- Spam links (spam score 60 or more): **47 of 319 linking domains** (about 15 %). Evidence: `evidence/dfs-refdomains-spam.json` (filter backlinks_spam_score >= 60, 47 results) and `evidence/dfs-backlinks-summary.json` (319 referring domains, 946 backlinks, 307 main domains, rank 233).
- All 47 spam domains have rank 0. Each links once, except datenrecherche.de (10 links) and gfk-training.blogspot.com (4). Types: casino and betting sites (.online), .shop sites, fake news sites (forbesstories.com, theforbestimes.com).
- Average spam score of the whole profile: 16 (`dfs-backlinks-summary.json`).

## 7. Cost and blockers
- DataForSEO spent: 0.1577 USD (ledger `cost_ledger.jsonl`). Cap 0.30 not reached.
- Two extra SERP calls (serp-3, serp-4, 0.007 USD) were added to prove the gap keyword. This is slightly above the 0.15 budget.
- No task failed (no status 40101). No Labs call. No browser used. Homepage menu read with curl.
