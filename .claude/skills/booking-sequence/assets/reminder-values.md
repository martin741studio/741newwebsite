# Reminder values (filled by scripts/reminders.py)

| | Message 1 | Message 2 | Message 3 |
|---|---|---|---|
| When (Martin 14.10.) | 24 h before the call | 08:00 her time on the call day | 30 min before the call |
| taskId | `<slug>-whatsapp-1-24h` | `<slug>-whatsapp-2-morning` | `<slug>-whatsapp-3-30min` |
| Section in whatsapp-sequence.md | `## 1 · 24 h vorher` | `## 2 · Morgen des Termins` | `## 3 · 30 Minuten vorher` |
| Late line | < 3 h before the call | < 30 min before the call | < 5 min before the call |
| Extra step | free site re-check (`quick_check.py --recheck`): warns when the site changed since the run | — | — |

Every reminder: never sends; after the call start it says "Zu spät"; a missing file or section = "not available"; it shows the ```text block, the WhatsApp-Link line (wa.me, text ready), the number and the call line. A message with mode "now" or "merged" gets no task.
