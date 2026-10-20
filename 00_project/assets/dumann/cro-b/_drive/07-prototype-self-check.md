# Self-Check — Startseite Dumann Track B, Prototyp v1

Raster 741 CRO-Raster (22 Items, strenge Skala). Bestehen: gesamt ≥ 36 von 44, alle Prio A = 2 oder durch Branchenregel oder fehlende Daten begründet. Vorher = Live-Seite (Diagnose Track A).

| # | Regel | Prio | Jetzt | Beleg |
| --- | --- | --- | --- | --- |
| 1 | Hero in 5 Sekunden | A | 2 | H1 mit Berufsbild, Bezirk und Hildegard-Heilkunde, Sub, Button, Portrait |
| 2 | Headline = Ergebnis + Stadt | A | 1 | Stadt und Fach stehen in der H1, ein Ergebnis nicht. Grund: HWG verbietet Wirkversprechen. Begründete Ausnahme |
| 3 | Sub-Headline Situation zuerst | A | 1 | Die Sub nennt Themen ("Verdauung, Erschöpfung, Schilddrüse, Hormonen"), keine erlebte Situation. Situationsworte hätten Krankheitsbezug (HWG). Begründete Ausnahme |
| 4 | CTA im ersten Bildschirm | A | 2 | Unterkante 616 px bei 757 px Höhe (Bewertungszeile darunter bis 656 px) |
| 5 | CTA-Text Schritt + Nutzen | A | 1 | "Termin buchen" nennt den Schritt, keinen Nutzen. Text ist von Martin freigegeben (Track A) |
| 6 | Rückversicherung unter dem CTA | A | 2 | Die Bewertungszeile "5,0 ★ bei 9 Google Bewertungen" steht direkt unter den Buttons (Prüfer-Hinweis behoben); Button-Unterkante 616 px, Zeile darunter bis 656 px, beides im ersten Bildschirm |
| 7 | Zwei Beweisformen above the fold | A | 2 | Google-Bewertung 5,0 bei 9 und "seit 2002" (Eyebrow, Schreibschrift) |
| 8 | Gesicht und Qualifikation | A | 2 | echtes Portrait, Namensschild "Heilpraktikerin", "seit 2002" |
| 9 | Erster Termin: Schritte, Dauer, Preis | A | 2 | vier Schritte, 60 Minuten, 220 € und 150 €, GebüH |
| 10 | Eine CTA-Farbe, Blur-Test | A | 2 | Oliv nur für Buchung; Blur-Test in Chrome bestanden |
| 11 | CTA mindestens alle 2 Sektionen | A | 2 | Hero, 3, 5, 6, 7, 9, 10 und Kopf |
| 12 | Bewertungen offen | B | 2 | drei offene Karten, Vorname, Google-Zeichen, Überschrift |
| 13 | Beweis-Überschrift trägt Nutzen | B | 1 | "5,0 Sterne bei 9 Google Bewertungen" ist eine Zahl ohne Nutzen |
| 14 | 3 bis 4 Beweisblöcke | B | 2 | Beweis-Leiste, Über Daniela mit Zeile, Bewertungen, Abschlusszeile |
| 15 | Situationen-Sektion | B | 1 | fünf Themen als "Begleitung bei", HWG-sauber, aber keine erlebten Situationen, Themen von der Kundin noch nicht bestätigt |
| 16 | Leistungen mit Nutzen-Überschrift und Link | B | 1 | sechs Zeilen mit Link je Zeile, aber alle Links sind `#`; die Titel sind nach der HWG-Korrektur Leistungsnamen, keine Nutzen-Überschriften |
| 17 | FAQ mit echten Einwänden | B | 1 | Kosten, Kasse, Vorbereitung, Hausbesuch; Absage fehlt ([FEHLT], Kundin) |
| 18 | Standort | B | 1 | Adresse, Lage, ÖPNV, Auto; Karte nur Platzhalter, Parken und Barrierefreiheit fehlen |
| 19 | Abschluss = Mini-Hero | B | 2 | Überschrift, Text, drei Haken (Bewertung, seit 2002, Erstgespräch), Button und Telefon |
| 20 | Überschriften mit Aussage | C | 1 | "Fragen vor dem ersten Termin" und "So finden Sie zu mir" beschreiben nur |
| 21 | Typografie und Hierarchie | C | 2 | H1 58 px, Body 17 px (3,4 ×), Body ≥ 16 px gemessen |
| 22 | HWG-Check | A | 2 | kein Heilversprechen, keine Krankheitsliste, kein Vorher-Nachher, Hinweisbox in Sektion 4 und Fuß (Fuß ergänzt, "schulmedizinisch nicht allgemein anerkannt"), Bach-Zitat entfällt, Hildegard-Zitat ohne Gesundheitsaussage. Prüfer-Funde "Entgiftung", "für mehr Wohlbefinden", "Belastungen sichtbar machen" gestrichen |

**Summe: 35 von 44.** Das Bestehenskriterium (36) ist um einen Punkt verfehlt, weil Daten der Kundin fehlen (Items 15, 17, 18) und zwei Prio-A-Items durch Branchenregel oder Martins Freigabe bei 1 bleiben. Erste Fassung 36, ein frischer Prüfer hat 6 auf 2 gehoben (Fix) und 15, 16 auf 1 gesenkt. Prio A unter 2: Item 2 und 3 (HWG verbietet Ergebnis und Krankheitssituation), Item 5 (Text "Termin buchen" ist von Martin freigegeben). Martin hat den Prototyp trotzdem freigegeben (2026-10-11).

## Track-B-Bedingungen
1. Eine Signature-Idee: Viriditas-Faden, nur Code, getestet (Pfadlänge 8270, Dash-Versatz von 7829 am Seitenanfang auf 0 am Ende, 48 Blätter bei 8.283 px Seitenhöhe, die Zahl hängt von der Seitenhöhe ab, Blüte am Ende).
2. Eine Bewegung je Sektion (Ausnahmen in `motion.md`) und höchstens vier Komponenten: Faden, Bild-Vorschau-Liste, haftender Titel mit Schrittlinie, Farbwechsel des Kopfes zum Abschlussband.
3. Nur Elemente mit "ja" von Martin (E01, E03, E04, E05, E07, E09, E11, E12, E13, E17 bis E22, E24, E25, E27 bis E30). Kein "nein" und keine Stimmenlosen eingebaut.
4. Performance-Budget eingehalten (`perf.md`), Reduced Motion und X-ray getestet (`visual-check.md`).

## Grauzonen für Martin (HWG)
Die Track-A-Leistungsnamen "Ausleitung und Entgiftung", "für mehr Wohlbefinden" und "Mineralstoffe und Belastungen sichtbar machen" wurden nach dem Prüfer gestrichen (Wirk- und Diagnoseaussagen). Martin kann sie zurückholen. "Heilkunde" in "Hildegard-Heilkunde" ist der Eigenname der Methode. Die Bewertungen betreffen Kurse und Lehre (im Prototyp markiert). Offen: Preis der Erstanamnese bei Homöopathie steht in FAQ 1.
