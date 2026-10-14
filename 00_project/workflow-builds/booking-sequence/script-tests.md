# 3.5 Script tests (verification step) — 2026-10-14

SKILL.md ends with '## Verification': check_sequence PASS + file times = booking.json + list_scheduled_tasks fireAt = booking.json; 'fix and run again, do not report done before all three pass'.

## tz_times.py — Korinna (DST switch 25.10.)
```
call Mo 26.10.2026, 16:30 WITA = Montag, den 26.10. um 9:30 Uhr CET
m2 2026-10-25T16:30:00+08:00 False
m3 2026-10-26T16:00:00+08:00 False
['daylight saving change in the prospect zone within 2 days before the call: times computed with zoneinfo']
```
## tz_times.py — late booking (22 h ahead)
```
m2 skip True late booking: merge message 2 into message 1
m3 2026-10-22T15:30:00+08:00 False
```
## find_prospect.py
```
{'status': 'OK', 'slug': 'korinna-heintze', 'website': 'https://korinnaheintze.de/', 'health': False, 'health_reason': 'no health word in title/company', 'reason': None}
{'status': 'OK', 'slug': 'sabine-schwarz', 'website': 'https://www.therapie-sasch.com/', 'health': True, 'health_reason': 'branch=health', 'reason': None}
{'status': 'OK', 'slug': 'catja-grieshaber-v2', 'website': 'https://www.praxis-naschmarkt.at/Home/', 'health': True, 'health_reason': 'guess from title/company: "Praxis"', 'reason': None}
{'status': 'ASK MARTIN', 'slug': None, 'website': None, 'health': None, 'health_reason': None, 'reason': 'no match'}
```
## check_sequence.py — Korinna (clean)
```
check_sequence korinna-heintze: m1 slop 5/5 · m2 slop 5/5 · m3 slop 5/5
  note: case: Maria Abel
  warning: daylight saving change in the prospect zone within 2 days before the call: times computed with zoneinfo
RESULT: PASS
```
## check_sequence.py — negative test (Korinna copy with planted errors, run 14.10. 14:39)
```
check_sequence zz-test-neg: m1 slop 4/5 · m2 slop 5/5 · m3 slop 5/5
  FAIL m1: last line must be "Martin"
  FAIL m1: booking link: "cal.com"
  FAIL m1: booking link: "/30min"
  FAIL m1: tool name: "dataforseo"
  FAIL m1: "unclaimed" claim: "unclaimed"
  FAIL m1: promise word: "garantier"
  FAIL m1: formal address "Sie" (use du)
  FAIL m1: link without https://: www.cal.com/741-studio-simjzw/30min
  FAIL m1: number 741 has no claim in claims.json
  FAIL m1: number 300 has no claim in claims.json
  FAIL m1: time 10:30 != call time 9:30 (prospect zone)
  FAIL m1: video link https://www.youtube.com/watch?v=dQ9OE8GSolw missing
  FAIL m1: call time 9:30 (prospect zone) missing
  FAIL m3: meeting link 'https://meet.google.com/nem-kxsy-ots' missing
  FAIL m3: "Handy" missing (Laptop/PC, nicht am Handy, Bildschirm teilen)
  FAIL m1: slop 4/5: invented proof: "300 kunden" ohne Beleg in der Claim-Liste
RESULT: FAIL (16)
```
All 16 planted errors caught. Test folder removed after the run.

## Update 2026-10-14 (new timing D7/D8): tz_times.py cases
```
A Korinna (normal) | call Montag, den 26.10. um 9:30 Uhr CET
   m1 slot  So 25.10.2026, 16:30 WITA = 9:30
   m2 slot  Mo 26.10.2026, 15:00 WITA = 8:00
   m3 slot  Mo 26.10.2026, 16:00 WITA = 9:00
B call 8:30 her time | call Donnerstag, den 22.10. um 8:30 Uhr CEST
   m1 slot  Mi 21.10.2026, 14:30 WITA = 8:30
   m2 merged m3 Do 22.10.2026, 14:00 WITA = 8:00
   m3 slot  Do 22.10.2026, 14:00 WITA = 8:00
C booked 20 h ahead | call Donnerstag, den 22.10. um 15:00 Uhr CEST
   m1 now  Mi 21.10.2026, 21:00 WITA = 15:00
   m2 slot  Do 22.10.2026, 14:00 WITA = 8:00
   m3 slot  Do 22.10.2026, 20:30 WITA = 14:30
D booked on the call day | call Donnerstag, den 22.10. um 15:00 Uhr CEST
   m1 now  Mi 21.10.2026, 21:00 WITA = 15:00
   m2 merged m1 Do 22.10.2026, 14:00 WITA = 8:00
   m3 slot  Do 22.10.2026, 20:30 WITA = 14:30
E booked 20 min ahead | call Donnerstag, den 22.10. um 15:00 Uhr CEST
   m1 merged m3 Mi 21.10.2026, 21:00 WITA = 15:00
   m2 merged m3 Do 22.10.2026, 14:00 WITA = 8:00
   m3 now  Do 22.10.2026, 20:30 WITA = 14:30
```

## check_sequence.py merge test (2026-10-14, temp copy of Korinna, call 8:30 her time → M2 into M3)
```
with story in M3:     m1 slop 5/5 · m3 slop 5/5 · m2 merged into m3 · note: case: Maria Abel · RESULT: PASS
story removed (M3 still has the word "Menge"):  FAIL m3: no success story with a name from case-library.json (m2 content) · RESULT: FAIL (1)
```
Found and fixed in this test: the case-name match used the last word only ("Menge" = Torsten Menge); now full name or the last 2 words with word boundaries.
