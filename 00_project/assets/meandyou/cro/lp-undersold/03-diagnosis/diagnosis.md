# Diagnose — Landingpage „The Undersold“ me&you / Michael Ehlers

Grundlage: Vorschau v2 `https://clients.741.studio/meandyou/v2/lp-undersold.html` (`02-data/v2-lp-undersold-first-viewport-1440.png`), `02-data/dataset.md`, Content Pool lp:undersold (Findings F1 bis F5).
Raster: 741 CRO-Raster, angepasst nach Workflow 4b. Die Seite ist eine Persona-Landingpage für Anzeigen-Traffic und Premium-Besucher (Unternehmer, Führungskräfte). Sie hat keine Stadt. Ersetzte Items:
- Item 2 (Stadt in der Headline) → **Headline = Persona-Zeile + Keyword** (Führung, Unternehmer).
- Item 9 (erster Termin) → **Gespräch erklärt** (Dauer, Kosten, wer, was danach).
- Item 11 (CTA alle 2 Sektionen) → **U3 Ein CTA weit unten, ohne Dringlichkeit, Header-Button sichtbar** (Persona-Regel, Auftrag Q7).
- Item 18 (Standort) → **U1 Orte und Termine als Überschriften**.
- Item 22 (Health/Recht) → **U2 Persona-Treue**: Ort vor Menschen, wenige Elemente, keine Konferenz-Ästhetik, kein Countdown, keine Garantie (UWG).
Bestehen: alle Prio A = 2, gesamt mindestens 36 von 44.

## 1. Bewertung der aktuellen Seite (v2)
| # | Regel | Prio | Score | Beleg |
|---|---|---|---|---|
| 1 | Hero in 5 Sekunden: was, für wen, nächster Schritt | A | 1 | Für wen (Unternehmen) und Button ja; „Rhetorik“, „Seminar“, Ort fehlen im Hero (Screenshot) |
| 2 | Headline = Persona-Zeile + Keyword | A | 1 | „Ihr Unternehmen ist größer, als es nach außen wirkt.“ ohne Keyword, in Sie-Form (Rest der Website du) |
| 3 | Sub: Situation zuerst, dann Hilfe | A | 1 | Sub nennt die Situation in 3 Sätzen, keine Hilfe, kein Angebot |
| 4 | CTA im ersten Bildschirm | A | 2 | Button „Gespräch buchen“ bei y 589 und Header-Button (1440 × 900) |
| 5 | CTA-Text: Schritt + Nutzen | A | 1 | „Gespräch buchen“ ohne Nutzenzeile |
| 6 | Rückversicherung unter dem CTA | A | 0 | nirgends „30 Minuten, kostenlos, per Video“ |
| 7 | Zwei Beweisformen above the fold | A | 0 | keine Bewertung, keine Zahl im ersten Bildschirm |
| 8 | Gesicht + Qualifikation in Hero oder Sektion 2 | A | 2 | Sektion 2: echtes Foto `michael-door.webp`, 30+ Jahre, 8.000+, Top 100, 9 Bücher |
| 9 | Gespräch erklärt | A | 0 | kein Ablauf, keine Dauer, kein Gesprächspartner |
| 10 | Eine CTA-Farbe, Blur-Test | A | 1 | Header-Button #7E99B6 mit weißer Schrift 2,95 : 1; Hero-Button creme: zwei Button-Stile |
| U3 | Ein CTA weit unten, ohne Dringlichkeit, Header sichtbar | A | 1 | drei Buttons im Inhalt (Hero, Warum Michael, Abschluss); keine Dringlichkeit |
| 12 | Bewertungen offen, Name + Quelle + Überschrift | B | 1 | Laufband (Karussell), jedes Zitat dreimal im DOM |
| 13 | Beweis-Überschrift trägt Nutzen | B | 0 | „Was Teilnehmer sagen.“ ist ein Label |
| 14 | 3–4 Beweisblöcke, einer am Kontakt | B | 1 | Zahlenreihe und Zitate; am Abschluss kein Beweis |
| 15 | Situationen: erkennbar + Weg hinaus | B | 0 | keine Situationen-Sektion; nur Hero-Sub |
| 16 | Formate als Karten mit Nutzen und Link | B | 0 | kein Seminar, kein Format, kein Link zu `/seminare` |
| 17 | FAQ mit echten Einwänden, Preis zuerst | B | 0 | keine FAQ; PAA „Was kostet ein Rhetorikkurs?“ unbeantwortet (F5) |
| U1 | Orte und Termine als Überschriften | B | 0 | keine Orte, keine Termine (F1, F3) |
| 19 | Abschluss = Mini-Hero | B | 1 | Headline + Button; keine Häkchen, kein Beweis, kein Telefon |
| 20 | Überschriften tragen Aussagen | C | 1 | drei Aussagen, ein Label („Was Teilnehmer sagen.“) |
| 21 | Typografie, Body ≥ 16 px | C | 1 | `--body` ab 15 px, `--small` 12,5 bis 14,5 px (Quelltext) |
| U2 | Persona-Treue | A | 0 | Hero-Foto Büro mit Handschlag und Applaus (Konferenz-Ästhetik, Mann ähnelt Michael, K6); drei CTAs; kein Ort |

**Summe v2: 15 von 44.** Prio A: 2 von 12 auf 2. Wörter 446 laut `wordcount.py` (mit dreifachem Laufband), eindeutig rund 250. Benchmark-Median 1.194, Untergrenze 836.

## 2. Lücken
**Prio A**
- Der Hero sagt nicht, was angeboten wird. Kein Wort zu Seminar, Ort oder Format.
- Kein Beweis im ersten Bildschirm, keine Rückversicherung.
- Das Bild widerspricht der Persona: Büro und Handschlag statt Ort in goldenem Licht.
- Das Gespräch ist nicht erklärt. Drei Buttons statt einem weit unten.

**Prio B**
- Orte und Termine fehlen ganz, obwohl sie für diese Persona das Produkt sind und kein Wettbewerber sie zeigt (F1).
- Kein Format, keine Gruppengröße, kein „Für wen“, keine FAQ (F3: 4 bis 6 von 8 Wettbewerbern haben diese Blöcke).
- Zitate als Laufband, eines davon (Subotic) ohne Zusammenhang und mit gestrichenem Bundesliga-Bezug.
- Abschluss ohne Beweis und ohne Telefon.

**Prio C**
- Ein Label als Überschrift; kleine Schrift unter 16 px.

## 3. Muster und Ziel
Muster: P2 (Luxus-Lead-Seite: Beweis zuerst, dann Situation, ein CTA mit Rückversicherung, Abschluss spiegelt den Hero) und P9 (Premium-Hierarchie: Bild, Headline, gedämpfter Text, ein CTA) aus `patterns.md`, mit der Persona-Regel aus den Design-Richtlinien: breite Bilder, wenige Elemente je Bildschirm, Orte und Daten als Überschriften, ein Button weit unten. Optik und Bausteine der freigegebenen Startseite und der Seminarseite (Ortskarten, Faktenreihe, Zitat-Karten, Schritte, Akkordeon). Copy-Deck-Zeile bleibt groß, in du (Q3). Ein kleines Keyword-Stück im selben H1.

Ziel-Hero: breites Ortsbild in goldenem Licht (Finca, Terrasse, Meer), kleine Schrift davor. Kicker als H1-Teil „Rhetorik-Seminar für Führungskräfte und Unternehmer“, große Zeile „Dein Unternehmen ist größer, als es nach außen wirkt.“, Sub (Q3) plus ein Satz zum Angebot, Beweiszeile „227 von 250 Bewertungen mit 5 Sternen auf ProvenExpert · seit 1990“. Kein Button im Hero-Inhalt; der Header-Button „Gespräch buchen“ ist sichtbar. Ein leiser Textlink „Orte und Termine“ führt zum Anker.

## 4. Abschnittsplan und P0-Abdeckung
| # | Abschnitt | Job | P0-Zeile |
|---|---|---|---|
| S01 | Hero | Persona-Zeile, Keyword, Angebot in einem Satz, Beweiszeile, Anker zu Orten | 1 Hero |
| S02 | Das Seminar in Kürze | Direkt-Antwort in 3 bis 4 Sätzen, Fakten-Reihe, ein Unternehmer-Zitat (Röser) | 2 Beweis-Leiste |
| S03 | Die Lage | 4 Situationen (Pitch, Beirat oder Board, Kundentermin, Medien), Weg hinaus | 3 Ist das etwas für mich? |
| S04 | Die Methode | „Wirkung beginnt nicht bei der Technik.“, drei Schritte | 4 Leistungen (Haltung) |
| S05 | Orte und Termine (`#orte`) | sechs Orte als breite Bildkarten, Daten als Überschriften, Stand-Zeile, freie Plätze im Gespräch | 9 Standort |
| S06 | Drei Tage, kleine Gruppe | Format, Video, VR, Gruppe 10 bis 14; drei Formate kurz mit Link `/seminare`; Bundle; Leistungen mit gelben Marken | 4 Leistungen |
| S07 | Für wen | Führungskräfte, Gründer, Unternehmer, Vertrieb; gemischte Gruppen; wofür die Seite nicht ist | 3 Ist das etwas für mich? |
| S08 | Michael | ruhige Autorität: seit 1990, 8.000, neun Bücher, St. Gallen, ARTE und WELT TV, ERFOLG; Mandantennamen nennt er nicht; Link `/michael` | 6 Über den Trainer |
| S09 | Stimmen | drei bis vier offene Karten mit Überschrift (Röser, Escher, Bourcevet, V. Barcelona), ProvenExpert-Zahl | 7 Bewertungen |
| S10 | Häufige Fragen | 6 bis 7 Fragen: Führungskräfte, Inhalte, Gruppe, Wo und wann, verstellen, Preis, wenig Zeit; Link `/faq` | 8 FAQ |
| S11 | Abschluss: das Gespräch | einziger Button im Inhalt: drei Schritte, Rückversicherung, Telefon, Beweis | 5 Erster Schritt, 10 Abschluss-CTA |

**Abdeckung (10 P0-Zeilen):** 1 → S01. 2 → S02. 3 → S03 und S07. 4 → S04 und S06. 5 → S11 (Gespräch in drei Schritten). 6 → S08. 7 → S09. 8 → S10. 9 → S05 (Orte statt Praxisstandort; Firmensitz im Footer). 10 → S11. Keine Zeile gestrichen. S05 und S11 zusammen tragen die Persona-Regel „Daten und Orte als Überschriften, ein CTA weit unten“.

CTA: ein Button „Gespräch buchen“ im Inhalt (S11) plus Header-Button. Ziel `gespraech-buchen.html?utm_source=lp-undersold&utm_content=abschluss` (Header: `utm_content=header`). Keine Dringlichkeit, kein „nur noch X Plätze“.

## 5. Offene Punkte
Aus `dataset.md` 8: du/Sie (K1), Seminarname, Person im Gespräch, Mallorca 2027, Sales-Checkliste (Übernachtung, Verpflegung), Seminarleitung, echte Ortsfotos, Unternehmerzitate mit Einwilligung, ProvenExpert-Gesamtnote, 1:1-Coaching und Medientraining, sameAs.
