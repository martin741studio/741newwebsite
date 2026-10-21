---
name: sales-pitch
description: Builds the comprehensive 60-minute live sales call cockpit and pitch architecture for Martin Drendel before an upcoming prospect strategy session. Ingests Review-Page audit data (Local Falcon grid, Speed, competitor gaps), formulates a tailored 6-phase diagnostic call choreography (Frame -> Discovery -> Prescription -> Offer Stack & Anchoring -> Objection Handling -> Close), and structures the two-package offer (Power Engine 7.999 € first as anchor, then 90-Tage-Erfolgspaket 4.999 € with value stack 15.000 €, Ergebnis-Garantie and three bonuses). Trigger on "/sales-pitch <prospect>", "Pitch-Call mit <name> vorbereiten", "Sales Call für <prospect>", or "60-Minuten Call vorbereiten". Do NOT use for sending automated messages to prospects (use booking-sequence) or for existing client roadmap work (use client-roadmap).
---

# 741 Sales Call & High-Ticket Pitch Architecture (`sales-pitch`)

Owner: Martin Drendel · Approved 741 Studio Standard v1.1 (offer update 2026-10-21).  
Specification: `00_project/workflow-builds/sales-pitch/pipeline.md`.  
Offer source of truth: live growth page `04_site/pages/growth-plan-de.html` (section "Zwei Wege, mit uns zu arbeiten") + memory `741studio-pricing.md`. Phase guide with exact wording: `references/call-raster.md`.

---

## Critical Rules & Guardrails

1. **No External Guru Names in Deliverables (Hard Rule):**
   Never use "Hormozi", "Miner", "Voss", "NEPQ", or "Gap Selling" in prospect-facing cockpits or scripts. All frameworks must be labeled strictly as the "741 Call-Raster" and "741 Wachstums-System".
2. **Two Packages Only, Anchor First:**
   Present the **Power Engine 7.999 € + monatliches Ads-Management** first as the anchor. Then recommend the **90-Tage-Erfolgspaket 4.999 €** ("Meistgewählt"). The Starter 1.999 € is NOT sold by phone anymore: never offer it, not even as a downsell. The **Marktführer-Retainer 5.000 €/Monat** after the Power Engine is said only in the call, never written in a message.
3. **Value Stack and Guarantee Before the Price:**
   In Phase 4, walk through the 10 phases with their values (Gesamtwert **15.000 €**), then state the Ergebnis-Garantie word for word, then open the **4.999 €** price:
   "Stehst du nach 90 Tagen für dein Haupt-Keyword nicht in den Top 3 auf Google Maps, arbeiten wir ohne Zusatzkosten weiter, bis du dort bist."
   No money-back promise. No −10 % discount, no struck-through list prices.
4. **Data Anchoring Invariant:**
   Every financial ROI calculation must be grounded in the prospect's real customer/patient lifetime value (LTV), not arbitrary generic numbers.
5. **Bonuses, Payment, Scarcity:**
   - Bonus bei voller Zahlung: full payment on day one → 1 Monat Sichtbarkeits-Schutz gratis (Wert 397 €). Full payment is the default.
   - Payment fallback only on request: 60 % am ersten Tag, Rest in bis zu zwei Zahlungen (no bonus).
   - Sofort-Start: yes in the call → Kick-off innerhalb von 48 Stunden.
   - Empfehlungs-Bonus: ask only AFTER the buying decision (Phase 6). Photo together in the call, the client sends it right away to two colleagues; both in a call → 1 Monat Sichtbarkeits-Schutz gratis (Wert 397 €).
   - Gebietsschutz as honest scarcity: "Pro Ort betreuen wir nur einen Betrieb deiner Fachrichtung." No invented deadlines or slot counts.
6. **Follow-up Product:** after the program, Sichtbarkeits-Schutz / Website Care 397 €/Monat, billed quarterly.
7. **Client-facing language:** all script lines in German, du-form.

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
    [ ] Draft Phase 2 (Min 05–20): 741 Diagnose-Fragen & Kosten des Wartens (cost of inaction)
    [ ] Draft Phase 3 (Min 20–35): 3-Pillar Solution Prescription (No feature vomit)
    [ ] Draft Phase 4 (Min 35–45): LTV anchor → Power Engine 7.999 € → 10-phase value stack (15.000 €) → Garantie → 4.999 € → 3 bonuses → Gebietsschutz
    [ ] Draft Phase 5 (Min 45–55): Accusation Audit & Top 3 Custom Rebuttals
    [ ] Draft Phase 6 (Min 55–60): Full payment default (fallback 60 %) → Sofort-Start kick-off in 48 h → referral photo after the yes → Sichtbarkeits-Schutz outlook

[ ] Phase 3: Deterministic Linting
    [ ] Run verify_pitch.py on the drafted cockpit
    [ ] Ensure 0 forbidden guru terms, 6 phases intact, 2 packages in anchor order, no Starter/discount, guarantee before price, bonuses + payment + referral after the yes

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
Must print: `VERIFICATION PASSED: All 10 invariant checks succeeded.`
The cockpit needs one Markdown heading per phase (e.g. `## Phase 4 …`); the order checks read the Phase 4 and Phase 6 sections.
Cockpits built before 2026-10-21 (old 3-tier prices) fail this check on purpose. Rebuild them before a call.
