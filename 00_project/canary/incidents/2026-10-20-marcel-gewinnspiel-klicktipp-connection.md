# Incident marcel-gewinnspiel-klicktipp-connection — 2026-10-20

- Client: Marcel Rosenbach
- Check: found via manual check after Zell's report (not yet a standing canary check)
- Detected: 2026-10-20, by Martin asking me to check after Zell's message
- Diagnosed: The KlickTipp connection "Klick-Tipp mrosenbach1" in Zapier (the one used by 250 Zaps, including the Gewinnspiel Zap) shows status "Expired". It stopped working on 2026-10-18 around 14:20. Since then 9 Zap runs are held: 8 for "GEWINNSPIEL Okt 2026: Tally > Klicktipp > Pipedrive" and 1 for "NLP PRAC: Skool → KlickTipp + Pipedrive". One run on 2026-10-18 05:27 errored outright (disconnected app).
- Self-heal tried: none — reconnecting needs a KlickTipp login. That is an M-class action (Martin or Marcel only), not on the self-heal allowlist.
- Restored: not yet
- Total outage so far: since 2026-10-18 14:20, still ongoing.
- Within 1-hour goal: no.

## What happened (plain)
KlickTipp ended the connection that Zapier uses for Marcel's funnels. The Zaps are still on. Every new run since 2026-10-18 14:20 is held, not failed outright, so nothing is lost yet. New sign-ups are not getting their KlickTipp tag or their Pipedrive deal until someone reconnects.

## Follow-up
- New check needed: a standing canary check on this KlickTipp connection (Zapier connection status), so this is caught within minutes next time, not days.
- Owner: Martin (for the reconnect login) + Claude (for the new check)
- Done by: next working session
