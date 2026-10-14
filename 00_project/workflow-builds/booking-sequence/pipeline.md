# 2.4 Pipeline — booking-sequence (2026-10-14)

Shape: patterns.md 4.1 sequential with gates + 4.3 iterative refinement (check → fix → re-check).

```
Martin pastes cal.com booking
   │
   ▼
S1 INTAKE ── booking.json (name, email, phone, start + zone as shown, meet link)
   │         tz_times.py → WITA + prospect zone, m2 = −24 h, m3 = −30 min, fireAt, skip flags
   ▼
S2 FIND ──── find_prospect.py <name> → slug, review URL, website, baseline (prospect.json | page text)
   │         ◆ CARD only if 0 or >1 match
   ▼
S3 FRESH CHECK ── quick_check.py <website> (free) → booking/site-check.json
   │              dfs.py <prospects/slug/booking> … (≤ 3 calls, cap 0,30 USD) → SERP / volumes
   ▼
S4 PICK ─── 2 NEW insights (diff vs. baseline), 1 volume chance, 1 case (branch match, facts only)
   ▼
S5 WRITE ── m1.txt, m2.txt, m3.txt + claims.json (every number with its source file)
   ▼
S6 CHECK ── check_sequence.py <slug> → rules + slop 5/5 per message
   │         └─ fail → rewrite the flagged message → re-run (loop until PASS)
   │         PASS → writes whatsapp-sequence.md + booking/_run.json
   ▼
S7 REMIND ─ 2 one-time scheduled tasks from assets/reminder-prompt.md (never send; late guard)
   │         verify with list_scheduled_tasks (fireAt matches tz_times output)
   ▼
S8 SHOW ─── Martin: 3 ```text blocks, WhatsApp number, times (WITA + DE), cost, reminder ids
            ◆ Martin sends message 1 himself (no send by Claude)
```

## Martin checkpoints (◆)
| # | When | What |
|---|---|---|
| CP1 | after design | this pipeline, use cases, tests |
| S2 card | prospect not found / ambiguous | which page, or no-page variant |
| S8 | end | he reads and sends m1 himself; reminders fire later |
| CP2 | after tests | scorecard + one real output |

## Hard limits
Never send WhatsApp, email or LinkedIn. No booking link (cal.com/Calendly) in messages. No tool names. No "unclaimed"/"nicht beansprucht". HWG for health. No promise: volumes as an example. Paid calls only via dfs.py, cap 0,30 USD per booking.

## Update 2026-10-14 (D7–D9): new timing
```
S1 FIND → S2 BOOKING + tz_times.py (mode per message: slot | now | merged) → S3 FRESH CHECK → S4 PICK → S5 WRITE
→ S6 CHECK (loop) → --write: whatsapp-sequence.md with a wa.me link per message
→ S7 REMIND: reminders.py → up to 3 one-time tasks
      M1  call − 24 h      (+ free site re-check, warns on change)
      M2  08:00 her time   (merged into M3 if the call is before 09:30)
      M3  call − 30 min
→ S8 SHOW: "now" messages = Your-click card; rest = schedule table
```
Nothing goes out right after the booking (Martin 14.10.). Claude never sends.
