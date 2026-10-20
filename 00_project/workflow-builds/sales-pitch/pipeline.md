# Step 2.4 Pipeline Specification: Sales Pitch Architecture (`sales-pitch`)

Date: 2026-10-17  
Workflow ID: `sales-pitch`  

---

## The Cybernetic Regulation Loop

```
[ Prospect Booking & Intelligence Ingestion ]
• Booking form inputs (goals, team size, current revenue)
• Review-Page audit: Local Falcon grid, Speed score, competitor gaps
• Prior touchpoints: WhatsApp pre-call sequence (M1–M3)
                     │
                     ▼
[ Phase 1: Mathematical & LTV Grounding (Deterministic) ]
• Script calculates Prospect LTV, monthly revenue upside, and price anchor
• Maps baseline gaps to the 3-Tier Offer Stack
• Generates pre-call diagnostic sheet
                     │
                     ▼
[ Phase 2: Checkpoint 1 Gate (Design & Strategy Go) ] ──► Martin Decision Card (ask_question)
• Martin reviews and approves customized call angle & price anchor
                     │ (Approved)
                     ▼
[ Phase 3: Cockpit Assembly & Rebuttal Generation ]
• Generates `sales-cockpit.md` for Martin's live 60-minute call
• Embeds 6 chronological phases (Min 00–60)
• Incorporates pre-emptive Voss accusation audit and top 3 custom rebuttals
                     │
                     ▼
[ Phase 4: Deterministic Linting & Compliance Filter ]
• Runs `scripts/verify_pitch.py`
• Checks: No guru names in prospect fields, valid price numbers, guarantee clearly stated
                     │ (0 Errors)
                     ▼
[ Phase 5: Checkpoint 2 Gate (Scorecard & Install Go) ] ──► Martin Decision Card (ask_question)
• Martin confirms scorecard ≥ 80% and approves deployment to registry
                     │ (Approved)
                     ▼
[ Phase 6: Delivery & Live Execution ]
• Cockpit ready in `00_project/prospects/<slug>/sales-cockpit.md`
• Telemetry written to `_run.json`
```
