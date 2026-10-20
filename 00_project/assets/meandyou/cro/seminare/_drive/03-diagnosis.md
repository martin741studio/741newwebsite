# Diagnose — Seminarseite me&you / Michael Ehlers

Grundlage: Vorschau v2 `https://clients.741.studio/meandyou/v2/seminare.html` (`02-data/v2-seminare-first-viewport-1440.png`, Messung in Chrome), `02-data/dataset.md`.
Raster: 741 CRO-Raster (`~/.claude/skills/cro-homepage/` scorecard), angepasst nach Workflow 4b. Die Seminarseite ist laut Copy Deck „the money page“, deshalb gelten die Entry-Page-Items weiter. Item 15 (Situationen) ist durch ein Seitentyp-Item ersetzt: **Formate vergleichbar**. Item 22 entfällt (kein Health/Recht). Bestehen: alle Prio A = 2 oder begründet, gesamt mindestens 34 von 42.

## 1. Bewertung der aktuellen Seite (v2)
| # | Regel | Prio | Score | Beleg |
|---|---|---|---|---|
| 1 | Hero in 5 Sekunden: was, für wen, nächster Schritt | A | 1 | „Seminare“ + „Ein Einstieg. Dann dein eigener Weg.“ Was genau (Rhetorik, 3 Tage, kleine Gruppe), für wen und der nächste Schritt fehlen |
| 2 | Headline = Ergebnis + Ort/Keyword | A | 0 | kein Keyword, kein Ergebnis, kein Ort |
| 3 | Sub-Headline: Situation, dann Hilfen | A | 0 | „Kein Stufenmodell mehr …“ erklärt die alte Struktur, die neue Besucher nicht kennen |
| 4 | CTA im ersten Bildschirm | A | 1 | nur der Header-Button; im Hero kein Button |
| 5 | CTA-Text: Schritt + Nutzen | A | 1 | „Gespräch buchen“, keine Zeile mit Nutzen |
| 6 | Rückversicherung unter dem CTA | A | 0 | nirgends „30 Minuten, kostenlos“ |
| 7 | Zwei Beweisformen above the fold | A | 0 | keine Bewertung, keine Zahl im Hero |
| 8 | Gesicht + Qualifikation | A | 0 | KI-Bild eines Trainers, der Michael ähnelt (K7); keine Qualifikation |
| 9 | Erster Schritt: Ablauf, Dauer, Preis | A | 0 | Abschluss sagt nur „Der nächste Schritt ist ein Gespräch.“ |
| 10 | Eine CTA-Farbe, Blur-Test | A | 1 | Button #7E99B6 wie v2-Startseite, weiße Schrift 2,95 : 1, schwach |
| 11 | CTA mindestens alle 2 Sektionen | A | 1 | Sektionen 4, 5, 6 hintereinander ohne Button |
| 12 | Bewertungen offen, Name + Quelle + Überschrift | B | 0 | keine einzige Bewertung |
| 13 | Beweis-Überschrift trägt Nutzen | B | 0 | kein Beweisblock |
| 14 | 3–4 Beweisblöcke, einer am Kontakt | B | 0 | keiner |
| 15 | **Formate vergleichbar** (Inhalt, für wen, Plätze, Orte, Termine je Format) | B | 1 | Stichworte und Plätze je Format; für wen, Orte und Termine je Format fehlen; Namen sind Platzhalter |
| 16 | Leistungen als Karten mit Nutzen-Überschrift + Link | B | 1 | Karten mit Button, Überschrift „[Seminar B]“ ohne Nutzen |
| 17 | FAQ mit echten Einwänden | B | 0 | keine FAQ |
| 18 | Orte und Termine | B | 1 | 6 Orte mit Monaten, keine Daten; Mallorca mit September (K2) |
| 19 | Abschluss = Mini-Hero | B | 1 | Headline + Button, keine Häkchen, kein Beweis, kein Telefon |
| 20 | Überschriften tragen Aussagen | C | 1 | H2 „[Seminar A]“ ist Platzhalter; „Drei Tage, zwölf Menschen“ stimmt nicht (K5) |
| 21 | Typografie | C | 1 | 66 Textstellen unter 16 px |
| 22 | (Health/Recht) | – | n/a | entfällt |

**Summe v2: 11 von 42.** Prio A: 0 von 11 auf 2.
Technik: Title „Seminare · me&you Prototyp v2“, keine Meta, kein Schema, 266 Wörter. Jede Sektion ist 100 vh hoch; das macht die Seite lang, obwohl sie wenig sagt.

## 2. Lücken
**Prio A**
- Der Hero sagt nicht, was die Seite anbietet: Rhetorik-Seminare, drei Formate, drei Tage plus ein Tag, kleine Gruppe, Orte.
- Kein Button und keine Rückversicherung im Hero.
- Kein Beweis auf der ganzen Seite, obwohl 250 ProvenExpert-Bewertungen, Medienlogos und Zitate da sind.
- KI-Trainer, der Michael ähnelt, im Hero (Regel: Michaels Gesicht nie erfinden).
- Kein Ablauf des Gesprächs.

**Prio B**
- Besucher können die Formate nicht vergleichen: Für wen ist welches Format, wo und wann findet es statt?
- Keine Termine, nur Monate; ein falscher Monat (September).
- Keine FAQ zu den Fragen, die vor einer Seminarbuchung kommen: Welches zuerst? Enthalten? Gruppe? Absage?

**Prio C**
- Platzhalter als Überschriften, „zwölf Menschen“ falsch, Schrift unter 16 px.

## 3. Idealer Ausgang und Muster
Muster: P0-Blueprint für die Angebotsseite, Optik und Bausteine der freigegebenen Startseite (gleiche Website). Die Copy-Deck-Zeilen des Kunden bleiben, wo sie stimmen: „Ein Einstieg. Dann dein eigener Weg.“, „Eigenständig. In beliebiger Reihenfolge.“, „Der Ort ist Teil der Arbeit.“, „Für wen das gedacht ist“, „Der nächste Schritt ist ein Gespräch.“ Sie werden ergänzt durch ein Keyword-H1, Fakten und Beweise.

Ziel-Hero: Bewertungszeile, Kicker-H1 „Rhetorik-Seminare mit Michael Ehlers“, große Zeile „Ein Einstieg. Dann dein eigener Weg.“, ein Satz mit Fakten (drei Formate, 3 + 1 Tage, höchstens 14 Menschen, sechs Orte), Button „Gespräch buchen“ + Rückversicherung, zweiter Link „Termine ansehen“. Echtes Foto von Michael (Bühne oder Gespräch) statt KI-Trainer.

Traffic: von der Startseite (Format-Links mit Anker) und aus Ads/Gespräch. Besucher wollen vergleichen und einen Termin sehen. Deshalb: Antwort-Block und Vergleich früh, Termine je Format in den Karten und nochmals gesammelt.

## 4. Abschnittsplan und P0-Abdeckung
| # | Abschnitt | Job | P0-Zeile |
|---|---|---|---|
| 1 | Hero | Was, für wen, wo, nächster Schritt, zwei Beweise | 1 Hero |
| 2 | Kurz-Antwort + Beweis-Leiste | „Welches Rhetorik-Seminar passt zu dir?“ in 50 Wörtern, Fakten 3 + 1 / 3 Videoanalysen / VR / 10–14 Plätze, 250 Bewertungen, Medienlogos | 2 Beweis-Leiste |
| 3 | Der Einstieg (R I, `#frei-sprechen`) | groß hervorgehoben: für wen, 7 Inhalte, was du übst, Plätze, Orte + nächste Termine, CTA | 4 Leistungen |
| 4 | Die Formate (R II `#ruhig-bleiben`, R III `#mit-sprache-fuehren`, Bundle) | gleiche Karten ohne Reihenfolge: Schwerpunkt, Inhalte, für wen, Plätze, Orte + Termine, CTA | 4 Leistungen |
| 5 | Vergleich | Tabelle „Welches Format passt zu dir?“ (Schwerpunkt, typische Situation, Plätze, Orte) | 3 „Ist das etwas für mich?“ (angepasst) |
| 6 | Im Raum | „Drei Tage, kleine Gruppe, kein Publikum.“ Ablauf der Tage: Videoanalysen, VR, Get Together; was enthalten ist | 4 Leistungen (Ablauf) |
| 7 | Stimmen | 4 offene Bewertungen zu Inhalten und Ablauf, Quelle, ProvenExpert-Zahl, 1 Video | 7 Bewertungen |
| 8 | Orte und Termine (`#termine`) | alle Termine nach Ort und Format, Fotos, CTA | 9 Standort (angepasst) |
| 9 | Michael | kurzer Trainer-Block: echtes Foto, 30 Jahre, über 8.000 Teilnehmer, ERFOLG Top 100, Link Michael-Seite | 6 Über den Trainer |
| 10 | Erst ein Gespräch | 3 Schritte, 30 Minuten, kostenlos, per Video, CTA, Telefon | 5 Der erste Termin |
| 11 | FAQ | 8–10 Fragen zu Auswahl, Reihenfolge, Gruppe, Enthalten, Anfänger, Absage, Preis | 8 FAQ |
| 12 | Abschluss | „Der nächste Schritt ist ein Gespräch.“ Häkchen, Bewertungszeile, Button, Telefon | 10 Abschluss-CTA |

**Abdeckung (10 P0-Zeilen):** 1 Hero → S1. 2 Beweis-Leiste → S2. 3 „Ist das etwas für mich?“ → S5 Vergleich (auf einer Angebotsseite ist die Frage „welches Format“; die Situationen stehen auf der Startseite). 4 Leistungen → S3, S4, S6. 5 Der erste Termin → S10. 6 Über den Trainer → S9 (kurz, Details auf der Michael-Seite). 7 Bewertungen → S7. 8 FAQ → S11. 9 Standort → S8 Orte und Termine (wechselnde Seminarorte, Firmensitz im Footer). 10 Abschluss → S12. Keine Zeile gestrichen.

CTA „Gespräch buchen“ in S1, S3, S4 (je Karte), S6, S8, S10, S12 + Header. Erfüllt Item 11.
Anker der Startseite (`#frei-sprechen`, `#ruhig-bleiben`, `#mit-sprache-fuehren`) werden hier gebaut. Damit ist offener Punkt 2 aus dem Startseiten-Sichtcheck gelöst.

## 5. Offene Punkte
Aus `dataset.md` 5: Seminarnamen, Bundle (ja/nein, Termine, Ort), Mallorca-Termine 2027 (K1), Person im Gespräch, Sales-Checkliste-Freigabe, echte Seminarfotos, DeepOcean in einem Satz.
