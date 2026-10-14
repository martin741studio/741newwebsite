# Message templates and the reference example (booking-sequence)

Rules for all 3 messages: German, "du", Ich-Form as Martin, WhatsApp plain text (no bold, no bullets, short paragraphs), sign-off line "Martin". Times always in HER zone (`times.call.prospect_time`), never Bali time. Links with https://. No booking link, no tool names, no "unclaimed", no "Prozess/Workflow" framing. `check_sequence.py` enforces these.

Timing (Martin 14.10.): nothing goes out right after the booking. M1 = 24 h before, M2 = 08:00 her time on the call day, M3 = 30 min before.

## Shape
- **M1 (24 h before):** "morgen um <Zeit> Uhr ist unser Gespräch, ich freue mich!" → "Ich habe mir deine Seite seit meiner Analyse noch einmal angesehen" → insight 1 (change + what is still open, or one real strength when nothing changed) → search demand + the 5 % example → the video line + link `https://www.youtube.com/watch?v=dQ9OE8GSolw` → "Bis morgen" + "Martin".
- **M2 (08:00 on the call day):** "Guten Morgen <Name>, heute um <Zeit> Uhr ist es so weit" → "Ich habe noch etwas für dich nachgeschaut" + insight 2 → success story (facts only) + "Oft sind es nur wenige Punkte." → "Bis später" + "Martin".
- **M3 (30 min before):** "in einer halben Stunde, um <Zeit> Uhr, geht es los. Hier ist der Link:" + meeting link → tip: Laptop oder PC, nicht am Handy, ich teile meinen Bildschirm → "Bis gleich" + "Martin".

## Merge variants (from `times.mX.mode` / `merged_into`)
- **Call before 09:30 her time → M2 into M3:** M3 = "in einer halben Stunde … Link" + "Vorher noch kurz: …" insight 2 + story + the laptop tip. No m2.txt.
- **Booking on the call day → M2 into M1 (M1 is "now"):** M1 = thanks for the booking + "heute um <Zeit> Uhr" + insight 1 + 5 % + video + insight 2 + story. No m2.txt.
- **Call in less than 35 min → all into M3:** one message: thanks + link + laptop tip + insight 1 + 5 % + video + the story in one sentence.
- **M1 is "now" (booking less than 24 h ahead):** start with "danke dir für die Buchung!" and the call day/time ("morgen um …").

## Reference example: Korinna Heintze (call Mo 26.10.2026 9:30 Uhr CET; all 5/5, check PASS)

M1 (So 25.10., 9:30 Uhr her time):
```text
Hallo Korinna, morgen um 9:30 Uhr ist unser Gespräch, ich freue mich!

Ich habe mir deine Seite seit meiner Analyse noch einmal angesehen. Schön: Titel und Beschreibung passen jetzt zu deinem Executive Sparring und nennen Erfurt und Leipzig. Der falsche Verweis auf feingold.de ist weg.

Eine Sache ist geblieben: Google sieht im Quelltext deiner Startseite nur 9 Wörter, der Rest lädt erst später. Bei „Führungskräfte-Coaching“ stehst du deshalb nicht unter den ersten 50 Treffern, obwohl danach rund 2.900 Mal im Monat gesucht wird. Schon 5 Prozent dieser Suchen wären rund 145 Besucher im Monat, mit eigenen Seiten für deine Formate ist das realistisch.

Wenn du vorher sehen magst, wie ich arbeite, hier mein ganzer Ablauf in einem Video:
https://www.youtube.com/watch?v=dQ9OE8GSolw

Bis morgen
Martin
```

M2 (Mo 26.10., 8:00 Uhr her time):
```text
Guten Morgen Korinna, heute um 9:30 Uhr ist es so weit, ich freue mich!

Ich habe noch etwas für dich nachgeschaut: In Leipzig wird rund 70 Mal im Monat nach „Business Coach Leipzig“ gesucht, dazu rund 30 Mal nach „Führungskräfte-Coaching Leipzig“. Dort ist der Wettbewerb deutlich kleiner als bundesweit, eine eigene Seite für Leipzig kann dich dort schneller nach vorn bringen.

Ein Beispiel aus meiner Arbeit: Maria Abel, Familienberatung bei Stuttgart, war bei Google kaum zu finden. Mit klaren Überschriften, den richtigen Suchbegriffen und einer schnelleren Website stand sie nach 8 Wochen im ganzen Gebiet unter den ersten drei. Oft sind es nur wenige Punkte.

Bis später
Martin
```

M3 (Mo 26.10., 9:00 Uhr her time):
```text
Hallo Korinna, in einer halben Stunde, um 9:30 Uhr, geht es los. Hier ist der Link:
https://meet.google.com/nem-kxsy-ots

Ein kleiner Tipp: Nimm das Gespräch am besten am Laptop oder PC, nicht am Handy. Ich teile meinen Bildschirm und zeige dir einiges, das auf einem großen Bildschirm viel besser zu sehen ist.

Bis gleich
Martin
```

claims.json for this example: `00_project/prospects/korinna-heintze/booking/claims.json` (numbers + quotes). Korinna was the hand-run: her paid files sit in `evidence/`. In a skill run, paid files from the booking sit in `booking/evidence/`.
