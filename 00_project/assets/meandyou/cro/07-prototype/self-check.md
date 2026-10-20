# Self-Check — Startseite me&you / Michael Ehlers, Prototyp v1 (2026-10-12)

Raster: 741 CRO-Raster, Item 22 entfällt (kein Health-/Rechtskunde). Bestehen: gesamt ≥ 34 von 42, alle Prio A = 2 oder begründet. Vorher = Entwurf A (`03-diagnosis/diagnosis.md`).

| # | Regel | Prio | Vorher | Jetzt | Beleg |
|---|---|---|---|---|---|
| 1 | Hero in 5 Sekunden: was, für wen, nächster Schritt | A | 1 | 2 | Kicker „Rhetorik-Seminar mit Michael Ehlers“, Headline, „Drei Tage Intensivtraining in kleiner Gruppe“, Button „Gespräch buchen“ |
| 2 | Headline = Ergebnis + Ort | A | 1 | 1 | Ergebnis und Keyword im H1, aber kein Ort. Begründung: kein lokaler Betrieb, 6 wechselnde Seminarorte; Orte stehen in S02 (Satz 3) und S09. Ein Ort im H1 würde die freigegebene Headline ändern |
| 3 | Sub-Headline: Situation, dann 3–4 Hilfen | A | 1 | 2 | „… die fachlich längst überzeugen und trotzdem nicht gehört werden. Drei Tage Intensivtraining in kleiner Gruppe, mit Videoanalyse und Sofort-Feedback.“ |
| 4 | CTA im ersten Bildschirm | A | 2 | 2 | Unterkante Hero-Button 649 px bei 1386 × 773 (Chrome, gemessen) |
| 5 | CTA-Text: Schritt + Nutzen | A | 1 | 1 | Button „Gespräch buchen“ (Copy Deck: gleicher Wortlaut auf jedem Button, Kundenvorgabe). Nutzen steht in der Zeile direkt darunter („Du klärst, welches Seminar zu dir passt.“) |
| 6 | Rückversicherung unter dem CTA | A | 0 | 2 | „30 Minuten, kostenlos, per Video. …“ in S01, S03, S07; Häkchen in S11 |
| 7 | Zwei Beweisformen above the fold | A | 1 | 2 | Bewertungszeile (250 ProvenExpert, 4,8 Google) + 8.000 Teilnehmer + 30 Jahre im Hero |
| 8 | Gesicht + Qualifikation im Hero | A | 2 | 2 | echtes Foto Michael (Magazin), „seit über 30 Jahren“ |
| 9 | Erster Schritt: Schritte, Dauer, Preis | A | 1 | 2 | S07: 3 Schritte, 30 Minuten, kostenlos; Person `[FEHLT]` sichtbar markiert |
| 10 | Eine CTA-Farbe, Blur-Test | A | 1 | 2 | #4F6D90 nur gefüllt auf Buttons (weiß 5,35 : 1); `screenshots/blur-test-first-viewport.png`: nur die zwei Buttons stechen heraus |
| 11 | CTA mindestens alle 2 Sektionen | A | 1 | 2 | „Gespräch buchen“ in S01, S03, S04, S06, S07, S08, S09, S11 + Header |
| 12 | Bewertungen offen, Vorname + Quelle + Überschrift | B | 1 | 1 | 6 offene Karten mit Überschrift, Name, Quelle, Sternen. Quelle als Text („Google“, „ProvenExpert“), kein Google-Logo (nur echte Logos; Google-Marke nicht als Datei vorhanden) |
| 13 | Beweis-Überschrift trägt Nutzen | B | 1 | 1 | „Was Teilnehmer über das Seminar schreiben“ (freigegeben, wahr, aber ohne Nutzen-Aussage) |
| 14 | 3–4 Beweisblöcke, einer am Kontakt | B | 1 | 2 | S02 Beweis-Leiste, S04 Zahlen, S08 Stimmen + Videos, S11 Bewertungszeile |
| 15 | Situationen + Weg hinaus | B | 1 | 2 | 3 Karten + „Der gemeinsame Punkt …“ + Für-wen-Liste + Button |
| 16 | Leistungen als Karten mit Link | B | 1 | 2 | 3 Format-Karten mit Bild, Themen-Überschrift, Link |
| 17 | FAQ, Preis zuerst | B | 0 | 2 | 12 Fragen, Preis zuerst, Akkordeon, eine offen |
| 18 | Standort | B | 0 | 1 | angepasst: 6 Orte mit Bild, Format und Daten; keine Karte, kein Parken (wechselnde Seminarorte, Firmensitz im Footer) |
| 19 | Abschluss = Mini-Hero | B | 1 | 2 | Headline, 3 Häkchen, Bewertungszeile, Button, Telefon |
| 20 | Überschriften tragen Aussagen | C | 1 | 2 | alle H2 mit Aussage; „Häufige Fragen zum Rhetorik-Seminar“ als Keyword-Ausnahme (Copy-Regel C5.1) |
| 21 | Typografie | C | 1 | 2 | H1 56 px / Body 18 px = 3,1 ×; Text ≥ 16 px (Labels 14 px, FEHLT-Marken 15 px) |
| 22 | (Health/Recht) | – | n/a | n/a | entfällt |

**Summe: 37 von 42** (vorher 20 von 42). Prio A: 9 von 11 auf 2. Items 2 und 5 bleiben bei 1 wegen Kundenvorgaben (freigegebene Headline ohne Ort, einheitlicher Button-Text laut Copy Deck); beide sind über die Zeile darunter bzw. S02/S09 abgefedert. Entscheidung bei Martin.

## Done-Bedingungen (Workflow Abschnitt 0)
1. Jedes Item 2 oder begründet: ja (2, 5, 12, 13, 18 begründet).
2. CTA im ersten Bildschirm: ja (649 px).
3. CTA alle 2 Sektionen: ja.
4. Erste 3 Sektionen beantworten für wen, was, erster Schritt, wo, warum vertrauen: ja (Hero, Beweis-Leiste mit Orten und erstem Schritt, Situationen).
5. Jeder Fakt in `dataset.md` / `claims.json` oder `[FEHLT]`: ja (G1 PASS, Prototyp-Text = freigegebene Copy, 0 Abweichungen außer erlaubter Liste).
6. Heilversprechen: entfällt (kein Health). Belege geprüft (UWG): ja.
7. Martin hat Checkpoints freigegeben: Copy ja (2026-10-11), Prototyp offen (Checkpoint 2).
