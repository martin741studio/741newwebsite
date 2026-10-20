# Recommendation: review report for clients

Date: 2026-10-13. Sources: see INDEX.md (S01–S30). Status: draft for Martin. Nothing is built.

## 1. Metrics (6 numbers per client)

| # | Metric | Calculation | Source IDs |
|---|---|---|---|
| 1 | Total Google reviews | count on the profile today | S02 |
| 2 | Average rating | stars, 1 decimal | S02 |
| 3 | New reviews | last 30 days, plus average per month over last 90 days | S13, S17 |
| 4 | Goal progress | count ÷ goal (goal = 2× market leader). Show the pace per month that reaches the goal by year end. | memory rule, S07 |
| 5 | Gap to top 3 competitors | their count and rating, monthly snapshot | S11, S13 |
| 6 | Reply rate and reply time | share of reviews with a reply; median days to reply | S02, S17 |

Do not show reviewer names or review text in the report. Numbers are enough (DSGVO data minimisation).

## 2. Cadence and format

- **Portal tile (weekly update):** count vs goal as a progress bar, new in last 30 days, pace needed per month, reply rate.
- **Monthly report section:** one chart (our count, goal line, market-leader line) plus the competitor table.
- **Alert (within 24 h):** a new review with 1–3 stars goes to our team first. The team prepares a neutral reply draft. Then the client gets one decision card.
- **Quarterly:** re-check the market leader and the goal. The leader can grow.

Proposed German client labels (no tool names): "Google-Bewertungen", "Neu in den letzten 30 Tagen", "Ziel 2026", "Nötiges Tempo pro Monat", "Abstand zum Marktführer", "Beantwortet".

## 3. Data source

- **Own profile:** GBP API v4 reviews endpoint (S01–S03). Apply for API access now. Approval can take 10+ business days (S06). Until approval, the team reads the numbers by hand once per month.
- **Competitors:** a third-party business-data API, monthly (S11). Do not use the Places API for history. Its terms forbid storage (S08, S30).
- **Detailed analysis:** the paid review analysis with 3 competitors, once per quarter, only when a client needs it (S13).

## 4. Guardrails

**All clients (Google policy, S07):**
- Ask every customer the same way. No filter step that sends only happy customers to Google.
- No gifts, discounts or rewards for a review.
- No pressure on the premises. No request for specific words or staff names.
- The 2× goal is a business goal. Never turn it into a review quota per staff member.

**Law firms (STÜRZL; S21–S26):**
- Ask in person or with a QR card at the end of the mandate. E-mail only with prior documented consent.
- Replies never confirm the mandate and never name case facts.
- Client reviews on the firm website only with express consent of that client (§ 6 Abs. 2 BORA).

**Health practices (S27–S29):**
- QR card at reception for all patients. E-mail or SMS only with explicit consent.
- Replies never confirm treatment, diagnosis or dates.
- Do not re-use reviews with healing claims in ads or on the website.

## 5. Decision questions for Martin

**Q1 — Data source for the client's own reviews**
1. GBP API, apply for access now, manual monthly count until approval (Recommended)
2. Third-party business-data API also for own profile (no review texts, no reply data)
3. Manual monthly count only

**Q2 — Data source for competitor numbers**
1. Third-party business-data API, monthly snapshot of top 3 (Recommended)
2. Paid review analysis with 3 competitors, quarterly only
3. All-in-one review tool per client (about $65 per month per location)

**Q3 — How to show the 2× goal to the client**
1. Show goal, progress bar and pace per month, framed as a practice/firm goal (Recommended)
2. Show only the interim milestone "overtake the market leader"
3. Keep the goal internal, show only count and trend

**Q4 — Alerts for critical reviews (1–3 stars)**
1. To our team within 24 h, team drafts a reply, client gets a decision card (Recommended)
2. Direct alert to the client, no draft
3. No alert, only in the monthly report

## 6. Martin's decisions (13.10.2026, grill chat)
- Q1: Google Business Profile API for the client's own reviews; apply for access now; manual monthly count until approval.
- Q2: monthly snapshot of the top 3 competitors from a third-party business-data service (check its storage terms first).
- Q3: client sees goal, progress bar and pace per month, framed as the practice/firm goal (never a staff quota).
- Q4: 1–3 star review → our team within 24 h, team drafts a neutral reply, client gets one decision card.
Next: Martin applies for the API access (Google form, his account); then build the portal tile + report section (needs its own go).
