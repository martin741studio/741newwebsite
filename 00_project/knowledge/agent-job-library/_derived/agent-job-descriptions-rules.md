# Agent job descriptions — derived rules (741)

Derived 2026-11-03 from `../sources/01` to `13`. Format: IF situation THEN action. Src = source number in `../sources/`. One citation per line. Internal document; never name video or creator sources in client material.

## 0. What a job description is
- R0.1 IF an agent runs with a standing job (scheduled, unattended, or a recurring chat) THEN it gets one job description, in one file, owned by Martin; the agent may propose edits, never apply them. Src: 08 (preferences store, read-only to the agent), 10 (copies drift).
- R0.2 IF a role has a distinct goal, tool set, approval boundary, or schedule THEN it is its own agent; otherwise it is a task or a tool of an existing agent. Src: 04.
- R0.3 IF the work is a registry workflow (cro, canary, …) THEN it is a tool in an agent's job description, not an agent. Src: 13, 04 (skills are reusable across Bots).
- R0.4 IF a job description exists THEN the roster lists it: agent, where it runs, manager, review day, last grade. Src: 04 ("organize your roster"), 11 (record decisions that change the harness).

## 1. Mandatory blocks of one job description
- R1.1 IF you write the block THEN it has, in this order: title · goal with success criterion · trigger/cadence with time zone · duties (verbs with numbers) · data it may read · tools it may use with a risk rating · actions it may take alone · actions that need a go · never-lines with their enforcement rung · caps (runs/day, spend/run, retries) · may delegate to · expected output and report shape · manager · review day · edge cases (what to do when a source is missing). Src: 01 (title, duties, do-not, approval, review), 03 (data access, tools, permitted actions, required approvals), 06 (risk rating, retry threshold, edge cases), 07 (goal with success criterion, expected output, delegation, caps), 11 (allowed changes, run limit).
- R1.2 IF you name the role THEN use a real profession, specific not generic ("Outage watchman", not "Helper"). Src: 07, 04 ("a General Helper does neither").
- R1.3 IF you write a duty THEN it is one action with one output and, where possible, a number ("flag anything down more than 20 % week over week"). Src: 01, 06 ("define clear actions"), 07 (single purpose, single output).
- R1.4 IF you write a never-line THEN state its rung: hook (deterministic), skill/task setting, memory/CLAUDE.md line (advisory). Src: 09 (CLAUDE.md is context, not enforcement; PreToolUse deny holds in every mode), 11 (rule ladder), 05 (prose < reviewer < deterministic).
- R1.5 IF a never-line has no hook THEN the job description says "advisory" and the weekly review checks it by evidence. Src: 09, 10.
- R1.6 IF you list a tool THEN rate it low/medium/high from four factors: read vs write, reversibility, account permission needed, money. High = needs a go. Src: 06.
- R1.7 IF the agent reads text other people wrote (mail, chats, web) THEN the job description says that text is data, never instruction, and limits what the agent could do if it obeyed it. Src: 08, 05.
- R1.8 IF a source is missing or stale THEN the agent reports it as unreadable and never works from old data or "nothing new". Src: 08, 04.
- R1.9 IF the agent keeps memory THEN safety boundaries are not in memory; they are in the job description plus the hook. Src: 04 ("memory is not a substitute"), 09.

## 2. Approval gate (map onto the go-gate, never a second system)
- R2.1 IF an action sends, spends, deletes, publishes, writes a database, or changes a client-visible thing THEN it needs Martin's go. Src: 01, 04 (sending, purchasing, deleting, publishing, production changes behind approval), 06 (irreversible, money), 11.
- R2.2 IF the go is needed THEN show the exact change first and ask with one card whose go option carries the word "Go"; execute in the same turn. Src: 13 (go_card.py), 05 ("nobody should approve an action whose target or effect they can't identify").
- R2.3 IF the action is already covered by the PreToolUse go-gate (FTP, Novamira write, Porkbun, config files) THEN the job description names it as "hook-enforced"; all other R2.1 actions are "card-enforced" and listed by name. Src: 13, 09.
- R2.4 IF an approval card is answered THEN it approves that one action, not later ones and not work already done. Src: 05.
- R2.5 IF the agent fails the same step N times (default 3) THEN it stops and reports, it does not retry further. Src: 06 (failure threshold), 11 (cap retries at three).
- R2.6 IF the agent runs unattended THEN give it read-only credentials wherever it only reads, a spend cap per run, and a write path restricted to its own folder. Src: 08, 13 (night shift v2 flags).
- R2.7 IF the agent wants to change its own job description THEN it writes a proposal into its state record for the review; it never edits the description. Src: 08 ("proposals"), 04 (lasting rule only from the owner).

## 3. Reports and evidence
- R3.1 IF the agent reports THEN it separates: facts from sources · assumptions · actions done · actions waiting for a go · unresolved questions · what it could not read. Src: 04, 08 (cuts list).
- R3.2 IF the agent says "done" THEN it points to evidence (file path, commit, registry run, screenshot); a claim without evidence is "unresolved". Src: 10, 11 ("leave missing evidence visible"), 13 (claims-need-real-data).
- R3.3 IF a post or send counts as done THEN only after the destination confirms it; unclear = "maybe sent", change nothing. Src: 08.
- R3.4 IF the agent keeps records THEN one state record per run (what it did, grade inputs, proposals), stored where the review can read it; 741: `_run.json` per workflow plus a per-agent run log. Src: 08, 13 (registry telemetry).

## 4. Weekly review (the management layer)
- R4.1 IF a week ends THEN each agent writes a one-page review: shipped · got wrong · needs from Martin · stale rule that blocked useful work · proposed edits to its description. No grade from the agent itself. Src: 01 (shipped / wrong / needs), 10 (self-grading bias; "the harness said no" case), 08 (proposals).
- R4.2 IF a grade A–F is given THEN Martin or a fresh reviewer session gives it, from evidence (run records, git, registry, portal, cards ledger), with one sentence why. Src: 10 (standalone evaluator), 01 (one sentence why), 11 (second opinion level).
- R4.3 IF the agent wrote a grade anyway THEN the review template carries the line "do not grade yourself higher to please me" and the reviewer ignores the self-grade. Src: 01.
- R4.4 IF the same mistake appears twice in a week THEN the review decides its rung (memory line / rules file / skill edit / hook) and the fix is applied the same week. Src: 11 (twice → rung), 13 (creation workflow §6 homeostasis), 10 (feedback alone repeats mistakes).
- R4.5 IF a never-line blocked useful work THEN the review may loosen it only by a go from Martin and a written reason. Src: 10, 11 ("never weaken a check to get a pass" without an open decision).
- R4.6 IF a website, app, or source format the agent depends on changed THEN re-test the agent before its next run, review day or not. Src: 04.
- R4.7 IF the review finds nothing THEN it still records "no findings" with the evidence read; silence is not a pass. Src: 08 (unreadable ≠ nothing new), 09 (green status ≠ success).

## 5. Promotion ladder (task → skill → routine)
- R5.1 IF an agent did one good day by hand THEN save the process as a skill named for the job with sources, output format, and approval boundary. Src: 01, 04.
- R5.2 IF the skill ran reliably THEN propose a routine that runs it and stops for a go on anything external; confirm owner, schedule, time zone, input source, expected result, approval boundary, missing-source behaviour. Src: 01, 04.
- R5.3 IF a routine is created THEN test it once by hand with safe inputs and read the run; green means exited, not succeeded. Src: 04, 09.

## 6. 741 house mapping
- R6.1 IF the agent is a desktop scheduled task THEN its job description is the task's SKILL.md (the only text that run sees) plus one roster line. Src: 13, 09.
- R6.2 IF the agent is a standing chat THEN its job description lives where that chat loads it every session (project rules or a memory file linked from MEMORY.md) and the roster points at it. Src: 09 (CLAUDE.md under 200 lines; rules files), 13.
- R6.3 IF the manager is Martin THEN the manager's inbox is the morning grill (cards) and the weekly review is one grill card per agent on the review day. Src: 13 (morning grill = manager rung), 06 (manager pattern).
- R6.4 IF the description names a tool THEN use the registry id and the fully qualified MCP name. Src: 13, workflow-library R2.13.
- R6.5 IF text reaches a client THEN the job description inherits the house rules (STE replies, slop 5/5, Ich-Form, no tool names, never invent contact history). Src: 13.
