---
name: sales-call-prep
description: Builds a one-page call-prep brief for Martin before HIS OWN sales call with a 741 prospect: her goal question, one new gap, one proof case, premium-first package, 2-4 ranked objections, call structure. Reads the booking folder so nothing shown is repeated. Use on "prep me for the call with <name>", "Anrufvorbereitung für <name>", "Call mit <name> vorbereiten". On request only. Not for messages TO the prospect (booking-sequence).
context: fork
allowed-tools: Read, Grep, Glob, Bash(python3:*)
---

# Sales call prep (Martin's own call, never the prospect's)

## Critical

- **Never contacts the prospect.** The skill reads the booking folder and writes a file Martin reads. No WhatsApp, email or LinkedIn message to the prospect is drafted or sent from here (that is `booking-sequence`).
- **No outside method source in the brief.** Internal research may use them (`references/picks.md` names the internal source). The file Martin reads says "741-Call-Raster" / "741-Einwand-Raster", never a guru or book name. `scripts/verify_brief.py` checks this.
- **Read the booking folder before picking what to say.** Skipping `m1.txt`-`m3.txt` repeats an insight she already saw, the one mistake the hand-run build caught.

## Inputs

The prospect's name as Martin said it (nickname or first name is fine). If `00_project/prospects/<slug>/booking/` does not exist, the brief is shorter ("thin case" below).

## Steps

1. **Find the booking.** `python3 .claude/skills/sales-call-prep/scripts/find_booking.py "<name>"`. One match prints `slug`, `booking_json`, `review_url`, `call_times` and which of `baseline.md` / `claims.json` / `m1-m3.txt` exist. 0 or more than 1 match exits 2: ask Martin with a card, never guess. `thin_case: true` (no `baseline.md`) means no review-page history to reuse.
2. **Read context** in this order: `booking/booking.json`, `booking/baseline.md` (her positioning, review-page findings, proof wall), `booking/claims.json` (every number already shown, with source; never repeat an unsourced number), `booking/m1.txt`, `m2.txt`, `m3.txt`. A newer `site-recheck.json` or `site-check.json` in the booking folder beats `baseline.md` and can make a listed gap stale (once she had added schema markup after the review page). Also read memory `741studio-pricing.md` (package order) and `00_project/sales-einwandbehandlung.md` (house objection playbook, call dramaturgy).
3. **Pick** with `references/picks.md`: the one new gap (never one already in m1-m3), one proof case matched to her business plus one in reserve, the package (premium named first, 90-Tage-Paket recommended by default, the only tier with the guarantee), 2-4 objections ranked for THIS prospect, not the full list. Thin case: one small fresh look at her website (and LinkedIn if reachable) instead of a "what she already saw" section; keep the other sections.
4. **Draft** in the section order of `references/template.md` (worked example: Korinna Heintze). Short sentences, one number per claim.
5. **Verify**, loop until `RESULT: PASS`: `python3 .claude/skills/sales-call-prep/scripts/verify_brief.py <call-prep.md> --claims <booking/claims.json>`. Fix the flagged sentence or number; delete a fact only if it has no source. Thin case without `claims.json`: run `deslop_de.py <file>` instead and grep for outside method names.
6. **Deliver.** Write `00_project/prospects/<slug>/call-prep.md`. Update or create `_run.json` in that folder (`workflow: "sales-call-prep"`, `status: "fertig"`). Show Martin the brief, the `verify_brief.py` result line, and the call time in both zones (his and hers). The brief stays in the prospect's language (usually German).

No mid-run checkpoint. The gate is step 5: nothing reaches Martin before PASS, because a wrong or unsourced brief right before a real call is the costly failure.

## References

- `references/picks.md`: choosing gap, proof, package and ranked objections; internal methodology grounding.
- `references/template.md`: fixed section order and the Korinna example.
