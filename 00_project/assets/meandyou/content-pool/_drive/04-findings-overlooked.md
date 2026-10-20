# Findings: The Overlooked (lp:overlooked), 2026-10-12

Items: `04-pool/candidates-overlooked.json` (20 items, 3 cut). Data files: `02-competitors/serp-21.json`, `serp-22.json`, `serp-23.json`, `metrics-overlooked.json`, `03-demand/autocomplete-overlooked.json`, `volume-overlooked.json`, shared `volume-1.json`.

Competitor set: niche = rhetorik-fuehrerschein.de, argumentorik.com, rhetorik-online.de, felixbehm.de, rhetorik-consulting.de, staerkentrainer.de. topic = mathias-fischedick.de, mm-coach.me.

## Finding 1: The demand is in the course term, not in the problem words
- "rhetorik kurs" and "rhetorik kurse" show 1600 each. "rhetorik online kurs" and "rhetorik kurs online" show 210 each (`volume-1.json`, `volume-overlooked.json`).
- "im meeting nicht gehört werden" and "im meeting durchsetzen" have no data (`volume-1.json`). "nicht gehört werden" shows 20 (`volume-overlooked.json`).
- "nicht ernst genommen werden" shows 170. Most autocomplete lines for it are about doctors, health and family (`autocomplete-overlooked.json`). We did not use it as a target.
- Result: the hero keeps the approved problem line for ad traffic. The organic hook is the course and the method (CP-SVC-201, CP-SVC-202, CP-BRD-203).

## Finding 2: "durchsetzungsvermögen" is big, but most of it is not buyer intent
- "durchsetzungsvermögen" shows 880 (`volume-1.json`). Page 1 has a dictionary (linguee.de), and the PAA asks for a synonym (`serp-22.json`).
- Autocomplete shows many synonym, translation, job-application and child intents. These are cut in CP-SVC-209.
- The learnable part is real but small. "durchsetzungsvermögen lernen" shows 30 and "überzeugungskraft" shows 170 (`volume-overlooked.json`).
- We use this demand in CP-SVC-204 (mapped to Rhetorik II contents) and in the FAQ (CP-SVC-207).

## Finding 3: Competitors show structure, but nobody names the competence gap
- 7 of 8 pages were readable (`metrics-overlooked.json`). felixbehm.de is unreadable.
- Course pages show a numbered structure and an online format in their headings. These are table stakes.
- Only argumentorik.com has Course schema with a rating. This is a gap for CP-AUT-204.
- No course page frames the problem as "right, but not followed". Only one blog teaser on rhetorik-online.de touches "kompetent".
- rhetorik-fuehrerschein.de shows a money-back guarantee. We did not add this item: there is no client fact for it, and UWG applies.

## Finding 4: The online course is the persona product, but the site does not sell it yet
- The design guide names the online course as the Overlooked product (`meandyou-design-richtlinien.html`, section 02).
- The approved FAQ data says the online course is not a goal of the website (`cro/faq/02-data/dataset.md`, L10, L11). Copy deck page 06 sets "Gespräch buchen" as the only CTA.
- Course facts are thin. We only have "video lessons" and "access at least 12 months".

## Finding 5: The current LP shows facts that conflict with the dataset
- `lp-overlooked.html` shows "5 Bücher", "Top 100 Speaker" and "30 Jahre".
- The dataset says "neun Bücher", "Top 100 Trainer laut ERFOLG Magazin" and "seit 1990" (`cro/michael/02-data/dataset.md`, K1, K2, K5).
- The sentence "gehört zu den bekanntesten Rhetoriktrainern" needs proof or removal (UWG).
- The heading "Vorher. Nachher." sits above quotes that show no before or after. Check the wording.
- "michael ehlers" shows 480 and "michael ehlers rhetorik" shows 90 (`volume-overlooked.json`). The first term can include other people with the same name.

## Open client facts ([FEHLT])
1. The online course name to use. "Intelligente" is no longer a main term.
2. The module list, and the number and length of lessons.
3. The access term (confirm 12 months), the extras (Q&A, community, workbook), the platform and the devices.
4. How to buy: direct checkout, or only through the call.
5. Which Rhetorik II topics the course also covers.
6. One sentence and one exercise for each of the three method steps.
7. Who leads the 30-minute call.
8. Consent to show names for quotes G5, G8 and G12.
9. Logo files and usage rights (ARTE, WELT TV, Universität St. Gallen, ERFOLG Magazin).
10. Does the book "Die 5 Säulen der positiven Kommunikation" answer the PAA "Was sind die 5 Säulen der Rhetorik?" (CP-AUT-205, fit 1)?
11. Is there a written refund policy? Only then can we add a risk-reversal item.

## Decisions for Martin
1. LP goal: sell the call only (copy deck), or show the online course (design guide)? Items CP-SVC-201, -O02, -O03 and CP-AUT-204 depend on this.
2. Fix the LP facts now? These are text-only changes: books, Top 100, years, "bekanntesten", "Vorher. Nachher.".
3. Keep "Gespräch buchen" as the only CTA, or add a quiet second link to a course page?

## Cut items
- CP-LOC-202: city and VHS intent.
- CP-SVC-208: free course intent. Route it to lp:replayers.
- CP-SVC-209: dictionary and HR intent.
