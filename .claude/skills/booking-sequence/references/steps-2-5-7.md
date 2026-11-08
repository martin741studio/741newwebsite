# booking-sequence: full text of steps 2, 5 and 7

All paths relative to `/Users/martindrendel/741website`. `S=.claude/skills/booking-sequence/scripts`.

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


**Step 5 · Write.** One `booking/mX.txt` per message that is not merged, with the shape and the reference example in `references/message-templates.md`. Then `booking/claims.json`: one entry per fact. A fact with numbers lists them; a fact without a number (a site change, a page feature, a link) carries a `"quote"` that occurs in the source file; a "something is missing" fact (no page for X) carries `"absent"`: a word that must NOT occur in the source (for example the URL list); computed numbers get `"derived"`. Paths: today's files as `booking/evidence/…` and `booking/site-check.json`, the review run's files as `evidence/…`, the cases as `00_project/prospect-mini/case-library.json`. Write no fact about her site that is not in a claim.


**Step 7 · Reminders.**

```bash
python3 $S/reminders.py <slug>
```

It prints `{"create": [...], "not_scheduled": [...]}`: one task definition per `slot` message (taskId, title, description, fireAt, fireAt_utc, prompt from `assets/reminder-prompt.md`) and lists the others under `not_scheduled`. The M1 reminder also runs a free site re-check (`quick_check.py --recheck`) and warns Martin when the site changed since the run. Call `mcp__scheduled-tasks__create_scheduled_task` once per entry with exactly these values (`notifyOnCompletion: false`). Then `mcp__scheduled-tasks__list_scheduled_tasks` and compare each `fireAt` (shown in UTC) with `fireAt_utc` from reminders.py. The reminders read `prospects/<slug>/whatsapp-sequence.md` by its fixed path: never move or rename it or the booking folder after the reminders are set. Task titles must be unique: never create and delete tasks in the same parallel step (one may fail while the other runs). A moved call: `update_scheduled_task` (new `fireAt` + prompt) after a new step 2 and step 6. A cancelled call: `update_scheduled_task` with `enabled: false` for both, and `_run.json` note "abgesagt".

