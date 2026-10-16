# Pipeline Specification: P4/P0 CRO Track B Design-Intense Showcase (`cro_b`)

Date: 2026-10-16
Workflow ID: `cro_b`

---

## The 5-Layer Cybernetic Architecture

```
[ Trigger: "/cro-track-b <client> <url>" or "Track B für <client>" ]
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ Layer 1: Ingestion Membrane & Boundary Filter                   │
│ • Step B0: Grill-Me Questionnaire (cro-track-b-questionnaire.md)│
│ • Step B1: Data & Brand Inventory (dataset.md, brand.md)        │
│ • Guard: Fails fast if client is HWG without Martin's override  │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ Layer 2: Transformation Core & Human-in-the-Loop Voting         │
│ • Step B2: Reference Board (5 refs, take/leave, 2 anti-refs)    │
│ • Step B2b: Live Interactive Element Pool (serve_pool.py)       │
│                                │                                │
│       [ CHECKPOINT 1: Martin Votes Ja/Vielleicht/Nein ]         │
│                                │                                │
│ • Step B3: Approved Copy (reuses Track A or content-writing)   │
│ • Step B4: Concept & Storyboard (1 signature idea, max 4 comps) │
│ • Step B5: Design Doc & Media Plan                              │
│ • Step B6: Full-Page Mockup & Media Generation                  │
│ • Step B7: 1440px HTML Build with Motion Layer & X-Ray Toggle   │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ Layer 3: Delivery & Expression                                  │
│ • Step B8: QA Suite (10-point Track B checks, visual check)     │
│                                │                                │
│       [ CHECKPOINT 2: Martin Final Approval on Prototype ]      │
│                                │                                │
│ • Step B9: Handoff Pack (08-handoff.md) + Staged Drive Mirror   │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ Layer 4: Sensor Loop & Telemetry                                │
│ • Universal Telemetry: writes _run.json at each milestone       │
│ • M1–M10 Performance Metrics via scripts/measure.js             │
│ • Performance Budget Verification (perf.md)                     │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ Layer 5: Governance & Invariant Schemas                         │
│ • scripts/guard_upload.py blocks accidental remote deployment   │
│ • scripts/verify.py checks file integrity and gate conditions   │
│ • Automatic sync to ~/Desktop/Workflow-Uebersicht.xlsx          │
└─────────────────────────────────────────────────────────────────┘
```

---

## Checkpoint Protocol

### Checkpoint 1 (Design Direction & Element Pool)
- **Timing:** After Step B2b.
- **Artifact:** `00-element-pool/index.html` served on local port + `votes.json`.
- **Criteria:** Martin has voted on all 20–35 shortlisted elements. Only `Ja` and `Vielleicht` items enter Step B4.

### Checkpoint 2 (Prototype & Handoff Approval)
- **Timing:** After Step B8.
- **Artifact:** `07-prototype/index.html`, `visual-check.md`, `self-check.md`, `perf.md`.
- **Criteria:** All 10 Track B QA checks PASS; CTA visible at 701px; performance budget met; zero upload attempts without confirmation.
