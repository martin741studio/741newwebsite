# Research note — sales-call-prep

## 1.1 Block chosen
Skill, triggered per prospect by Martin ("prep me for the call with X" / call booked). Reason: a repeatable procedure Martin (or a chained step) triggers per call, not a schedule and not a multi-day stream — per `patterns.md` §3 step 3. No `disable-model-invocation` (no external send, no live-site change, no destructive action — it only writes a local brief file). `context: fork` candidate since the run reads several sources (LinkedIn/CRM, review page, site, offer, objection playbook) and should keep the main chat clean.

## 1.2 Library search
- Generic workflow library (`00_project/knowledge/workflow-library/`): no Hormozi material there (it is about building Claude workflows, not sales). Confirms memory file `hormozi-library-local.md` points to the correct, separate path: `00_project/knowledge/hormozi-library/` (109 sources, NotebookLM export, 06.10.2026).
- Hormozi library grep for sales-call terms (`sales call`, `closing`, `objection`, `close rate`, `discovery call`) hit ~30 files. Most relevant: `072-how-to-think-like-the-top-1-sales-masterclass.md` (full sales-call structure) and `009-what-s-the-best-book-to-learn-closing.md` (names Hormozi's own named frameworks — internal reference only, never in the deliverable).
- Extracted from 072 (internal notes, never shown to a prospect or in the deliverable):
  - Sales call shape: intro → **discovery** (9 steps; two reusable digging questions: "can you give me an example of that" / "tell me more about that", asked after "what brought you in" + "how long has this problem existed") → pitch → close on the spot.
  - Discovery is the longest and most important part. Pain-driven motivation beats gain-driven. One root pain is enough ("most buyers are single-issue voters") — do not stack five reasons.
  - Qualify before the call: make sure the decision maker is on the call, or closing on the spot becomes impossible.
  - Close on the spot by default; a slow sales motion signals a qualification or education gap, not a pricing problem.
  - Offer repeats through the whole funnel (ad → page → call) — the call should reuse the same offer language the prospect already saw (our review page / Loom).
  - Reframe objections as opportunity cost ("what does NOT having this cost you over a year") rather than defending price.
  - Source 009 names two frameworks (never quote by name outside this note): a 4-letter objection-handling framework and a "diagnostic sale" approach — both map onto what 741 already has in `sales-einwandbehandlung.md` (Agree & Reframe, proof over promise, risk reversal before price). No new framework needed; 741's own file already covers this ground and is more specific to our packages.
- `00_project/sales-einwandbehandlung.md` (27.07.2026): 741's own objection playbook — 3 principles (Agree & Reframe, Beweis schlägt Behauptung, Risk Reversal before price), 11 classic objections with EN scripts, and a short call dramaturgy (quantify the goal → show the gap → proof → two engines + recommendation → guarantee before price → objection → close question). This is the house voice to reuse; the deliverable should point into it, not duplicate it.

## 1.3 Freshness
`INDEX.md` of the workflow-library: last refresh 2026-10-11, next due 2026-11-22 — inside the 6-week window, no re-fetch needed. The Hormozi library (separate, sales-specific) is undated by the freshness rule (it is Martin's own NotebookLM export, not the Claude-workflow knowledge base); used as-is per memory `hormozi-library-local.md`. No web research was needed — the local libraries covered call-prep/closing methodology adequately.

## 1.4 Existing assets
- `.claude/skills/booking-sequence/`: prepares 3 WhatsApp reminder messages **to the prospect** before a booked call (24h/morning/30min). It does NOT prepare Martin for the call itself — no prospect research pack, no objection pre-read, no talk track. Complementary, not overlapping. sales-call-prep can read the same booking folder (`00_project/prospects/<slug>/booking/`) for call time + context, but produces a different artifact (Martin-only brief) with a different trigger.
- No existing skill produces a call-prep brief for Martin. `program-deliverable-rules.md` and `no-method-sources-in-deliverables.md` set the house rule: Martin's own call-prep notes may name sources internally, but anything Martin reads "as if it were client-facing style" should still use 741's own framing by habit — the brief is Martin-only, never shown to the prospect, but guru names are kept out even here per the hard limit in the brief, to keep one habit across all deliverables.
- `linkedin-crm-access.md`: Pipeline tab in "741 Studio CRM" Sheet, red NAD = overdue, orange X = replied. Usable to find an upcoming/recent prospect call. LinkedIn thread reading is slow (no JS access) — use it only if the Pipeline/Sheet or Calendar does not already show a booked call.

## Open questions (relay to Martin via grill-me cards, not answered here)
1. Trigger phrase and scope: does sales-call-prep run only on request ("prep me for X"), or auto-chain right after booking-sequence creates `booking.json`?
2. Real test case for step 2.3: use an upcoming/recent booked call found in the LinkedIn CRM Pipeline tab or calendar — flagged to the orchestrator since this needs Martin's confirmation it's an appropriate test subject, not invented.
