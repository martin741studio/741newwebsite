# CRO Homepage — Motion and Highlight Spec (draft for Martin's review)

Status: APPROVED by Martin 2026-10-11 (all five recommendations accepted). Fixed input to Step 6 (prototype build) for every client. Per-client overrides only when the brand needs them, written to `07-prototype/motion.md`.

**Scope (Martin, 2026-10-11): this workflow builds desktop only.** Everything about mobile (smaller reveal distance, tap feedback, the sticky mobile bar) applies only to a later mobile build. All other rules apply to the desktop prototype.

Purpose: define how the page moves and what each section highlights, so the prototype feels calm, smooth and a little alive, never busy. The CRO library rule applies throughout: no autoplay, no parallax, motion only where it explains or guides the eye (rules.md R9.7, R9.10; patterns.md "No autoplay animation").

---

## 1. Principles

1. **One highlight per section.** Each section has exactly one element that gets a small, deliberate motion. Everything else in that section is still. The highlight always points at the section's job: the CTA in the hero, the stars in the proof strip, the connecting line in the steps.
2. **Calm, smooth, little.** Motion is short, soft and rare. If a visitor notices the animation as a thing in itself, it is too much. The test: it should feel like the page settling into place, not performing.
3. **Reveal once, then rest.** Sections build in as the visitor scrolls to them, one time. Nothing re-animates when scrolling back up. After the reveal, the only things that still move are hover states and the two breathing CTAs (hero and closer).
4. **Motion guides toward the CTA.** Where a motion has a direction, it leads the eye toward the primary action: the step line draws toward the last step, hover arrows nudge toward "Mehr erfahren", the proof stars fill toward the "Alle Bewertungen lesen" link.
5. **Reduced motion is respected.** If the visitor's device asks for reduced motion, all movement is replaced by plain opacity fades, and the breathing CTAs stay still. Nothing is lost, only the motion.
6. **Only transform and opacity animate.** No animated widths, heights, colours on large areas, or layout changes while revealing. This keeps it smooth on older phones and avoids layout shift.

## 2. Global motion settings (used by every section)

| Setting | Value | Why |
| --- | --- | --- |
| Reveal distance | 16 px up (mobile), 24 px up (desktop) | enough to feel like settling, too little to feel like sliding |
| Reveal duration | 500 ms | smooth, not slow |
| Easing | `cubic-bezier(0.22, 1, 0.36, 1)` (ease-out, soft landing) | calm deceleration, no bounce |
| Stagger between siblings (cards, steps, quotes) | 90 ms | reads as a sequence without feeling like a queue |
| Reveal trigger | element enters the viewport by about 20 % of its height | starts before the visitor stares at empty space |
| Reveal count | once per page load | rule 3 |
| Hover transition | 180 ms, same easing | responsive, not snappy |
| Tap feedback (mobile) | scale 0.98 for 120 ms on press | confirms the touch |
| Breathing CTA | scale 1 → 1.025 → 1 over 4.5 s, soft shadow grows with it, ease-in-out, continuous, pauses on hover | slow enough to be felt, not seen |
| Sticky mobile bar | slides up 24 px + fades in over 300 ms when the hero CTA leaves the viewport; stays until the closer section is in view, then slides back down | one CTA visible at all times, never two stacked |
| Reduced motion | all translate/scale set to 0, fades stay at 300 ms, breathing off | rule 5 |

Hero is the exception to the scroll trigger: it reveals immediately on page load, no scroll needed, in this order: headline, body text, CTA pair, reassurance line, then the portrait, 90 ms apart.

## 3. Per-section highlight (one each)

| # | Section | The one highlight | Motion | Trigger |
| --- | --- | --- | --- | --- |
| 1 | Hero | Primary CTA "Termin buchen" | breathing (see settings); on hover: lifts 2 px, shadow deepens, arrow nudges 4 px right | page load, continuous |
| 2 | Proof strip | The five stars | fill in left to right, 80 ms apart, from outline to gold; the "5,0" fades in with the last star | enters viewport |
| 3 | Fünf Themen | The five icons | each icon scales from 0.85 to 1 as its card reveals; on hover the card lifts 4 px, icon stays | staggered reveal |
| 4 | So arbeite ich | The "Mehr erfahren" arrows | cards reveal staggered; on hover the image inside zooms to 1.03 and the arrow slides 4 px right | staggered reveal, hover |
| 5 | Vier Schritte | The connecting line | line draws from step 1 to step 4 over 900 ms; each number badge fills with the brand colour as the line reaches it; step text fades in just after its badge | enters viewport |
| 6 | Über die Behandlerin | The credential line under the paragraph | portrait fades in from the left, text from the right, 24 px; then a thin underline draws beneath the credential line over 500 ms | enters viewport |
| 7 | Bewertungen | The stars on each card | three cards reveal staggered; stars fill left to right per card, 60 ms apart; the Google mark fades in last | staggered reveal |
| 8 | FAQ | The open question | accordion opens over 250 ms (height + content fade), chevron rotates 180°; the open question's text shifts to the brand colour; only one open at a time | click / tap |
| 9 | Standort | The map pin | map image fades in; the pin drops 12 px into place with one soft settle (no bounce loop) | enters viewport |
| 10 | Abschluss | Primary CTA "Termin buchen" | same breathing as the hero; the three reassurance points fade in 90 ms apart before the buttons | enters viewport, then continuous |

Rule check: the hero and the closer are the only two places with a continuous motion, and it is the same motion, on the same element, the primary CTA. That keeps the eye on the one action the page exists for.

## 4. What does not move (fixed list)

- No parallax on any background or photo.
- No autoplay carousels or sliders anywhere. Reviews and themes are laid out open.
- No looping decorative animations: no floating leaves, no drifting gradients, no animated backgrounds, no shimmer.
- No motion on body text or headlines beyond the one-time reveal fade.
- No animation that re-triggers on scrolling back up.
- No bounce or elastic easing. The one "settle" on the map pin is a single soft ease-out, not a bounce.
- No hover animations that move text out from under the cursor.
- No motion on the sticky mobile bar except its one slide-in and slide-out.

## 5. Accessibility and performance

- `prefers-reduced-motion: reduce` → every reveal becomes a 300 ms opacity fade with no translate or scale; breathing CTAs are static; the step line appears instantly; the FAQ still animates height (it is functional, not decorative) but faster, 150 ms.
- All animations use `transform` and `opacity` only. The FAQ height change is the one exception, and it is user-initiated.
- Reveals use IntersectionObserver, one observer for the whole page, elements unobserved after they reveal.
- Reserved space for every image before it loads, so no layout shift during reveals.
- No animation library. Plain CSS keyframes and about 30 lines of JavaScript, inline in `index.html`, so the prototype stays one file.

## 6. Implementation notes for Step 6

- Class `.reveal` on every section's inner content block, with `.reveal--1` … `.reveal--n` for stagger order inside a section. The observer adds `.is-in` once.
- Class `.cta--breathe` on the two primary CTA buttons only.
- The step line is an SVG path with `stroke-dasharray`/`stroke-dashoffset` animated to 0; badges use a `transition-delay` matched to the line's progress.
- Stars are inline SVG with a fill transition, delayed per star.
- The sticky bar is a fixed element toggled by an observer on the hero CTA and on the closer section.
- Everything in this spec is checked in the self-check before Checkpoint 2: one highlight per section present, nothing from section 4 present, reduced-motion verified by toggling it in the browser.

## 7. Decisions (Martin, 2026-10-11)

1. Breathing CTA: continuous.
2. Proof strip "5,0": fades in with the stars, no count-up.
3. Map pin: one-time drop.
4. About section: credential underline draws.
5. Scope: default for every client, overrides only when a brand needs them.

Implementation note: the step line and the pin drop use transform and opacity only (scaleX/scaleY for the line, translateY for the pin), which keeps rule 6 of the principles.
