# 2.3 One real task by hand — Korinna Heintze (2026-10-14, chat "⚙️🎬 Build 10-minute scripts", 06:16–06:28 UTC)

Input from Martin: voice brief (D1 in decisions.md) + cal.com screenshot (What "30 min meeting between 741 Studio and Korinna", When "Monday, October 26, 2026 4:30pm - 5:00pm (Asia/Makassar)", guest email, Google Meet link, Phone number +49 172 …).

What was done (and the context that had to be supplied):
1. Found the page: `ls 04_site/review 00_project/prospects | grep korinna`. Only `04_site/review/korinna-heintze/index.html` (old v1 page from 29.09., no `prospect.json`, no PROSPECT_DATA) → baseline = visible page text. **Context: old pages have no prospect folder data; read the HTML.**
2. Fresh free check: curl korinnaheintze.de → title + meta description now new (Executive Sparring, Erfurt, Leipzig), wrong canonical to feingold.de gone, but only **9 visible words in the raw HTML** (JS-rendered). → the "new since the analysis" insight (positive change + remaining gap).
3. Paid checks (0,098 USD total): SERP top 50 for "führungskräfte coaching" (DE) → not in top 50; Google Ads volumes for 12 terms → "coaching für führungskräfte" 2.900/month, "business coach leipzig" 70, "führungskräfte coaching leipzig" 30. **Context: volumes only from the Google Ads endpoint (lesson 1 in the prospect workflow).**
4. Message 1: thanks + call time in German time, the change seen, the remaining gap, 2.900 searches → "Schon 5 Prozent dieser Suchen wären rund 145 Besucher im Monat" (example, no promise), the 39-min video link.
5. Message 2: one more insight (Leipzig volumes, smaller competition) + Maria Abel case from case-library.json (facts only: unsichtbar → 8 Wochen unter den ersten drei).
6. Message 3: Meet link + "am besten am Laptop oder PC, nicht am Handy … Ich teile meinen Bildschirm".
7. Slop check `deslop_de.py --claims` per message → 5/5 all three. Saved `prospects/korinna-heintze/whatsapp-sequence.md`.
8. Time zones by hand: 16:30 WITA (UTC+8) = 08:30 UTC = **9:30 Uhr DE (CET, because DST ended 25.10.)**. Reminders: `korinna-whatsapp-2-24h` fireAt 2026-10-25T16:30+08:00, `korinna-whatsapp-3-15min` fireAt 2026-10-26T16:15+08:00. Prompt: never send, read the file section, push notification, show ```text block + number + call line, STE.
9. Martin's cards: reminder = scheduled tasks; make it a workflow.

Context Martin had to supply / gaps found → skill body:
- The 3-message structure and timing (D1), now m3 = 30 min (D4).
- The YouTube URL (fixed: https://www.youtube.com/watch?v=dQ9OE8GSolw).
- "Show more effort" = a NEW finding since the review page, not a repeat.
- Volume example framing ("schon 5 % … wären rund …").
- Hand time-zone maths across the DST switch is error-prone → script.
- The reminder prompt had no guard for a late catch-up run (sleeping laptop) → add.
- `dfs.py` cap counts the whole prospect ledger → use the booking folder as ledger dir so the review-page costs do not block the 0,30 cap.
