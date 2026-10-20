# Handoff (page part) — LP „The Replayers“ (2026-10-12)

**Current version: v2 community (`07-prototype/v2/`).** Martin 2026-10-12: the page sells the community Talk to ME (Skool), no sales call. v1 (call version) stays in `07-prototype/` for reference. Points 1 to 8 below describe v1; the v2 changes follow at the end.

The main session writes the joint handoff. This is the page part.

1. Prototype: `07-prototype/index.html` (build `07-prototype/build.py`, imports rhetorik → michael → seminare → homepage). Design doc `05-gpt-design-doc/`, mockup `06-gpt-assets/full-page-v1-final.png`, images `06-gpt-assets/images/` + `SLOTS.md`.
2. Copy: `04-copy/approved-copy.md` (= `content-writing/lp-replayers/05-final/page.md`). Title „Schlagfertigkeit lernen: Wenn die Worte zu spät kommen“, meta in the frontmatter, H1 „Schlagfertigkeit lernen. Dir fehlen nicht die Worte. Sie kommen nur zu spät.“
3. URL: proposed `/schlagfertigkeit-lernen` (decision Martin, RP2). No old URL to redirect (v2 preview only).
4. Links to this page (none yet): homepage situation card 1 „Mehr dazu“, one text link from the rhetorik page and one from the FAQ answer „Ich bin introvertiert“ (RP11). Meta ads of the Replayers persona can point here.
5. Tracking: event `booking_click` on every termin link with `section` = utm_content (hero, momente, methode, michael, ablauf, abschluss, header); `video_click` on the /sichtbarkeit-neu link (video).
6. Prototype links point to the v2 preview (`termin.html`, `seminare.html` …) like the sibling prototypes. At integration: `/gespraech-buchen?utm_source=lp-replayers&utm_content=<section>`.
7. Persona rule built in: the header button hides while a section button is in view (JS at the end of `build.py`).
8. Shoot list: hero image is a generated persona (mood image). S03 reuses the homepage image `sit-replayers.webp`.

## [FEHLT] (yellow marks on the page)
1. Content, length (Wistia 29:39 min) and sign-in of the free video training.
2. Further exercises from Michael word for word.
3. Michael's own sentence on why the words come late.
4. Current title and source of „Nie wieder sprachlos!“ (new edition announced with a changed title), cover file and permission.
5. Name and role of the person in the call.
6. Seminar name of the Schlagfertigkeit format (working title Rhetorik II).
7. Consent to name the quoted participants.
8. Podcast cover permission (S09 placeholder).

## Before / after
v2 18 of 44 → prototype 43 of 44. Words: about 260 → 1.698.

## Corrections on other pages
- ERFOLG Magazin: this page uses the past tense („zählte ihn“, cover 2017). The sibling pages still use present tense (RP8).

## v2 community version (2026-10-12)
1. Prototype `07-prototype/v2/index.html`, build `07-prototype/v2/build.py`. Copy `04-copy/approved-copy.md` (v7, community); the call version is `04-copy/approved-copy-v1-call.md`.
2. All buttons and the header/footer link go to `https://www.skool.com/talk-to-me-9409/about?utm_source=lp-replayers&utm_content=<section>` (header, hero, momente, methode, community, community-bild, michael, start, abschluss, footer). Tracking event `community_click` with `section`. The free video is one text link in S09 (`video_click`). No „Gespräch buchen“ anywhere on this page. At integration: the site header on this page shows „Community beitreten“ instead of „Gespräch buchen“.
3. Verified Skool facts and sources: `02-data/dataset.md` section 9 (T1 to T3).
4. [FEHLT] for v2: price (Skool text 39 €/Monat vs. button $44/Monat), live-call rhythm, cancellation rule beyond the Skool platform rule, beginner fit, permission for the Skool cover image, consent for the Skool reviewer's name. Plus the open v1 items 2, 3, 4, 6, 7.
5. Client recommendation: the Skool about text has result promises and „intelligente Köpfe“ (RP4). This page now sends traffic there.
6. Before / after: v2 page 18 of 44 → v1 call 43 → v2 community 42 (price unconfirmed).
