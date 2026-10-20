# Step 2.5 & 2.6 Decisions Record: Sales Pitch Architecture (`sales-pitch`)

Date: 2026-10-17  
Author: Martin Drendel & Antigravity Assistant  
Workflow ID: `sales-pitch`  

---

## 2.5 Degrees of Freedom (R1.7 Separation)

| Step | Type | Implementation | Freedom |
|---|---|---|---|
| Step 1: Ingestion & Baseline Parse | Deterministic | Python (`scripts/parse_prospect.py`) | Zero (Must match schema, no hallucinations) |
| Step 2: LTV & Math Anchoring | Deterministic | Python math formula | Zero (Mathematical exactness based on ticket size) |
| Step 3: Discovery Questioning Formulation | Guided Heuristic | LLM Prompt via NEPQ principles | Controlled (Tailored to specific prospect niche) |
| Step 4: Offer Stack & Guarantee Packaging | Deterministic | House Offer Stack (1.999 / 3.699 / 7.999 €) | Fixed price anchors, customizable target metric |
| Step 5: Accusation Audit & Objection Scripts | Guided Heuristic | Chris Voss tactical empathy & 741 matrix | Contextual adaptability |
| Step 6: Verification & Invariant Linting | Deterministic | Python (`scripts/verify_pitch.py`) | Zero (Binary Pass/Fail) |

---

## 2.6 Checkpoint 1 Decision Record (Martin Go on Design)

- **Date:** 2026-10-17
- **Participant:** Martin Drendel
- **Decisions Confirmed via Decision Cards:**
  1. *Methodology Stack:* Confirmed Hybrid Approach combining:
     - Alex Hormozi ($100M Offers & Closer Framework: Value Equation, 3-Tier Offer Stack, Risk Reversal).
     - Jeremy Miner (NEPQ: Non-needy tone, deep discovery, problem and consequence questioning).
     - Chris Voss (Tactical Empathy: Accusation audits, emotion labeling, calibrated questions).
  2. *Offer Stack Structure:* Confirmed 3-Tier Price Ladder:
     - **Core Offer (Empfehlung):** 90-Tage Local SEO & Growth Engine (3.699 €) mit messbarer Ergebnis-Garantie (Top-3 Ranking-Ziel nicht erreicht = kostenlos weiterarbeiten oder Geld zurück).
     - **Upsell:** Power Engine (7.999 €) inklusive Paid Ads Management, High-End CRO Redesign und Content-Cluster.
     - **Downsell:** Starter Setup (1.999 €) für reine technische Basisbereinigung ohne Garantie.
  3. *Call Duration & Tone:* 60-Minute structured diagnostic masterclass (Min 00–60), peer authority, zero sleazy pressure.

**Status Checkpoint 1:** APPROVED (Martin Go).

---

## 2.7 Checkpoint 2 Decision Record (Martin Go on Ship)

- **Date:** 2026-10-17
- **Participant:** Martin Drendel
- **Scorecard:** 46 / 46 (100 %) · Zero blocking zeros.
- **Evidence Output:** `00_project/prospects/korinna-heintze/sales-cockpit.md` verified via `scripts/verify_pitch.py`.
- **Decision:** Martin confirmed Checkpoint 2 GO via interactive Decision Card.
- **Approved Deployment:**
  - Register as `sales-pitch` in `workflow-registry`.
  - Install skill in `.claude/skills/sales-pitch/`.
  - Add `/sales-pitch` command to UpNote workflow overview table.

**Status Checkpoint 2:** APPROVED & SHIPPED (Martin Go).
