# 2.1 Use cases — Night Shift + Server

## UC1 Scheduled night (main case)
- Trigger: systemd timer on the VPS, 17:30 WITA, Mon–Fri (later all days if Martin wants).
- Steps: read kill switch → read Martin's confirmed night queue (17:00 card; without answer only read-only items) → per item one fresh `claude -p` Executor + one Critic → night cards → 19:15 and 21:15 "cards ready" mail → read check-in answers → next batch → 05:00 stop → REVIEW + night report → push to branch `nightshift/<date>` → pulse line.
- Tools: runner script (bash/python), `claude -p` (plan login via setup-token), skill `night-shift` v2, seo-page-optimizer, deslop, DataForSEO / GSC / GA4 read scripts, Local Falcon MCP (read tools only), Playwright MCP headless, Supabase REST as machine user `nightshift-bot`.
- Result: drafts, audits, research files and builds on the server branch; ≤ 5 cards per check-in in the Command Center; night report for the 06:13 grill.

## UC2 Evening check-in from the phone
- Trigger: mail "Night shift: 4 cards ready" to martin@741.studio at 19:15 / 21:15; Martin opens the Command Center (admin) on the phone at 19:30 / 21:30.
- Steps: Martin answers ≤ 5 cards (approve draft / redo with note / park with reason / own answer). Runner pulls answers before the next batch; redo notes go into the next Executor prompt.
- Tools: Command Center tab (existing), `grill_answers` (existing), night card rows.
- Result: course correction without the laptop; nothing goes live from a card (approve = "draft accepted for day release").

## UC3 Ad-hoc night item (manual)
- Trigger: Martin says "Nachtschicht: <task> für <client>" or "put this in tonight's night queue" in any chat or in the 17:00 log.
- Steps: classify the item (night class or never class) → add it to tonight's queue file → it shows on the 17:00/17:30 queue card.
- Tools: skill `night-shift` v2 queue mode, `queue_add.py`.
- Result: item queued with class, client, inputs, done-definition; a "never" item becomes a day card instead.
