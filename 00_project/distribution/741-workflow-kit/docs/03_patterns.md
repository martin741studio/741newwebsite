# 03. Workflow Patterns & Building Blocks

---

## 1. The Building Blocks Catalog

| Primitive | Where It Lives | When It Loads | Best Used For |
|---|---|---|---|
| **Global Rule** | `CLAUDE.md`, `AGENTS.md` | Every session, full text | Universal conventions, build commands, global invariants. Keep under 200 lines. |
| **Scoped Rules** | `.claude/rules/<topic>.md` | On demand when matching files open | Subsystem conventions (e.g. frontend, database, auth). |
| **Skill** | `.claude/skills/<name>/SKILL.md` | Description at startup, body on invocation | Repeatable multi-step procedures, tool usage manuals, slash commands. |
| **Subagent** | `.claude/agents/<name>.md` | When spawned, isolated context | Heavy research, code reviews, parallel data gathering. |
| **Dynamic Workflow** | Script-orchestrated agents | When invoked | Complex multi-agent fan-out and cross-verification. |
| **Hook** | `settings.json` / `hooks.json` | On specific lifecycle events | Deterministic linting, formatting, security guardrails, blocking actions. |
| **MCP Server** | `.mcp.json` | Tool names indexed at startup | External integrations (Supabase, Drive, Telegram, Canva, browser). |
| **Routine / Scheduled** | Cloud runner / Cron | Scheduled / Webhook trigger | Unattended, repeatable jobs against a repository or API. |

---

## 2. The 3-Layer Implementation Blueprint

Every robust automation maps directly into three distinct layers:

| Layer | Responsibility | File Location |
|---|---|---|
| **1. Directives** | Objective, inputs, deliverable schema, edge cases, quality bar | `SKILL.md` checklist body, `references/` |
| **2. Orchestration** | Decision points, validation feedback loops, human checkpoints | `SKILL.md` conditional logic, subagents, stop gates |
| **3. Execution** | Pure deterministic scripts, API calls, file transforms | `scripts/*.py`, MCP tools, `assets/` templates |

*Note: Global rules files (`CLAUDE.md`) are NOT layer 1. Global rules hold only always-on invariants. Multi-step procedures always go into skills.*

---

## 3. Decision Tree: Choosing the Right Primitive

1. **Does it run on a schedule with nobody present?**
   - Yes, against a code repo $\to$ **Routine / Cron Runner**.
   - Yes, production automation with API secrets and budget cap $\to$ **Managed Agent**.
   - No $\to$ Continue.
2. **Is it a stream of related tasks across multiple days?**
   - Yes $\to$ **Project / Milestone Tracker**.
3. **Is it one repeatable procedure a human triggers?**
   - Yes $\to$ **Skill** (set `disable-model-invocation: true` if it modifies data or deploys).
4. **Does it read many large files or require parallel workers?**
   - Yes $\to$ **Subagent** with isolated context.
5. **Must a validation step execute every single time with zero exceptions?**
   - Yes $\to$ **Hook**.
6. **Does it need access to an external database, API, or service?**
   - Yes $\to$ **MCP Server** + a **Skill** that explains how to use it safely.

---

## 4. Proven Workflow Shapes

### 4.1 Sequential Workflow with Gates (Default Shape)
```markdown
# Workflow: <name>
Copy this checklist and tick it off:
- [ ] Step 1: Run pre-flight check (`python3 scripts/verify_env.py`)
- [ ] Step 2: Collect data (`python3 scripts/collect.py`)
- [ ] Step 3: Transform and draft artifact
- [ ] Step 4: Run automated validation (`python3 scripts/validate.py`)
- [ ] Step 5: Checkpoint: Present draft to human and wait for explicit "Go"
- [ ] Step 6: Finalize deliverable and write telemetry to `_run.json`
```

### 4.2 Iterative Refinement Loop
Draft artifact $\to$ run check script $\to$ inspect errors $\to$ fix draft $\to$ re-run check $\to$ proceed only when tests pass 100%.

### 4.3 Plan-Validate-Execute (Batch / Destructive Operations)
Analyze request $\to$ write `plan.json` $\to$ run `python3 scripts/validate_plan.py plan.json` $\to$ execute changes $\to$ verify outcome.

### 4.4 Writer / Reviewer Pattern
Agent A (Writer) generates the artifact in session context. Agent B (Reviewer, fresh subagent with read-only tools) inspects the generated diff against the specification and reports only functional correctness gaps.

---

## 5. Context Budget Rules of Thumb

| Component | Target Budget |
|---|---|
| Global rule files (`CLAUDE.md`) | Under 200 lines |
| `SKILL.md` body | Under 500 lines |
| Skill description in frontmatter | Under 1,024 characters (cut at 1,536 total) |
| Reference files in `references/` | Max 1 level deep; include TOC if over 100 lines |
