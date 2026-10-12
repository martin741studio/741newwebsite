# Dataset — Landingpage „The Undersold“ me&you (Stand 2026-10-12)

Gemeinsame Fakten: `../../02-data/dataset.md` (Startseite), `../../seminare/02-data/dataset.md` (Seminare, Orte, Termine, Leistungen), `../../michael/02-data/dataset.md` (Michael), `../../02-data/reviews.md` (Bewertungen). Brand und Fotos: `../../02-data/brand.md`, `../../01-input/INVENTORY.md`. Content Pool: `../../../content-pool/04-pool/pool.json` (lp:undersold), `findings-undersold.md`. Diese Datei enthält nur, was die Landingpage zusätzlich braucht.

## Quellen
- Q1 Copy Deck Round 3, Page 06 „Landing page template“, Treatment 3 Undersold: H1 „Ihr Unternehmen ist größer, | als es nach außen wirkt.“, Button „Gespräch buchen“ („Identical on all three. Only colour changes.“), „Warm golden palette, location photography.“ Offene Frage im Deck: du oder Sie (`../../02-data/copydeck-r3.txt` Z. 295 ff.).
- Q2 Design-Richtlinien, Abschnitt 02 Persona 03 „The Undersold“ (`quellen/meandyou-design-richtlinien.html`): Kernzeile „Dein Unternehmen ist größer, als du klingst.“; Ton „Weit, warm, goldenes Licht. Seltenheit statt laut. Souveränität durch Zurückhaltung und durch das, was weggelassen wird.“; Einsatz „Die Seminare, die Locations, das Bewerbungsformular, das private Follow-up. Das kleinste Publikum, der höchste Wert.“; Visuelles Ziel „Location und Gruppe sollen wie das eigentliche Produkt anführen. Nie Konferenz-Ästhetik, nie ein Hotel-Ballsaal.“; Layout „Breite Ausschnitte, viel Raum · Kleine Schrift vor großformatigem Bild · Weniger Elemente pro Bildschirm als überall sonst · Daten und Orte werden wie Überschriften behandelt · Ein CTA, weit unten auf der Seite, ohne Dringlichkeit“; Foto „Landschaft und Location vor Menschen · Goldene Stunde, lange Schatten · Kleine Gruppen, nie eine Menge · Keine Lanyards, keine Bühne, keine Ballsäle“.
- Q3 Freigegebene Startseiten-Copy (`../../04-copy/approved-copy.md` Z. 63 f.): Karte „Dein Unternehmen ist größer, als es nach außen wirkt.“ + „Die Substanz stimmt. Der Auftritt bleibt darunter. Nach außen wirkt das Unternehmen kleiner, als es ist.“ (du-Form, freigegeben).
- Q4 Vorschau v2 `lp-undersold.html` (curl + Screenshot 2026-10-12, `v2-lp-undersold-first-viewport-1440.png`). Section-Map unten.
- Q5 Freigegebene Copy Seminare, Michael, FAQ, Gespräch buchen (2026-10-12): `../../seminare/04-copy/approved-copy.md`, `../../michael/04-copy/approved-copy.md`, `../../faq/04-copy/approved-copy.md`, `../../termin/04-copy/approved-copy.md`.
- Q6 Content Pool lp:undersold (17 Items, Freigabe 2026-10-12): CP-BRD-301 bis 303, CP-LOC-301 bis 304, CP-SVC-301 bis 307, CP-AUT-301 bis 303. Findings F1 bis F5.
- Q7 Auftrag der Hauptsitzung (2026-10-12): Hero in du; ein CTA weit unten, Header-Button darf bleiben; kein Bewerbungsformular; Orte und Termine laut Live-Seite; Kostenfrage ohne Preis; 1:1-Coaching und Medientraining erst nach Kundenbestätigung; VHS, IHK, Bildungsurlaub gestrichen.

## 1. Aktuelle Seite (Q4) — Section-Map
| Nr | Sektion | Inhalt |
|---|---|---|
| 1 | Hero (dunkel #47403A, Foto rechts) | Label „Unter Wert“, H1 „Ihr Unternehmen ist größer, als es nach außen wirkt.“ (Sie-Form), Sub „Die Substanz stimmt. Der Auftritt bleibt darunter. …“, Button „Gespräch buchen“. Foto: Handschlag im Büro, Applaus, Mann mit Glatze und Brille |
| 2 | Warum Michael | H2 „30 Jahre. Über 8.000 Menschen. Eine Methode.“, Zahlen 30+ / 8.000+ / Top 100 Trainer / 9 Bücher, ERFOLG-Satz, Button |
| 3 | Die Methode | H2 „Wirkung beginnt nicht bei der Technik.“, Absatz (Copy Deck), 3 Schritte Persönlichkeit, Kongruenz, Wirkung |
| 4 | Stimmen | H2 „Was Teilnehmer sagen.“, 4 Zitate (Röser, Escher, Ates, Subotic) als Laufband, jedes dreimal im DOM, 3 Video-Buttons (1:00, 1:12, 1:23) |
| 5 | Abschluss | „Der nächste Schritt ist ein Gespräch.“, Button, Footer |

### 1.1 Technischer Zustand (gemessen 2026-10-12)
- Title „Landingpage Undersold · me&you Prototyp v2“. Keine Meta-Description, kein JSON-LD, kein robots-Tag im HTML.
- H1 ohne Keyword. 446 Wörter laut `wordcount.py` (Laufband dreifach und Footer mitgezählt; eindeutiger Inhalt rund 250).
- 3 Buttons „Gespräch buchen“ im Inhalt plus Header (Persona-Regel: ein CTA weit unten).
- Sektionen 100 vh, Seite rendert im Headless-Vollbild leer (nur ein Bildschirm sichtbar).
- Keine Orte, keine Termine, kein Format, keine Gruppengröße, kein „Für wen“, keine FAQ, kein Ablauf des Gesprächs, kein Preis-Hinweis (Findings F3).
- Zitat Subotic auf der Live-Seite ohne Zusammenhang („Ersteres ist manchmal genau so schwer wie Letzteres …“), Bundesliga-Bezug ist bei Michael K10 gestrichen.
- Hero-Foto zeigt Büro-Szene (Persona-Regel: Ort vor Menschen, keine Konferenz). Mann ähnelt Michael (Seminare K7).

## 2. Fakten für diese Seite (alle aus freigegebenen Quellen)
| # | Fakt | Wortlaut / Wert | Quelle |
|---|---|---|---|
| U1 | Hero (du) | „Dein Unternehmen ist größer, als es nach außen wirkt.“ | Q3, Q7 (Copy Deck Q1 in Sie) |
| U2 | Sub | „Die Substanz stimmt. Der Auftritt bleibt darunter. Nach außen wirkt das Unternehmen kleiner, als es ist.“ | Q3 |
| U3 | Format | 3 Tage Intensivtraining + 1 Tag Get Together, 3 Videoanalysen mit Sofort-Feedback, VR-Training | Seminare 2.1 |
| U4 | Gruppen | Frei sprechen 14, Ruhig bleiben 10, Mit Sprache führen 12 Plätze | Seminare 2.2 bis 2.4 |
| U5 | Formate (Arbeitstitel) | Frei sprechen (R I), Ruhig bleiben, wenn es eng wird (R II), Mit Sprache führen (R III), Rhetorik Bundle (2 Tage, ohne Termine) | Q5 Seminare S03, S04 |
| U6 | Bundle-Zielgruppe | „Führungskräfte, Entscheider:innen, Unternehmer:innen sowie Expert:innen aus Vertrieb, Marketing und Kommunikation“; Bausteine Elevator Pitches, Auftrittscoaching mit Videoanalyse, „Wirkung bewusst steuern“ | Seminare 2.5 (Q2 Bundle-PDF) |
| U7 | Termine | siehe Tabelle 3 | Seminare 2.7 (Live-Seite, Stand 2026-10-12) |
| U8 | Leistungen | Übernachtungen im Seminarzeitraum (3 Nächte), Snacks, Getränke, leichtes Frühstück; nicht: Anreise, Transfer, Hotelfrühstück, Abendessen | Seminare 2.8, nur mit gelber Marke |
| U9 | Storno | bis 8 Wochen vor Start gegen 30 Prozent, danach voller Preis | AGB, Seminare S11 |
| U10 | Michael | seit 1990; über 30 Jahre; über 8.000 Teilnehmer; neun Bücher als Autor oder Herausgeber; Lehrbeauftragter Universität St. Gallen; Rhetorik-Analyst für ARTE und WELT TV; laut ERFOLG Magazin Top 100 Trainer; arbeitet mit „Vorständen, mit Unternehmerinnen und Unternehmern und mit Menschen, die in der Öffentlichkeit stehen“; „Mandantennamen nennt er nicht.“ | Michael 2 (Q1 institut-ehlers.de) |
| U11 | Methode | „Persönlichkeit. Kongruenz. Wirkung.“ · „Die meisten Rhetoriktrainings starten bei Werkzeugen. Wir starten davor …“ · „Wirkung beginnt nicht bei der Technik.“ | Copy Deck, voice.md |
| U12 | Gespräch | 30 Minuten, kostenlos, per Video, mit einem Mitglied aus Michaels Team; Bestätigung per E-Mail, Erinnerung per WhatsApp; danach in Ruhe entscheiden | Q5 Gespräch buchen S01, S02 |
| U13 | Telefon | +49 15888367664 | Live-Seite Footer |
| U14 | ProvenExpert | 250 Bewertungen, 227 mit 5 Sternen | reviews.md B |
| U15 | Für wen | „Führungskräfte, Gründerinnen und Gründer sowie Beraterinnen und Berater“ (Seminare S09); Bundle: Vertrieb, Marketing, Kommunikation (U6) | Q5 |
| U16 | Mischung der Gruppen | Christin R.: „… ein Mix von Anfänger bis Profi …“ | reviews.md P4 |

## 3. Orte und Termine (Seminare 2.7, Live-Seite, nur künftige)
| Ort | Format | Termine |
|---|---|---|
| Mallorca | Frei sprechen | 3. bis 6.12.2026 · 4. bis 7.3.2027 · 29.4. bis 2.5.2027 · 14. bis 17.10.2027 |
| Dubai | Mit Sprache führen | 10. bis 13.12.2026 |
| Barcelona | Ruhig bleiben | 15. bis 18.4.2027 · 21. bis 24.10.2027 |
| Frankfurt | Frei sprechen | 17. bis 20.6.2027 |
| Berlin | Frei sprechen | 12. bis 15.8.2027 |
| Zypern | Mit Sprache führen | 7. bis 10.10.2027 |
Alle Termine beginnen an einem Donnerstag und enden am Sonntag (FAQ Q6, Kalender geprüft). Mexico „Rhetorik 4“ nicht auf der Seite (Seminare K4).

## 4. Stimmen für diese Persona (Unternehmer, Ort, Haltung)
| # | Zitat | Quelle | Einsatz |
|---|---|---|---|
| S1 | „Ein begeisterndes Training mit einer anregenden und humorvollen Atmosphäre. Rundum gelungen.“ | Sarna Röser, Bundesvorsitzende „Die Jungen Unternehmer“, Live-Seite | Unternehmerstimme |
| S2 | „Trotz 40 Jahren Medienerfahrung konnte ich erstaunlich viel vom Rhetoriktraining profitieren.“ | Peter Escher, Moderator MDR, Live-Seite | Erfahrene |
| S3 | „Statt ‚höher, schneller, perfekter‘ geht es um Authentizität, Substanz und das Vertrauen in die eigene Stimme.“ (Auszug) | Adrian Bourcevet, Google, 1 Jahr (G5) | Haltung, Substanz |
| S4 | „Dieses Training hat beruflich wie privat einiges in Bewegung gebracht. Ein intensiver Stretch der Komfortzone in wunderschönem Ambiente …“ | V., Rhetorik II Barcelona, ProvenExpert (P7) | Ort |
| S5 | „Aufgrund der tollen Atmosphäre und einzigartigen Lage lernt es sich sehr entspannt.“ | Christian S., Rhetorik I Mallorca, ProvenExpert (P1) | Ort |
| S6 | „… zwischen der ersten und der letzten Rede lagen wirklich Welten.“ | Jenny Eikel, Google (G7) | Erlebnis, keine Garantie |
Nicht verwenden: Neven Subotic (Bundesliga-Bezug gestrichen, Michael K10), Tajan Fattah (Partner), Google-Sternzahl 4,8.

## 5. Suchnachfrage (Content Pool, DataForSEO 2026-10-12)
- Führung: „rhetorik seminar“ 880, „führungskräfte kommunikation“ 210, „coaching für geschäftsführer“ 170, „kommunikationstraining führungskräfte“ 140, „executive presence“ 140, „rhetorik für führungskräfte“ 110, „rhetorik seminar für führungskräfte“ 40, „präsentationstraining“ 260, „pitch training“ 110, „auftrittscoaching“ 50, „souverän auftreten“ 50.
- Marke: „michael ehlers“ 480 (Obergrenze, Namensgleiche), „michael ehlers rhetorik“ 90.
- Orte: „rhetorik seminar frankfurt“ 90, „rhetorik seminar berlin“ 30, „seminar mallorca“ 20; Mallorca, Barcelona, Dubai als Rhetorik-Seminar ohne Daten. Autocomplete „rhetorik seminar mallorca“, „michael ehlers rhetorik mallorca“.
- PAA: „Was kostet ein Rhetorikkurs?“ (serp-31, serp-33), „Wie kann ich Rhetorik trainieren?“, „Was gehört zur Rhetorik?“ (serp-31), „Wie kommuniziere ich als Führungskraft richtig?“, „Was sind die 5 Säulen der Rhetorik?“ (serp-32), „Was kostet ein 1 zu 1 Coaching?“ (serp-33, nicht beantwortet, D4).
- SERP: Akademien (Haufe, IHK, manager-institut) halten „rhetorik für führungskräfte“. Folge (F2): Seite ist Anzeigen- und Premium-Seite, Führungsbegriffe in Title, H2 und „Für wen“, keine SEO-Money-Page.
- Keyword primär: „Rhetorik-Seminar für Führungskräfte und Unternehmer“ (Title, H1 klein). Kannibalisierung: `/seminare` zielt auf „Rhetorik-Seminare“ (Auswahl), Startseite auf „Rhetorik-Seminar“ (Marke).

## 6. Benchmark (Gate A0)
8 lesbare Wettbewerberseiten (Content Pool `metrics-undersold.json`, kopiert nach `content-writing/lp-undersold/_work/bench-metrics.json`): Median 1.194 Wörter, Untergrenze 836 (70 %). Ziel: 900 bis 1.300 Wörter (Persona: wenige Elemente, viel Raum; Länge über Orte, Termine und FAQ, nicht über Fließtext).
Bausteine bei Wettbewerbern (F3): Inhalte/Ziele 6 von 8, Buchung 6, Termine 5, Stimmen 5, Zielgruppe 4, Gruppe/Format 4, FAQ 2.

## 7. Konflikte und Compliance
| # | Fund | Quelle | Behandlung |
|---|---|---|---|
| K1 | Sie (Copy Deck, v2) vs. du (Startseite, ganze Website) | Q1, Q3 | du (Q7). Entscheidung an Martin gemeldet |
| K2 | Persona: „Bewerbungsformular, privates Follow-up“ vs. Copy Deck: „Gespräch buchen“ auf allen drei LPs | Q2, Q1 | Gespräch buchen (Q7), kein Formular |
| K3 | Persona: ein CTA weit unten vs. 741-Raster: CTA im ersten Bildschirm und alle 2 Sektionen | Q2, scorecard | ein Button im Inhalt weit unten, Header-Button bleibt sichtbar (Q7). Raster-Items 4 und 11 nach Persona-Regel bewertet |
| K4 | Mallorca 2027: PDF 22. bis 25.4. und 23. bis 26.9. vs. Live-Seite 29.4. bis 2.5., kein September | Seminare K1 | Live-Seite (Q7) |
| K5 | „5 Bücher“ (Copy Deck) vs. neun Bücher | Michael K1 | neun |
| K6 | Hero-Foto v2: Büro, Handschlag, Michael-ähnlicher Mann | Q4 | nicht verwenden; Ortsbild in goldenem Licht |
| K7 | Übernachtung, Verpflegung nur aus Sales-Checkliste | Seminare 2.8 | gelbe Marken |
| K8 | Seminarnamen offen | Seminare K6 | Themen-Titel, `[von Kunde bestätigen: Seminarname]` einmal |
| K9 | Leitet Michael jedes Seminar selbst? | Michael 6.3 | gelbe Marke |
| K10 | Person im Gespräch | Gespräch buchen | „Michaels Team“ + gelbe Marke |
| K11 | 1:1-Coaching, Medientraining (Pool CP-SVC-308, 309) | Q6 | nicht auf der Seite (Q7) |
| K12 | VHS, IHK, Bildungsurlaub, Inhouse (CP-SVC-310) | Q6 | gestrichen (Q7) |
| K13 | Ergebnisaussagen (Pool „Wirkung bewusst steuern“) | Seminare K8 | als Übung oder Lernziel, keine Garantie |
| K14 | „Seltenheit“ nicht über Dringlichkeit: kein „nur noch X Plätze“, kein Countdown | Q2, UWG | Plätze als Fakt (10, 12, 14), freie Plätze „erfährst du im Gespräch“ |
| K15 | Vorstände, Mandanten: keine Namen | Michael K4 | nur Gruppen nennen |

## 8. Offen [FEHLT]
1. du oder Sie für diese Seite (K1), Bestätigung Martin.
2. `[von Kunde bestätigen: Seminarname]`.
3. `[von Kunde bestätigen: Name und Rolle der Person im Gespräch]`.
4. Mallorca-Termine 2027 (K4).
5. Freigabe Sales-Checkliste: `[von Kunde bestätigen: Übernachtung]`, `[von Kunde bestätigen: Verpflegung]`.
6. `[von Kunde bestätigen: Leitet Michael die Seminare selbst]`.
7. Echte Fotos je Ort (heute Pexels).
8. Zitate von Unternehmern mit Einwilligung (heute Röser, Escher).
9. ProvenExpert-Gesamtnote wörtlich.
10. 1:1-Coaching und Medientraining: gibt es das (K11)?
11. Profil-URLs für sameAs.
