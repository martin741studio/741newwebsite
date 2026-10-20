# 741 CRO-Raster — Layout patterns (derived from the CRO library)

Derived 2026-10-11. Internal document. Src = file numbers in `00_project/knowledge/cro-library/`. Use these as the layout input for the GPT design doc (Step 4) and the prototype (Step 6).

---

## P0. The blueprint (the base for every local practice homepage)

Combined from the five-block template (Src: 022), the Figma blueprint (Src: 051), the full long-form order (Src: 012, 046, 064) and the local adaptation.

**Hero anatomy (desktop: text left, image right; mobile: image above text, all stacked)**

1. Proof line 1 above the headline: Google rating + review count with logo, linked.
2. Headline: felt outcome + city. H1 holds the keyword, visibly smaller if needed.
3. Sub-headline: situation first ("Du hast …"), then how the practice helps, 3–4 specifics.
4. Primary CTA button (one accent colour) + clickable phone number as outline button beside it.
5. Reassurance check marks under the CTA: reply time, first-visit duration, no obligation, hours.
6. Proof line 2 under the image or beside the CTA: years, patients per year, or one handpicked quote.
7. Image: the real practitioner, smiling, gaze towards the headline or CTA. Soft brand backplate behind the photo.
8. A visible edge of the next section.

**Section order for search and Maps traffic (default):**

| # | Section | Job | Layout |
| --- | --- | --- | --- |
| 1 | Hero | who, what, for whom, next step | see above |
| 2 | Proof wall | trust before anything else | 3–6 Google reviews open, each with headline, first name, Google logo; "mehr anzeigen" on mobile |
| 3 | "Ist das etwas für dich?" | recognition | 3–5 situation cards (icon + 2 lines), then one line "So helfe ich" |
| 4 | Leistungen | route to service pages | 3–6 cards with image, benefit heading, 1 line, link |
| 5 | Dein erster Termin | remove fear of the unknown | 3–4 step pills with image, duration, price range, CTA |
| 6 | Über die Behandlerin | people buy from people | photo left, name, qualifications, years, personal quote, CTA |
| 7 | Reviews 2 | trust before decision | 2–3 quotes matched to objections, beside real room photo |
| 8 | FAQ | last doubts | accordion, price first, 6–8 questions |
| 9 | Standort | can I get there | map, address, parking, transit, hours, entrance photo |
| 10 | Closer | mini hero | benefit headline, 3–5 check marks, proof, CTA + phone |

CTA in sections 1, 3, 5, 6, 7, 10 at least. (Sticky WhatsApp or phone button on mobile: out of scope in the desktop-only workflow, see P10.)

**Visual system:** 3 brand colours (one dark, two light) + one CTA accent. 2 fonts. Alternating light and dark bands. Headline 3–4× body. Body ≥ 16 px, 18 px mobile. 8-pt spacing. Button radius about 12 px for calm or clinical brands. No autoplay animation. Icons for value props. Real photos only, GPT images in the look of the real practice.

---

## P1. Virtual therapy practice page (Src: 042) — closest to a healing practice

- Hero: headline left "Finally feel understood, supported and in control from the very first session" in 3 lines at about 54 px; body = pain + 3 value props; primary button "Book free consult" (12 px radius) + phone number as outline button; practitioner photos right.
- Trust strip: stats box (people helped, happy with first match, reply within 10 minutes) with 3 avatars and stars; check marks under CTA (virtual, no wait list, 8am–10pm); insurance logo strip.
- Section order: hero → stats → pain section (short sales letter, bold phrases) → wall of love (Google reviews with headline per review) → value prop "someone who cares" → value prop "problem solvers" → 4-point icon section → video reviews → how it works (4 step pills) → therapist slider (photo, name, speciality pills, quote) → insurance logos → scrolling text band → three colour-coded "real quotes" boxes → FAQ → closer (3 steps + form + proof) → footer.
- CTA design: same button in every section; same check marks under every CTA; sticky phone + CTA on mobile; CTA leads to a calm contact page because the audience is anxious.
- Typography / visual: serif headline (Newsreader), sans body (Lato), 3 brand colours (primary pink, light pink, dark grey body), alternating bands, highlight pill behind key words, soft image backplates, custom graphics on photos, mobile at 390 px with 5–6 reviews stacked.
- Why it matters for 741: emotional, trust-based service, people buy the person, dual CTA, calm contact path.

## P2. Luxury closet lead page rebuild (Src: 046) — the "proof first, then situation" page

- Hero: Google rating at the very top; benefit headline + functional benefit; sub-headline starts with the pain ("tired of messy closets") then lists 4 USPs; CTA with reassurance (fast response, financing, warranty); large real product image.
- Trust strip: proof 2 stacked next to proof 1 in the hero; mobile stacks vertically.
- Section order: hero → short pain/benefit → Google review text with photo of the real result → value props → how it works ("seamless three-step process") → closer with form on the right and background image.
- CTA design: one CTA, reassurance under it, repeated; closer mirrors the hero.
- Typography / visual: old page had "who we are" headline, "how it works" first and a review carousel; rebuild gave +282 % and +109 % in two cases.

## P3. Kitchen and bathroom remodel page (Src: 022, 034) — the "situation before/after" section

- Hero: emotional headline ("finally get the bathroom you've been wanting"); sub-headline pain → 3 benefits (family team, no subcontractors, on time); image side = scrolling stack of real work and team photos; "Book free consult" + phone side by side; reassurance: no subcontractors, transparent pricing, satisfaction guarantee.
- Trust strip: two proof blocks above the fold.
- Section order: hero → graphical situation section (old room with downside overlay beside new room with benefits) → proof → value props → how it works → closer.
- Why it matters for 741: the situation section can show "so fühlt es sich jetzt an" vs. "so läuft ein Termin bei mir" without any healing claim.

## P4. Hair-loss clinic rebuild (Src: 028, 064) — the "one action, short hero" page

- Hero: old page had 8 lines of text, two offers, "Contact us", venue image. New: 2–3 sentences, one action, benefit CTA, rating "5/5, 800+ reviews" at the top, stats row (years, people helped).
- Trust strip: rating at the top, stats row, specific testimonial instead of a generic quote.
- Section order: hero → proof (Google traffic) → situation + solution → value props (process, how it works) → success stories → closer with short form (replaced calendar booking).
- CTA design: CTA after each section; reassurance under each; form instead of calendar.
- HWG note: the example promises hair growth in 12 weeks. For a German practice the headline carries the felt outcome and service facts only.

## P5. Local service page with keyword H1 (lawn care, Src: 048) — the SEO + conversion hero

- Hero: H1 tag "Lawn care services in [city]" styled small; large visible headline "Own the best lawn on your block"; lead form in the hero because traffic is high-intent search; background image.
- Trust strip: proof 1 and 2 (reviews, guarantee).
- Section order: hero → situation → proof → value props → proof → how it works → FAQ → closer.
- Why it matters for 741: this is how the keyword + city stays in the H1 while the hero still sells. For a practice the form becomes the WhatsApp CTA block.

## P6. Solar panel cleaning page (Src: 022) — the "wall of love right after the hero" page

- Hero: standard hero (benefit headline, two proofs, CTA, reassurance, image).
- Trust strip: directly after the hero a wall of love with many open reviews; proof headline "join thousands who …".
- Section order: hero → wall of love → value props → FAQ with simple guarantee badge → closer (headline, proof, phone number, form on the right with 3–4 "what to expect" bullets, another proof below).
- Mobile: reviews shown open one by one, no carousel.

## P7. Contact / closer block (Src: 036, 046, 048, 061, 064) — the standard high-converting form block

- Headline: benefit and action ("Dein erster Schritt zu …"), never "Kontakt".
- Left: 3–5 check marks of what happens next (reply within X, first call 15 min, no obligation). Testimonial below.
- Right: form with max 4 fields, single column, labels above fields, one "Name" field; or the WhatsApp button block with prefilled message.
- Under the button: reassurance line or one short review.
- Mobile: everything stacks in one column.

## P8. Thank-you / after-contact pattern (Src: 042)

- Confirmation line ("Deine Nachricht ist da. Daniela meldet sich bis …").
- Photo of the practitioner, optional 30-second "what to expect" video.
- FAQ, then proof.
- For WhatsApp: the auto-reply carries the same content in 3 lines.

## P9. Premium service hero hierarchy (HVAC, dentistry, Src: 021, 029, 035)

- Order the eye travels: image → bold headline in brand colour → subdued smaller body text → big CTA in the same colour family. Headings 48–64 px, body 16–20 px, 3–4 colours, 2 fonts, 8-pt spacing.
- Badges on a grey bar so they do not compete with the CTA. Custom brand shapes repeated in icons and image masks.
- Reported: +64 % conversion from the hierarchy fix alone.

## P10. Mobile 390 px rules (Src: 005, 007, 042, 063)

> Out of scope in the CRO homepage workflow (desktop only, Martin 2026-10-11). Kept for the later mobile workflow.

- Image above the text. Headline max 3 lines. Body cut to 3 lines. One proof line. CTA and reassurance in the first screen.
- Logo and header small. No announcement bar.
- 5–6 reviews stacked, "mehr anzeigen". Steps and value props open, no carousel.
- Sticky bottom bar: WhatsApp (primary) + phone.
- Tap targets ≥ 44 px. Body 18 px.

---

## Choosing the pattern for a client (Step 2)

1. Default: P0 blueprint with the P1 visual mood for emotional practices (therapy, Heilpraktiker, Ayurveda) or the P9 hierarchy for clinical practices (Physio, Zahnarzt, Steuerrecht-like calm brands).
2. If the brand needs a "situation" section: use P3 as the visual idea for section 3.
3. If the current page has one big flaw (long hero, two offers, "Kontakt" button): use P4 as the before/after reference in the diagnosis.
4. Contact block always P7. Closer always a mini hero (P0 row 10).
5. Mobile always P10.
