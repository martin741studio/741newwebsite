# 2.4 Pipeline Map: P6 Proof Tracking (`tracking`)

Date: 2026-10-16
Workflow: Proof Tracking + Quarterly War Room (`tracking`)

---

```
[ Real-World Agency Context / Ingestion Membrane ]
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ 1. Data Ingestion (Supabase & Core 5 APIs)                  │
│ • Local Falcon GBP tool reads (Free daily performance)       │
│ • Search Console daily search rollups (public.gsc_daily...) │
│ • Portal Leads (public.leads) & Form submissions            │
│ • Paid Ads spend & Campaign data (public.google_campaigns)  │
└──────────────────────────────┬──────────────────────────────┘
                               │ (Clean Normalized State)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Deterministic Calculation (Isolated Scripts in scripts/) │
│ • Weekly delta vs baseline (WoW / MoM % change)             │
│ • Goal discrepancy calculation: Δ = Actual - Goal           │
│ • Cost per booked job reconciliation                        │
│ • Rule Engine check: Red (R1–R6) and Yellow (Y1–Y9) flags   │
└──────────────────────────────┬──────────────────────────────┘
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
    [ Weekly Cadence ]                    [ Quarterly Cadence ]
┌──────────────────────────────┐      ┌──────────────────────────────┐
│ 3A. Weekly Card Draft        │      │ 3B. War-Room Pack Synthesis  │
│ • 3-bullet concise text card │      │ • 90-day progress vs goals   │
│ • Loom talking points draft  │      │ • Revenue & CAC attribution  │
│ • Error alert flags if any   │      │ • 3 renewal strategy options │
└──────────────┬───────────────┘      └──────────────┬───────────────┘
               │                                     │
               ▼                                     ▼
    🛑 CHECKPOINT: GO-W                   🛑 CHECKPOINT: GO-Q1
    (Martin 1-click release)              (Martin review of war pack)
               │                                     │
               ▼                                     ▼
┌──────────────────────────────┐      ┌──────────────────────────────┐
│ 4A. Client Portal Publish    │      │ 4B. Strategy Meeting & Log   │
│ • Tab "Ergebnisse" updated   │      │ • Client decisions logged    │
│ • Martin Loom link embedded  │      │ • Next quarter targets set   │
└──────────────┬───────────────┘      └──────────────┬───────────────┘
               │                                     │
               └──────────────────┬──────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. Universal Telemetry & Sync                               │
│ • Emits _run.json to assets/<client>/tracking/<YYYY-MM-DD>/ │
│ • Auto-syncs to ~/Desktop/Workflow-Uebersicht.xlsx          │
└─────────────────────────────────────────────────────────────┘
```
