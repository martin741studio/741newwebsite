# OPEN-FLAGS — Gespräch buchen (2026-10-12)

## Entscheidungen zur Buchungsstrecke (Checkpoint 1, Martin)
| # | Punkt | Vorschlag (741) | Wer entscheidet |
|---|---|---|---|
| E1 | Bestätigung nach der Buchung | Zustand auf derselben Seite (S08) über das Calendly-Signal `calendly.event_scheduled`. Links „Dein Termin steht.“ mit 3 nächsten Schritten, rechts zeigt Calendly Datum und Uhrzeit. Keine Änderung an Calendly. Eigene Seite `/gespraech-gebucht` mit Weiterleitung erst, wenn Pauspapier Calendly umstellt | Martin |
| E2 | Drei Pflichtfragen und Buchungsfenster 48 bis 72 h | Seite nennt beides nicht als Tatsache. Schritt 1 trägt nur die gelbe Marke „Fragen eingerichtet“. Umstellung in Calendly macht Pauspapier (wir ändern keine Einstellung). Danach Marke entfernen | Martin, dann Pauspapier |
| E3 | Gesprächspartner | Seite sagt „ein Mitglied aus Michaels Team“. Name, Rolle und Foto vom Kunden. Michael-Foto nur in S03 als „Kopf dahinter“, nie als Gesprächspartner | Kunde |
| E4 | UTM-Weitergabe | Alle 5 UTM-Werte aus der Seiten-URL in die Calendly-URL übernehmen, bevor das Widget lädt. Keine Werte erfinden (kein Standard-utm_medium). Test im Prototyp mit `?utm_source=startseite&utm_content=hero` | Martin |
| E5 | Calendly-Cookie-Banner | v2 blendet es aus (`hide_gdpr_banner=1`). Vorschlag: im Prototyp ausgeblendet lassen, für live nur, wenn die Einwilligung der Website Calendly abdeckt. Sonst Banner zeigen | Martin, Datenschutz Kunde |
| E6 | Telefon | +49 15888367664 (Website), nicht die Nummer aus dem Google-Profil | Martin (gesetzt laut Auftrag) |
| E7 | Video von Michael in S08 | Platz mit gelber Marke, bis Michael das Video (Skript liegt vor, 60 bis 90 s) dreht. Ohne Video fällt Schritt 3 weg | Michael |
| E8 | URL | `/gespraech-buchen`, noindex. Live `/sichtbarkeit-termin` leitet später per 301 hierher (Ads und VSL-Button) | Martin, Pauspapier |

## Inhaltliche Flags
| # | Flag | Stelle | Vorschlag | Wer entscheidet |
|---|---|---|---|---|
| F1 | Umbuchen-Link in der Bestätigungsmail ist Calendly-Standard, im Konto nicht geprüft | S05, S06, S08 | prüfen, sobald Calendly-Zugang da ist | 741 |
| F2 | Erinnerung per WhatsApp: heute manuell durch das Team (24 h vorher, Termintag, 15 min vorher mit Link). Erste WhatsApp kurz nach der Buchung ist geplant, nicht eingerichtet | S05, S08 | S05 nennt nur den heutigen Stand, S08 trägt gelbe Marke | Setter |
| F3 | Video-Tool des Gesprächs unbekannt | S06 | Kunde nennt es | Kunde |
| F4 | v2 nannte „Zeitzone Berlin“ und „nur die nächsten Tage buchbar“. Beides stimmt heute nicht | entfernt | so lassen | Martin |
| F5 | „Kein Verkaufsdruck“ (v2) ist eine Zusage ohne Beleg | ersetzt durch „Ob und wann du buchst, entscheidest du danach.“ | so lassen | Martin |
| F6 | Ad verspricht Training, Seite ein Gespräch (Funnel-Check 06.10.) | ganze Seite sagt klar „Gespräch“ | Ad-Abgleich bei Pauspapier | Pauspapier |
