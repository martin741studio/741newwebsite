# Backlink DACH Design Note

Workflow ID: backlink
Date: 2026-10-16
Owner: Martin

## 1. Concrete Use Cases (Step 2.1)

### Use Case A: Monthly Prospecting Sprint (e.g. Martin Hüwel)
- **Trigger:** `/backlink-dach huewel, nürnberg`
- **Steps:** Ingest budget & competitors; run DataForSEO backlink gap analysis against 8 competitors; filter out Pillar A directories (route to citations); score targets across Pillars B–E; generate Google Sheet with Freigabe boxes; wait for Martin's Checkpoint 4 Go; hand off approved rows to outreach team.
- **Tools:** `node scripts/gap-analysis.mjs`, `python3 scripts/build_sheet.py`, `python3 scripts/write_run.py`.
- **Result:** Phased backlink target sheet with approved contacts and `_run.json`.

### Use Case B: Zero-Budget Organic Partner Outreach
- **Trigger:** "Kostenlose lokale Backlinks für <Kunde> finden"
- **Steps:** Set budget to 0 €; restrict analysis to Pillar B (ecosystem, associations, suppliers) and Pillar D (digital PR, expert quotes); produce target list for direct relationship outreach.
- **Tools:** `node scripts/gap-analysis.mjs`, `python3 scripts/build_sheet.py`.
- **Result:** Curated organic collaboration target sheet.

## 2. Real Task Solved by Hand (Step 2.3)
- **Reference Simulation:** Martin Hüwel pilot run (`00_project/assets/huewel/backlinks/`).
- **Context Noted:**
  - Pillar A border is absolute: all directories (Jameda, Doctolib, Theralupa, Gelbe Seiten) belong to `citations-dach`. `build_sheet.py` strictly refuses Pillar A rows.
  - Outreach must be human-executed: agents never send emails, never poll inboxes, and never trigger automated payment.
  - Every row in the deliverable sheet requires a traceable Quelle and Kontakt. Rows with missing contacts are rejected by the validator.
  - Reviews do not block backlinks: weak reviews are handled as a separate task; local B2B partnerships proceed independently.

## 3. Pipeline Map & Checkpoints (Step 2.4)

```
[Martin's Trigger: /backlink-dach <client>, <city>]
                    │
                    ▼
[Step 0: Start Gate & Readiness Check]
                    │
                    ▼
         🛑 [ CHECKPOINT 0: Martin Go for Paid API calls ]
                    │
                    ▼
[Step 1–3: Competitor Gap Analysis (DataForSEO) & Filtering]
                    │ (Pillar A routed to Citations module)
                    ▼
[Step 4: Build Target Workbook (build_sheet.py)]
                    │
                    ▼
         🛑 [ CHECKPOINT 4: Martin approves Sheet & Freigabe boxes ]
                    │
                    ▼
[Step 5: Hand Off to Human Outreach (Airmailer) & Log Telemetry]
```

## 4. Degrees of Freedom Breakdown (Step 2.5 - Rule R1.7)

| Step | Operation Type | Implementation | Degree of Freedom |
|---|---|---|---|
| Step 0: Input validation | Deterministic | Verify client ID, city, budget | 0 (Strict check) |
| Step 1: Competitor gap | Deterministic | `gap-analysis.mjs` (8+ competitors via DataForSEO) | 0 (Script) |
| Step 2: Target classification | Qualitative / Prompt | Map to Pillars B–E; weed out PBNs | High (Prompt heuristics) |
| Step 3: Directory routing | Deterministic | Split Pillar A to `citations` hand-over | 0 (Strict script filter) |
| Step 4: Workbook generation | Deterministic | `build_sheet.py` (XlsxWriter) | 0 (Python script) |
| Checkpoint 4 | Governance | Review Sheet; tick Freigabe boxes | Human Gatekeeper |
| Step 5: Outreach execution | Controlled Action | Human sends via Airmailer; agent logs telemetry | Human Executor |
