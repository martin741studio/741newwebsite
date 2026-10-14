# 2.1 Use cases — booking-sequence (2026-10-14)

## UC1 — New booking from a review page (main case)
- **Trigger:** Martin pastes a cal.com booking (screenshot or text: name, email, phone/WhatsApp, "When … (Asia/Makassar)", Google Meet link), often with "neue Buchung", "hat einen Call gebucht", "mach die WhatsApp-Sequenz".
- **Steps:** (1) parse the booking into `prospects/<slug>/booking/booking.json`; (2) `tz_times.py` → call time in WITA + prospect zone, send times (m2 = −24 h, m3 = −30 min), fireAt values, late-booking flags; (3) `find_prospect.py` → slug, review URL, website, baseline (old findings) from `prospect.json` or the old page text; (4) fresh check: `quick_check.py` on the website (free) + max 2–3 DataForSEO calls via `dfs.py` with the booking folder as ledger (cap 0,30 USD); (5) pick 2 NEW insights (one for m1, one for m2) + one volume opportunity + one case from `case-library.json`; (6) write m1/m2/m3 + `claims.json`; (7) `check_sequence.py` → rule check + slop 5/5 per message, fix until it passes, then it writes `whatsapp-sequence.md` + `_run.json`; (8) create 2 one-time reminder tasks from `assets/reminder-prompt.md`; (9) show Martin the 3 messages in ```text blocks + the WhatsApp number.
- **Tools:** Read/Bash, dfs.py, deslop_de.py, scheduled-tasks MCP.
- **Result:** `prospects/<slug>/whatsapp-sequence.md`, booking evidence, 2 armed reminders, message 1 ready to send now.

## UC2 — Late booking (call in less than ~26 h) or booking without a review page
- **Trigger:** same paste, but the call is soon, or `find_prospect.py` finds no page.
- **Steps:** late: `tz_times.py` flags `m2_skip` → m2's insight + story go into m1 (one longer m1), only the m3 reminder is set; if even m3's time has passed, no reminders. No page: card to Martin (which prospect / skip the "seit meiner Analyse" line); write the sequence from the fresh check only.
- **Result:** a sequence that never schedules a reminder in the past.

## UC3 — Call moved or cancelled
- **Trigger:** "Korinna hat verschoben auf …", a cal.com "rescheduled"/"cancelled" mail pasted.
- **Steps:** re-run `tz_times.py` with the new time, update `booking.json`, rewrite only the time lines in m1–m3 (or a short "neuer Termin" note), re-run the check, `update_scheduled_task` (new fireAt + prompt) for both reminders; cancelled → disable both tasks (`enabled: false`) and mark `_run.json` note "abgesagt".
- **Result:** reminders match the real call time; nothing fires for a dead call.

## Update 2026-10-14 (D7–D9, after checkpoint 1)
Timing changed by Martin: nothing goes out right after the booking. M1 = 24 h before (insight + 5 % + video), M2 = 08:00 her time on the call day (insight + story), M3 = 30 min before. UC2 is now "short-notice booking": a past slot = "send now"; call before 09:30 her time → M2 into M3; booking on the call day → M2 into M1; call in < 35 min → all into M3. Each message gets a wa.me link and (when it has a slot) a reminder; the M1 reminder re-checks the site for free.
