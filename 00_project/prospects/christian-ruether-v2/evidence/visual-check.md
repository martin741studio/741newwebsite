# Visual check: christian-ruether-v2

Page: http://localhost:3000/review/christian-ruether-v2/
Run: 10:14:35 to 10:17 (Oct 12 2026)
Files: page-desktop-1500.jpg (headless Chrome, 1500 px wide, first 13200 px of 13430 px), page-mobile-375.jpg (three iframes 375x812: top, #maps-scan, #telefon-klingeln)

## Desktop 1500 px, findings per section

Note: the screenshot cuts off the last 230 px of the footer. The cookie banner and the pixel dog are sitewide parts, not page content.

| Section | Result |
|---|---|
| Hero (H1, lead, CTA, Martin bubble) | OK. H1 breaks in 5 lines, no cut text. Video slot shows the placeholder text "Dein persoenliches Video folgt in Kuerze" (intended). Gap of about 100 px between lead text and CTA button. |
| Maps scan (HEUTE 49 x "20+" vs. ZIEL grid) | OK. Both grids show 7 x 7 points, the map image loads. Label "Ziel-Szenario (Simulation)" is visible. |
| Proof wall (4 cases) | OK. 4 cards, 4 photos load. Values: Platz 18 -> 1, 0 -> 100 %, Platz 85 -> 1, -> Platz 1. |
| Three levers | OK. Numbers match the later sections (260, 0 von 49, 5 von 44). |
| Schritt 1 (search volumes, 966 / 0 / 700) | OK. Bars match the numbers. No empty slot. |
| 6 new contents | OK. 6 cards, no cut text. |
| Schritt 2 (competitor table) | OK. 5 rows, 0 % / 16,3 % / 12,2 % / 10,2 % / 10,2 %. |
| Change list, "Vorher aufraeumen" 4 tiles | OK. 47 / 319, 9 Treffer, 0, 1 Platzhalter. |
| Schritt 3 (Heute / So sollte es aussehen) | OK. Both screenshots load. 5 / 44 and Ziel: 36+ / 44. 5-second test shows 5 cards. |
| Wachstums-Rechner | OK. Sliders: 20 (min 20), 20 %, 150 EUR, 5,30 EUR, 4 %, 40 %, 1.200 EUR. Result 32 / 1,3 / 0,5 / 7.442 EUR / 12 % / 88 % / 331 EUR. I recomputed the numbers: they match. The right card is stretched and shows about 130 px empty space above and below the tiles (centered, not a missing element). |
| Website-Check accordion | OK. 4 panels, panel 1 open with 5 findings, "4 Bereiche - 17 Punkte". |
| Sofort-Massnahmen (6) | OK. Text lines in the cards are tight (line height small), no cut text. |
| 8-Wochen-Plan table | OK. 5 rows. |
| Ausgangslage (4 cards) | OK. |
| Closing CTA | OK. Both buttons visible. |

Minor, no fix needed: several sub-headlines sit very close under the H2 (Website-Check, Sofort-Massnahmen, Plan, hero video text). No broken images on desktop.

## Mobile 375 px (Claude in Chrome, iframe 375 wide, vertical scrollbar 15 px so layout width is 360)

| Measurement | Result |
|---|---|
| html.scrollWidth | 360 (inner width 375, scrollbar 15 px) = no horizontal page scroll. html and body have overflow-x hidden. |
| body.scrollWidth | 474, but it is clipped by overflow-x hidden. |
| Root font size | 6.75 px (fluid root) |
| H1 font size | 20.3 px |
| Hero lead line (large) | about 24 px visually |
| Hero body paragraph | 12.32 px |
| Body font size | 16 px (body element, content uses rem) |
| Broken images | 0 of 23. Only the empty image in .rvw-lb (allowed). |
| Fixed header | Banner 0-52 px, menu bar "START NOW" 52-100 px. |
| Hero badge | Sits fully under the fixed menu in the screenshot (badge at y 148, menu ends at 110). |
| #maps-scan anchor | Heading visible below the header (label at y 162). |
| #telefon-klingeln anchor | Heading visible below the header (label at y 259). |
| 8-week plan table, competitor table, audit table | Inside overflow-x auto wrappers (324 px wide, content 718 px / 679 px) = scroll inside the card, page does not scroll. The last columns are cut at the edge by design. |

### Problem found (mobile)

1. Section #telefon-klingeln, block "Vorher aufraeumen" (.sys-stats): the right column of the 2 x 2 grid is 20 px too wide. Cards 2 and 4 end at x = 380, the visible width is 360. The right edge of the cards ("9 Treffer", "1 Platzhalter") is cut off, and the word "Platzhalter" touches the edge. Grid columns are 154.5 px + 193.6 px. Cause: the long word "Platzhalter" forces the column to grow (grid min-content). Fix idea: `grid-template-columns: repeat(2, minmax(0, 1fr))` plus `overflow-wrap: anywhere` or a smaller font for the number on mobile.

### Minor (mobile)

- Hero body paragraph (12.3 px) is clearly smaller than the lead line above it. It is readable but small.
- No other overflow found.
