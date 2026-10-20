# AI Phone Agent — Setup-Checkliste

Übergeordneter Plan: [../ai-phone-agent-plan.md](../ai-phone-agent-plan.md)

## ✅ Schon erledigt (von Claude, 2026-08-07)
- **Supabase-Tabelle `phone_leads`** im Projekt **741-leads** (`bgiljrygqvlgwsrjvhnp`, eu-central-1) angelegt.
  - Spalten: name, firma, telefon, caller_id, email, anliegen, branche, stadt, sprache, zusammenfassung, transcript, recording_url, dauer_sekunden, conversation_id, status (default `neu`), created_at, quelle, seite.
  - RLS an, Policy `anon_insert_only` (wie `advertorial_leads`). Schreibzugriff für n8n läuft über den **Service-Role-Key** (umgeht RLS).
  - `conversation_id` ist unique → Webhook-Retries erzeugen keine Doppel-Leads (Upsert).
- **ElevenLabs-Agent-Prompt** (DE/EN) fertig: [elevenlabs-agent-prompt.md](elevenlabs-agent-prompt.md)
- **n8n-Workflow** importierbar: [n8n-phone-lead-workflow.json](n8n-phone-lead-workflow.json)

## ⛔ Von Martin zu erledigen (Account-/Finanz-/Rechts-Aktionen — kann Claude nicht)
1. **Twilio-Account** anlegen, Zahlungsmittel hinterlegen, **DE-Nummer** kaufen + **Regulatory Bundle** einreichen (Firmendokumente 741 Digital Solutions LLC + EU-Adresse). Long-Lead-Item → zuerst starten. Alternativ sipgate SIP-Trunk.
2. **ElevenLabs-Account** (Creator-Plan reicht anfangs), AGB akzeptieren.

## 🔧 Verbinden (danach, teils gemeinsam machbar)

### A) ElevenLabs-Agent bauen
- Neuen Agent anlegen, Felder aus [elevenlabs-agent-prompt.md](elevenlabs-agent-prompt.md) übernehmen (System-Prompt, First Message, alle Data-Collection-Variablen, Evaluation-Kriterium).
- Stimme testen (DE **und** EN Satz).
- Über das Web-Widget probehalber ein Gespräch führen, Prompt iterieren.

### B) Nummer anbinden
- ElevenLabs → **Phone Numbers → Import from Twilio** (Twilio SID + Auth-Token) → dem Agenten zuweisen. Inbound läuft dann automatisch.

### C) n8n-Workflow importieren
- `n8n-phone-lead-workflow.json` in n8n importieren (**Workflows → Import from File**).
- **Environment-Variablen** in n8n setzen (Settings/Env, NICHT im Workflow hardcoden):
  - `SUPABASE_SERVICE_KEY` = Service-Role-Key des 741-leads-Projekts (Supabase → Project Settings → API → service_role secret).
  - `TELEGRAM_BOT_TOKEN` = Token des bestehenden Telegram-Bots (gleicher wie in der Trading-Alert-Pipeline verwendbar).
  - `TELEGRAM_CHAT_ID` = Martins Chat-ID.
- Workflow **aktivieren**, Production-Webhook-URL kopieren (der Pfad ist `/webhook/elevenlabs-postcall`).
- In ElevenLabs → **Settings → Webhooks → Post-call webhook** diese URL eintragen, Event `post_call_transcription`.
- **Optional aber empfohlen:** ElevenLabs-Webhook-Secret in einem zusätzlichen n8n-Node (HMAC-Check auf Header `elevenlabs-signature`) verifizieren, bevor geschrieben wird.

### D) Testanruf
- Nummer anrufen, DE-Gespräch führen → in Supabase (`phone_leads`) prüfen, Telegram-Ping prüfen. Dann EN-Gespräch testen.

### E) Live schalten
- Nummer als **primäre Telefonnummer** ins **Google Business Profile** von 741 eintragen.
- Website + Schema aktualisieren (Snippets unten), damit NAP konsistent bleibt.
- Datenschutz-Absatz ergänzen (unten).

---

## Website-Snippets (kann Claude einbauen, sobald die Nummer feststeht)

### LocalBusiness-Schema (`telephone`)
```json
"telephone": "+49 XXX XXXXXXX"
```
(im bestehenden LocalBusiness/Organization-JSON-LD ergänzen bzw. aktualisieren)

### Sichtbare Nummer
- Kontaktseite, Footer, ggf. Header-CTA — überall dieselbe Nummer, identisches Format wie im GBP.

### Datenschutz-Absatz (Entwurf, DE)
```
Telefonische Kontaktaufnahme / KI-Assistent
Wenn Sie uns anrufen, wird Ihr Anruf von einem KI-gestützten Sprachassistenten
entgegengenommen. Zu Beginn des Gesprächs werden Sie darauf hingewiesen. Der Anruf
sowie die von Ihnen genannten Angaben (Name, Anliegen, Rückrufnummer, ggf. E-Mail)
werden verarbeitet und gespeichert, um Ihre Anfrage zu bearbeiten und Sie zurückzurufen.
Zur Bereitstellung dieses Dienstes setzen wir Auftragsverarbeiter ein (Telefonie:
Twilio; Sprach-KI: ElevenLabs; Workflow-Automatisierung: n8n; Speicherung: Supabase,
Serverstandort EU). Rechtsgrundlage ist Art. 6 Abs. 1 lit. b und f DSGVO. Sie können
der Verarbeitung jederzeit widersprechen; kontaktieren Sie uns dazu unter [E-Mail].
```
> Vor Veröffentlichung von einem Anwalt/DSGVO-Berater gegenlesen lassen — das ist ein Entwurf, keine Rechtsberatung.

---

## Kosten-Erinnerung
~$25–35/Monat bei ~50 Calls à 3 min (Twilio-Nummer + Minuten + ElevenLabs + n8n self-host). Siehe Plan.
