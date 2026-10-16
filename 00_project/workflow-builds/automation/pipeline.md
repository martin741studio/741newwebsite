# 2.4 Pipeline with checkpoints (automation-completion)

Two nested pipelines. The inner one (what `/automation-build` runs for a client job) is
unchanged from design-note.md section 4 — reused, not redesigned:

```
P0 Intake + full inventory (read only)
P1 Spec (L0) -> CHECKPOINT A: go spec
P2 Environment (L1, L3): preflight, TEST records, flow off, snapshots
P3a Zapier AI draft (if Zapier): check bound account first; draft stays off; not evidence
P3 Build (L4): one change at a time, readback + evidence + changelog line
P4 Test (L5): test plan -> test-report.json
P5 Verify: fresh verifier subagent, then check_report.py -> CHECKPOINT B: Martin sees it
P6 Go-live (L6): cleanup, each G action after "go A<n>", canary record, +24h check
P7 Monitor + handover: alerts, daily reconciliation, runbook, client message draft
```

The outer one (this build, "automation-completion" = finish and install the above):

```
Step 1 — Verify existing build artifacts (done: coverage-map.md). Skill draft, 3 hooks,
         2 scripts, 9 templates, scorecard, test scenarios all present and current
         (skill draft last touched 2026-10-14).
Step 2 — CHECKPOINT 1 (this report): scope question to Martin — finish/install the
         existing automation-build design under this id, or build something else. Also:
         where to install the hooks (user-level vs project-level settings.json).
Step 3 — Install: copy the skill to the chosen location, merge the hooks settings
         snippet, after Martin's install-location go. (Separate from, and gating, the
         install build-checklist gate for THIS id.)
Step 4 — Re-run S1-S3 trigger tests in a fresh session (4.1); run one real functional
         test — the next real Marcel/other-client automation task, or a safe dry run if
         none is pending (4.2); baseline vs. the Skool-funnel build's own history of
         corrections/tool calls (4.3); re-score with the scorecard, now expecting D5/D6
         to clear (4.5).
Step 5 — CHECKPOINT 2: show Martin the new scorecard + one real tested output. Wait.
Step 6 — Ship: commit, confirm registry entry (already present), memory file update
         noting "installed" instead of "NOT installed", no scheduled run (this skill is
         Martin-triggered, not scheduled).
```
