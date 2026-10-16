# Scorecard: Automation Build / automation-completion (re-score 2026-10-15, after install)

Scored with `00_project/knowledge/workflow-library/_derived/scorecard.md`, same categories
as `00_project/automation-workflow/scorecard-2026-10-11.md`. Only the rows that changed
since 2026-10-11 are explained below; all other rows carry their 2026-10-11 score and note
forward unchanged (full table in that file).

## Changed rows

| # | 10-11 | 10-15 | Note |
|---|---|---|---|
| B3 | 1 | 2 | "Real Skool build replayed through the guard (paper)." Now also: 3 real fresh-session tests against the installed hooks, from outside the repo (trigger-tests.md) |
| D5 | 0 | 1 | Trigger tests run in a real fresh session against the installed skill+hooks (S1, S3 pass as designed). Not 2 (full pass) because S2 surfaced a real, previously unknown gap: a paraphrase without the literal `/automation-build` prefix gets neither the skill nor the hook, and the model attempted real work ad hoc (blocked only by an unrelated OAuth limitation in the test session, not by any 741 guard). See trigger-tests.md |
| D6 | 0 | 1 | Baseline built from the real historical incident (without) vs. the hooks' proven, now-wired behaviour on the same inputs (with) — baseline.md. Not 2 because this is not a live start-to-finish A/B rerun of one real task (that is 4.2, not done this round) |

## Full table (all other rows unchanged from 2026-10-11)

A1=2, A2=2, A3=2, A4=n/a, B1=2, B2=2, B3=2 (↑), B4=2, B5=2, C1=2, C2=2, C3=2, C4=2, C5=2,
C6=1, C7=2, C8=1, D1=2, D2=2, D3=2, D4=2, D5=1 (↑), D6=1 (↑), E1-E7=n/a, F1=1, F2=2, F3=2,
F4=2, F5=2, F6=2.

Sum: 2+2+2 + 2+2+2+2+2 + 2+2+2+2+2+1+2+1 + 2+2+2+2+1+1 + 1+2+2+2+2+2
   = 6 (A) + 10 (B) + 14 (C) + 10 (D) + 11 (F) = 51

Total: 51 / 56 = 91.1 %. Blocking zeros: 0 (previous blockers D5/D6 both moved off zero).

## What is still open before checkpoint 2

- 4.2 functional test (not attempted this round — needs a real, currently-pending
  automation task; none is queued right now, and manufacturing one would be scope creep
  beyond what was asked for this round).
- 4.4 — skipped (reason: not a plugin; `/doctor prompt-audit` does not apply to a single
  skill + 3 hooks build; the equivalent check here is the 95/95 sandbox suite plus the
  real fresh-session tests).
- The S2 finding (paraphrase bypasses both the skill and the hook) is new and unresolved —
  flagged to the orchestrator, not decided unilaterally, since it could mean changing the
  hook's match pattern or accepting it as a documented limit (both are judgment calls
  beyond "finish installing what Martin already approved").
- `_hooks:` HOOKDIR is currently the live path inside the `741website` git repo
  (`00_project/automation-workflow/hooks/`). If that repo folder is ever moved or that
  branch is deleted, the hooks silently stop firing (Claude Code hook commands that fail to
  resolve just produce no output, per each hook's own "never block on a crash" design).
  Worth a note in the memory file as a known fragility, not a blocker.
