# Dataset — me&you Communication / Michael Ehlers (Stand 2026-10-11)

Quellen: Live-Seite meandyou.de (Firecrawl 2026-10-11, maxAge 0; HTML per curl), Google Maps (Claude in Chrome), ProvenExpert (Firecrawl), DataForSEO (Ort 2276, de; Kosten 0,11 USD), Google-Autocomplete, Copy Deck Round 3 (Pauspapier, 29.09.2026, freigegebene Texte), PDF „2026 Michael Ehlers Kursinhalte R1-R3 4 Tage“, Sales-Checkliste (über build_v2.py-FAQ, Entwurf), Projekt-Memory, Entwurf A (prototype-v2).

## 0. Kontext und Ziel dieses Laufs
- Seite: Startseite. Basis ist **Entwurf A** (`prototype-v2/index.html`, live als Vorschau unter https://clients.741.studio/meandyou/v2/index.html). Phil (Pauspapier) bevorzugt Entwurf A. Auftrag Martin 2026-10-11: gleiche Struktur, bessere Umsetzung.
- Kontaktkanal: Buchung eines kostenlosen Gesprächs (Calendly-Event „Sichtbarkeit Neu“, 30 Minuten, online) über die neue Terminseite (`prototype-v2/termin.html`). Telefon sekundär.
- Kein Health-, kein Rechtskunde. Ergebnisaussagen nur mit echten Daten.
- Traffic: bezahlte Meta-Ads (8 aktive Ads führen auf /sichtbarkeit-neu, nicht auf die Startseite) und Marken-Suche („michael ehlers“). Die Startseite bekommt vor allem warmen Marken-Traffic und Rückkehrer aus den Ads.

## 1. Aktuelle Live-Startseite (Section-Map)
URL https://www.meandyou.de/ · CMS Framer · Sprache de · „Made by Pauspapier“.

| Nr | Abschnitt | Inhalt (Originalwortlaut, gekürzt) |
|---|---|---|
| 1 | Hero | Badge „Seminartermine - 2026“; H-Zeile „Seminare für Intelligente“; „Endlich verstanden werden, ohne dich zu verstellen“; doppelte Zeile „Lerne in diesem Kurs so zu kommunizieren, dass du überzeugst“ / „Lerne in diesen Seminaren so zu kommunizieren, dass du überzeugst und die Anerkennung bekommst, die du verdienst“; Button „Jetzt Gespräch buchen“ → /seminare-termin; ProvenExpert-Logo + „Bereits über 8.000+ Teilnehmer: innen überzeugt“; Freisteller Michael; 3 Ort-Kärtchen (Dubai „Wachstum trifft Wüste.“, Mallorca „Insel. Klarheit. Umsetzung.“, Barcelona/Nordzypern „Verändere deine Sprache. Verändere deine Wirkung.“) |
| 2 | Trust-Leiste | „Top 100 Trainer im DACH-Raum“ · „Über 1000 Vorträge & Medienauftritte“ · „Gründer des Ehlers-Rhetorik-Frameworks“ · „+30 Jahre Erfahrung als Rhetorik-Trainer“ |
| 3 | Story | „Du bist der Klügste im Raum, aber niemand hört dir zu?“ … Meeting-Szene, Kollege bekommt das Lob |
| 4 | Warum | „Tatsächlich haben es Intelligente Menschen oft schwerer …“ „Gehirn im Durchschnitt 5x mehr und schneller Lösungen“ (ohne Beleg), 4 Bildkarten |
| 5 | Termine | „Wo Wirkung beginnt: Deine Rhetorik-Termine 2026“ und „2027“ mit allen Daten (siehe 2.2), ein Preis sichtbar: „Mexico Rhetorik 4 Investition: 9.999 €“ |
| 6 | Versprechen | „… dass dich ‚Rhetorik für Intelligente‘ in 30 Tagen zu dem Menschen macht, der …“ (6 Punkte) |
| 7 | Woher ich das weiß | 30 Jahre, über 8.000 Menschen, „Darunter bekannte Schauspieler, Moderatoren, Politiker, Fußballtrainer der Nationalmannschaft, Profi-Sportler, Führungskräfte, Unternehmer und – Speaker“, „Jeder kann andere rhetorisch begeistern … Völlig gleich, wie introvertiert du bist.“ |
| 8 | Ausgezeichnet | „Michael Ehlers gehört laut ERFOLG Magazin zu den Top 100 Trainern im deutschsprachigen Raum & ist Top10 Speaker.“ „Vertrauen ist kein Zufall. Sondern das Ergebnis von 25 Jahren Bühnen, Medien, Boardrooms …“ |
| 9 | Veränderungen | 9 Sätze („Du kannst überzeugende Reden improvisieren …“) |
| 10 | Warum Trainings scheitern | „Auf den meisten Seminaren lernst du: Gestik und Mimik – und sollst schauspielern …“ „In ‚Rhetorik für Intelligente‘ bringe ich dir NICHT bei zu schauspielern.“ |
| 11 | Zitate | Sarna Röser, Peter Escher, Emrullah Ates, Neven Subotic (als Endlos-Laufband) |
| 12 | Video-Stimmen | 3 Wistia-Videos (1:00, 1:12, 1:23) |
| 13 | Für wen | „Diese Seminare sind genau richtig für dich, wenn du:“ 4 Punkte, „Jetzt direkt bewerben“ |
| 14 | Abschluss | „Starte heute noch mit unsere Seminare …“ Button |
| 15 | FAQ | 13 Fragen, überwiegend zum Online-Kurs (Zugang 12 Monate, Video-Lektionen) |
| 16 | Kontakt | „Fragen vorab? Schreiben Sie uns.“ Formular (Sie-Form) |

### 1.1 Technischer Zustand
- Title: „Rhetorik-Seminar mit Michael Ehlers – Klar sprechen, souverän führen“ (68 Zeichen, zu lang).
- Meta: „Intensive Rhetorik-Seminare 2026 in Dubai, Mallorca und Barcelona/Nordzypern. Stärke deine Wirkung, Präsenz und Kommunikation in exklusiven Intensivseminaren mit Praxis, Feedback und klarer Umsetzung“ (über 155 Zeichen).
- **Kein H1** auf der Seite (H1 = 0, H2 = 4, alle im Kontaktformular). Kein JSON-LD-Schema. Canonical https://www.meandyou.de/.
- Erster Bildschirm 1440 × 701: Button „Jetzt Gespräch buchen“ sichtbar (unterer Rand etwa bei 658 px). Kein Sterne-Wert, nur ProvenExpert-Logo ohne Zahl. Screenshots: `live-first-viewport-1440.png`, `live-full-1440.png` (Seitenhöhe 9.254 px).
- Copy-Fehler im Hero: zwei fast gleiche Sätze direkt untereinander.

### 1.2 Entwurf A (Basis dieses Laufs)
Reihenfolge: Hero („Werde unübersehbar, wenn es darauf ankommt.“, Foto Magazin) → Drei Situationen (3 Karten, freigegebene Persona-Headlines) → Warum Michael (Zahlenreihe, Medienlogos, Video-Platzhalter) → Die Methode (3 Schritte) → Seminare-Band (Foto, „Drei Tage. Kleine Gruppe.“) → Stimmen („Vorher. Nachher.“, Zitate als Laufband, 3 Videos) → Abschluss („Unübersehbar wird man nicht, indem man lauter wird.“). Seitenhöhe 6.492 px. Screenshot `entwurfA-full-1440.png`.
Schwächen (Messung): keine Bewertungszahl im ersten Bildschirm; Zitate als Laufband (Karussell); kein Ablauf des Gesprächs; keine FAQ; keine Termine/Orte; Video-Platzhalter `[Platzhalter: Videountertitel, eine Zeile]`; kleine Schrift `--small` 12,5 bis 14,5 px; CTA nur in Hero, Seminare-Band, Abschluss; Button-Ziel /seminare-termin (alte Seite).

## 2. Fakten (mit Quelle)

### 2.1 Michael Ehlers
| Fakt | Wortlaut / Wert | Quelle |
|---|---|---|
| Erfahrung | „seit über 30 Jahren Rhetorik-Trainer“, „+30 Jahre Erfahrung“, „3 Dekaden“ | Live-Seite |
| Teilnehmer | „über 8.000 Menschen ausbilden“ | Live-Seite |
| Auszeichnung | „laut ERFOLG Magazin zu den Top 100 Trainern im deutschsprachigen Raum & ist Top10 Speaker“; Cover Heft 3/2017 „TOP 100 Erfolgstrainer Deutschland/Österreich“ | Live-Seite, Grafik |
| Vorträge | „Über 1000 Vorträge & Medienauftritte“ | Live-Seite |
| Methode | „Gründer des Ehlers-Rhetorik-Frameworks“; Copy Deck: „Persönlichkeit. Kongruenz. Wirkung.“ | Live-Seite, Copy Deck |
| Kunden | „bekannte Schauspieler, Moderatoren, Politiker, Fußballtrainer der Nationalmannschaft, Profi-Sportler, Führungskräfte, Unternehmer und – Speaker“ | Live-Seite |
| Bücher | Copy Deck „5 Bücher“; Anzahl offen | Copy Deck `[FEHLT: Anzahl Bücher bestätigen]` |
| Medien | Logos ZDF, ARD, RTL, stern, MDR, hr2 | Live-Seite (Prototyp-Assets) |
| Sitz | Institut Michael Ehlers GmbH, Landsknechtstraße 50, 96103 Hallstadt | GBP, ProvenExpert |

### 2.2 Seminare (Präsenz)
| Fakt | Wert | Quelle |
|---|---|---|
| Format | 3 Tage Intensivtraining + 1 Tag Get Together (4 Seminartage, 3 Nächte) | Kursinhalte R1-R3 PDF; Sales-Checkliste |
| Bausteine | 3 Videoanalysen mit Sofort-Feedback, VR-Training, Worksheets/Workbooks | Kursinhalte PDF |
| Plätze | Rhetorik I 14, Rhetorik II 10, Rhetorik III 12 (also 10 bis 14) | Kursinhalte PDF |
| Themen R I | Sicher auftreten, Rede halten (in 2 Minuten ein starkes Statement), Struktur, Echt wirken, Sprache nutzen, Körper lesen, Fragen stellen | Kursinhalte PDF |
| Themen R II | Schlagfertigkeit, Überzeugungspsychologie, Angriffe abwehren, Körpersprache lesen, Meetings führen | Kursinhalte PDF |
| Themen R III | DeepOcean (Persönlichkeit), Führen lernen, Zuhören, Stegreifrede, Gruppen überzeugen | Kursinhalte PDF |
| Preis | steht im PDF, **nie auf der Seite** (Martin) | Regel |
| Übernachtung | im Seminarzeitraum enthalten; An-/Abreise nicht | Sales-Checkliste (Entwurf, Freigabe Kunde offen) |
| Seminarnamen | noch beim Kunden; Copy Deck: Platzhalter | `[FEHLT: Seminarnamen]` |

**Termine (Live-Seite, Stand 2026-10-11, nur künftige):** 2026: Mallorca 03.–06.12., Dubai 10.–13.12. 2027: Mexico 21.–24.01. (Rhetorik 4), Mallorca 04.–07.03., Barcelona 15.–18.04., Mallorca 29.04.–02.05., Frankfurt 17.–20.06., Berlin 12.–15.08., Zypern 07.–10.10., Mallorca 14.–17.10., Barcelona 21.–24.10.
Hinweis: Live-Seite schreibt „(3-Tages-Seminar)“ bei 4 Kalendertagen; das passt zu „3 Tage + 1 Tag Get Together“.

### 2.3 Das Gespräch (Konversionsziel)
| Fakt | Wert | Quelle |
|---|---|---|
| Format | 30 Minuten, kostenlos, online | Calendly „Sichtbarkeit Neu“ (30 min), Copy Deck Abschluss |
| Inhalt | „Wir klären, wo du stehst und welches Format passt.“ | Copy Deck |
| Buchung | Calendly inline auf der Terminseite; Formular Name, E-Mail, Telefon; Erinnerungen per WhatsApp vom Setter | Funnel-Check 06.10., No-Show-Plan 08.10. |
| Wer spricht | ein Mitglied aus Michaels Team (Setter), nicht Michael selbst | Funnel-Check; `[FEHLT: Name/Rolle des Gesprächspartners]` |
| Wartezeit bis Termin | Kalender heute einen Monat offen; geplant: 48 bis 72 Stunden | No-Show-Plan (nicht umgesetzt) |

### 2.4 Online-Angebote (nicht Ziel dieser Seite)
Online-Kurs „Rhetorik für Intelligente“ („in 30 Tagen“, Zugang mindestens 12 Monate), Community „Talk to Me“ (Skool), kostenloses Training (VSL /sichtbarkeit-neu). Die Live-FAQ mischt Kurs und Seminar. Die neue Startseite verkauft das Seminar über das Gespräch.

## 3. Google-Unternehmensprofil
„Institut Michael Ehlers GmbH“, Kategorie „Adult education school“, **4,8 Sterne, 23 Bewertungen**, Landsknechtstraße 50, 96103 Hallstadt, +49 160 96600322, meandyou.de. Details und Wortlaut: `reviews.md` Teil A.

## 4. Bewertungen
- Google 4,8 / 23 (eine 1-Stern-Bewertung, eine von Tajan Fattah, Pauspapier: nicht verwenden).
- **ProvenExpert: 250 veröffentlichte Bewertungen**, 227 × 5 Sterne, 21 × 4, 2 × 3. Rechnerischer Schnitt 4,90. Anzeige-Gesamtnote wörtlich `[FEHLT]`.
- Zitate mit Logo auf der Live-Seite: Sarna Röser, Peter Escher, Emrullah Ates, Neven Subotic.
- 3 echte Video-Stimmen (Wistia).
- Phrasen der Teilnehmer: siehe `reviews.md` Teil D.

## 5. Suchnachfrage (DataForSEO, Deutschland, de)
| Keyword | Volumen/Monat | CPC € |
|---|---|---|
| rhetorik kurs | 1.600 | 4,85 |
| rhetorik seminar | 880 | 7,29 |
| michael ehlers | 480 | 3,14 |
| rhetorik training | 390 | 6,92 |
| rhetorik coaching | 390 | 9,69 |
| präsentationstraining | 260 | 11,26 |
| rhetorik lernen | 210 | 3,12 |
| rhetorikseminar | 170 | 10,39 |
| rhetoriktraining | 170 | 7,98 |
| rhetoriktrainer | 170 | 7,03 |
| rhetorik für führungskräfte | 110 | 9,88 |
| rhetorik seminar frankfurt | 90 | 6,25 |
| michael ehlers rhetorik | 90 | 3,77 |
| rhetorik seminar führungskräfte | 40 | 9,31 |
| schlagfertigkeit seminar | 40 | 5,38 |
| rhetorik seminar berlin | 30 | 7,48 |
| rhetorik seminar mallorca / barcelona | keine Daten | (Autocomplete ohne Treffer) |

People Also Ask („rhetorik seminar“, SERP DE): „Was macht man in einem Rhetorik-Seminar?“, „Was kostet ein Rhetorik-Seminar?“, „Wie lerne ich am besten Rhetorik?“, „Welche Übungen kann ich machen, um Rhetorik zu trainieren?“, „Was sind die 5 Säulen der Rhetorik?“. Verwandte Suchen: „Rhetorik Seminar Wochenende“, „Rhetorik Seminar Führungskräfte“, „Rhetorik Seminar für Anfänger“, „Rhetorik Seminar Bildungsurlaub“, „Rhetorik Seminar online“.
Autocomplete „michael ehlers“: „michael ehlers institut“, „michael ehlers rhetorik“, „wer ist michael ehlers“, „michael ehlers kritik“.
Rohdaten: `demand/`.

## 6. Aktuelle Rankings
meandyou.de rankt für 4 Keywords: „michael ehlers“ Platz 1 (Startseite), „michael ehlers rhetorik“ Platz 1, „michael ehlers-rhetorik“ Platz 3, „rhetorik training“ Platz 19 (/videokurs/start). Keine Rankings für „rhetorik seminar“. Top-10 dort: Akademien und Portale (Haufe, IHK, Kitzmann, Semigator), keine Intensivseminare im Ausland. Lücke: Positionierung „Intensivseminar, kleine Gruppe, besonderer Ort“ besetzt dort niemand.

## 7. Konflikte und Compliance (UWG, Belegpflicht)
| # | Fund | Quelle | Behandlung im Prototyp |
|---|---|---|---|
| K1 | „30 Jahre“ und „25 Jahre“ auf derselben Seite | Live-Seite | nur „über 30 Jahre“ (häufigster Wert, Copy Deck). `[FEHLT: Bestätigung 30 Jahre]` |
| K2 | „in 30 Tagen zu dem Menschen macht, der …“ | Live-Seite (Kurs) | nicht übernommen (Ergebnisversprechen, Online-Kurs) |
| K3 | „Gehirn … 5x mehr und schneller Lösungen“ | Live-Seite | nicht übernommen (kein Beleg) |
| K4 | „dass du garantiert vorankommst“ (FAQ 3) | Live-Seite | nicht übernommen (Garantie ohne Grundlage) |
| K5 | „Top 100 Trainer“: Cover von 2017 | Grafik | Formulierung „laut ERFOLG Magazin“ wie Live-Seite, ohne Jahreszahl-Behauptung „aktuell“ |
| K6 | „Fußballtrainer der Nationalmannschaft“ ohne Namen | Live-Seite | nicht übernommen (Namensnennung nicht freigegeben); Kundengruppen ja |
| K7 | Preis „9.999 €“ für Mexico sichtbar | Live-Seite | keine Preise (Regel Martin) |
| K8 | Google-Bewertung von Tajan Fattah (Partner-Agentur) | GBP | nie auf der Seite zeigen |
| K9 | „Seminare für Intelligente“ als Hauptheadline | Live-Seite | Copy Deck/Sales-Feedback: nicht mehr Hauptheadline |
| K10 | Live-FAQ beschreibt Online-Kurs, Seite verkauft Seminar | Live-Seite | FAQ neu nur zu Seminar und Gespräch |
| K11 | „Teilnehmer: innen“ mit Leerzeichen, „unsere Seminare“ Grammatik | Live-Seite | nicht übernommen |

## 8. Bestehende 741-Daten
- Copy Deck Round 3 (freigegebene Texte, `copydeck-r3.txt`): Hero, Situationen (Persona-Headlines vom Kunden freigegeben, nicht ändern), Warum Michael, Methode, Seminare-Teaser, Stimmen, Abschluss.
- Copy Version C (an Tajan, 08.10.): Doc „me&you – Website-Copy (08.10.2026)“ (Direct-Response-Varianten, Pain-Sektion, 8 Alleinstellungsmerkmale, 5 CTA-Texte). Pauspapier jagt sie durch ihre Copy-KI; Rückläufer offen.
- No-Show-Plan (08.10.): Buchungsfenster kürzen, 3 Pflichtfragen, Bestätigungsseite, WhatsApp-Sequenz.
- Terminseite-Prototyp `termin.html` (08.10.): Ziel aller Buttons in diesem Lauf.
- VSL-Seite: 8.138 Aufrufe, 140 Buchungen, 1,72 % (Zahlen unbestätigt, nur intern).
- Phil-Feedback 06.10.: Entwurf A bevorzugt (klarer, weniger Animation); Parallaxe einheitlich (Martin 08.10.: „Parallax ist gut“, Faktor überall gleich).

## 9. Brand, Fotos, Logo
→ `brand.md`, `01-input/INVENTORY.md`.

## 10. Offene Punkte [FEHLT]
1. `[FEHLT: Seminarnamen]` (Arbeitstitel Rhetorik I, II, III).
2. `[FEHLT: Anzahl Bücher]` (Copy Deck 5, früher 9 genannt).
3. `[FEHLT: Bestätigung 30 Jahre]` (Live-Seite auch 25).
4. `[FEHLT: Name und Rolle der Person im Gespräch]`.
5. `[FEHLT: echte Seminarfotos]` (Gruppe, Raum, Übung).
6. `[FEHLT: Video „Warum Michael“]` (Copy Deck: noch nicht geliefert).
7. `[FEHLT: ProvenExpert-Gesamtnote wörtlich]` (rechnerisch 4,90).
8. `[FEHLT: Freigabe Sales-Checkliste-Antworten]` (Übernachtung, Verpflegung, Absage).
