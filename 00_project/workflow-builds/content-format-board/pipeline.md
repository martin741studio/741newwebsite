# Pipeline map (step 2.4)

```
[ Trigger: client/prospect name ]
        │
        ▼
[ 1. Intake ]
  - scripts/resolve_target.py <name> → prospects/<slug>/ or assets/<client>/?
  - read existing files there (reuse, never re-derive)
        │
        ▼
[ 2. Readiness + on-camera check ]
  - known from existing files? → use it
  - not known? → write as an open question in the board (never guessed, never blocks the run)
        │
        ▼
[ 3. Public-question sourcing ]
  - firecrawl_search (Reddit/forum, industry/travel blog roundups)
  - optional: competitor comment mining (YouTube/IG), only if a competitor link is already on file
  - scripts/log_research_calls.py tallies calls made (reported, not a hard cap — Martin's go, 0.0)
        │
        ▼
[ 4. Gap/finding synthesis ]  (qualitative, Rule R1.7 — heuristic, not scripted)
  - state the ONE real finding in plain words before any format talk
        │
        ▼
[ 5. Format mapping ]
  - scripts/label_map.py — looks up each internal taxonomy term (One-Shot, Ten-Shot, Yap, How/Why)
    against the plain-English client-facing label (deterministic, never typed freehand)
  - qualitative: which level/variant fits the real situation (heuristic, worked example = Little Frenchie)
        │
        ▼
[ 6. Quality bar ]
  - internal reference examples from content-format-library/001 may be cited in build notes
  - NEVER named in the client-facing board (no-method-sources-in-deliverables)
  - quality stated in execution terms: composition, lighting, hook, shot list — not brand name-drops
        │
        ▼
[ 7. Draft board ]
  - assets/board-template.md → filled board
        │
        ▼
[ 8. CHECKPOINT — Martin's go ]
  - show full board; board is a proposal, never auto-sent to a client or folded into a live pitch deck
        │
        ▼
[ 9. Deliver ]
  - prospects/<slug>/content-format-board.md  OR  assets/<client>/content-format-board/<date>/board.md
  - note: feeds INTO sales-pitch/booking-sequence or content-writing by hand later — this workflow never calls them
```
