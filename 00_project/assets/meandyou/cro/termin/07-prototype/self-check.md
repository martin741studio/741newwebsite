# Self-Check — „Gespräch buchen“ me&you, Prototyp v1 (2026-10-12)

Raster: 741 CRO-Raster für Buchungsseite (Workflow 4b, siehe `03-diagnosis/diagnosis.md`). Vorher = v2 `termin.html`.

| # | Regel | Prio | Vorher | Jetzt | Beleg |
|---|---|---|---|---|---|
| 1 | Hero: was, für wen, nächster Schritt in 5 Sekunden | A | 2 | 2 | Overline „Kostenloses Gespräch · 30 Minuten · per Video“, H1, Kalender rechts |
| 2 | Headline = Ergebnis des Gesprächs | A | 2 | 2 | „Gespräch buchen:“ + „Finde heraus, wo du gerade Wirkung verlierst.“ |
| 3 | Sub: was du bekommst, mit wem | A | 1 | 2 | Body + 3 Häkchen + Zeile „Mitglied aus Michaels Team“ (Name gelb) |
| B1 | Kalender im ersten Bildschirm, Rücksprung | A | 1 | 2 | Kalender-Oberkante 104 px (Chrome 1440 × 757); 4 Buttons springen zu `#kalender` (gemessen: Oberkante 96 px nach Klick) |
| 6 | Rückversicherung am Kalender | A | 1 | 2 | Zeitzone, Grund für Handynummer, Telefon, Datenschutz; keine falsche Angabe mehr |
| 7 | Zwei Beweisformen am Kalender | A | 0 | 2 | ProvenExpert-Logo + Sterne + „227 von 250 … · seit 1990“ in der Kalenderkarte, Unterkante 185 px |
| B3 | Gesprächspartner benannt | A | 0 | 1 | Rolle klar, Michael ausdrücklich nicht im Gespräch; Name und Foto gelb (Kunde) |
| B2 | Ablauf des Gesprächs | A | 1 | 2 | S02 drei Schritte + „Im Gespräch klärst du“; Fragen im Formular gelb |
| 10 | Eine CTA-Farbe, Blur-Test | A | 2 | 2 | `screenshots/blur-test-first-viewport.png`; Calendly-Akzent auf #4F6D90 gesetzt |
| B4 | Ablenkungsfrei | A | 2 | 2 | Header nur Logo + Telefon, Footer nur Rechtliches + Kontakt |
| B5 | Rückfallweg Telefon am Kalender | A | 0 | 2 | unter der Karte, im Header, S06, S07, S08 |
| B6 | Bestätigungszustand | A | 0 | 2 | S08 über `calendly.event_scheduled`, Vorschau `?booked=1` (`screenshots/booked-*.png`) |
| B7 | UTM bis Calendly | A | 0 | 2 | Chrome-Test: 5 von 5 UTM-Werten im iframe; ohne UTM keine erfundenen Werte |
| B8 | Verbindlichkeit | B | 2 | 2 | S05 Vorbereitung, Umbuchen statt verfallen lassen |
| B9 | Keine falschen Angaben zum Tool | B | 0 | 2 | Zeitzone Berlin, Buchungsfenster und „Drei kurze Fragen“ entfernt bzw. gelb |
| 12 | Bewertungen offen, Vorname, Quelle | B | 0 | 2 | 3 Karten, kein Laufband |
| 13 | Beweis-Überschrift trägt Nutzen | B | 0 | 1 | „Was Teilnehmer nach dem Seminar schreiben“ beschreibt, verkauft nicht |
| 17 | FAQ mit echten Einwänden | B | 1 | 2 | Kosten, Pflicht danach, mit wem, Technik, Absage, Telefon |
| 19 | Abschluss = Mini-Hero | B | 0 | 1 | Headline, Zeile, Button, Telefon; kein Beweis im Abschluss (Copy Deck Block 08) |
| 20 | Überschriften tragen Aussagen | C | 1 | 1 | „Mit wem du sprichst“ und FAQ-Überschrift sind eher Labels |
| 21 | Typografie | C | 1 | 2 | Text ≥ 16 px; 14 bis 15 px nur Labels, Quellen, gelbe Marken, Datenschutz-Zeile |

**Summe: 38 von 42** (vorher 17). Prio A: 12 von 13 auf 2; B3 = 1, weil Name und Foto vom Kunden fehlen.
