# Degrees of freedom per step (2.5)

| Step | Freedom | Why |
| --- | --- | --- |
| 1 Find the prospect | Low (script-like lookup, same pattern as booking-sequence's find_prospect.py) | Fragile: wrong slug = wrong prospect's data in a sales brief. Exact match or ask, never guess. |
| 2 Read context | Low (fixed file order) | Fragile: skipping m1-m3 is exactly the failure the hand-run caught (repeating a shown insight). Order is a checklist, not a judgment call. |
| 3 Pick (gap, case, package, objections) | High (heuristic) | Open: which gap to lead with and which objections are likely depends on the prospect's business shape — this is judgment, not a formula. Give the heuristics (business-shape -> likely objection pattern; new vs. already-shown gap), not a rigid script. |
| 4 Draft | Medium (template with fixed sections, free text inside) | The section order and the "no outside names" rule are fixed (rule R2.8 template pattern); the sentences inside are written per prospect. |
| 5 Verify | Low (exact script, no parameters) | Fragile and the one hard gate (R1.7, R4.1): run deslop_de.py with --claims, grep for outside names, loop until it passes. No freedom to skip or soften this. |
| 6 Deliver | Low (fixed output path + fixed report shape) | Consistency with the registry/_run.json convention (R8.1-style) and so Martin always knows where to find it. |

## Decision record — 2.6 Checkpoint 1: Martin's go (2026-10-15, relayed by the orchestrator)

Martin answered the 3 checkpoint-1 questions:

1. **Trigger/scope: A — On-request only.** sales-call-prep runs only when Martin explicitly
   asks ("prep me for the call with X" / "Anrufvorbereitung für X"). It is never auto-chained
   or auto-offered right after booking-sequence. UC2 (chained) in `use-cases.md` becomes: the
   two skills can be asked for in the same message, but neither triggers the other on its own.
2. **Test/build case: A — use Korinna Heintze's real booked call (26.10.2026).** Confirmed:
   the hand-run output already built for her (`hand-run-output-korinna-heintze.md`) is the
   real task for 2.3/4.2 functional testing. No new prospect needed.
3. **Auto-invocation: A — leave it model-invocable.** No `disable-model-invocation` in the
   frontmatter — it only reads data and writes a local file Martin reads before the call; no
   send, no live-site change, no destructive action.

This is the checkpoint-1 go. Proceeding into section 3 (build).

## Decision record — 5.1 Checkpoint 2: Martin's go (2026-10-15, relayed by the orchestrator)

Martin reviewed the cp2 gate output (GATE PASSED), the scorecard (59/60 = 98%, no zero
anywhere), and the real brief for his own 26.10.2026 call with Korinna Heintze
(`00_project/prospects/korinna-heintze/call-prep.md`, verified 5/5 CLEAN).

**Martin's words: "ship it."**

Proceeding into section 5 (commit, registry, memory file, install gate).
