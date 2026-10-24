# Research note — content-format-board

## 1.1 Building block
**Skill**, `.claude/skills/content-format-board/`. Decision-tree reason (patterns.md §3, step 3): "Is it one repeatable procedure Martin triggers?" — yes, per client/prospect, on demand, no schedule, no parallel-worker fan-out needed. Same shape as `cro-homepage`, `personal-posts`, `local-seo-review-page` (sequential workflow with gates, patterns.md §4.1).

## 1.2 Library search
`grep -ril` for "garcia", "one shot", "ten shot", "yapping", "answer the public", "content format", "format library" across `00_project/knowledge/` returned no real match — confirmed still true (2026-10-24). Two false-positive word collisions found and ruled out: `design-video-notes/fq3wx-AR6B0-transcript.md` (unrelated Jack Roberts motion-design video, coincidental "one shot"/"yapping" word hits) and `hormozi-library/106-...mona-lisa-or-go-volume.md` (Hormozi talking about production polish trade-offs, coincidental "yapping" word hit, not a format taxonomy).

## 1.3 Freshness
Real source found and ingested: `00_project/knowledge/content-format-library/001-you-only-need-4-content-formats-alex-garcia.md`. Video "You Only Need 4 Content Formats to Blow Up Your Brand", channel Alex Garcia, published 2026-06-24 (≈4 months old), pulled 2026-10-24 via Apify `johnvc/YoutubeTranscripts` (not youtube-transcript-api — IP-blocked, R8.4). The library-freshness gate (<3 months) governs the meta-workflow knowledge base (official docs/blog/video index), not this skill's own reference source; flagged in the new library's `INDEX.md` instead with a re-verify-by date (2027-04-24) since the content is a durable production framework, not a time-sensitive claim.

Web search alone could not confirm the exact video — multiple wrong "Alex Garcia" candidates surfaced (a film producer, a chef, a Twitter marketer @alexgarcia_atx with a different bio). Asked Martin directly for the real link rather than guessing (`no-invented-reference-examples`); he supplied `https://www.youtube.com/watch?v=Q2T1kv0aAyA`.

## 1.4 Asset reuse
Checked `.claude/skills/` (full listing) and the 5 memory files named in the brief (`social-visuals-workflow`, `story-automation-system`, `content-pool-workflow`, `content-writing-workflow`, `741-youtube-channel-avatar`). No overlap: `content-pool` = SEO keyword/topic pool for pages+blog; `content-writing` = page/blog copy in client voice; `social-visuals`/`story-automation-system` = static image templates and Local-Falcon before/after result cards, not video-format strategy. `personal-posts` = Martin's/741's own account voice, explicitly out of scope per Martin's go (see `inputs-grill.md`). Nothing to reuse directly; the headless-Chrome render pattern from `social-visuals-workflow` is a candidate IF this workflow ever needs to render a visual board (not required for v1 — a markdown/sheet board is enough).

## 1.4b NotebookLM knowledge base (added at CP1, Martin's instruction)
Martin's NotebookLM notebook "The Content Marketing Playbook" (`notebook.google.com/notebook/7f6a765f-7a30-446e-9259-e1a497c318eb`, 36 sources, Google login = Martin's account) is the fourth knowledge source. Source list captured 2026-10-24: the Alex Garcia 4-formats video is in it, plus hook/retention/looping research (ReelForge, UGC Copilot, Socialync, Virvid), platform-algorithm reports (LinkedIn 2026, X, StoryChief, Hootsuite), trend-discovery tools (Exploding Topics, BuzzSumo, Answer Socrates), Hormozi content strategy, Jonah Berger virality, a "Deep Research Report" synthesis. Prior reuse: `.claude/skills/personal-posts/references/strategy-notes.md` extracted the TEXT-post findings from the same notebook on 2026-10-22 and explicitly left video findings out — so this skill gets its own extraction (`references/playbook-notes.md`), queried live in the notebook. Internal only: the notebook's named sources are never shown to a client.

## 1.5 Rules and pattern applied
- R1.1 (define 2-3 use cases before anything else) → step 2.1 next.
- R1.7 (degrees of freedom: deterministic script vs heuristic) → question sourcing (DataForSEO/Apify calls) = scripts; format-matching and quality judgment = heuristics in SKILL.md.
- R8.4 (Apify transcript actor, not youtube-transcript-api) → already applied above.
- R8.1/no-method-sources-in-deliverables → format taxonomy is internal; client-facing board uses 741's own neutral labels, never "Alex Garcia" or "Cut 30".
- Pattern §4.1 (sequential workflow with gates) → the build's checklist shape.

## Open questions going into step 2
- Real taxonomy has 4 formats (One-Shot, 10-Shot, Yap, How/Why-We-Do-It), not the "SM Volume umbrella + Authority Educational YouTube" framing in Martin's original paraphrase — the video's actual pre-step is a 3-question content-level readiness check (ops/quality/team-skill at 2x volume), not a named format. Correct this at design review (step 2).
- Martin's "~6:00 structure" detail for 10-Shot LV2 does not appear in the real transcript — drop it rather than keep an unverified number.
