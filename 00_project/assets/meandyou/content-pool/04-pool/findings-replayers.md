# Findings: The Replayers (lp:replayers), 2026-10-12

Data: `02-competitors/serp-11.json`, `serp-12.json`, `serp-13.json`, `02-competitors/metrics-replayers.json`, `03-demand/autocomplete-replayers.json`, `03-demand/volume-1.json`, `03-demand/volume-replayers.json`. Items: `04-pool/candidates-replayers.json`.

## Competitor set (for the merge)
| Domain | Tier | Page type |
| --- | --- | --- |
| rhetorik-online.de | niche | Trainer blog, Schlagfertigkeit |
| einfach-klartext.de | niche | Trainer blog, Schlagfertigkeit |
| schlossgangl.com | niche | Trainer blog, Schlagfertigkeit |
| mycompetence.de | niche | Online course page, Schlagfertigkeit |
| kutscher-seminare.de | niche | Seminar provider blog, Schlagfertigkeit |
| tobias-beck.com | topic | Coach blog, Lampenfieber |
| wir-machen-redner.de | topic | Trainer page, Lampenfieber |
| seidirselbstbewusst.com | topic | Coach blog, Lampenfieber |

Left out because they are portals or big media: haufe-akademie.de, karrierebibel.de, stepstone.de, wiwo.de, 7mind.de, amazon.de, youtube.com, reddit.com.

## F1. Searchers name the exact persona problem. No trainer answers it.
- `03-demand/volume-1.json`: "treppenwitz" has 1600 searches per month.
- `03-demand/volume-replayers.json`: "was ist ein treppenwitz" has 320, and "treppenwitz bedeutung" has 260.
- `03-demand/autocomplete-replayers.json` contains:
  - "schlagfertigkeit ist das was einem auf dem nachhauseweg einfällt"
  - "schlagfertigkeit ist etwas worauf man erst 24 stunden später kommt"
  - "nächtliche schlagfertigkeit"
- `02-competitors/serp-12.json`: the results are dictionaries, joke pages and history pages. No trainer, coach or course is in the results.

Result: CP-BRD-102 puts this moment on the LP as a recognition block. An explainer article is an option for later.

## F2. Competitor pages sell techniques. Michael's method starts before the technique.
- `02-competitors/metrics-replayers.json`: the Schlagfertigkeit pages are lists of techniques, exercises and tips. Example headings:
  - "Technik 1: Die Pause" (kutscher-seminare.de)
  - "Grundtechniken der Schlagfertigkeit" (einfach-klartext.de)
  - "10 Schlagfertigkeitstechniken für Einsteiger" (mycompetence.de)
- Only two pages explain why people go silent: kutscher-seminare.de and schlossgangl.com.
- `03-demand/volume-1.json`: "schlagfertigkeit" has 2400 searches per month, and "schlagfertigkeit lernen" has 480.

Result: CP-SVC-102 (Persönlichkeit, Kongruenz, Wirkung) is the difference. Visitors still expect a few exercises (CP-SVC-103). The exercises must come only from Michael's book or podcast.

## F3. Lampenfieber has large demand but much medical and brand noise.
- `03-demand/volume-1.json`: "lampenfieber" has 1900 searches per month, and "lampenfieber überwinden" has 90.
- `03-demand/volume-replayers.json`: "redeangst" has 110.
- `03-demand/autocomplete-replayers.json` has medication and remedy terms (Betablocker, Propranolol, Globuli, Homöopathie). It also has theatre and company names.
- People Also Ask in `serp-13.json` includes "Woher kommt Lampenfieber?"
- `cro/02-data/reviews.md` P5 says Michael helps "die Redeangst zu nehmen".

Result: Lampenfieber goes on the LP only as an FAQ set (CP-SVC-109). The answer is practice with feedback. The flag is `review`: no health claims, no remedy names, no "angstfrei" promise.

## F4. The free first step is the Replayers product, but the LP sells only the call.
- `cro/02-data/dataset.md`: the 8 active Meta ads lead to /sichtbarkeit-neu.
- Design guidelines section 02: the free training, the book and the community belong to this persona.
- Copy deck R3 page 06: the CTA on all three LPs is "Gespräch buchen".
- The current `prototype-v2/lp-replayers.html` shows only the call.
- `02-competitors/metrics-replayers.json`: mycompetence.de sells a course with a price. The trainer blogs use a form or a newsletter.

Result: CP-LOC-101, CP-SVC-104 (book), CP-SVC-105 (community) and CP-AUT-103 (podcast) fill this gap. Only one CTA is visible at a time.

## F5. The current LP proof does not speak to this persona, and two numbers conflict.
- `prototype-v2/lp-replayers.html` shows quotes from public figures. The quotes do not name the problem.
- `cro/02-data/reviews.md` has the persona language: "unsicher oder sprachlos" (P1), "die Redeangst zu nehmen" (P5), "zwischen der ersten und der letzten Rede lagen wirklich Welten" (G7).
- The LP shows "5 Bücher". `cro/michael/02-data/dataset.md` K1 has "neun Bücher".
- The LP shows "Top 100 Speaker". `cro/04-copy/approved-copy.md` has "Top 100 Trainern" and "Top-10-Speaker".

Result: CP-AUT-101 changes the proof to quotes from this persona. CP-AUT-102 corrects the numbers.

## Cut (fit 0, not in the candidates)
| Topic | Source | Why cut |
| --- | --- | --- |
| Lampenfieber medication and remedies | `autocomplete-replayers.json` | Michael does not offer this. Health claim risk. |
| "Die richtigen Worte" for grief or illness, and the hymn | `autocomplete-replayers.json` | Other intent. |
| Schlagfertigkeit for children, Sprüche, Kreuzworträtsel, translations | `autocomplete-replayers.json`, `serp-11.json` | Michael does not offer it, or the intent is a joke or a puzzle. |
| "Treppenwitz der Geschichte" | `autocomplete-replayers.json`, `serp-12.json` | History idiom. |
| Lampenfieber with theatre, band or company names | `autocomplete-replayers.json` | Brand noise. |
| "sprachlos" as a target | `volume-replayers.json` | The intent is mixed and we have no SERP for it. Only "nie wieder sprachlos" (book title) stays. |

These have no volume, but they are not cut: "rhetorik für introvertierte", "kostenloses rhetorik training", "schlagfertigkeit online kurs". "Schlagfertigkeit online kurs" is in the autocomplete data, so it stays in CP-LOC-101.

## Open client facts ([FEHLT])
1. Content and length of the free video training.
2. Two or three exercises from Michael, word for word, with his release.
3. Michael's own sentence on why the words come late.
4. "Nie wieder sprachlos!": edition, publisher and where to get it. No price on the page.
5. Number of books: 5 or nine.
6. Exact wording of the ERFOLG Magazin award.
7. The current offer of the community "Talk to Me".
8. The new name of the Schlagfertigkeit seminar format (R II).
9. Consent for the quote names (Jenny Eikel, Julian L., Christian S.).

## Decisions for Martin
1. **Main CTA of this LP:** "Gespräch buchen" (copy deck) or the free training (product ladder). F4 supports the free training first and the call second.
2. **Community:** the FAQ run cut it (`cro/faq/02-data/dataset.md` V10), but the design guidelines list it for the Replayers. In or out?
3. **Treppenwitz:** a block on the LP only, or also an explainer article later?
4. **CP-SVC-107 (Schlagfertigkeit im Job):** it overlaps with The Overlooked. Keep it here with the "after the meeting" angle, or move it to `lp:overlooked`?
