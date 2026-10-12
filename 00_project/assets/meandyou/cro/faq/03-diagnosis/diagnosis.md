# Diagnose — Seite „FAQ“ me&you / Michael Ehlers

Grundlage: Vorschau v2 `https://clients.741.studio/meandyou/v2/faq.html` (`02-data/v2-faq-first-viewport-1440.png`), `02-data/dataset.md`.
Raster: 741 CRO-Raster, angepasst nach Workflow 4b. Die FAQ-Seite ist eine Sammel- und Entscheidungsseite: Besucher kommen mit einer konkreten Frage, meist kurz vor der Buchung. Ersetzte Items: Item 3 (Sub mit Situation) → **F1 Einleitung + Sprungnavigation** (Gruppen sofort sichtbar); Item 9 (erster Termin) → **F2 Gespräch erklärt** (Dauer, Kosten, wer, was danach); Item 15 (Situationen) → **F3 Fragen gruppiert** (Themen, Reihenfolge nach Buchungsnähe); Item 16 (Leistungen als Karten) → **F4 Brücke zu den Fachseiten** (jede Gruppe verlinkt die Detailseite); Item 18 (Ort) → **F5 Stand und Kontakt** (Datum der Termine, Kontakt für fehlende Fragen). Item 22 entfällt (kein Health/Recht). Bestehen: alle Prio A = 2 oder begründet, gesamt mindestens 34 von 42.

## 1. Bewertung der aktuellen Seite (v2)
| # | Regel | Prio | Score | Beleg |
|---|---|---|---|---|
| 1 | Hero in 5 Sekunden: was, für wen, nächster Schritt | A | 1 | „FAQ · Häufige Fragen“ sagt was; für wen und der nächste Schritt fehlen |
| 2 | Headline = Thema + Keyword | A | 1 | „Häufige Fragen“ (Copy Deck), ohne Bezug zu Rhetorik-Seminar oder Michael Ehlers |
| F1 | Einleitung + Sprungnavigation | A | 0 | keine Einleitung, keine Gruppen, 10 Fragen nummeriert in zwei Spalten |
| 4 | CTA im ersten Bildschirm | A | 1 | nur der Header-Button „Gespräch buchen“ |
| 5 | CTA-Text: Schritt + Nutzen | A | 1 | „Gespräch buchen“ ohne Nutzenzeile |
| 6 | Rückversicherung unter dem CTA | A | 0 | nirgends „30 Minuten, kostenlos, per Video“ |
| 7 | Zwei Beweisformen above the fold | A | 0 | keine Bewertung, keine Zahl |
| 8 | Gesicht + Qualifikation | A | 0 | kein Foto, keine Qualifikation; keine Frage zu Michael |
| F2 | Gespräch erklärt (Dauer, Kosten, wer, danach) | A | 0 | keine Frage zum Gespräch, obwohl es das Ziel jeder Seite ist |
| 10 | Eine CTA-Farbe, Blur-Test | A | 1 | Header-Button #7E99B6, weiße Schrift 2,95 : 1 (Messung Seminarseite, gleiche v2-Basis) |
| 11 | CTA mindestens alle 2 Sektionen | A | 0 | kein CTA im Inhalt |
| 12 | Bewertungen offen, Name + Quelle + Überschrift | B | 0 | keine |
| 13 | Beweis-Überschrift trägt Nutzen | B | 0 | keine |
| 14 | 3–4 Beweisblöcke, einer am Kontakt | B | 0 | keine; ein Zitat (V8) ohne Namen und Quelle |
| F3 | Fragen gruppiert, Reihenfolge nach Buchungsnähe | B | 0 | gemischte Liste: Ablauf, Hotel, Storno, Haltung, Community |
| F4 | Brücke zu den Fachseiten | B | 0 | kein Link zu Seminare, Michael, Was ist Rhetorik |
| 17 | FAQ mit echten Einwänden und PAA | B | 1 | Einwände Übernachtung, Storno, Schauspiel ja; Preis, Anfänger, Gespräch, PAA fehlen; Storno-Antwort widerspricht den AGB (K1) |
| F5 | Stand und Kontakt | B | 0 | kein Datum, keine Kontaktzeile für fehlende Fragen |
| 19 | Abschluss = Mini-Hero | B | 0 | kein Abschluss, Seite endet leer |
| 20 | Überschriften tragen Aussagen | C | 1 | Fragen sind klar; eine Frage bewirbt die Community statt eine Sorge zu beantworten |
| 21 | Typografie | C | 1 | Antworttext kleiner als der Fließtext der Startseite (Screenshot) |
| 22 | (Health/Recht) | – | n/a | entfällt |

**Summe v2: 8 von 42.** Prio A: 0 von 11 auf 2. 286 Wörter (Benchmark Median 858, Anbieter-FAQs 500 bis 860).

## 2. Lücken
**Prio A**
- Der Kopf sagt nicht, worum es geht, und bietet keinen Weg zur gesuchten Frage (Sprungnavigation).
- Kein Beweis und kein Gesicht. Wer eine FAQ liest, prüft gerade, ob er buchen soll.
- Keine einzige Frage zum kostenlosen Gespräch, dem Ziel aller Buttons.
- Kein Button im Inhalt.

**Prio B**
- Fragen ohne Ordnung; Gruppen fehlen.
- Keine Links zu Seminare, Michael, Was ist Rhetorik. Die vier Geschwisterseiten verlinken auf `/faq`, die FAQ verlinkt zurück auf keine.
- Storno-Antwort (Gutschein) widerspricht den AGB (8 Wochen, 30 %).
- Kein Stand-Datum für Termine, kein Kontakt für Fragen, die fehlen.

**Prio C**
- Community-Frage aus internem Briefing; kleine Schrift.

## 3. Muster und Ziel
Muster: FAQ-Seite aus `page-templates.md` 6 (Hero, Direkt-Antwort, Fragegruppen, Abschluss-CTA), Optik und Bausteine der freigegebenen Startseite. Copy-Deck-H1 „Häufige Fragen“ bleibt groß, davor ein kleines Keyword-Stück. Antworten aus den freigegebenen Geschwisterseiten, neu formuliert (Ähnlichkeit unter 25 %), jede Gruppe mit Link zur Detailseite.

Ziel-Hero: Bewertungszeile, H1 „Häufige Fragen zu den Rhetorik-Seminaren mit Michael Ehlers“ (Copy-Deck-Teil groß), ein Satz Einleitung, Sprungnavigation mit sieben Gruppen, Button „Gespräch buchen“ + Rückversicherung, echtes Foto Michael klein.

Reihenfolge der Gruppen nach Buchungsnähe: erst „Ist das etwas für mich?“ (Seminar und Inhalte), dann Wo und Wann, Ablauf und Leistungen, Kosten und Storno, Das Gespräch, Michael, zuletzt Rhetorik allgemein (Einsteiger, Brücke zu `/rhetorik`).

## 4. Abschnittsplan und P0-Abdeckung
| # | Abschnitt | Job | P0-Zeile |
|---|---|---|---|
| 1 | Hero | Thema, Einleitung, Sprungnavigation, CTA + Rückversicherung, Beweiszeile | 1 Hero |
| 2 | Das Wichtigste in Kürze | Direkt-Antwort in 3 bis 4 Sätzen + Fakten-Kacheln + ein Zitat | 2 Beweis-Leiste |
| 3 | Seminar und Inhalte (`#seminar`) | Was macht man, Einstieg, Reihenfolge, Anfänger, Führung, erfahren, introvertiert, schauspielern, Fortschritt, Online-Kurs; Link /seminare; CTA | 3 „Ist das etwas für mich?“, 4 Leistungen |
| 4 | Orte und Termine (`#orte`) | sechs Orte, Zuordnung, nächste Termine, Wochentage, Deutschland, Bundle, freie Plätze, Stand; CTA | 9 Standort |
| 5 | Ablauf und Leistungen (`#ablauf`) | Seminartage, Video, VR, Gruppe, Get Together, Material, Übernachtung, Anreise, Verpflegung, Begleitperson | 4 Leistungen |
| 6 | Kosten und Storno (`#kosten`) | Preis im Gespräch, was enthalten, Storno laut AGB; CTA | 8 FAQ (Preis zuerst) |
| 7 | Das Gespräch (`#gespraech`) | Dauer, Kosten, wer, Inhalt, Verkaufsgespräch?, Vorbereitung, Umbuchen, Anrufen; CTA | 5 Der erste Termin |
| 8 | Michael (`#michael`) | wer, seit wann, leitet er selbst, Methode, Unternehmen, Bewertungen; Link /michael | 6 Über den Trainer, 7 Bewertungen |
| 9 | Rhetorik allgemein (`#rhetorik`) | was ist Rhetorik, Säulen, lernen, Übungen, Bücher und Videos, Alltag ohne Bühne; Link /rhetorik | 8 FAQ (PAA) |
| 10 | Abschluss | Frage nicht dabei? Kontakt + Gespräch, Häkchen, Beweis | 10 Abschluss-CTA |

**Abdeckung (10 P0-Zeilen):** 1 → S1. 2 → S2. 3 → S3 (Fragen „Bin ich richtig?“). 4 → S3, S5. 5 → S7. 6 → S8 (kurz, Details auf `/michael`). 7 → S2 Zitat und S8 Frage zu Bewertungen mit Link auf `/stimmen` (eigene Stimmen-Seite im Parallel-Lauf); kein eigener Bewertungsblock, weil eine FAQ-Seite sonst die Stimmen-Seite dupliziert. 8 → ganze Seite. 9 → S4. 10 → S10. Keine Zeile gestrichen.

CTA „Gespräch buchen“ in S1, S3, S4, S6, S7, S10 + Header. Erfüllt Item 11. Ziel: `termin.html?utm_source=faq&utm_content=<abschnitt>`.

## 5. Offene Punkte
Aus `dataset.md` K1 bis K12: AGB vs. Sales-Checkliste, Übernachtung, Verpflegung, Begleitperson, Seminarleitung, Person im Gespräch, Bundle, Programm Get Together, Kundenfragen ohne Antwort (Vertraulichkeit Video, Bildungsurlaub, Rechnung, Sprache, Zertifikat).
