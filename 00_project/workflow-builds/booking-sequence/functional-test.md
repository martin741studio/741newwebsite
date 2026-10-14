# 4.2 Functional test — booking-sequence (fresh agent "Claude B", 2026-10-14 14:41:46–14:44:25 WITA)

Task: test scenario T1, dry-run booking for Sabine Schwarz (real review page `sabine-schwarz`, health, Coburg). Booking: Do 22.10.2026 16:00 WITA, Meet https://meet.google.com/abc-defg-hij, phone +4915112345678 (test). Mode Trockenlauf.

Result (agent report):
- Skill loaded, all 8 steps run in order, ~28 tool calls, ~3 minutes, 155 k tokens.
- find_prospect.py → 1 match, no card needed. tz_times.py → 10:00 CEST (before the 25.10. switch), m2 Mi 21.10. 16:00 WITA, m3 Do 22.10. 15:30 WITA.
- 3 paid calls, 0,106 USD (volumes 0,09 + 2 × SERP 0,008), all task status 20000.
- check_sequence.py: 2 × FAIL (m1 slop 4/5: "nicht nur …, sondern"; even sentence lengths) → rewrite → **RESULT: PASS** (m1/m2/m3 slop 5/5). Feedback loop worked as designed.
- Reminders: both created as `-dryrun`, verified with list_scheduled_tasks (fireAt 2026-10-21T08:00Z, 2026-10-22T07:30Z = booking.json), then deleted. Nothing sent.
- Output kept as evidence: `00_project/prospects/sabine-schwarz/booking-dryrun-2026-10-14/` (whatsapp-sequence.md, picks.md, claims.json, m1–m3, _run.json = Trockenlauf).

Gaps found by Claude B → fixes made the same day:
| # | Gap | Fix |
|---|---|---|
| 1 | Step 1/2 order unclear (find runs before booking.json) | SKILL.md: step 1 = find_prospect.py, step 2 = booking.json + tz_times.py |
| 2 | "health" vs case branches "gesundheit/heilpraktiker/psychotherapie" | insight-menu §4 branch map |
| 3 | No template for "no site change" | insight-menu §1 + message-templates: one real strength (quoted), then the new finding |
| 4 | baseline.md cut the page text at 12 000 chars | find_prospect.py: 60 000 chars |
| 5 | SERP location national for a local term ("Platz 7" for heilpraktiker coburg was measured for all of DE) | insight-menu §3: local term → `location_name` of her town, and say where it was measured. The dry-run m2 "Platz 7" claim would need a re-measure from Coburg (kept only as test evidence) |
| 6 | Success story already on the review page | insight-menu §4: prefer a case not on the page / not in the Loom; else one fact the page did not show; never a fact the library marks unclear |
| 7 | claims.json path convention unclear | SKILL.md step 5: booking/evidence/… vs evidence/… vs case-library path |
| 8 | Facts without numbers are not checked | check_sequence.py: claim `"quote"` must occur in the source; every claim needs numbers or a quote; quick_check.py saves `booking/evidence/home.html`; step 3 saves other pages as `page-<name>.html` |
| 9 | list_scheduled_tasks shows UTC, booking.json +08:00 | reminders.py prints `fireAt_utc`; SKILL step 7 + Verification compare with it |
| 10 | Korinna task ids not one pattern | Korinna m2 task re-created as `korinna-heintze-whatsapp-2-24h` |
| 11 | Booking phone ≠ site phone | SKILL step 2: the booking phone is the WhatsApp number |

Re-check after fixes: `check_sequence.py korinna-heintze` → RESULT: PASS; tz_times night test (05:00 WITA = 23:00 CEST) → `m1_send_now_ok: false` + warning.

---

# 4.2b Functional test 2 — new timing D7/D8 (fresh agent, 2026-10-14 16:24:47–16:27:54 WITA)

Task: dry-run booking Manuela Stetter (real review page, health), call Mo 2.11.2026 16:00 WITA = **9:00 CET** → exercises the merge rule (call before 09:30 her time → M2 into M3) and the DST switch between booking and call.

Result:
- tz_times.py: M1 slot So 1.11. 16:00 WITA (9:00 CET); M2 merged into M3; M3 slot Mo 2.11. 15:30 WITA (8:30 CET). Correct.
- 2 paid calls, 0,098 USD. Check: 1 × FAIL (m3 slop 4/5, " - " dash) → rewrite → **RESULT: PASS** (`m1 slop 5/5 · m3 slop 5/5 · m2 merged into m3`).
- M1: strength (free Hormon-Selbsttest) + new term "Östrogendominanz" 9.900/month, not in the top results, 5 % = 495 + video. M3: link + M2 content (Wechseljahre terms 140 + 70, course without own page) + Schlirf story + laptop tip.
- reminders.py → 2 tasks (M2 not scheduled, merged). Created as -dryrun, list_scheduled_tasks matched fireAt_utc (2026-11-01T08:00Z, 2026-11-02T07:30Z), deleted one by one, folders removed. Output moved to `prospects/manuela-stetter/booking-dryrun-2026-10-14b/` (Trockenlauf). Nothing sent. ~27 tool calls, 175 k tokens.

Findings → fixes (same day):
| # | Finding | Fix |
|---|---|---|
| 1 | Title "change" was scrape noise ("Chevron up") | quick_check.py: normalized compare, containment = no change |
| 2 | No DST warning although the switch lies between booking and call | tz_times.py: warns on any offset change between now and the call |
| 3 | All fitting cases already on her page | rule allows reuse of the best fit (kept); never unclear facts |
| 4 | loom-transcript.md missing, only loom-script.md | insight-menu: transcript, else loom-script.md |
| 5 | home.html path pointed to the review run | insight-menu: `booking/evidence/home.html` |
| 6 | baseline.md mixes internal notes with what she saw | insight-menu: "new" = not in "Visible review-page text" and not in the video text |
| 7 | Korinna example paths vs SKILL path rule | message-templates: Korinna was the hand-run, skill runs use booking/evidence/ |
| 8 | No claim type for "X is missing" | check_sequence.py: `"absent"` (must NOT occur in the source); tested true/false |
| 9 | HTML entity broke a quote | check_sequence.py: quotes compared against html-unescaped source |
| 10 | reminders.py JSON key not named in SKILL | SKILL step 7 names `{"create", "not_scheduled"}` |
| 11 | Reminders read a fixed path | SKILL step 7: never move/rename the sequence file or booking folder after the reminders are set |
| 12 | HWG and symptom search terms | insight-menu: name terms neutrally, no promise to treat, no serious-disease terms |

Re-check after fixes: Korinna check PASS; absent/quote test (true absent passes, false absent fails, entity quote passes).
