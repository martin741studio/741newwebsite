# Self-Check — Seminarseite me&you / Michael Ehlers, Prototyp v1 (2026-10-12)

Raster: 741 CRO-Raster, angepasst nach Workflow 4b (Item 15 = Formate vergleichbar), Item 22 entfällt. Bestehen: gesamt ≥ 34 von 42, alle Prio A = 2 oder begründet. Vorher = Vorschau v2 (`../03-diagnosis/diagnosis.md`).

| # | Regel | Prio | Vorher | Jetzt | Beleg |
|---|---|---|---|---|---|
| 1 | Hero in 5 Sekunden: was, für wen, nächster Schritt | A | 1 | 1 | Was (drei Seminare + Bundle, 3 + 1 Tage, ≤ 14 Menschen) und nächster Schritt klar. „Für wen“ steht erst in S02 (Einstieg) und S09. Begründung: freigegebene Copy, Hero-Text nicht ändern |
| 2 | Headline = Ergebnis + Ort/Keyword | A | 0 | 1 | Keyword im H1 („Rhetorik-Seminare mit Michael Ehlers“), große Zeile ist die freigegebene Copy-Deck-Zeile ohne Ergebnis und Ort. Orte im Hero-Link „Termine ansehen“ und S08 |
| 3 | Sub-Headline: Situation, dann Hilfen | A | 0 | 1 | Hilfen konkret (Einstieg frei sprechen, Schlagfertigkeit, Führung, 3 + 1 Tage, kleine Gruppe), keine Situation. Begründung wie 1 |
| 4 | CTA im ersten Bildschirm | A | 1 | 2 | Unterkante Hero-Button 643 px bei 1500 × 807 (Chrome, gemessen) |
| 5 | CTA-Text: Schritt + Nutzen | A | 1 | 1 | „Gespräch buchen“ (Copy Deck: gleicher Button überall). Nutzen in der Zeile darunter („Du klärst, welches Seminar zu dir passt.“) |
| 6 | Rückversicherung unter dem CTA | A | 0 | 2 | „30 Minuten, kostenlos, per Video. …“ (S01), „Das Gespräch kostet nichts.“ (S10), Häkchen S12 |
| 7 | Zwei Beweisformen above the fold | A | 0 | 2 | ProvenExpert 227 von 250 mit 5 Sternen + über 8.000 Teilnehmer + echtes Foto Michael |
| 8 | Gesicht + Qualifikation | A | 0 | 2 | echtes Foto Michael statt KI-Trainer; 8.000 Teilnehmer im Hero, 30 Jahre + ERFOLG in S09 |
| 9 | Erster Schritt: Ablauf, Dauer, Preis | A | 0 | 2 | S10: 3 Schritte, 30 Minuten, kostenlos, per Video; Person `[FEHLT]` markiert |
| 10 | Eine CTA-Farbe, Blur-Test | A | 1 | 2 | #4F6D90 nur gefüllt auf Buttons; `screenshots/blur-test-first-viewport.png` |
| 11 | CTA mindestens alle 2 Sektionen | A | 1 | 2 | Buttons in S01, S03, S04 (je Karte), S06, S08, S10, S12 + Header; nie zwei Sektionen ohne Button hintereinander |
| 12 | Bewertungen offen, Name + Quelle + Überschrift | B | 0 | 1 | 4 offene Karten mit Überschrift, Sternen, Name, Seminar, Ort, Quelle. Quelle als Text, kein ProvenExpert-Logo an der Karte |
| 13 | Beweis-Überschrift trägt Nutzen | B | 0 | 2 | „Was Teilnehmer aus den Seminaren mitnehmen“ |
| 14 | 3–4 Beweisblöcke, einer am Kontakt | B | 0 | 2 | S01 Bewertungszeile, S02 Kacheln + Zitat + Medien, S07 Stimmen + Videos, S09 ERFOLG, S12 Bewertungszeile |
| 15 | Formate vergleichbar | B | 1 | 2 | Karten mit Inhalt, für wen, Plätzen, Orten, Daten; Vergleichstabelle S05; Bundle-Daten `[FEHLT]` |
| 16 | Leistungen als Karten mit Nutzen-Überschrift + Link | B | 1 | 2 | „Ruhig bleiben, wenn es eng wird“, „Mit Sprache führen“, Einstieg als Feature; je Button |
| 17 | FAQ mit echten Einwänden | B | 0 | 2 | 9 Fragen: Reihenfolge, Anfänger, Führungskräfte, Preis, Gruppen, Übernachtung, Storno |
| 18 | Orte und Termine | B | 1 | 2 | 6 Ortskarten mit Seminar und allen Daten; Daten zusätzlich je Format |
| 19 | Abschluss = Mini-Hero | B | 1 | 2 | Headline, 3 Häkchen, Bewertungszeile, Button, Telefon, Link Startseite |
| 20 | Überschriften tragen Aussagen | C | 1 | 2 | keine Platzhalter-Überschriften mehr; „Häufige Fragen zu den Rhetorik-Seminaren“ als Keyword-Ausnahme |
| 21 | Typografie | C | 1 | 2 | H1 56 px / Body 18 px; Text ≥ 16 px (Labels und Tabellenköpfe 14 px, gelbe Marken 15 px) |
| 22 | (Health/Recht) | – | n/a | n/a | entfällt |

**Summe: 37 von 42** (vorher 11 von 42). Prio A: 7 von 11 auf 2. Items 1, 2, 3 und 5 bleiben bei 1, weil der Hero-Text und der Button-Text freigegebene Copy (Copy Deck + Checkpoint 1) sind. Abgefedert durch Kicker-H1 mit Keyword, Rückversicherung unter dem Button und die Kurz-Antwort in S02. Entscheidung bei Martin: ein Satz „Für Führungskräfte, Gründer und Berater, …“ im Hero würde 1 und 3 auf 2 heben.

## Done-Bedingungen
1. Jedes Item 2 oder begründet: ja.
2. CTA im ersten Bildschirm: ja (643 px).
3. CTA alle 2 Sektionen: ja.
4. Erste 3 Sektionen: was (S01), für wen und erster Schritt (S02), wo (S01-Link, S03 Termine), warum vertrauen (S01, S02): ja.
5. Jeder Fakt in `claims.json` oder `[FEHLT]`: ja (G1 PASS, Prototyp-Text = freigegebene Copy, Abweichungen nur Footer und Videolängen).
6. Belege geprüft (UWG): ja, Lernziele statt Versprechen, keine Google-Bewertung.
7. Checkpoints: Copy freigegeben (12.10.), Prototyp offen (Checkpoint 2).
