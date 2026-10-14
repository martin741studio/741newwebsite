# 3.7 Unattended rules (rules.md §6) — for the 2 reminder tasks (2026-10-14)

The main run is attended (Martin pastes the booking). The reminders run unattended on the laptop (Desktop one-time tasks).

| Rule | Applied |
|---|---|
| R6.6 state the time zone | the prompt carries the call start in UTC + prospect zone + WITA; the task runs `date -u` first |
| desktop-scheduled-tasks "Missed runs" (catch-up after sleep) | prompt step 2: after the call start → "Zu spät … nicht mehr senden"; step 4 late-lines for m2 (< 3 h) and m3 (< 5 min) |
| R6.2 failed read ≠ nothing | prompt step 3: file/section missing → "not available … Nothing to send", never write a message itself |
| R6.3 count as sent only after confirmation | nothing is sent by the task; Martin sends. No ledger to update |
| R6.5 read-only, spend cap | task only reads one file + push; no paid call |
| R6.7 self-contained prompt | absolute file path, name, phone, call line inside the prompt (built by reminders.py) |
| R6.10 open the run | test run in step 4.2/5.4: run once by hand and read the output |
| Bookmarks (R6.1) | n/a (one-time task, no source stream) |
