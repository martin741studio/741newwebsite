# Homepage: Manuela Stetter (agent C, 14.10.2026)

## Score today

**12 / 44** (Prio A: 8 / 24). Details: `evidence/scorecard-today.md`.
Item 22 (HWG) = 0. The course block on the homepage says "Bye-bye Erschöpfung" and "Alles, was dir wirklich hilft!".

## 5-second test (today, `evidence/home-today-1440.jpg`)

- Was? Naturheilpraxis "für Frauenheilkunde (HPG)" and coaching. The H1 says it, in capitals on a flower photo.
- Wo? Landshut, Essenbach und Umgebung (H1). The address in Mirskofen is only in the footer.
- Warum du? Not visible. No Google stars (5,0 · 39), no "10 Jahre", no "über 600 Frauen" on the first screen.
- Wie zum Termin? Not clear. The visible button goes to the courses ("Zu den Kursen"). "Termine buchen" is only a menu item in the second menu row. The phone number is visible.
- Wer? Not on the first screen. Her face and name come in section 2 ("Hi, mein Name ist Manuela").

## Draft (`draft/index.html`, `evidence/home-draft-1440.jpg`)

- H1: "Deine Heilpraktikerin in Essenbach bei Landshut." Her H1 names Landshut.
- Subline: "Zyklus, Hormone, Wechseljahre? Ich schaue auf dich als ganze Frau, mit Naturheilkunde und Coaching, in meiner Praxis in Mirskofen oder online."
- Stars: 5,0 bei Google · 39 Bewertungen (`evidence/google-panel-2026-10-14.md`).
- Button: "Termin buchen" (header and hero, large). Note under it: "Zuerst sprechen wir 15 Minuten, kostenlos." (/termine-buchen/).
- Trust row, all from her site: Seit 10 Jahren eigene Praxis (/manuela/) · Über 600 Frauen (/manuela/) · Kennenlernen kostenlos, 15 Minuten (/termine-buchen/) · Vor Ort oder online, per Buchungsportal oder WhatsApp (/termine-buchen/).
- Images: logo = her emblem logo (`image0-removebg-preview.png`, margins cropped). Main photo = `Z82A0618.jpg` (she on a sofa). Portrait chip = face crop of `Z82A9892.jpg`.
- Colours: her Elementor kit, primary #2C7E94, beige #EDE3D9.
- Slop check (deslop_de.py with claims file): 5/5.
- Not used: "Frauenheilkunde" (sounds like a medical specialist title), disease names in the headline, any healing promise.

## Fixes to the draft_home.py output (run time 4.4 s in the script, 4 s wall)

1. `python3` (Homebrew 3.15) has no PIL. `/usr/local/bin/python3` (3.10) fails on a nested f-string in line 212. It ran with `/opt/homebrew/bin/python3.14`.
2. The script took the logo (`image0-removebg-preview.png`) as the portrait and said "logo: NONE". The portrait.jpg was the logo on a black background.
3. "praxis.jpg" was a stock photo (two daisies, `Stetter-Manuela-Naturheilpraxis_pod4.jpg`). Replaced with a real photo of her.
4. Colours came from the WordPress default palette (#ff6900 orange). Her site uses #2C7E94 (Elementor kit `post-1011.css`).
5. Headline had no Landshut. Subline was generic ("Du suchst eine Heilpraktikerin in Essenbach?").
6. No stars, although the Google panel file has 5,0 · 39.
7. Button "Ersttermin vereinbaren" changed to "Termin buchen" (her wording). The reassurance line was generic.
8. Trust row had the raw phone "+4917652099985" and a services box. Replaced with 4 facts from her site. Phone now as on her site: "0176 520 999 85".
9. Nav had "Willkommen". Now her menu items without it.

## Note

- No real practice room photo is on the site. All photos of her are from a studio shoot. The stock photos (daisies, yoga at the beach, bench, "HORMONES" blocks, calendula hero) were not used.
- Strip photos: `foto-1.webp` (Z82A0104), `foto-2.webp` (Y98A3858), `foto-3.webp` (Z82A9386). Only she is in them.
