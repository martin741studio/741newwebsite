# Workflow patterns — which building block for which job

Derived 2026-10-11 from `../official-docs/` and `../blog/`. Companion to `rules.md`. Internal document.

## 1. The building blocks (state October 2026)

| Block | Where it lives | Loads | Use it for |
| --- | --- | --- | --- |
| CLAUDE.md | `./CLAUDE.md`, `~/.claude/CLAUDE.md` | every session, full text | "always do X" rules, build commands, conventions. Keep under 200 lines |
| Rules | `.claude/rules/<topic>.md` with `paths:` | every session, or when a matching file opens | scoped conventions |
| Skill | `.claude/skills/<name>/SKILL.md` + `scripts/`, `references/`, `assets/` | description at start, body on use | repeatable procedures, reference knowledge, `/name` commands |
| Subagent | `.claude/agents/<name>.md` | when spawned, own context | research, review, isolated workers, cheap-model work |
| Dynamic workflow | `.claude/workflows/<name>.js` | when invoked | dozens of agents from one script, cross-checked findings |
| Hook | `settings.json` → `hooks` | on lifecycle event | deterministic checks, formatting, blocking, notifications |
| MCP | `claude mcp add`, `.mcp.json`, claude.ai connectors | tool names at start | external systems (Drive, Supabase, Slack, browser) |
| Plugin | `<plugin>/.claude-plugin/plugin.json` + skills/agents/hooks/mcp/mods | where enabled | package and distribute a setup |
| Mod | TypeScript function inside a plugin | at startup | change Claude Code UI or behaviour |
| Routine | claude.ai/code/routines, `/schedule` | cloud, on schedule / API / GitHub event | unattended repeatable work with a repository |
| Cowork scheduled task | Cowork → Scheduled | cloud, on schedule | unattended knowledge work with connectors and account skills |
| Project | claude.ai/code → Projects | one coordinating conversation + cloud threads | a stream of related tasks with a goal that outlasts a session |
| Managed Agent | Claude Platform, `agent.md` + `deployment.md` | cloud, cron | production automations with vault credentials, memory stores, budget |

## 2. The 3-layer blueprint, mapped to real files

The "3 layers" idea from the planning note (Directives, Orchestration, Execution) maps to concrete files:

| Layer | What it holds | Where it goes |
| --- | --- | --- |
| 1 Directives | goal, inputs, deliverable, edge cases, quality bar | `SKILL.md` body (steps + checklist + template), `references/` |
| 2 Orchestration | decision points, error handling, when to ask the human, checkpoints | `SKILL.md` conditional workflow section; `context: fork`; subagent definitions; `/goal` or Stop hook as gate |
| 3 Execution | scripts, API calls, data folders | `scripts/*.py`, MCP tools (fully qualified `Server:tool`), `assets/` templates |

CLAUDE.md is NOT layer 1. It holds only the always-on rules. Procedures go into skills.

## 3. Decision tree for a new 741 workflow

1. Does it run on a schedule with nobody present?
   - Yes, with a repository → Routine.
   - Yes, knowledge work with connectors → Cowork scheduled task.
   - Yes, production-grade with secrets and budget → Managed Agent (daily-brief reference implementation).
   - No → continue.
2. Is it a stream of related tasks over days or weeks? → Project.
3. Is it one repeatable procedure Martin triggers? → Skill with `disable-model-invocation: true` if it has side effects.
4. Does it read many files or need parallel workers? → Skill that spawns subagents, or a dynamic workflow if more than ~10 agents.
5. Must one step happen every time without fail? → Hook.
6. Does it need an external system? → MCP + a skill that teaches the usage.

## 4. Proven skill shapes

### 4.1 Sequential workflow with gates (most 741 deliverables)

```
# Workflow: <name>
Copy this checklist and tick it off:
- [ ] Step 1: Collect inputs (run scripts/collect.py)
- [ ] Step 2: Research (subagent, read only)
- [ ] Step 3: Draft (template in assets/)
- [ ] Step 4: Validate (run scripts/validate.py; fix until it passes)
- [ ] Step 5: Checkpoint: show Martin the draft, wait for "go"
- [ ] Step 6: Deliver (file + Drive link + client message)
```

Techniques: explicit order, dependencies between steps, validation at each gate, rollback instructions. Src: platform/complete-guide-skills.md Pattern 1.

### 4.2 Multi-MCP coordination

Phases per system: Phase 1 Drive, Phase 2 Supabase, Phase 3 Portal, Phase 4 message. Pass data between phases in files. Validate before each phase change. Src: Pattern 2.

### 4.3 Iterative refinement

Draft → run check script → fix → re-check → stop when the quality threshold is met. State the threshold. Src: Pattern 3; platform/best-practices.md feedback loops.

### 4.4 Plan-validate-execute (batch or destructive)

Analyze → write `changes.json` → `scripts/validate.py changes.json` (verbose errors) → execute → verify. Src: platform/best-practices.md.

### 4.5 Verification chain

`/code-review` → `/simplify` → `/verify` → custom `/design-check`. Embed a check at the end of the producing skill, or chain with a wrapper skill. Src: blog/building-verification-loops-with-skills.md.

### 4.6 Writer / Reviewer

Session A writes. Session B (fresh context, or a subagent with `tools: Read, Grep, Glob`) reviews against the plan and reports only correctness gaps. Src: claude-code/best-practices.md.

### 4.7 Research fan-out

Dynamic workflow: one agent per source → verifier agents refute each finding → one synthesis agent. Bundled example: `/deep-research`. Src: claude-code/workflows.md.

### 4.8 Scheduled brief (daily-brief reference)

Sources with per-source bookmarks → decide (an item earns a line only if the reader acts today) → verify live right before posting → post → confirm → update ledger and bookmarks → run record. Two memory stores: `preferences` (read-only), `state` (read-write). Budget per run. Src: blog/building-effective-agent-automations.md.

## 5. Skill file template (741 default)

```
---
name: <kebab-case>
description: <What it does>. Use when <trigger phrases Martin says>. Do NOT use for <neighbour task>.
disable-model-invocation: true   # only for skills with side effects
context: fork                    # only for long self-contained runs
allowed-tools: Read, Grep, Glob, Bash(python:*)
---

# <Name>

## Critical
- <the 2–3 rules that must never be broken>

## Inputs
- <what Martin provides>

## Workflow
Copy this checklist and tick it off:
- [ ] Step 1 …
- [ ] Step N: Verify (run `scripts/validate.py`), fix until it passes

## Output template
<exact template or default>

## Checkpoints
- After step X: show Martin … and wait for "go".

## References
- `references/<topic>.md` (one level deep, with table of contents if over 100 lines)
```

## 6. Context budget rules of thumb

| Item | Budget |
| --- | --- |
| CLAUDE.md | under 200 lines |
| SKILL.md body | under 500 lines |
| All subagent descriptions together | under 15,000 tokens |
| MEMORY.md index | first 200 lines / 25 KB load |
| Skill description + when_to_use | 1,536 characters shown |
| Dynamic workflow default size | medium = fewer than 10 agents |

## 7. What changed recently (watch list)

- Mods for Claude Code (2026-10-01): TypeScript functions in plugins change UI and behaviour.
- Projects in Claude Code (beta, 2026-09/10): coordinating conversation + cloud threads.
- `claude plugin eval` (2026-09, week 37): test suites for plugins.
- Routines: research preview, cloud, schedule / API / GitHub triggers; `/schedule` in CLI.
- Cowork and chat merged into one Claude (rolling out); scheduled tasks run in the cloud.
- Managed Agents reference implementation for scheduled automations (2026-10-08).
- `/doctor prompt-audit` finds outdated or conflicting instruction files (v2.1.283+).
- Auto mode is the default permission mode in interactive sessions (v2.1.283+).
