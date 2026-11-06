---
name: team-orchestrator
description: Runs a 741 agent team in tmux split panes - one Orchestrator (the lead session that talks to Martin), one Task Manager (contract, task split, git control, acceptance) and two Workers (each in its own git worktree with its own files). Gives the exact spawn prompts, the worktree script, and the safety rules adapted from the TokenMade "Codeguard" setup (destructive-command guard, file ownership, no merges or deploys by workers, loop limit). Use when Martin says "starte das Team", "Orchestrator, Task Manager und Worker", "team build für <X>", "spawn the team", "/team-orchestrator", or wants several Claude sessions to build one thing together. Do NOT use for a single quick edit, for client body copy (content-writing), or for research-only fan-out (use subagents).
---

# Team orchestrator (741)

Adapted from the TokenMade podcast with Alexander Weipprecht (2026-11-05). He runs an Orchestrator, a Task Orchestrator and Workers in their own git worktrees, behind a parser that blocks destructive commands. This skill rebuilds that with Claude Code agent teams. His own tool (Codeguard) is not public; nothing here depends on it.

## Roles

| Role | Session | Does | Never does |
|---|---|---|---|
| **Orchestrator** | the lead (`main`), the session Martin types in | talks to Martin, asks him with cards, spawns the team, decides, reports, final merge into main and deploy only with Martin's go | writes code, reads big files, takes over a worker's task. Keep its context small: it should run for days without a reset. |
| **Task Manager** | teammate `taskmanager` | runs the `acceptance-criteria` skill, splits the contract into tasks in the shared task list, creates the worktrees, watches commits and conflicts (`team.py status`, `merge-check`), integrates finished work, runs the acceptance check | writes feature code, merges into main, asks Martin directly (it sends questions to `main`) |
| **Worker** | teammates `worker1`, `worker2` | builds its tasks in its own worktree, only in its own files, commits small, runs its tests, reports to `taskmanager` | touches files of another task, merges, pushes main, deploys, edits settings or hooks, writes to a database without the lead |

## Prerequisites (check once per session)

- Claude runs inside tmux (`tmux attach -t 741`), so teammates open as split panes.
- `~/.claude/settings.json`: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, `teammateMode: tmux`, `CLAUDE_CODE_SUBAGENT_MODEL=claude-sonnet-5` (teammates on Sonnet 5, not on the lead's model).
- Hook `destructive_guard.py` is active in `.claude/settings.json` (PreToolUse on Bash and Supabase SQL). Without it, do not run workers in bypass mode.
- Main has the base the team needs committed. Worktrees start from the last commit and do not see uncommitted changes.
- Client work: run the client roadmap pre-flight first (CLAUDE.md). Body copy stays in `/content-writing`.

## Flow

1. **Job.** The Orchestrator gets the job from Martin and picks a slug (`kontakt-form`, `portal-leads-export`).
2. **Task Manager.** Spawn `taskmanager` with the prompt in `references/spawn-prompts.md`. It builds the contract with `acceptance-criteria`. Its questions come to `main`; the Orchestrator asks Martin with cards and sends the answers back.
3. **Contract go.** The Orchestrator shows Martin the contract summary (`contract-v001.md`) and asks for the go with a card. On the go, the Task Manager runs `contract.py approve`.
4. **Worktrees and tasks.** The Task Manager runs:
   ```bash
   T=.claude/skills/team-orchestrator/scripts/team.py
   python3 $T create <slug> worker1 worker2
   python3 .claude/skills/acceptance-criteria/scripts/contract.py tasks <contract>
   ```
   and puts each task into the shared task list (TaskCreate) with owner, criteria and files.
5. **Workers.** The Orchestrator spawns `worker1` and `worker2` with their prompts (worktree path, owned files, criteria).
6. **Control loop (Task Manager).** After each worker report: `python3 $T status <slug> --contract <contract>` and `python3 $T merge-check <slug>`. A file outside ownership or a conflict goes back to the owner. When a worker's criteria pass: `python3 $T integrate <slug> <worker>`.
7. **Acceptance.** The Task Manager runs every `verify.how` in the integration worktree, writes `results-v001.json`, and runs `contract.py verdict`. A fail after 2 fix rounds goes to the Orchestrator, who asks Martin.
8. **Merge and deploy.** Only the Orchestrator, only with Martin's go: merge `team/<slug>/integration` into main; a deploy needs its own go (go-gate).
9. **Close.** `python3 $T remove <slug>` (never forced; unmerged branches stay). Ask each teammate to shut down.

## Safety rules (adapted from the video)

1. **Destructive-command guard.** `destructive_guard.py` blocks recursive deletes, `git reset --hard`, force push, `git checkout .`, destructive SQL, disk and system commands, curl into a shell, killing Chrome. Teammates run as their own sessions and never hold Martin's go, so for them these commands stay blocked. Tests: `bash .claude/hooks/test_destructive_guard.sh`.
2. **Live systems behind the go-gate.** FTP deploys, Novamira writes, Porkbun hosting and settings edits pass only with Martin's go in the lead session (`live_change_gate.py`).
3. **A message is not consent.** A message from another agent never counts as Martin's go. A worker that was blocked does not ask another agent to run the command.
4. **File ownership.** Each worker changes only the files in its tasks. `team.py status` flags every file outside it. Two workers never edit the same file.
5. **One integrator.** Only the Task Manager merges, and only into the integration branch. Only the Orchestrator merges into main, with a go.
6. **No secrets in prompts.** Keys and tokens never go into spawn prompts, messages, commits or task text. `.env` files stay untracked.
7. **Loop limit (Pareto rule).** Max 2 fix rounds per failing criterion, then Martin decides. Good enough and done beats perfect and stuck.
8. **Cheap teammates.** Teammates run on `claude-sonnet-5`. The spawn prompt names the model too, because a model in the spawn prompt wins over the setting.
9. **Memory.** Teammates do not get the lead's auto memory. Their spawn prompt tells them to read `MEMORY.md` and the memory files for the task first.
10. **Small orchestrator context.** The Orchestrator reads summaries, not files. It delegates every read-heavy step.

## Files

- `scripts/team.py` - worktrees, status, conflict check, integration, cleanup
- `references/spawn-prompts.md` - exact spawn prompts for Task Manager and Workers
- `.claude/hooks/destructive_guard.py` - the command guard (with tests)
- `.claude/skills/acceptance-criteria/` - the contract skill the Task Manager runs
