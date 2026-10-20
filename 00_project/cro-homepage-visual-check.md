# CRO Homepage: Visual Check (mandatory gate before Checkpoint 2)

Added 2026-10-11 on Martin's instruction. Used by Step 6b of `00_project/cro-homepage-workflow.md`.

**Rule:** the agent never reports "prototype done" until it has opened the prototype in Claude in Chrome (the external Chrome, never the built-in browser pane), scrolled it from top to bottom, and checked every item below with its own eyes. Headless screenshots and code reading do not replace this. A check that was not done is written as "not checked", never as "ok".

Result file: `07-prototype/visual-check.md`. One row per item: section, item, result (ok / fixed / open), evidence (screenshot name or measured value), what was fixed. Items found wrong are fixed and checked again. Only then the agent reports.

## 0. Setup

1. Serve the prototype folder over HTTP (`python3 -m http.server <free port>`, check the port with `curl` first). Open it in Claude in Chrome in a new tab.
2. Set the window to 1440×900 with `resize_window`. Confirm with `window.innerWidth`. If Chrome gives less (1430 on Martin's Mac), write the real width in the result file.
   Use `scrollTo({top, behavior:'instant'})` for measuring, because the page's smooth scrolling makes position reads too early. After changing an image file, hard-reload it (`fetch(url,{cache:'reload'})`, then reload the page). Chrome can show the old file.
3. Load the page fresh. Wait 2 seconds. Do not use `?shot=1` for this check, because the check must show the real reveal behaviour.
4. Have the approved copy (`04-copy/approved-copy.md`), the final mockup (`06-gpt-assets/`) and `SLOTS.md` open for comparison.

## 1. Measured checks (run with `javascript_tool`, write the numbers down)

Tool (2026-10-11): `~/.claude/skills/cro-homepage/scripts/measure.js` runs M1 to M10 in one paste and returns JSON. `scripts/verify.py <cro-dir>` covers M11, the required files and the report line. The script result does not replace looking at the page.

| # | Check | Pass rule |
| --- | --- | --- |
| M1 | `innerWidth` | 1440 |
| M2 | Horizontal scroll: `scrollWidth <= innerWidth` | true |
| M3 | Console errors and failed network requests (`read_console_messages`, `read_network_requests`) | none |
| M4 | Every `<img>`: loaded, and `naturalWidth >= clientWidth` (target 1.5 times) | none broken, none upscaled |
| M4b | Image distortion: for every `<img>` without `object-fit: cover`, rendered width/height equals natural width/height within 2 percent. (A fixed `height` attribute with `width:100%` in CSS stretches the picture. Always set `height:auto` as well.) | none distorted |
| M5 | Web fonts loaded: `document.fonts.check` for both families | true |
| M6 | Every `href`: booking link is the real URL, `tel:` links match the NAP, anchors point to an existing id, no `#` placeholder except those listed as open | list the exceptions |
| M7 | All `.rv` elements become visible after one top-to-bottom scroll | 0 stay hidden |
| M8 | Hero CTA bottom edge is above 900 px (first screen) | true |
| M9 | Text size (computed style scan of every text element): body text, menu, buttons, card text and footer at least 16 px. Source lines and captions at least 14 px. | none below the rule |
| M10 | Breathing animation only on the hero CTA and the closer CTA | exactly 2 |
| M11 | Text of every section equals the approved copy. Split the page text into segments and test each against the normalised copy file. | no difference, or every difference is listed with its reason |

## 2. Visual pass: how to scroll

Scroll in steps of about 700 px (one screen less a margin). Take a screenshot at every stop and a zoom into every image, card, button and edge. Wait 1 second after each scroll so reveals finish. For each stop, look at it like a visitor first, then like an editor with the mockup beside it. Run the pass twice: once scrolling down, once scrolling back up (nothing may re-animate, nothing may disappear).

## 3. Global visual items (look at every screen)

- G1 Alignment: left edges, column gutters and section padding follow one grid. No element sits 3 px off.
- G2 Spacing rhythm: section padding looks even. No section looks squeezed or empty.
- G3 Text: no cut-off words, no word broken mid-word, no orphan single word on a line in a headline, no text over a busy image part without enough contrast (look at the actual pixels).
- G4 Images: no blur, no halo at cutout edges, no hard edge that should be soft, no wrong content, no text or logo inside the picture, faces not distorted or badly cropped, same style across images.
- G5 Colour: one CTA colour only. Blur test: squint at the screen, the one primary action must still stand out. Purple, cream and olive match the brand file.
- G6 Typography: the two fonts only. Headline hierarchy is clear. Line length of body text under about 75 characters.
- G7 Buttons and links look clickable and have the same style in every section.
- G8 Compared with the mockup: section order, layout, proportions, colours. Every difference is written down and marked "intended" or "fix".
- G9 Hover: hover on the CTA, a card, a link and a nav item. The effect works and matches the motion spec. Nothing jumps.
- G10 Sticky header: it does not cover section headings after an anchor click. Click every menu item and check where it lands.

## 4. Per-section checks

### Header
- Logo is the real file, sharp, not stretched, links to the top.
- Menu items match the mockup, fit on one line, hover state works.
- Header stays at the top while scrolling and does not hide content.

### Section 1: Hero
- H1 is fully visible, not more than 4 to 5 lines, carries the keyword and the city.
- Sub-headline and CTA pair sit together; CTA and phone button are the same height.
- Reassurance line and rating line are readable and under the buttons.
- Portrait: sharp, face not cut, no cutout halo, the faded edge looks natural, the background plate does not make text hard to read.
- The next section's edge is visible, or the page clearly continues.
- First screen at 1440×900 shows headline, CTA and at least one proof element.

### Section 2: Proof strip
- Score, stars, Google logo, quote, link sit on one line and are vertically centred.
- Stars fill when the strip enters the view. The quote is one real review, with first name.

### Section 3: Themes
- All cards have equal height and equal spacing.
- Icons are sharp, equal size, with no box or off-white edge around them.
- No word is broken mid-word. Hyphenation is acceptable only at syllables.
- CTA below the cards is centred and visible.

### Section 4: Services
- Every card has an image, a heading, a link. Image crops show the subject, not an empty area.
- Image style is consistent. Real photos and generated photos do not clash in colour or light.
- Card heights are equal in a row. The hover zoom works and does not overflow the card.

### Section 5: First appointment (steps)
- Four steps, numbers, line between them. The line draws once from step 1 to step 4. Badges fill as the line reaches them.
- Step text is complete (duration, price). Heights and top edges are aligned.
- The note row (for example no home visits) is readable. The CTA below is visible.

### Section 6: About
- Portrait sits cleanly on the background, no halo, bottom edge flush with the band.
- Text column does not touch the decoration. Credential line is visible and underlines once.
- Decoration image blends into the band with no visible rectangle.
- Contrast of text on the photo background is enough everywhere.

### Section 7: Reviews
- Cards show stars, quote, first name, Google logo. No carousel. Equal heights.
- The count in the heading matches the Google profile. The link to the profile works.

### Section 8: FAQ
- Open every question: it opens and closes smoothly, only one is open at a time, the chevron turns.
- Answers equal the approved copy. A placeholder answer carries a visible `[FEHLT]` flag.

### Section 9: Location
- Map loads and the pin is on the right spot. Address, transit, car and hours rows have matching icons.
- Address, phone and hours equal the NAP in the dataset.
- Booking button is visible.

### Section 10: Closer
- Headline, reassurance items, CTA pair. Decorations at both sides do not touch the text.
- The CTA breathes slowly and stops on hover.

### Footer
- Address, phone, email correct. Legal links present (placeholder allowed only if listed as open).

## 5. Interaction checks

- Click the booking CTA in three sections: each opens the real booking URL in a new tab (do not submit anything).
- Click the phone button: the `tel:` link is correct.
- Click each menu item and each "Mehr erfahren": lands where expected or is listed as an open placeholder.

## 6. Output and reporting

1. Write `07-prototype/visual-check.md` (German) with the result table, the list of fixes made, and the list of items still open.
2. Save the screenshots of the final state in `07-prototype/screenshots/`.
3. In the report to Martin, state: "Visual check done in Chrome, N items checked, N fixed, N open", and name the open items. Never write "done" without this line.
