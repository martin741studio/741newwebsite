# Voice profile — Martin's personal posts

Built from one live interview (2026-10-22), not from old posts. Martin has never posted before, so this file is the only source of tone. Treat every rule here as provisional until Martin corrects it on a real draft; the first corrections update this file (house rule: patch the skill, not a one-off reply).

## Core stance

- Contempt for corporate-platitude dishonesty. Example target: "we're all a family."
- Belief: competition and direct confrontation produce more real freedom and empathy than performative niceness.
- Prefers an uncomfortable truth over a comfortable narrative.
- Willing to be hard or polarizing. The post can make some readers push back.

## What the voice sounds like

- States the claim first, then the reasoning. Not: build-up, then reveal.
- Names the thing it is against by its real shape ("we're a family" line), not a vague gesture at it.
- Draws a line between the surface claim and what is actually true underneath.
- Short, declarative sentences mixed with one longer sentence that carries the real argument.
- Ends on the stance, not on a summary or a call to engage ("thoughts?", "agree?").
- **"How I" not "How to"** (`references/strategy-notes.md`): speak from what Martin did and saw, never from prescribing what the reader should do. "Here's what I did and what I saw" over "here's what you should do" — the first is unfalsifiable and builds rapport, the second reads as lecturing.
- **Negative/contrarian openings outperform positive framing** and match the voice already — lean into it, do not soften a sharp opening into a positive-sounding one.
- A real, specific number in the opening line beats a vague version of the same claim — another reason the claim-proof pairing rule (C8.4 below) matters beyond just honesty.

## Hard no's (Martin's own limits, do not soften these into "safe")

- No empty motivational-poster lines: "success is a journey", "hustle harder", "trust the process".
- No false-modesty humblebrag framing: "I didn't want to share this, but...", "I almost didn't post this".
- No invented or exaggerated numbers. Every number real and sourced (`claims-need-real-data`).
- No hedge-everything corporate softening ("in my humble opinion", "no offense to anyone, but"). State the view straight.
- No forced engagement bait ("comment YES if you agree", "tag someone who needs this").
- No throat-clearing openers: "the truth is", "to be honest", "honestly". State the claim; do not announce that you are about to be honest about it. (Found in the 4.2 functional test: a first-pass LinkedIn draft scored 4/5 on the slop lint for exactly this.)

## Style defaults (not a hard rule, applied unless it kills the voice)

- Avoid stacking multiple em-dashes in one post; split into separate sentences instead. Reason: it is both a slop-lint tell and a cadence that reads as written-for-you rather than said-by-you.
- One real example or number per post where the topic allows it, never a stacked list of three.
- Keep contractions and the occasional sentence fragment. A rough edge reads as a person, not a caption generator.
- **No outbound links in the post body, ever.** If a link matters, it goes in the first comment, never the post text itself (`references/strategy-notes.md`; `scripts/check_lengths.py` warns if a draft contains a bare URL). This is unrelated to the no-auto-post rule — it is a drafting rule about where a link lives, not permission to post one.
- A real, owned flaw or limitation stated plainly (not a hedge) can open or anchor a post — it reads as more credible than a claim with no acknowledged edge. Optional, not required on every post.

## Topic lanes (all four in rotation)

1. Agency insights / build-in-public — real 741 numbers and decisions.
2. SEO/marketing opinions.
3. Client results — anonymized by default (industry + real number, no name, no logo); named only with that client's own go for that specific post.
4. Personal/mindset pieces.

## Headline-prompt / copy-rules reuse (Martin's go, 2026-10-22)

Draft the opening line of every post the way the DR hero formula builds a headline, scaled down to one sentence instead of a page hero. Source: `~/.claude/skills/content-writing/references/copy-rules.md` (741 Content-Raster). Read directly, never call `/content-write` — that skill is scoped to client-voice page and blog copy.

- **C2.1 pattern, adapted:** the opening line states the claim plainly, then the post gives the one reason to believe it (not three). Never "here's a thought" or "something I've been thinking about" as an opener.
- **C2.8 no dashes:** stack of em-dashes reads as written-for-you; split into separate sentences instead.
- **C4.1 scanability:** short sentences, 2 sentences per paragraph at most, one idea per paragraph.
- **C4.5 / slop gate:** if it sounds like AI or marketing copy, rewrite in the words Martin actually uses. `slopmonster/tools/deslop.py` is the automated check for this (step 6 of the workflow).
- **C8.4 claim-proof pairing:** a stated number or result sits next to its source in the same post, never floating unattributed.

## Per-platform adaptation (same core take, different shape)

- **LinkedIn:** full argument, 3-6 short paragraphs. The platform people expect reasoning from. No hashtags.
- **X/Twitter:** the sharpest single version of the claim, under 280 characters where possible; if the argument needs more, a short thread (2-4 posts), first post standalone.
- **Instagram caption:** shorter than LinkedIn, pairs with the image; the line that would work as a pull-quote on the image goes first.
- **Facebook caption:** close to the Instagram length and tone, slightly more conversational opening line; same image.

See `platform-specs.md` for the checkable length rules.

## Image (Instagram + Facebook, Martin's go 2026-10-22)

No 741 branding. These are Martin's personal posts, not agency marketing material. Build the image with `scripts/build_personal_image.py "<pull-quote>" "Martin Drendel" <platform>`: it reuses the existing headless-Chrome render pipeline (`social-visuals-workflow`) but with a new, separate, minimal template (`07_social/templates/personal_post_quote.html`) — plain background, no logo, no 741 colors, just the pull-quote and "Martin Drendel" underneath. Never point a personal post at the 741-branded templates (`linkedin_post.html` and similar) — those are client/agency material.
