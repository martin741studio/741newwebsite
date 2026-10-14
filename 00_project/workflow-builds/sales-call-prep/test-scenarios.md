# Test scenarios (step 2.2) — written before the skill body

## Scenario 1 — obvious trigger
Input: "Bereite mich auf den Call mit Korinna Heintze vor, der ist am 26.10."
Expected: skill loads, finds `00_project/prospects/korinna-heintze/`, produces a one-page
call-prep brief (goal question, gap with sources, 1 proof case + 1 reserve case, package
recommendation with premium-first order, 2-4 ranked objections, call structure, a "nicht
vergessen" section with the call link), runs the deslop/claims check, reports the score, and
never names an outside methodology source anywhere in the output.

## Scenario 2 — paraphrase
Input: "Ich hab in 20 Minuten den Call mit Korinna, gib mir schnell die wichtigsten Punkte."
Expected: same skill loads despite no literal "prep"/"Vorbereitung" wording and no explicit
date. It should recognise "Call mit <Name>" + urgency as the trigger, still read the booking
folder if it exists, and may shorten the brief (skip the reserve case) given the 20-minute
window, but must still run the claims check before showing it — "schnell" is not a reason to
skip verification.

## Scenario 3 — must NOT trigger
Input: "Schick Korinna nochmal eine Erinnerung vor dem Call." / "Schreib die WhatsApp-Nachricht
für morgen an Korinna."
Expected: this is booking-sequence's job (message TO the prospect), not sales-call-prep. The
skill must NOT load/run, or if invoked by name directly must say so and point at
booking-sequence instead of producing a prospect-facing message itself. Negative-trigger
wording in the frontmatter description must cover this explicitly ("Do NOT use to write or
send a message to the prospect — see booking-sequence").

## Decision from these scenarios
Scenario 3 means the frontmatter needs both a positive trigger set ("prep me for the call
with X", "Anrufvorbereitung für X", "Call mit X vorbereiten") and an explicit negative
trigger naming booking-sequence by task (not by name, since Martin may not remember the
skill's name) — "sending/writing a message to the prospect".
