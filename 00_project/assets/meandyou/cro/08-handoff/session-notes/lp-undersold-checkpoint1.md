# lp-undersold — Checkpoint 1 (Copy), 2026-10-12

Run: `00_project/assets/meandyou/cro/lp-undersold/`. Copy master: `content-writing/lp-undersold/05-final/page.md` (1,440 words, G1 to G6 PASS).
Drive: https://drive.google.com/drive/folders/14yCptAjFldgweRhjgcLjiasto9KYx4kk

For the main session (integration):
- CTA links follow `_site`: `gespraech-buchen.html?utm_source=lp-undersold&utm_content=abschluss` (one in-page button, S11) and `utm_content=header`.
- G6c: lp-undersold has only 1 inbound text link. The homepage card "Dein Unternehmen ist größer, als es nach außen wirkt." should link to the LP. Same for lp-overlooked.
- Slug `/lp-undersold` has no keyword. Choose the live slug before indexing (proposal `/rhetorik-seminar-fuehrungskraefte`).
- Schema plan: `content-writing/lp-undersold/05-final/schema.jsonld` (3 Course, 11 CourseInstance, no price, no instructor until confirmed).
- Similarity to seminare page.md is 21.1 % (dates and format facts), under the 25 % limit.

# lp-undersold — Checkpoint 2 (Prototyp), 2026-10-12
- Prototype: `cro/lp-undersold/07-prototype/index.html`, built by `build.py` (loads `seminare/07-prototype/build.py` → homepage system). Assets in `07-prototype/assets/` (new: `hero-coast.webp`, `format-terrace.webp`).
- Links follow the sibling pattern `V2 termin.html?utm_source=lp-undersold&utm_content=header|abschluss|footer`; `site-build/assemble.py` maps termin.html → gespraech-buchen.html.
- Header nav links point to V2 pages (seminare, michael, rhetorik, stimmen, faq) like the siblings.
- Port: 8833 was taken by a helper server of the lp-replayers run, so this run served on 8836 (server stopped).
- Score 40/44 (v2 15). verify.py: only the handoff items fail (Step 7 belongs to the main session).
- Handoff items for Step 7: slug with keyword before indexing, one phone number, homepage card link to the LP, sameAs, `instructor` in Course schema only after the client confirms Michael leads the seminars, shoot list (real place photos, terrace group).
