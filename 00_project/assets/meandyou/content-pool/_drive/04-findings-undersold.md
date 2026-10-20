# Findings: Undersold (lp:undersold), 2026-10-12

Scope: content pool for the Undersold landing page. Items are in `04-pool/candidates-undersold.json` (20 items, 1 cut). The competitor set has 8 readable pages, all in tier "niche". The paid calls of this part cost 0.1005 USD (`spend.jsonl`).

Competitor set: deutsche-rednerschule.de, beatrixschwarzbach.de, manager-institut.de, haufe-akademie.de, akzent-consulting.de, wip-management.de, ifmera.com, drgkitzmann-akademie.de.

## F1. The places are the clear gap, but they are not a search lever
- No readable competitor page names Mallorca, Barcelona, Zypern or Dubai (`02-competitors/metrics-undersold.json`, field `places` and the headings).
- 6 of 8 pages name only Frankfurt or Berlin.
- "seminar mallorca" has 20 searches (`03-demand/volume-undersold.json`). "rhetorik seminar mallorca" has no data (`volume-1.json`). "rhetorik seminar barcelona" and "rhetorik seminar dubai" have no data (`volume-undersold.json`).
- Autocomplete shows "rhetorik seminar mallorca" and "michael ehlers rhetorik mallorca" (`03-demand/autocomplete-undersold.json`).
- The current LP has no places and no dates (`../prototype-v2/lp-undersold.html`).
- Result: use the places for conversion of ad traffic (CP-LOC-301, CP-LOC-302). Do not expect organic traffic from them.

## F2. Leader demand exists, but academies hold the SERP
- In `volume-1.json`: "rhetorik seminar" 880, "führungskräfte kommunikation" 210, "coaching für geschäftsführer" 170, "kommunikationstraining führungskräfte" 140, "executive presence" 140, "rhetorik für führungskräfte" 110, "rhetorik seminar führungskräfte" 40.
- In `volume-undersold.json`: "rhetorik seminar für führungskräfte" 40.
- `serp-32.json` shows an AI overview, Haufe, IHK, manager-institut and book shops.
- `serp-31.json` shows portals and the city pages of academies.
- Result: the LP is an ad and premium page first. Use the leader terms in the title, the H2 and "Für wen". Do not build it as an SEO money page.

## F3. The current LP misses most table-stakes blocks
Each number is the count of readable competitor pages with the block (`02-competitors/metrics-undersold.json`).

| Block | Competitors | On the current LP |
| --- | --- | --- |
| Contents or goals | 6 of 8 | no |
| Booking, form or contact | 6 of 8 | yes (3 buttons) |
| Dates | 5 of 8 | no |
| Ratings or voices | 5 of 8 | yes |
| Target group | 4 of 8 | no |
| Group, format, methods | 4 of 8 | no |
| FAQ | 2 of 8 | no |

Other defects on the current LP:
- It says "5 Bücher", but `../cro/michael/02-data/dataset.md` K1 says "neun Bücher".
- The carousel shows each quote three times.
- The heading "Vorher. Nachher." can read as a result promise (UWG).
- The persona rule asks for one CTA far down, but the LP has three.

## F4. People search for Michael by name
- "michael ehlers" has 480 and "michael ehlers rhetorik" has 90 (`volume-undersold.json`).
- Autocomplete also shows other people with the same name. Read 480 as an upper bound.
- Autocomplete shows "michael ehlers rhetorik seminar", "michael ehlers coaching", "michael ehlers podcast" and "michael ehlers nie wieder sprachlos".
- Result: name Michael in the title and add Person and Event schema (CP-AUT-303).

## F5. The page must answer the cost question without a price
- The PAA question "Was kostet ein Rhetorikkurs?" is in `serp-31.json` and `serp-33.json`. "Was kostet ein 1 zu 1 Coaching?" is in `serp-33.json`.
- 3 of 8 competitors show a price or a price heading.
- The rule is no prices on any page. CP-SVC-306 answers with what is included and points to the call.

## Unreadable pages
- topgunspeaking.com: timeout.
- bostonprograms.com: Access Denied.
- rhetorikhelden.de: the page builds its content with scripts, so the HTML has no title and no headings.

## Open client facts [FEHLT]
1. du or Sie.
2. Name and role of the person in the call.
3. The seminar names R I to R III and one sentence on DeepOcean.
4. The Mallorca dates 2027 (conflict K1).
5. The number of books: 5 or 9.
6. Approval of the sales checklist.
7. Real photos for each place.
8. Quotes from entrepreneurs with consent.
9. The ProvenExpert total score as the profile shows it.
10. Does 1:1 coaching with Michael exist?
11. Does Michael offer media training?
12. The profile URLs for sameAs.

## Decisions for Martin
- **D1 du or Sie.** The approved hero says "Ihr Unternehmen …". The persona line and the rest of the site use du. Choose one form for the whole page.
- **D2 Call or application.** The copy deck uses "Gespräch buchen" on all three LPs. The persona guide names an application form and a private follow-up. Choose one.
- **D3 Number of CTAs.** The persona rule is one CTA far down; the LP has three. Choose one rule.
- **D4 Adjacent offers.** Keep 1:1 coaching (CP-SVC-308) and media training (CP-SVC-309) out until the client confirms them. Both are fit 1.
- **D5 Cut.** CP-SVC-310 (VHS, IHK, Bildungsurlaub, inhouse) is fit 0. "rhetorik seminar vhs" has 170 in `volume-undersold.json`, but the client does not offer this.
