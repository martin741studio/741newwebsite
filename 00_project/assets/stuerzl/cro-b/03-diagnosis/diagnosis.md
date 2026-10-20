> Aus dem Track-A-Lauf übernommen (`../cro/`), gilt unverändert für Track B. Stand 2026-10-11.

# Diagnose — Startseite STÜRZL Steuerstrafrecht (Dr. Anja Stürzl)

Stand 2026-10-11. Grundlage: `02-data/dataset.md`, Screenshots `live-home-first-viewport-1440.png` und `live-home-1440.png`. Bewertung nach `00_project/knowledge/cro-library/_derived/scorecard.md` (Desktop 1440 px), strenge Skala 0/1/2. Item 22 = **Anwaltswerbe-Check** (BRAO § 43b, BORA § 6, UWG, § 43c BRAO/FAO), Hard Gate. Bestehenskriterium Prototyp: alle Prio-A-Items = 2, gesamt mindestens 36 von 44.

## 1. Bewertung der aktuellen Startseite

| # | Regel | Prio | Score | Beleg |
| --- | --- | --- | --- | --- |
| 1 | Hero in 5 Sekunden | A | 0 | Hero zeigt nur "Aufklären. Verständigen. Verteidigen." in grauer Box. Kein Fachgebiet, kein Ort, kein Schritt (`live-home-first-viewport-1440.png`). |
| 2 | Headline = Ergebnis + Stadt | A | 0 | H1 im Code ist "Kanzlei"; Title "Stürzl Steuerstrafrecht – Home". Weder "Steuerstrafrecht" noch Frankfurt oder München in H1 (dataset 1.1). |
| 3 | Sub-Headline Situation zuerst | A | 0 | Keine Sub-Headline. Der Fließtext darunter beginnt mit einem Emerson-Zitat. |
| 4 | CTA im ersten Bildschirm | A | 1 | Nur der kleine schwebende Chat-Button "HIER ONLINE-ANFRAGE STELLEN" unten rechts, ohne Link, kein Button im Hero. Cookie-Banner überdeckt links unten. |
| 5 | CTA-Text Schritt + Nutzen | A | 1 | "Online-Anfrage stellen" nennt den Schritt, aber keinen Nutzen, keine Vertraulichkeit. Die Seiten-Buttons heißen "MEHR ZUR KANZLEI", "MEHR ZU DEN SCHWERPUNKTEN". |
| 6 | Rückversicherung unter dem CTA | A | 0 | Keine Zeile zu Antwortzeit, Vertraulichkeit oder Kosten. |
| 7 | Zwei Beweisformen above the fold | A | 0 | Keine Bewertung, keine Zahl, kein Zitat von Mandanten. 5,0 (Google 14, anwalt.de 79) steht nirgends. |
| 8 | Gesicht und Qualifikation | A | 1 | Foto von Dr. Stürzl im Hero (echt, stark). Keine Qualifikation, kein Name, keine Fachanwaltsangabe im ersten Bildschirm. |
| 9 | Erster Termin: Schritte, Dauer, Preis | A | 1 | Nur der Claim "Erstberatung zum Festpreis" (Kontakt-Seite), ohne Preis, Schritte oder Dauer. |
| 10 | Eine CTA-Farbe, Blur-Test | A | 0 | Hellgraue Flächen, dunkle Buttons mit kleiner Schrift, der Chat-Button ist blasses Salbei. Kein Button gewinnt den Blur-Test. |
| 11 | CTA mindestens alle 2 Sektionen | A | 1 | Der Chat-Button schwebt überall, aber ohne Ziel. Sektions-Buttons führen nur zu Unterseiten, kein Anfrage-CTA. |
| 12 | Bewertungen offen | B | 0 | Keine Bewertungen auf der Startseite. |
| 13 | Beweis-Überschrift trägt Nutzen | B | 0 | Keine Beweis-Sektion. |
| 14 | 3 bis 4 Beweisblöcke | B | 0 | Keiner. Titel, Lehrtätigkeit, Werdegang stehen nur auf der Kanzlei-Seite. |
| 15 | Situationen-Sektion | B | 0 | Nur Rechtsbegriffe in einem Absatz ("Durchsuchungen / Beschlagnahme oder Untersuchungshaft"). Keine erkennbare Situation, keine Trennung Privat und Unternehmen. |
| 16 | Leistungen als Karten mit Link | B | 1 | Ein Fließtext mit einem Button "MEHR ZU DEN LEISTUNGEN", keine Karten, keine Nutzen-Überschriften. |
| 17 | FAQ mit echten Einwänden | B | 1 | Starker FAQ-Hub liegt auf Unterseiten (6 Seiten, ca. 2.555 Wörter, 6×H1). Auf der Startseite fehlt jede FAQ, Kosten und Ablauf unbeantwortet. |
| 18 | Standort | B | 1 | Beide Städte im Fließtext genannt, keine Adresse, keine Karte, kein Parken, keine ÖPNV-Hinweise. Die stehen nur auf der Kontakt-Seite (mit alter Adresse). |
| 19 | Abschluss = Mini-Hero | B | 0 | Die Seite endet mit dem Porträt-Block und dem Fuß. Kein Abschluss-CTA. |
| 20 | Überschriften mit Aussage | C | 0 | "Kanzlei", "Schwerpunkte", "Leistungen" sind Labels. |
| 21 | Typografie und Hierarchie | C | 1 | Lesbar (Light-Sans, grau auf Grau, kleiner Fließtext), flache Hierarchie, geringer Kontrast der Zitat-Quellen (`live-home-1440.png`). |
| 22 | Anwaltswerbe-Check | A | 1 | "Spezialisierung", "hohe Spezialisierung", "hohe fachliche Expertise", "kompetent und hart in der Sache", "fachliche Exzellenz" (alles Selbstlob ohne Beleg). "Erstberatung zum Festpreis" ohne Preis (dataset C2 bis C5). |

**Summe Ist-Zustand: 10 von 44 Punkten.**

## 2. Lücken

Prio A: Hero (1 bis 3, 5, 6, 10), Beweise above the fold (7), Qualifikation (8), erster Termin (9), CTA-Wiederholung (11), Anwaltswerbe-Check (22).
Prio B: Bewertungen (12 bis 14), Situationen (15), Leistungskarten (16), FAQ (17), Standort (18), Abschluss (19).
Prio C: Aussageüberschriften, Typografie (20, 21).
Sonderbefunde:
- **SEO:** Nur Marke und Namen ranken (#1). "anwalt steuerstrafrecht" #27. H1 und Title tragen weder Fachgebiet noch Ort. Der H1 braucht "Steuerstrafrecht", "Frankfurt" und "München".
- **Conversion-Kanal:** Kein Formular, kein Rückruf, Chatbot-Button ohne Ziel, WhatsApp nicht erlaubt. Der Prototyp braucht eine vertrauliche Anfrage ohne Falldaten.
- **Zwei Standorte** müssen gleichwertig sichtbar sein (Martin, 2026-10-11).
- **Notfall:** Der Akutfall "Durchsuchung läuft gerade" hat heute keinen sichtbaren Einstieg.
- **Stark und bleibt:** echte Fotos (Hero, Sessel-Porträt, Büro), das Logo, der ruhige Ton, die belegten Fakten zum Werdegang.

## 3. Idealer Ausgang (Plan) und gewähltes Muster

Eine Seite, die in 5 Sekunden sagt: "Steuer- und Wirtschaftsstrafrecht in Frankfurt und München. Dr. Anja Stürzl und ihr Team vertreten Privatpersonen und Unternehmen. Vertrauliche Anfrage per Formular, Telefon oder E-Mail. Google 5,0 und anwalt.de 5,0." Im ersten Bildschirm: ein schmaler Notfall-Streifen, H1, Sub-Headline, ein Button, eine Rückversicherungs-Zeile, eine Beweis-Zeile, das echte Foto. Darunter: Beweis-Leiste, zwei Mandantengruppen, sechs Leistungskarten, vier Schritte vom Erstkontakt, Dr. Stürzl mit belegten Qualifikationen, offene Bewertungen ohne Falldetails, ein Block "Vertraulich und transparent", FAQ mit den Einwänden Kosten, Ablauf, Vertraulichkeit, bundesweit, zwei Standort-Karten und ein ruhiger Abschluss.

**Muster:** P1-Stimmung (Person kaufen, Vertrauen) mit Notfall-Ergänzung für Akutmandate. Layout: Hero als Split (Text links, echtes Foto rechts), viel Weißraum, ein Salbei-CTA, dunkles Anthrazit-Band für Notfall und Abschluss, Karten mit 12 px Radius. Keine Waage, kein Hammer.

## 4. Abschnittsplan (12 Sektionen) und P0-Abdeckung

| # | Abschnitt | Job | P0 |
| --- | --- | --- | --- |
| 0 | Notfall-Streifen (oben, schmal) | Akutfall sofort erreichen | 1 Hero (CP-LOC-003) |
| 1 | Hero | wer, was, wo, nächster Schritt, Beweis | 1 Hero |
| 2 | Beweis-Leiste | fünf belegte Zahlen und Titel | 2 Beweis-Leiste |
| 3 | Zwei Mandantengruppen | Privatpersonen und Unternehmen erkennen sich | 3 Ist das etwas für mich |
| 4 | Leistungen | sechs Bereiche als Karten mit Link | 4 Leistungen |
| 5 | Ablauf: So beginnt ein Mandat | vier Schritte, Vertraulichkeit, Reaktion | 5 Dein erster Termin |
| 6 | Über Dr. Stürzl | Foto, Titel, Werdegang, Arbeitsweise | 6 Über die Behandlerin |
| 7 | Bewertungen | 5,0, drei offene Zitate, Link zu Google | 7 Reviews |
| 8 | Vertraulich und transparent | Verschwiegenheit, Berufsrecht, Honorar | Ergänzung Anwaltsseite |
| 9 | Häufige Fragen | sechs Fragen, Akkordeon, Direktantworten | 8 FAQ |
| 10 | Standorte | Frankfurt und München, Karte, Telefon, Zeiten | 9 Standort |
| 11 | Abschluss | Mini-Hero mit Formular, Telefon, E-Mail | 10 Closing CTA |

**Abdeckungs-Prüfung:** Alle 10 P0-Zeilen sind enthalten: 1 → Sektion 1 (plus 0), 2 → 2, 3 → 3, 4 → 4, 5 → 5, 6 → 6, 7 → 7, 8 → 9, 9 → 10, 10 → 11. Nichts gestrichen. Sektion 8 ist die Anwalts-Ergänzung.
CTA-Verteilung (Item 11): Hero, nach 3, nach 5, nach 6, nach 7, Abschluss (Sektionen 1, 3, 5, 6, 7, 11).

## 5. Offene Punkte
Alle [FEHLT] aus `dataset.md` Abschnitt 10. Entscheidend für den Freigabe-Checkpoint: Titelbestätigung, Frankfurter Adresse, eine Erreichbarkeitszeit, Notfallnummern, Einwilligungstext, Preis der Erstberatung.
