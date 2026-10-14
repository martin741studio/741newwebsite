# 2.5 Degrees of freedom per step (rule R1.7) — booking-sequence

| Step | Fragile? | Freedom | Form |
|---|---|---|---|
| Parse booking | medium | MEDIUM | Claude reads screenshot/text → `booking.json` (schema fixed in SKILL.md) |
| Time-zone maths, send times, fireAt, skip flags | yes (DST, day names) | LOW | `scripts/tz_times.py` |
| Find prospect + baseline | yes (old/new folder layouts) | LOW | `scripts/find_prospect.py` |
| Free site check | yes (same facts each time) | LOW | `scripts/quick_check.py` |
| Paid checks | medium (cost) | LOW–MEDIUM | `dfs.py` only, booking dir as ledger, cap 0,30; endpoint menu in references |
| Pick the NEW insight | no, many valid | HIGH | heuristic priority list in references/insight-menu.md |
| Pick the case | medium (facts only) | MEDIUM | branch match rule; text only from case-library.json |
| Write messages | medium (voice) | MEDIUM | template + Korinna example in references/message-templates.md |
| Rule + slop check | yes | LOW | `scripts/check_sequence.py` (wraps deslop_de.py) |
| Reminders | yes | LOW | fixed prompt template `assets/reminder-prompt.md`, values from tz_times.py |
