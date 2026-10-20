# Diagnose — Michael-Seite me&you

Grundlage: Vorschau v2 `https://clients.741.studio/meandyou/v2/michael.html` (`02-data/v2-michael-first-viewport-1440.png`), `02-data/dataset.md`.
Raster: 741 CRO-Raster nach Workflow 4b für eine Personen-Seite. Entry-Page-Items 3 (Situation), 9 (erster Termin als eigene Sektion), 15 (Situationen) und 16 (Leistungskarten) entfallen und werden ersetzt durch: **A1** Name, Rolle und Thema in Title, H1 und Meta · **A2** Person-Schema · **A3** Werdegang belegt und lesbar · **A4** Weg zum Angebot (Seminare + Gespräch). Item 22 entfällt. Bestehen: ≥ 34 von 42, Prio A = 2 oder begründet.

## 1. Bewertung v2
| # | Regel | Prio | Score | Beleg |
|---|---|---|---|---|
| 1 | Hero in 5 Sekunden: wer, wofür, nächster Schritt | A | 1 | Name im Logo, H1 Zahlen, kein Button |
| 2 | Headline = Person + Ergebnis/Thema | A | 1 | „30 Jahre. Über 8.000 Menschen. Eine Methode.“ ohne Rolle |
| A1 | Name, Rolle, Thema in Title, H1, Meta | A | 0 | Title „Über Michael · me&you Prototyp v2“, keine Meta |
| 4 | CTA im ersten Bildschirm | A | 1 | nur Header-Button |
| 5 | CTA-Text Schritt + Nutzen | A | 1 | „Gespräch buchen“ |
| 6 | Rückversicherung | A | 0 | keine |
| 7 | Zwei Beweisformen above the fold | A | 2 | Zahlen + ERFOLG + Medienlogos |
| 8 | Gesicht + Qualifikation | A | 2 | echtes Foto, 30+ Jahre |
| A2 | Person-Schema | A | 0 | kein JSON-LD |
| 10 | Eine CTA-Farbe, Blur | A | 1 | blasser Button #7E99B6 |
| 11 | CTA alle 2 Sektionen | A | 1 | Hero ohne, nur Abschluss |
| 12 | Bewertungen offen | B | 0 | keine |
| 13 | Beweis-Überschrift mit Nutzen | B | 1 | „Ausgezeichnet statt austauschbar.“ |
| 14 | 3–4 Beweisblöcke | B | 1 | Zahlen, ERFOLG, Logos in einem Block |
| A3 | Werdegang belegt und lesbar | B | 0 | Platzhalter statt Text |
| A4 | Weg zum Angebot | B | 1 | Abschluss-Button, kein Link zu Seminaren |
| 17 | FAQ | B | 0 | keine |
| 18 | Ort (Institut, Seminarorte) | B | 0 | nichts |
| 19 | Abschluss = Mini-Hero | B | 1 | Headline + Button |
| 20 | Überschriften tragen Aussagen | C | 1 | Platzhalter sichtbar |
| 21 | Typografie | C | 1 | kleine Labels |

**Summe v2: 15 von 42.** Fehler: „5 Bücher“ (richtig neun), „Top 100 Speaker“ (richtig Trainer).

## 2. Lücken
Prio A: Rolle und Thema fehlen im Hero, kein Button, keine Rückversicherung, kein Schema, Title/Meta fehlen. Prio B: kein Werdegang, keine Bücher, keine Lehre, keine Medienarbeit im Detail, keine Stimmen über Michael als Trainer, kein Weg zu den Seminaren, keine FAQ („Wer ist Michael Ehlers?“ wird gesucht).

## 3. Muster
P1 (Personen-Seite, Vertrauen): Hero mit Name und Rolle, Kurz-Antwort „Wer ist Michael Ehlers?“, belegter Werdegang als Zeitleiste, Haltung und Methode, Belege (Bücher, Lehre, Medien), Stimmen, Weg zum Angebot, Gespräch, FAQ, Abschluss. Copy-Deck-Zeilen bleiben: „Dreißig Jahre vor vollen Räumen.“ und „Autorität, die man nicht behaupten muss.“ Design = Startseiten-System.

## 4. Abschnittsplan und P0-Abdeckung
| # | Abschnitt | Job | P0 |
|---|---|---|---|
| 1 | Hero | Name, Rolle, Copy-Deck-Zeile, Fakten, CTA, Beweiszeile; Foto Stuhl 2026 | 1 |
| 2 | Kurz-Antwort | „Wer ist Michael Ehlers?“ 3 Sätze + Fakten-Kacheln + Medienlogos | 2 |
| 3 | Werdegang | Zeitleiste 1990 → heute (nur belegte Jahre) | 6 |
| 4 | Haltung und Methode | Motto, Persönlichkeit/Kongruenz/Wirkung, kein Schauspiel, direkte Rückmeldung | 6 |
| 5 | Bücher und Podcast | 9 Titel, Podcast seit 2008, LinkedIn-Newsletter | 7 (Beleg) |
| 6 | Lehre und Medien | St. Gallen (zwei Rollen), Analysen ARTE/WELT TV, Einordnungen ARD/ZDF/… | 7 (Beleg) |
| 7 | Stimmen | Zitate über Michael als Trainer, Quelle | 7 |
| 8 | Seminare mit Michael | echtes Gruppenfoto, drei Formate, Link /seminare, CTA | 4 |
| 9 | Erst ein Gespräch | 3 Schritte, CTA | 5 |
| 10 | FAQ | Wer ist, Bücher, St. Gallen, leitet er selbst, Podcast | 8 |
| 11 | Abschluss | Mini-Hero, Hallstadt im Footer | 10, 9 |
Abdeckung: P0 3 „Ist das etwas für mich?“ steckt in S08 (Für-wen-Satz) und gehört sonst auf die Startseite; alle anderen Zeilen enthalten. CTA in S01, S04, S06, S08, S09, S11.
