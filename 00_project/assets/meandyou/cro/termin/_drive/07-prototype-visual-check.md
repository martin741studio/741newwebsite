# Visual Check in Chrome — „Gespräch buchen“, Prototyp v1 (2026-10-12)
Setup: `python3 -m http.server 8818`, Claude in Chrome (eigener Tab), Fenster 1440 × 900 = Viewport 1440 × 757. Seite oben bis unten in 700-px-Schritten, echter Calendly-Kalender geladen. Keine Buchung abgeschickt, keine Calendly-Einstellung geändert.

| # | Ergebnis | Wert |
|---|---|---|
| M1 | ok (Höhe notiert) | 1440 × 757 |
| M2 | ok | keine horizontale Scrollleiste |
| M3 | ok | keine Konsolenfehler |
| M4 | ok | 0 kaputte, hochskalierte oder verzerrte Bilder |
| M5 | ok | Inter, Libre Baskerville geladen |
| M6 | ok | 0 fehlende Anker, 0 „#“, tel:+4915888367664, extern nur meandyou.de (Rechtliches) |
| M7 | ok | 0 unsichtbare Elemente nach dem Scroll |
| M8 | ok | Kalender-Oberkante 104 px, Beweiszeile 185 px, H1-Unterkante 341 px (alles im Bildschirm 701 px) |
| M9 | fixed | Beweiszeile und Zeilen unter dem Kalender waren 14,5 bis 15,5 px → 15 bis 16 px; Rest unter 16 px nur Labels, Quellen, gelbe Marken |
| M10 | ok, Abweichung | 1 atmender Button (Abschluss). Hero-CTA ist der Kalender selbst |
| M11 | fixed | Fakten-Chips „über 8.000 Teilnehmer“ standen nicht wörtlich in der Copy → entfernt. Rest: Footer, Ladehinweis, FAQ-Nummern, Prototyp-Schild |
| UTM | ok | `?utm_source=startseite&utm_content=hero` → beide im iframe; alle 5 UTM-Werte → 5 von 5; ohne UTM → keine utm-Werte |
| Sprung „Termin wählen“ | ok | Klick in S06 → Kalender-Oberkante 96 px, URL behält die UTM-Werte |
| Datum klicken | ok | 13.10. zeigt Uhrzeiten 16:00 bis 18:00 im Kalender; nicht gebucht |
| Bestätigungszustand | fixed | `?booked=1` schaltete nicht (Inline-Style) → Klasse; jetzt links „Dein Termin steht.“ mit 3 Schritten |
| Kalenderkarte | fixed | Klasse `.book` kollidierte mit dem Design-System (dunkle Karte) → `.bkc` |
| Overline | fixed | brach in 2 Zeilen → eine Zeile |
| FAQ | fixed | Reihenfolge jetzt spaltenweise 1 bis 3 links, 4 bis 6 rechts wie Mockup |
| ProvenExpert-Logo | fixed | zu klein → 30 px (Karte), 40 px (S04) |
| Mit wem du sprichst | ok | Platzhalter-Avatar gelb, echtes Foto Michael, Text „nicht dabei“ |
| Stimmen, Vorbereitung, Abschluss, Footer | ok | 3 offene Karten, 3 Kärtchen, Navy-Band, Footer ohne Menü |
| Vergleich Mockup | ok mit Abweichung | Beweiszeile oben in der Kalenderkarte statt unten (Regel 701 px), sonst Reihenfolge und Aufbau gleich |

## Offen
1. Calendly zeigt „Wählen Sie einen Tag aus“ (Sie-Form, Sprache des Calendly-Kontos). Ändern nur in Calendly (Pauspapier).
2. Am 12.10. waren nur 12. bis 15.10. buchbar. Das Buchungsfenster ist offenbar schon kurz. Bitte bei Pauspapier bestätigen, dann gelbe Marke prüfen.
3. Name, Rolle und Foto der Person im Gespräch, Video von Michael, Umbuchen-Link, Video-Tool, erste WhatsApp (gelb, siehe OPEN-FLAGS).

**Visual check done in Chrome, 22 items checked, 8 fixed, 3 open.**
