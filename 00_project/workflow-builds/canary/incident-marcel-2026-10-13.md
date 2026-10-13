# Incident: Marcel Rosenbach, Gewinnspiel funnel (2026-10-08 to 2026-10-14)

Source: client chat "👥🧠 Marcel Rosenbach — NLP-Funnel Automation" (session local_61b8f208…, transcript c4cdeb06…jsonl), Marcel's WhatsApp screenshot (forwarded 13.10. 21:06 WITA), memory marcel-rosenbach-client.md. All times WITA (UTC+8) unless marked.

## System
Landing page deep-nlp.com/gewinne-jetzt → Tally form 2EMGve → Zap 382522671 "GEWINNSPIEL Okt 2026: Tally > Klicktipp > Pipedrive" (Marcel's Zapier) →
1. KlickTipp Add/Update Contact + tag "Gewinnspiel Skool Oktober 2026" (starts the instant mail)
2. KlickTipp Tag Contact
3. Pipedrive Find/Create Person → Create Deal (pipeline GEWINNSPIEL 🎉 PRAC, id 8, stage 🎉NLP-FREUND, id 66) → Create Note.

## Timeline
| When (WITA) | What | Evidence |
|---|---|---|
| 08.10. ~15:11 | Zap built. Tag field set as a custom value `100456`. The chat said the tag was "created", but it never existed in Marcel's KlickTipp. Step tests were skipped. | chat 2026-10-08T07:08–07:11Z |
| 08.10. ~15:38 | Marcel publishes the Zap (v1). The chat reports "live and tested". | chat 07:38–07:55Z |
| 10.10. | Our own form test runs. Zap run fails at step 2: `[406] Validation error: "tagid" Tag not found`. Nobody reads the run history. | chat 2026-10-11T09:00Z |
| 11.10. ~17:00 | Marcel says the automation does not work. The chat finds the root cause. Fix needs the tag in KlickTipp. The fix stays open, with no owner and no deadline. | chat 2026-10-11T09:00Z |
| 11.–13.10. | Campaign goes live ("wir sind live"). Every real signup fails at step 2: no KlickTipp contact, no instant mail, no Pipedrive deal. Tally keeps the submissions. | screenshot, chat 22:01Z |
| 13.10. 21:00 | Zapier turns the Zap OFF ("keeps erroring each time it runs") and mails alerts@mail.zapier.com → kontakt@marcel-rosenbach.de (Marcel's inbox, 15:00 CEST). | screenshot |
| 13.10. 21:06 | Marcel forwards the mail to Martin on WhatsApp: "passt jetzt alles mit dem Gewinnspiel, wir sind nämlich live". | screenshot |
| 14.10. 05:41 | Martin posts the screenshot in the client chat (about 8.5 h after the forward). | chat 21:41Z |
| 14.10. 05:43–06:09 | Zapier and KlickTipp sessions expired. Agent must wait for Martin's logins (no credentials by agent). Tag created in KlickTipp. | chat 21:43–22:09Z |
| 14.10. 06:11 | Zap turned on again. 06:15 test: Pipedrive OK, KlickTipp step still fails (new error under investigation). | chat 22:11–22:16Z |

## Impact
- Known broken since 10.10. (in run history) and 11.10. (Marcel's report). Live campaign broken for all signups until at least 14.10. 06:15, and KlickTipp still failing then.
- Outage far above the 1-hour target: days, not hours.
- Exact count of lost signups: not yet verified (needs Zap history + Tally submissions count).

## Why we did not catch it (5 gaps)
1. **No launch gate.** "Live and tested" was claimed with skipped step tests. Nobody checked the Zap run history after the first real test.
2. **Alerts go to the client, not to 741.** Zapier error and auto-pause mails go to the Zap owner's inbox (Marcel).
3. **No outside check.** Nothing compared "form submissions in" with "deals / contacts out".
4. **Known blocker without owner.** The 11.10. finding had no owner, deadline or escalation. It did not reach the morning grill as a red item.
5. **Slow human path.** WhatsApp forward at 21:06 → seen 05:41. Fix then blocked twice on expired logins.

## Signals that would have caught it (canary candidates)
| # | Signal | Type | Catch time |
|---|---|---|---|
| S1 | Pre-launch end-to-end gate: submit a test record, then read the Zap run history and the target records | launch gate | before launch (10.10.) |
| S2 | Zapier Manager trigger "New Zap Error" / "Zap turned off" → webhook to the 741 canary inbox | push from the source | ≤ 1–15 min after the first failed run |
| S3 | Zap state poll: Zap 382522671 is "on" | liveness | ≤ 1 check interval after auto-pause |
| S4 | Reconciliation: Tally submissions vs Pipedrive deals in pipeline 8 / stage 66 vs KlickTipp tag count in the last window | absence of signal | ≤ 1 window after the first real signup |
| S5 | Landing page + Tally form answer 200 and contain the form | liveness | ≤ 1 interval |
| S6 | Open-blocker aging: any "client system broken" finding older than 1 h without owner → red card | process | 11.10. |

## Self-heal options for this case (allow-list candidates)
- Safe without go: re-read config, refresh tag lists, replay failed Zap runs AFTER the root cause is fixed (Zapier "Replay"), re-check.
- Needs go / human: create a tag in the client's KlickTipp, edit and republish a Zap, any login. The agent never enters credentials.
- Prevention: read-only API keys / agent account for KlickTipp, Pipedrive, Zapier so a check does not depend on Martin's browser session.
