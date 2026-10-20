# 741 Workflow-Raster — Rules for building Claude workflows

Derived 2026-10-11 from the official docs in `../official-docs/` (fetched the same day), the recent blog posts in `../blog/` (July–October 2026) and the video extracts in `extracts/`. Internal document. Call it "741 Workflow-Raster" in client material. Never name YouTube sources in client material.

Format: IF situation THEN action. Why. Src = file in `../official-docs/` or `../blog/`, or `V<NNN>` = video number in `../videos/`.

Freshness rule: this file reflects the state of October 2026. Re-run `00_project/workflow-creation-workflow.md` section 7 every 4–6 weeks. Drop any source older than 3 months.

---

## 0. Decide first: which primitive

- R0.1 IF the instruction must hold in every session THEN put it in `CLAUDE.md` (under 200 lines). IF it is a multi-step procedure THEN make it a skill. Why: CLAUDE.md loads every request and costs context; a skill loads only when used. Src: claude-code/features-overview.md, claude-code/memory.md
- R0.2 IF you paste the same playbook or prompt for the third time THEN save it as a skill in `.claude/skills/<name>/SKILL.md`. Src: claude-code/features-overview.md ("Build your setup over time")
- R0.3 IF a side task reads many files or produces output you never reread THEN route it through a subagent. Why: the summary comes back, the noise stays out of the main context. Src: claude-code/sub-agents.md, claude-code/best-practices.md
- R0.4 IF a job needs more than a handful of subagents, or findings must be cross-checked before you see them THEN ask for a dynamic workflow (`ultracode` keyword or "use a workflow"). Src: claude-code/workflows.md
- R0.5 IF something must happen every time with zero exceptions THEN write a hook, not a CLAUDE.md line. Why: CLAUDE.md and skills are advisory; hooks are deterministic. Src: claude-code/hooks-guide.md, claude-code/features-overview.md ("Put guardrails in hooks")
- R0.6 IF Claude needs an external system THEN connect it as MCP and teach the usage in a skill. Why: MCP = tools, skill = how to use them well. Src: platform/complete-guide-skills.md (kitchen analogy), claude-code/features-overview.md
- R0.7 IF the task repeats on a schedule with no conversation around it THEN use a routine (Claude Code, cloud) or a Cowork scheduled task. IF it is a stream of related tasks with a goal that outlasts one session THEN use a Project. Src: claude-code/routines.md, claude-code/claude-projects.md, cowork/schedule-recurring-tasks.md
- R0.8 IF a second repository or a teammate needs the same setup THEN package skills, hooks, agents and MCP as a plugin. Src: claude-code/plugins_overview.md
- R0.9 IF a workflow runs unattended on a schedule and talks to external systems THEN consider Claude Managed Agents with vault credentials, memory stores and a budget. Src: blog/building-effective-agent-automations.md
- R0.10 IF the task is small and you can describe the diff in one sentence THEN skip plan mode and do it directly. Why: planning adds overhead. Src: claude-code/best-practices.md

## 1. Design the workflow before you write it

- R1.1 IF you start a new workflow THEN define 2–3 concrete use cases first: trigger phrase, steps, tools, result. Src: platform/complete-guide-skills.md ("Start with use cases")
- R1.2 IF you build a skill THEN write evaluations BEFORE extensive documentation: run the task without the skill, note the failures, write three test scenarios, then write the minimal instructions that pass them. Src: platform/best-practices.md ("Build evaluations first")
- R1.3 IF you want a reliable skill THEN iterate on ONE hard task until Claude succeeds, then extract the winning approach into the skill. Why: faster signal than broad testing. Src: platform/complete-guide-skills.md ("Pro Tip")
- R1.4 IF the feature is large THEN let Claude interview you with `AskUserQuestion` first and write a spec to `SPEC.md`; execute the spec in a fresh session. Src: claude-code/best-practices.md ("Let Claude interview you")
- R1.5 IF you design the process THEN separate the phases: Explore (plan mode, read only) → Plan → Implement → Verify → Commit. Src: claude-code/best-practices.md
- R1.6 IF you define success THEN set measurable targets: triggers on ~90 % of relevant queries, completes in X tool calls, 0 failed API calls, no user corrections. Src: platform/complete-guide-skills.md ("Define success criteria")
- R1.7 IF a step is fragile or must run in exact order THEN give low freedom (exact script, no parameters). IF many approaches are valid THEN give high freedom (heuristics). Src: platform/best-practices.md ("Set appropriate degrees of freedom")
- R1.8 IF the workflow is a batch or destructive operation THEN use plan-validate-execute: write a plan file, validate it with a script, then execute, then verify. Src: platform/best-practices.md ("Create verifiable intermediate outputs")

## 2. Write the SKILL.md

- R2.1 IF you write the frontmatter THEN the `description` states WHAT the skill does AND WHEN to use it, in third person, with the trigger phrases users really say. Max 1,024 characters; combined `description` + `when_to_use` is cut at 1,536 characters in the listing. Src: platform/best-practices.md, claude-code/skills.md (frontmatter table)
- R2.2 IF you name the skill THEN use kebab-case, max 64 characters, no "claude" or "anthropic", no XML brackets anywhere in the frontmatter. Src: platform/best-practices.md, platform/complete-guide-skills.md
- R2.3 IF the body grows THEN keep SKILL.md under 500 lines and move detail into reference files linked ONE level deep from SKILL.md. Why: Claude previews nested references with `head -100` and misses content. Src: platform/best-practices.md ("Avoid deeply nested references")
- R2.4 IF a reference file is longer than 100 lines THEN put a table of contents at the top. Src: platform/best-practices.md
- R2.5 IF a step is deterministic THEN bundle a script (`scripts/validate.py`) and tell Claude to RUN it, not to read it. Why: code is deterministic, language is not; scripts save tokens. Src: platform/best-practices.md ("Provide utility scripts"), platform/complete-guide-skills.md
- R2.6 IF the workflow has many steps THEN include a checklist Claude copies into its reply and ticks off. Src: platform/best-practices.md ("Use workflows for complex tasks")
- R2.7 IF output quality matters THEN add a feedback loop: run validator → fix → repeat, and state "only proceed when validation passes". Src: platform/best-practices.md ("Implement feedback loops")
- R2.8 IF the output format is fixed THEN give a template and say "ALWAYS use this exact template". IF adaptation helps THEN give a default and allow judgment. Src: platform/best-practices.md ("Template pattern")
- R2.9 IF style matters THEN give 2–3 input/output example pairs. Why: examples beat descriptions. Src: platform/best-practices.md ("Examples pattern")
- R2.10 IF the skill has side effects (deploy, send, publish) THEN set `disable-model-invocation: true` so only `/name` triggers it. Src: claude-code/skills.md, claude-code/best-practices.md
- R2.11 IF the skill is long and self-contained THEN set `context: fork` so it runs in a subagent and keeps the main context clean. Src: claude-code/skills.md
- R2.12 IF the skill needs live data THEN inject it with `` !`command` `` (dynamic context) so the data is inlined before Claude reads the skill. Src: claude-code/skills.md ("Create your first skill")
- R2.13 IF the skill calls MCP tools THEN write fully qualified names `Server:tool`. Why: otherwise "tool not found". Src: platform/best-practices.md ("MCP tool references")
- R2.14 IF you write instructions THEN use one term per concept, present a default with one escape hatch, never a list of alternatives, and never time-sensitive text (put old behaviour in an "Old patterns" section). Src: platform/best-practices.md
- R2.15 IF Claude does not follow an instruction THEN put it at the top under `## Critical`, make it verifiable ("Run X before Y"), or move it into a script. Src: platform/complete-guide-skills.md ("Instructions not followed")
- R2.16 IF the skill is for Cowork or the claude.ai account THEN enable it in Customize > Skills; `~/.claude/skills/` is NOT read by Cowork, cloud sessions or routines. Src: claude-code/skills.md ("Use skills in Cowork and cloud sessions")

## 3. Context and memory

- R3.1 IF performance drops THEN the context is probably full. Run `/clear` between unrelated tasks and after two failed corrections on the same issue. Src: claude-code/best-practices.md ("Avoid common failure patterns")
- R3.2 IF a rule matters only for part of the project THEN put it in `.claude/rules/<topic>.md` with `paths:` frontmatter so it loads on demand. Src: claude-code/memory.md
- R3.3 IF CLAUDE.md grows THEN ask for each line "would removing this cause a mistake?" and cut what Claude can derive from the code. Run `/doctor` for trim proposals. Src: claude-code/best-practices.md, claude-code/memory.md
- R3.4 IF Claude keeps skipping ONE instruction THEN add emphasis ("IMPORTANT") to that one line only. Src: claude-code/best-practices.md
- R3.5 IF important facts must survive compaction THEN write them into CLAUDE.md or add "When compacting, always preserve …" to CLAUDE.md. Src: claude-code/best-practices.md, claude-code/memory.md
- R3.6 IF you want Claude to learn from corrections THEN keep auto memory on; `MEMORY.md` loads only its first 200 lines or 25 KB, so keep one line per entry. Src: claude-code/memory.md
- R3.7 IF a scheduled agent needs to remember state THEN give it two stores: `preferences` (yours, read-only) and `state` (its own, read-write: bookmarks, ledger, run records). Re-read preferences every run. Src: blog/building-effective-agent-automations.md

## 4. Verification

- R4.1 IF you hand Claude a task THEN give it a check it can run: tests, build, script that diffs output, screenshot compare. Why: without a check, "looks done" is the only stop signal. Src: claude-code/best-practices.md ("Give Claude a way to verify its work")
- R4.2 IF the run is unattended THEN gate the stop: `/goal` condition, a Stop hook, or a verification subagent. Src: claude-code/best-practices.md
- R4.3 IF you repeat the same manual check after each change THEN encode it as a verification skill. Chain: `/code-review` → `/simplify` → `/verify`. Src: blog/building-verification-loops-with-skills.md
- R4.4 IF a skill produces an artifact THEN embed the check in the producing skill ("After creating X, run Y and fix errors before reporting"). IF the check spans workflows THEN keep it standalone. Src: blog/building-verification-loops-with-skills.md
- R4.5 IF work ran unattended THEN have a fresh subagent review the diff against the plan and report only gaps that affect correctness. Src: claude-code/best-practices.md ("Add an adversarial review step")
- R4.6 IF Claude reports success THEN demand evidence: the command, its output, or a screenshot. Src: claude-code/best-practices.md
- R4.7 IF you test a skill THEN test three things: triggers on obvious tasks, triggers on paraphrases, does NOT trigger on unrelated tasks; then functional tests; then baseline comparison with/without skill. Src: platform/complete-guide-skills.md ("Recommended Testing Approach")
- R4.8 IF a skill under-triggers THEN add keywords and trigger phrases to the description. IF it over-triggers THEN add negative triggers ("Do NOT use for …"). Src: platform/complete-guide-skills.md
- R4.9 IF you build a plugin THEN run `claude plugin eval` against test cases; it also runs each case without the plugin to show the gain. Src: claude-code/plugin-evals.md, whats-new/2026-w37.md

## 5. Subagents and parallel work

- R5.1 IF you define a subagent THEN give it one clear goal, a short `description` (all descriptions together under 15,000 tokens), a restricted `tools` list, and a model that fits the job (Haiku for cheap reads). Src: claude-code/sub-agents.md
- R5.2 IF a review must be independent THEN run it in a fresh context (subagent or second session). Why: a model is biased towards code it just wrote. Src: claude-code/best-practices.md ("Writer/Reviewer")
- R5.3 IF you fan out over many files THEN loop `claude -p` with `--allowedTools` and `--permission-mode dontAsk`, or run `/batch`; test on 2–3 items first. Src: claude-code/best-practices.md ("Fan out across files")
- R5.4 IF a workflow runs many agents THEN run it on a small slice first and watch `/workflows` for token use. Default size guideline is `medium` (under 10 agents). Src: claude-code/workflows.md ("Cost")
- R5.5 IF a reviewer is told to find gaps THEN tell it to flag only correctness gaps. Why: it will always find something. Src: claude-code/best-practices.md

## 6. Scheduled and unattended automations

- R6.1 IF the automation reads sources on a schedule THEN read from a bookmark per source, never from a fixed window like "last 24 hours". Src: blog/building-effective-agent-automations.md
- R6.2 IF a source fails THEN report it as unreadable, never as "nothing new". Src: blog/building-effective-agent-automations.md
- R6.3 IF the automation posts somewhere THEN count the post as sent only after the destination confirms it; update ledger and bookmarks only after that. Src: blog/building-effective-agent-automations.md
- R6.4 IF items can change between read and post THEN re-check every item right before posting; assert or drop, never hedge. Src: blog/building-effective-agent-automations.md
- R6.5 IF the agent only reads a source THEN give it read-only credentials there, and cap spend per run (start at 3–5× a normal run). Src: blog/building-effective-agent-automations.md
- R6.6 IF the automation computes dates THEN state the time zone in the prompt. Why: server time zone makes "today" into "yesterday". Src: blog/building-effective-agent-automations.md
- R6.7 IF you write a routine prompt THEN make it self-contained and explicit about success. Why: nobody is there to clarify. Src: claude-code/routines.md
- R6.8 IF a routine must act on fire-payload text THEN say so explicitly in the prompt ("Investigate the alert in the routine-fire-payload block"); otherwise the payload is inert data. Src: claude-code/routines.md
- R6.9 IF you schedule a routine on the hour THEN pick a few minutes past the hour (9:07, not 9:00). Minimum interval is one hour. Src: claude-code/routines.md
- R6.10 IF a routine shows a green status THEN still open the run; green means the session exited, not that the task succeeded. Src: claude-code/routines.md
- R6.11 IF a routine needs a skill THEN commit it to the repository's `.claude/skills/` or enable it on the claude.ai account. Src: claude-code/skills.md, claude-code/routines.md
- R6.12 IF a Cowork scheduled task should run THEN validate the skill in chat first, then schedule; scheduled tasks run in the cloud with the same connectors, skills and plugins. Src: cowork/schedule-recurring-tasks.md, cowork/get-started-with-cowork.md

## 7. Mods, projects and new surfaces (October 2026)

- R7.1 IF you want to change how Claude Code behaves or looks THEN write a mod (small TypeScript function in a plugin) instead of fighting the prompt. Src: claude-code/plugins_mods_overview.md, blog/claude-code-mods.md
- R7.2 IF the work is a stream of related tasks across sessions THEN use a Project: set instructions once, send tasks to one conversation, let threads run in the cloud. Start with "propose threads before starting" until a few come back right. Src: claude-code/claude-projects.md
- R7.3 IF you want Claude to keep working until a condition holds THEN set a `/goal`; a separate evaluator re-checks after every turn. Src: claude-code/goal.md, claude-code/best-practices.md
- R7.4 IF you want to distribute to others THEN submit the plugin to the Claude directory through the developer portal. Src: blog/build-plugins-for-claude.md

## 8. 741-specific adaptations

- R8.1 IF a workflow produces client material THEN it ends with the message draft for the client and the Drive link (see memories `message-before-deploy`, `always-give-drive-link`).
- R8.2 IF a workflow touches a live website THEN it includes a per-change "go" checkpoint (memory `no-website-changes-without-go`).
- R8.3 IF a workflow quotes data THEN every data point is verified or asked for, never guessed (memory `page-content-qa-checklist`, `claims-need-real-data`).
- R8.4 IF a workflow includes a knowledge library THEN pull transcripts via Apify actor `johnvc/YoutubeTranscripts`, not via youtube-transcript-api from this IP (blocked 2026-10-11), and keep only sources from the last 3 months.

## 9. Practitioner rules from the videos (July–October 2026)

Lower authority than sections 0–8. Keep a rule here only while it agrees with the official docs. Src = video number in `../videos/`, extract in `extracts/`.

- R9.1 IF you write a prompt or skill THEN spend the words on three things: where to look, the definition of done, and a self-check. Drop personas and filler openers. Src: V027
- R9.2 IF you write a "do not" rule THEN also write what to do instead. Why: negative rules alone confuse the model. Src: V027
- R9.3 IF you create a routine THEN remove every connector it does not need; all connectors are added by default. Src: V027, claude-code/routines.md
- R9.4 IF you built a skill in `.claude/skills/` and want it in Cowork THEN add it again under Customize > Skills and restart the session. Src: V027, claude-code/skills.md
- R9.5 IF you add a rule to CLAUDE.md mid-session THEN compact, clear or restart; the file is read at session start. Src: V027
- R9.6 IF a subagent must follow a CLAUDE.md rule THEN restate it in the subagent prompt; Explore and Plan skip CLAUDE.md, and no subagent gets the conversation history. Src: V027, claude-code/sub-agents.md
- R9.7 IF you weigh subagents or agent teams THEN use them for looking (search, parallel investigation), not for context-heavy doing. Src: V027, V036
- R9.8 IF Claude makes the same tool mistake again THEN tighten the feedback loop with a PostToolUse hook that appends the check output to the tool result. Why: "a tighter feedback loop beats a smarter model". Src: V036
- R9.9 IF you already have a CLI for a system THEN write a skill that explains the CLI instead of building an MCP server. MCP is for public integrations that must work in any client. Src: V036
- R9.10 IF you add MCP servers THEN give tools descriptive names; a tool named "query" is rarely found by tool search. Src: V036
- R9.11 IF a check should fire only sometimes THEN write a hook that decides relevance fast and exits at once when irrelevant. Why: zero context cost. Src: V036
- R9.12 IF you run several sessions THEN give each its own worktree and label it with `/rename` and `/color`. Src: V036
- R9.13 IF a weekly task means logging into a portal with no API (rank tracker, ads dashboard, supplier site) THEN give it to Cowork browser use and let it drop the numbers into a file. Src: V017
- R9.14 IF a Cowork task needs local files or the local browser THEN the computer must stay awake with the desktop app open; cloud tasks run with the laptop closed. Src: V017, cowork/get-started-with-cowork.md
- R9.15 IF a non-technical person should capture a process THEN use "Record a skill" in Cowork on Mac, with no passwords or client data on screen. Src: V017, cowork/how-to-create-custom-skills.md
- R9.16 IF you switch model or fast mode mid-conversation THEN expect a full cache rebuild and higher cost; decide the model before you start. Src: V027
