---
name: booking-sequence
description: Prepares the 741 booking sequence after a prospect books a call from a review page or Loom video - finds the review page, runs a small fresh check of the site and search data for something NEW, writes 3 German WhatsApp messages in Martin's voice (24 h before, morning of the call day, 30 min before), converts the call time to the prospect's time zone, saves prospects/<slug>/whatsapp-sequence.md with a wa.me link per message and sets one-time reminders. Never sends anything. Use when Martin pastes a cal.com booking ("A new event has been scheduled", "30 min meeting between 741 Studio and …", a phone number), or says "neue Buchung", "hat einen Call gebucht", "hat einen Termin gebucht", "WhatsApp-Sequenz für <Name>", "bereite die Nachrichten nach der Buchung vor", or a booked call was moved or cancelled. Do NOT use for the review page itself or its Loom/final message (local-seo-review-page), for call preparation notes, or for client messages of running clients.
---

# Booking sequence (WhatsApp after a call booking)

## Critical

- **Never send anything.** No WhatsApp, email or LinkedIn message, no tool that contacts the prospect. Martin sends every message himself. The reminders only show him the ready text and its wa.me link.
- **Timing (Martin 14.10.):** nothing goes out right after the booking. M1 = 24 h before the call (new insight + 5 % example + video), M2 = 08:00 her time on the call day (insight + success story), M3 = 30 min before (link + laptop tip). Merges and "send now" cases come only from `tz_times.py`.
- **Something NEW, real data only.** Message 1 and 2 each carry one insight that is not on the review page, backed by an evidence file in `claims.json`. Traffic numbers are an example ("wären rund"), never a promise. No "unclaimed". No tool names. HWG for health prospects.
- **Run `scripts/check_sequence.py <slug>` and deliver only on `RESULT: PASS`** (all hard rules + slop 5/5 per message). Times come only from `scripts/tz_times.py`, never from mental maths.

## Inputs

From the booking (cal.com screenshot or text): name, email, phone (= WhatsApp), call start + zone as shown (cal.com shows Asia/Makassar = Bali, WITA, UTC+8), meeting link. Nothing else is needed. A missing meeting link → write m3 with the link once Martin gives it (ask with a card).

## Workflow

All paths below are relative to `/Users/martindrendel/741website`. `S=.claude/skills/booking-sequence/scripts`. Copy this checklist and tick it off:

```
Booking sequence <Name>:
- [ ] 1 find_prospect.py (card if 0 or >1 match)
- [ ] 2 booking.json + tz_times.py
- [ ] 3 quick_check.py + max 3 paid calls (cap 0,30 USD)
- [ ] 4 two NEW insights + traffic example + case picked
- [ ] 5 m1/m2/m3 + claims.json written
- [ ] 6 check_sequence.py → PASS (loop) → --write
- [ ] 7 reminders.py → tasks created and verified
- [ ] 8 shown to Martin
```

**Step 1 · Find the review page.**

```bash
python3 $S/find_prospect.py "<name>" --email <email> --phone "<phone>"
```

It creates `booking/`, writes `booking/baseline.md` (what the prospect already saw: full page text + the review run's findings) and prints slug, review URL, website, health flag. Exit 2 = no or several matches → AskUserQuestion card with the candidates (and "no review page" as an option; then the messages drop the "seit meiner Analyse" line). When `health_reason` is only a guess, check the page title once.

**Step 2 · Booking + times.** Write `00_project/prospects/<slug>/booking/booking.json`:

```json
{"name": "Korinna Heintze", "first_name": "Korinna", "email": "…", "phone": "+4915112345678",
 "meet_link": "https://meet.google.com/…", "start_as_shown": "2026-10-26 16:30", "tz_as_shown": "Asia/Makassar",
 "slug": "<slug>", "review_url": "https://741.studio/review/<slug>/", "health": false, "mode": "Echt", "booked_at": "<now ISO>", "language": "de"}
```

`phone` = the number from the booking (that is her WhatsApp), even when her website shows another number. `health` from step 1. `mode` = `Trockenlauf` for a test booking. Then:

```bash
python3 $S/tz_times.py --start "<start_as_shown>" --tz <tz_as_shown> --phone "<phone>" --out 00_project/prospects/<slug>/booking/booking.json
```

The phone prefix sets the prospect zone. If the review page shows a town in another country than the phone prefix (for example a German number, practice in Vienna), pass `--prospect-tz` with the practice's zone. Read `mode` per message: `slot` = a reminder fires at `fireAt`; `now` = the slot is already past, Martin sends this message right after the run; `merged` = its content goes into `merged_into` (call before 09:30 her time → M2 into M3; booking on the call day → M2 into M1; call in less than 35 min → all into M3). Write no file for a merged message; write its content into the target message. `warnings`: daylight-saving change, night for her (a "now" message waits until 07:00 her time).

**Step 3 · Fresh check.** Free first:

```bash
python3 $S/quick_check.py <slug>
```

Then at most 3 paid calls from the menu in `references/insight-menu.md` section 3 (local term = measured from her town), always with the booking folder as ledger dir:

```bash
python3 00_project/prospect-mini/scripts/dfs.py 00_project/prospects/<slug>/booking <endpoint> '<json>' <out> 0.30
```

Every other page you read for an insight: `curl -sL -A "Mozilla/5.0" <url> -o 00_project/prospects/<slug>/booking/evidence/page-<name>.html`, so a claim can quote it. A source that fails (timeout, task status ≠ 20000 after one retry) is "unreadable": drop that insight, never write "nothing found".

**Step 4 · Pick.** Read `booking/baseline.md`, `booking/site-check.json` and today's evidence. Choose two NEW insights, the traffic example and the success story with the rules in `references/insight-menu.md`. Write one line per pick into `booking/picks.md` (insight → evidence file).

**Step 5 · Write.** One `booking/mX.txt` per message that is not merged, with the shape and the reference example in `references/message-templates.md`. Then `booking/claims.json`: one entry per fact. A fact with numbers lists them; a fact without a number (a site change, a page feature, a link) carries a `"quote"` that occurs in the source file; a "something is missing" fact (no page for X) carries `"absent"`: a word that must NOT occur in the source (for example the URL list); computed numbers get `"derived"`. Paths: today's files as `booking/evidence/…` and `booking/site-check.json`, the review run's files as `evidence/…`, the cases as `00_project/prospect-mini/case-library.json`. Write no fact about her site that is not in a claim.

**Step 6 · Check (feedback loop).**

```bash
python3 $S/check_sequence.py <slug>
```

On `FAIL`: fix the flagged message (rewrite the sentence, do not delete the fact unless it has no evidence), run again. Repeat until `RESULT: PASS`. Then:

```bash
python3 $S/check_sequence.py <slug> --write
```

This writes `00_project/prospects/<slug>/whatsapp-sequence.md` and `booking/_run.json` (the overview Excel picks it up by itself).

**Step 7 · Reminders.**

```bash
python3 $S/reminders.py <slug>
```

It prints `{"create": [...], "not_scheduled": [...]}`: one task definition per `slot` message (taskId, title, description, fireAt, fireAt_utc, prompt from `assets/reminder-prompt.md`) and lists the others under `not_scheduled`. The M1 reminder also runs a free site re-check (`quick_check.py --recheck`) and warns Martin when the site changed since the run. Call `mcp__scheduled-tasks__create_scheduled_task` once per entry with exactly these values (`notifyOnCompletion: false`). Then `mcp__scheduled-tasks__list_scheduled_tasks` and compare each `fireAt` (shown in UTC) with `fireAt_utc` from reminders.py. The reminders read `prospects/<slug>/whatsapp-sequence.md` by its fixed path: never move or rename it or the booking folder after the reminders are set. Task titles must be unique: never create and delete tasks in the same parallel step (one may fail while the other runs). A moved call: `update_scheduled_task` (new `fireAt` + prompt) after a new step 2 and step 6. A cancelled call: `update_scheduled_task` with `enabled: false` for both, and `_run.json` note "abgesagt".

**Step 8 · Show Martin.** Reply in STE: call time (her zone + WITA), WhatsApp number, a short table "message → send time (WITA / her time) → reminder id or JETZT SENDEN", each message as one ```text block with its WhatsApp-Link line, the new insights and their source, the cost, and the check output line. A message with mode `now` is a "Your click" AskUserQuestion card (send now). Anything else that waits on Martin goes into a card too, never into prose.

## Output

- `00_project/prospects/<slug>/whatsapp-sequence.md` (written only by `check_sequence.py --write`)
- `00_project/prospects/<slug>/booking/`: booking.json, baseline.md, site-check.json, evidence/, cost_ledger.jsonl, picks.md, m1–m3.txt, claims.json, _run.json
- one-time scheduled tasks `<slug>-whatsapp-1-24h`, `<slug>-whatsapp-2-morning`, `<slug>-whatsapp-3-30min` (only for `slot` messages)

## References

- `references/insight-menu.md`: what counts as new, the 5 % example, paid-call menu, success-story rules (HWG)
- `references/message-templates.md`: shape of each message, merge variants, Korinna reference example
- `assets/reminder-prompt.md`: the reminder task prompt (filled by `scripts/reminders.py`; `assets/reminder-values.md` explains each value)

## Verification

Before the reply in step 8, all three must hold. Paste the evidence lines into the reply:

1. `python3 $S/check_sequence.py <slug>` prints `RESULT: PASS` (paste the first line and the result line).
2. `whatsapp-sequence.md` exists, its 3 headings show the same times as `booking.json → times`, and every message has a WhatsApp-Link line.
3. `list_scheduled_tasks` shows each reminder at the `fireAt_utc` from reminders.py (or the reason it was skipped).

If one fails, fix it and run the check again. Do not report "done" before all three pass.
