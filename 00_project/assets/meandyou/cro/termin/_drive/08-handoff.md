# Übergabe „Gespräch buchen“ — Teil für die gemeinsame Übergabe `../../08-handoff/handoff.md` (schreibt die Hauptsession)

Prototyp: `07-prototype/index.html` (Build `07-prototype/build.py`, Port 8818). Copy: `04-copy/approved-copy.md`. Entscheidungen E1 bis E8: `04-copy/OPEN-FLAGS.md`.

## URL und Links
- Neue URL `/gespraech-buchen`, `noindex, follow`, nicht in die Sitemap.
- 301 von `/sichtbarkeit-termin` auf `/gespraech-buchen` (Button auf /sichtbarkeit-neu, alte Links). Die UTM-Werte müssen beim Redirect erhalten bleiben.
- Jeder CTA der neuen Seiten zeigt auf `/gespraech-buchen?utm_source=<seite>&utm_content=<abschnitt>` (heute im Prototyp `termin.html?…`).

## Technik
- Calendly inline: `https://calendly.com/me-you/sichtbarkeit-neu` mit `hide_event_type_details=1&hide_gdpr_banner=1&background_color=ffffff&text_color=2a2622&primary_color=4f6d90`. Das Skript hängt utm_source, utm_medium, utm_campaign, utm_content, utm_term aus der Seiten-URL an, bevor `widget.js` lädt (sonst speichert Calendly sie nicht). Getestet in Chrome.
- Bestätigung: Listener auf `calendly.event_scheduled` (postMessage, Origin calendly.com) schaltet S08 ein. Keine Calendly-Einstellung nötig. An dieser Stelle später auch das Conversion-Event (GA4, Meta) auslösen.
- `hide_gdpr_banner=1` nur live lassen, wenn die Einwilligung der Website Calendly abdeckt (E5).

## Für Pauspapier (Calendly, wir ändern nichts)
- Drei Pflichtfragen und Hinweis am Telefonfeld laut Doc „No-Show: Buchungsstrecke“ (08.10.).
- Buchungsfenster: am 12.10. waren nur 12. bis 15.10. buchbar. Bitte bestätigen, ob 48 bis 72 h schon eingestellt sind.
- Sprache des Calendly-Kontos: Widget zeigt „Wählen Sie …“ (Sie-Form), Seite nutzt du.
- Umbuchen-Link in der Bestätigungsmail prüfen.

## Offene Marken [FEHLT] auf dieser Seite
- [von Kunde bestätigen: Name und Rolle der Person im Gespräch]
- [von Kunde bestätigen: Foto der Person im Gespräch]
- [von Kunde bestätigen: drei kurze Fragen im Formular eingerichtet]
- [von Kunde bestätigen: Video-Tool des Gesprächs]
- [von Kunde bestätigen: erste WhatsApp nach der Buchung eingerichtet]
- [von Kunde bestätigen: Video von Michael für die Bestätigung]
- [von Kunde bestätigen: Umbuchen-Link in der Bestätigungsmail]
