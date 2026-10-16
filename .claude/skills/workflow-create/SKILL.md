---
name: workflow-create
description: Runs the 741 workflow creation process for a new or reworked workflow, step by step, with a build checklist and a check script that blocks each checkpoint until every step has evidence. Use when Martin says "new workflow", "create a workflow", "build a workflow for …", "rework workflow X", "chat-based workflow architecture", or when a workflow chat is started from the chat base. Do NOT use to run an existing workflow for a client (use that workflow's own skill), and not for a one-off task.
---

# Workflow create (741 chat base)

## Critical

- The plan is `00_project/workflow-creation-workflow.md`. A brief from the chat base only adds context, topics and limits. It never replaces or shortens the steps.
- Every build keeps `00_project/workflow-builds/<id>/build-checklist.json`. Mark each step with its evidence file the moment it is done.
- Before checkpoint 1, checkpoint 2 and the install, run the check and show Martin its full output. A blocked gate means: do the missing steps first. Never ask for a go on a blocked gate.
- Questions to Martin only as AskUserQuestion cards. Replies in STE. Every delivered text through the slop check (CLAUDE.md).

## Start

```bash
C=.claude/skills/workflow-create/scripts/check_build.py
python3 $C init <id> "<Workflow name>"      # id = the later registry id, e.g. nightshift
```

Put all build files in `00_project/workflow-builds/<id>/`, unless the brief names other paths. Recommended file names: `inputs-grill.md` (Step 0.0 4 parameters), `research-note.md`, `coverage-map.md`, `use-cases.md`, `test-scenarios.md`, `hand-run.md`, `pipeline.md`, `decisions.md` (Martin's gos with date and his words), `trigger-tests.md`, `functional-test.md`, `baseline.md`, `scorecard.md`.

## Steps (sections of the creation workflow)

Copy this checklist into your reply at each checkpoint and tick it off:

```
Build progress <id>:
- [ ] 0.0 inputs grill (Job, Surface, Cadence, Limits)   - [ ] 1.1 block chosen   - [ ] 1.2 library searched   - [ ] 1.3 freshness   - [ ] 1.4 existing assets   - [ ] 1.5 research note
- [ ] 2.1 use cases   - [ ] 2.2 3 test scenarios (before the body)   - [ ] 2.3 one real task by hand   - [ ] 2.4 pipeline   - [ ] 2.5 freedom
- [ ] CHECK cp1 → 2.6 checkpoint 1 (Martin go)
- [ ] 3.1-3.7 build per template, verification step, unattended rules
- [ ] 4.1 trigger tests (fresh session)   - [ ] 4.2 functional test (fresh session)   - [ ] 4.3 baseline   - [ ] 4.4 eval/audit   - [ ] 4.5 scorecard >= 80 %
- [ ] CHECK cp2 → 5.1 checkpoint 2 (Martin go)
- [ ] 5.2 commit   - [ ] 5.3a registry   - [ ] 5.3b Martin guide   - [ ] 5.3 memory   - [ ] 5.4 scheduled run by hand
- [ ] CHECK install → install
```

After each step:

```bash
python3 $C done <id> <step> <evidence-path> "short note"
python3 $C skip <id> <step> "reason"        # only 3.7, 4.4, 5.3b, 5.4
```

At each gate:

```bash
python3 $C check <id> --gate cp1      # then cp2, then install
```

The gate log is stored in the checklist, so a later chat can see which gates passed.

## What the check enforces

- Every required step is `done` with an evidence file that exists and is not empty.
- 2.2 contains at least one must-not-trigger scenario.
- 2.6 and 5.1 point to a decision record with Martin's go.
- 4.5 shows a scorecard of 80 % or more with no blocking zero.
- 5.3a: the workflow id is in the registry. 5.3: the memory file exists and MEMORY.md lists it.

## Verification

Before you report "done" to Martin, run `python3 $C check <id> --gate install` and paste the output. Only `GATE PASSED` counts as done.
