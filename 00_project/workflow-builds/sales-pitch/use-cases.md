# Step 2.1 Use Cases: Sales Pitch Architecture (`sales-pitch`)

Date: 2026-10-17  
Workflow ID: `sales-pitch`  

---

### Use Case 1: Standard Review-Page Follow-up Call (High Intent)
- **Context:** A local medical clinic or boutique law firm watched their personalized Review-Page video and booked a 60-minute strategy call via Cal.com.
- **Trigger:** `/sales-pitch <prospect-slug>` or `Prep sales call für <Name>`.
- **Steps:**
  1. Reads `00_project/prospects/<slug>/baseline.md` and `claims.json` (Local Falcon score, Speed, Competitor gaps).
  2. Calculates Prospect LTV (e.g. 1 patient = 1.200 € LTV; 3 new patients/mo = 43.200 €/year).
  3. Prepares tailored NEPQ discovery questions and pre-emptive Voss accusation audit.
  4. Generates the 60-minute live call cockpit (`sales-cockpit.md`) with the 3-Tier Offer Stack (Core 90-Day 3.699 € mit Garantie, Upsell 7.999 €, Downsell 1.999 €).
- **Tools:** Python parser, template engine.
- **Result:** Martin enters the call with exact metrics, calibrated questions, and a structured offer presentation.

---

### Use Case 2: Inbound Referral / Warm Lead (No Review-Page Yet)
- **Context:** An inbound prospect was referred by an existing client (e.g. Maria Abel or Peggy / Bali Healing) without a prior automated Review-Page video.
- **Trigger:** `/sales-pitch <prospect-name> <domain>`.
- **Steps:**
  1. Ingests domain and runs a rapid live baseline check (Speed + Google Maps ranking overview).
  2. Formulates a live discovery flow focused on diagnosing current agency fatigue and growth blockers.
  3. Prepares an agile 3-tier presentation where audit findings are revealed interactively during Min 10–25 of the call.
- **Tools:** `read_url_content`, Rapid Audit script.
- **Result:** Full 60-minute call cockpit tailored for warm relational referral selling.

---

### Use Case 3: Skeptical / Price-Sensitive Enterprise or Niche Prospect
- **Context:** A prospect previously burned by an expensive agency ("SEO hat nichts gebracht") needs deep reassurance and hard proof before investing.
- **Trigger:** `/sales-pitch <prospect-slug> --skeptical`.
- **Steps:**
  1. Highlights the 741 Risk-Reversal Guarantee (3.699 € 90-Tage-Ziel nicht erreicht = kostenlos weiter oder Geld zurück).
  2. Front-loads proven case evidence (Sven Böhme 17→4, Maria Abel 0→100% Top-3).
  3. Generates specific Chris Voss reframing scripts for agency trauma.
- **Tools:** Proof asset indexer, risk-reversal generator.
- **Result:** Ironclad de-risking call cockpit that turns skepticism into confidence.
