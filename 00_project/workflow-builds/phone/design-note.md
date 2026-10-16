# Maps Playbook Design Note

Workflow ID: phone
Date: 2026-10-16
Owner: Martin

## 1. Concrete Use Cases (Step 2.1)

### Use Case A: 90-Day Build-Up Plan (e.g. Praxis Suriya)
- **Trigger:** `/maps-playbook suriya`
- **Steps:** Ingest audit run JSON (populates 69 measures); harvest GSC, Falcon, and citation data for remaining 8 measures; run `scripts/score.py` to triage gaps into `d1-30`, `m2+`, and `later`; generate HTML board and Excel sheet; present to Martin at Checkpoint A; draft client bundle at Checkpoint B; execute approved batch at Checkpoint C.
- **Tools:** `python3 scripts/validate_catalog.py`, `python3 scripts/score.py`, `python3 scripts/render_board.py`, `python3 scripts/build_sheet.py`.
- **Result:** Phased 77-measure growth road map, live status tracking, and `_run.json`.

### Use Case B: Strategic Competitive Review (e.g. Martin Hüwel)
- **Trigger:** "Maps-Playbook für Hüwel: Was fehlt für Platz 1?"
- **Steps:** Check bedrock clearance from un-burning; evaluate high-leverage measures (G01–G25 profile optimizations, W01–W34 website local signals, O01–O18 authority links); compute gap score; present prioritized task list.
- **Tools:** `python3 scripts/falcon_read.py`, `python3 scripts/validate_run.py`, `python3 scripts/render_board.py`.
- **Result:** Competitive gap analysis highlighting top 5 growth levers.

## 2. Real Task Solved by Hand (Step 2.3)
- **Reference Simulation:** Martin Hüwel & Praxis Suriya audit feeds.
- **Context Noted:**
  - Audit feed reuse is essential: 69 of 77 measures come directly from the audit. Never recompute audit fields from scratch.
  - Active un-burning harm blocks matching growth measures (e.g., G01, G02, G04, G20–G22, W13, W14, W18, W19, W34, O02–O04, O16, O19 must remain locked while harm items are unresolved).
  - Every measure status requires proof: `done`, `partly`, `missing`, `n/a`, or `unknown`.
  - Phasing matches 90-day sprints: `d1-30` (quick wins), `m2+` (medium-term structural work), `later` (ongoing maintenance).

## 3. Pipeline Map & Checkpoints (Step 2.4)

```
[Martin's Trigger: /maps-playbook <client>]
                    │
                    ▼
[Step 0–1: Readiness & Evidence Harvest from Audit]
                    │
                    ▼
[Step 2–3: Build 77-Measure Matrix & Validate]
                    │
                    ▼
         🛑 [ CHECKPOINT A: Martin reads board ]
                    │
                    ▼
[Step 4–5: Convert Gaps to Tasks & Client Bundle]
                    │
                    ▼
         🛑 [ CHECKPOINT B: Martin releases client bundle ]
                    │ (Client approves)
                    ▼
         🛑 [ CHECKPOINT C: Martin approves batch execution ]
                    │
                    ▼
[Step 6–8: Execute Approved Batch, Re-Check & Deliver]
```

## 4. Degrees of Freedom Breakdown (Step 2.5 - Rule R1.7)

| Step | Operation Type | Implementation | Degree of Freedom |
|---|---|---|---|
| Step 0: Readiness gate | Deterministic | Verify client ID, audit run file, unburn state | 0 (Strict check) |
| Step 1: Evidence harvest | Deterministic | Read audit JSON, GSC, and cached Falcon report | 0 (Python scripts) |
| Step 2: Matrix generation | Deterministic | Map audit fields to 77 measures via catalog rules | 0 (Python script) |
| Step 3: Validation | Deterministic | `validate_run.py` (checks evidence, age, schema) | 0 (Python script) |
| Checkpoint A | Governance | Review one-page board; count corrections | Human Gatekeeper |
| Step 4: Gap scoring & tasks | Semi-Deterministic | `score.py` generates priority; agent adds copy | Medium (Structured prompt) |
| Step 5: Client bundle | Qualitative | Draft client-safe summary (HWG/BRAO checked) | High (Prompt copywriting) |
| Checkpoint B & C | Governance | Release bundle; approve execution batch | Human Gatekeeper |
| Step 6–8: Execution & delivery | Controlled Action | Execute approved batch; emit `_run.json` | 0 (Strict protocol) |
