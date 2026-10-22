# Decisions — personal-posts (Martin's gos, with date and his words)

## Design inputs (grilled live in the chat-base session before this build, 2026-10-22)

Martin's own words, carried into this build as the brief (see `inputs-grill.md` for the full write-up): platforms Instagram/Facebook/LinkedIn/X, dictated raw thought as input, every post needs his own explicit go, 3-4x/week cadence he triggers, images via the existing social-visuals-workflow for IG/FB only, English, direct/polarizing tone with no corporate hedging, client results need that client's own go or go anonymized, voice built from one live interview since he has no post history.

## Degrees of freedom (2.5, Rule R1.7)

| Step | Fragile/deterministic -> script | Open/qualitative -> guided prompt |
| --- | --- | --- |
| Slop lint | `slopmonster/tools/deslop.py` (regex, run not read) | — |
| Cleanse (only below 5/5) | `slopmonster/tools/cleanse.sh` (external rival-model pass) | — |
| Claim check | — | heuristic: trace every number to a real source before drafting; ask Martin if none found |
| Client-go check | — | heuristic: ask Martin via card when no go is on file for that specific post |
| Core argument drafting | — | guided by `voice-profile.md` (stance, hard no's, 2-3 example shapes) |
| Platform adaptation | — | guided by `voice-profile.md` §"Per-platform adaptation" (length/shape per platform) |
| Image build | reuse of `social-visuals-workflow` scripts (already deterministic) | — |

## Checkpoint 1 clarifications (Martin, 2026-10-22, cards)

Martin's first answer to the CP1 go card: "I want you also to integrate into this workflow our content pool workflow and our writing workflow, so we avoid AI slop and write it more engagingly according to our headline prompting, etc." Two follow-up cards resolved the scope:

1. **Content-pool role:** "Topic backlog, same idea (Recommended)" — personal-posts keeps a small backlog of post topic ideas (one per topic lane: agency insight, SEO opinion, client-result candidate, mindset), the same role `content-pool` plays for SEO pages, so Martin is not always starting cold. His own raw dictated thought stays the primary input per post; the backlog is a secondary "what should I post about" entry point. NOT content-pool's real DataForSEO/GSC scoring machinery — too heavy for a personal-voice backlog.
2. **Writing-workflow depth:** "Reuse its rule files directly (Recommended)" — personal-posts reads `~/.claude/skills/content-writing/references/copy-rules.md` (headline/DR formulas, C2.1 hook pattern, C2.8 no-dashes, C4.1 scanability, C4.5 anti-slop, C8.4 claim-proof pairing) and the slop scripts directly, adapted for post length. No cross-call into the `/content-write` skill itself — that skill is scoped to client-voice page/blog copy, this one to Martin's own voice. (Path corrected during 4.2 functional test: the skill is installed globally at `~/.claude/skills/content-writing/`, not under the project's `.claude/skills/`.)

## Checkpoint 1 (2.6) — pending

Design (this file + `use-cases.md`, `test-scenarios.md`, `pipeline.md`) and the hand-drafted real post (`hand-run.md`) are ready for Martin's go, now updated with the topic-backlog and copy-rules integration above. Recorded below once he answers the card.

**Martin's go, 2026-10-22 (card):** "Go, build it (Recommended)" on the updated design (topic backlog + copy-rules mapping included). Design approved, build authorized.

## Knowledge-base integration (Martin, 2026-10-22, mid-build)

Martin sent a NotebookLM link ("The Content Marketing Playbook", 37 sources) during the build and asked to integrate its strategy into the workflow. Queried it directly (signed in as martin.stylectric@googlemail.com, verified via account switcher) for the rules specific to a founder's own personal posts. Full extraction and sourcing in `.claude/skills/personal-posts/references/strategy-notes.md`.

Integrated directly (enriches the approved design, does not change its shape): no-outbound-links-in-body rule (now scripted in `check_lengths.py`), "How I not How To" framing, damaging-admission technique, numerical-specificity and negative-framing citations backing rules already in the voice profile.

Flagged, decided by card: the notebook's "Test -> Record -> Contextualize" repurposing pipeline (post a raw idea to X first, only expand what lands into LinkedIn/long-form). Martin's answer: "Keep current pipeline (Recommended)" — stay with the simultaneous 4-platform draft already approved at checkpoint 1; revisit test-first repurposing once there's real post history.

## Checkpoint 2 (5.1) — Martin's go, 2026-10-22 (card)

Shown: scorecard 98% (53/54), no blocking zeros, and one real output (the "we're all a family" post: 4 platform drafts, all 5/5 slop-clean and link-checked, plus the rendered non-branded Instagram image). Martin's answer: "Go, ship it (Recommended)." Proceeding to register, commit, and write the memory file.
