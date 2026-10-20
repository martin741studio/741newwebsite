# Handoff (page part) — LP „The Replayers“ (2026-10-12)

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
