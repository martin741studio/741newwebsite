# Scorecard: live homepage (today), claudia-breuer

Source: evidence/home-today-1440.jpg (1456 px, cropped to 1440 px: review-assets/claudia-breuer/startseite-heute.webp), evidence/raw/home.html (full text, used for items below the fold), evidence/home-images.txt.
Scale: 0 = missing, 1 = partial, 2 = met. Max 44 (22 items x 2).
Note: the brief says "22 points". The scorecard gives 0/1/2 per item, so the maximum is 44.

| # | Rule | Prio | Score | Evidence |
| --- | --- | --- | --- | --- |
| 1 | Hero: what, who, next step in 5 s | A | 1 | Screenshot: H1 "Sorgen Sie für Ihre seelische Gesundheit" names no service. Service only in logo line "Heilpraktikerin für Psychotherapie / Beratung | Coaching | Therapie". |
| 2 | Headline = result + city | A | 0 | Screenshot: H1 has no city. Raw home.html: "Bonn" only in title and meta, not in H1. |
| 3 | Sub-headline: situation, then 3-4 helps | A | 1 | Screenshot sub: "...berate ich Sie in Lebenskrisen, bei Ängsten, emotionalen Blockaden, Stress oder Erschöpfung..." Situations yes; no concrete help list. |
| 4 | Primary CTA visible at 1440x800 | A | 0 | Screenshot: no button in the first screen. |
| 5 | CTA text = next step + benefit | A | 0 | No CTA button on home (raw home.html: no button text; only nav "Kontakt"). |
| 6 | Reassurance under CTA | A | 1 | Screenshot: "Sie erhalten kurzfristig Termine - auch in den Abendstunden." Present, but not under a CTA. |
| 7 | Two proof forms above fold | A | 0 | Screenshot: no review rating, number or quote in first screen. |
| 8 | Face + qualification in hero | A | 2 | Screenshot: portrait in hero; sub: "Als Heilpraktikerin im Bereich Psychotherapie". |
| 9 | "Erster Termin": 3-4 steps, duration, price | A | 1 | Raw home.html: "Honorar & Ablauf: Erstgespräch - kostenlos (30 Minuten), Einzelgespräch - 100 € (60 Minuten)". Steps and full section not on home. |
| 10 | One CTA accent colour; blur test | A | 0 | No CTA on screen to test. |
| 11 | CTA repeats every 2 sections | A | 0 | Raw home.html: no button CTA found; "Termin" only in running text. |
| 12 | Reviews open, name + Google + heading | B | 0 | Raw home.html: no "Google" or "Bewertung" on home. |
| 13 | Proof heading carries a benefit | B | 0 | No proof section on home. |
| 14 | 3-4 proof blocks spread over page | B | 0 | No proof blocks on home. |
| 15 | Situations section, 3-5 items, way out, HWG-clean | B | 1 | Raw home.html: cards "Stress", "Erschöpfung", "Ängste", "Lebenskrisen" with teasers; no explicit "way out" section. HWG issue see item 22. |
| 16 | Services as cards with benefit heading and link | B | 1 | Raw home.html: cards with "Mehr Lesen" links (01-04). Card headings are topic labels, not benefits. |
| 17 | FAQ with real objections | B | 0 | Raw home.html: no FAQ on home. |
| 18 | Location block: map, address, parking, transit, hours | B | 0 | Raw home.html: no "Wurzerstra", "Parken", "ÖPNV", "Öffnungszeit" on home. |
| 19 | Closing block = mini hero with CTA + phone | B | 1 | Raw home.html: closing paragraph "...einen Termin mit mir zu vereinbaren", no button, no phone. |
| 20 | Section headings carry a statement | C | 0 | Raw home.html h2 list: "Über meine Arbeit", "Über mich", "Behandlungsfelder", "Honorar & Ablauf", "Ablauf" (site-pages.json). Labels. |
| 21 | Type hierarchy: H1 3-4x body, body >= 16 px | C | 1 | Screenshot: H1 about 50 px, body text visually about 14 px. Visual estimate only, computed style not measured. |
| 22 | HWG gate: no healing promise, no before/after, no fear appeal | A | 0 | Raw home.html, teaser card: "Angst machtlos ausgeliefert?" and home-linked Ängste text: "Gibt es immer mehr Situationen, die Ihnen Angst machen? ... Angst krank zu werden..." Fear appeal = hard gate fail. No healing claim found. |

Total: 10 / 44 (scores 2 = items 8; 1 = items 1, 3, 6, 9, 15, 16, 19, 21; 0 = the other 13).
Prototype rule (all Prio A = 2, total >= 36/44): not met. Prio A items at 0 or 1: 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 22.
Status: partial screenshot scoring. Items 12-19 use raw HTML text (not the first screen).
