# Zapier Manager alert setup — manual build steps (no public API to create Zaps)

Proven live 2026-10-14 on Marcel Rosenbach's account (hand-run.md). Repeat per client Zapier account. Each client needs TWO Zaps (one trigger per Zap).

## Before you start
- Confirm the Telegram bot token exists: `.secrets/canary-telegram.env`. If the client needs a dedicated channel (e.g. a shared group), that is a separate decision — default is Martin's private 741 Canary chat.
- You need to be looking at the client's own Zapier account (their tab, their login — never type credentials).

## Zap 1 — New Zap Error
1. zapier.com/webintent/create-zap → Trigger → app "Zapier Manager" → event "New Zap Error".
2. Configure: leave Account/Folder/Zap empty to watch the whole account (default), or pick a specific Zap if the client has non-741 Zaps and over-alerting must be avoided.
3. Test trigger (read-only, loads a recent sample error) → Continue with selected record.
4. Action → app "Telegram" → event "Send Message" → connect/select the "741 Canary" bot account.
5. Chat Id: pick Martin's private chat (or the escalation group once it exists) from the dropdown.
6. Message Text — type `/` inside the field to open the inline field list (coordinate-click on the "+" picker is unreliable, see hand-run.md gotcha), then build:
   ```
   🔴 CANARY SEV1 · <Client> · Zap-Fehler
   Zap: <Title>
   Schritt: <Node Title>
   Fehler: <Message>
   Lauf: <Zap Run Link>

   Nächster Schritt: Canary-Chat öffnen, Diagnose läuft. Nichts an <Client> senden.
   ```
   Verify with `document.querySelector('[contenteditable="true"]').innerText` via javascript_tool before continuing.
7. Disable Link Preview = Yes. Continue → Test step (sends one real Telegram message — tell Martin to expect it). Publish, name it `741 Canary: Zap-Fehler → Telegram Alarm`.

## Zap 2 — Zap Turned Off
Same steps, trigger event "Zap Turned Off" (fires on auto-pause AND manual pause). Message fields: `Title`, `State`, `Zap Link` (there is no error message here). Template:
```
🔴 CANARY SEV1 · <Client> · Zap abgeschaltet oder pausiert
Zap: <Title>
Status: <State>
Zap-Link: <Zap Link>

Nächster Schritt: Canary-Chat öffnen, Diagnose läuft. Nichts an <Client> senden.
```
Publish, name it `741 Canary: Zap AUS/pausiert → Telegram Alarm`.

## After both are live
- Add two rows to `00_project/canary/canaries.json` (type E, status live, runner zapier_manager) with `registry.py add`.
- Tell Martin both Zap names/ids and that test alerts were sent — do not claim "done" without a delivered test message.
