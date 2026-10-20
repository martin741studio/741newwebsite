# Self-Check — Startseite STÜRZL Steuerstrafrecht, Prototyp v1

Raster 741 CRO-Raster (22 Items, strenge Skala). Bestehen: gesamt ≥ 36 von 44, alle Prio A = 2 oder durch fehlende Kundendaten oder Berufsrecht begründet. Vorher = Live-Seite aus `03-diagnosis/diagnosis.md`.

| # | Regel | Prio | Vorher | Jetzt | Beleg |
| --- | --- | --- | --- | --- | --- |
| 1 | Hero in 5 Sekunden | A | 0 | 2 | H1 mit Fachgebiet und beiden Städten, Sub mit Situationen, Button, Foto (`prototype-first-viewport-1440.png`) |
| 2 | Headline = Ergebnis + Stadt | A | 0 | 1 | Fachgebiet und Städte stehen in der H1, ein "gefühltes Ergebnis" nicht. Grund: BRAO § 43b und BORA § 6 verbieten Ergebnisversprechen. Begründete Ausnahme |
| 3 | Sub-Headline Situation zuerst | A | 0 | 2 | "Ein Ermittlungsverfahren, eine Selbstanzeige, eine Durchsuchung, eine Prüfung im Unternehmen: …" |
| 4 | CTA im ersten Bildschirm | A | 1 | 2 | Unterkante 636 px bei 801 px Höhe (Chrome gemessen) |
| 5 | CTA-Text Schritt + Nutzen | A | 1 | 2 | "Vertraulich anfragen" nennt Schritt und Nutzen |
| 6 | Rückversicherung unter dem CTA | A | 0 | 1 | Vertraulichkeit und "nur Ihr Thema" stehen darunter, die Reaktionszeit fehlt ([FEHLT], Kunde) |
| 7 | Zwei Beweisformen above the fold | A | 0 | 2 | Bewertungszeile (Google und anwalt.de) plus Namensschild mit Titel. anwalt.de-Freigabe offen |
| 8 | Gesicht und Qualifikation | A | 1 | 2 | echtes Foto, Namensschild "Dr. Anja Stürzl LL.M., Fachanwältin für Steuerrecht" (Titel bestätigt) |
| 9 | Erster Termin: Schritte, Dauer, Preis | A | 1 | 1 | vier Schritte; Dauer und Preis [FEHLT] (Kunde) |
| 10 | Eine CTA-Farbe, Blur-Test | A | 0 | 2 | #4E6F55 überall; Blur-Test in Chrome bestanden |
| 11 | CTA mindestens alle 2 Sektionen | A | 1 | 2 | Hero, 3, 5, 6, 7, 10, 11 und Kopf |
| 12 | Bewertungen offen | B | 0 | 2 | drei offene Karten, Initial, Google-Zeichen, Überschrift |
| 13 | Beweis-Überschrift trägt Nutzen | B | 0 | 2 | "Verständlich erklärt, ernst genommen: Das schreiben Mandanten" |
| 14 | 3 bis 4 Beweisblöcke | B | 0 | 2 | Beweis-Leiste, Über Dr. Stürzl, Bewertungen, Abschluss-Zeile |
| 15 | Situationen-Sektion | B | 0 | 2 | zwei Mandantengruppen mit je vier Situationen; Anwaltswerbe-Check sauber |
| 16 | Leistungen als Karten mit Link | B | 1 | 1 | sechs Karten mit Link; Titel sind Leistungsnamen, keine Nutzen-Überschriften; Links `#` |
| 17 | FAQ mit echten Einwänden | B | 0 | 1 | sechs Fragen, Kosten zuerst; Antworten sind Platzhalter bis die Kanzlei liefert |
| 18 | Standort | B | 1 | 1 | zwei Karten mit Adresse, Telefon, Zeiten; Karte nur Platzhalter, Parken fehlt ([FEHLT]) |
| 19 | Abschluss = Mini-Hero | B | 0 | 2 | Überschrift, Haken, Beweis, Formular, Telefon, E-Mail |
| 20 | Überschriften mit Aussage | C | 0 | 1 | Die meisten H2 sind Aussagen. "In vier Schritten zum ersten Gespräch" und "Zwei Büros: Frankfurt und München" beschreiben nur (Prüfer 2026-10-11) |
| 21 | Typografie und Hierarchie | C | 1 | 2 | H1 54 px, Fließtext 18 px (3,0 ×), Body ≥ 16 px gemessen |
| 22 | Anwaltswerbe-Check | A | 1 | 2 | Grep und Text-Check: kein "spezialisiert", "Experte", Ergebnisversprechen, Superlativ; Titel bestätigt; Bewertungen ohne Falldetail. Prüfer fand "damit aus einer Unsicherheit kein Verfahren wird" (F5) und "ist darauf eingerichtet, schnell zu reagieren" (F3): gestrichen, "Ansprechpartnerin" in der Überschrift ersetzt |

**Summe: 37 von 44** (vorher 10 von 44). Erste Fassung 38; ein frischer Prüfer hat Item 20 auf 1 gesetzt.
Prio A mit Score unter 2: Item 2 (Berufsrecht), Item 6 und Item 9 (fehlende Daten der Kanzlei). Alle drei sind begründet.

## Done-Bedingungen (Workflow Abschnitt 0)
1. Alle Fakten im Dataset oder `[FEHLT]`: ja (`verify.py`, Abschnitt 10 des Datasets).
2. Anwaltswerbe-Check bestanden: ja, mit Grauzonen für Martin (Notfallnummern, anwalt.de, Bewertungen als Werbung, FAQ F3 und F4).
3. Text gleich approved copy: ja (M11, 0 Abweichungen).
4. Visual check in Chrome: ja, `visual-check.md`.
5. Strenger Gegencheck durch frischen Prüfer: ja, 12 Lücken gemeldet und behoben (siehe `visual-check.md` Abschnitt "Prüfer").
6. Prototyp lokal, nichts hochgeladen: ja.
7. Handoff mit `[FEHLT]`-Liste: siehe `08-handoff/handoff.md`.
