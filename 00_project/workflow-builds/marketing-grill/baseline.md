# Baseline comparison (Step 4.3)

## Without the skill (what would have happened on a plain "marketing grill" request)
- No structured grep of the knowledge base — the Core Four / Lead Getter / More-Better-New framework would have been recalled from general knowledge, not from a sourced library, risking an unsourced or generically-phrased recommendation.
- No infra-state check script — real state (e.g. the cold-email channel's legal/paused history, the giveaway page's draft T&Cs) would likely have been asserted from memory rather than read fresh, with real risk of repeating the stale "Maya" assignment that actually surfaced mid-run.
- No fixed output location or citation check — the result would have been a chat answer, not a `playbook.md` with a verifiable `## Sources` section, harder to refer back to on a re-run.
- Card rounds, if used at all, would not have had a pre-built question bank grounded in the library (`_derived/marketing-grill-questions.md`), so phrasing and coverage would vary run to run.

## With the skill
- 4 grounded card rounds, each citing a specific rule in `_derived/marketing-grill-rules.md`.
- One real stale-data catch during the run (the "Maya" correction), now hard-coded as a skill rule so it cannot silently recur.
- A deterministic infra-state scan (`check_infra_state.py`) ran before Round 1, surfacing real flags (Zapmail retired, the Abmahnung history, giveaway T&Cs still draft) instead of relying on memory.
- Output: one `playbook.md`, slop-checked to 5/5, with every claim traceable to a file `check_citations.py` verifies exists.
- Tool calls for the actual decision work: 2 memory-file read batches (infra state + context files) + 4 AskUserQuestion rounds + 1 Write + 2 verification script runs — a bounded, repeatable shape for every future run, including a re-run (use case 2) that only needs the rounds that actually changed.

## Corrections avoided going forward
The single correction needed during this build (the stale "Maya" fact) is now a `## Critical` rule and a `references/card-pattern.md` instruction — a future run of the installed skill should not need that correction again, which is the concrete thing this baseline is meant to demonstrate improves.
