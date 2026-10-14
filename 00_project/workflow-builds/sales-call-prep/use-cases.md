# Use cases (step 2.1)

## UC1 — Martin asks for prep on a specific booked call
Trigger: "prep me for the call with Korinna" / "Anrufvorbereitung für Korinna" / "call prep Korinna".
Steps: find her booking folder (reuse `find_prospect.py` pattern from booking-sequence) → read
booking.json + baseline.md + claims.json + m1-m3 (if present) → pick 1 new, not-yet-shown gap
+ reuse what she already saw → pick 1 proof case + 1 reserve case → recommend a package
(house pricing memory, premium-first order) → pick 2-4 likely objections from
`sales-einwandbehandlung.md`, ranked for her profile, not a generic top-11 list → write the
one-pager → run the deslop/claims check → show Martin.
Tools: Read/Bash (grep, file reads), the deslop_de.py checker with `--claims`.
Result: `00_project/prospects/<slug>/call-prep.md`, shown to Martin in chat before the call,
STE where it is Martin-facing prose, German where the brief itself is in German (matches the
language of the booking record).

## UC2 — Martin says a call is booked and wants prep right away (chained)
Trigger: Martin pastes a cal.com booking text, same input booking-sequence takes, but says
"und bereite mich gleich auf den Call vor" / "prep me too". booking-sequence runs first
(unchanged) and writes `booking/booking.json` + `baseline.md`; sales-call-prep then runs as
its own step, reading that same folder. Steps/Tools as UC1. Result: both the WhatsApp sequence
AND the call-prep brief exist, from one Martin instruction. They are never the same skill run:
booking-sequence has its own gates (check_sequence.py, reminders) and must not be blocked by
call-prep, and call-prep must not block or alter the WhatsApp sequence.

## UC3 — No review-page/booking history exists for this prospect (thin case)
Trigger: Martin names a prospect for an upcoming call that did NOT come through the normal
review-page -> booking-sequence pipeline (e.g. a warm intro, a referral call, a call booked
directly on LinkedIn). Steps: no `baseline.md`/`claims.json` to reuse — do a small fresh look
(prospect's own website + LinkedIn profile if reachable) instead of inventing a review-page
history, skip the "already shown her X" section entirely, keep everything else (goal
question, package recommendation, objection picks, call structure). Tools: same, plus a
website fetch. Result: a shorter one-pager that is honest about having less prior history
with this prospect — never pretends a review page exists when it does not.

## Must-not-trigger (see 2.2 scenario C)
A request to run or write WhatsApp reminder messages for a booked call is booking-sequence's
job, not this skill's — even though both read the same booking folder.
