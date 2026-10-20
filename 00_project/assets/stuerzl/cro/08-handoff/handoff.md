# Handoff — Startseite STÜRZL Steuerstrafrecht (Prototyp v1, Desktop)

Stand 2026-10-11. Für den späteren Rebuild-Workflow ("we will implement later", Martin). Nichts ist live. Der Prototyp läuft nur lokal.

## 1. Pfade
- Prototyp: `00_project/assets/stuerzl/cro/07-prototype/index.html` (mit `assets/`), lokal öffnen oder `python3 -m http.server`. Generator: `_build/build.py` und `_build/template.html`.
- Bewegung: `07-prototype/motion.md`
- Prüfdateien: `07-prototype/visual-check.md` (55 Punkte, 8 fixed, 0 open), `07-prototype/self-check.md` (37 von 44)
- Mockup: `06-gpt-assets/full-page-v1-final.png`, Bilder-Slots: `06-gpt-assets/images/SLOTS.md`
- Design-Doc und Prompt: `05-gpt-design-doc/design-doc.md`, `prompt.txt`
- Text: `04-copy/approved-copy.md` (FAQ-Antworten sind Platzhalter)
- Diagnose: `03-diagnosis/diagnosis.md`. Daten: `02-data/dataset.md`, `02-data/brand.md`
- Screenshots: `07-prototype/screenshots/`. Live-Seite vorher: `02-data/screenshots/`
- Vorarbeit: Content-Pool `00_project/assets/stuerzl/content-pool/`, Audit `00_project/assets/audit/stuerzl/2026-10-11-kickoff/`

## 2. Text und Meta
- Title (52 Zeichen): Anwalt Steuerstrafrecht Frankfurt & München | STÜRZL
- Meta Description (145): STÜRZL Steuerstrafrecht: Verteidigung im Steuerstrafverfahren, Selbstanzeige, Durchsuchung. Büros in Frankfurt und München. Vertraulich anfragen.
- H1: Steuerstrafrecht und Wirtschaftsstrafrecht in Frankfurt und München. (Varianten B und C in `approved-copy.md`)
- Schema: zwei `LegalService`-Einträge (Frankfurt, München) mit getrennten Zeiten (JSON-LD im Prototyp). Noch offen: `Person` (Dr. Stürzl), `FAQPage` (nach Antworten der Kanzlei), `sameAs`.
- Der Prototyp trägt `noindex,nofollow`. Vor dem Livegang entfernen.
- Die Adresse im JSON-LD (Untermainkai 26) erst setzen, wenn die Frankfurter Adresse bestätigt ist.

## 3. Marke
Echtes Logo (`01-input/site-originals/stuerzl_logo_rgb.svg`, Anthrazit #323335 und Salbei #8DA38E). Im Prototyp ist nur die `viewBox` auf die Logoform beschnitten (`assets/logo.svg`) und eine weiße Fußvariante gebaut (`logo-white.svg`, gleiche Form). Das Original bleibt unverändert. Farben: Anthrazit #323335, Weiß, Creme #F4F1EC, Linie #E2DDD4, ein CTA-Grün #4E6F55 (Salbei abgedunkelt für Kontrast 5,6 zu 1), Grau #6A6C70. Schrift Newsreader 500 und Manrope.

## 4. Bilder und Shoot-Liste
Alle drei Bilder im Prototyp sind echte Dateien der Live-Seite (Hero `start6e.jpg`, Porträt `potrait_start3b3.jpg`, Büro `fusszeile5.jpg`). Es gibt kein KI-Bild. Fehlt für die Umsetzung:
1. Echte Fotos der Büros Frankfurt (Untermainkai 26, Eingang) und München (Oberanger 32). Das vorhandene Innenraum-Foto: Welches Büro zeigt es? [FEHLT]
2. Freigabe für das Empathy-Gruppenbild und das Siegel Young TLE, falls sie auf die Seite sollen. Dritte sind erkennbar.
3. Eine echte Karte pro Standort, nach Einwilligung (Cookie-Banner), statt der Platzhalterkachel.

## 5. Tracking-Spezifikation (Einrichtung ist nicht Teil dieses Workflows)
Events mit Parameter `section` (hero, notfall, mandanten, ablauf, ueber, bewertungen, faq, standorte, abschluss, footer):
- `form_submit`: Absenden des Anfrage-Formulars (Parameter `standort`). Keine Falldaten, nur das Ereignis.
- `phone_click`: jeder `tel:`-Link, Parameter `standort` (frankfurt, muenchen).
- `emergency_phone_click`: die beiden Notfallnummern im Notfall-Streifen (nur dort). FAQ F3 nennt keine Nummer; entfällt der Streifen, entfällt auch F3 oder verweist auf die Kontaktnummern.
- `email_click`: jeder `mailto:`-Link.
Kein WhatsApp-Event (Kanal nicht erlaubt, § 203 StGB, DSGVO).

## 6. [FEHLT]-Liste (was Martin bei der Kanzlei klären muss)
1. Endgültige Frankfurter Adresse (Untermainkai 26?), Eingang, Anfahrt zum Hauptbahnhof, Parken. Kontaktseite und Google-Profil Frankfurt zeigen noch die alte Adresse Wiesenhüttenstraße 17.
2. Notfallnummern 0160 3396513 und 0160 95945730: Freigabe und Zeiten der Besetzung. Ohne Freigabe entfällt der Streifen.
3. Einwilligungstext für das Formular (DSGVO, § 203 StGB), wer Anfragen bearbeitet, Reaktionszeit. Ablauf der vier Schritte und Vertraulichkeitszusage bestätigen; "Auf Wunsch zuerst per E-Mail" bestätigen.
4. Preis oder Preisrahmen und Dauer der Erstberatung; Kostenseite ("Honorar im Detail").
5. Freigabe: anwalt.de 5,0 mit 79 Bewertungen; Datum der Google-Bewertungen; Link zum Google-Profil; Wortlaut der drei Bewertungsauszüge (Selina M., Milad, J. S.) gegen Google prüfen.
6. FAQ-Antworten (die Kanzlei liefert sie später). Besonders F3 (Durchsuchung) und F4 (Selbstanzeige): juristischer Inhalt, die Kanzlei prüft.
7. München: Ansprechpartnerin, Parken. Bundesweit: Videogespräch oder Termine vor Ort?
8. Zuständige Kammer und Berufshaftpflicht (für den Vertrauensblock).
9. Compliance-Text von Dr. Glogger (siebte Leistung), Seiten für die sechs Leistungskarten.
10. Welches Büro zeigt das Innenraum-Foto? Büro-Fotos.
11. Titel "Dr." (Universität, Jahr) bestätigen. Der Lebenslauf von Dr. Stürzl nennt keine Promotion; "Dr." steht auf der Live-Seite und im Pool.
12. Impressum, Datenschutz und Cookie-Einstellungen sind im Prototyp `#`-Platzhalter und werden im Rebuild die echten Seiten.

## 7. Hinweise für den Rebuild
- Live-Seite: Joomla, H1 "Kanzlei", Title "Stürzl Steuerstrafrecht – Home", Link `/index.php/schwerpunkte` ist 404, keine `sitemap.xml`, sechs FAQ-Seiten mit je H1, Chat-Button "Online-Anfrage" ohne Ziel, kein Formular. Rankings: nur Marke und Namen auf Platz 1, "anwalt steuerstrafrecht" ca. #27.
- Page-Swap: neue Seite bauen, alte offline, Slug übernehmen (Regel aus dem Memory). Kontaktwege (Nummern, Zeiten) 1:1 prüfen: Die Kontaktseite nennt 9:30 bis 14:30, Google nennt 9 bis 18 Uhr (Martin: Google gilt).
- Zeitleiste folgt dem Lebenslauf von Dr. Stürzl (Rettenmaier "2022 bis 2023", Gründung 12/2023). Die Live-Seite sagt "Dezember 2022 bis zur Gründung". Bitte auf der Live-Seite angleichen.
- Zwei Standorte brauchen eigene Landingpages (Frankfurt, München) mit der Hero-Logik dieser Seite.
- Google-Profile aktualisieren (Adresse Frankfurt, Kategorien, Leistungen). Das gehört zum Maps-Playbook, nicht zu diesem Workflow.
- Kein "Fachanwalt für Strafrecht", kein "spezialisiert", keine Peer-Zitate mit Superlativen (siehe `dataset.md` Abschnitt 7).

## 8. Vorher und Nachher
Live-Seite 10 von 44 → Prototyp 37 von 44. Prio A unter 2: Item 2 (Berufsrecht), 6 und 9 (fehlende Kundendaten).

## 9. Learnings (auch in `rules.md`)
- `pbcopy` ohne `LC_ALL=en_US.UTF-8` zerstört Umlaute im GPT-Prompt (ST√úRZL). Immer mit UTF-8-Locale kopieren und vor dem Senden prüfen.
- `measure.js` M6 fand zwei falsche `tel:`-Nummern (je eine Ziffer zu wenig) bei der Handarbeit. Nummern immer aus der Quelle ziehen und im Check abgleichen.
- Ein SVG-Logo hat oft Rand in der `viewBox`. Beschneiden, sonst wirkt das Logo klein.
- Chrome-`resize_window` ändert den Viewport nicht, wenn das Fenster größer ist. Die echte Breite in `visual-check.md` angeben.
- FAQ in `details` mit CSS-Spalten liest sich in falscher Reihenfolge. Eine Spalte nutzen.

## Nachtrag 2026-10-11: FAQ, Kosten, Mobil
- FAQ: acht recherchierte Antworten (Quellen und Rückfragen an die Kanzlei in `../cro-b/08-handoff/handoff.md`, Abschnitt 13). Kosten-Fakten nach dem Kostentext der Kanzlei: Erstberatung üblicherweise Pauschale 250 bis 350 Euro, Abrechnung nach Zeitaufwand, nicht nach RVG.
- Notfallnummern von Martin freigegeben, anwalt.de-Zahlen und Titel "Dr." bestätigt, Adresse Untermainkai 26 gilt, Google-Profil-Links Frankfurt und München eingebaut.
- Mobil: Layout für 320 bis 1099 px, Messungen in `07-prototype/mobile-check.md`, Desktop ab 1100 px unverändert.
- Bilder: das Sessel-Porträt (`about.jpg`) ist als HD-Version (1536×1024) eingebaut, das Büro-Foto in 1920 px.
