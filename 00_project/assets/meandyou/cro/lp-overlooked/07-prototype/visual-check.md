# Visual check — lp-overlooked prototype v1 (2026-10-12)

Claude in Chrome (external Chrome), `http://localhost:8832/index.html`, window 1440 wide, real viewport 1440 × 757 (Chrome UI takes the rest). Loaded without `?shot=1`. Compared with `06-gpt-assets/full-page-v1-final.png` and `04-copy/approved-copy.md`. Scrolled top to bottom in steps of about 700 px, then back up.

Visual check done in Chrome, 39 items checked, 14 fixed, 1 open

## 1. Measured checks
| # | Result | Evidence |
|---|---|---|
| M1 | ok | innerWidth 1440 |
| M2 | ok | no horizontal scroll |
| M3 | ok | no console errors, all assets 200 |
| M4 | ok | every image loaded, none upscaled (hero 1536 × 1024 shown 670 × 814 with cover) |
| M4b | ok | no distortion (all photos `object-fit: cover`) |
| M5 | ok | Inter and Libre Baskerville loaded |
| M6 | ok | 0 missing anchors, 0 `#` placeholders, tel `+4915888367664`, hosts clients.741.studio, meandyou.de, instagram, linkedin |
| M7 | ok | 0 reveals hidden after a slow scroll |
| M8 | ok | hero CTA bottom at 636 px (rule: under 701) |
| M9 | fixed | table headers and seminar tags were 15 px, now 16 px. Remaining under 16 px: overlines 14 px („Drei Teile …“, „Rolle/Beleg“, footer headings) and the yellow badges 15 px, as on the other pages |
| M10 | ok | 2 breathing CTAs (hero, closing) |
| M11 | ok | `check_text.py`: only footer, video durations and prototype notice differ (same as sibling pages) |

## 2. Global items
| # | Result | Note |
|---|---|---|
| G1 Alignment | ok | one 1240 px wrap, the visible six-column grid lines up with the content edges |
| G2 Spacing | ok | 120 px section padding, proof strip 40 px |
| G3 Text | fixed | method H2 had one word per line (column 330 px), now 3 lines at 390 px. Grid lines in light bands were strong behind text, alpha lowered |
| G4 Images | ok | hero image sharp, same cool light as mockup; real photos of Michael elsewhere |
| G5 Colour | ok | one CTA colour #4F6D90, cream on navy; blur test: hero button stands out |
| G6 Typography | ok | two fonts, serif headlines, body 17 to 19 px |
| G7 Buttons and links | ok | same pill on every section, text links with underline |
| G8 Mockup comparison | ok | order and layouts match (navy hero with photo right, proof strip, answer with 3 parts, cards, navy diagram, intro column beside each table, 3 steps, photo + evidence table, 2 × 2 quotes + videos, FAQ two columns, three-part navy closing). Intended differences: no photo caption in the hero and under the Michael photo (the mockup invented caption text, not in the approved copy); no icons in the diagram boxes (numbers instead); diagram arrows simplified |
| G9 Hover | ok | CTA lifts and darkens, tags darken, FAQ rows change colour |
| G10 Sticky header | ok | menu „FAQ“ lands with H2 at 216 px, header bottom 86 px |

## 3. Sections
| Section | Result | Note |
|---|---|---|
| Header | ok | real logo, five menu items, button |
| S01 Hero | fixed | photo did not show (absolute figure inside a relative grid wrapper), text column ran too wide, grid lines crossed the photo. All fixed |
| S02 Proof strip | fixed | numbers were cramped, „Top 100“ label on 5 lines; columns re-weighted, now 3 lines |
| S03 Answer | ok | H2 and answer side by side, 3 parts with hairlines, podcast pull quote |
| S04 Situations | fixed | summary row squeezed the bold line into a narrow column; restructured to text left, button right |
| S05 Method | fixed | boxes overflowed (default `figure` margin), connector line ran through the boxes, box heights uneven; all fixed |
| S06 Comparison | ok | highlighted right column, quote with source, button right |
| S07 Topics | fixed | a class name clashed with the homepage `.sit` card style (white rounded cells); renamed. Tags were 15 px pills with underline, now 16 px tags |
| S08 Formats | ok | „Gespräch“ column highlighted, yellow badges in place |
| S09 First step | fixed | yellow badge broke the sentence („. Michaels Team …“ on a new line); badge now inline |
| S10 Michael | ok | real photo, evidence table, link |
| S11 Voices | ok | 4 open cards, no carousel, 3 real videos |
| S12 FAQ | ok | 9 questions, one open at a time, plus turns to x |
| S13 Closing | ok | H2, three checks, proof line, cream button breathes, phone link |
| Footer | ok | address, phone, mail, legal links |

## 4. Interactions
| Check | Result |
|---|---|
| Booking CTAs | ok: 9 links to `termin.html?utm_source=lp-overlooked&utm_content=` header, hero, situationen, vergleich, formate, ablauf, stimmen, abschluss, footer. Nothing submitted |
| Phone | ok: `tel:+4915888367664` |
| Menu and text links | ok: Seminare, Michael, Was ist Rhetorik, Stimmen go to the v2 preview pages; FAQ to `#faq`; seminar tags to `seminare.html#frei-sprechen`, `#ruhig-bleiben`, `#mit-sprache-fuehren` |

## Open
1. S01 hero photo is generated (face from the real photo). Shoot list: a real photo of Michael in a glass meeting room. Needs the client.

Client facts shown as yellow badges (6): Freigabe Zitat, ein Satz und eine Übung je Methodenschritt, Seminarname, Extras des Online-Kurses, Kursname, Name und Rolle der Person im Gespräch.
