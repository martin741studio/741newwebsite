# N05 — How to run Claude Code overnight safely

- Author/org: Matrix OS (cloud agent workspace vendor; "Field Notes" blog)
- Type: practitioner guide
- Publish date: 2026-08-14 (verified: article:published_time and JSON-LD)
- URL: https://matrix-os.com/blog/run-claude-code-overnight-safely
- Fetch date: 2026-10-13

## Extract (own words)

- Good overnight work has clear inputs, measurable outputs and a reversible result: tests for named modules, one dependency upgrade, one documented bug, release notes, a draft PR.
- Avoid "fix everything", production deploys, irreversible migrations, billing changes, secret rotation, and tasks that need product judgment at every step.
- Isolate the files: own worktree and branch per agent.
- Remove credentials it does not need. No production database or admin keys in the environment.
- Keep approvals for destructive commands and external writes. "Unattended" means safe work continues, not that all commands are pre-approved.
- Write explicit stop conditions into the prompt: allowed paths, allowed tests, and when to stop and leave a question.
- The run ends with a report: root cause, files changed, exact tests and results, remaining risks, draft PR link.
- Morning review: start with git status, commits and diff, not with the agent's prose. Reject "all tests pass" without the command output.

## IF/THEN rules for 741

1. IF a night task is given to an agent, THEN its prompt names allowed files, allowed commands, stop conditions and the five-part end report.
2. IF a stop condition fires, THEN the agent writes a decision card and moves to the next task instead of guessing.
3. IF Martin reviews night output, THEN the card shows the diff or the draft first and the agent's summary second.

## Limits / caveats

- Written for coding work. For 741 the "artifact" is a draft page spec, audit or message draft; the same rules apply.
- Vendor blog promoting its workspace.
