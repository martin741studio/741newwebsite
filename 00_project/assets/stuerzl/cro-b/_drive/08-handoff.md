# Handoff — STÜRZL Startseite, Variante B (Track B, Briefbogen), Prototyp v1, Desktop (nach Prüfer-Lauf)

Stand 2026-10-11. Zweite Version zur Auswahl für Dr. Stürzl (Variante A: `../cro/`). Nichts ist live. Der Prototyp läuft nur lokal und trägt `noindex,nofollow`.

## 1. Pfade
- Prototyp: `00_project/assets/stuerzl/cro-b/07-prototype/index.html` (mit `assets/`). Generator `_build/build.py` und `_build/template.html`.
- Bewegung `07-prototype/motion.md`, Gewicht `perf.md`, Prüfdateien `visual-check.md` (58 Punkte, 26 fixed gesamt, davon 15 nach Prüfer, 0 open), `self-check.md` (38 von 44).
- Konzept `05-gpt-design-doc/concept/concept.md`, Design-Doc und Prompt `05-gpt-design-doc/`, Mockup `06-gpt-assets/full-page-v1-final.png`, Slots `06-gpt-assets/images/SLOTS.md`, Media `06-gpt-assets/media/MEDIA-PLAN.md`.
- Text `04-copy/approved-copy.md`. Brief `00-brief-b/brief-b.md`. Element-Pools und Stimmen `00-element-pool/` (`votes-summary-pool1.md`, `votes-summary-pool2.md`). Recherche `02-data/research-*.md`, Katalog `02-data/elements-catalog.md`.
- Variante A zum Vergleich: `../cro/07-prototype/index.html`.

## 2. Unterschiede A und B (für das Gespräch mit Dr. Stürzl)
| | Variante A (ruhig) | Variante B (Briefbogen) |
| --- | --- | --- |
| Idee | klare, ruhige Kanzlei-Seite | die Seite liest sich wie ein Brief der Kanzlei |
| Schrift | Newsreader und Manrope | Fraunces und Instrument Sans |
| Kopf | Logo, sechs Menüpunkte, Button | Briefkopf mit beiden Büros, Wort Menü (Vollbild), Button, Rückruf-Reiter |
| Hero | Foto rechts mit Namensschild | Foto setzt sich, Beleg-Karte am Rand |
| Leistungen | sechs Karten | sechs Foto-Streifen, öffnen sich beim Überfahren |
| Über Dr. Stürzl | Foto, Absatz, Zeitleiste | Foto mit Platte, Absatz füllt sich beim Scrollen, großes Zitat |
| Standorte | zwei Karten mit Kartenkachel | gestaffelte Skylines, zwei Spalten mit eigener Rückruf-Schaltfläche |
| Abschluss | dunkles Band, Formular rechts | 50/50-Split mit Formular in drei Schritten, Gruß am Ende |
| Texte | geprüft | dieselben geprüften Texte, H1-Variante B |
| Score | 37 von 44 | 38 von 44 |

## 3. Text und Meta
- Title (52 Zeichen): Anwalt Steuerstrafrecht Frankfurt & München | STÜRZL
- Meta Description (145): STÜRZL Steuerstrafrecht: Verteidigung im Steuerstrafverfahren, Selbstanzeige, Durchsuchung. Büros in Frankfurt und München. Vertraulich anfragen.
- H1: Verteidigung im Steuerstrafverfahren. In Frankfurt und München. (Variante A: Steuerstrafrecht und Wirtschaftsstrafrecht in Frankfurt und München.)
- Schema: zwei `LegalService` (Frankfurt, München) im JSON-LD; Frankfurter Straße steht bewusst nicht im JSON-LD, bis die Adresse bestätigt ist (Ort und Land stehen drin). Offen: `Person`, `FAQPage`.

## 4. Komponentenliste (Track B)
| Komponente | Wo | Funktion |
| --- | --- | --- |
| Rückruf-Reiter | `#cb`, `#cbt` | fester Reiter am rechten Rand, Panel mit Standort und Zeitfenster (keine Falldaten) |
| Vollbild-Menü | `#mo`, `#menub` | öffnet ein Menü mit nummerierten Einträgen, Notfall-Zeile bleibt sichtbar |
| Foto-Streifen | `#strips` | sechs Streifen, einer offen, Hover, Fokus, Tippen |
| Lead-Absatz | `#leadp`, Funktion `lead` | Wörter füllen sich nach Scroll-Anteil |
| Weitere Muster | Funktionen `steps`, `tl` | Schrittlinie mit Zähler, Zeitleiste |
| Schalter | `?xray=1` oder Taste `x`; `?rm=1`; `?shot=1` | X-ray, Reduced Motion, Screenshots |

## 5. Marke
Echtes Logo (viewBox beschnitten, Fuß weiß, gleiche Form). Farben Anthrazit #323335, Weiß, Creme #F4F1EC, Linie #E2DDD4, ein CTA-Grün #4E6F55, Salbei hell #8DA38E nur für Linien und Flächen. Schrift Fraunces (Gewicht 350, optische Größe automatisch) und Instrument Sans. Siehe `02-data/brand.md`.

## 6. Bilder und Shoot-Liste
Alle Bilder echt (Live-Seite). Shoot-Liste: Büro Frankfurt (Untermainkai 26) und Büro München (Oberanger 32) als echte Fotos; welches Büro zeigt das vorhandene Innenraum-Foto? [FEHLT]; Hochformat-Porträts in höherer Auflösung für die Streifen; Freigabe für das Empathy-Gruppenbild bleibt offen (nicht verwendet).

## 7. Tracking-Spezifikation (Einrichtung gehört nicht zu diesem Workflow)
Events mit Parameter `section` (kopf, hero, mandanten, leistungen, ablauf, ueber, bewertungen, fragen, standorte, abschluss, menue, rueckruf-reiter): `form_submit` (Schritt-Parameter, keine Falldaten), `phone_click` (Parameter `standort`), `emergency_phone_click` (Notfall-Streifen, Menü), `email_click`, `callback_open` (Reiter), `callback_request`, `strip_open` (Parameter `row`). Kein WhatsApp-Event.

## 8. [FEHLT]-Liste (Martin klärt mit der Kanzlei)
1. ~~Frankfurter Adresse~~ erledigt: Untermainkai 26 (Martin, 2026-10-11). Eingang und Parken nicht auf der Seite.
2. Notfallnummern 0160 3396513 und 0160 95945730: Freigabe und Zeiten der Besetzung (ohne Freigabe entfallen Streifen, Menü-Zeile und FAQ F3-Verweis).
3. Rückruf-Zusage und Zeitfenster der Kanzlei (Reiter) und Reaktionszeit.
4. Einwilligungstext (DSGVO, § 203 StGB), Bearbeiter der Anfragen.
5. Preis oder Preisrahmen und Dauer der Erstberatung (Kostenseite kommt später).
6. ~~anwalt.de-Zahlen~~ freigegeben (Martin). Offen: Datum der Google-Bewertungen, Wortlaut Zitat 2 gegen Google.
7. FAQ-Antworten (kommen später).
8. München: Parken und Ansprechpartnerin sind für diese Version nicht nötig (Martin). Bundesweit: Videogespräch oder Termine vor Ort?
9. Titel "Dr.": von Martin bestätigt (2026-10-11), erledigt.
10. ~~Zuständige Kammer, Berufshaftpflicht~~ stehen im Impressum der Live-Seite (Rechtsanwaltskammer Frankfurt am Main, Berufshaftpflicht R+V Allgemeine Versicherung AG) und kommen beim Rebuild in das Impressum, nicht auf die Startseite.
11. Gruß "Mit freundlichen Grüßen, Dr. Anja Stürzl": Freigabe der Kundin für den Briefbogen-Ton (nur gesetzter Text, kein Faksimile).

## 9. Hinweise für den Rebuild
- Joomla. Die Komponenten brauchen eigenen Code (Template-Override oder Custom-HTML). Ohne den Code bleibt die Seite voll nutzbar (Test T5). Das Menü kann auf eine einfache Navigation zurückfallen.
- Schriften selbst hosten (DSGVO). Page-Swap: neue Seite bauen, alte offline, Slug übernehmen. Kontaktwege 1:1 prüfen (Live-Kontaktseite zeigt 9:30 bis 14:30, Google 9 bis 18 Uhr, Martin: Google gilt).
- Zwei Standort-Landingpages mit der Hero-Logik dieser Seite.
- Kein "spezialisiert", kein "Fachanwalt für Strafrecht", keine Peer-Zitate mit Superlativen.

## 10. Learnings
- Der Element-Pool als Abstimmungsseite hat die Konzeptwahl getragen. Der erste Pool wirkte zu nah am Dumann-Pool; erst die erweiterte Recherche (Award-Seiten, Typografie, Notfall-Muster) und ein zweiter Pool mit Mini-Seiten zum Scrollen brachten klare Stimmen.
- Fraunces bei optischer Größe 144 wirkt in Überschriften zu fein und eng. Optische Größe automatisch lassen und Gewicht 350 nutzen.
- Schmale Foto-Streifen brauchen senkrechte Titel und einen Index-Code oben, sonst überlappen sich Text und Code.
- Weiße Karten auf Creme sind nicht sichtbar, wenn die Karte selbst Creme ist.
- Chrome-Viewport war 1490 × 757, `resize_window` ändert ihn nicht.

## 11. Ergänzungen nach dem Prüfer-Lauf
- Drive-Ordner: siehe `_status.md` und Registry (Link wird beim Upload eingetragen).
- Bewegungs-Ausnahmen: Rückruf-Panel öffnet nur auf Klick, Notfall-Streifen, Telefonnummern, Formularfelder und Bewertungstexte bewegen sich nie. Alle weiteren Regeln in `07-prototype/motion.md`.
- Tracking: Der Prototyp enthält keine `data-`-Hooks. Die Spezifikation in Abschnitt 7 gilt für den Rebuild.
- Fotos: Es gibt nur sechs echte Dateien (Hero, Über, Kanzlei-Innenraum, Foto Treppe/Fenster, zwei Skylines). Die Streifen nutzen verschiedene Ausschnitte. Shoot-Wunsch: 6 neue Fotos (Mandantengespräch von hinten, Aktenarbeit, Empfang, Büro Frankfurt, Büro München, Detail Hände/Unterlagen), alle ohne erkennbare Mandanten.
- Offene Daten kommen nur von der Kanzlei: Freigabe der anwalt.de-Zahlen, Zitat 2 gegen Google-Wortlaut, Rückruf-Zusage.
- Unterschied zu Variante A: Reihenfolge und Texte sind gleich (Texte sind geprüft). B ist eine andere Gestaltung, kein anderes Konzept der Seitenfolge. Wenn Dr. Stürzl eine echte Alternative der Seitenfolge will, ist das ein eigener Schritt.
- Google-Profile (nach Martins Hinweis eingebaut): Frankfurt https://www.google.com/maps/place/?q=place_id:ChIJyVGAdikEaW8RUOWpEJs-2XA (Link "Alle Bewertungen bei Google lesen" und "Route planen"), München https://www.google.com/maps?cid=8324159804288938278 ("Route planen"). Die Frankfurter Karte im Profil zeigt noch die alte Adresse Wiesenhüttenstraße 17, bis die Kanzlei sie ändert.

## 12. Stand nach Martins Feedback (2026-10-11)
- Hero: Telefon-Pille "Anrufen" entfernt. Die Nummern stehen im Kopf-Streifen, im Abschluss und im Fuß.
- "Dr." und anwalt.de-Zahlen gelten als bestätigt, Hinweise entfernt. Hinweis zu Kostenseite, Kammer und Berufshaftpflicht entfernt (Kostenseite kommt später, Kammer steht im Impressum).
- Standorte: je Büro ein Kasten "Karte laden". Die Google-Karte lädt erst nach Klick und der Satz zur Datenübertragung steht im Kasten. Frankfurt und München zeigen die STÜRZL-Pins.
- Datenschutz beim Rebuild: Karten-Einbindung in die Datenschutzerklärung aufnehmen.

## 13. FAQ-Antworten (recherchiert 2026-10-11, für die Kanzlei zur Freigabe)
Acht Fragen in Sektion 9 (Kosten, Vertraulichkeit, Durchsuchung, Selbstanzeige, Unternehmen, bundesweit, Strafe, Verjährung). Quellen: Kostentext und Compliance-Text der Kanzlei, Gesetzestexte (BRAO § 43a, StPO § 136/137, AO § 169/370/371/376/235, StGB § 78/78a/78c), Wettbewerber-Seiten zum Gegenprüfen (steuerdelikt.de, wild.legal). Nachfrage nach Suchvolumen: "steuerhinterziehung strafe" 4.400, "steuerhinterziehung verjährung" 2.400, "selbstanzeige finanzamt" 720 (DataForSEO).
Punkte, die die Kanzlei bestätigen soll (Hinweis von der Recherche, nicht auf der Seite):
1. Erstberatungs-Pauschale 250 bis 350 Euro: netto oder brutto? Text der Kanzlei sagt es nicht, die Seite nennt nur die Zahl.
2. § 34 RVG begrenzt das Honorar für ein Erstberatungsgespräch gegenüber Verbrauchern ohne Gebührenvereinbarung auf 190 Euro. Die Pauschale sollte daher vor dem Gespräch vereinbart werden. Das ist Sache der Kanzlei.
3. F3: Ob eine Begleitung vor Ort angeboten wird und wann die Notfallnummern besetzt sind, ist nicht belegt. Der Text sagt "hängt vom Einzelfall ab".
4. F4: Formulierung "kann dazu führen, dass Sie wegen dieser Taten nicht bestraft werden" freigeben. Auslassungen mit Absicht: Grenze 25.000 Euro je Tat und § 398a AO, Zehnjahresregel.
5. F5: "Mitarbeiter, Leitungspersonen, Zeugenvernehmungen" stammt aus der Leistungsliste der Live-Seite, nicht aus einem Kanzlei-Dokument.
6. Ersatzfrage zur Wahl: "Muss ich auf eine Vorladung der Steuerfahndung reagieren?" (belegter Entwurf liegt vor, nicht eingebaut, ohne Suchvolumen).
7. Einwilligungstext im Formular ist ein Entwurf von 741. Datenschutzberatung der Kanzlei prüft ihn vor dem Livegang.

## 14. HD-Bilder und Mobil (2026-10-11)
- Bilder: Skylines Frankfurt und München, Porträt weiße Bluse und Sessel-Porträt sind per ChatGPT hochskaliert (1536×1024 bzw. 1122×1402), Gesicht, Pose, Kleidung, Licht und Bildausschnitt wie das Original. Das Büro-Foto läuft in 1920 px. Die Originale und die Roh-Dateien von ChatGPT liegen unter `06-gpt-assets/hd/`. Hinweis: Beim Bluse-Porträt fehlt in der HD-Version der unscharfe helle Fleck auf dem Rock, der im Original zu sehen war.
- Mobil: Layout für 320 bis 1099 px in `_build/template.html`, Messungen und Screenshots in `07-prototype/mobile-check.md` und `07-prototype/screenshots/mobile/`. Desktop ab 1100 px unverändert (Pixelvergleich 0 Unterschiede).
- Mobil, bewusste Entscheidungen: Hero-Reihenfolge Text, Foto, Beleg-Karte. Zähler "1 : 4" im Ablauf ist mobil ausgeblendet. Rückruf-Reiter ist mobil eine Pille unten rechts und verschwindet, wenn das Formular im Bild ist.
- Mobil, offen: Bei 320 × 640 px liegt der Hero-Button knapp unter dem sichtbaren Bereich. Auf 360 bis 430 px ist er sichtbar.
