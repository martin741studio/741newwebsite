# Homepage: therapie-sasch.com (agent C, 2026-10-12)

## Score

- Today: **22 / 44** (evidence/scorecard-today.md). Item 22 (HWG) = 0, so the hard gate fails.
- Screenshots: evidence/home-today-1440.jpg (operator), evidence/home-draft-1440.jpg (our draft).
- Review assets: 04_site/public/review-assets/sabine-schwarz/startseite-heute.webp, startseite-entwurf.webp, foto-1.webp, foto-2.webp, foto-3.webp.

## 5-second test

| Question | Today (first screen) | Draft (first screen) |
| --- | --- | --- |
| Was? | "Paartherapeutin & Heilpraktikerin für Psychotherapie" in the H1 sub-line. Services hide in the "Angebote" dropdown. | "Ihre Heilpraktikerin für Psychotherapie in Coburg und Ahorn." plus Psychotherapie (HPG), Paartherapie, Coaching in the sub-line. |
| Wo? | Not visible. Ahorn and Coburg appear only in the Standorte section further down. | Coburg and Ahorn in the H1. "2 Praxisorte: Ahorn-Schorkendorf · Coburg" in the trust row, "oder online" in the sub-line. |
| Warum du? | Membership logos at the fold (Reiki-Verband, VFP, Heilnetz). Google 5,0 with 15 reviews is not on the site. | 5,0 bei Google · 15 Bewertungen, Erlaubnis seit 2019, Mitglied im VFP e.V. und Heilnetz e.V. |
| Wie zum Termin? | Button "Kontakt". The floating "Erstgespräch buchen · kostenlos · 15 Min." is semi-transparent and covers the Heilnetz text. No phone in the first screen. | Button "Kostenloses Erstgespräch buchen", line "15 Minuten, kostenlos. Online buchen, anrufen oder schreiben.", phone 0151 124 8989 0 in the top bar and the trust row. |
| Wer? | Real photo of her in the practice room, name in the H1. | Same room photo as the hero image, name card with face photo and "Heilpraktikerin für Psychotherapie · Paartherapeutin". |

Notes for the review page:
- Her strongest asset is unused: 15 of 15 Google reviews are 5 stars, and she answered all of them. The site shows none.
- She already has an online booking page (Buchung.html, "Erstgespräch buchen, kostenlos, 15 Min."). The hero button still says only "Kontakt".
- HWG risk on the homepage: "Selbstheilungskräfte zu aktivieren", "schnell spürbare Fortschritte", "nachhaltige Veränderungen zu ermöglichen".
- The Google category is "Alternativmediziner". Her main service is Psychotherapie (HPG) and Paartherapie. Agent D/E must check this against the keyword.
- Mobbing-Beratung appears only on about.html (training 2016-2018, Fachausbildung). It is not a service on the homepage.
- Imprint: "Heilpraktikerin beschränkt auf das Gebiet der heilkundlichen Psychotherapie", Erlaubnis vom 18.11.2019 (Stadt Nürnberg). Never write "Psychotherapeutin".

## Test of draft_home.py

Run: `python3 prospect-mini/scripts/draft_home.py sabine-schwarz --service "Heilpraktikerin für Psychotherapie"`, 3 s wall time (script reports 2.8 s).

What I had to fix by hand in draft/index.html:
1. **Wrong logo.** logo.png was Logo_Verband.png, the VFP membership seal. Her site has no logo image, only the text brand "Psychotherapie Sasch" (green "Sasch"). Replaced with that text brand. File removed.
2. **Wrong second photo.** praxis.jpg was Paar1_Sasch.jpg, a love-lock on a bridge in Würzburg (decorative, not her room). Removed. The room photo with her (HeroSectionSASCH2.jpeg) is now the main hero image.
3. **Portrait card used the room photo.** A full-room photo does not work as a 56 px face. New badge.jpg = face crop from Brett_SASCH.jpeg (her real photo, from her site).
4. **Phone format.** "+4915112489890" in the top bar and the trust row. Changed to her imprint format, "0151 124 8989 0".
5. **City.** Script used only "Coburg" and "mit eigener Praxis in Coburg". Her own practice is in Ahorn-Schorkendorf, Coburg is Studio FRIEDA, Zinkenwehr 5 (Thursday 9-18 Uhr). H1 now "in Coburg und Ahorn", trust card "2 Praxisorte".
6. **Sub-headline.** "Sie suchen eine Heilpraktikerin für Psychotherapie in Coburg? Ich nehme mir Zeit …" repeated the H1. Rewritten: situation (Krise, allein oder als Paar) + 3 helps + 3 places (Ahorn, Coburg, online).
7. **Nav.** "Alternativmedizin" removed (HWG risk, not the main offer). "Preise" added (her real nav item). "Online-Paartherapie" shortened to "Paartherapie".
8. **CTA and reassurance.** "Ersttermin vereinbaren" / "Termin vereinbaren" → "Kostenloses Erstgespräch buchen" / "Erstgespräch buchen", from her real booking offer (15 Min., kostenlos). Note line now has facts. Ghost button "Leistungen ansehen" → "Angebote ansehen" (her menu word).
9. **No stars.** The script had no rating. Added "5,0 bei Google · 15 Bewertungen" from evidence/google-panel-2026-10-12.md.
10. **Trust row.** 3 cards, one repeated the eyebrow. Replaced by 4 cards with facts: Erlaubnis seit 2019 (imprint), 2 Praxisorte, Mitglied im VFP e.V. und Heilnetz e.V., Telefon.
11. **Colours and font.** Script cream #edf2ee and Fraunces serif. Changed to her site: Poppins, sand #f6f3ed, line #e9e4da, ink #333333. Green #4a7c59 kept.
12. **Layout at 1440.** Nav items and the header button wrapped to two lines. Fixed with nowrap, a header gap and a smaller nav gap.

Checks passed: form of address "Sie" (her site uses "Sie"). No healing or success promise in the draft. No "Psychotherapeutin". No skip link or info page in nav, eyebrow or trust row.

Strip photos (all from therapie-sasch.com, opened and checked):
- foto-1 = HeroSectionSASCH2.jpeg, her in the practice room (1200 px).
- foto-2 = Brett_SASCH.jpeg, her portrait with the systemic board (1000 px).
- foto-3 = praxis_header.jpeg, her hands writing notes in a session (1000 px).
Not used: Rutengehen and Reiki photos (alternative methods, HWG risk next to psychotherapy), Paar1/Paar2 (love-locks, not her).
