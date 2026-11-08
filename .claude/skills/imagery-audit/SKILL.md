---
name: imagery-audit
description: Audit a website's or an ad's imagery against the direct-response conversion blueprint (Hormozi / Arsh Sanwarwala method): hero image, visual social proof, FUD-reducers, ad creative, with findings and fixes tied to what is on the page. Use on "check the imagery on <url>", "audit the images", "is my hero image converting", "review the ad creative", or when Martin drops a URL or ad screenshot and asks about the visuals.
---

# Imagery Audit — direct-response conversion blueprint

Score imagery as a **conversion mechanism**, never as decoration. Generic stock photos and office/handshake shots are automatic fails.

Part 1 = website imagery (input is a URL). Part 2 = ad creative (input is an ad or a screenshot of one). If both apply, run both.

## Workflow (live URL)

Check hero and proof sections at desktop and mobile (60% never scroll past the fold). Read every `<img>` with its `alt` and file name: they expose stock photos and show whether the image describes the outcome. Screenshot each proof section and each CTA with its surroundings. Reset the viewport to desktop afterwards.

**Blur litmus test:** hide all text, screenshot the hero.
```js
// via javascript_tool
[...document.querySelectorAll('h1,h2,h3,h4,p,span,a,button,li')].forEach(e=>e.style.color='transparent');
```
If the dream is still obvious from the image alone: pass. If not, the hero is decoration, not a mechanism.

For an ad or a pasted creative skip the browser and judge the image against Part 2.

## Part 1 — Website imagery

### Rule 1 — the hero visually represents the Dream Outcome
Show, don't tell. The hero shows the exact outcome the headline promises (the finished closet, the before/after, real high-performing clips). Not the office, not a handshake, not stock. Fail the blur test = fail the rule.

### Rule 2 — maximize VISUAL social proof
- Text-only reviews score low; audiences read them as easy to fake.
- Pair each claim with visual evidence: "lost 20 pounds" with a before/after photo, "generated revenue" with a real dashboard screenshot.
- Build a visual Wall of Love: screenshots of Google reviews, text messages and video thumbnails stacked floor-to-ceiling. **Carousels are a fail** (low engagement, they hide the best assets). Flag every testimonial slider.

### Rule 3 — FUD-reducers directly under the CTA button
Fear, uncertainty and doubt spike when the user decides to click. Put small recognizable trust badges under the button (money-back guarantee, secure checkout, warranty). Flag any primary CTA with nothing reassuring beneath it.

## Part 2 — Ad creative (Meta / Google)

The creative does the targeting: algorithms read image and copy to find the demographic.

### Rule 1 — Capture over Manufacture
- Highly produced ads (pro lighting, stages, corporate actors) get scrolled past on reflex. Raw converts: smartphone footage of the team doing the service.
- Static pattern-interrupts: images that look like medical-textbook diagrams, raw cell breakdowns or hand-drawn sketches, not polished banners.

### Rule 2 — the Local Service "Visual Loop" (best local format)
Splice raw before/after at site 1 and site 2. Show the arc arrival, team working, clean outcome. Proof cap: end on a screenshot of the client's real 5-star Google review.

### Rule 3 — Visual "Persona Callouts" (Meta static)
Plain white background, bold black sans-serif calling out the exact avatar ("If you run a B2B agency doing over $1M…"). Only for a large warm or retargeting audience with real brand authority. On cold traffic use a pattern-interrupt (story or diagram) instead.

## Output

A scored audit, most severe gap first:

| Rule | Status | What is on the page now | Exact fix |
|---|---|---|---|
| Hero = Dream Outcome | ❌ / ⚠️ / ✅ | … | … |
| Visual social proof | … | … | … |
| FUD-reducers under CTA | … | … | … |
| (ads) Capture over Manufacture / Visual Loop / Persona Callout | … | … | … |

- Every finding names the actual element on the page and the exact fix. Never invent metrics.
- Attach the hero screenshot and the blur-test screenshot as proof.
- Rank fixes by conversion impact; hero and under-CTA badges first.
- For a client or prospect deliverable, offer to publish the audit as an Artifact. German prospect copy in "du".
