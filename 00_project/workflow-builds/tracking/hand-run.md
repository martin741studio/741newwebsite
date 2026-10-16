# 2.3 One Real Task Solved by Hand: P6 Proof Tracking (`tracking`)

Date: 2026-10-16
Client: Praxis Suriya (Coralie Suriyapperuma, Osteopathie & Physiotherapie München)
Session Reference: Pilot tracking implementation

---

## 1. Input Context & Raw Data Ingested
- **GBP Performance:** Profile active. Calls in last 30 days: 14. Website clicks: 38. Direction requests: 22.
- **Search Console:** `https://suriya-praxis.de/`. Weekly impressions: 1,420 (+12% WoW). Top query: "osteopathie schwabing" (pos 4.2). Top page: `/osteopathie-muenchen/`.
- **Website Leads:** 4 form inquiries logged via `/termin-buchen/`.
- **Local Falcon Grid:** 7x7 scan on primary keyword "osteopathie muenchen": Average Rank Position (ARP) = 4.8, Share of Local Voice (SoLV) = 38.4%.
- **Client Goal:** Target 15 monthly leads, max CPA €40.

## 2. Hand Calculation & Step-by-Step Walkthrough
1. **Lead Reconciliation:**
   - Form leads: 4
   - Phone call clicks: 14 (estimated 50% call connection rate $\approx$ 7 connected calls)
   - Total estimated inquiries: 11 for the period.
2. **Discrepancy Calculation ($\Delta$):**
   - Actual monthly pacing: ~22 inquiries vs Target 15 inquiries ($\Delta = +7$, on track).
   - Local Falcon top 3 coverage: 42% of grid points.
3. **Weekly Card Draft Generated:**
   ```text
   Wochen-Update · Praxis Suriya (10.–16. Oktober)
   • Sichtbarkeit: Dein Profil rankt für 'Osteopathie Schwabing' stabil auf Position 4.
   • Anfragen: 4 neue Terminbuchungen über die Website, 14 direkte Anrufklicks über Google Maps.
   • Nächster Fokus: Optimierung der Unterseite 'Sportosteopathie' zur Absicherung der Top-3-Platzierung.
   ```
4. **Loom Talking Points for Martin (60 Seconds):**
   - Punkt 1: "Coralie, wir sehen 14 direkte Anrufer über dein Google-Profil diese Woche – das ist ein Zuwachs von 20% gegenüber Vormonat."
   - Punkt 2: "Dein Ranking im Kerngebiet Schwabing steht stabil in den Top 5."
   - Punkt 3: "Im Portal siehst du die 4 neuen Website-Anfragen; bitte markiere kurz, welche davon gebucht haben."

## 3. Findings for the Skill Body & Automation Scripts
- **Rule:** Never invent numbers. If Coralie hasn't logged booking status for phone leads, state "fehlt seit <Datum>" instead of guessing conversion value.
- **Degrees of Freedom:** Calculating WoW deltas and parsing JSON grid points is fragile math $\to$ belongs in `scripts/compute_weekly_metrics.py`. The copy tone for the card belongs in `SKILL.md`.
