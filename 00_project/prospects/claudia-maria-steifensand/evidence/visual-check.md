# Visual check, claudia-maria-steifensand (agent G)

Run: 12:58:14 to 13:01:26, 13.10.2026.
Note: nothing listened on port 3000 at the start. I started `npm run dev` (vite) myself. A plain static server shows `{{> header_de}}` and broken images, so the vite server is needed.

## Desktop (1500 px, headless Chrome)
File: evidence/page-desktop-1500.jpg (page height 14171 px, the screenshot covers the first 14000 px).
- H1 = 37.44 px. Body = 16 px. Button "Zeig mir meinen Markt" at y 470 to 518, inside 757 px. OK.
- Broken images: none. Only the empty .rvw-lb image (invisible) fails. OK.
- Hero: video slot shows "Dein persoenliches Video folgt in Kuerze" (placeholder, as intended). Martin figure and speech bubble load.
- Scan map: real map with 49 points. Slider numbers match the text: 2 points on Platz 1, 4 points on Platz 4 (NW). Ziel grid loads.
- Numbers checked: 45 of 49, 13 / 44, 172 words, 564 / 324, table 91,8 / 100 / 98 / 8,2 / 2 %. Calculator: 19 visitors, 0,7 requests, 0,3 families, 5.346 EUR. The result follows from the 10,30 EUR click price in the note. The slider label shows "10 EUR".
- Images: Trauerhalle (chairs, coffin, urns), house facade, rose photo. All fit a funeral home. No inappropriate image.
- Empty slots: none.

## Problems (desktop)
1. Section "Wachstums-Rechner", right card: about 110 px of empty space above and below the 4 result tiles (the content sits in the middle of a 560 px card). Minor.
2. Section "Website-Check" and "Sechs Schritte" and "Plan": the line under the H2 sits tight (line height too small, about 1.0). Minor.
3. Hero: the badge sits directly under the fixed menu (y 80 to 112 against menu bottom 80). It does not overlap. OK.
4. Headless screenshot shows the cookie banner at the bottom right. It is a screenshot artefact, not a page error.

## Mobile (375 px iframes in Chrome, usable width 360 px)
File: evidence/page-mobile-375.jpg (5 stacked views: hero, maps-scan, Schritt 2 table, cs-top-proof, sys-intro, sys-stats, rechner, check, Schritt 3, plan, video).
- scrollWidth of the document = 360 = client width (all 3 iframes). OK. body.scrollWidth = 474 comes from `.footer-social-links` (site chrome, clipped). No page element is wider than the viewport (0 hits outside header, footer, menu, cookie).
- H1 = 20.3 px, body = 16 px. H1 is only 1.27 times the body size. Readable, but small.
- Badge under the fixed menu: visible at scroll 0, not hidden. #maps-scan and #telefon-klingeln: heading about 100 px below the top, not hidden under the menu (92 px fixed bar). OK.
- Broken images: none (only the empty .rvw-lb).
- .sys-stats: 2 x 2 cards, x 18 to 173 and 187 to 342. No overflow.

## Problems (mobile)
1. `.sys-stats` card 3: "2 Eintraege" breaks inside the word ("Eintraeg / e"). Cause: big number font in a 155 px card. Fix: smaller font or `overflow-wrap:normal` with `hyphens`, or the text "2 Listings".
2. `.sys-table-wrap` (Bestatter table, Schritt 2): table is 640 px wide in a 324 px wrapper (overflow auto). Columns "Google-Bewertungen" and "Oben in der Karte" are off screen. No visible hint to scroll (a thin scrollbar only). Important numbers (91,8 %, 100 %) are hidden. Fix: card layout on mobile or a "wischen" hint.
3. Rechner result tile "5.346 EUR": the euro sign wraps to a second line. Minor.
4. "Wer dahintersteht" card: the avatar sits at the bottom left with empty space above, text is pushed right. Minor.
5. Anchor name #telefon-klingeln points to Schritt 2 (Google-Karte / Vorher aufraeumen). The name does not match the content. Cosmetic.
