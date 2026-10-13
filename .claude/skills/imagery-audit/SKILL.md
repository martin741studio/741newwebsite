---
name: imagery-audit
description: >
  Audit a website's or an ad's imagery against the direct-response conversion blueprint
  (Hormozi / Arsh Sanwarwala method). Score the hero image, visual social proof, FUD-reducers,
  and ad creative; return specific findings + fixes tied to what is actually on the page.
  Trigger on "check the imagery on <url>", "audit the images", "is my hero image converting",
  "scan the site imagery", "review the ad creative", "does this image sell the dream", or when
  Martin drops a prospect/client URL or an ad screenshot and asks about the visuals.
---

# Imagery Audit — direct-response conversion blueprint

Score imagery as a **conversion mechanism**, never as decoration. The brain processes images ~60,000× faster than text; ~90% of information to the brain is visual. Generic stock photos and office/handshake shots are automatic fails.

Two contexts: **Part 1 = website imagery** (hero + page). **Part 2 = ad creative** (Meta / Google). Pick the context from the input. If the input is a full URL, run Part 1. If the input is an ad, a creative, or a screenshot of one, run Part 2. If both apply, run both.

---

## Workflow (live URL)

1. Load the page: `mcp__Claude_Browser__preview_start {url}` (or `navigate` if the pane is open).
2. Capture the hero: `computer {action:"screenshot"}` at desktop, then `resize_window {preset:"mobile"}` + reload + screenshot. Mobile matters — 60% never scroll past the fold.
3. `read_page` → pull every `<img>`, its `alt`, its file name, and the section it sits in. File names and alt text expose stock photos and reveal whether the image describes the outcome.
4. Scroll the full page; screenshot each proof section and every CTA button with its surrounding area.
5. **Blur litmus test (power move):** inject CSS to hide all text, then screenshot the hero.
   ```js
   // via javascript_tool
   [...document.querySelectorAll('h1,h2,h3,h4,p,span,a,button,li')].forEach(e=>e.style.color='transparent');
   ```
   If the dream is still obvious from the image alone → pass. If not → the hero is decoration, not a mechanism.
6. Score each rule below. Every finding names the actual element on the page and the exact fix. Reset the viewport (`resize_window {preset:"desktop"}`) when done.

For an ad or a static creative image the user pastes, skip the browser steps and judge the image directly against Part 2.

---

## Part 1 — Website imagery

The above-the-fold (hero) is the most expensive real estate on the site. 100% of visitors see it; ~60% never scroll past it.

### Rule 1 — the hero visually represents the Dream Outcome
- **Show, don't tell.** The hero shows the exact outcome the headline promises — the finished luxury closet, the brighter-smile before/after, the carousel of real high-performing clips. Not the office. Not a generic handshake. Not stock.
- **Litmus test:** blur all text (step 5). Is the dream being sold still obvious from the image alone? If no → fail.

### Rule 2 — maximize VISUAL social proof
- Text-only reviews score low; modern audiences read them as easy to fake.
- **Pair each claim with visual evidence:** "lost 20 pounds" → before/after photo; "generated revenue" → real Stripe / dashboard screenshot.
- **Build a visual Wall of Love:** stack screenshots of Google reviews, text messages, and video thumbnails floor-to-ceiling. **Carousels are a fail** — low engagement, they hide the best assets. Flag any testimonial slider.

### Rule 3 — FUD-reducers directly under the CTA button
- Fears, Uncertainties, and Doubts spike the millisecond the user decides to click.
- **The fix:** small, recognizable trust badges / checkmarks under the button — money-back guarantee, secure checkout, warranty. This visual pattern-interrupt is credited with up to a 30% conversion lift.
- Flag any primary CTA with nothing reassuring beneath it.

---

## Part 2 — Ad creative (Meta / Google)

In paid, **the creative does the targeting** — algorithms (e.g. Meta "Andromeda") read the image + copy to find the demographic.

### Rule 1 — Capture over Manufacture (raw beats produced)
- Highly-produced "Mona Lisa" ads with pro lighting, stages, and corporate actors get scrolled past on reflex — they "look like ads".
- **Raw converts:** authentic B-roll / smartphone footage of the team actually doing the service (lawn care, painting, setup).
- **Static pattern-interrupts:** make static images look like medical-textbook diagrams, raw cell breakdowns, or hand-drawn sketches — not polished banners. This slips past the user's ad-detector.

### Rule 2 — the Local Service "Visual Loop" (highest-performing local format)
- Splice raw before/after at site 1 + before/after at site 2. Show the full arc: arrival → team working → clean/fixed outcome.
- **Proof cap:** end on a screenshot of the client's real 5-star Google review, tying result to authority.

### Rule 3 — Visual "Persona Callouts" (Meta static)
- Solid plain-white background, bold black sans-serif calling out the exact avatar: e.g. "If you run a B2B agency doing over $1M…".
- **Warning:** only for a large warm/retargeting audience with real brand authority. On cold traffic, use a visual pattern-interrupt (story or diagram) instead to build first trust.

---

## Output

Return a scored audit, most severe gap first:

| Rule | Status | What is on the page now | Exact fix |
|---|---|---|---|
| Hero = Dream Outcome | ❌ / ⚠️ / ✅ | … | … |
| Visual social proof | … | … | … |
| FUD-reducers under CTA | … | … | … |
| (ads) Capture over Manufacture | … | … | … |
| (ads) Visual Loop | … | … | … |
| (ads) Persona Callout | … | … | … |

- Attach the hero screenshot and the blur-test screenshot as proof.
- Rank fixes by conversion impact; put the hero and the under-CTA badges first.
- For a client/prospect deliverable, offer to publish the audit as an Artifact (private page, shareable link).
- Follow project rules: never invent metrics, never put personal data on a page, keep German prospect copy in "du".
