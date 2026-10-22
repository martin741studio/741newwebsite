# Voice profile — 741 Studio (business account)

Built from one live interview (2026-10-22, card "Test opinion"; raw material in `00_project/workflow-builds/personal-posts/business-voice-interview-raw.md`). Separate from `voice-profile.md` (Martin's personal account) — same house mechanics (slop gate, no-links, claim check), different account, different voice, different image branding. Martin's tone call, 2026-10-22: "Direct but professional" — not a toned-down version of the personal voice, a different register for a different purpose.

## Core stance

- Educational first. The core 741 Studio move: close a real gap in understanding (SEO, marketing, AI, agency operations), not sell a service in disguise.
- Contrarian where it's earned by evidence, not provocative for its own sake: challenges the "AI makes agencies unnecessary" narrative with what Martin actually sees (companies try DIY, come back to agencies).
- The real value 741 sells is execution infrastructure (routine, conditioning, long-term distributed responsibility) — not access to information or tactics, which is already abundant. "Not enough education" is the real gap, not "not enough content."

## What the voice sounds like

- Direct, honest, no corporate hedging — same house standard as the personal account.
- Topics stay educational and business-grounded (SEO, marketing, AI, agency reality, execution systems), not personal-political or social commentary — that's the personal account's territory, not this one.
- Credibility over polarization: the goal is "this person clearly knows what's actually true in this industry," not "this person will say anything to get a reaction."
- States the real mechanism, not just the critique: don't just say "AI doesn't replace agencies," say what the actual gap is (execution over months, not information).

## Hard no's (same house standard as the personal account, `voice-profile.md`)

- No empty motivational-poster lines, no false-modesty humblebrag, no invented or exaggerated numbers (`claims-need-real-data`), no hedge-everything corporate softening, no forced engagement bait, no throat-clearing openers, no fake luxury entrepreneurship, no forced controversy, no exaggerated certainty, no invented personal stories or client stories.
- No disguised pitch. An educational post that quietly turns into a sales pitch for 741 breaks the "educational first" stance above — if a post needs a CTA, it goes in a comment or bio link, never worked into the post body as a soft sell.
- Client transformations follow the SAME rule as the personal account: anonymized by default (industry + real number, no name, no logo); named only with that client's own go for that specific post.
- An unclear or unconfirmed detail from a dictated thought is never guessed into a post — confirm with Martin first (see personal account's "Accuracy rules", same standard applies here).

## Topic pillars (741 Studio business account)

1. Educational agency content — how SEO, marketing, AI, or ranking actually works, the parts most people get wrong.
2. Client transformations — anonymized by default, named only with that client's go.
3. Agency operations / build-in-public — real 741 decisions and numbers.
4. Execution reality — why access to information or AI tools isn't the bottleneck; routine, conditioning, and long-term distributed responsibility are.
5. Measurable results — real, sourced numbers only.

## Per-platform adaptation

Same shape as the personal account (`voice-profile.md` §"Per-platform adaptation"): LinkedIn full argument (3-6 short paragraphs, no hashtags), X sharpest single version (thread if needed), Instagram/Facebook caption pairs with the image, pull-quote line first.

## Image (Instagram + Facebook, Martin's go 2026-10-22)

Full 741 branding — the same visual system as every other 741 social asset: yellow `#fac118`, dark background `#111`/`#252525`, Anton headline font, logo. Build with `scripts/build_business_image.py "<pull-quote>" <platform>`: renders `07_social/templates/business_post_quote.html` through the same headless-Chrome pipeline as the personal account's image script, but the 741-branded template, not the plain one. Never use the plain personal template (`personal_post_quote.html`) for a business post, and never use the plain non-branded script (`build_personal_image.py`) here.

## Trigger

`/741-post <thought>` — separate command from `/personal-post`, deliberately, so the account (and therefore the voice and the branding) is never ambiguous.
