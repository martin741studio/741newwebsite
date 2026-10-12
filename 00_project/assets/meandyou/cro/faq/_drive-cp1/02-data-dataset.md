# Dataset — Seite „FAQ“ me&you (Stand 2026-10-12)

Gemeinsame Fakten: `../../02-data/dataset.md` (Startseite), `../../seminare/02-data/dataset.md`, `../../michael/02-data/dataset.md`, `../../rhetorik/02-data/dataset.md`. Bewertungen: `../../02-data/reviews.md`. Brand und Fotos: `../../02-data/brand.md`, `../../01-input/INVENTORY.md` (nicht kopiert).

## Quellen
- Q1 Copy Deck Round 3, Page 05: H1 „Häufige Fragen“ (EN „Frequently asked questions“). Navigation: „Seminare · Michael · Was ist Rhetorik · Stimmen · FAQ“.
- Q2 Vorschau v2 faq.html (2026-10-12, curl + Screenshot): 10 Fragen im Akkordeon, 286 Wörter, Title „FAQ · me&you Prototyp v2“, `noindex, nofollow`, kein JSON-LD, kein CTA außer Header-Button, keine Gruppen. Quellen der v2-Antworten laut `build_v2.py`: Kursinhalte R1-R3 (1 Frage), Sales-Checkliste Entwurf (5 Fragen, Freigabe Kunde offen), Live-Seite (2), Skool-Briefing „Talk to Me“ (2). Screenshots `v2-faq-first-viewport-1440.png`, `v2-faq-full-1440.png`.
- Q3 Live-Startseite meandyou.de, FAQ-Block „Hier findest du Antworten auf mögliche Fragen und Einwände“ (13 Fragen, `ist-seite/index.html`, Abruf 2026-10-11). Wortlaut und Entscheidung je Frage: Tabelle unten.
- Q4 Freigegebene Copy der Geschwisterseiten (2026-10-11/12): `../04-copy/approved-copy.md` (Startseite, FAQ 12 Fragen), `../seminare/04-copy/approved-copy.md` (FAQ 9), `../michael/04-copy/approved-copy.md` (FAQ 8), `../rhetorik/04-copy/approved-copy.md` (FAQ 10). Alle verlinken auf `/faq`.
- Q5 Kontakt Live-Seite (Footer): Telefon +49 15888367664, E-Mail management@meandyou.de, Formular „Fragen vorab? Schreiben Sie uns.“ (Sie-Form).
- Q6 Termine laut Live-Seite (Stand 2026-10-11): alle elf künftigen Termine beginnen an einem Donnerstag und enden am Sonntag (Kalender geprüft 2026-10-12: 3.12.2026, 10.12.2026, 21.1.2027, 4.3.2027, 15.4.2027, 29.4.2027, 17.6.2027, 12.8.2027, 7.10.2027, 14.10.2027, 21.10.2027 sind Donnerstage).
- Q7 Terminseite v2 `termin.html` (741-Entwurf 08.10.): „Mit wem spreche ich? Mit einem Mitglied aus Michaels Team.“, „Was kostet das Gespräch? Nichts. Es gibt keine Verpflichtung.“, Vorbereitung „Einen ruhigen Ort · Stift und Papier · Eine konkrete Situation“, „In deiner Bestätigung ist ein Link, mit dem du in zwei Klicks umbuchst.“ (Calendly-Standard).
- Q8 Bewertungen ProvenExpert (`reviews.md` B): Julian L. „Michael schafft es, das Maximum aus einem rauszuholen und die Redeangst zu nehmen.“ (Rhetorik 1 Mallorca, 2023); Jasmina L. „Die Herangehensweise und das individuelle Feedback haben mich sehr motiviert …“; Michael B. (Feedback von Michael und Gruppe, VR „unglaublich real“); Christin R. (Mix von Anfänger bis Profi).

## Suchnachfrage
Keine eigene Suchnachfrage für „FAQ“. Die Seite sammelt die Fragen, die Besucher vor einer Buchung stellen, und die echten PAA der Geschwister-Läufe:
- PAA „rhetorik seminar“ (SERP DE 2026-10-11, `../../02-data/demand/serp1-out.json`): „Was macht man in einem Rhetorik-Seminar?“, „Was kostet ein Rhetorik-Seminar?“, „Wie lerne ich am besten Rhetorik?“, „Welche Übungen kann ich machen, um Rhetorik zu trainieren?“, „Was sind die 5 Säulen der Rhetorik?“, „Was sind die 3 Säulen der Rhetorik?“.
- PAA „rhetorik für führungskräfte“ (`serp2-out.json`): „Wie lernt man gute Rhetorik?“.
- Autocomplete (`autocomplete.json`): „was ist ein rhetorik seminar“, „was kostet ein rhetorik seminar“, „rhetorik seminar online“; „wer ist michael ehlers“, „michael ehlers kritik“.
- Verwandte Suchen: „Rhetorik Seminar Wochenende“, „Rhetorik Seminar für Anfänger“, „Rhetorik Seminar Führungskräfte“, „Rhetorik Seminar Bildungsurlaub“, „Rhetorik Seminar online“.
- Volumen (DataForSEO 11.10.): „rhetorik seminar“ 880, „rhetorik lernen“ 210, „michael ehlers“ 480. DataForSEO am 12.10. blockiert (IP nicht freigegeben, Flag S12 der Seminarseite).

## Benchmark (FAQ-Seiten von Rhetorik-Anbietern, `content-writing/faq/_work/bench-metrics.json`, 2026-10-12)
| Seite | Wörter | Art |
|---|---|---|
| kct-de.com/faqs | 497 | Anbieter-FAQ |
| rhetorik-im-schloss.de/faq | 794 | Anbieter-FAQ |
| seminar-institut.de/faq | 858 | Anbieter-FAQ, FAQPage-Schema |
| uwefreund.com FAQ Seminare | 593 | Anbieter-FAQ |
| timchristophergasse.de/faq | 3.746 | Wissens-FAQ |
| rhetorikhelden.de/rhetorik-faq | 4.023 | Wissens-FAQ (25 Fragen) |
| karstennoack.de FAQ Präsentation | 3.480 | Wissens-FAQ (33 Fragen) |
Median 858 Wörter. Anbieter-FAQs 500 bis 860 Wörter, Wissens-FAQs 3.500 bis 4.000. Die me&you-Seite verbindet beides (Buchungsfragen plus Rhetorik allgemein, Details auf den Fachseiten): Ziel 1.600 bis 2.400 Wörter.

## Live-FAQ (Q3): Entscheidung je Frage
| # | Live-Frage (Kurzform) | Entscheidung | Grund |
|---|---|---|---|
| L1 | „Kann ich mir das nicht auch einfach auf Youtube beibringen?“ | neu schreiben, mit L7 zusammen: „Reichen Bücher und Videos nicht?“ | „Zeit ist Geld“ und „System + Community“ beschreiben den Online-Kurs; Kern (Wissen ohne Übung) bleibt |
| L2 | „Ich bin sehr introvertiert …“ | behalten, auf Seminar umgestellt | Kundenwendung „Präzision und Ruhe“ bleibt |
| L3 | „Was, wenn ich keine Fortschritte … mache?“ | neu schreiben ohne „garantiert“ | K4 Startseite: Garantie ohne Grundlage (UWG) |
| L4 | „Kann ich dir meine Fragen auch persönlich stellen?“ | neu schreiben: Gespräch vorher, Feedback im Seminar, Kontakt | Q&A gehört zum Online-Kurs |
| L5 | „Der Kurs ist mir zu teuer …“ | streichen, ersetzt durch „Was kostet …?“ | Einwand-Rhetorik („Was kostet es dich, nicht …“) und Online-Kurs; keine Preise auf der Seite |
| L6 | „… kaum Zeit …“ | neu schreiben für Seminar (vier Tage, Donnerstag bis Sonntag, Q6) | „kurze Lektionen“ beschreibt den Online-Kurs |
| L7 | „… viele Bücher … gelesen. Reicht das nicht?“ | mit L1 zusammen | Duplikat |
| L8 | „… bereits Kommunikations-Trainings gemacht …“ | behalten, ohne „25 Jahre“ | K1 Startseite: 25 vs. 30 Jahre; Beleg Zitat Emrullah A. |
| L9 | „Woher weiß ich, ob ich überhaupt ‚intelligent‘ bin?“ | streichen | „Intelligente“ ist kein Hauptbegriff mehr (K9, Sales-Feedback) |
| L10 | „… Selbstlernkurs oder … persönliche Betreuung?“ | streichen, ersetzt durch „Seminar oder Online-Kurs?“ | Online-Kurs ist nicht Ziel der Website |
| L11 | „Wie lange habe ich Zugang zum Online-Kurs …?“ | streichen | Online-Kurs (12 Monate); Antwort gehört auf die Kursseite |
| L12 | „Muss ich mich verstellen oder schauspielern?“ | behalten | Kundenwendung „Nicht anders werden, klarer werden.“ |
| L13 | „Du hast tatsächlich bis hierhin gelesen?“ | streichen | keine Frage, keine Information |

## v2-FAQ (Q2): Entscheidung je Frage
| # | v2-Frage | Entscheidung |
|---|---|---|
| V1 | Wie läuft ein Seminar ab? | behalten (Gruppe Ablauf) |
| V2 | Ist die Übernachtung enthalten? | behalten, gelbe Marke wie Seminarseite (S6) |
| V3 | Sind An- und Abreise enthalten? | behalten |
| V4 | Welche Verpflegung ist enthalten? | behalten, gelbe Marke (S6) |
| V5 | Kann ich eine Begleitperson mitbringen? | behalten, gelbe Marke (Startseite F10: Sales-Checkliste nicht freigegeben) |
| V6 | Was passiert, wenn ich absagen muss? (Gutschein) | AGB-Wortlaut 8 Wochen / 30 %, wie Startseite F4 und Seminarseite S7 |
| V7 | Muss ich mich verstellen …? | behalten (= L12) |
| V8 | Kommunikations-Trainings gemacht …? | behalten (= L8) |
| V9 | Ich stehe nie auf großen Bühnen … | behalten, Antwort neu aus der Rhetorik-Seite (Beruf) statt „exakt dieselben Gesetze“ |
| V10 | Community Talk to Me? | streichen: Skool-Community ist nicht Ziel der Website, Inhalt nur aus internem Briefing (Flag) |

## Konflikte und Regeln (übernommen aus den Geschwister-Läufen, gleiche Behandlung)
| # | Fund | Behandlung |
|---|---|---|
| K1 | AGB: Storno bis 8 Wochen gegen 30 %, danach voller Preis. Sales-Checkliste: keine Erstattung, Gutschein | AGB-Wortlaut, Widerspruch an Kunde (Startseite F4, Seminare S7) |
| K2 | Übernachtung und Verpflegung nur aus Sales-Checkliste | gelbe Marken `[von Kunde bestätigen: Übernachtung]`, `[von Kunde bestätigen: Verpflegung]` (Seminare S6) |
| K3 | Leitet Michael jedes Seminar selbst? | gelbe Marke `[von Kunde bestätigen: Leitet Michael die Seminare selbst]` (Michael M5) |
| K4 | Person im Gespräch | „Michaels Team“ + `[von Kunde bestätigen: Name und Rolle der Person im Gespräch]` |
| K5 | Rhetorik Bundle ohne Termine, Ort, Plätze | `[von Kunde bestätigen: Termine und Ort Bundle]` (Seminare S2) |
| K6 | Seminarnamen offen | Themen-Titel + Arbeitstitel, `[von Kunde bestätigen: Seminarname]` nur einmal |
| K7 | Begleitperson aus Sales-Checkliste | gelbe Marke `[von Kunde bestätigen: Begleitperson]` |
| K8 | Programm des Tages „Get Together“ ist nirgends beschrieben | gelbe Marke `[von Kunde bestätigen: Programm Get Together]` |
| K9 | Mexico „Rhetorik 4“ ohne Inhalte, mit Preis | nicht auf der Seite (Seminare S3) |
| K10 | Google 4,8 / Tajan-Bewertung | nicht verwenden; nur ProvenExpert 250 / 227 |
| K11 | Fragen ohne Kundenantwort (Vertraulichkeit Videoaufnahmen, Bildungsurlaub, Rechnung an Firma, Sprache Englisch, Zertifikat) | nicht auf der Seite, Liste in OPEN-FLAGS für den Kunden |
| K12 | Inhouse und Krisenkommunikation laufen über institut-ehlers.de | erwähnen ohne Link (Michael M6) |

## Technischer Zustand v2
Kein H1-Keyword, keine Einleitung, keine Gruppen, keine Sprungnavigation, kein CTA im Inhalt, keine Links zu Fachseiten, kein Schema, `noindex` (Vorschau). Seite nach dem Akkordeon leer (Höhe durch `min-height` der Sektion).
