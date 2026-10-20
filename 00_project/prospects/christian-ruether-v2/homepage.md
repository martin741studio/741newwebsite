# Homepage: soziokratie.org (agent C, 2026-10-12)

## Score

- Today: **5 / 44** (evidence/scorecard-today.md). Without item 22 (not a health client): 3 / 42.
- Screenshots: evidence/home-today-1440.jpg (operator), evidence/home-draft-1440.jpg (our draft).
- Review assets: 04_site/public/review-assets/christian-ruether-v2/startseite-heute.webp, startseite-entwurf.webp, foto-1.webp, foto-2.webp, foto-3.webp.

## 5-second test

| Question | Today (first screen) | Draft (first screen) |
| --- | --- | --- |
| Was? | Only from the menu item "Was ist Soziokratie?". The screen is a stock photomontage. | "Ihr Soziokratie-Berater in Wien." plus Beratung, KonsenT-Moderation, Workshops to SKM, S3, Holakratie. |
| Wo? | Not visible. Address only in the imprint. | Wien in the H1. Neustiftgasse 89-91, 1070 Wien in the top bar and the trust row. |
| Warum du? | Not visible. Book and Masterthesis appear only further down as list links. | Author of the textbook "KonsenT-Moderation", Masterthesis on Soziokratie, Mag., MBA. |
| Wie zum Termin? | Not visible. Only "See More". Phone is plain text in the sidebar, no tel link. | Button "Erstgespräch vereinbaren", phone in the top bar, workdays 8 to 17 Uhr. |
| Wer? | Not visible. Portrait only in the sidebar below the first screen. | His portrait is the hero image, name and qualification in the trust row. |

Notes for the review page:
- The cookie banner covers the lower part of the first screen today. Its purple button is the strongest colour on the screen.
- The Google profile has 0 reviews, so the draft has no stars. The proof line uses the book instead.
- The Google panel lists the address "in: Cult Café". The draft uses the imprint address only as the business address, not as an office.

## Test of draft_home.py

Run: `python3 prospect-mini/scripts/draft_home.py christian-ruether-v2 --service "Soziokratie"`, 9 s wall time (script reports 8.9 s). Script output kept as draft/index.script-output.html.

What I had to fix by hand in draft/index.html:
1. **No logo.png.** The site has no logo image (text title "Soziokratie"). The script fell back to a text brand. That is correct, but the brief says it writes logo.png. The script should report "no logo" in draft-home.json.
2. **"Skip to content" taken as content.** The screen-reader link went into the nav, the eyebrow, the sub-headline, the services list and a trust card. The script must drop skip links.
3. **Services taken from the nav.** "Fallbeispiele" and "Begleiter*innen" are information pages, not services. Real offer from the site: Beratung, KonsenT-Moderation of meetings and Klausuren, workshops on request.
4. **Headline grammar.** "Ihre Soziokratie in Wien." uses the service as a person. Fixed to "Ihr Soziokratie-Berater in Wien." (who + what + where).
5. **Sub-headline.** "Sie suchen eine Soziokratie in Wien? ... Skip to content, Fallbeispiele und Begleiter*innen." Rewritten: situation (team or organisation wants to decide on equal footing) + 3 helps.
6. **Practice words.** "Ersttermin vereinbaren" → "Erstgespräch vereinbaren". Trust card "mit eigener Praxis in Wien" → removed. "Leistungen ansehen" → "Buch gratis als PDF" (a real offer on his site).
7. **Wrong second photo.** praxis.jpg is the site header, a stock photomontage (Pixabay 1514218), not his room or work. Removed. The portrait is now the main hero image; the book cover (buch.jpg, from the site) is the small card.
8. **Top bar without facts.** The script wrote only "Termin vereinbaren". Phone (+43 699 11114398) and address (imprint) were on the site. Added.
9. **Trust row.** 2 cards, both wrong. Replaced by 4 cards from the site: Mag. Christian Rüther, MBA; book 2022; SKM, S3 und Holakratie; Christian Rüther e.U., address.
10. **Layout at 1440.** Nav items and the header button wrapped to two lines, brand touched the nav, the portrait crop cut the chin. Fixed with nowrap, a header gap and a fixed picture width (430 px).

Checks passed: form of address "Sie" (correct, his site uses "Sie" in the main text). No promise of results in the draft.

Strip photos: foto-1 = portrait laechelnd-neu.jpg (soziokratie.org), foto-2 = portrait ohne-brille-angelehnt.jpg (from his second site christianruether.com, same person), foto-3 = book cover (soziokratie.org). The site has no third real photo of him.
