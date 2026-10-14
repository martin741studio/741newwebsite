# 5.4 Scheduled run once by hand and read — reminder tasks (2026-10-14)

Two dry-run reminders built from `assets/reminder-prompt.md` (Sabine dry-run file `prospects/sabine-schwarz/booking-dryrun-2026-10-14/whatsapp-sequence.md`), then opened and read (rule R6.10).

| Test | How it ran | Session | Result (read in the run transcript) |
|---|---|---|---|
| On time (M3, call start = now + 33 min) | one-time `fireAt` 14:50 WITA, fired by the scheduler at 14:50:52 | local_0e602b0a-f16a-48a6-9b70-a660b5221aad | `date -u` → before the call; read section "## 3 · 30 Minuten vorher"; showed the ```text block + number + call line; PushNotification called (not delivered because the terminal was active: expected app behaviour). Nothing sent. **PASS** |
| Too late (M2, call start = now − 10 min) | "Run now" (run_scheduled_task) 14:47 WITA | local_c2b365d2-ad5e-4a6a-ba40-c76ecde4422f | `date -u` → after the call start → replied only "Zu spät: Nachricht 2 an Sabine Schwarz (TROCKENLAUF) nicht mehr senden" + "The laptop was probably asleep at the send time." No message shown. **PASS** |

Side note: Martin saw the late-test run in the sidebar and asked in it why Sabine got routines; the run explained it was a test. Lesson for future tests: put "TROCKENLAUF" at the start of the title (done) and tell Martin before a live reminder test.
Both test tasks were deleted after the runs; their folders were removed.

Template change after this test (D7–D9): 3 reminders, a WhatsApp-Link line in step 7, a free site re-check in the M1 reminder. The guard logic (steps 1–3) is unchanged, so the late/on-time results still hold. The M1 re-check command was run by hand: `quick_check.py korinna-heintze --recheck` → "NO CHANGE since 2026-10-14".
