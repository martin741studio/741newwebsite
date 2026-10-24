# Research note — marketing-grill

## 1.1 Building block
Skill, triggered in chat (`/marketing-grill` or natural phrase), not a subagent, hook, or routine. Reason: it is one repeatable procedure Martin triggers on demand, needs his live presence to answer AskUserQuestion cards, and has no fixed schedule (R0.1, R0.2, workflow-library `_derived/rules.md`). Not `disable-model-invocation: true` — the workflow has no side effects of its own (no sending, no spending, no live-site writes); it only produces a document.

## 1.2 Library search
`grep -ril "grill|interview|AskUserQuestion" 00_project/knowledge/workflow-library/` — hits in `_derived/rules.md` (R1.4: let Claude interview with AskUserQuestion for large features; R2.6: checklist pattern) and `_derived/patterns.md` §4.1 (sequential workflow with gates, the shape 741 deliverables use). No existing library pattern is named "grill" specifically; the closest proven in-house precedent is the `morning-grill` skill itself (card-based decision pattern, `state/cards.json` ledger, max-cards-per-round rule) — reused as the direct template for the card mechanics here.

## 1.3 Freshness
`workflow-library/INDEX.md`: built 2026-10-11, next refresh due 2026-11-22 — within the 3-month/6-week window, no refresh needed for this build.
Hormozi library (`hormozi-library/INDEX.md`): exported 2026-10-06, 109 sources, 19 days old — within the 6-week freshness window, no mandatory refresh. BUT: the live NotebookLM notebook (ed95df8f-28d3-4c6b-aea9-408154c442ee) now shows **120 sources** vs. 109 locally exported — 11 new sources since 06.10. Flagged to Martin as a card (export the 11 new ones with the same method, per `hormozi-library-local` memory's own update instruction).
Second notebook (7f6a765f-7a30-446e-9259-e1a497c318ee, named in the brief): does not resolve ("Notebook not found") under Martin's logged-in account (martin.stylectric@googlemail.com, verified). Not exported. Flagged to Martin as an open item — see `decisions.md`.

## 1.4 Existing assets (coverage map)
See `coverage-map.md`. Summary: no existing skill does a Martin-facing "what marketing to do" grill. Closest adjacent skills to route INTO, not duplicate: `content-format-board` (organic-content execution), `personal-posts` (741's own organic posting), `sales-pitch` / `sales-call-prep` / `booking-sequence` (the sales leg after a lead engages). `morning-grill` supplies the card mechanics pattern, not the marketing-strategy content.

## 1.5 Knowledge-base work completed (update, same day)
- Notebook 2 URL corrected (one-character typo in the brief, Martin confirmed the right link live); it is Martin's "The Content Marketing Playbook" (37 sources), not a second Hormozi-branded notebook.
- Notebook 2 was already queried twice by sibling skills (`content-format-board` 2026-10-24, `personal-posts` 2026-10-22) for video-hook and text-post findings. Per Martin's decision, this build reused those two extracts and ran ONE new scoped query for its own angle (channel selection, Lead Getters, focus, structure) — saved to `playbook-notes-channel-selection.md`. No full raw re-export of the 37 sources.
- Hormozi library freshness gap (109 vs. 120 live sources) exported same day: 11 new sources added as `00_project/knowledge/hormozi-library/110-...md` through `120-...md`, `INDEX.md` updated. Per Martin's decision (the full audiobook source alone is 242,570 characters), 110-120 are captured as the NotebookLM AI source-guide summary in full plus a representative excerpt, not full raw transcripts — marked in `INDEX.md`.

## Open questions going into design (Step 2)
- Scope of card rounds: the brief lists 4 fixed areas but says "there is more to it" — the derived question bank (`_derived/marketing-grill-questions.md`, built in Step 3) must come from the knowledge base, not be capped to exactly 4 areas.
