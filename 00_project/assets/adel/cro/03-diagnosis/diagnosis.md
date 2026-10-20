# Diagnose — Startseite Rechtsanwältin Aydan Adel

Stand 2026-10-10. Grundlage: `02-data/dataset.md`. Bewertung nach `00_project/knowledge/cro-library/_derived/scorecard.md` (Desktop 1440 px). Item 22 gilt hier als **Anwaltswerbe-Check** statt HWG (BRAO § 43b, BORA § 6, UWG, siehe dataset Abschnitt 7). Bestehenskriterium: alle Prio-A-Items = 2, gesamt mindestens 36 von 44.

## 1. Bewertung der aktuellen Startseite

| # | Regel | Prio | Score | Beleg |
| --- | --- | --- | --- | --- |
| 1 | Hero in 5 Sekunden | A | 0 | H1 "Rechtsanwältin Aydan Adel", darunter nur ein Linien-Symbol. Kein Rechtsgebiet, kein Ort, kein Schritt (live-home-first-viewport-1440.png). |
| 2 | Headline = Ergebnis + Stadt | A | 0 | Weder "Bonn" noch Erbrecht oder Familienrecht in H1, Title oder Meta (dataset 1.1). |
| 3 | Sub-Headline Situation zuerst | A | 0 | Keine Sub-Headline. Der Begrüßungssatz steht unter dem Hero, beginnt mit "Ich freue mich". |
| 4 | CTA im ersten Bildschirm | A | 0 | Kein CTA auf der ganzen Seite. Cookie-Banner deckt den Hero ab. |
| 5 | CTA-Text Schritt + Nutzen | A | 0 | Kein Button. Nur Satz: "Für einen Beratungstermin bitte ich Sie mich per E-Mail zu kontaktieren." |
| 6 | Rückversicherung unter dem CTA | A | 0 | Nicht vorhanden. |
| 7 | Zwei Beweisformen above the fold | A | 0 | Keine Bewertung, keine Zahl, kein Zitat im ersten Bildschirm. 5,0 Sterne mit 18 Bewertungen nirgends auf der Seite. |
| 8 | Gesicht und Qualifikation | A | 0 | Kein Foto auf der Startseite. Das Porträt (mit Sonnenbrille) liegt nur auf /über-mich/. |
| 9 | Erster Termin: Schritte, Dauer, Preis | A | 1 | Ein Satz zu E-Mail, Video und Telefon. Keine Schritte, keine Dauer, kein Preis. |
| 10 | Eine CTA-Farbe, Blur-Test | A | 0 | Kein CTA, die ganze Seite ist ocker und grau. |
| 11 | CTA mindestens alle 2 Sektionen | A | 0 | Kein CTA. |
| 12 | Bewertungen offen | B | 0 | Keine Bewertungen. |
| 13 | Beweis-Überschrift trägt Nutzen | B | 0 | Keine Beweis-Sektion. |
| 14 | 3 bis 4 Beweisblöcke | B | 0 | Kein Beweisblock. Kammer, Haftpflicht und Jahre nur im Impressum und auf /über-mich/. |
| 15 | Situationen-Sektion | B | 0 | Nur Rechtsbegriffe ("Erbschaftsanspruch", "Erbunwürdigkeit"). Keine erkennbare Situation. |
| 16 | Leistungen als Karten mit Link | B | 1 | Vier Listen mit Aufzählungspunkten, ca. 70 Stichwörter, keine Karten, keine Links. |
| 17 | FAQ mit Einwänden | B | 0 | Keine FAQ. Kosten stehen nur auf /honorar/ als Gesetzestext. |
| 18 | Standort | B | 1 | Anfahrt liegt auf einer eigenen Seite, die Startseite nennt Adresse nicht. |
| 19 | Abschluss = Mini-Hero | B | 0 | Letzter Absatz ohne Button, danach Fuß. |
| 20 | Überschriften mit Aussage | C | 0 | "Herzlich Willkommen!", "Erbrecht", "Familienrecht", "Zivilrecht". |
| 21 | Typografie und Hierarchie | C | 1 | Lesbar (Garamond-Überschrift, Condensed-Body ca. 17 px), aber flach, ocker-graue Flächen, Kontrast Text auf Ocker gering. |
| 22 | Anwaltswerbe-Check | A | 1 | "spezialisierte Rechtsanwältin" (ohne Fachanwaltstitel), "auf jedem Rechtsgebiet behilflich", "Vertretung vor allen Strafgerichten" (dataset C2, C3). |

**Summe Ist-Zustand: 5 von 44 Punkten.**

## 2. Lücken

Prio A: alles ab Hero (1 bis 8, 10, 11), erster Termin (9), Anwaltswerbe-Check (22).
Prio B: alle Beweis-, Situations-, FAQ-, Standort- und Abschlussblöcke (12 bis 19).
Prio C: Aussageüberschriften, Hierarchie (20, 21).
Sonderbefund SEO: Die Startseite rankt nur für türkische Vollmacht-Begriffe, nicht für ein Keyword zu Erbrecht, Familienrecht oder Bonn (dataset 6). Der Hero-H1 muss "Bonn", "Erbrecht" und "Familienrecht" tragen.

## 3. Idealer Ausgang (Plan)

Eine Seite, die in 5 Sekunden sagt: "Rechtsanwältin Aydan Adel, Erbrecht und Familienrecht in Bonn, 5,0 von 18 Google-Bewertungen, Erstberatung per WhatsApp, Telefon oder E-Mail". Sie zeigt ihr Gesicht, die fünf Belege in einer Leiste, erkennbare Situationen, die drei Rechtsgebiete mit je vier Teilleistungen, die vier Schritte bis zur Beratung, ihre Laufbahn, echte Bewertungen mit Vorname, ein Block mit Berufsrecht und Verschwiegenheit, eine FAQ mit den Einwänden Kosten, Online, Ort, Vollmacht, die Anfahrt mit Parken und ÖPNV und einen ruhigen Abschluss.

**Muster:** P1-Stimmung (Person kaufen, Vertrauen) im Layout der Ronas-IT-Elemente: große enge Überschriften, Wellenlinien unter Schlüsselwörtern, Scroll-Reveal grau zu Tinte, nummerierte Blöcke 01 bis 03, schwarze Pille wird Bronze-Pille, Plus-FAQ, dunkler Abschluss mit Wellenkante.

## 4. Abschnittsplan (11 Sektionen) und P0-Abdeckung

| # | Abschnitt | Job | P0 |
| --- | --- | --- | --- |
| 1 | Hero | wer, was, wo, nächster Schritt, Rating | 1 Hero |
| 2 | Beweis-Leiste | fünf Belege plus ein Zitat | 2 Beweis-Leiste |
| 3 | Wann Sie mich brauchen | sechs erkennbare Situationen, Scroll-Reveal | 3 Ist das etwas für mich |
| 4 | Leistungen 01 bis 03 | Erbrecht, Familienrecht, Weitere Gebiete, je 4 Teilleistungen, Links | 4 Leistungen |
| 5 | Der Weg zur Beratung | vier Schritte, Kanäle, Ort | 5 Dein erster Termin |
| 6 | Über mich | Porträt, Laufbahn-Zeitleiste, Haltung | 6 Über die Behandlerin |
| 7 | Bewertungen | 5,0, 18, drei offene Karten, Link zu Google | 7 Reviews |
| 8 | Sicher und transparent | Kammer, Haftpflicht, Verschwiegenheit, Honorar, Schlichtung | Ergänzung Anwaltsseite, Muster Ronas Compliance |
| 9 | Häufige Fragen | sechs Fragen, Plus-Akkordeon | 8 FAQ |
| 10 | Standort | Karte, Adresse, Auto, ÖPNV, Zeiten | 9 Standort |
| 11 | Abschluss | Mini-Hero, drei Kanäle | 10 Closer |

**Abdeckungs-Prüfung (alle 10 P0-Zeilen):** 1 bis 10 enthalten, keine Zeile gestrichen. Sektion 8 ist Zusatz, weil Anwälte Berufsrecht und Verschwiegenheit als Vertrauensfaktor brauchen (Ronas hat dafür einen eigenen Block). CTA in Sektion 1, 3, 5, 6, 8, 10, 11, dazu Kopf.

## 5. Offene Punkte

Siehe `02-data/dataset.md`, Abschnitt 10. Keine Rückfrage nötig für den Entwurf.
