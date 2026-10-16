# Un-Burning Design Note

Workflow ID: unburning
Date: 2026-10-16
Owner: Martin

## 1. Concrete Use Cases (Step 2.1)

### Use Case A: Client Onboarding Bedrock Repair (e.g. Praxis Suriya)
- **Trigger:** `/un-burning suriya`
- **Steps:** Ingest audit findings; run read-only public scan across GBP, directories, search index, and reviews; build `harm-register.json`; calculate Bedrock lights B–E; generate Bedrock Pack HTML report; prompt Martin for batch approval; execute approved fixes with rollback snapshot; verify bedrock light transitions to GREEN.
- **Tools:** `python3 scripts/merge_parts.py`, `python3 scripts/validate_run.py`, `python3 scripts/build_report.py`, `python3 scripts/bedrock.py`.
- **Result:** Fully remediated online profile, 0 critical red harm items, clean foundation for growth SEO.

### Use Case B: Emergency Reputation / Incident Remediation
- **Trigger:** "Schädliche Rezensionen oder falsche Adress-Einträge bei <client> bereinigen"
- **Steps:** Isolate specific malicious or invalid listings; draft official Google appeal / directory deletion requests; validate requests against Google policies; await Martin's per-item Go; submit and track verification.
- **Tools:** `python3 scripts/validate_changes.py`, `python3 scripts/bedrock.py`.
- **Result:** Legally compliant removal requests filed and tracked in `harm-register.json`.

## 2. Real Task Solved by Hand (Step 2.3)
- **Reference Simulation:** Praxis Suriya dry run (`00_project/assets/un-burning/praxis-suriya/2026-10-11-dryrun/`).
- **Context Noted:**
  - Area A (ownership/contract) must be completely decoupled from Un-Burning; it is handled during onboarding. Un-Burning treats ownership as a read-only precondition.
  - Distinguish strictly between **Harm** (broken redirects, old addresses, spam duplicate listings) and **Gap** (missing citations, low word counts). Gaps belong to growth workflows.
  - Every live change requires an explicit plan file, pre-validation, execution, and post-verification.
  - WordPress edits must be gated: never touch menu 16, page 1511, or client lead forms directly without explicit per-change Go.

## 3. Pipeline Map & Checkpoints (Step 2.4)

```
[Martin's Trigger: /un-burning <client>]
                    │
                    ▼
[Phase 1: Scan & Ingestion (Audit + Public + Preconditions)]
                    │
                    ▼
[Phase 2: Triage & Damage Map (harm-register.json)]
                    │
                    ▼
[Phase 3: Bedrock Pack Generation (HTML report)]
                    │
                    ▼
         🛑 [ CHECKPOINT 1: Martin's Go ] ──> Approved Remediation Plan
                    │
                    ▼
[Phase 4: Plan-Validate-Execute & Verification]
                    │
                    ▼
         🛑 [ CHECKPOINT 2: Martin's Go ] ──> Bedrock Green Confirmation
```

## 4. Degrees of Freedom Breakdown (Step 2.5 - Rule R1.7)

| Step | Operation Type | Implementation | Degree of Freedom |
|---|---|---|---|
| Step 1: Precondition check | Deterministic | Verify access & canonical NAP | 0 (Strict check) |
| Step 2: Audit triage | Qualitative / Synthesis | Map audit yellow/red to Harm vs Gap | Medium (Agent heuristics) |
| Step 3: Schema validation | Deterministic | `validate_run.py` against JSON schema | 0 (Python script) |
| Step 4: Bedrock status | Deterministic | `bedrock.py` (calculates lights B–E) | 0 (Python script) |
| Step 5: Report rendering | Deterministic | `build_report.py` (internal + client HTML) | 0 (Python script) |
| Checkpoint 1 | Governance | Present damage map; wait for Martin's Go | Human Gatekeeper |
| Step 6: Change staging | Deterministic | `validate_changes.py` + snapshot creation | 0 (Python script) |
| Step 7: Live remediation | Controlled Action | Execute approved deletions/appeals | Strict human Go |
| Checkpoint 2 | Governance | Verify bedrock light GREEN; wait for Go | Human Gatekeeper |
