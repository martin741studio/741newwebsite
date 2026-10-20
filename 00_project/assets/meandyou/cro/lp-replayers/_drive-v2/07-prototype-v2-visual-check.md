# Visual check in Chrome — LP „The Replayers“, prototype v2 community version (2026-10-12)

Setup: server `python3 -m http.server 8831` in `07-prototype/` (v2 at `/v2/index.html`). Claude in Chrome, own tab (closed after the check). Chrome kept the viewport at 1512 × 801 even after resize to 1440 × 900 (measured, noted). Page loaded fresh without `?shot=1`, scrolled top to bottom in 500 px steps, then each changed section opened by anchor. Unchanged sections (S02 to S07, S10, S11) were checked in v1 (`../visual-check.md`) and re-scanned in the headless screenshot.

| # | Result | Value / what was fixed |
|---|---|---|
| M1 | ok (deviation noted) | 1512 × 801 |
| M2 | ok | no horizontal scroll |
| M3 | ok | console without errors |
| M4/M4b | ok | 7 images, none broken, none upscaled; Skool cover 1084 × 576 shown at 510 × 271 |
| M5 | ok | Inter and Libre Baskerville |
| M6 | ok | 8 buttons, all „Community beitreten“ → www.skool.com/talk-to-me-9409/about, utm_source=lp-replayers, utm_content header, hero, momente, methode, community, michael, start, abschluss; data-event community_click. Cover image also links (community-bild). Footer link „Community Talk to ME“ (footer). Video only as text link in S09 (utm_content=video). 0 missing anchors (#faq, #community exist), 0 „#“ |
| M6b | ok | the page text contains no „Gespräch buchen“ (header, body, footer checked by script) |
| M7 | ok | 0 hidden after scroll |
| M8 | ok | hero button bottom 686 px |
| M9 | ok | below 16 px only: yellow marks (15 px), overline (14 px label), footer headings, prototype badge |
| M10 | ok | 2 breathing buttons (hero, closer) |
| M11 | ok with list | see verify.py: differences only in the shared footer |
| One CTA visible | ok | header button hides while a section button is on screen (hero, S04, S06, S08, S10, S12, S14), header shows „Community beitreten“ otherwise |
| S01 Hero | ok | price line with yellow mark under the button; proof line now „für Michael Ehlers … Seminarteilnehmer“ |
| S08 Community | ok | dove box, real Skool cover left, Skool review below, 5 check rows, button + price line with yellow mark |
| S09 | ok | heading „Zum Lesen, Hören und Zuschauen, ganz ohne Mitgliedschaft“, video as quiet text link with yellow mark |
| S12 Start | ok | 3 soft steps, side card with monthly/cancel line, seminar line, button |
| S13 FAQ | ok | 12 questions, 2 columns, click opens one and closes the other (tested on „Kann ich kündigen?“) |
| S14 Closer | fixed | price check row showed the yellow mark as raw text → rendered as badge |
| Way back up | ok | nothing re-animates |

Open (client data): price confirmation 39 € vs $44, live-call rhythm, cancellation rule, beginner fit, Skool cover permission, book cover.

Visual check done in Chrome, 22 items checked, 1 fixed, 6 open.
