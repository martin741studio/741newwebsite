# 2.3 Hand-run — first canary for Marcel's Gewinnspiel funnel (2026-10-14, 06:20–06:40 WITA)

Real task: "Set up the canary for Marcel's Gewinnspiel funnel and prove an alert reaches Martin." Done by hand in this chat with Martin (cards C1–C8). Incident analysis: incident-marcel-2026-10-13.md.

## What I did, step by step
| # | Step | How | Result |
|---|---|---|---|
| 1 | Map the lead path | client memory + Marcel chat transcript | page /gewinne-jetzt → Tally 2EMGve → Zap 382522671 → KlickTipp tag 15229620 + Pipedrive pipeline 8 / stage 66 |
| 2 | L check: landing page | `curl -A … https://deep-nlp.com/gewinne-jetzt/` | 200 in 2.05 s; page links `tally.so/r/2EMGve` (2×) → keyword check = "tally.so/r/2EMGve" |
| 3 | L check: form | `curl https://tally.so/r/2EMGve` | 200 in 0.58 s |
| 4 | S/E check: Zap runs | Chrome, zapier.com/app/history (read-only) | Gewinnspiel Zap: 1 error 10.10. 18:55 (our test, nobody read it), **7 errors 13.10. 20:24–20:54 WITA**, Zapier turned the Zap off ~21:00, restored v2 14.10. 06:26 (2 successful runs 06:27 + 06:31, 1 retry "Scheduled"). History page is account-wide (`zap_id` URL param does not filter) → reader must filter by Zap name/id per row. Times shown in WITA. Plan tasks 34/2,000; Autoreplay ON. |
| 5 | R check: Tally submissions | Chrome tally.so/forms/2EMGve/submissions | **UNREADABLE**: page stays a loading skeleton after reload (2 tries). Logged as "unreadable", not as "0". → Reconciliation needs a read-only Tally API key (Martin/Marcel creates it). |
| 6 | R check: Pipedrive deals stage 66 | not done | Pipedrive login is not ours (Marcel chat 22:29Z). → needs a read-only Pipedrive API token or the Zapier MCP Pipedrive connection (exists, needs re-auth). |
| 7 | Alert path | `handrun_alert.py` (scratchpad → becomes `scripts/alert.py`): Telegram sendMessage to Martin's private bot chat with inline button "✅ Übernommen", long-poll getUpdates for the callback | sent 06:33:21 WITA (message_id 33). Ack: see below. |

## Ack measurement
- sent: 2026-10-14 06:33:21 WITA
- acknowledged: PENDING (listener runs 60 min in the background; result appended here)

## Context I had to supply (→ becomes the skill body / references)
1. Where the lead path is documented: client memory file + the client chat transcript (session JSONL in `~/.claude/projects/-Users-martindrendel-741website/`).
2. Zapier history is account-wide; filter rows by Zap name; times are in the account time zone (WITA here); Autoreplay delays error alerts.
3. "Label ≠ Tag" in KlickTipp: a tag ID copied from a label looks valid in Zapier but fails with 406. Check catalogue item: "tag/field IDs in a Zap exist in the target system".
4. Browser reads are fragile (Tally skeleton, Pipedrive login, expired Zapier/KlickTipp sessions at night). → Canaries must read via API keys / read-only tokens, never via Martin's browser session.
5. Telegram bot chat = Martin's private chat (getChat type private); no webhook set, so getUpdates long-poll works for acks. Only one consumer may long-poll → the ack listener must be a single process (server runner later).
6. Real signups came in at 20:24–20:54 WITA = 14:24–14:54 CEST (DACH afternoon). → confirms C2 (SEV1 pages 24/7).
7. A fix that needs a client login cannot meet 1 hour at night unless the login works headless → runbook item "pre-authorised read/write paths per client" for the server phase.

## Gaps found (feed into design)
- G-a: Need read-only API access per system: Tally API key, Pipedrive API token (read), Zapier (Zapier Manager push + optional Zapier API `zap:runs`), KlickTipp (tag count).
- G-b: Zapier Manager Zap in Marcel's account ("New Zap Error" / "Zap Turned Off" → Telegram) needs Martin's go (G1) and uses Marcel's tasks (≤ a few per month).
- G-c: Open blocker 11.10. → 13.10. without owner: the grill (UC3) must surface "client system broken, no owner, > 1 h".

## Update (2026-10-14, 06:33–07:05 WITA) — alert path built and proven live

Under gos C9/C12/C13 (decisions.md round 3+4), Martin created the alert bot himself ("741 Canary", @canary741_alerts_bot via @BotFather) and pasted the token into Zapier (Zapier may never receive the token from me directly). I saved the token to `.secrets/canary-telegram.env` (mode 600) and read the chat ID via `getUpdates` after Martin pressed Start.

**Live in Marcel's Zapier (read-only trigger, write only inside Zapier's own UI, nothing in KlickTipp/Pipedrive/Tally touched):**
- Zap 383443160 "741 Canary: Zap-Fehler → Telegram Alarm" — trigger Zapier Manager "New Zap Error" (all Zaps/folders, unfiltered) → Telegram Send Message to Martin's private chat. Published v1, ON. Test message delivered and confirmed by Martin in the "741 Canary" Telegram chat (screenshot).
- Zap 383444346 "741 Canary: Zap AUS/pausiert → Telegram Alarm" — trigger Zapier Manager "Zap Turned Off" (fires on auto-pause AND manual pause) → Telegram Send Message. Published v1, ON. Test message sent.

**Message template (both Zaps):** 🔴 CANARY SEV1 header, Zap title, failing step / state, error text / zap link, "Nächster Schritt: Canary-Chat öffnen, Diagnose läuft. Nichts an Marcel senden." → becomes `references/templates/telegram-alert.md`.

**Finding — "Schritt:" line empty in the test:** the sample Zap-Error record's Node Title had no data. A real error (like 10./13.10.) carries a real step name — confirmed from the Zap history read in step 2.3 (e.g. "Add or Update Contact" / "406 Tag not found"). Verify with the next real error; if Node Title is unreliable, fall back to Step Output or the Zap Run Link alone.

**Zapier UI gotcha (→ runbook note):** the message-text field's "+ insert data" picker is unreliable by coordinate click after typing — inserts can land as literal text instead of a token. Reliable method: type "/" inside the field, which opens an inline list anchored to the field itself (not a floating popover); click the field name directly in that list. Verify every insert by reading `[contenteditable="true"]`.innerText before moving on.

**This is the add-mode template for every client:** 2 Zapier Manager Zaps per Zapier account the client uses (Error, Turned Off), no filter needed when 741 manages the whole account; filter by Zap id when the account has non-741 Zaps and over-alerting must be avoided. Reusable action: `scripts/zapier_manager_alert.md` (manual build steps; Zapier has no public API to create Zaps, so this step stays a documented click sequence, not a script, until further notice).
