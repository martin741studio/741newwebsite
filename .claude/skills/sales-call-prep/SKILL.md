---
name: sales-call-prep
description: Builds a one-page call-prep brief for Martin before HIS OWN upcoming sales call with a 741 prospect - her goal question, the one new not-yet-shown gap, one proof case, a premium-first package recommendation, 2-4 ranked likely objections from the house playbook, and a short call structure. Reads the prospect's existing booking folder (booking.json, baseline.md, claims.json, WhatsApp m1-m3) so nothing already shown to her is repeated. Use when Martin says "prep me for the call with <name>", "Anrufvorbereitung für <name>", "Call mit <name> vorbereiten", or "was muss ich vor dem Call mit <name> wissen". On-request only - never auto-runs after a booking. Do NOT use to write or send any message TO the prospect (WhatsApp reminders before a booked call are booking-sequence's job, not this skill's) and do NOT use for an existing running client's account/status work.
context: fork
allowed-tools: Read, Grep, Glob, Bash(python3:*)
---

# Sales call prep (Martin's own call, never the prospect's)

## Critical

- **Never contacts the prospect.** This skill only reads the booking folder and writes a file
  Martin reads. No WhatsApp, email, or LinkedIn message is ever drafted or sent to the
  prospect from here - that is `booking-sequence`.
- **No outside method source ever appears in the brief.** Internal research may use them
  (`references/picks.md` names the internal source); the file Martin reads calls the shape
  "741-Call-Raster" / "741-Einwand-Raster", never a guru or book name. Run
  `scripts/verify_brief.py` before showing Martin anything - it checks this automatically.
- **Read the booking folder before picking what to say.** Skipping `m1.txt`-`m3.txt` means
  repeating an insight she already saw - the one mistake the hand-run build caught. Read
  `booking.json`, `baseline.md`, `claims.json`, `m1-m3.txt` in that order before drafting.

## Inputs

- The prospect's name, as Martin said it (a nickname or first name is fine).
- Nothing else is required. If `00_project/prospects/<slug>/booking/` does not exist yet
  (no review-page / booking-sequence history), the brief is shorter - see "Thin case" below.

## Workflow

Copy this checklist and tick it off:

```
Call prep <Name>:
- [ ] 1 find_booking.py (card if 0 or >1 match, or confirm thin case)
- [ ] 2 read booking.json + baseline.md + claims.json + m1-m3.txt
- [ ] 3 pick: new gap, proof case + reserve, package, 2-4 ranked objections (references/picks.md)
- [ ] 4 draft the one-pager (references/template.md)
- [ ] 5 verify_brief.py --claims <claims.json> -> PASS (loop: fix, re-run)
- [ ] 6 write call-prep.md, update _run.json, show Martin
```

**Step 1 - Find the booking.**

```bash
python3 .claude/skills/sales-call-prep/scripts/find_booking.py "<name>"
```

Exactly one match: prints `slug`, `booking_json`, `review_url`, `call_times`, and which of
`baseline.md` / `claims.json` / `m1-m3.txt` exist. 0 or more than 1 match: prints candidates
and exits 2 - this is a card for Martin (0 or >1 match, or "no booking folder - thin case"),
never a guess. `thin_case: true` (no `baseline.md`) means: skip straight to step 3's "thin
case" note, no review-page history to reuse.

**Step 2 - Read context**, in this order: `booking/booking.json` (who, when, call link,
language), `booking/baseline.md` (her positioning + the review page's findings + proof wall -
the richest single source), `booking/claims.json` (every number already shown, with its
source file - never repeat an unsourced number), `booking/m1.txt`, `m2.txt`, `m3.txt` if
present (what has already gone out since the review page). **Check the booking folder for a
newer `site-recheck.json` or `site-check.json`** - if one exists, it is fresher than
`baseline.md`'s review-page scan and can make a listed gap stale (the functional test found
her adding schema markup after the review page; the brief led with that instead of a now-fixed
point). Also read memory `741studio-pricing.md` (package order) and
`00_project/sales-einwandbehandlung.md` (the house objection playbook and call dramaturgy)
once per run.

**Step 3 - Pick.** Full heuristics in `references/picks.md`: the one new gap to lead with
(never one already in m1-m3), one proof case matched to her business shape + one in reserve,
the package recommendation (premium named first, 90-Tage-Paket recommended by default, it is
the only tier with the guarantee), and 2-4 objections ranked for THIS prospect - not the full
house list. **Thin case** (no `baseline.md`): do one small fresh look at her website (and her
LinkedIn profile if reachable) instead of a "what she already saw" section; keep the goal
question, proof, package, objections and call structure sections as normal.

**Step 4 - Draft** with the exact section order in `references/template.md` (worked example:
the Korinna Heintze brief referenced there). Short sentences, one idea per sentence, one
number per claim.

**Step 5 - Verify (loop until it passes).**

```bash
python3 .claude/skills/sales-call-prep/scripts/verify_brief.py <call-prep.md> --claims <booking/claims.json>
```

On anything but `RESULT: PASS`: fix the flagged sentence or number (never delete a fact unless
it has no source), run again. Repeat until `RESULT: PASS`. For a thin case with no
`claims.json`, run the plain `deslop_de.py <file>` check instead (no `--claims` flag) and
still grep the file for outside method names.

**Step 6 - Deliver.** Write `00_project/prospects/<slug>/call-prep.md`. Update or create
`_run.json` in that prospect's folder (`workflow: "sales-call-prep"`, `status: "fertig"`) so
the overview Excel picks it up on the next sync. Show Martin in chat: the brief, the
`verify_brief.py` result line, and the call time in both zones (his and hers). STE for any
prose around the brief; the brief itself stays in the prospect's language (usually German, to
match her booking record and Martin's own working language for call notes).

## Output template

See `references/template.md` for the exact section order and the worked example.

## Checkpoints

None mid-run - this is a one-shot prep document, not a multi-day client deliverable. The one
non-negotiable gate is step 5 (`verify_brief.py` → `RESULT: PASS`) before anything is shown to
Martin: a wrong or unsourced brief right before a real sales call is the failure mode that
actually costs money.

## References

- `references/picks.md` - how to choose the gap, proof, package and ranked objections (the
  judgment step); also where the internal-only methodology grounding lives.
- `references/template.md` - the fixed output section order + the worked Korinna example.
