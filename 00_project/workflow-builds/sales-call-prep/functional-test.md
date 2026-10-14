# Functional test (step 4.2) — fresh session, real task

A fresh general-purpose subagent (no memory of this build) loaded `sales-call-prep` via the
Skill tool and ran it for real on "Bereite mich auf den Call mit Korinna Heintze vor." —
the same real booked call used for the 2.3 hand-run, now run through the finished skill
instead of by hand.

## Result
- No stall, no guess, no invented fact. One real judgment call surfaced: the skill's own
  `references/template.md` pointed at a prior hand-run brief for the SAME prospect as its
  "worked example" — a copy-paste trap. The subagent instead re-read the current
  `booking/site-recheck.json` (dated 2026-10-14, already in the folder) and found she had
  since added schema markup (`schema_types` now lists Person/ProfessionalService/Service),
  which made the hand-run's "0 strukturierte Daten" gap stale. It led the real brief with the
  current gap instead (missing H1/H2 + no GA4/GTM), verified by re-reading `site-recheck.json`
  directly rather than trusting the example.
- No question needed for Martin — everything required was already in the booking folder.
- Verification (re-run independently by me, not just trusted from the subagent):
  ```
  Checking 00_project/prospects/korinna-heintze/call-prep.md
  --- deslop_de.py ---
  670 Wörter sichtbarer Text (de)
    score 5/5  CLEAN
  OK: no outside method source named.
  RESULT: PASS
  ```
- Output file: `00_project/prospects/korinna-heintze/call-prep.md` (a real, usable deliverable
  for Martin's actual 26.10.2026 call — not a throwaway test artifact).
- `00_project/prospects/korinna-heintze/_run.json` written (`workflow: sales-call-prep,
  status: fertig`) — the registry sync will pick this up.
- Grep for outside method names on the real output: no match (exit 1).

## Fix applied from this test
`references/template.md` now says explicitly: the worked example is for STYLE only, never for
facts, even for the same prospect across different runs — with the schema-markup incident as
the stated reason. `SKILL.md` step 2 now explicitly tells the skill to check for a newer
`site-recheck.json`/`site-check.json` in the booking folder, since it can be fresher than
`baseline.md`. This converts the subagent's one-off good judgment into a standing instruction.
