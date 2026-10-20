# me&you homepage prototype: handover

Date: 2026-10-05. Owner: Martin (741). This file lets another person, with another Claude account, continue the work. It contains no prices and no access data.

## 1. The project in short

- **Client:** Michael Ehlers / me&you Communication (meandyou.de). He is a rhetoric trainer with 3-day seminars in Mallorca, Barcelona, Dubai, Cyprus, Frankfurt and Berlin.
- **Partner agency:** Pauspapier. They do creative work and content. They built the current site in Framer.
- **741:** we do the technical work: website, funnel, ads.
- **This task:** a new design for the homepage. The result so far is a live prototype for internal review. It is not a final site.

## 2. Where things are

All paths start at `00_project/` in the repository.

| What | Path |
|---|---|
| Prototype source (the page) | `assets/meandyou/prototype/page.html` |
| Local preview file (generated) | `assets/meandyou/prototype/index.html` |
| Build script | `assets/meandyou/prototype/build.py` |
| Images used by the page | `assets/meandyou/prototype/assets/` |
| Raw image sources | `assets/meandyou/prototype/src/` |
| Design source of truth (PDF, 20 pages) | `assets/meandyou/quellen/Ehlers.pdf` |
| Design guidelines (written from the PDF) | `assets/meandyou/quellen/meandyou-design-richtlinien.html` |
| Content of the current site, section by section | `meandyou-sektionen-kontext.md` |
| Notes on the ChatGPT mockup and the prototype rules | `meandyou-prototyp-notizen.md` |
| Analysis of the reference site (Remedy) | `meandyou-referenz-remedy-bausteine.md` |
| Raw files of the reference site | `assets/meandyou/referenz-remedy/` |
| Raw HTML of the current site | `assets/meandyou/ist-seite/index.html` |
| Prompt for a full-page mockup image | `meandyou-fullpage-image-prompt.md` |

Live prototype: https://claude.ai/artifact/WMQWs1dZ91Lng2qqoagAUS
The page is private. Martin must share it from the Share menu before another person can open it.

## 3. How we got here (the process)

1. **Wrote the design guidelines.** We read the Ehlers.pdf and wrote clean rules: brand, colours, type, three personas, photo rules, always/never list.
2. **Collected reference sites.** We searched awwwards.com. Martin then chose https://remedyeditorial.com/ as the model for structure and scroll feel.
3. **Recorded the current site.** We read https://www.meandyou.de/ and saved every section with its exact text, including all 13 FAQ answers.
4. **Wrote an image prompt.** Martin gave it to ChatGPT, with the PDF, to get a full-page mockup image.
5. **Reviewed the mockup.** The direction was good. The spacing was too tight, and ChatGPT invented most of the small texts, the faces and the award seal.
6. **Analysed Remedy.** We downloaded its HTML, CSS and JS and measured what makes it feel good (section 6 below).
7. **Built the live prototype.** One HTML page with the real texts, real photos of Michael, and the Remedy scroll behaviour.
8. **Created the missing images in ChatGPT.** The first set had no people. Martin corrected this: the PDF always shows people. We made a second set with people.
9. **Published** the page as a private artifact and checked it at 1440 × 900, 1280 × 720 and phone width.

## 4. Rules from Martin (do not break these)

1. **One section fills one screen height.** When you scroll, you see one section at a time.
2. **One exception:** "Dein Ergebnis" (a narrow quote band with icons) and "Unser Ansatz" share one screen.
3. **Do not change the page text.** All copy is the current text of meandyou.de. This includes "Seminare für Intelligente". Text changes come later. Do not propose text corrections.
4. **Images always show people.** Follow the photo pages of the PDF: candid, like a reportage, nobody looks at the camera, natural light, light grain, small groups. Never: stage, conference, hotel ballroom, lanyards, stock look.
5. **Image order of preference:** real files first, then the PDF as the style model, then generate missing images with ChatGPT.
6. **Never invent Michael's face.** Use the real photos only.
7. **Real logos only.** Never redraw a logo or an award seal.
8. **No seminar prices on the page.** Buttons go to the booking page.
9. **The PDF decides design questions.** About 20 percent is flexible.
10. **Remedy decides structure and scroll behaviour.**

## 5. Design system

- **Fonts:** Libre Baskerville for headlines and quotes. Inter for everything else.
- **Colours (approximate, exact values are still to come from Figma):** cream `#F2EDE4`, light grey `#E7E8E8`, sand `#D8CCB7`, dove blue `#7E99B6`, dark navy `#2B3C52`, warm anthracite `#47403A`.
- **Background decision:** warm off-white `#FAF8F4` as the base. Cream only for alternate screens and cards. The flat beige of the ChatGPT mockup looked muddy.
- **Layout:** much white space, one idea per screen, soft corners, no hard lines, one CTA style (dove blue pill).
- **Navigation:** Seminare | Für wen | Unsere Methode | Über Michael.
- **Three personas** (details in the guidelines file): The Replayers (warm, private), The Overlooked (precise, cool light), The Undersold (rare, golden hour, place and group lead).

## 6. What we took from Remedy

- **Smooth scroll:** Lenis, `duration: 1.1`, ease `1.001 - 2^(-10t)`, wheel only. Off for "reduce motion".
- **Header:** open at the top, becomes a floating capsule after 60 px of scroll.
- **Grid:** title on the left, content on the right.
- **Parallax:** images move a little slower or faster than the page. Factors 0.06 to 0.14. Desktop only (from 1024 px).
- **One dark section** as a colour change (the navy band).
- **Measures:** container max 1440 px, side padding up to 60 px.

## 7. The prototype

### The 12 screens

| # | id | Content |
|---|---|---|
| 1 | `hero` | Hero with real photo, three speech cards, trust figures, ERFOLG cover |
| 2 | `story` | "Du bist der Klügste im Raum" story |
| 3 | `warum` | "Intelligente haben es schwerer" with the five problem cards |
| 4 | `orte` | Three location cards |
| 5 | `termine` | Dates with a 2026 / 2027 switch |
| 6 | `ansatz` | Navy band "Dein Ergebnis" plus "Unser Ansatz" comparison |
| 7 | `veraenderungen` | The nine changes |
| 8 | `michael` | "Woher ich das weiß?", award, media logos |
| 9 | `stimmen` | Switch: video placeholders / four client quotes |
| 10 | `fuerwen` | "Diese Seminare sind genau richtig für dich, wenn du:" |
| 11 | `faq` | 13 questions, accordion in two columns |
| 12 | `kontakt` | Closing CTA, contact form, footer |

### How the file works

- `page.html` is the source. It has no `<!doctype>`, `<html>` or `<body>` tags, because the artifact host adds them.
- All CSS and JS is inline. Design tokens are in `:root` at the top.
- `.screen` gives each section `min-height: 100svh`. Below 980 px the sections have natural height and stack.
- `data-plx="0.1"` on an image frame turns on parallax. `.rv` gives the reveal on scroll.
- The FAQ text is a JS array `FAQ` near the end of the file.
- External loads: Google Fonts, and Lenis from `cdn.jsdelivr.net/npm/lenis@1.1.20`.

### Build and preview

```bash
cd 00_project/assets/meandyou/prototype
python3 build.py
python3 -m http.server 8963
```

Then open http://localhost:8963/index.html. `build.py` wraps `page.html` into `index.html`. It also converts new ChatGPT images from `~/Downloads/meandyou-g2-<name>.png` to `assets/gen-<name>.webp`.

### Publish

Publish `page.html` as an artifact with the `assets/` files as supporting files. With edit access to Martin's artifact, update the same link. Without it, publish a new artifact from your account.

## 8. Images

| File | Source | Used in |
|---|---|---|
| `michael-cafe.webp` | Real, from meandyou.de | Hero |
| `michael-door.webp` | Real, from meandyou.de | Über Michael |
| `michael-table.webp`, `michael-olive.webp`, `michael-jacket.webp` | Real, from meandyou.de | Not used yet |
| `logo-dark.webp`, `logo-light.webp` | Real | Header, footer |
| `erfolg-top100.webp`, `top10-speaker.webp` | Real | Trust band, award |
| `logo-zdf`, `-ard`, `-rtl`, `-stern`, `-mdr`, `-hr2` and others | Real | Media row |
| `gen-dubai.webp`, `gen-mallorca.webp`, `gen-barcelona.webp` | ChatGPT | Location cards |
| `gen-meeting.webp` | ChatGPT | Story |
| `gen-group.webp` | ChatGPT | Für wen |
| `gen-closing.webp` | ChatGPT | Closing CTA |

The photos inside the PDF are too small for a full screen (each PDF page is 920 × 514 px). Use them as the style model only.

### How to make a new image

Use ChatGPT image generation, one image per message, landscape 3:2. Start with this style block, then describe the scene:

> Candid documentary photography with real-looking people, like an editorial reportage. Nobody looks at the camera, people are in natural motion or conversation, natural light, light film grain kept, never retouched or glossy, never stock-looking, no lanyards, no stage, no conference look, no text. Landscape 3:2.

For the "Overlooked" mood add: cooler daylight, architectural lines, person in context, muted blue-grey palette. For the "Undersold" mood add: golden hour, long shadows, wide framing, the location is as important as the people.

Look at every image before you use it. Set `object-position` in `page.html` so the crop keeps the people in view.

## 9. Decisions in the prototype that are not from the current site

- The small labels above headlines are new (for example "Seminarorte", "Dein nächster Schritt", "Deine Veränderungen").
- The nine changes have short new titles above the original sentences.
- Two helper texts are new: the button "Zu den Terminen" and the line "Alle Termine sind 3-Tages-Seminare."
- The emoji in the story text is removed.
- The price line for Mexico is removed (rule 8).
- The ChatGPT mockup had dropped the problem section and the nine changes. The prototype keeps both as their own screens.
- Client quotes show first. The video tab has marked placeholders, because we do not show invented participants.

## 10. Known gaps and open points

- **Mobile:** readable, but not tuned.
- **Videos:** the real participant videos are missing. Ask the client for the files.
- **Form:** it sends nothing.
- **Dates 2027:** the live site was edited while we read it. Check the dates against the client's date list before any real use.
- **Hero carousel:** the guidelines plan a hero carousel with one variant per persona. The prototype has one static hero.
- **Campaign layer "UNÜBERSEHBAR":** planned in the strategy, not in the prototype.
- **Seminar names:** the client still owes the new seminar names and the definition of the starter seminar.
- **Exact colour values:** take them from the Figma or branding file before the real build.
- **Platform:** Framer or own HTML is not decided.
- **Barcelona image:** it shows a wine glass. Replace it if the client wants a pure work mood.
- **Scroll snap:** not used. It is an option if the one-screen rule should feel stricter.

## 11. First steps for the next person

1. Read this file, then the guidelines file, then look at the Ehlers.pdf.
2. Run the build and open the local preview.
3. Compare each screen with the rules in section 4.
4. Ask Martin which open point from section 10 comes first.

## 12. Update 2026-10-05 (later): prototype v2 with all pages

Martin approved the next step. Version 2 uses the new texts from the Copy Deck Round 3 and has all pages. Version 1 (old site texts, one page) stays unchanged in `prototype/`.

- **Live:** https://claude.ai/artifact/DpyEL5pa1Bc42nT8z1kCyx (private, Martin must share it).
- **Source:** `assets/meandyou/prototype-v2/build_v2.py`. All page content is in this one script. Run `python3 build_v2.py`. It writes `page.html` (home, for the artifact), `index.html` and eight sub pages. The folder `assets` is a link to `../prototype/assets`.
- **Preview:** `python3 -m http.server 8964` in `prototype-v2/`, then open http://localhost:8964/index.html.
- **Copy source:** `assets/meandyou/quellen/ME&YOU_CopyDeck_Round3_DE-EN.docx`. German is the live copy. Text in [square brackets] is a placeholder.
- **Site structure and image mapping:** `meandyou-website-struktur.md`.
- **Feedback mapping and VSL test plan:** `meandyou-feedback-und-vsl-testplan.md`.

### New rule from Martin
**Take the persona photos from the Ehlers.pdf.** The PDF says which look belongs to which persona. Use these photos where the PDF places them. Generate an image only where the PDF has none (locations, wide backgrounds), and follow the PDF photo rules.

The PDF photos are crops from pages of 920 × 514 px, scaled up two times. They are soft when shown large. The crop script is in section "pdf" of this history: files `prototype/assets/pdf-*.webp`, raw pages in `prototype/src/pdfnat/`. Ask for the original photo files before the real build.

### Context for the feedback
The reviewers saw only the three-persona presentation. They did not see the prototype or the Copy Deck. Their website points are about the live site.
