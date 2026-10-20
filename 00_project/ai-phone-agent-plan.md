# AI Phone Agent für 741.studio — Plan (Stand 2026-08-07)

**Ziel:** Eigene Rufnummer, die im Google Business Profile (und auf der Website) steht. Anrufer aus DE/AT/CH oder international landen bei einem AI-Agenten, der freundlich aufnimmt worum es geht, Kontaktdaten erfasst und einen Rückruf ankündigt. Lead landet automatisch bei uns (Supabase + Benachrichtigung).

**Status:** Nur Plan, noch nichts aufgesetzt.

---

## 1. Architektur-Entscheidung: Was macht was

Wichtigste Erkenntnis vorab: **n8n macht NICHT das Echtzeit-Gespräch.** n8n kann keine Live-Audio-Streams verarbeiten. Die Arbeitsteilung ist:

```
Anrufer (aus GBP / Website)
   │
   ▼
Telefonnummer (Twilio DE-Nummer oder SIP-Trunk)
   │
   ▼
Voice-Agent-Plattform  ← führt das Gespräch in Echtzeit
(ElevenLabs Agents / Retell / Vapi)
   │  Post-Call-Webhook (Transkript + extrahierte Daten als JSON)
   ▼
n8n auf unserem Server  ← Orchestrierung NACH dem Call
   ├─ Lead in Supabase speichern (analog advertorial_leads)
   ├─ Telegram/WhatsApp-Ping an Martin ("Neuer Anruf: …")
   ├─ Bestätigungs-Mail via Resend (optional)
   └─ Später: Kalender-Slot, Rückruf-Task, CRM-Sheet
```

Der Voice-Layer (STT → LLM → TTS, Interruption-Handling, Latenz <1s) ist bei den Plattformen gelöst — selbst bauen (Twilio Media Streams + Realtime API) lohnt sich für uns nicht, außer als späteres Lernprojekt.

## 2. Plattform-Wahl

| | ElevenLabs Agents | Retell AI | Vapi |
|---|---|---|---|
| Preis/min | ~$0.08–0.12 | ab ~$0.07 flat | real ~$0.13–0.31 (Plattform + Provider-Kosten addieren sich) |
| Deutsch-Qualität | Beste Stimmen (Multilingual) | gut | gut, flexibel |
| Twilio-Anbindung | nativ, sehr einfach | nativ | nativ |
| n8n-Webhooks | ja (Post-Call + Tool-Calls mid-call) | ja | ja |

**Empfehlung: ElevenLabs Agents.** Gründe: beste deutsche Stimmen (wichtig — deutscher Mittelstand ist unsere Zielgruppe, eine roboterhafte Stimme killt das Vertrauen), native Twilio-Integration, wir kennen ElevenLabs schon, transparente Kosten. Der Agent kann mid-call Tools aufrufen (= n8n-Webhooks), z.B. "prüfe Kalender-Verfügbarkeit" später.

Fallback: Retell, falls ElevenLabs-Kosten bei Volumen stören.

## 3. Die Nummer

**Option A — Twilio DE-Nummer (+49):** ~$5/Monat. Achtung: Deutschland verlangt ein **Regulatory Bundle** (Adressnachweis, Business-Verifizierung) bevor die Nummer aktiv wird — dauert 1–3 Tage, US-LLC-Dokumente + eine DE/EU-Adresse nötig. Ggf. geht auch eine +43/+41 oder internationale Nummer schneller.

**Option B — SIP-Trunk (z.B. sipgate trunking):** Deutsche Nummer bei deutschem Provider, per SIP an ElevenLabs geroutet. Sauberer für DE-Regulatorik, minimal mehr Setup.

**Empfehlung:** Erst Twilio probieren (eine Plattform weniger), bei Regulatory-Problemen auf sipgate ausweichen.

**Local-SEO-Hinweis (NAP!):** Die Nummer, die ins GBP kommt, wird Teil unserer NAP-Citations. Also: Nummer einmal festlegen und nie wieder wechseln → Nummer gehört uns dauerhaft (nicht an eine Plattform gebunden, Twilio-Nummern sind portierbar).

## 4. Agent-Design (Gespräch)

- **Zweisprachig:** startet auf Deutsch, wechselt automatisch auf Englisch wenn der Anrufer Englisch spricht (ElevenLabs kann Language-Detection im Agent).
- **Persona:** freundliche Assistenz von 741 Studio, kein Fake-Mensch — sagt offen, dass sie die digitale Assistentin ist (rechtlich in DE ohnehin nötig, siehe unten).
- **Gesprächsziel (in dieser Reihenfolge):**
  1. Begrüßung + "Womit können wir helfen?"
  2. Anliegen aufnehmen (Branche, Ort, was gewünscht — SEO/Ads/Website)
  3. Name, Firma, beste Rückrufnummer (Caller-ID vorbefüllen + bestätigen), optional E-Mail
  4. Rückruf ankündigen: "Martin meldet sich innerhalb von 24 Stunden persönlich zurück."
  5. Kein Pricing am Telefon (Zahlen nur im Call — bestehende Regel), keine Zusagen.
- **Guardrails:** Bei Bestandskunden-Support oder komplexen Fragen → Daten aufnehmen + Rückruf, nicht improvisieren.

## 5. n8n-Workflow (Post-Call)

Ein Workflow, Trigger = ElevenLabs Post-Call-Webhook:

1. **Webhook-Node** empfängt JSON (Transkript, extrahierte Variablen: name, firma, telefon, anliegen, sprache, Audio-Link).
2. **Supabase-Node** → neue Tabelle `phone_leads` im 741-leads-Projekt (Spalten analog `advertorial_leads` + transcript, recording_url, caller_id, duration).
3. **Telegram-Node** → Sofort-Ping an Martin mit Zusammenfassung + Rückrufnummer (gleiches Muster wie die TradingView-Alert-Pipeline).
4. **Resend-Node** (optional) → Bestätigungsmail an den Anrufer, falls E-Mail genannt.
5. **Filter:** Spam/Robocalls (Calls <10s ohne Inhalt) nicht als Lead speichern.

n8n läuft auf dem geplanten Dev-VPS/Desktop-Docker (Tailscale) — oder als n8n-Cloud-Starter, falls der Server noch nicht steht. Der Webhook braucht eine öffentlich erreichbare URL (bei Self-Host: Tailscale Funnel oder Reverse-Proxy auf dem cPanel-VPS).

## 6. Google-Business-Profile-Anbindung

- Nummer als **primäre Telefonnummer** im 741-GBP eintragen → der "Anrufen"-Button in Maps/Suche geht direkt an den Agenten.
- Website (Kontaktseite, Footer, LocalBusiness-Schema `telephone`) mit derselben Nummer aktualisieren → NAP konsistent.
- Alternative Betriebsart, falls wir irgendwann selbst rangehen wollen: Nummer bleibt im GBP, aber Twilio routet erst 15s auf Martins Handy und DANN auf den Agenten ("Missed-Call-Catcher"). Für den Start: direkt auf den Agenten.

## 7. Rechtliches (DE, kurz)

- Anrufer zu Gesprächsbeginn informieren, dass ein KI-Assistent spricht und der Anruf verarbeitet/aufgezeichnet wird (ein Satz in der Begrüßung reicht).
- Datenschutzerklärung auf 741.studio um Telefon-/Voice-Verarbeitung ergänzen (ElevenLabs + Twilio als Prozessoren, EU-Data-Residency bei ElevenLabs wählbar).

## 8. Kosten (Schätzung bei niedrigem Volumen)

| Posten | ca. |
|---|---|
| Twilio DE-Nummer | $5/Monat |
| Twilio Inbound-Minuten | ~$0.01–0.03/min |
| ElevenLabs Agents | ~$0.10/min (Creator-Plan reicht anfangs) |
| n8n | $0 (self-host) oder ~$24/Monat Cloud |
| **Bei ~50 Calls à 3 min/Monat** | **~$25–35/Monat gesamt** |

## 9. Umsetzungs-Phasen

- **Phase 1 (½ Tag):** Twilio-Account + DE-Nummer beantragen (Regulatory Bundle einreichen — das ist der Long-Lead-Item, zuerst starten). ElevenLabs-Agent mit deutschem Prompt bauen, per Web-Widget testen.
- **Phase 2 (½ Tag):** Nummer mit Agent verbinden, Testanrufe DE + EN, Prompt iterieren.
- **Phase 3 (½ Tag):** `phone_leads`-Tabelle + n8n-Workflow (Webhook → Supabase → Telegram).
- **Phase 4 (1h):** Nummer ins GBP + Website + Schema, Datenschutz-Absatz, Live-Test über den Maps-Anrufen-Button.
- **Phase 5 (später):** Kalender-Buchung mid-call, Outbound-Rückrufe, WhatsApp-Follow-up via WABA.

## 10. Bonus: Produktisierung

Exakt dieses Setup ist als **Kunden-Produkt** verkaufbar ("Verpasse nie wieder einen Anruf — KI-Rezeption für deine Praxis"): pro Kunde eigene Nummer + geklonter Agent + eigener n8n-Workflow. Passt perfekt zur Local-SEO-Zielgruppe (Praxen, die während Behandlungen nicht ans Telefon gehen). Erst am eigenen GBP validieren, dann Case draus machen.
