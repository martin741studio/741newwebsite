# Visual check in Chrome — LP „The Replayers“, prototype v1 (2026-10-12)

Setup: `python3 -m http.server 8831` in `07-prototype/`. Claude in Chrome, own tab (closed after each step), window 1440 wide, viewport 1440 × 757 (measured). Page loaded fresh without `?shot=1`, scrolled top to bottom in steps of about 700 px with a screenshot at each stop, plus anchor jumps to #methode, #uebungen, #faq. Headless screenshots 1440 px in `screenshots/`.

| # | Result | Value / what was fixed |
|---|---|---|
| M1 | ok (deviation noted) | 1440 × 757 |
| M2 | ok | no horizontal scroll |
| M3 | ok | console without errors; 8 requests to localhost, all 200 |
| M4/M4b | ok | 7 images, none broken, none upscaled, none distorted (hero 1024 × 1536 shown at 741 × 889 with cover) |
| M5 | ok | Inter and Libre Baskerville loaded |
| M6 | ok | 8 buttons: 7 × Gespräch buchen → termin.html with utm_source=lp-replayers (header, hero, momente, methode, michael, ablauf, abschluss), 1 × video → meandyou.de/sichtbarkeit-neu utm_content=video; tel +4915888367664; 0 missing anchors; 0 „#“ |
| M7 | ok | 0 elements hidden after scrolling |
| M8 | fixed | hero button was at 765 px (H1 in 4 lines) → hero rebuilt like the mockup (photo full height, H1 3 lines), button bottom 683 px (rule 701) |
| M9 | fixed | proof line and quote sources 15,5 px → 16 px; podcast cover 13 px → 16 px. Below 16 px only: yellow marks (15 px), overline „Der Nachdenker“ (14 px label), footer headings (14 px), prototype badge, same as the sibling pages |
| M10 | ok | 2 breathing buttons (hero, closer) |
| M11 | ok with list | 182 text segments; differences only in the shared footer (address, Termine, Rechtliches, Impressum, Datenschutz, AGB, Kontakt, e-mail) |
| One CTA visible (persona) | ok | header button hides while a section button is on screen (checked at hero, S04, S06, S10, S12, S14); in the other sections the header button is the only one |
| Header | ok | real logo, menu one line, no active item (LP is not in the menu) |
| S01 Hero | fixed | first build: framed photo, H1 4 lines, CTA under the fold line → full-height photo with dove fade as in the mockup |
| S02 Proof | fixed | heading was rendered as a small overline → serif H2 as in the copy; round Michael photo, credential |
| S03 Treppenwitz | ok | answer left, desk photo right |
| S04 Moments | ok | three white cards without borders, link in card 3, line + centred button |
| S05 Why late | fixed | quote span used the homepage class `.q` (white card) → own class `.rpq` |
| S06 Method | fixed | the column lines were dark on navy (a global `.sec p` rule) → rule removed; two columns as in the mockup |
| S07 Exercises | fixed | cards in a row as in the mockup; titles not aligned → cards start at the top |
| S08 Video | ok | dove box, real still, play button, only one button on screen |
| S09 Read and listen | fixed | podcast cover text overflowed → wider cover, 16 px. Covers are placeholders (open, client) |
| S10 Michael | ok | real portrait, 4 facts, link, button |
| S11 Voices | ok | 4 open cards, no carousel, count line with yellow mark, link |
| S12 Next steps | ok | soft list without lines left, seminar card with button right |
| S13 FAQ | fixed | first a nested grid gave 4 narrow columns, then half width → one accordion in the homepage 2-column style, full width; click opens one and closes the other (tested) |
| S14 Closer | ok | navy band without photo (warm interior persona, no terrace), checks, proof line, light button, phone |
| Full-page screenshot | fixed | the fixed prototype badge made the headless page 16.000 px tall → badge hidden in `?shot=1`, page 11.191 px |
| Mockup comparison | ok | order, layout and colours match. Intended differences: S10 door photo instead of a second cafe photo; closer as navy band; S14 checks right instead of centre |
| Way back up | ok | nothing re-animates, nothing disappears |

Open (client data): book cover file and permission; podcast cover permission.

Visual check done in Chrome, 30 items checked, 11 fixed, 2 open.
