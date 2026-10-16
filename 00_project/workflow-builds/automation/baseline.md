# 4.3 Baseline — with vs without the installed hooks

A true parallel A/B run (same real task, once with the skill/hooks and once without) is not
possible here without creating a second real incident on purpose. Per rule R1.6/4.7, the
baseline instead compares the real historical "without" case (Marcel Gewinnspiel, 2026-10-08
to 10-14, measured in `00_project/workflow-builds/canary/incident-marcel-2026-10-13.md`)
against the now-installed hooks' proven behaviour on the exact same two inputs (the literal
claim text and the literal publish-without-go action), both in the 95/95 sandbox suite
(`00_project/automation-workflow/tests/test_hooks.py`, re-run 2026-10-15, unchanged) and now
confirmed wired into a real session (trigger-tests.md, S1).

| Measure | Without the hooks (real, 2026-10-08 to 10-14) | With the hooks (installed, 2026-10-15) |
|---|---|---|
| "Live and tested" claim with skipped tests | Published, acted on by the client for days | `automation_done_gate.py` blocks the claim in the same turn — test "gate blocks 'fertig' without report" passes; the claim never reaches Martin or the client unverified |
| Publish without a recorded go | Happened (Zap v1 published 2026-10-08) | `automation_guard.py` denies the class-G action and requires `run_state.py request` + Martin's literal `go A<n>` — tests "class G needs go token" / "approved mail to Marcel goes through once" pass |
| Time from root-cause-findable to caught | ~3 days (tag/label confusion sat in the Zap from 10-08, found 10-11, not fixed until 10-14) | 0 turns — the done gate and guard are synchronous PreToolUse/Stop checks, not a later audit |
| Corrections needed after the fact | At least 3 real fix rounds over 6 days (tag→label fix, Tally redirect-on-completion fix, Zap v2 + 2 tests) | N/A for the same failure classes — they are blocked before the "done" claim or the publish happens, not fixed afterward |
| Escalation delay on the live outage | 8.5 h (Marcel → Martin via WhatsApp forward, seen 05:41 the next morning) | Separate concern, already covered by the installed `canary` skill (Telegram, SEV1 pages 24/7), not by automation-build itself |
| Real signups lost | 23 of 23 real entrants during the outage window | N/A — not re-created for this baseline |
| Tool-call/correction overhead of the guard itself | — | 0 extra correction rounds in the 3 real fresh-session tests (S1/S2/S3); 1 new finding (S2, see trigger-tests.md), not a correction, a gap to decide on |

Honest limit: this is evidence that the SAME inputs are now blocked deterministically, not a
live replay of a brand-new automation build start to finish (that is step 4.2, the
functional test, not run in this round — no new real client automation task is pending
right now to run it on safely, and creating one just to test would be scope creep beyond
what this round was asked to do). 4.2 stays `todo` and is flagged openly in the cp2 report
rather than marked done without real evidence.
