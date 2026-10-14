# Hand-run — one real task solved by hand (step 2.3)

## The real call used
Korinna Heintze (FEINGOLD, Executive Sparring für Führungsfrauen), 30-min call booked for
Mon 2026-10-26, 9:30 Europe/Berlin (16:30 WITA for Martin), found via the Google Calendar
MCP (`search by keyword "30 min meeting between 741 Studio"` surfaced the cal.com booking
event directly; `list_upcoming_meetings` alone did not show it because it is 11 days out
and that tool's window is capped at 168h/one week — the calendar `list_events` full-text
search found it). A real, already-known prospect: `00_project/prospects/korinna-heintze/`
already exists from the booking-sequence run on 2026-10-14.

## Context that had to be supplied by hand (this becomes the skill body)
To write the one-page brief (`hand-run-output-korinna-heintze.md`) the following had to be
read, in this order — this list is the first draft of the pipeline (2.4):

1. `booking/booking.json` — who, when (both zones), call link, language, health flag.
2. `booking/baseline.md` — the review page she already saw: positioning, the critical/opportunity
   findings, the proof wall (case list), the offer CTA. This is the single richest source —
   it already contains most of "who she is" and "her gap".
3. `booking/claims.json` — every number already shown to her, with its source file. Needed
   so the brief never repeats an unsourced number and so the slop/claims check passes.
4. `booking/m1.txt`, `m2.txt`, `m3.txt` — what she has ALREADY been told since the review
   page (two new insights + a case + a laptop tip). Without reading these, the brief would
   repeat an insight she has already seen twice, which would read as sloppy on the call.
5. Memory `741studio-pricing.md` — the 3-tier package structure and the anchor order
   (premium first, 90-Tage recommended, guarantee only on the middle tier).
6. `00_project/sales-einwandbehandlung.md` — 741's own objection playbook (3 principles,
   the classic objections with scripts, the call dramaturgy). Used to (a) pick the 2-4 most
   likely objections for THIS prospect profile (solo premium coach → objection #11 "wir sind
   ausgelastet"/"wachsen schon über Empfehlungen" variant is the most likely, not a generic
   "zu teuer" list) and (b) reuse the house call-dramaturgy shape instead of inventing a new one.
7. `00_project/knowledge/hormozi-library/072-…-sales-masterclass.md` (internal only, never
   quoted) — confirms the shape: quantify the prospect's own goal before pitching, lead with
   the single clearest pain/gap, one proof point beats a list, reframe price as opportunity
   cost, close on the spot. Nothing here is prospect-specific; it only validated the order
   of sections, so the skill body should state the order as a house rule, not re-derive it
   from the library every run.

Nothing had to be guessed: every number and every "already shown to her" claim traces to a
file. The one open gap: I did not check the LinkedIn CRM Pipeline tab (`linkedin-crm-access.md`)
for her stage/notes, since the booking folder already had everything needed and that lookup
is slow (no JS access, ~2 calls per prospect). The skill should treat the LinkedIn Pipeline
check as optional — only when the booking folder is thin (e.g. a call booked without going
through the review-page workflow first, so no `baseline.md` exists).

## What this fixes vs. a cold "just write a call-prep doc" prompt
- Without step 4 (m1-m3), a first attempt repeated the Leipzig insight verbatim — caught only
  by rereading the WhatsApp texts. The skill body must say explicitly: read the booking
  messages before picking which gap to lead with in the call, and show something NEW in the
  structured-data finding.
- Without step 6, a first draft picked "zu teuer" as objection #1. Her profile (solo, premium,
  warm positioning) makes "ich wachse schon über Empfehlungen" the realistic #1 — the
  einwandbehandlung.md capacity-objection pattern (#11), not the generic price objection.
- The deslop_de.py claims check caught two numbers ("rund 70", "rund 30 Suchen") that were
  accurate but needed the `--claims` flag pointing at the real `claims.json` to pass — the
  skill's verification step must always run deslop with `--claims <booking/claims.json>`,
  never the bare text check, when this much of the brief is "according to the review page".

## Evidence
- Output: `00_project/workflow-builds/sales-call-prep/hand-run-output-korinna-heintze.md`
- Check: `python3 00_project/content-writing-skill/scripts/deslop_de.py <file> --claims 00_project/prospects/korinna-heintze/booking/claims.json` → `score 5/5 CLEAN`
- No outside method name appears in the output file (grep clean for "Hormozi", "Ramoszi", "closer").
