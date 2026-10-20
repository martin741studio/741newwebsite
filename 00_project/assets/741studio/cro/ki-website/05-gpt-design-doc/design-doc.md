# Design-Doc — 741 KI-Website (Landingpage)

Stand 2026-10-13. Eingaben: `04-copy/approved-copy.md`, `02-data/brand.md`, Muster aus `03-diagnosis/diagnosis.md` (P0-Blueprint, Hero nach P9 und der 741-Live-Startseite).

## 1. Globaler Style-Block
GLOBAL STYLE: Design one complete, tall desktop landing page (1440 px wide layout, shown as one tall portrait image) for the German agency 741.Studio, product '741 KI-CMS'. Brand: exactly like the attached 741.studio homepage screenshot. Fonts: DM Sans (headings semibold 600, body regular), one accent phrase per main headline in Fraunces italic serif. Colours: ink #1c1c1a for headings, dark green-anthracite #1f2a22 for the ONE primary CTA colour (pill buttons, radius 100 px, white text, small arrow), lemon yellow #fac118 only as accent (small pill badges, thin underlines, number badges, icons), warm cream hero background gradient #fbfaf7 to #f6f4ee with a soft lemon radial glow top right, other sections alternate white, very light cream and one or two dark green-anthracite bands; green #16a34a only for positive numbers. Mood: clear, confident, warm, technical but never cold, honest. Large radii 16 to 24 px on cards, soft long shadows, generous white space, 8 pt spacing, thin light dividers. Imagery: real screenshots in device mockups (laptop) with floating white proof cards, no stock people. The attached file '741 logo' is the real brand logo, reproduce this exact logo top left in the header and in the footer, do not invent a different logo. The attached Praxis Hüwel website screenshots are the REAL product: show them inside a modern laptop mockup in the hero and as two smaller browser frames in the case study section. The attached photo of Martin Drendel (black shirt, cap, mountain) is the real founder: use his likeness in the person section. Header: real 741 logo left, simple navigation right, one lemon button top right. Footer: dark, logo, small links. Use the exact German texts below (they are final copy), in this order, each section clearly separated. Body text at least 16 px. Only one CTA colour on the whole page. 

## 2. Prompt pro Abschnitt
- **S01:** Section 1 Hero, two columns: left text column with a small lemon pill badge above the headline, H1 large in two to three lines with the words 'per Chat geändert' in Fraunces italic, answer paragraph, then a dark pill CTA plus beside it a small text link, the reassurance line in small grey and three check items with lemon check icons below. Right column: a laptop mockup showing the attached real Praxis Hüwel homepage screenshot, with two floating white cards overlapping the laptop edge: one stat card with a big '1,3 Sekunden' number, one small card with a green check icon. Texts:
- **S02:** Section 2 Proof strip directly under the hero: white band, four stat items in one row, each a big number with a short line, small lemon line above each. Texts:
- **S03:** Section 3 situations: light cream background, headline left, four situation rows as soft white cards with small line icons, then the explanation paragraph and the dark pill CTA with the reassurance line. Texts:
- **S04:** Section 4 package: white background, headline centered, five cards in a grid (3 plus 2), each with a lemon line icon, a bold card title and the text; inline links underlined. Texts:
- **S05:** Section 5 steps: light cream background, four numbered steps in one horizontal row connected by a thin line, number badges in lemon, bold step title then text, dark pill CTA and reassurance line under the steps. Texts:
- **S06:** Section 6 person: dark green-anthracite band, real founder photo left in a large rounded frame, text right in white, CTA as light pill on the dark band. Texts:
- **S07:** Section 7 case study: white background, headline, short paragraph, two browser-frame screenshots of the real Praxis Hüwel site side by side, a clean two-column before/after table with 'Vorher' and 'Heute' columns, an empty quote card with a dashed border as placeholder for a client quote, the link and the CTA. Texts:
- **S08:** Section 8 deep-dive: light cream background, headline, seven accordion rows; the first row is open and shows its full text, the row 'Was laufend kostet' shows a small clean cost table. Texts:
- **S09:** Section 9 FAQ: white background, headline, ten accordion questions, the first one open with its answer. Texts:
- **S10:** Section 10 help band: very light lemon tint background, centered headline and paragraph with an underlined link. Texts:
- **S11:** Section 11 closer: dark green-anthracite band, mini hero centered: headline in white, three check items with lemon checks, one proof line, a large light pill CTA and the reassurance line. Texts:

## 3. Ganzseiten-Prompt
`05-gpt-design-doc/prompt.txt` (ein Block, alle Texte wörtlich aus der freigegebenen Copy; geprüft mit check_prompt.py).

## 4. Bildregel
Echte Bilder sind die Referenz: 741-Logo (`01-input/logo-741-black.png`), echte Hüwel-Screenshots (`01-input/huewel-*.png`), Martins Foto (`01-input/martin-drendel-founder.jpg`), Stil-Referenz `02-data/741-de-home-1440-first.png`. GPT zeichnet keine eigenen Logos und keine Stock-Personen. Text im Bild ist nur Platzhalter; `approved-copy.md` bleibt die Quelle.

## 5. Anhänge für ChatGPT
1. `01-input/logo-741-black.png` (echtes Logo)
2. `02-data/741-de-home-1440-first.png` (Marke und Hero-Muster der Live-Seite)
3. `01-input/huewel-home-1440-first.png` (echtes Produkt, Laptop im Hero)
4. `01-input/huewel-ueber-mich-1440-first.png` (zweiter Screen fürs Fallbeispiel)
5. `01-input/martin-drendel-founder.jpg` (Gründer)
