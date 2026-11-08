---
name: booking-sequence
description: Prepares the 741 booking sequence after a prospect books a call. Finds the review page, runs a fresh check for something NEW, writes 3 German WhatsApp messages in Martin's voice, converts the call time to her time zone, sets reminders. Never sends. Trigger on a pasted cal.com booking ("A new event has been scheduled"), "neue Buchung", "hat einen Call gebucht", "WhatsApp-Sequenz für <Name>", or a moved or cancelled call.
---

# Booking sequence (WhatsApp after a call booking)

## Critical

- **Never send anything.** No WhatsApp, email or LinkedIn message. Martin sends every message himself. The reminders only show him the ready text and its wa.me link.
- **Timing (Martin 14.10.):** nothing goes out right after the booking. M1 = 24 h before the call (new insight + 5 % example + video), M2 = 08:00 her time on the call day (insight + success story), M3 = 30 min before (link + laptop tip). Merges and "send now" cases come only from `tz_times.py`.
- **Something NEW, real data only.** M1 and M2 each carry one insight that is not on the review page, backed by an evidence file in `claims.json`. Traffic numbers are an example ("wären rund"), never a promise. No "unclaimed". No tool names. HWG for health prospects.
- **Deliver only on `RESULT: PASS`** from `scripts/check_sequence.py <slug>` (hard rules + slop 5/5 per message). Times come only from `scripts/tz_times.py`.

## Inputs

From the booking (cal.com screenshot or text): name, email, phone (= WhatsApp), call start + zone as shown (cal.com shows Asia/Makassar = Bali, WITA, UTC+8), meeting link. A missing meeting link: write m3 once Martin gives it (card).

## Workflow

Paths relative to `/Users/martindrendel/741website`. `S=.claude/skills/booking-sequence/scripts`.

```
- [ ] 1 find_prospect.py (card if 0 or >1 match)
- [ ] 2 booking.json + tz_times.py
- [ ] 3 quick_check.py + max 3 paid calls (cap 0,30 USD)
- [ ] 4 two NEW insights + traffic example + case picked
- [ ] 5 m1/m2/m3 + claims.json written
- [ ] 6 check_sequence.py → PASS (loop) → --write
- [ ] 7 reminders.py → tasks created and verified
- [ ] 8 shown to Martin
```

**1 · Find the review page.** `python3 $S/find_prospect.py "<name>" --email <email> --phone "<phone>"`. It creates `booking/`, writes `booking/baseline.md` (what the prospect already saw) and prints slug, review URL, website, health flag. Exit 2 = no or several matches: AskUserQuestion card with the candidates and "no review page" (then the messages drop the "seit meiner Analyse" line).

**2 · Booking + times.** Write `00_project/prospects/<slug>/booking/booking.json` (fields and sample: `references/steps-2-5-7.md`), then:

```bash
python3 $S/tz_times.py --start "<start_as_shown>" --tz <tz_as_shown> --phone "<phone>" --out 00_project/prospects/<slug>/booking/booking.json
```

`phone` = the number from the booking, even when her website shows another. The phone prefix sets her zone; if the practice is in another country, pass `--prospect-tz`. Read `mode` per message: `slot` (reminder fires at `fireAt`), `now` (slot past, Martin sends right after the run), `merged` (content goes into `merged_into`, no file for it; merge rules in the reference). Note `warnings` (DST, night for her: a "now" message waits until 07:00 her time).

**3 · Fresh check.** `python3 $S/quick_check.py <slug>` (free). Then at most 3 paid calls from `references/insight-menu.md` section 3, booking folder as ledger dir:

```bash
python3 00_project/prospect-mini/scripts/dfs.py 00_project/prospects/<slug>/booking <endpoint> '<json>' <out> 0.30
```

Save every other page read as `curl -sL -A "Mozilla/5.0" <url> -o 00_project/prospects/<slug>/booking/evidence/page-<name>.html`. A failing source is "unreadable": drop the insight, never write "nothing found".

**4 · Pick.** Read `booking/baseline.md`, `booking/site-check.json`, today's evidence. Choose two NEW insights, the traffic example and the success story (rules: `references/insight-menu.md`). One line per pick into `booking/picks.md`.

**5 · Write.** One `booking/mX.txt` per non-merged message (shape: `references/message-templates.md`), then `booking/claims.json`, one entry per fact (number lists / `"quote"` / `"absent"` / `"derived"`; details: `references/steps-2-5-7.md`). No fact about her site outside a claim.

**6 · Check loop.** `python3 $S/check_sequence.py <slug>`. On FAIL fix the message (rewrite the sentence; drop a fact only if it has no evidence) and rerun until `RESULT: PASS`. Then `python3 $S/check_sequence.py <slug> --write` (writes `whatsapp-sequence.md` and `booking/_run.json`).

**7 · Reminders.** `python3 $S/reminders.py <slug>` prints `{"create": [...], "not_scheduled": [...]}`. Call `mcp__scheduled-tasks__create_scheduled_task` once per entry with exactly these values (`notifyOnCompletion: false`), then `list_scheduled_tasks` and compare each `fireAt` with `fireAt_utc`. Never move `whatsapp-sequence.md` or the booking folder after this. Never create and delete tasks in the same parallel step. Moved or cancelled call: `references/steps-2-5-7.md`.

**8 · Show Martin.** Reply in STE: call time (her zone + WITA), WhatsApp number, table "message → send time (WITA / her time) → reminder id or JETZT SENDEN", each message as one ```text block with its WhatsApp-Link line, new insights with source, cost, check output line. A `now` message is a "Your click" card.

## Output

- `00_project/prospects/<slug>/whatsapp-sequence.md` (written only by `check_sequence.py --write`)
- `00_project/prospects/<slug>/booking/`: booking.json, baseline.md, site-check.json, evidence/, cost_ledger.jsonl, picks.md, m1–m3.txt, claims.json, _run.json
- one-time tasks `<slug>-whatsapp-1-24h`, `<slug>-whatsapp-2-morning`, `<slug>-whatsapp-3-30min` (only `slot` messages)

## References

- `references/steps-2-5-7.md`: booking.json sample, claims.json rules, reminder details, moved/cancelled call
- `references/insight-menu.md`: what counts as new, 5 % example, paid-call menu, success-story rules (HWG)
- `references/message-templates.md`: shape of each message, merge variants, Korinna reference example
- `assets/reminder-prompt.md`, `assets/reminder-values.md`: reminder prompt and its values

## Verification (before step 8, paste the evidence lines)

1. `check_sequence.py <slug>` prints `RESULT: PASS` (first line + result line).
2. `whatsapp-sequence.md` exists, its 3 headings match `booking.json → times`, every message has a WhatsApp-Link line.
3. `list_scheduled_tasks` shows each reminder at `fireAt_utc` (or the reason it was skipped).
