# 2.6 Checkpoint 1 — Martin's go (automation-completion)

Date: 2026-10-15. Relayed via the orchestrator session, Martin's own answers:

- **Q1 (scope):** "Finish and install the existing `automation-build` workflow (not a new
  separate one)." → approved. automation-completion is NOT a new workflow design. Its
  checklist id stays "automation-completion" per the original brief, but its deliverable
  IS `automation-build`, finished and installed. Nothing under this id replaces or
  redesigns `00_project/automation-workflow.md`, the failure map, the skill draft, the
  hooks, the scripts, or the templates — it finishes installing and proving them.
- **Q2 (hook install location):** "user-level `~/.claude/settings.json`." → approved.
  Consequence: the skill itself also installs at user level (`~/.claude/skills/
  automation-build/`), consistent with Martin's own reasoning (client automation work
  also happens in other project folders, e.g. `~/huewel-site`) — a project-only install
  under `741website/.claude/skills/` would not reach those. This required fixing several
  relative paths in the skill body (see build-note.md) so the skill behaves identically
  no matter which folder it runs from.

Go recorded. Proceeding to step 3 (install) and step 4 (the two blocked tests: trigger
tests 4.1, baseline 4.3), then re-score (4.5), then report back to the orchestrator before
checkpoint 2 and before the install gate — not asking Martin directly, per the brief.
