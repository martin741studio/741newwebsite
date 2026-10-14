# N02 — "v2.1.206 silently broke unattended scheduled tasks" (bug report)

- Org/author: community reporter, archived on claudeissues.com (mirror of an anthropics/claude-code GitHub issue)
- Type: bug report / issue tracker page
- Publish date: opened **2026-07-15**, reported against v2.1.205/209, confirmed still present on v2.1.215 and v2.1.219. Verified from the dates printed on the issue page.
- URL: https://claudeissues.com/issue/77817-bug-v2-1-206-silently-broke-unattended-scheduled-tasks-runs-no-longer-inherit-pe
- Fetch date: 2026-10-15

## Extract (own words)

- The reporter's scheduled tasks worked unattended through v2.1.205. Starting with the auto-update to v2.1.206 (observed 2026-07-14/15), every existing scheduled task silently stopped inheriting `permissions.defaultMode` from the project's `.claude/settings.local.json` and fell back to "Manual" permission mode instead.
- Evidence: captured run transcripts show `"permissionMode":"bypassPermissions"` in a run from v2.1.205 and `"permissionMode":"default"` in a run from v2.1.209, with no settings file changed in between — i.e. the CLI/app's own update changed the effective behaviour, not any local configuration edit.
- Unattended runs then stall on a permission prompt nobody is there to answer.
- The per-task permission mode can only be set through the Desktop app's task-edit form; `create_scheduled_task`/`update_scheduled_task` have no permission-mode parameter, and there is no bulk fix.
- Follow-on reports in the same thread: a macOS commenter found the per-task override sometimes reverts to "default" on its own; a Windows commenter found the per-task mode is ignored at spawn time, so runs start in Manual even when Bypass was explicitly set at task creation.
- Status at fetch time: Open, no maintainer reply cached, no fix version identified.

## IF/THEN rules for 741

1. IF the night shift (or any scheduled task) depends on an inherited or default permission mode to stay unattended, THEN don't assume an update preserves that — a documented incident shows a routine point release silently flipped every existing scheduled task from bypass to manual with zero warning and zero changelog note.
2. IF Martin pins the Claude Code version on 741-agents-01 (per N01's "pin and re-check" rule), THEN add one explicit extra check after any version bump: run one scheduled/headless task by hand immediately after updating and confirm it does NOT stop on a permission prompt, before trusting the nightly queue to it.
3. IF this class of bug recurs, THEN the fastest real-world signal is the run's own JSON output (`--output-format json`, or the task's saved transcript) showing `permissionMode` — compare it against what was configured, don't just trust that "the task ran" in the scheduler's eyes.

## Caveats

- This is a single, still-open, unverified-by-Anthropic community bug report (no maintainer reply), not an official acknowledgement. Treat the mechanism as credible (consistent with N01's and N04's documented permission-handling churn in the same months) but the specific root cause as the reporter's own analysis.
- It describes the Desktop app's scheduled-tasks feature specifically, not systemd-driven `claude -p` cron jobs like 741's night-shift-v2 runner — the exact failure path may differ, but the underlying risk (an update silently changing permission-mode defaults) generalises to any unattended invocation method.
