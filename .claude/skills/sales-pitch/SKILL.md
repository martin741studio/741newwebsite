---
name: sales-pitch
description: Builds the comprehensive 60-minute live sales call cockpit and pitch architecture for Martin Drendel before an upcoming prospect strategy session. Ingests Review-Page audit data (Local Falcon grid, Speed, competitor gaps), formulates a tailored 6-phase diagnostic call choreography (Frame -> Discovery -> Prescription -> Offer Stack & Anchoring -> Objection Handling -> Close), and structures the 3-Tier Offer Stack (Starter 1.999 € / Core 90-Day 3.699 € mit Garantie / Power Engine 7.999 €). Trigger on "/sales-pitch <prospect>", "Pitch-Call mit <name> vorbereiten", "Sales Call für <prospect>", or "60-Minuten Call vorbereiten". Do NOT use for sending automated messages to prospects (use booking-sequence) or for existing client roadmap work (use client-roadmap).
---

# 741 Sales Call & High-Ticket Pitch Architecture (`sales-pitch`)

Owner: Martin Drendel · Approved 741 Studio Standard v1.0.  
Specification: `00_project/workflow-builds/sales-pitch/pipeline.md`.  

---

## Critical Rules & Guardrails

1. **No External Guru Names in Deliverables (Hard Rule):**
   Never use "Hormozi", "Miner", "Voss", "NEPQ", or "Gap Selling" in prospect-facing cockpits or scripts. All frameworks must be labeled strictly as the "741 Call-Raster" and "741 Wachstums-System".
2. **Fixed 3-Tier Offer Ladder:**
   Always present the upper anchor first (**Power Engine 7.999 €**), recommend the core offer with the guarantee (**90-Tage-Erfolgspaket 3.699 €**), and keep the technical fix (**Starter 1.999 €**) strictly as a downsell fallback.
3. **The Guarantee Precedes the Price:**
   In Phase 4, the Performance Guarantee (Ziel in 90 Tagen nicht erreicht = kostenlose Weiterarbeit oder Geld zurück) must be explained *before* the 3.699 € price tag is opened.
4. **Data Anchoring Invariant:**
   Every financial ROI calculation must be grounded in the prospect's real customer/patient lifetime value (LTV), not arbitrary generic numbers.

---

## Operational Checklist

When triggered for a prospect, execute sequentially:

```
[ ] Phase 1: Ingestion & Intelligence Scan
    [ ] Ingest prospect profile from 00_project/prospects/<slug>/
    [ ] Read baseline audit data (Local Falcon SoLV, Page Speed, competitor density)
    [ ] Calculate prospect-specific economics (Ticket size x frequency = LTV)

[ ] Phase 2: Call Cockpit Assembly
    [ ] Draft Phase 1 (Min 00–05): Non-needy Frame & Diagnostic Agenda
    [ ] Draft Phase 2 (Min 05–20): NEPQ Discovery & Cost of Inaction (Keenan Gap)
    [ ] Draft Phase 3 (Min 20–35): 3-Pillar Solution Prescription (No feature vomit)
    [ ] Draft Phase 4 (Min 35–45): 3-Tier Offer Stack, Math Anchor & Guarantee
    [ ] Draft Phase 5 (Min 45–55): Accusation Audit & Top 3 Custom Rebuttals
    [ ] Draft Phase 6 (Min 55–60): Seamless Close & Onboarding Calendar Hold

[ ] Phase 3: Deterministic Linting
    [ ] Run verify_pitch.py on the drafted cockpit
    [ ] Ensure 0 forbidden guru terms, 6 phases intact, 3 price tiers validated

[ ] Phase 4: Stage Deliverable & Telemetry
    [ ] Save to 00_project/prospects/<slug>/sales-cockpit.md
    [ ] Emit telemetry to _run.json
    [ ] Present cockpit summary to Martin
```

---

## Verification Command

Before handing over the call cockpit to Martin, run:

```bash
python3 .claude/skills/sales-pitch/scripts/verify_pitch.py 00_project/prospects/<slug>/sales-cockpit.md
```
Must print: `VERIFICATION PASSED: All 4 invariant checks succeeded.`
