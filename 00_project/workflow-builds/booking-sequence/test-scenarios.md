# 2.2 Test scenarios — booking-sequence (written 2026-10-14, BEFORE the skill body)

Pass = the skill loads for T1 and T2, and does NOT trigger for T3 and T4.

## T1 — obvious trigger (cal.com paste)
Prompt: "Neue Buchung: A new event has been scheduled. What: 30 min meeting between 741 Studio and Sabine. When: Thursday, October 22, 2026 4:00pm - 4:30pm (Asia/Makassar). Who: Sabine Schwarz, sabine@example.de. Where: Google Meet https://meet.google.com/abc-defg-hij. Phone number +4915112345678"
Expected:
- `booking-sequence` loads. Finds `sabine-schwarz` (review page + prospect folder).
- Converts 16:00 WITA → 10:00 Uhr DE (CEST, before the 25.10. switch). m2 reminder 21.10. 16:00 WITA, m3 reminder 22.10. 15:30 WITA.
- One fresh free site check + ≤ 3 paid calls, ledger in `prospects/sabine-schwarz/booking/`, total ≤ 0,30 USD.
- 3 German "du" messages in Ich-Form, each 5/5, `check_sequence.py` passes; m1 has the YouTube link and a volume example labelled as example; m2 a case from case-library.json; m3 the Meet link + Laptop/PC hint. No cal.com link, no tool names, no "unclaimed", HWG-safe (she is a health prospect).
- 2 reminder tasks created; nothing sent.

## T2 — paraphrase (German, no "cal.com", no "Sequenz")
Prompt: "Manuela Stetter hat über die Analyse-Seite einen Termin gebucht, Montag 2.11. um 17 Uhr Bali-Zeit, WhatsApp +49 171 0000000. Bereite die Nachrichten für sie vor."
Expected: `booking-sequence` loads; 17:00 WITA → 10:00 Uhr DE (CET after 25.10.); same outputs as T1. Asks for the Meet link only as a card if it is missing (m3 needs it), or writes m3 with a placeholder the check flags.

## T3 — must NOT trigger (review-page final message)
Prompt: "Hier ist der Loom für Manuela Stetter: https://www.loom.com/share/xyz – mach die WhatsApp-Nachricht dazu."
Expected: `booking-sequence` does NOT load. `local-seo-review-page` step 13 handles it (Loom transcript + email ask).

## T4 — must NOT trigger (call prep / new review page)
Prompt: "Mach mir eine Review-Page für Physiopraxis Müller in Ulm, hier ist die Website."
Expected: `booking-sequence` does NOT load; `local-seo-review-page` does.

## T5 — functional (used in 4.2): late booking
Input: booking made today for tomorrow 09:00 WITA. Expected: `tz_times.py` flags m2 skip, m1 carries both insights + the story, only the m3 reminder is created (or none if past).
