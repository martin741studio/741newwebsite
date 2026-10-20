---
name: template-workflow
description: Analyzes and transforms input data into verified deliverables. Use when user says "run workflow", "generate deliverable", or "process task". Do NOT use for general casual chat or unapproved direct database edits.
disable-model-invocation: true
context: fork
allowed-tools: Read, Grep, Glob, Bash(python:*)
---

# Template Workflow

## Critical Rules
1. Never apply modifications to live production systems without an explicit human confirmation checkpoint.
2. Every number, metric, and analytical claim must be validated via `scripts/run.py`; never hallucinate data.
3. If `scripts/verify_env.py` fails, halt immediately and prompt user to inspect `.env`.

## Prerequisites & Setup
- Python 3.10 or higher installed.
- Dependencies installed: `pip install -r requirements.txt`
- Configuration file configured: Copy `.env.example` to `.env` and supply required variables.

## Execution Checklist
Copy this markdown checklist into your response and tick each step off sequentially:

- [ ] **Step 1: Pre-Flight Verification**
  Run `python3 scripts/verify_env.py`. Confirm environment variables and dependencies are valid before proceeding.

- [ ] **Step 2: Collect & Ingest Data**
  Execute deterministic data intake:
  `python3 scripts/run.py --client "<ClientName>" --mode "audit"`

- [ ] **Step 3: Qualitative Synthesis & Review**
  Review the generated output at `00_project/assets/<ClientName>/output.json`. Apply brand voice heuristics and format according to the output template.

- [ ] **Step 4: Automated Output Validation**
  Validate the integrity of the generated artifacts:
  `python3 scripts/validate.py --file "00_project/assets/<ClientName>/output.json"`
  *Note: If validation fails, correct the issues and re-run. Do NOT proceed to checkpoint until validation passes 100%.*

- [ ] **Step 5: Human Checkpoint (Go / No-Go)**
  Present the validated draft and key metrics to the human supervisor. Wait for explicit "Go" before final delivery.

- [ ] **Step 6: Telemetry & Record Keeping**
  Confirm that `_run.json` has been updated with the run status, timestamp, and metrics.

## Standard Output Format
Every final deliverable must conform to this schema:
```markdown
# [Deliverable Title]

### 1. Executive Summary
- Concise 3-bullet breakdown of key findings and status.

### 2. Verified Metrics Table
| Metric | Value | Verification Source |
|---|---|---|
| [Key Metric 1] | [Value] | [Script / API] |

### 3. Action Items & Next Steps
1. Immediate action item.
2. Secondary recommendation.
```
