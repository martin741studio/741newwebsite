# 02. The 741 Workflow Rules (741 Workflow-Raster)

Format: **IF** [situation] **THEN** [action]. [Why].

---

## 0. Decide First: Which Primitive to Use

- **R0.1 IF** the instruction must hold in every session **THEN** put it in `CLAUDE.md` (keep under 200 lines). **IF** it is a multi-step procedure **THEN** make it a skill. *Why:* `CLAUDE.md` loads on every request and consumes context; a skill loads only on demand.
- **R0.2 IF** you paste the same playbook or prompt for the third time **THEN** save it as a skill in `.claude/skills/<name>/SKILL.md`.
- **R0.3 IF** a side task reads many files or produces output you never reread **THEN** route it through a subagent. *Why:* The summary comes back, while raw file noise stays out of the primary context.
- **R0.4 IF** a job needs more than a handful of subagents, or findings must be cross-checked before display **THEN** ask for a dynamic multi-agent workflow.
- **R0.5 IF** an action must happen every time with zero exceptions **THEN** write a hook, not a prompt instruction. *Why:* Prompts are advisory; hooks are deterministic.
- **R0.6 IF** an agent needs an external system (database, file drive, browser) **THEN** connect it via MCP and teach usage in a skill. *Why:* MCP provides tools; the skill teaches strategy and safety.
- **R0.7 IF** the task repeats on a schedule with no active conversation **THEN** use a routine (cloud) or scheduled runner. **IF** it is a stream of related tasks outlasting one session **THEN** use a Project.
- **R0.8 IF** another repository or teammate needs the same setup **THEN** package skills, hooks, agents, and MCP configs into a portable starter kit or plugin.
- **R0.9 IF** a workflow runs unattended and touches external systems **THEN** use vault credentials, memory stores, and a strict budget cap per run.
- **R0.10 IF** a task is small and you can describe the diff in one sentence **THEN** skip plan mode and do it directly.

---

## 1. Design the Workflow Before Writing

- **R1.1 IF** you start a new workflow **THEN** define 2–3 concrete use cases first: trigger phrase, steps, tools, and deliverable.
- **R1.2 IF** you build a skill **THEN** write evaluations BEFORE extensive documentation: run the task without the skill, note failures, write three test scenarios, then write minimal instructions that pass them.
- **R1.3 IF** you want a reliable skill **THEN** iterate on ONE hard task until the agent succeeds, then extract the winning approach into the skill.
- **R1.4 IF** the feature is large **THEN** conduct an interactive interview first to produce a specification; execute the spec in a fresh session.
- **R1.5 IF** you design the process **THEN** separate the phases: Explore (read-only) $\to$ Plan $\to$ Implement $\to$ Verify $\to$ Commit.
- **R1.6 IF** you define success **THEN** set measurable targets: triggers on ~90 % of relevant queries, completes in target tool calls, zero failed API calls, zero human corrections.
- **R1.7 IF** a step is fragile or must run in exact order **THEN** give low freedom (exact script, strict parameters). **IF** many creative approaches are valid **THEN** give high freedom (heuristics and quality guidelines).
- **R1.8 IF** the workflow performs batch or destructive operations **THEN** use plan-validate-execute: write a plan file, validate with a script, execute, then verify.

---

## 2. Writing the `SKILL.md`

- **R2.1 IF** you write the frontmatter **THEN** `description` states WHAT it does AND WHEN to use it in third person, with real user trigger phrases and an explicit negative trigger (`NOT:`).
- **R2.2 IF** you name the skill **THEN** use kebab-case, maximum 64 characters, and no XML tags in the frontmatter.
- **R2.3 IF** the body grows **THEN** keep `SKILL.md` under 500 lines and move detail into reference files linked ONE level deep. *Why:* Deeply nested references get truncated.
- **R2.4 IF** a reference file is longer than 100 lines **THEN** include a table of contents at the top.
- **R2.5 IF** a step is deterministic **THEN** bundle a script (`scripts/validate.py`) and instruct the agent to RUN it, not read it. *Why:* Scripts save tokens and eliminate hallucinated math.
- **R2.6 IF** the workflow has many steps **THEN** include a tickable markdown checklist the agent copies into its response.
- **R2.7 IF** output quality matters **THEN** add an automated feedback loop: run validator $\to$ fix errors $\to$ repeat $\to$ proceed only when tests pass.
- **R2.8 IF** the output format is fixed **THEN** provide an exact template and state "ALWAYS use this exact template".
- **R2.9 IF** style matters **THEN** give 2–3 concrete input/output example pairs. *Why:* Examples beat descriptions.
- **R2.10 IF** the skill has side effects (deploy, commit, send messages) **THEN** set `disable-model-invocation: true` so only explicit command invocations trigger it.
- **R2.11 IF** the skill is long and self-contained **THEN** set `context: fork` so it runs in an isolated subagent and preserves the main session context.
- **R2.12 IF** the skill calls MCP tools **THEN** use fully qualified names: `Server:tool_name`.
- **R2.13 IF** an agent fails to follow an instruction **THEN** move it under `## Critical Rules` at the top, make it verifiable, or move it into a deterministic Python script.

---

## 3. Context and Memory Management

- **R3.1 IF** performance drops or errors repeat **THEN** clear context (`/clear`) between unrelated tasks.
- **R3.2 IF** a rule applies only to specific files **THEN** put it in scoped rules with path matching so it loads only when needed.
- **R3.3 IF** global rules grow **THEN** audit each line: "Would removing this cause a mistake?" Cut instructions that the agent can derive from code.
- **R3.4 IF** an agent must remember state across runs **THEN** provide two stores: `preferences` (read-only configuration) and `state` (read-write: bookmarks, ledger, run records).

---

## 4. Verification and Quality Gates

- **R4.1 IF** you hand an agent a task **THEN** give it an automated check it can run: tests, build command, diff script, or output validator.
- **R4.2 IF** a run is unattended **THEN** gate the stopping condition with a verification step or subagent review.
- **R4.3 IF** an agent reports success **THEN** demand evidence: execution command output, validated file path, or test log.
- **R4.4 IF** you test a skill **THEN** verify 3 dimensions: triggers on direct prompt, triggers on paraphrases, and rejects unrelated prompts.

---

## 5. Unattended and Scheduled Automations

- **R5.1 IF** an automation reads sources on a schedule **THEN** read from a stateful bookmark per source, never from a sliding time window (e.g. "last 24 hours").
- **R5.2 IF** a source read fails **THEN** report it explicitly as unreadable; never report "nothing new found".
- **R5.3 IF** the automation posts or publishes data **THEN** record the action only after the destination confirms receipt.
- **R5.4 IF** the agent only reads data **THEN** supply read-only credentials, and enforce a strict spend cap per run.
- **R5.5 IF** dates are computed **THEN** explicitly declare the timezone in prompt and code.
- **R5.6 IF** a scheduled routine reports a green status **THEN** inspect the log; green indicates process exit, not business logic success.

---

## 6. House Rules & Operational Invariants

- **R6.1 IF** a workflow touches live production systems **THEN** require an explicit human confirmation checkpoint before changes are applied.
- **R6.2 IF** a workflow quotes data or metrics **THEN** every data point must be verified by a script or confirmed by user input; never guess.
- **R6.3 IF** an execution completes **THEN** write a standardized `_run.json` telemetry record.
- **R6.4 IF** a user corrects an agent's output in chat **THEN** the agent MUST immediately patch the underlying `SKILL.md` or script in `scripts/` so the mistake never occurs again.
