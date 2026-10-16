# 2.4 Pipeline Map: P4 CRO Homepage Track A (`cro`)

Date: 2026-10-16
Workflow: CRO Homepage Track A (`cro`)

---

```
[ Inputs: Practice Name, Live URL, GBP Link, Preferred Contact Channel ]
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 0: Intake & Folder Setup                               │
│ • Local asset directory: 00_project/assets/<client>/cro/    │
│ • Drive mirror initialization: CRO Homepage                 │
│ • Initialize _status.md and run-checklist.md                │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 1 & 2: Research, Crawl & Data Extraction               │
│ • Firecrawl / Chrome crawl of current website               │
│ • Extract brand colors, typography tokens, logo file        │
│ • Ingest Content-Pool keywords & sitetree (Step 1.0)        │
│ • Compile 02-data/dataset.md (every fact cited or [FEHLT])  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 3: Copywriting via content-writing Skill               │
│ • Voice sheet from live site + direct-response headlines     │
│ • SEO & GEO optimization (H1 keyword+city, entity blocks)   │
│ • Gates G1–G6 verification via run_gates.py                 │
│ • HWG / BRAO compliance check                               │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
                   🛑 CHECKPOINT 1: COPY APPROVAL
                   (Martin reviews 04-copy/copy.md)
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 4 & 5: Design Document & GPT Visual Style Reference    │
│ • check_prompt.py verifies every quoted text matches copy   │
│ • GPT creates ideal visual reference image (layout/mood)    │
│ • Style reference is strictly layout guide, never copy      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 6: Desktop HTML Prototype & Verification               │
│ • Build index.html at 1440px desktop viewport               │
│ • First screen fits in 701px height (H1, proof, CTA)        │
│ • Measure DOM via scripts/measure.js (M1–M10)               │
│ • Chrome visual check (cro-homepage-visual-check.md)        │
│ • verify.py verification loop until PASS                    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
                   🛑 CHECKPOINT 2: PROTOTYPE APPROVAL
                   (Martin reviews prototype at 1440px)
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 7: Drive Staging, Registry & Desktop Sync              │
│ • stage_drive.py packages files; browser upload to Drive     │
│ • check_drive.py validates MANIFEST.json                    │
│ • Register in cro-registry/registry.json                    │
│ • Rebuild ~/Desktop/Workflow-Uebersicht.xlsx                │
│ • Deliverable report with full-page screenshot & Drive link │
└─────────────────────────────────────────────────────────────┘
```
