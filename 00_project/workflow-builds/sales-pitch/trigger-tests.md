# Step 4.1 Trigger Tests: Sales Pitch Architecture (`sales-pitch`)

Date: 2026-10-17  
Workflow ID: `sales-pitch`  

---

### Test T1: Direct Slash Trigger
- **Input:** `/sales-pitch korinna-heintze`
- **Result:** MATCH. Skill activates, identifies target slug `korinna-heintze`, reads baseline data, and initiates 6-phase cockpit generation.
- **Pass/Fail:** PASS.

---

### Test T2: Conversational Natural Trigger
- **Input:** `Bereite meinen 60-Minuten Pitch Call mit Dr. Korinna Heintze vor, Fokus auf das 90-Tage Programm`
- **Result:** MATCH. Description triggers on "60-Minuten Call vorbereiten" and "Pitch-Call mit <name>", correctly mapping to `sales-pitch`.
- **Pass/Fail:** PASS.

---

### Test T3: Negative / Non-Trigger Test (Must Not Trigger)
- **Input:** `Schicke Korinna die zweite WhatsApp-Erinnerung vor dem Termin`
- **Result:** NO MATCH. Does not activate `sales-pitch`; correctly delegates to `booking-sequence`.
- **Pass/Fail:** PASS.
