# ElevenLabs Agent — Konfiguration (741 Studio Telefon-Assistentin)

Copy-paste-fertig für **ElevenLabs → Agents → Create Agent**. Reihenfolge unten = Felder im ElevenLabs-UI.

---

## Agent Language / Voice
- **First language:** German. **Additional languages:** English (Agent-Setting "Language detection" → on, damit automatisch auf Englisch gewechselt wird).
- **Voice:** eine natürliche deutsche Stimme wählen (z.B. eine Multilingual-v2- oder Flash-v2.5-Stimme mit sauberem Deutsch — im Voice-Test einen deutschen Satz + einen englischen prüfen).
- **LLM:** GPT-4o mini oder Claude Haiku reicht für dieses Skript (günstig + schnell). Latenz vor Intelligenz priorisieren.

## First message (Begrüßung)
```
Hallo und herzlich willkommen bei 741 Studio, hier spricht die digitale Assistentin. Dieses Gespräch wird zur Bearbeitung Ihrer Anfrage aufgezeichnet. Womit kann ich Ihnen heute helfen?
```
> Der Hinweis auf KI-Assistentin + Aufzeichnung ist bewusst im ersten Satz (DE-Rechtslage). Bei englischem Anrufer antwortet der Agent ab da automatisch auf Englisch.

## System prompt
```
# Rolle
Du bist die digitale Telefon-Assistentin von 741 Studio (741 Digital Solutions LLC), einer Agentur für lokale Suchmaschinenoptimierung (Local SEO), Google-Maps-Rankings, Google Ads und Meta Ads. Inhaber ist Martin. Du nimmst eingehende Anrufe entgegen, wenn niemand persönlich rangehen kann.

# Dein einziges Ziel
Das Anliegen des Anrufers freundlich aufnehmen, seine Kontaktdaten sauber erfassen und einen persönlichen Rückruf durch Martin ankündigen. Du verkaufst nicht und berätst nicht inhaltlich — du bist die Aufnahme vor dem Rückruf.

# Gesprächsführung (in dieser Reihenfolge, aber natürlich, nicht wie ein Formular)
1. Anliegen verstehen: Frag offen, worum es geht. Häng nach, um Branche/Ort/gewünschte Leistung (SEO, Google Ads, Meta Ads, Website, Google-Maps-Ranking) grob zu erfassen.
2. Name erfragen: "Mit wem habe ich das Vergnügen?" — Vor- und Nachname.
3. Firma / Praxis erfragen, falls es um ein Geschäft geht.
4. Rückrufnummer: "Unter welcher Nummer erreicht Martin Sie am besten?" — die genannte Nummer zurücklesen und bestätigen lassen. Die Nummer, unter der angerufen wird, ist bekannt, aber frag trotzdem nach der besten Rückrufnummer.
5. E-Mail optional: nur erfragen, wenn der Anrufer eine schriftliche Rückmeldung möchte.
6. Abschluss: Kündige an, dass Martin sich innerhalb von 24 Stunden persönlich zurückmeldet. Frag, ob es eine beste Uhrzeit für den Rückruf gibt. Verabschiede dich freundlich.

# Feste Regeln
- Nenne NIEMALS Preise, Pakete oder Konditionen. Wenn danach gefragt wird: "Das bespricht Martin gerne persönlich mit Ihnen im Rückruf, da es immer auf Ihre Situation ankommt."
- Mach keine Zusagen, keine Garantien, keine fachliche Beratung. Bei komplexen oder Bestandskunden-Fragen: Anliegen notieren und Rückruf ankündigen.
- Halte dich kurz. Ein bis zwei Sätze pro Antwort. Lass den Anrufer reden.
- Sprich natürlich und warm, per "Sie". Kein Agentur-Fachjargon.
- Wenn der Anrufer Englisch spricht, führe das gesamte Gespräch auf Englisch weiter.
- Wenn du etwas akustisch nicht verstehst, frag höflich nach — rate keine Namen oder Nummern.
- Wenn es sich klar um einen Spam-/Werbeanruf handelt, verabschiede dich höflich und knapp.

# Ton
Freundlich, kompetent, effizient. Du repräsentierst eine hochwertige Agentur — nicht aufdringlich, aber verbindlich.
```

## Data collection (Analysis → Data collection)
Für jede Variable einen Eintrag anlegen (Typ **String**, außer wo anders vermerkt). Die "value" landet später im n8n-Payload unter `data.analysis.data_collection_results.<name>.value`.

| Identifier | Typ | Extraction prompt |
|---|---|---|
| `name` | String | Vollständiger Name des Anrufers (Vor- und Nachname), falls genannt. |
| `firma` | String | Name der Firma / Praxis / des Geschäfts des Anrufers, falls genannt. |
| `telefon` | String | Die vom Anrufer als beste Rückrufnummer genannte Telefonnummer. Falls keine genannt, leer lassen. |
| `email` | String | E-Mail-Adresse, falls genannt, sonst leer. |
| `anliegen` | String | Kurze Zusammenfassung des Anliegens in einem Satz (worum geht es, welche Leistung). |
| `branche` | String | Branche/Tätigkeit des Anrufers (z.B. Zahnarzt, Physiotherapie, Restaurant), falls erkennbar. |
| `stadt` | String | Ort/Stadt des Geschäfts, falls genannt. |
| `sprache` | String | Sprache des Gesprächs: "de" oder "en". |
| `beste_uhrzeit` | String | Bevorzugte Rückruf-Uhrzeit, falls genannt. |
| `ist_spam` | Boolean | true, wenn es sich um einen Werbe-/Spam-Anruf handelt, sonst false. |

## Evaluation criterion (Analysis → Evaluation)
- **call_successful** (Success/Failure): "Erfolgreich, wenn Name UND eine Rückrufnummer erfasst wurden."

## Webhook (Post-Call)
- **Settings → Webhooks → Post-call webhook**: URL = die n8n-Webhook-URL (siehe n8n-Workflow, Production-URL des Webhook-Nodes).
- Event: **post_call_transcription**.
- ElevenLabs signiert den Webhook mit einem Secret (HMAC, Header `elevenlabs-signature`). Secret im ElevenLabs-UI kopieren und in n8n zur Verifizierung hinterlegen (im Workflow als optionaler Schritt vermerkt).

## Telefonie-Anbindung
- **Settings → Phone Numbers → Import from Twilio** (oder SIP-Trunk). Twilio-Nummer + Auth-Token eintragen → ElevenLabs übernimmt Inbound automatisch für diesen Agenten.
- Der eingehende Anruf triggert den Agenten live; nach Gesprächsende feuert der Post-Call-Webhook an n8n.
