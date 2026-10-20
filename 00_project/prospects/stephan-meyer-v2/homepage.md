# Homepage: stephanmeyer.com (agent C, 2026-10-12)

## Score

- Today: **15 / 44** (evidence/scorecard-today.md). Item 22 = 2 (no health or legal risk).
- Screenshots: evidence/home-today-1440.jpg (operator), evidence/home-draft-1440.jpg (our draft).
- Review assets: 04_site/public/review-assets/stephan-meyer-v2/startseite-heute.webp, startseite-entwurf.webp, foto-1.webp, foto-2.webp, foto-3.webp.

## 5-second test

| Question | Today (first screen) | Draft (first screen) |
| --- | --- | --- |
| Was? | Not clear. "Are you a visionary?" + "I help you turn your visions into reality". No service named. | "Dein Experte für Change Management" + Vorträge, Coaching, Beratung in the sub-line and the eyebrow. |
| Wo? | Not visible. Start page is English. No place, no "online". | "online per Videocall" in the H1 and the top bar (his contact page and Google "Onlinetermine"). |
| Warum du? | Only "Dr." in the header. No proof in the first screen. | Promotion 2019 (University of Gloucestershire), Diplom-Psychologe RWTH Aachen, über 25 Jahre, frühere Kunden Allianz, Audi, Mercedes, PwC. |
| Wie zum Termin? | "Start Now" / "Read More". The video-call booking is only on /contact/. | Button "Erstgespräch per Videocall buchen", line "Lass uns prüfen, ob ich dir helfen kann. Du wählst den Termin selbst." |
| Wer? | Hero photo cuts his head off. Name only in the header. | His keynote photo as the hero, name card with his real studio portrait: "Dr. Stephan Meyer · „Doctor Change“ · Wirtschaftspsychologe". |

Trust-row sources (all on his site, 2026-10-12):

| Card | Source | Exact text |
| --- | --- | --- |
| Promotion 2019 | https://stephanmeyer.com/about/ | "In 2019, I received my doctorate degree at the University of Gloucestershire" |
| Diplom-Psychologe | https://stephanmeyer.com/about/ | "business psychology with focus on organizational development at the RWTH Aachen University … Diplom-Psychologe" |
| Über 25 Jahre | https://stephanmeyer.com/about/ | "more than 25 years of coordinating successful transformations … international corporations and at family businesses" |
| Frühere Kunden | https://stephanmeyer.com/ | Section "A Few Previous Clients", logos Allianz, Audi, Mercedes, PwC (also Aon, BMWi, E.ON, Evonik, Novartis, Ottobock, P&C, Zurich) |

Notes for the review page:
- Place conflict. Google entry: Wurzbach area, Thüringen, service-only, no address (evidence/google-panel-2026-10-12.md). Imprint: Almademey Limited, Paphos (Geroskipou), Cyprus. Coach page: "nicht den ganzen Weg von Zypern hergeflogen". His site names no German region. The draft H1 therefore says "online per Videocall", not "in Wurzbach". Agent E must not write that he works in Wurzbach or Thüringen without a source.
- Experience: about page says "more than 25 years", the homepage says "three decades", the Google web snippet says "30+ years". The draft uses the lowest value (25).
- Google: 0 reviews, no stars. The draft has no stars.
- The 2025 photos on his site (Speaker-002/005/012, Lounge-001, Leasure-001, Doctor-Change-Pack-2) look AI-generated (same face style, Flux-type sizes 1152×896 and 1024×1024). They are his own site images, named "Stephan-Meyer-…". The only clear real photos are the studio portrait (Dr-Stephan-Meyer-freigestellt-01.png, 2020) and the field selfie (Dr-Stephan-Meyer-outstanding-in-his-field-1c.jpeg). Martin decides if the AI look is a point for the review page.
- Unsourced claims on the homepage: "SLASH TRANSFORMATION TIME BY 50%", "Teams functioning at 40% potential", "Increased Profit". Not health, so no HWG gate.
- The start page is English. The German page is /de/. Most German blog posts and /de/ use "du".

## Test of draft_home.py

Run: `python3 prospect-mini/scripts/draft_home.py stephan-meyer-v2 --service "Change-Management-Experte"`, 9 s wall time (script reports 9.1 s).

What I had to fix by hand in draft/index.html:
1. **Wrong hero photo.** praxis.jpg was wpautoblog-image-46.jpg, an auto-blog image of another speaker ("The Future of Social Media", CHATI logos). Not him. Removed. New hero.jpg = Stephan-Meyer-Speaker-002-Upscale.jpeg, the hero background of his own start page.
2. **No logo.** Script said "NONE: no logo image on the site". His site has a logo: cropped-Dr.-Stephan-Meyer-transparent-black.png (cow head + "STEPHAN MEYER"). Cropped the transparent margins → logo.png.
3. **No portrait card.** Added portrait.jpg = head-and-shoulders crop of his real studio photo (Dr-Stephan-Meyer-freigestellt-01.png) in the name card.
4. **Headline grammar and place.** "Deine Change-Management-Experte in Wurzbach." (wrong gender, Wurzbach not on his site). → "Dein Experte für Change Management – online per Videocall."
5. **Sub-line.** Repeated the H1 and listed nav labels ("Keynotes, Coach/Counsellor und Trusted Advisor"), "wir" form. → situation (Wandel, Widerstand im Team) + Vorträge, Coaching, Beratung, "ich" form, "Wirtschaftspsychologe" from his site.
6. **Practice words.** Trust card "Praxis in Wurzbach", button "Ersttermin vereinbaren". → no "Praxis"; button "Erstgespräch per Videocall buchen", header "Videocall buchen" (his real booking path).
7. **"wir" → "ich".** Script set we=true. He works alone. Note line "Wir melden uns persönlich bei dir" → "Lass uns prüfen, ob ich dir helfen kann. Du wählst den Termin selbst." (from /de/: "Lass uns prüfen, ob ich helfen kann.").
8. **Nav.** English labels (Home, About, Services, Keynotes, Coach/Counsellor). → his German nav words: Über mich, Vorträge, Coaching, Trusted Advisor, Kontakt. "Home" removed.
9. **Eyebrow.** "Keynotes · Coach/Counsellor · Trusted Advisor" → "Vorträge · Executive Coaching · Beratung" (his "Drei Wege" section on /de/).
10. **Top bar.** "Termin vereinbaren" (same as the button) → "Erstgespräch per Videocall · Termin direkt online buchen".
11. **Trust row.** 2 cards that repeated the H1 and the eyebrow. → 4 cards with facts from his site (table above), each with a data-source attribute.
12. **Colours.** Script used navy #003388. His buttons use purple #5304b5 (16× in the CSS). Changed acc, head, cream and border colours to his purple scheme.
13. **Hero crop.** object-position 50% 60% cut the face. → 40% 15%.

Checks passed: form of address "du" (as /de/ and the German blog). No "Praxis", no "Patienten". No result promise. No skip link or info page in nav, eyebrow or trust row. No stars (0 Google reviews).

Strip photos (all from stephanmeyer.com, opened and checked):
- foto-1 = Stephan-Meyer-Speaker-005.jpeg, him on stage at a keynote (1152 px wide).
- foto-2 = Stephan-Meyer-Lounge-001.jpeg, him seated in a lounge, coaching setting (1024 px).
- foto-3 = KKA-Cover.jpg, cover of his German workbook "Das Kuh Kanvas Arbeitsbuch" (924 px).
Not used: wpautoblog images (other people, auto-blog), client logos (not his brand), pexels avatars (stock), Doctor-Change-Pack-2 (toy-figure AI image).
