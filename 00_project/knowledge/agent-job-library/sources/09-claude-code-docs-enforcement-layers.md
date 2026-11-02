# 09 — Claude Code docs: where an instruction is enforced (CLAUDE.md, rules, skills, hooks, subagents, permissions)

Type: official documentation. Local copies in `00_project/knowledge/workflow-library/official-docs/claude-code/` (memory.md, hooks-guide.md, sub-agents.md, skills.md, best-practices.md). Checked 2026-11-03 against the local copies; the derived rules R0.1, R0.5, R2.10, R3.2, R5.1 in `workflow-library/_derived/rules.md` already cover them.

## Key content
- CLAUDE.md is "context, not enforced configuration". A line in it is a request. Under 200 lines; every line checkable; prune what the code already tells.
- `.claude/rules/*.md` with `paths:` frontmatter loads only when matching files are touched (scoped standing instructions).
- Skills load on demand; `disable-model-invocation: true` restricts a skill with side effects to an explicit `/name` call; `allowed-tools` narrows what the skill may use.
- Hooks are deterministic. `PreToolUse` fires "before any permission-mode check, in every permission mode, including dontAsk. A hook that returns permissionDecision: 'deny' blocks the tool even in bypassPermissions mode." Decision values: allow / deny (reason fed back to Claude) / ask (prompt the user). `Stop` hooks can block the end of a turn (cap 8 consecutive blocks). `PermissionRequest` hooks can answer prompts on the user's behalf; keep matchers narrow.
- Subagent frontmatter: `tools` (allowlist), `disallowedTools` (denylist), `model`, `permissionMode`, `maxTurns`, `memory`, `skills`, `isolation: worktree`. "disallowedTools is applied first, then tools."
- Auto mode (blog, 2026-03-24, GA 2026-07-10): a classifier reviews each tool call for destructive actions; it may allow risky ones when intent is ambiguous; recommended only in isolated environments.
- Memory: auto memory loads the first 200 lines / 25 KB of MEMORY.md; one line per entry.
- Desktop scheduled tasks and routines: a scheduled run's prompt must be self-contained; green status means the session exited, not that the task succeeded; open the run.

## Assessment for 741
New vs. video: the enforcement ladder. Tyler's "do not" lines live at the weakest rung (prose in memory). Claude Code gives five rungs: CLAUDE.md line → path rule → skill → hook → subagent tool list.
Marketing: none; documentation.
Usable for 741: the job description must state, per "never" line, its rung. 741 already has the go-gate at the hook rung for FTP deploys, Novamira writes, Porkbun, config files, and the slop gate at Stop. Lines without a hook are advisory and must say so. For a scheduled agent, the job description is the SKILL.md of the scheduled task (`~/.claude/scheduled-tasks/<id>/SKILL.md`), which is the only text that run sees.
