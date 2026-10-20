# Step 2.2 Test Scenarios: Sales Pitch Architecture (`sales-pitch`)

Date: 2026-10-17  
Workflow ID: `sales-pitch`  

---

### Scenario 1 (Obvious Positive Trigger):
- **Input:** Martin says: `Bereite den 60-Minuten Sales Call für Dr. Korinna Heintze vor` or `/sales-pitch korinna-heintze`.
- **Expected Output:**
  - Skill triggers cleanly.
  - Reads existing baseline and claims from `00_project/prospects/korinna-heintze/`.
  - Emits complete 60-minute cockpit with Hormozi 3-tier pricing (Core 3.699 €, Upsell 7.999 €, Downsell 1.999 €), NEPQ discovery path, and Voss objection handling.

---

### Scenario 2 (Subtle Positive Trigger):
- **Input:** Martin says: `Ich habe morgen früh den Pitch-Call mit einem neuen Interessenten für das 90-Tage Programm, hilf mir das strukturiert aufzubauen`.
- **Expected Output:**
  - Skill detects pitch call intention.
  - Prompts for prospect name/domain if missing.
  - Guides Martin through the 6-phase call structure and anchors the offer stack.

---

### Scenario 3 (Negative / Must-Not-Trigger Scenario):
- **Input:** Martin says: `Schicke Korinna eine WhatsApp-Erinnerung für den morgigen Termin` or `Erstelle eine Review-Page für Praxis Müller`.
- **Expected Output:**
  - Skill **MUST NOT TRIGGER**.
  - WhatsApp reminders are delegated strictly to `booking-sequence`.
  - Review-Page creation is delegated strictly to `prospect-mini`.
