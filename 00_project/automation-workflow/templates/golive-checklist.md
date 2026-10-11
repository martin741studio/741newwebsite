# Go-live checklist: <client> · <automation>

Tick each line only with evidence (file in `evidence/` or record ID). G actions need `go A<n>`. M actions are Martin's.

## Before go-live
- [ ] `check_report.py` PASS (paste the output line)
- [ ] Martin saw the evidence at checkpoint B (date)
- [ ] `rollback.md` written and the rollback path tested once where it is safe (for example Zap OFF/ON on the draft)
- [ ] Account check: the flow runs under <account>, from-address <…>, project <…>

## Cleanup
- [ ] TEST-741 records deleted in every target system (list IDs)
- [ ] Test connections, test members, test bookings removed (M steps in `martin-steps.md` if money is involved)
- [ ] Test settings reset (prices, limits, sender, placeholder texts)
- [ ] Search for "TEST-741" in every target system returns 0

## Switch on (each line = one G action)
- [ ] A<n> <switch on / publish> → readback shows "on" (evidence)
- [ ] A<n> alert path on → test alert received at martin@741.studio
- [ ] A<n> reconciliation check scheduled → first run output in `evidence/`

## Canary
- [ ] First real record end-to-end, every field read back (IDs)
- [ ] +24 h check: counts match, no errors in task history (date)

## Handover
- [ ] `runbook-de.md` and `testprotokoll-de.md` live at the client node (portal link)
- [ ] Client message draft ready for Martin (Ich-Form, du, no team names)
- [ ] `_run.json` status "fertig, Freigabe offen"
