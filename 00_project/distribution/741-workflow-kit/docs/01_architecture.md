# 01. The Universal Cybernetic Meta-Architecture

Every 741 workflow is architected as a **recursive regulation loop** across five structural checkpoints:

```
[ Real-World Agency Context / Client Need ]
                      │
                      ▼
    [ 1. Ingestion Membrane & Boundary Filter ]
    • Step 0: Strict 4-parameter contract (Job, Surface, Cadence, Hard Limits).
    • Step 1: Read-only research, freshness check (< 3 months), asset reuse check.
    • Filter: Fails fast on ambiguity before any file is written.
                      │ (Validated State)
                      ▼
    [ 2. Transformation Core (Degrees of Freedom) ]
    • Step 2: Solve 1 real task by hand; extract winning context; 3 test scenarios.
    • Step 3: Strict Rule R1.7 separation:
        - Deterministic math/APIs/parsing = isolated scripts in scripts/.
        - Qualitative/creative strategy = guided prompt instructions in SKILL.md.
    • Standard Structure: SKILL.md (<500 lines) + scripts/ + references/ + assets/.
                      │ (Packaged Deliverable)
                      ▼
    [ 3. Delivery & Expression ]
    • Step 5: .claude/skills/<id>/ (or .agents/skills/<id>/).
    • Universal Telemetry: writes _run.json at each checkpoint and at completion.
    • Master Overview: auto-syncs to central registry and overview dashboard.
                      │
    [ 4. Sensor Loop & Discrepancy Detection (Gates) ] ◄────────┐
    • Step 4: 3 Trigger Tests + Claude A/B Test + Baseline comparison.│
    • Scorecard: scorecard.md (≥ 80 % with zero 0s in Fit or Verif).  │
    • Gatekeeper: check_build.py blocks cp1, cp2, and install.       │
    • Homeostasis: repeated chat corrections become skill edits.     │
                      ▲                                              │ (Calibration)
                      │ (Governance)                                 │
    [ 5. Governance & Invariant Schemas (Meta-Controller) ] ─────────┘
    • Invariant Rules: rules.md, patterns.md, plain technical English.
    • Decision Records: Explicit Go at Checkpoint 1 (Design) and 2 (Ship).
```

---

## The 7 Diagnostic Parameters Audit

Every workflow must pass this 7-parameter audit before Checkpoint 2 (Ship):

| # | Diagnostic Parameter | Required Standard | Verification Method |
|---|---|---|---|
| **1** | **Membrane Contract** | Crystal-clear trigger phrase, explicit input schema, strict negative trigger (`NOT:` in frontmatter), `disable-model-invocation: true` for side effects. | Step 2.1, 3.2, 4.1 |
| **2** | **State vs. Ephemeral Flow** | Persistent records stored in DB, Git, or `_run.json`. Conversation contexts and scratchpads are strictly transient. | Step 3.1, 5.3a |
| **3** | **Idempotence & Predictability** | Running the workflow twice on identical inputs produces identical, clean outputs without duplicate records or side effects. | Step 3.5, 4.2 |
| **4** | **Single Source of Truth** | One central definition for every rule or schema. Procedural logic lives in `SKILL.md`; data schema lives in `schema.md`. | Step 1.4, 3.4 |
| **5** | **Clear Definition of Done** | Sequential tickable checklist with verifiable evidence files demanded for each gate. | Step 3.3, 3.5, `check_build.py` |
| **6** | **Error Telemetry** | Emits standardized `_run.json` status at every step. Fails loudly on API timeout or unreadable sources. | Step 3.7, 5.3a |
| **7** | **Decoupled Architecture** | High modularity. Compute agents are decoupled from data schemas and delivery artifacts. | Step 2.5 (Rule R1.7) |

---

## Step-by-Step Execution Sequence

### Phase 1: Ingestion & Boundary Filter (Steps 0–1)

#### 0.0 Inputs Contract (Mandatory 4-Point Grill)
Before creating any files or directories, the 4 core inputs must be confirmed:
- **The Job:** 1–2 sentences on what enters, what transforms, and who uses the output.
- **Runtime Surface:** Terminal (Claude Code), Desktop IDE, Cloud Routine, or Subagent.
- **Frequency / Cadence:** On demand, per client, daily, or weekly.
- **Hard Limits:** What must NEVER happen (e.g. no billable API credit burn, no live production overwrite without approval).

#### 1. Read-Only Research (No files written yet)
- **1.1 Building Block:** Select the appropriate primitive (Skill, Subagent, Hook, Routine, or Managed Agent).
- **1.2 Pattern Search:** Search existing library for patterns before reinventing the wheel.
- **1.3 Asset Reuse:** Check existing capability scripts and libraries. Reuse before building.
- **1.4 Research Note:** Document the chosen block, 3 relevant rules, and open questions.

---

### Phase 2: Transformation Core & Degrees of Freedom (Steps 2–3)

#### 2. Design (Plan Mode)
- **2.1 Use Cases:** Write 2–3 concrete use cases: trigger phrase, steps, tools, deliverable.
- **2.2 Three Test Scenarios (BEFORE Body):**
  1. Obvious trigger.
  2. Paraphrased trigger.
  3. Negative trigger (must NOT trigger).
- **2.3 Simulation by Hand:** Solve ONE real task manually step-by-step; record every friction point and edge case.
- **2.4 Degrees of Freedom (Rule R1.7):**
  - **Fragile / Deterministic Step:** Data math, API parsing, file moving $\to$ isolated script in `scripts/`.
  - **Open / Qualitative Step:** Copywriting, critique, wireframing $\to$ prompt heuristics with 2–3 examples.
- **2.5 Checkpoint 1 (CP1 Gate):**
  Run `check_build.py check <id> --gate cp1`. Review the use cases, pipeline, and test scenarios. Proceed only upon explicit "Go".

#### 3. Deterministic Build
- **3.1 Directory Template:** Set up standard folder structure (`SKILL.md`, `scripts/`, `references/`, `assets/`).
- **3.2 Frontmatter Contract:** Explicit description with triggers, negative trigger (`NOT:`), and `disable-model-invocation: true` if actions cause side effects.
- **3.3 Body Structure:** Sequential tickable checklist with gates. Top 2–3 critical rules under `## Critical Rules`.
- **3.4 Modularity:** Move reference documentation into `references/`. Keep `SKILL.md` under 500 lines.
- **3.5 Verification Step:** Add an automated verification script at the end of the body: run check $\to$ fix until pass $\to$ report evidence.

---

### Phase 3: Sensor Loop & Discrepancy Detection (Step 4)

#### 4. Testing & Calibration
- **4.1 Trigger Tests:** Run the 3 scenarios in a fresh session. Verify the skill loads for 1 and 2, and rejects 3. Fix the `description`, never the body, if triggering fails.
- **4.2 Functional Test:** Run the real task in a fresh session with the skill active. Record where it stalls, guesses, or asks. Refine the skill body based on findings.
- **4.3 Baseline Comparison:** Compare with vs. without the skill: corrections, tool calls, and tokens consumed.
- **4.4 Scorecard Evaluation:** Score the workflow against `scorecard.md`. **Must score $\ge 80\%$ with zero 0s in Section A (Fit) or Section D (Verification).**

---

### Phase 4: Delivery, Expression & Governance (Steps 5–6)

#### 5. Ship
- **5.1 Checkpoint 2 (CP2 Gate):**
  Run `check_build.py check <id> --gate cp2`. Review scorecard result and one real delivered output.
- **5.2 Version Control:** Commit workflow files to Git repository.
- **5.3 Telemetry Contract:** Write `_run.json` at each checkpoint and at completion.

#### 6. Homeostatic Maintenance (Closed-Loop Self-Regulation)
- **Strict Immediate Skill/Script Patch Rule:** Every time a user corrects an output or identifies a flaw in chat during execution, the agent **MUST immediately patch the underlying `SKILL.md` or script in `scripts/`** to make the correction permanent. Never just apologize in chat.
- **Recalibration:** Re-score the workflow against `scorecard.md` after every 5 real runs.
