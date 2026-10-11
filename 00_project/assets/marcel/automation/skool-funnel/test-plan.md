# Test plan: Marcel Rosenbach · Skool funnel (Trockenlauf: template copied, cases from spec section 9; fill in P4)

flow_class: <messages | crm | internal> · TEST marker: `TEST-741` · test inbox: <test…@741.studio>

Rules: one row per case. Each case names its input, the expected result in EVERY target system, how it is read back, and the evidence file. Run the cases in order. Max 3 fix attempts per case.

| ID | Type | Input (TEST data) | Expected result per system | Readback (API call or page + field) | Evidence file |
|---|---|---|---|---|---|
| T1 | e2e | TEST-741 record with all fields filled | <system A: contact with fields x,y,z · system B: deal in stage S, linked to person> | <calls / pages> | `evidence/T1-*.png`, `evidence/T1-readback.json` |
| T2 | error | required field empty | <clear error in task history, alert mail, no half record> | | |
| T3 | error | bad format (phone with letters, date as text) | | | |
| T4 | error | auth expired (disconnect test connection, if safe) | <alert "unreadable"> | | |
| T5 | idempotency | same TEST record triggered twice | <one contact, one deal, tag once, one mail> | | |
| T6 | alert | force one failure | <alert mail from alerts@741.studio reaches martin@741.studio within X min> | | |
| T7 | role (Supabase only) | anon / client / admin call | <anon 401, client sees own rows only> | | |

After the run: write `test-report.json` (see `test-report.example.json`), then start the verifier subagent.
