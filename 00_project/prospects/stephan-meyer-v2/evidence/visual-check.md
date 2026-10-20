# Visual check: stephan-meyer-v2

URL: http://localhost:3000/review/stephan-meyer-v2/
Start 15:24:29, end 15:28 (agent G). Date 2026-10-12.

## Files
- evidence/page-desktop-1500.jpg (full page, 1500 x 14520, headless Chrome, PIL q80)
- evidence/page-mobile-375.jpg (3 iframes 375 px: top, #maps-scan, #telefon-klingeln; first 801 px of each)

## Desktop 1500 (8 crops read)
Hero H1: 39.3 px at 1512 px viewport (brief: about 37 px). Button "Zeig mir meinen Markt" at y 632 to 680, inside the first 757 px. PASS.
No broken image. All maps, photos, strips, Martin figures, case avatars and the YouTube thumbnail load.
Slider numbers checked against the script: 210 / 20 % / 150 EUR / 6,90 EUR / 4 % / 40 % / 1.500 EUR give 64 visitors, 2,5 requests, 1 customer, 18.357 EUR per year, split 66/34, 431 EUR per customer. All correct.
Numbers in the page agree with each other (0 of 49 points, 15/44, 2.166 vs 1.616 words, 63/1139, 91,8 %).

### Problems (desktop)
1. Hero, video box: shows only the play icon and "Dein persönliches Video folgt in Kürze". This is an empty slot until the Loom is added.
2. Header banner (site component, above the page): "Benötigen Sie Hilfe beim Entfernen unerwünschter Bewertungen aus Ihren Konten? Wir können Helfen Sie!" Wrong topic for a coach and a grammar error. It is not part of the prospect page.
3. Tight line-height (lines touch or overlap), cosmetic:
   - section "Selbst bei business coach jena": sub paragraph under the H2.
   - section "Wachstums-Rechner": small source paragraph ("Echte Google-Suchen ...", 12,5 px).
   - sections "Der Website-Check", "Sofort-Maßnahmen", "Priorisierter Plan": H2 lines and the `<p>` below have no line-height and no margin.
   - closing black CTA ("Wenn du magst: 30 Minuten ..."): H2 lines overlap, the `<p>` below is tight.
4. Calculator, right card (.wr-card with justify-content:center): about 130 px blank space above and below the 4 KPI tiles, because the left card is taller. By design, but it looks empty.
5. Dark "Vorher aufräumen" cards: automatic hyphenation ("Ca-sino", "ers-ten", "ma-nagement"). Cosmetic.
6. Footer (site component) renders grey with a large "Results Driven + Human Creativity" and a yellow shape. The cookie banner covers the lower right. Site-wide, not page-specific.

## Mobile 375 (Chrome, 3 iframes, images eager)
- scrollWidth = 375 = iframe width in all 3 frames. No horizontal page scroll. PASS.
- H1: 20.3 px, body 16 px. H1 is only 1.27 x body, small for a hero. The first sub text is about 14,85 px. The `.audit-subheadline` paragraph ("Du hast eine Promotion ...") is 12,32 px with !important, smaller than the text above it and below 14 px.
- Broken images: 0 of 35. Only the empty .rvw-lb image (fine).
- Badge "PRIVATE WEBSITE- & SICHTBARKEITS-ANALYSE": top y 112, fixed menu bottom y 100. 12 px clearance. PASS. #maps-scan and #telefon-klingeln headings stay below the fixed menu (heading at about y 148 and y 238).
- Elements wider than the viewport, outside scroll wrappers: only DIV.footer-social-links (right edge 497). Its 4 icons end at x 190, so nothing is cut. Body and html have overflow-x hidden.
- Tables in horizontal scroll wrappers: `.sys-table` (Anbieter table, "Schritt 2") shows 338 of 640 px. Only the columns "Anbieter" and "So ordnet Google sie ein" are visible. The columns "Google-Bewertungen" and "Oben in der Karte" need a swipe, and no hint is visible. `.audit-table` (8-week plan) scrolls the same way (right edge 680 px). Medium: the key numbers (0 / 39 / 91,8 %) are hidden on a phone.
- Header banner text (3 lines in a 40 px bar) is cut at the top edge on mobile. Site component.

## Verdict
No blocker. Fix before send: problem 1 (video slot), problem 2 (header banner text, if Martin can change it), mobile `.sys-table` columns, mobile sub text 12,32 px. The rest is cosmetic.
