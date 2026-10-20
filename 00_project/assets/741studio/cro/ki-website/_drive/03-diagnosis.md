# Diagnose — Landingpage 741 KI-Website

Grundlage: 741 CRO-Raster (scorecard.md, 22 Items). Item 22 (HWG) entfällt: 741 ist kein Health-Kunde; Beispiele aus Gesundheitsberufen bleiben trotzdem HWG-sicher (dataset K7). Item 18 (Standort) entfällt: Online-Produkt ohne Ladenlokal, Begründung unten. Bestehenskriterium damit: alle Prio-A-Items = 2, Gesamt mindestens 32 von 40 (80 %, gleiche Quote wie 34/42).

Ist-Zustand: Es gibt keine Live-Seite. Bewertet wird die Abkürzungs-Vorschau vom 13.10.2026 (`04_site/de/ki-website-vorschau.html`, ohne Workflow gebaut, von Martin verworfen: "keine Bilder, keine optimale Hero-Section"). Messwerte aus Chrome 1440×863 am 13.10.2026.

## 1. Bewertung der aktuellen Vorschau
| # | Regel | Prio | Score | Beleg |
| --- | --- | --- | --- | --- |
| 1 | Hero in 5 s: was, für wen, nächster Schritt | A | 1 | Was + CTA klar; für wen fehlt (keine Zielgruppe im Hero genannt) |
| 2 | Headline = Ergebnis + Ort/Keyword | A | 1 | H1 "Deine Website änderst du ab heute per Chat …" ohne Keyword "KI-Website" (1.300/Monat, dataset §5) |
| 3 | Sub-Headline: Situation, dann 3–4 Hilfen | A | 1 | Situation ja ("kostet dich eine Mail …"), Hilfen als ein Satz, nicht konkret aufgezählt |
| 4 | CTA im ersten Bildschirm (701 px) | A | 1 | Button-Unterkante 705 px > 701 px |
| 5 | CTA-Text = Schritt + Nutzen | A | 2 | "Kostenlos prüfen, ob deine Website umziehen kann" |
| 6 | Rückversicherung unter CTA | A | 1 | Nur Beleg-Zeile, keine Dauer/unverbindlich-Zeile |
| 7 | Zwei Beweisformen above the fold | A | 1 | Eine Textzeile (Hüwel, 0 €); kein Bild-Beweis, keine Kennzahl-Karte |
| 8 | Gesicht + Qualifikation im Hero oder Sektion 2 | A | 0 | Kein Foto von Martin, keine Person bis zur FAQ |
| 9 | Erster Schritt: 3–4 Schritte, Dauer, Preisrahmen | A | 1 | 3 Schritte der Änderung, aber kein Start-Ablauf (Gespräch, Bau, Einrichtung) und keine Dauer |
| 10 | Eine CTA-Farbe, Blur-Test | A | 1 | CTA gelb = gleiche Farbe wie Highlight-Wörter; im Blur-Test konkurrieren 6 gelbe Flächen |
| 11 | CTA alle 2 Sektionen | A | 1 | CTA nur in Hero und Abschluss (2 von 9 Sektionen) |
| 12 | Bewertungen offen mit Namen | B | 0 | Keine Stimme, keine Bewertung |
| 13 | Beweis-Überschrift trägt Nutzen | B | 2 | "Vorher 2.000 € Abo im Jahr. Nachher Chat und 0 € Hosting." |
| 14 | 3–4 Beweisblöcke verteilt | B | 1 | Hero-Zeile, Vorher/Nachher, FAQ-Antwort: kein Beweis am Abschluss |
| 15 | Situationen-Sektion | B | 2 | "Kennst du das?" mit 3 Situationen und Weg hinaus |
| 16 | Leistungen als Karten mit Link | B | 1 | 7 Karten ohne Links zu Unterseiten |
| 17 | FAQ, Preis zuerst | B | 1 | Keine Preisfrage an erster Stelle |
| 18 | Standort | B | entfällt | Online-Produkt ohne Ort; ersetzt durch "Hilfe 24/7" |
| 19 | Abschluss = Mini-Hero | B | 1 | Headline + CTA + Zeile; keine Häkchen, kein Beweis |
| 20 | Überschriften mit Aussage | C | 1 | "Fragen zur KI-Website", "24/7 Hilfe von 741" sind Labels |
| 21 | Typografie, Body ≥ 16 px | C | 1 | Kartentext 15,8 px (1,1 rem bei 14,4 px Root) |
| 22 | HWG | A | entfällt | Kein Health-Kunde |

Summe Ist-Zustand: **21 von 40**. Prio A: keines auf 2 außer Item 5.

## 2. Lücken
**Prio A:** Keyword "KI-Website" in die H1 (2), Zielgruppe im Hero (1), Hilfen konkret als Häkchen (3), CTA sicher über 701 px (4), Rückversicherung "kostenlos · 30 Minuten · unverbindlich" (6), Bild-Beweis im Hero: echte Hüwel-Seite im Laptop plus Kennzahl-Karte (7), Martin mit Foto spätestens in Sektion 2 (8), Start-Ablauf mit Dauer (9), eine CTA-Farbe: dunkler Pill-Button wie auf 741.studio, Gelb nur als Akzent (10), CTA in Sektion 1, 3, 5, 6, 7, 10 (11).
**Prio B:** Stimme oder Beleg-Block statt Bewertungen (12, [FEHLT: Stimme Hüwel]), Beweis am Abschluss (14), Karten mit Links zu bestehenden 741-Seiten (16), FAQ mit Preis zuerst (17), Abschluss mit Häkchen und Beweis (19).
**Prio C:** Aussage-Überschriften (20), Body 16 px+ (21).

## 3. Idealer Ausgang und Muster
Muster: **P0-Blueprint**, Hero nach **P9 (Premium-Service-Hero)** und der **741-Live-Startseite** (Badge über H1, kursiver Fraunces-Akzent, dunkler Pill-CTA, Laptop-Mockup mit echtem Screen und schwebenden Beweis-Karten). Begründung: gleiche Marke wie 741.studio, und das Produkt IST eine Website, also zeigt der Hero die echte Website.

## 4. Abschnittsplan und P0-Abdeckung
| # | Abschnitt | Job | P0-Zeile |
| --- | --- | --- | --- |
| 1 | Hero | KI-Website für Praxen und lokale Unternehmen, per Chat änderbar, Beweis Hüwel, CTA | 1 Hero |
| 2 | Beweis-Leiste | 4 echte Kennzahlen der Hüwel-Seite (1,3 s · 0 fremde Skripte · 0 € Hosting · 88 Weiterleitungen) | 2 Proof wall (kompakt) |
| 3 | Kennst du das? | 3–4 Situationen + "So geht es anders", CTA | 3 "Ist das etwas für dich?" |
| 4 | Was du bekommst | 4 Karten (Website-Bau, Pflege per Chat, Prüfung und Freigabe, Formulare/Kontakte) mit Links zu bestehenden 741-Seiten | 4 Leistungen |
| 5 | So startest du | 4 Schritte mit Dauer (Gespräch 30 Min, Bau/Umzug [FEHLT: Dauer], Einrichtung 15 Min, ab dann per Chat), CTA | 5 Erster Termin |
| 6 | Über Martin | echtes Foto, Martin Drendel, 741.studio, Team, Zusage 24/7, CTA | 6 Über die Behandlerin |
| 7 | Fallbeispiel Praxis Hüwel | Vorher/Nachher mit echten Screens und Zahlen, Platz für Stimme [FEHLT], CTA | 7 Reviews 2 (ersetzt, siehe unten) |
| 8 | FAQ | Preis zuerst, KI-Kosten, Technik, Fehler, nachts, Tempo, Umzug/Rankings | 8 FAQ |
| 9 | Hilfe 24/7 + Schutz | Was die Prüfung stoppt + wer hilft | 9 Standort (ersetzt, siehe unten) |
| 10 | Abschluss | Mini-Hero: Headline, 3–5 Häkchen, Beweis, CTA + "Live-Beispiel ansehen" | 10 Closer |

Abdeckungs-Prüfung (10 P0-Zeilen):
1. Hero: enthalten als Sektion 1.
2. Proof wall: enthalten als Sektion 2 (Kennzahlen statt Google-Bewertungen; Grund: zum Produkt gibt es noch keine Bewertungen, die Zahlen sind echt gemessen).
3. Situationen: enthalten als Sektion 3.
4. Leistungen: enthalten als Sektion 4.
5. Erster Termin: enthalten als Sektion 5.
6. Über die Person: enthalten als Sektion 6.
7. Reviews 2: ersetzt durch Sektion 7 Fallbeispiel; Grund: keine Produktbewertungen vorhanden, das Fallbeispiel ist der stärkste echte Beweis; Stimme Hüwel als [FEHLT]-Platz.
8. FAQ: enthalten als Sektion 8.
9. Standort: gestrichen, Grund: Online-Produkt ohne Ort; der Platz geht an "Hilfe 24/7 und Schutz" (Sektion 9), weil "Was passiert, wenn etwas schiefgeht?" der Haupteinwand ist.
10. Closer: enthalten als Sektion 10.

## 5. Offene Punkte
[FEHLT: Stimme Hüwel] · [FEHLT: Dauer Bau/Umzug] · [FEHLT: 24/7-Kanal] · Preis bleibt im Gespräch (741-Regel, kein [FEHLT]).
