# 1.4 Existing 741 assets (automation-completion)

`ls ~/.claude/skills/ .claude/skills/`:
- No `automation-build` skill installed in either location (confirmed).
- `canary` is installed and live in `.claude/skills/canary/` — built 2026-10-14 directly
  from the SAME Marcel Gewinnspiel incident. It self-describes as covering "the missing L6
  monitor half of Automation Build" (canary coverage-map.md). It already handles: outage
  detection, one safe self-heal, escalation (Telegram, SEV1 pages 24/7), daily status, and
  explicitly defers the automation BUILD process itself back to automation-build.

`grep -l "<term>" ~/.claude/projects/-Users-martindrendel-741website/memory/*.md`:
- `automation-build-workflow.md` — full design summary, states plainly: "hooks and skill
  are NOT installed — install only after Martin's install go." Lists open items: scorecard
  D5/D6 (blocking), daily reconciliation runner not built, test inbox not created, one
  secret (Smartlead key) still in a memory file instead of `.secrets/`.
- `marcel-rosenbach-client.md` — client facts, original Skool-tier funnel, LastPass access
  grants, the Sept 2026-09-03 Zap v1 failure that first motivated automation-build.
- `marcel-message-in-martin-voice.md` — style-only memory (how to draft messages in
  Martin's voice for this client), not process-relevant here.

What already exists, concretely, on disk:
| Artifact | Path | State |
|---|---|---|
| Full spec (L0-L6) | `00_project/automation-workflow.md` | Approved cp1, 2026-10-11 |
| Failure map | `00_project/automation-failure-map.md` | Final v1, grilled with Martin |
| Design note + decisions | `00_project/automation-workflow/design-note.md` | cp1 go recorded |
| Skill draft | `00_project/automation-workflow/skill-draft/automation-build/SKILL.md` | Drafted, updated 2026-10-14 (P3a, never-test-on-live rule). NOT installed |
| Hooks | `00_project/automation-workflow/hooks/*.py` (3 files) | Drafted, sandbox-tested 95/95. NOT merged into settings.json |
| Scripts | `run_state.py`, `check_report.py` | Exist |
| Templates | 9 files (spec de/en, test-plan, test-report example, golive, martin-steps, rollback, runbook-de, testprotokoll-de, verifier-prompt) | All present |
| Scorecard | `scorecard-2026-10-11.md` | 48/56 = 85.7%, blocked by D5 (trigger tests) and D6 (baseline) — both need install first |
| Test scenarios | `test-scenarios.md` | S1-S5 written; S4/S5 passed sandbox; S1-S3 need the installed skill |
| Registry | `00_project/workflow-registry/registry.json` | id `automation` already added (scorecard F6=2) |

Conclusion: nothing to build from zero. The only missing pieces are: (a) Martin's decision
on scope (new workflow vs. finish this one — flagged at cp1), (b) the install step itself
(hooks into settings.json, skill copied to a skills folder), (c) the two blocked test
steps (D5 trigger tests, D6 baseline), which can only run once installed, (d) folding in
the two fresh 2026-10-14 lessons (Zapier AI draft handling, never-test-on-live) which are
already in the skill draft text but not yet re-scored.
