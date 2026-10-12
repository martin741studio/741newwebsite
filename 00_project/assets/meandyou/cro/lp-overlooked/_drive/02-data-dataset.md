# Dataset — Landingpage „The Overlooked“ me&you (Stand 2026-10-12)

Gemeinsame Fakten (nicht kopiert): `../../02-data/dataset.md` (Startseite), `../../michael/02-data/dataset.md`, `../../seminare/02-data/dataset.md`, `../../rhetorik/02-data/dataset.md`, `../../faq/02-data/dataset.md`. Bewertungen: `../../02-data/reviews.md`. Brand und Fotos: `../../02-data/brand.md`, `../../01-input/INVENTORY.md`.

## 0. Auftrag
Hauptsession (Martin, 2026-10-12): CRO-Lauf nach Workflow 4b für `lp-overlooked`, Persona „The Overlooked“. Stopp bei Checkpoint 1 (Copy), dann Checkpoint 2 (Prototyp). Port 8832. Nichts deployen.

Vorgaben der Hauptsession (bei Checkpoint 1 änderbar):
- D1 Hero: „Recht zu haben war nie das Problem.“ (Copy Deck R3, Page 06, vom Kunden freigegeben).
- D2 Einziger CTA: „Gespräch buchen“ → `/gespraech-buchen?utm_source=lp-overlooked&utm_content=<abschnitt>`.
- D3 Online-Kurs nur als eine Spalte in einer Formattabelle (Online-Kurs, Seminar, Gespräch), nur belegte Fakten. Kein Kurslink, keine Modulliste.
- D4 1:1-Coaching, Medientraining und die Antwort zu den „5 Säulen“ bleiben draußen, bis der Kunde sie bestätigt.

## 1. Quellen
| ID | Quelle | Stand |
|---|---|---|
| L1 | Content Pool, 17 Items `page_tag = lp:overlooked` (`content-pool/04-pool/pool.json`), Findings `findings-overlooked.md` | 2026-10-12, Checkpoint „go“ |
| L2 | Copy Deck Round 3, Page 06 „Landing page template“: „One structure, three treatments. Only these three lines change.“ Treatment 2: „Recht zu haben \| war nie das Problem.“ „Cool palette, architectural photography.“ Button „Gespräch buchen“, „Identical on all three. Only colour changes.“ | `../../02-data/copydeck-r3.txt` |
| L3 | Design-Richtlinien, Abschnitt 02: Ton „Gefasst, strukturiert, kühles Licht. Respektiert die Intelligenz der Leser:innen. Nirgends ein motivierender Ton.“ Einsatz „Der 999-Euro-Onlinekurs, die Methodenseiten, Michaels Referenzen, Vergleiche und FAQ.“ Layout „Sichtbares Raster, ausgerichtete Linien, nummerierte Schritte“, „Diagramm vor Dekoration“, „Tabellen und Vergleiche sind willkommen“, „Bildunterschriften transportieren echte Information“. Foto „Räume und Publikum, mit leichtem Abstand“, „Härteres Licht, architektonische Linien“, „Schwarz-Weiß ist hier erlaubt“. Nie: Preise, Gedankenstriche. | `../../../quellen/meandyou-design-richtlinien.html` |
| L4 | Live-Startseite meandyou.de, Story-Block: „Du sitzt in einem Meeting und erklärst deine Lösung. Aber statt Zustimmung bekommst du nur glasige Blicke zurück. Jemand im Raum unterbricht dich: ‚Können wir das vereinfachen?‘ Fünf Minuten später wiederholt ein Kollege deine Idee mit anderen Worten. Alle nicken begeistert. Und er bekommt das Lob...“ | `../../../ist-seite/index.html`, Abruf 2026-10-11 |
| L5 | Live-FAQ meandyou.de, Frage 11: „Wie lange habe ich Zugang zum Online-Kurs und der Community? Mindestens 12 Monate.“ Frage 10: „ein klar strukturiertes System für dein Tempo, plus persönliche Betreuung durch Q&A, Feedback und Community“ (nicht freigegeben, siehe K7) | wie L4 |
| L6 | Freigegebene Copy: Startseite (`../../04-copy/approved-copy.md`), Michael, Seminare, Rhetorik, FAQ | 2026-10-11/12 |
| L7 | Seminarinhalte R I bis R III (Kursinhalte-PDF, Wortlaut in `../../seminare/02-data/dataset.md` 2.2 bis 2.4) | 2026-10-11 |
| L8 | Podcast „Unübersehbar“ (Folgentexte, `../../rhetorik/02-data/dataset.md` R5): „Kommunikation ist ein Raum, und wer ihn nicht selbst bespielt, überlässt ihn anderen“ | 2026-10-12 |
| L9 | Vorschau v2 `prototype-v2/lp-overlooked.html` (curl + Screenshot, 2026-10-12) | 2026-10-12 |

## 2. Aktuelle Seite (L9)
Reihenfolge: Hero („Das Problem“, H1 „Recht zu haben war nie das Problem.“, Sub = Startseiten-Karte, Button, KI-Bild Glastisch) → „Warum Michael“ (H2 „30 Jahre. Über 8.000 Menschen. Eine Methode.“, Zahlen 30+ / 8.000+ / Top 100 Trainer / 9 Bücher, ERFOLG-Satz, Button) → Methode (3 Schritte) → „Stimmen“ (H2 „Was Teilnehmer sagen.“, Zitate als Laufband, 3 Videos 1:00/1:12/1:23) → Abschluss („Der nächste Schritt ist ein Gespräch.“).
- Etwa 223 sichtbare Wörter (ohne Kopf, Fuß und Laufband-Dubletten). Benchmark-Median 1.704, Untergrenze A0 1.193 (`pool.json` meta.benchmark.overlooked).
- Title „Landingpage Overlooked · me&you Prototyp v2“. Keine Meta-Description, kein Canonical, kein JSON-LD, kein `noindex`.
- H1 ohne Suchbegriff. H2 sind Aussagen. Keine FAQ, keine Tabelle, kein Diagramm, kein Ablauf des Gesprächs, keine Bewertungszahl.
- Erster Bildschirm 1440 × 900: H1, Sub, Button sichtbar. Keine Beweiszeile. Button hellgrau auf Navy (schwacher Kontrast). Screenshots `v2-lp-overlooked-first-viewport-1440.png`, `v2-lp-overlooked-full-1440.png` (8.427 px).
- Zitate: Neven Subotic (Satz ohne Zusammenhang: „Ersteres ist manchmal genau so schwer wie Letzteres …“), Laufband (Karussell).
- Heute schon korrigiert (Hauptsession): 9 Bücher, Top 100 Trainer, kein „bekanntesten“, kein „Vorher. Nachher.“.

## 3. Fakten für diese Seite
| ID | Fakt (Wortlaut) | Quelle |
|---|---|---|
| F1 | Michael trainiert seit 1990, „über 30 Jahre“ | michael K5, Startseite K1 |
| F2 | über 8.000 Teilnehmer | Live-Seite |
| F3 | neun Bücher als Autor oder Herausgeber | michael K1 |
| F4 | „laut ERFOLG Magazin Top 100 Trainer“ im deutschsprachigen Raum | michael K2, Startseite K5 |
| F5 | Lehrbeauftragter an der Universität St. Gallen | michael Q1 |
| F6 | Rhetorik-Analyst, angefragt von ARTE und WELT TV | michael Q1 |
| F7 | Podcast „Unübersehbar“ seit 2008, alle zwei Wochen | michael Q3 |
| F8 | ProvenExpert: 250 veröffentlichte Bewertungen, 227 mit 5 Sternen. Google-Sternwert nie zeigen (Hauptsession) | reviews B |
| F9 | Methode „Persönlichkeit. Kongruenz. Wirkung.“, Zeilen 01 bis 03, „Die meisten Rhetoriktrainings starten bei Werkzeugen …“ | Copy Deck, Startseite S05 |
| F10 | Seminar: 3 Tage Training + 1 Tag Get Together, 3 Videoanalysen mit Sofort-Feedback, VR-Training, 10 bis 14 Plätze, Orte Mallorca, Barcelona, Dubai, Frankfurt, Berlin, Zypern | Startseite S06, S09 |
| F11 | R II Inhalte: Schlagfertigkeit, Überzeugungspsychologie („Motive erkennen, Argumente gezielt platzieren“), Angriffe abwehren („Unfaire Methoden durchschauen und kontern“), Körpersprache lesen, Meetings führen („Diskussionen leiten, Ergebnisse klar sichern“) | L7 |
| F12 | R I: „In 2 Minuten ein starkes Statement setzen“, „Mit klarer Formel jede Rede aufbauen“, „Mit den richtigen Fragen Gespräche lenken“. R III: „Gruppen überzeugen“, „Zuhören meistern“, „Stegreifrede halten“, DeepOcean | L7 |
| F13 | Gespräch: 30 Minuten, kostenlos, per Video, mit Michaels Team; „Wir klären, wo du stehst und welches Format passt.“ Bestätigung per E-Mail, Erinnerung per WhatsApp | Startseite S07, Copy Deck |
| F14 | Online-Kurs: Selbstlernkurs mit Video-Lektionen (freigegebene FAQ-Antwort Startseite); Zugang mindestens 12 Monate (L5) | L6, L5 |
| F15 | Für wen: „Führungskräfte · Gründerinnen und Gründer · Beraterinnen und Berater“ | Copy Deck „Who it is for“ |
| F16 | Startseiten-Karte: „Du bist bestinformiert im Raum. Gefolgt wird trotzdem jemand anderem. Zwischen Kompetenz und Wirkung liegt eine Lücke.“ | Copy Deck, Startseite S03 |
| F17 | Telefon +49 15888367664 | Live-Seite Footer |

## 4. Bewertungen für diese Persona (Wortlaut, `reviews.md`)
| ID | Auszug | Quelle | Nutzung |
|---|---|---|---|
| G12 | „Michael Ehlers zeigt, wie man nicht nur spricht, sondern wirklich gehört wird.“ | Google, Firmenkonto „AfO Worldwide“ | ohne Namen, „Bewertung bei Google“; Freigabe offen |
| G8 | „Statt starrer Schemata, die nur Kopien erzeugen, gibt er einem die richtigen Werkzeuge an die Hand, um selbst zum Rhetorik-Experten zu werden.“ | Google, Jan Barthauer | „Jan B.“ wie Startseite (Initial) |
| G5 | „Ich habe gelernt, meine innere Haltung zum Ausgangspunkt jeder Präsentation zu machen […] Wie ich spreche, wie ich wirke, wie ich wahrgenommen werde.“ | Google, Adrian B. | wie Startseite freigegeben |
| P5 | „Die Trainings vor der Kamera mit den darauf folgenden Auswertungen helfen die Selbst- und Fremdwahrnehmung zu schärfen.“ | ProvenExpert, Julian L. | wie Startseite freigegeben |
| C-PE | „Trotz 40 Jahren Medienerfahrung konnte ich erstaunlich viel vom Rhetoriktraining profitieren.“ | Peter Escher, Moderator MDR, Live-Seite | wie Startseite |
| G9 | „Ich habe in diesem Kurs mehr gelernt als in all meinen bisherigen Schulungen zusammen.“ | Google, Emrullah A. | wie Startseite FAQ |
Video-Stimmen: 3 echte Wistia-Videos (1:00, 1:12, 1:23).

## 5. Suchnachfrage (Pool, DataForSEO 2026-10-12)
| Keyword | Volumen | Item |
|---|---|---|
| rhetorik kurs / rhetorik kurse | 1.600 / 1.600 | CP-BRD-204, CP-SVC-202 |
| rhetorik seminar | 880 | CP-SVC-203 |
| durchsetzungsvermögen | 880 (meist Wörterbuch- und Bewerbungsabsicht) | CP-SVC-204 |
| michael ehlers | 480 | CP-AUT-201 |
| rhetorik online kurs / kurs online | 210 / 210 | CP-SVC-201 |
| überzeugungskraft | 170 | CP-SVC-204 |
| argumentationstraining | 70 | CP-SVC-204 |
| gehör verschaffen | 50 | CP-BRD-201 |
| souverän auftreten | 50 | CP-SVC-205 |
| überzeugend argumentieren | 40 | CP-SVC-204 |
| durchsetzungsvermögen lernen | 30 | CP-SVC-204 |
| 5 säulen der rhetorik | 30 | CP-AUT-205 (raus, D4) |
| nicht gehört werden | 20 | CP-BRD-201 |
| kompetent wirken | 10 | CP-BRD-203 |
PAA: „Was bringt ein Rhetorikkurs?“, „Was kostet ein Rhetorikkurs?“, „Wie lerne ich am besten Rhetorik?“, „Wie kann ich Durchsetzungsvermögen lernen?“, „Welche Kompetenz ist Durchsetzungsvermögen?“, „Welche Rhetorikseminare sind am besten?“ (nicht beantwortet: Vergleich mit Anbietern, UWG). Autocomplete: „kann man durchsetzungsvermögen lernen“, „wie souverän auftreten“, „nicht ernst genommen werden im job“.
Benchmark (`content-pool/02-competitors/metrics-overlooked.json`): 7 lesbare Seiten, Median 1.704 Wörter. Typische H2: Format online, Kursinhalt/Module, Trainer, Kundenstimmen, FAQ, „Was bringt …“. Keine Seite nennt die Lücke „Recht haben, nicht gehört werden“ (Finding 3).

## 6. Konflikte und Compliance
| # | Fund | Behandlung |
|---|---|---|
| K1 | Pool/Richtlinie: Online-Kurs ist das Persona-Produkt. Copy Deck: einziger CTA Gespräch. FAQ-Lauf: Kurs ist kein Ziel der Website | D2, D3: Kurs nur in der Formattabelle, Entscheidung Martin |
| K2 | Kursname „Rhetorik für Intelligente“ (Live) vs. „Intelligente“ kein Hauptbegriff mehr | Kurs ohne Namen: „Online-Kurs“ `[von Kunde bestätigen: Kursname]` |
| K3 | Live-FAQ: „in 30 Tagen“, „Investition, die sich schnell auszahlt“, „garantiert“ | nicht übernommen (Ergebnisversprechen, UWG) |
| K4 | Live: „5x mehr und schneller Lösungen“ | nicht übernommen (kein Beleg) |
| K5 | Pool: „Durchsetzungsvermögen“ 880, aber Absicht gemischt | nur „Durchsetzungsvermögen lernen“ als FAQ, kein Versprechen „sofort durchsetzen“ |
| K6 | Laufband-Zitat Neven Subotic ohne Zusammenhang | nicht übernommen |
| K7 | Live-FAQ 10: Q&A, Feedback, Community im Kurs | nicht übernommen, `[von Kunde bestätigen: Extras des Online-Kurses]` |
| K8 | G12 ist ein Firmenkonto | Zitat ohne Namen, Freigabe im Handoff |
| K9 | Wettbewerber mit Geld-zurück-Garantie (rhetorik-fuehrerschein.de) | keine Rückgabe-Aussage ohne Kundenfakt (UWG) |
| K10 | „5 Säulen der Rhetorik“ (PAA, 30) | draußen (D4) |
| K11 | Wer führt das Gespräch? | „Michaels Team“ wie Startseite, `[von Kunde bestätigen: Name und Rolle]` |

## 7. Offen [FEHLT]
1. Kursname (K2). 2. Lektionen: Anzahl, Länge, Module. 3. Zugang 12 Monate bestätigen, Extras (K7), Plattform, Geräte. 4. Kauf direkt oder nur über das Gespräch. 5. Welche R-II-Themen der Kurs abdeckt. 6. Ein Satz und eine Übung je Methodenschritt. 7. Person im Gespräch (K11). 8. Namensfreigabe G12 (K8). 9. Logo-Rechte ARTE, WELT TV, Universität St. Gallen, ERFOLG Magazin. 10. Schriftliche Rückgaberegel (nur dann Risk-Reversal).
