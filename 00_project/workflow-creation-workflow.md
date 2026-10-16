# 741 Workflow-Creation Workflow (The Meta-Architecture)

Version 1.0 · 2026-10-16 · Owner: Martin · Approved Cybernetic Meta-Standard.
Language: STE. Enforcement: `python3 .claude/skills/workflow-create/scripts/check_build.py`.
Knowledge base: `00_project/knowledge/workflow-library/` (see `INDEX.md`, `_derived/rules.md`, `_derived/patterns.md`, `_derived/scorecard.md`).

Purpose: the definitive master specification for how 741 Studio designs, builds, verifies, ships, and maintains workflows. Every new or reworked workflow begins here. This meta-architecture guarantees that every workflow operates as a self-regulating, leak-proof cybernetic system.

---

## 0. The Universal Cybernetic Meta-Architecture

Every 741 workflow is architected as a **recursive regulation loop** across five structural checkpoints:

```
[ Real-World Agency Context / Client Need ]
                      │
                      ▼
    [ 1. Ingestion Membrane & Boundary Filter ]
    • Step 0: Strict 4-parameter contract (Job, Surface, Cadence, Hard Limits).
    • Step 1: Read-only research, library freshness (< 3 mo), asset reuse check.
    • Filter: Fails fast on ambiguity before any file is written.
                      │ (Validated State)
                      ▼
    [ 2. Transformation Core (Degrees of Freedom) ]
    • Step 2: Solve 1 real task by hand; extract winning context; 3 test scenarios.
    • Step 3: Strict R1.7 separation:
        - Deterministic math/APIs/parsing = isolated scripts in scripts/.
        - Qualitative/creative strategy = guided prompt instructions in SKILL.md.
    • Standard Structure: SKILL.md (<500 lines) + scripts/ + references/ + assets/.
                      │ (Packaged Deliverable)
                      ▼
    [ 3. Delivery & Expression ]
    • Step 5: ~/.claude/skills/<id>/, registered in workflow_registry.py.
    • Universal Telemetry: writes _run.json at each checkpoint and at completion.
    • Master Overview: auto-syncs to ~/Desktop/Workflow-Uebersicht.xlsx.
                      │
    [ 4. Sensor Loop & Discrepancy Detection (Gates) ] ◄────────┐
    • Step 4: 3 Trigger Tests + Claude A/B Test + Baseline comparison.│
    • Scorecard: scorecard.md (≥ 80 % with zero 0s in Fit or Verif).  │
    • Gatekeeper: check_build.py blocks cp1, cp2, and install.       │
    • Homeostasis: repeated chat corrections become skill edits.     │
                      ▲                                              │ (Calibration)
                      │ (Governance)                                 │
    [ 5. Governance & Invariant Schemas (Meta-Controller) ] ─────────┘
    • Invariant Rules: _derived/rules.md, _derived/patterns.md, ASD-STE100 English.
    • Decision Records: Martin's explicit Go at Checkpoint 1 (Design) and 2 (Ship).
```

---

## 1. The 7 Diagnostic Parameters Audit

Every workflow must pass this 7-parameter audit before Checkpoint 2:

| # | Diagnostic Parameter | Standard Required by 741 Studio | Verification Method |
|---|---|---|---|
| **1** | **Membrane Contract** | Crystal-clear trigger phrase, explicit input schema, strict negative trigger (`NOT:` in frontmatter), `disable-model-invocation: true` for side effects. | Step 2.1, 3.2, 4.1 |
| **2** | **State vs. Ephemeral Flow** | Persistent records stored in Supabase, Git, or `_run.json`. Conversation contexts and scratchpads are strictly transient. | Step 3.1, 5.3a |
| **3** | **Idempotence & Predictability** | Running the workflow twice on identical inputs produces identical, clean outputs without duplicate records or side effects. | Step 3.5, 4.2 |
| **4** | **Single Source of Truth** | One central definition for every rule or schema. Procedural logic lives in `SKILL.md`; data schema lives in Supabase. | Step 1.4, 3.4 |
| **5** | **Clear Definition of Done** | Sequential tickable checklist with verifiable evidence files demanded for each gate. | Step 3.3, 3.5, `check_build.py` |
| **6** | **Error Telemetry** | Emits standardized `_run.json` status at every step. Fails loudly on API timeout or unreadable sources. | Step 3.7, 5.3a |
| **7** | **Coupling** | High modularity. Compute agents (Claude/Antigravity/Human) are decoupled from data schemas (Postgres) and delivery artifacts. | Step 2.5 (Rule R1.7) |

---

## 2. Gate Enforcement Protocol (`check_build.py`)

A brief from chat only adds context, topics, and limits. It never replaces or skips these steps.

1. Every new or reworked workflow runs the skill `/workflow-create <id>` (`.claude/skills/workflow-create/`).
2. It initializes `00_project/workflow-builds/<id>/build-checklist.json` with one entry per step and its evidence file.
3. The check script strictly blocks each checkpoint:
   ```bash
   python3 .claude/skills/workflow-create/scripts/check_build.py check <id> --gate cp1|cp2|install
   ```
4. Checkpoint 1, Checkpoint 2, and Installation proceed **only after `GATE PASSED`**. The full check output is presented to Martin.

---

## 3. Step-by-Step Execution Sequence

### Layer 1: Ingestion & Boundary Filter (Steps 0–1)

#### 0. Inputs Martin Gives (Mandatory Interactive Grill-Me Interview)
The agent must validate the 4 core inputs before creating any files or directories. If Martin gives a raw objective or brief, the agent is strictly forbidden from silently writing files; it must initiate an interactive grill interview:
- **The Job:** 1–2 sentences on what enters, what transforms, and who uses the output.
- **Runtime Surface:** Terminal (Claude Code), Desktop IDE, Cowork, Cloud routine, or Project.
- **Frequency:** On demand, per client, daily, or weekly.
- **Hard Limits:** What must NEVER happen (e.g. no billable API credit burn, no live client overwrite without Go, no local model daemons).
*The agent must use the grill protocol to confirm all 4 parameters before proceeding to Step 1.*

#### 1. Read-Only Research (No files written yet)
* **1.1 Building Block:** Read `_derived/rules.md` §0–1 and `_derived/patterns.md` §3. Select the building block (Skill, Subagent, Hook, Routine, or Managed Agent). Record the choice in one line.
* **1.2 Library Search:** Grep `00_project/knowledge/workflow-library/` for existing patterns:
  ```bash
  grep -ril "<term>" 00_project/knowledge/workflow-library/ | head -40
  ```
  Read order: Official doc → Recent blog → Video extract. Never read raw video transcripts when extracts exist.
* **1.3 Freshness Rule:** Verify sources in `INDEX.md` are younger than 3 months. If older than 6 weeks, re-fetch.
* **1.4 Asset Reuse:** Check existing 741 capabilities: `ls ~/.claude/skills/ .claude/skills/ 2>/dev/null` and check memory files. Reuse before building.
* **1.5 Research Note:** Write a 10–20 line note in `00_project/workflow-builds/<id>/research-note.md`: block chosen, 3 relevant rules, 1 pattern, open questions.

---

### Layer 2: Transformation Core & Degrees of Freedom (Steps 2–3)

#### 2. Design (Plan Mode)
* **2.1 Use Cases:** Write 2–3 concrete use cases: trigger phrase, steps, tools, deliverable (Rule R1.1).
* **2.2 Three Test Scenarios (BEFORE Body):** Write 3 scenarios in `test-scenarios.md`:
  1. Obvious trigger.
  2. Paraphrased trigger.
  3. Negative trigger (must NOT trigger) (Rule R1.2).
* **2.3 Simulation by Hand (Live Chat Simulation):** Solve ONE real client task live in chat with Martin BEFORE drafting the skill body. Walk through each prompt and tool call step-by-step; record every piece of context, friction point, and edge case that arises. That exact verified context forms the skill body and scripts (Rule R1.3).
* **2.4 Pipeline Map:** Draw the pipeline using `patterns.md` §4 shapes. Mark checkpoints where Martin gives approval.
* **2.5 Degrees of Freedom (Rule R1.7):**
  - **Fragile / Deterministic Step:** Data math, API parsing, file moving, database writes $\to$ isolated script in `scripts/`.
  - **Open / Qualitative Step:** Copywriting, critique, wireframing $\to$ prompt heuristics with 2–3 examples.
* **2.6 Checkpoint 1 (CP1 Gate):**
  Run `check_build.py check <id> --gate cp1`. Show Martin the full output, use cases, pipeline, and test scenarios. **Wait for Martin's explicit "Go".**

#### 3. Deterministic Build
* **3.1 Directory Template:** Create the folder from `patterns.md` §5:
  ```
  ~/.claude/skills/<name>/          # Personal / cross-project
    SKILL.md                       # Tickable checklist body (< 500 lines)
    scripts/                       # Deterministic executables (run, not read)
    references/                    # 1 level deep, TOC if > 100 lines
    assets/                        # Templates, schemas, output examples
  ```
  *(Project-only skills go to `.claude/skills/<name>/`)*.
* **3.2 Frontmatter Contract:**
  - `description`: Strict WHAT + WHEN + negative trigger (`NOT:`).
  - `disable-model-invocation: true` for workflows with side effects.
  - `allowed-tools`: As narrow as possible.
* **3.3 Body Structure:** Sequential checklist with gates (Rules R2.6, R2.7). Top 2–3 critical rules under `## Critical`.
* **3.4 Modularity:** Move reference documentation into `references/`. Keep `SKILL.md` under 500 lines.
* **3.5 Verification Step:** Add an automated verification script at the end of the body: run check $\to$ fix until pass $\to$ report evidence (Rules R4.1, R4.4).
* **3.6 741 House Rules:** Verified data only, ASD-STE100 technical English, client link + Drive link at the end, per-change "Go" for live production.
* **3.7 Unattended Rules (if applicable):** Apply `rules.md` §6: bookmarks, failed reads reported as unreadable, confirm before ledger write, spend cap per run, read-only credentials.

---

### Layer 4: Sensor Loop & Discrepancy Detection (Step 4)

#### 4. Testing & Calibration
* **4.1 Trigger Tests:** Run the 3 scenarios from 2.2 in a fresh session. Verify the skill loads for 1 and 2, and rejects 3. Fix the `description`, never the body, if triggering fails (Rule R4.8).
* **4.2 Functional Test (Claude A / Claude B):** Run the real task from 2.3 in a fresh session with the skill active. Record where it stalls, guesses, or asks. Refine the skill body based on findings.
* **4.3 Baseline Comparison:** Compare with vs. without the skill: corrections, tool calls, and tokens consumed (Rule R1.6).
* **4.4 Tool Evaluations:** For plugins: `claude plugin eval`. For prompt files: `/doctor prompt-audit`.
* **4.5 Scorecard Evaluation:** Score the workflow against `scorecard.md`. **Must score $\ge 80\%$ with zero 0s in Section A (Fit) or Section D (Verification).**

---

### Layer 3 & 5: Delivery, Expression & Governance (Steps 5–6)

#### 5. Ship
* **5.1 Checkpoint 2 (CP2 Gate):**
  Run `check_build.py check <id> --gate cp2`. Present Martin with the scorecard result and one real delivered output. **Wait for Martin's explicit "Go".**
* **5.2 Version Control:** Commit project skills to Git `main`. For personal skills, log path in project memory.
* **5.3a Registry & Telemetry Contract:**
  - Register workflow: `python3 00_project/workflow-registry/workflow_registry.py add-workflow --workflow <id> --name "Label"`.
  - Enforce `_run.json`: The skill must write `00_project/assets/<client>/<workflow_id>/<YYYY-MM-DD>/_run.json` at each checkpoint and at completion.
  - Auto-sync: Stop hook runs `sync` automatically to update `~/Desktop/Workflow-Uebersicht.xlsx`.
* **5.3b Martin Guide:** If the workflow produces an artifact seen by clients or prospects, place the Martin character guide per `00_project/assets/brand/martin-guide/README.md`.
* **5.3c Memory File:** Create `~/.claude/projects/-Users-martindrendel-741website/memory/<workflow>.md` with trigger, path, checkpoints, and known boundaries. Add one line to `MEMORY.md`.
* **5.4 Scheduled Setup:** If scheduled, create the routine or LaunchAgent, run it once by hand, inspect the log output (Rule R6.10).
* **5.5 Install Gate:** Run `check_build.py check <id> --gate install`. Verify final clean status.

#### 6. Homeostatic Maintenance (Closed-Loop Self-Regulation)
* **Strict Immediate Skill/Script Patch Rule:** Every time Martin corrects an output or identifies a flaw in chat during any workflow execution, the agent is strictly forbidden from merely apologizing and re-running with a one-off prompt patch. The agent **MUST immediately patch the underlying `SKILL.md` or script in `scripts/`** to make the correction permanent.
* **Recalibration:** Re-score the workflow against `scorecard.md` after every 5 real client runs.
* **Upstream Updates:** When Claude Code or model APIs ship relevant upgrades, review `official-docs/whats-new/` and eliminate obsolete workarounds.

---

## 4. Quick Execution Card

```
1. Validate 4 inputs (Job, Surface, Cadence, Limits).
2. Choose building block; verify source freshness (< 3 mo).
3. Write 3 test scenarios (Obvious, Paraphrase, Negative) BEFORE body.
4. Solve 1 real task by hand with Martin; extract context.
5. Decompose by Rule R1.7: deterministic scripts vs qualitative prompts.
6. 🛑 CHECKPOINT 1 (Design Go) via check_build.py.
7. Build SKILL.md (<500 lines) + scripts/ + references/ + assets/.
8. Run Trigger Tests, Claude A/B Test, Baseline comparison.
9. Score against scorecard.md (≥ 80 %, no zero in A or D).
10. 🛑 CHECKPOINT 2 (Ship Go) via check_build.py.
11. Register in workflow_registry.py; enforce _run.json telemetry.
12. Commit to Git; document in Claude Project memory.
```
