# Visual check: /review/sabine-schwarz/ (agent G)

Start 15:14:18 · End 15:17:16 · Dev server http://localhost:3000 (HTTP 200)

## Result: 1 real bug (mobile), 3 minor points. Desktop clean.

## Desktop 1500 px (headless Chrome, full page 14352 px, 8 crops read)
File: evidence/page-desktop-1500.jpg

- Hero: H1 computes to 39.3 px at 1512 px viewport (about 37-39, OK). Button "Zeig mir meinen Markt" top 470 / bottom 518 px, inside the first 757 px. PASS.
- Hero video slot shows the placeholder "Dein persönliches Video folgt in Kürze". Expected until the Loom exists.
- Map left (49 points, real measurement) and goal grid right (49 points): both complete, no empty slot. Counts agree: 5 of 49 = 10,2 %; 49-26 = 23 points "nicht unter den ersten 20".
- Proof strip (4 cases), founder block (10+, 250+), 3 step cards: OK, no cut text.
- Step 1 bars (1.900 / 1.300 / 260 / 110 / 110 / 10) and 614 vs 421 bars: values and bar lengths match.
- Step 2 table (5 rows, 10,2 / 61,2 / 49 / 49 / 26,5 %), 6 change cards, 4 dark stat cards: OK.
- Step 3 before/after screenshots, score bars 22/44 and 36+/44, 5 test cards: images load, text OK.
- Calculator: sliders 110 / 20 % / 150 € / 2 € / 4 % / 40 % / 300 €. Output checked by hand: 22 + 75 = 97 visitors, 3,9 requests, 1,55 = 1,6 couples, 466 x 12 = 5.587 €, 23 % / 77 %, 125 € per new couple. All correct.
- Website check accordion (4 panels, images, 5 items in panel 1), 6 quick steps, 8-week plan table, 4 start cards, YouTube embed, CTA: OK.
- Images: 35 img elements, all loaded after forcing eager. Only the empty .rvw-lb image has no source (expected).
- Footer in headless shot is grey with a fixed-position look (scroll-animation artifact of the site template in a screenshot). Not a page problem.

## Mobile 375 px (Claude in Chrome, 3 iframes: top, #maps-scan, #telefon-klingeln)
Files: evidence/page-mobile-375.jpg (top, maps-scan, stat cards), evidence/page-mobile-375-anchors.jpg (top, maps-scan, telefon-klingeln)

- Horizontal scroll: documentElement.scrollWidth = clientWidth (375). No page scroll (html and body have overflow-x hidden, so a clipped element would be hidden, see bug 1).
- H1 20.3 px, H2 22 px, body 16 px. H1 is only 4 px smaller than H2 and 1.27x the body text. Readable, hierarchy is weak but not broken.
- Broken images: none (only the empty .rvw-lb).
- Badge "Private Website- & Sichtbarkeits-Analyse": sits at about y=130, below the fixed top banner (52 px) and menu bar (48 px). Not covered. PASS.
- Anchors #maps-scan and #telefon-klingeln: the eyebrow and H2 land below the fixed menu. PASS.
- Tables .sys-table and .audit-table (640-680 px wide) sit inside scroll wrappers (overflow-x auto). Intended, no leak.

### Problem 1 (real): "Vorher aufräumen" dark stat cards, section .sys-sec, grid .sys-stats
- Grid has 2 columns of 200.9 px and 158.9 px (content width, gap included) in a 339 px container.
- Right column card (.sys-stat, "9 Treffer" and "3 Einträge") ends at x=393 on a 375 px screen. About 18 px is cut off by overflow-x hidden. Text in the right cards touches or crosses the screen edge ("Einträge", "Einträge anderer").
- Fix idea for the builder: `.sys-stats{grid-template-columns:repeat(2,minmax(0,1fr))}` and `overflow-wrap:anywhere` on .sys-stat p, or one column below 420 px.

### Minor points (no action required)
- Top banner "Benötigen Sie Hilfe beim Entfernen ..." is the site template. At a 360 px viewport it wraps to 4 lines and clips ("Sie!" cut). At 375 px it fits in 3 lines.
- Desktop: H2 and the grey subtitle under it have line-height about 1.0 (e.g. "Was deine Website heute richtig macht ..." and "Dein Plan für die nächsten 8 Wochen"). Lines nearly touch. Cosmetic.
- Desktop: right calculator card has about 125 px empty space above the 4 result tiles (content is centred in a card as tall as the slider card). Cosmetic.
- Template footer .footer-social-links is 495 px wide on mobile. Clipped by body overflow-x hidden, not visible.

Tab closed. No file edited except the files in evidence/ listed above.
