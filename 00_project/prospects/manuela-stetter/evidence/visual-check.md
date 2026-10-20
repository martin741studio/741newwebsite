# Visual check agent G - manuela-stetter (14.10.2026, 14:26:43 to 14:28:26)

Source: http://localhost:3000/review/manuela-stetter/ (vite dev). Desktop: headless Chrome 1500 px, screenshot page-desktop-1500.jpg (cut at 14000 px; page is 14320 px, only the site footer is cut). Mobile: Chrome, three 375x812 iframes (top, #maps-scan, #telefon-klingeln).

## Desktop - result: no blocking problem
- Hero: H1 39.3 px at 1512 px width (limit 40 px, target about 37 px: slightly above target, inside limit). Button "Zeig mir meinen Markt" ends at y=544 px (inside 757 px).
- Hero video slot: placeholder text "Dein persönliches Video folgt in Kürze" (empty slot by design, until the Loom is added).
- Maps scan: left map has 49 points, real tiles loaded. Values 20+, 19, 18, 15, 12, 6, 6, 19 match the text (7 points under the first 20, 0 in the top three). Right grid shows the target scenario, 49 points.
- Counts agree on the page: 0 von 49, 7 von 49, 12 von 44, 39 Bewertungen, 320 Suchen.
- Case cards (4 avatars), Martin block (photo, 10+, 250+), all character images: loaded, no broken image.
- Search bars, 6 content cards, competitor table, 4 black cards, today/target screenshots, 5-second test: no cut text, no empty slot.
- Calculator: slider values 320 / 20 % / 150 € / 1 € / 4 % / 40 % / 300 € give 214 Besucher, 8,6 Anfragen, 3,4 Patientinnen, 12.326 Euro, 30/70 split, 62 Euro per Patientin. Numbers add up.
- Website check accordion (4 areas, 17 points), 6 quick steps, 8-week plan, Ausgangslage, YouTube video, closing CTA: render correct.

Minor (no fix needed):
- Calculator result card: about 120 px empty space above the four number tiles (content centered).
- Tight line height (about 1.0 to 1.1) in: maps-scan intro paragraph, "Wer in der Google-Karte ..." line, calculator source line (small), "Sechs Schritte" card texts and the subtitles of the last three section headings. Readable, but cramped.
- "Heute" screenshot in step 3 is cropped at the bottom (intended preview crop, "Zum Vergrößern antippen").
- Cookie banner overlaps the site footer in the screenshot (site element, not page content).

## Mobile 375 px - result: ok
| Check | top | #maps-scan | #telefon-klingeln |
|---|---|---|---|
| Iframe client width | 358 | 358 | 358 |
| documentElement.scrollWidth | 358 | 358 | 358 |
| Broken images | 0 | 0 | 0 |
| H1 / body font | 20.3 px / 16 px | same | same |

- No horizontal page scroll. Elements wider than the viewport: only .sys-table (inside .sys-table-wrap, overflow-x auto, scrolls inside the card), hidden nav links and .footer-social-links (site footer, clipped, does not widen the page). No page-section element is too wide.
- H2 on mobile: 22 px. H1 is 20.3 px, smaller than the H2 (22 px) and only 4 px above body text. Note: H1 is smaller than H2 on mobile. Check the size rule if you want H1 > H2.
- Text under 12 px on mobile: pills (11.5 px), table cells in competitor table (11.2 px), hero-card-sub (10.9 px), pill-critical (10.5 px), audit-eyebrow (9.8 px), heading-style-xl in two places (10.1 px, site footer). Footer / cookie texts are 5 to 6 px (fluid root, site chrome).
- Top banner on mobile wraps to 4 lines over the header (site element).

## Problems (summary)
1. Mobile H1 (20.3 px) is smaller than H2 (22 px): hero h1 on 375 px.
2. Hero H1 on desktop 39.3 px (target about 37 px, limit 40 px): ok but above target.
3. Mobile text under 12 px: .pn-pill, .sys-table td, .hero-card-sub, .pill-critical, .audit-eyebrow.
4. Calculator result card: empty space at the top (desktop). Tight line height in maps-scan intro and "Sechs Schritte" cards.
Nothing blocking: no wrong slider number, no empty slot (except the planned video), no broken image, no horizontal overflow.
