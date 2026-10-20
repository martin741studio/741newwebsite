# Dataset — Seminarseite me&you / Michael Ehlers (Stand 2026-10-12)

Gemeinsame Fakten (Michael, Bewertungen, Gespräch, Brand, Fotos): `../../02-data/dataset.md`, `../../02-data/reviews.md`, `../../02-data/brand.md`, `../../01-input/INVENTORY.md`. Diese Datei enthält nur, was die Seminarseite zusätzlich braucht.

Quellen dieses Laufs:
- Q1 PDF „2026 Michael Ehlers Kursinhalte R1-R3 4 Tage“ (Downloads, 28.09.2026)
- Q2 PDF „Rhetorik Bundle Preisliste“ (Downloads, 28.09.2026; Preise nicht übernommen)
- Q3 PDF „Rhetorik-Seminar Termine 2027“ (Downloads, 28.09.2026)
- Q4 PDF „Checkliste Sales MeandYou“ (Downloads, 28.09.2026)
- Q5 Live-Seite meandyou.de, Terminblöcke (Firecrawl, maxAge 0, 2026-10-12)
- Q6 Copy Deck Round 3, Page 02 Seminare (`../../02-data/copydeck-r3.txt` Z. 175–255)
- Q7 Vorschau v2 `https://clients.741.studio/meandyou/v2/seminare.html` (Quelle `prototype-v2/build_v2.py`)
- Q8 Freigegebene Startseiten-Copy (`../../04-copy/approved-copy.md`, S06, S09, S10)

## 0. Auftrag
Martin 2026-10-12: „den Prozess auch durchgehen für die Seminarseite … die muss überarbeitet werden.“ Basis: Seminarseite der Vorschau v2 (Q7), auf die die neue Startseite verlinkt. Die Live-Seite meandyou.de hat keine eigene Seminarseite (Links nur `/seminare-termin`, Impressum, Datenschutz, AGB). Ziel-URL neu: `/seminare`. CTA: Gespräch buchen → Terminseite (wie Startseite).

## 1. Aktuelle Seite (Q7) — Section-Map
| Nr | Sektion | Inhalt |
|---|---|---|
| 1 | Hero (Vollbild-Foto) | Label „Seminare“, H1 „Ein Einstieg. Dann dein eigener Weg.“, „Kein Stufenmodell mehr. Ein klarer Einstieg, danach eigenständige Formate, die du frei wählst.“ Kein Button im Hero |
| 2 | Der Einstieg | „Arbeitstitel: Rhetorik I“, H2 „[Seminar A]“, ein Satz aus Q1, 7 Themen-Stichworte, „14 Plätze“, Button |
| 3 | Die Formate | H2 „Eigenständig. In beliebiger Reihenfolge.“, 3 Karten [Seminar B] R II (10 Plätze), [Seminar C] R III (12 Plätze), [Seminar D] Rhetorik Bundle („Rhetorik I und II“), je Stichworte + Button |
| 4 | Im Raum | H2 „Drei Tage, zwölf Menschen, kein Publikum.“, Faktenreihe 3 + 1 / 3 Videoanalysen / VR / 10–14 Plätze |
| 5 | Orte | H2 „Der Ort ist Teil der Arbeit.“, 6 Bildkarten mit Monaten (z. B. Mallorca „März · April · September · Oktober 2027“) |
| 6 | Für wen | Führungskräfte · Gründerinnen und Gründer · Beraterinnen und Berater |
| 7 | Abschluss | „Der nächste Schritt ist ein Gespräch.“ Button, Footer |

### 1.1 Technischer Zustand (gemessen, Chrome 1494 × 863)
- Title „Seminare · me&you Prototyp v2“, keine Meta-Description, kein JSON-LD, kein robots-Tag.
- H1 ohne Keyword. H2 „[Seminar A]“ ist ein Platzhalter. H3 [Seminar B–D].
- 7 Sektionen je 100 vh (863 px), Seitenhöhe 6.041 px, 266 Wörter sichtbar.
- Kein Button im ersten Bildschirm außer im Header. 66 Textstellen unter 16 px.
- Keine Bewertung, kein Zitat, kein Video auf der Seite. Keine FAQ. Kein Ablauf des Gesprächs. Keine konkreten Termine (nur Monate).
- Hero-Bild `ai-seminar-room.webp`: KI-Bild eines Trainers mit Glatze und Brille, sieht Michael ähnlich (siehe K7).
- Screenshot: `v2-seminare-first-viewport-1440.png`.

## 2. Seminare (Fakten)
### 2.1 Gemeinsam für Rhetorik I, II, III (Q1)
„3 Tage Intensivtraining + 1 Tag Get Together“ · „3 Videoanalysen mit Sofort-Feedback“ · „Einzigartiges VR-Training“ · R I „Worksheets & Übungen“, R II und R III „Exklusive Strategien & Workbooks“.

### 2.2 Rhetorik I (Arbeitstitel; Einstieg) — Q1
- Plätze: „14 exklusive Teilnehmerplätze“.
- Inhalte (wörtlich): „Sicher Auftreten I Angstfrei vor Menschen reden, ohne Zittern“ · „Rede Halten I In 2 Minuten ein starkes Statement setzen“ · „Struktur Lernen I Mit klarer Formel jede Rede aufbauen“ · „Echt Wirken I Deinen eigenen, überzeugenden Redestil finden“ · „Sprache Nutzen I Auch Kritik charmant und souverän ausdrücken“ · „Körper Lesen I Gestik gezielt einsetzen statt unbewusst zappeln“ · „Fragen Stellen I Mit den richtigen Fragen Gespräche lenken“.
- „Wo stehst du nach dem Seminar“ (Q1, Ergebnisaussagen des Kunden): frei und professionell sprechen ohne zu verhaspeln; mit Lampenfieber ruhig auftreten; Gespräche mit Fragen lenken; schwierige Fragen gelassen meistern; Argumente, denen Menschen folgen.
- Orte (Q5): „Mallorca & Deutschland Rhetorik 1“ → Mallorca, Frankfurt, Berlin.

### 2.3 Rhetorik II (Arbeitstitel) — Q1
- Plätze: „Limitierte Gruppe mit nur 10 Plätzen“.
- Inhalte: „Schlagfertigkeit zeigen I Auf Angriffe schnell und präzise reagieren“ · „Überzeugungspsychologie nutzen I Motive erkennen, Argumente gezielt platzieren“ · „Angriffe abwehren I Unfaire Methoden durchschauen und kontern“ · „Körpersprache lesen I Signale erkennen, bewusst für Wirkung einsetzen“ · „Meetings führen I Diskussionen leiten, Ergebnisse klar sichern“.
- Nach dem Seminar (Q1): Sprache professionell in Rede, Präsentation, Alltag; spontane Fragen souverän; aus Sicht der Zielgruppe argumentieren; unvorhersehbare Situationen schlagfertig; Selbstbewusstsein durch Verständnis der eigenen Wirkung.
- Ort (Q5): „Barcelona Rhetorik 2“.

### 2.4 Rhetorik III (Arbeitstitel) — Q1
- Plätze: „Limitierte Gruppe mit nur 12 Plätzen“.
- Inhalte: „DeepOcean I Persönlichkeit prägt deine Rhetorik entscheidend“ · „Führen lernen I Kritik klar, motivierend formulieren“ · „Zuhören meistern I Kunden und Partner wirklich verstehen“ · „Stegreifrede halten I Spontan sprechen und sofort überzeugen“ · „Gruppen überzeugen I Methoden großer Redner im Alltag“.
- Nach dem Seminar (Q1): Aussagen mit Wirkung; Gespräche mit Klarheit führen; in unerwarteten Situationen souverän; Sicherheit unter Druck; komplexe Inhalte einfach präsentieren.
- Orte (Q5): 2026 „Dubai Rhetorik 3“, 2027 „Zypern Rhetorik 3“.

### 2.5 Rhetorik Bundle — Q2
- „Rhetorik 1 & Rhetorik 2“, „Dieses exklusive 2-Tages-Seminar richtet sich an Führungskräfte, Entscheider:innen, Unternehmer:innen sowie Expert:innen aus Vertrieb, Marketing und Kommunikation.“
- Bausteine: Analyse deiner Körpersprache & Wirkung · Sprache als Führungsinstrument · Storytelling, Elevator Pitches, Schlagfertigkeit · Auftrittscoaching mit Videoanalyse · Wirkung auf der Bühne, im Vertrieb & im Alltag.
- Nach dem Training: souverän & schlagfertig kommunizieren · Manipulation sofort erkennen · Gespräche und Meetings gezielt führen · frei, sicher & überzeugend sprechen · Wirkung bewusst steuern.
- Keine Termine, kein Ort in keiner Quelle. Siehe K3.

### 2.6 Rhetorik 4 Mexico — Q5
- „Mexico Rhetorik 4“, „21.01.27-24.01.27 (3-Tages-Seminar)“, Preis sichtbar. Keine Inhalte in keiner Quelle. Siehe K4.

### 2.7 Termine (nur künftige, Stand 2026-10-12)
Quelle Q5 (Live-Seite), weil die Startseiten-Copy (Q8, freigegeben) dieselben Daten nutzt:
| Format | Ort | Termine |
|---|---|---|
| R I | Mallorca | 3.–6.12.2026 · 4.–7.3.2027 · 29.4.–2.5.2027 · 14.–17.10.2027 |
| R I | Frankfurt | 17.–20.6.2027 |
| R I | Berlin | 12.–15.8.2027 |
| R II | Barcelona | 15.–18.4.2027 · 21.–24.10.2027 |
| R III | Dubai | 10.–13.12.2026 |
| R III | Zypern | 7.–10.10.2027 |

### 2.8 Leistungen rund um das Seminar (Q4, Freigabe Kunde offen)
- Übernachtungen im offiziellen Seminarzeitraum enthalten (Beispiel 05.–08.: 3 Nächte, 4 Seminartage). Zusätzliche Nächte nicht.
- An- und Abreise, Transfer nicht enthalten.
- Enthalten: Seminarverpflegung/Tagespauschale (Snacks, Getränke), leichte Frühstücksverpflegung im Seminar. Nicht enthalten: Hotelfrühstück, Abendessen.
- Begleitpersonen: Kosten nicht übernommen, Upgrade selbst beim Hotel.
- Absage durch Teilnehmer: keine Rückerstattung (AGB), Gutschein für ein künftiges Seminar.
→ Auf der Seite nur mit Marke `[von Kunde bestätigen: …]` (wie Startseite Flag F4).

## 3. Suchnachfrage
Volumen aus dem Startseiten-Lauf (DataForSEO 2026-10-11, `../../02-data/demand/`). Ein neuer Abruf am 2026-10-12 scheiterte: DataForSEO meldet „Your IP is not whitelisted“ (40207). Ersatz: Google-Autocomplete (`demand/autocomplete.json`).
- Relevante Volumen: rhetorik seminar 880 · rhetorik kurs 1.600 · rhetorik für führungskräfte 110 · rhetorik seminar frankfurt 90 · michael ehlers rhetorik 90 · rhetorik seminar führungskräfte 40 · schlagfertigkeit seminar 40 · rhetorik seminar berlin 30 · Mallorca, Barcelona: keine Daten.
- Autocomplete: „rhetorik seminar für führungskräfte / für anfänger / für geschäftsführer“, „rhetorik intensivtraining“, „michael ehlers rhetorik seminar“, „schlagfertigkeit lernen / trainieren“, „stegreifrede halten / übung“.
- Kannibalisierung: Die Startseite zielt auf „Rhetorik-Seminar“. Die Seminarseite zielt auf die Auswahl: **„Rhetorik-Seminare: Inhalte, Orte und Termine“** plus Formate (Einstieg/Anfänger, Schlagfertigkeit, Führung). Keyword primär: „Rhetorik-Seminare“.

## 4. Konflikte und Compliance
| # | Fund | Quelle | Behandlung |
|---|---|---|---|
| K1 | Mallorca 2027: Q3 nennt 22.–25.4. und 23.–26.9.; Live-Seite (Q5) nennt 29.4.–2.5. und keinen Septembertermin | Q3, Q5 | Q5 verwenden (aktuell gepflegt, gleich wie freigegebene Startseite). Flag an Martin |
| K2 | Q7 Mallorca „März · April · September · Oktober 2027“ (enthält September aus Q3) | Q7 | ersetzt durch Daten aus Q5 |
| K3 | Bundle = „2-Tages-Seminar“, alle anderen 3 + 1 Tage; keine Termine, kein Ort | Q2 | als vierte Karte nur mit `[von Kunde bestätigen: Termine und Ort Bundle]`; Entscheidung Martin, ob Bundle auf die Seite gehört |
| K4 | Mexico „Rhetorik 4“ ohne Inhalte, mit Preis | Q5 | nicht auf der Seite (keine Inhalte, keine Preise). Flag |
| K5 | „Drei Tage, zwölf Menschen“ (Q6/Q7) vs. 10, 12, 14 Plätze (Q1) | Q6, Q1 | „höchstens 14 Menschen“ bzw. Plätze je Format |
| K6 | „Kein Stufenmodell mehr“ (Q6) vs. Bundle „Rhetorik 1 & Rhetorik 2“ und Arbeitstitel I, II, III | Q6, Q2 | Formate ohne Reihenfolge darstellen, Arbeitstitel nur als Marke `[von Kunde bestätigen: Seminarname]` |
| K7 | Hero-Bild Q7 zeigt KI-Trainer, der Michael ähnelt | Q7 | nicht verwenden (Regel: Michaels Gesicht nie erfinden). Echtes Foto oder Gruppenbild ohne Trainer |
| K8 | Ergebnisaussagen „Wo stehst du nach dem Seminar“ (Q1) | Q1 | als Lernziele formulieren („Du übst …“, „Du lernst …“), keine Garantie (UWG) |
| K9 | „Angstfrei vor Menschen reden, ohne Zittern“ | Q1 | nicht als Versprechen; „mit Lampenfieber umgehen“ |
| K10 | Gendern „Entscheider:innen“ (Q2) | Q2 | Startseiten-Stil: „Führungskräfte, Gründerinnen und Gründer“ |
| K11 | Preise in Q1, Q2, Q5 | — | nie auf der Seite (Regel Martin) |

## 5. Offene Punkte [FEHLT]
1. `[von Kunde bestätigen: Seminarname]` für R I, R II, R III (und Bundle).
2. `[von Kunde bestätigen: Termine und Ort Bundle]`, Bundle ja/nein.
3. Mallorca-Termine 2027 (K1).
4. `[von Kunde bestätigen: Name und Rolle der Person im Gespräch]`.
5. Freigabe Sales-Checkliste (Übernachtung, Verpflegung, Absage).
6. Echte Seminarfotos (Raum, Gruppe, Übung).
7. Was ist DeepOcean genau (ein Satz Erklärung)? Q1 nennt nur „Persönlichkeit prägt deine Rhetorik entscheidend“.
