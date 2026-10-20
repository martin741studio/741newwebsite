# Diagnose — Seite „Gespräch buchen“ me&you

Grundlage: v2 `termin.html` (`02-data/v2-termin-first-viewport-1440.png`), Live /sichtbarkeit-termin (`02-data/live-sichtbarkeit-termin-full-1440.png`), `02-data/dataset.md`. Seitentyp: Buchungsseite (Ziel aller CTAs, noindex). Raster nach Workflow 4b angepasst:
- Item 2 (Headline + Stadt) → Headline nennt Ergebnis des Gesprächs, keine Stadt (online).
- Item 9 (erster Termin) → **B2 Ablauf des Gesprächs** (Schritte, Dauer, Kanal, was danach passiert).
- Item 11 (CTA alle 2 Sektionen) → **B1 Kalender im ersten Bildschirm, Rücksprung von jeder Sektion**.
- Item 15, 16, 18 entfallen (keine Situationen, keine Leistungen, kein Ort). Item 22 entfällt (kein Health-Kunde).
- Neu: **B3 Gesprächspartner benannt**, **B4 ablenkungsfrei**, **B5 Rückfallweg Telefon**, **B6 Bestätigungszustand mit nächsten Schritten**, **B7 UTM bis Calendly**, **B8 Verbindlichkeit (Vorbereitung, Umbuchen statt Absagen)**, **B9 keine falschen Angaben zum Buchungstool**.

## Bewertung v2 (termin.html)
| # | Regel | Prio | Score | Beleg |
|---|---|---|---|---|
| 1 | Hero: was, für wen, nächster Schritt in 5 Sekunden | A | 2 | Kicker „Kostenloses Gespräch · 30 Minuten · Online“, H1, Kalender rechts |
| 2 | Headline = Ergebnis des Gesprächs | A | 2 | „Finde heraus, wo du gerade Wirkung verlierst.“ |
| 3 | Sub: was du bekommst, mit wem | A | 1 | „Team von Michael Ehlers“, Rolle der Person fehlt, „Kein Verkaufsdruck“ ist unbelegt |
| B1 | Kalender im ersten Bildschirm, Rücksprung aus jeder Sektion | A | 1 | Kalender im ersten Bildschirm; unten kein Rücksprung, kein Button |
| 6 | Rückversicherung am Kalender | A | 1 | „Zeitzone Berlin · nur die nächsten Tage buchbar“: beides falsch (K1) |
| 7 | Zwei Beweisformen am Kalender | A | 0 | nur Textzeile unter Michael, unter dem Fold |
| B3 | Gesprächspartner benannt (Name, Rolle, Bild) | A | 0 | Rundbild Michael, aber Michael führt das Gespräch nicht (K2) |
| B2 | Ablauf des Gesprächs | A | 1 | drei Schritte, Schritt 2 „Drei kurze Fragen“ gibt es im Formular nicht |
| 10 | Eine CTA-Farbe, Blur-Test | A | 2 | Calendly in Markenblau `64809e`, sonst keine Buttons |
| B4 | Ablenkungsfrei | A | 2 | Header nur Logo, keine Navigation |
| B5 | Rückfallweg Telefon am Kalender | A | 0 | Telefon nur im Footer |
| B6 | Bestätigungszustand mit nächsten Schritten | A | 0 | Calendly-Standard „Du bist eingeplant“ im Rahmen, kein Video, kein WhatsApp-Hinweis |
| B7 | UTM bis Calendly | A | 0 | `CALENDLY` ohne utm, eingehende `utm_source`/`utm_content` gehen verloren (T10) |
| B8 | Verbindlichkeit: Vorbereitung, Umbuchen | B | 2 | „Das bringst du mit.“ + Umbuchen-Satz |
| B9 | Keine falschen Angaben zum Tool | B | 0 | Zeitzone Berlin, Fragen, Buchungsfenster (K1) |
| 12 | Bewertungen offen mit Vorname und Quelle | B | 0 | keine Zitate |
| 13 | Beweis-Überschrift trägt Nutzen | B | 0 | keine |
| 17 | FAQ mit echten Einwänden | B | 1 | 3 Fragen; fehlen: „Muss ich danach buchen?“, Technik, Absage |
| 19 | Abschluss = Mini-Hero | B | 0 | kein Abschluss, Seite endet mit FAQ |
| 20 | Überschriften tragen Aussagen | C | 1 | „Drei Fragen vorab.“ ist Label |
| 21 | Typografie | C | 1 | Zeile unter Michael 12,5 px, blass |

**Summe v2: 17 von 42** (21 Items). Live /sichtbarkeit-termin liegt darunter (kein Ablauf mit Dauer, Laptop-Mockup, grauer Kasten, kein Beweis, kein Telefon am Kalender).

## Muster und Abschnittsplan
Buchungsseiten-Muster: Kalender oben, links nur das Nötigste (was, mit wem, wie lange, was danach), Beweis direkt am Kalender, darunter Einwände, dann zurück zum Kalender. Nach der Buchung derselbe Ort als Bestätigung (Muster P8 im 741 CRO-Raster).
| # | Abschnitt | Job |
|---|---|---|
| S01 | Hero + Kalender | H1, Sub, 3 Häkchen, Gesprächspartner, Kalender rechts, Beweiszeile und Telefon direkt unter dem Kalender |
| S02 | Ablauf | 3 Schritte (freigegebene Startseiten-Copy S07), was du im Gespräch klärst |
| S03 | Wer dich erwartet | Gesprächspartner (Platzhalter), Michael als Leiter der Seminare, 3 Fakten |
| S04 | Stimmen | ProvenExpert-Zeile, 3 offene Zitate |
| S05 | Vorbereitung | 3 Dinge mitbringen, WhatsApp-Hinweis, Umbuchen |
| S06 | FAQ | 6 Einwände: Kosten, Pflicht danach, mit wem, Technik, Absage, lieber anrufen |
| S07 | Abschluss | Copy-Deck-Zeile, Rücksprung zum Kalender, Telefon |
| S08 | Bestätigung (Zustand nach Buchung) | „Dein Termin steht.“, 3 nächste Schritte, Video-Platz Michael |
CTA „Termin wählen“ (Rücksprung zum Kalender) in S01, S02, S04, S06, S07.
