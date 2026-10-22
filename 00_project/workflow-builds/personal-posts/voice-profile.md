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

## Hard no's (Martin's own limits, do not soften these into "safe")

- No empty motivational-poster lines: "success is a journey", "hustle harder", "trust the process".
- No false-modesty humblebrag framing: "I didn't want to share this, but...", "I almost didn't post this".
- No invented or exaggerated numbers. Every number real and sourced (`claims-need-real-data`).
- No hedge-everything corporate softening ("in my humble opinion", "no offense to anyone, but"). State the view straight.
- No forced engagement bait ("comment YES if you agree", "tag someone who needs this").

## Style defaults (not a hard rule, applied unless it kills the voice)

- Avoid stacking multiple em-dashes in one post; split into separate sentences instead. Reason: it is both a slop-lint tell and a cadence that reads as written-for-you rather than said-by-you.
- One real example or number per post where the topic allows it, never a stacked list of three.
- Keep contractions and the occasional sentence fragment. A rough edge reads as a person, not a caption generator.

## Per-platform adaptation (same core take, different shape)

- **LinkedIn:** full argument, 3-6 short paragraphs. The platform people expect reasoning from. No hashtags.
- **X/Twitter:** the sharpest single version of the claim, under 280 characters where possible; if the argument needs more, a short thread (2-4 posts), first post standalone.
- **Instagram caption:** shorter than LinkedIn, pairs with the image; the line that would work as a pull-quote on the image goes first.
- **Facebook caption:** close to the Instagram length and tone, slightly more conversational opening line; same image.

## Topic lanes (from the grill, all four in rotation)

1. Agency insights / build-in-public — real 741 numbers and decisions.
2. SEO/marketing opinions.
3. Client results — anonymized by default (industry + real number, no name, no logo); named only with that client's own go for that specific post.
4. Personal/mindset pieces — like the test opinion in `voice-interview-raw.md`.

## Headline-prompt / copy-rules reuse (Martin's go, 2026-10-22)

Draft the opening line of every post the way the DR hero formula builds a headline, scaled down to one sentence instead of a page hero:

- **C2.1 pattern, adapted:** the opening line states the claim plainly, then the post gives the one reason to believe it (not three). Never "here's a thought" or "something I've been thinking about" as an opener — that is the build-up `voice-profile.md` already forbids.
- **C2.8 no dashes:** house rule for client copy, applied here too. Stack of em-dashes reads as written-for-you; split into separate sentences instead (matches the style default above).
- **C4.1 scanability:** short sentences, 2 sentences per paragraph at most, one idea per paragraph.
- **C4.5 / slop gate:** if it sounds like AI or marketing copy, rewrite in the words Martin actually uses. `slopmonster/tools/deslop.py` is the automated check for this; see Workflow step below.
- **C8.4 claim-proof pairing:** a stated number or result sits next to its source in the same post, never floating unattributed.

Source: `~/.claude/skills/content-writing/references/copy-rules.md` (741 Content-Raster). Read directly, not called as a sub-skill — `/content-write` is scoped to client-voice page and blog copy.

## Topic backlog (secondary entry point, Martin's go 2026-10-22)

When Martin has no specific thought ready and asks "what should I post about" (or similar), the skill offers 2-3 open ideas from the backlog instead of leaving him to start cold — the same role `content-pool` plays for SEO pages, scaled down to a flat idea list (no DataForSEO/GSC scoring, that is too heavy for a personal-voice backlog).

- **File:** `00_project/assets/741studio/personal-posts/topic-backlog.json` — array of `{id, lane, idea, source, status, added, used_date}`. `lane` is one of the 4 topic lanes above. `status` is `open`, `used`, or `skipped`.
- **Adding ideas:** when a chat produces a usable fragment that is not used right away (e.g. Martin mentions something in passing), the skill offers to add it to the backlog rather than losing it.
- **Martin's own dictated thought stays the primary input for every real run.** The backlog only fills the gap when he has none ready; it never auto-selects and posts a backlog idea without him restating or approving it as the actual post content.
