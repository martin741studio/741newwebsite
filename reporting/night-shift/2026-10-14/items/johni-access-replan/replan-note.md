# Johni Jaya Motor — re-plan of the 25 overdue portal tasks

Portal goal (Martin, 2026-10-13): "Restart: 3 missing access done, overdue list cleared or re-planned, then the normal Maps goal."
Today's re-check (2026-10-14 morning grill, source `701c3ead`) already tested part of the list against the live site and the actual access state. This note carries that result forward and sorts it into an action plan.

[fehlt: the raw portal table with all 25 task rows and IDs was not found in the local repo (no SQL/JSON export for client b84427b9-57bc-4145-83fc-ec284d2de785 lists task-level titles for the current 44-task program). The categories below come from (a) the verified cross-check already run today and logged in the morning-grill files, and (b) the project memory's own "Open" list, both cited in sources.md. Martin should open the live portal task list once and match each of the 25 rows against the 3 buckets below — most should sort in under 5 minutes.]

## Bucket 1 — Done, just needs the checkbox ticked (re-verified today)
These were done in the 2026-08-08 on-page pass or the 2026-10-13 restart/GBP pass, and today's check confirms they are still true on the live site:
- Opening hours shown correctly: site footer says "Senin – Sabtu: 09.00 – 16.30" (Mon–Sat), matches GBP. Confirmed live 2026-10-14.
- Booking / WhatsApp link live and working: wa.me/628176583223, confirmed live 2026-10-14 (also set as the GBP booking link on 2026-10-13).
- GBP categories, all 28 services with prices, business description — done 2026-10-13, pending Google review (≤1 day), portal task w9 already logged as done in memory.
- GA4 restart chain: new 741-owned GA4 property created and tag live on the site, reporting-bot given access, Google Search Console property verified for johnijayamotor.com with the robot as owner — all done 2026-10-13.

Action: tick these in the portal. They are not real backlog.

## Bucket 2 — Genuinely still open (keep on the list, not stale)
- **FAQ section on the homepage** — intentionally postponed by Martin in August 2026, not forgotten. Confirmed again today: the live homepage has no FAQ section. Keep open, but note it is a deliberate hold, not neglect — do not flag it as overdue in the same way as a missed task.
- **Citations / directory listings** — Apple Maps, Bing, Facebook, and the Indonesian directory set are genuinely untouched. Real gap.
- **Review-engine briefing** (asking happy customers for Google reviews) — genuinely untouched. Real gap.
- **Local Falcon baseline ranking scan** — blocked, not done: the Local Falcon connector is disconnected in claude.ai. Needs Martin to re-enable it (2 switches), then the scan ('bengkel mobil jakarta utara', grid 7, radius 3km) can run.
- **2FA / login-limit plugin** — recommended after the August attack-probing incident, not yet installed. Password rotation itself is done.
- **Certificate logos** — the old (broken/fake) certificate block was removed from the site; waiting on the client to send real certificate images before it can be replaced.
- **Client message on GTM access + old GA4 history** — drafted in English, parked; not sent. Needed to find out who holds the old tag G-XZCKK6Z6BJ.

## Bucket 3 — Could not confirm (needs a portal look, not a code look)
Any of the 25 items not covered by Bucket 1 or 2 above (e.g. onboarding steps, other week-9/10/11 program tasks) could not be checked from site + memory alone — the portal UI itself was not opened (no login, per night-shift rules). Martin: open the portal, the 2 buckets above should account for most of the 25; whatever is left over sorts itself into "done, tick it" or "real gap" using the same test (does the live site / live GBP already show it?).

## Net re-plan
- Program goal stays "restart"; the blocking access items are closed as of 2026-10-13.
- Only genuine backlog left: FAQ (on hold by Martin's own choice), citations, review-engine briefing, Local Falcon (waiting on Martin), 2FA, certificate logos, and the parked client message.
- Recommend: Martin re-ticks Bucket 1 in the portal, then the "25 overdue" count should drop to roughly 7 real open items (Bucket 2) plus whatever Bucket 3 turns out to hold.
