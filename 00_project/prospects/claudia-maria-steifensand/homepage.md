# Homepage: bestattung-pinkertundpartner.de (agent C, 2026-10-13)

## Score

- Today: **13 / 44** (evidence/scorecard-today.md). Item 22 = 2 (not health, no legal risk).
- Screenshots: evidence/home-today-1440.jpg (operator, 1440 × 813), evidence/home-draft-1440.jpg (our draft, 1440 × 838).
- Review assets: 04_site/public/review-assets/claudia-maria-steifensand/startseite-heute.webp, startseite-entwurf.webp, foto-1.webp, foto-2.webp, foto-3.webp.

## 5-second test

| Question | Today (first screen) | Draft (first screen) |
| --- | --- | --- |
| Was? | Brand text "Bestattungsinstitut Pinkert & Partner" only. No H1. The hero is a stock photo of roses. | H1 "Ihr Bestattungsinstitut in Riesa." + sub-line for families: "Ein Mensch aus Ihrer Familie ist gestorben? Wir begleiten Sie und Ihre Angehörigen ruhig und persönlich durch den Abschied." |
| Wo? | Not visible. No city, no address on the homepage. | "in Riesa" in the H1. Top bar "Goethestr. 1, 01589 Riesa". Card "Eigene Trauerhalle, Riesaer Straße 40, Oelsitz". |
| Warum Sie? | Only the Bestatter-Handwerk badge (top part at the fold). "1991" is in section 3. | Eyebrow "Familienunternehmen in Riesa seit 1991", stars "5,0 bei Google · 4 Bewertungen", trust row: Seit 1991, Fachgeprüfte Bestatter, 4 Bestattungsarten, Bestattungsvorsorge. |
| Wie erreichen? | Header text "Rufen Sie an: 03525 735814". No button. The 24-hour line is only on /kontakt/. | Top bar "Im Trauerfall Tag und Nacht für Sie da: 03525 735814", header button "03525 735814 anrufen", hero button "Jetzt anrufen: 03525 735814", note "Tag und Nacht telefonisch erreichbar. Büro: Montag bis Freitag, 8 bis 17 Uhr." |
| Wer? | No person, no photo of the house. | Real photo of the office front Goethestr. 1 (goethestr-_1.jpg from /kontakt/), inset card with the real Trauerhalle photo. No person named (see notes). |

Trust-row and hero sources (all on her site, curl 2026-10-13):

| Item | Source | Exact text |
| --- | --- | --- |
| Seit 1991, Familien | https://bestattung-pinkertundpartner.de/ | "Unser Unternehmen wurde von den Familien Pinkert und Eisner 1991 in Riesa gegründet." |
| Fachgeprüfte Bestatter | https://bestattung-pinkertundpartner.de/unser-haus/ | "Deshalb bieten wir, als "Fachgeprüfte Bestatter", unsere Dienste an" |
| 4 Bestattungsarten | https://bestattung-pinkertundpartner.de/leistungen/ | "Erd-, Feuer-, Wald- und Seebestattung" |
| Bestattungsvorsorge | https://bestattung-pinkertundpartner.de/leistungen/ | "Abschluss von Bestattungsvorsorgeverträgen" |
| Eigene Trauerhalle | /kontakt/ + /leistungen/ | "Unsere Trauerhalle, Riesaer Straße 40, 01589 Oelsitz"; "Aufbahrungen in unserer Trauerhalle, die auch für die Trauerfeier zur Verfügung steht" |
| Tag und Nacht | https://bestattung-pinkertundpartner.de/kontakt/ | "Tag und Nacht sind wir telefonisch dienstbereit unter Telefon (03525) 735814." |
| Büro-Zeiten | /kontakt/ | "Montag - Freitag 8.00 - 17.00 Uhr" |
| "so viel, wie Sie es möchten" | /unser-haus/ | "übernehmen soviel wie möglich, oder Sie es möchten, an Dienstleistungen" |
| 5,0 · 4 Bewertungen | evidence/google-panel-2026-10-13.md | panel 1 (Goethestraße 1): "Rating: 5,0 · 4 Rezensionen" |

Notes for the review page:
- **Person.** Claudia Maria Steifensand is not named on the site. The imprint names "Inhaberin: Conny Pinkert-Stockert". The draft names no person. Agent E must not give Claudia a role without a source (LinkedIn chat or profile).
- **Two Google entries** share the phone +49 3525 735814. Panel 1: Goethestraße 1, 5,0 with 4 reviews, newest about 1 year old, "Rund um die Uhr geöffnet", 0 owner replies. Panel 2: Riesaer Str. 40, Riesa-Oelsitz (the Trauerhalle), 3,2 with 5 reviews, newest about 3 years old, "Als Inhaber eintragen" shown, opening hours "Öffnet um 08:00" (conflicts with the 24-hour line). The draft uses panel 1 only.
- **Postcode conflict.** The site writes "01589 Oelsitz" for the Trauerhalle. Google panel 2 writes "01594 Riesa-Oelsitz". The draft writes no postcode for the Trauerhalle.
- **Stock hero.** The imprint names the rose photo: "Rose: Pexels / KoolShooters". The real photos (house, office entrance, Trauerhalle, Ausstellungsraum, arrangements) are only on /unser-haus/ and /kontakt/.
- **Logo.** The site has no logo image. The brand is text in Cinzel, colour rgb(188,174,154). The draft uses the same text brand. The badge logo-bestatterhandwerk.png is a trade badge, not her logo. Not used.
- **Typo** on the homepage: "kompetender Ansprechpartner" (correct: "kompetenter").
- No H1 on the homepage. No address, map or hours on the homepage.

## Test of draft_home.py

Run: `python3 prospect-mini/scripts/draft_home.py claudia-maria-steifensand --service "Bestattungsinstitut"`, 7.9 s wall time (script reports 7.8 s). Output: no logo, no images in the draft (4 candidates found, none used), 2 trust cards.

What I had to fix by hand in draft/index.html:
1. **No hero photo.** The `.pic` box was empty. The homepage has only the stock rose photo. New haus.jpg = goethestr-_1.jpg (office front Goethestr. 1, from /kontakt/, 2000 × 1069, resized to 1400).
2. **No inset card.** Added a card with trauerhalle.jpg (bild_trauerhalle2.jpg from /kontakt/, real photo of the Trauerhalle): "Eigene Trauerhalle, Riesaer Straße 40, Oelsitz". No person card (no portrait on the site).
3. **Colours.** The script took cyan #00b2ff and red #cc0918. These come from library CSS (plyr player and form styles), not from her design. Her CSS variables: --col-secondary rgb(188,174,154) (taupe), --col-primary rgb(82,82,82) (grey). Changed to taupe #bcae9a, button dark taupe #7d6e58 (for white text contrast), grey bar #525252, cream #f5f1eb. Cyan was also wrong in tone for a funeral home.
4. **Fonts.** Fraunces + Inter → her fonts: Cinzel (header font) for the brand and the H1, Roboto for text.
5. **Brand.** Text "Bestattungsinstitut Pinkert und Partner" in one line → "Bestattungsinstitut / Pinkert & Partner" in two lines, as on her site.
6. **Sub-line grammar and tone.** "Sie suchen einen Bestattungsinstitut in Riesa? Wir nehmen uns Zeit für Ihr Anliegen." (wrong gender "einen", "Anliegen" too cold). → "Ein Mensch aus Ihrer Familie ist gestorben? Wir begleiten Sie und Ihre Angehörigen ruhig und persönlich durch den Abschied. Wir übernehmen so viel, wie Sie es möchten."
7. **Practice words.** Trust card "Praxis in Riesa", button "Ersttermin vereinbaren", top bar and header "Termin vereinbaren". → no "Praxis", no "Termin". Button "Jetzt anrufen: 03525 735814", header "03525 735814 anrufen", top bar "Im Trauerfall Tag und Nacht für Sie da: 03525 735814 · Goethestr. 1, 01589 Riesa".
8. **Phone format.** "+493525735814" → "03525 735814" (as on her site and imprint).
9. **24-hour line.** Missing. Added in the top bar and the note under the button (source /kontakt/).
10. **Eyebrow.** "Unser Haus" (a nav label) → "Familienunternehmen in Riesa seit 1991".
11. **Stars.** Missing. Added "5,0 bei Google · 4 Bewertungen" (panel 1).
12. **Trust row.** 2 cards ("Bestattungsinstitut / Praxis in Riesa", "Telefon / +493525735814") → 4 cards with facts from her site (table above).
13. **Headline size.** 48 px broke the H1 into 3 lines in Cinzel → 42 px, 2 lines.
14. **Note line.** "Rufen Sie an oder schreiben Sie uns. Wir melden uns persönlich bei Ihnen." → "Tag und Nacht telefonisch erreichbar. Büro: Montag bis Freitag, 8 bis 17 Uhr."

Checks passed: form of address "Sie" (as on the site). Words: Familie, Angehörige, Abschied. No "Kunden", "Patienten", "Praxis", "Termin". No sales words, no promises. Trust row has only facts from her site. Address and phone from the imprint and Google panel 1.

Strip photos (all from bestattung-pinkertundpartner.de, opened and checked, real photos):
- foto-1 = bild_trauerhalle2.jpg, the Trauerhalle with rows of chairs (600 px wide, the largest size on the site).
- foto-2 = 20230304_110116.jpg, the Ausstellungsraum with urns (1200 px).
- foto-3 = allich9.jpg, an urn arrangement with flowers (1200 px).
Not used: header-rosen.jpg (Pexels stock), bg-rose-box.png (background), logo-bestatterhandwerk.png (trade badge), coffin and urn shelf photos (too hard for a first view), WhatsApp flower photos 2016 (low quality).
