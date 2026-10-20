# Visual Check — Startseite STÜRZL Variante B (Track B, Briefbogen), Prototyp v1

Datum 2026-10-11 · geprüft in Claude in Chrome (externes Chrome) · Server `python3 -m http.server 8823` · echter Viewport 1490 × 757 (das Chrome-Fenster ließ sich nicht schmaler stellen; headless zusätzlich bei 1440) · ohne `?shot=1` · Seitenhöhe 10.176 bis 10.241 px.

## Gemessene Prüfungen (M1 bis M11)
| # | Prüfung | Ergebnis | Wert |
| --- | --- | --- | --- |
| M1 | Breite | Hinweis | 1490 × 757 statt 1440 |
| M2 | kein horizontaler Scroll | ok | scrollWidth ≤ innerWidth |
| M3 | Konsole und Netz | ok | 0 Konsolenfehler; alle Requests 200 oder 304 |
| M4 | Bilder geladen, nicht hochskaliert | ok | hero 1800 für 835 px, about 1100 für 430 und 720, office 1400, kanzlei 614, Skylines 800 |
| M4b | keine Verzerrung | ok | alle als CSS-Hintergrund oder `object-fit` mit festem Ausschnitt |
| M5 | Schriften | ok | Fraunces und Instrument Sans geladen |
| M6 | Links | ok mit Liste | Anker alle vorhanden, alle landen 94 bis 95 px unter dem Kopf; `tel:+4969298028870`, `tel:+498972444170`, `tel:+491603396513`, `tel:+4916095945730` je gegen den sichtbaren Text geprüft; 12 Links mit `#` (siehe Offen) |
| M7 | Reveals | ok | 0 versteckt nach Abwärts- und Aufwärts-Scroll |
| M8 | Hero-CTA im ersten Bildschirm | ok | Unterkante 620 px |
| M9 | Textgröße | ok nach Review | Fließtext, Menü, Buttons, Karten, Fuß, Beleg-Karte, Formular-Labels, Bewertungsnamen ≥ 16 px (vier Stellen von 14 bis 15,5 auf 16 gesetzt). Unter 16 (Beschriftung, mindestens 14): Labels, Briefkopf-Adressen, Index-Zahlen. `[FEHLT]`-Hinweise 14 px |
| M10 | Atmen | ok | genau 2 (Hero-Button, Formular-Button) |
| M11 | Text = approved copy | ok | `check_text.py`: 245 Segmente, 0 Abweichungen (erlaubt: `[FEHLT]`-Hinweise und Prototyp-Zeile) |

## Track-B-Prüfungen (T1 bis T10)
| # | Prüfung | Ergebnis | Beleg |
| --- | --- | --- | --- |
| T1 | Scroll-Ruckler | ok | 394 Frames, Mittel 8,3 ms, Maximum 17 ms, 0 über 50 ms, 0 Long Tasks |
| T2, T3 | Loops, Video | entfällt | kein Video |
| T4 | Reduced Motion (`?rm=1`) | ok | Atmen 0, Hero-Foto ohne Zoom, keine Transforms auf `.rv`, Schritte 1111, Lead 50/50 Wörter, erster Streifen offen |
| T5 | Komponenten aus | ok | Rückruf-Reiter und Menü ausgeblendet: Seite voll nutzbar, 12 Verweise auf `#anfrage` |
| T6 | Gewicht | ok | 0,65 MB gesamt, 0,14 MB erster Bildschirm (`perf.md`) |
| T7 | X-ray | ok | Taste `x`: Streifen blau, Haarlinien rot gestrichelt |
| T8 | CTA im ersten Bildschirm | ok | 620 px, Foto-Zoom läuft währenddessen |
| T9 | Tastatur | ok nach Review | Prüfer: geschlossenes Menü und Panel blieben im Tab-Pfad. Behoben: `visibility:hidden` im geschlossenen Zustand, Fokus geht beim Öffnen ins Menü und kehrt zurück, Escape schließt beide |
| T10 | Kontrast über Medien | ok nach Review | Prüfer: geschlossene Streifen hatten weißen Text auf hellem Foto (1,2 bis 1,4 zu 1). Behoben: Verlauf über die ganze Höhe, 62 bis 86 % Anthrazit |

## Globale Punkte
| # | Punkt | Ergebnis | Beleg |
| --- | --- | --- | --- |
| G1 | Raster | ok | linke Kante 144 px bei 1440 für alle Sektionen |
| G2 | Rhythmus | ok | Weiß, Creme, Weiß, Creme, Creme, Weiß, Creme, Weiß, Creme, Weiß, dunkel |
| G3 | Text | fixed | H1 brach "In" ans Zeilenende: Zeilenumbruch gesetzt; Telefonzeile im Hero ohne Umbruch |
| G4 | Bilder | ok nach Review | Prüfer: Salbei-Ton auf den Skylines war grau (Filter auf dem Container). Behoben mit `background-blend-mode:luminosity`, im Screenshot geprüft |
| G5 | Farbe | ok | #4E6F55 nur für Buttons; Blur-Test (7 px): die zwei Salbei-Buttons bleiben die einzigen gesättigten Flächen |
| G6 | Typografie | fixed | Fraunces bei Größe 144 war zu fein und eng ("Verteidigung" klebte): optische Größe automatisch, Gewicht 350, Laufweite -.012em |
| G7 | Buttons | ok | gleicher Stil in allen Sektionen |
| G8 | gegen Mockup | ok, Abweichungen unten | Reihenfolge, Farben, Proportionen gleich |
| G9 | Hover | ok | Streifen öffnet (gemessen: Streifen 4 aktiv), Karte hebt 3 px |
| G10 | Sticky Header | ok | schrumpft beim Scrollen (84 auf 68 px), Adressen blenden aus |

Abweichungen zum Mockup (bewusst): Briefkopf-Adressen im Kopf statt in einer eigenen Zeile; Skylines ohne Verbindungslinie (die Linie zwischen den Büros ist die senkrechte Haarlinie der Spalten); Beleg-Karte am Hero-Rand statt Plaketten im Hero.

## Sektionen
| Sektion | Ergebnis | Beleg |
| --- | --- | --- |
| Notfall, Kopf | ok | Streifen, Logo, zwei Adressen, Wort Menü, Button; Menü öffnet Vollbild mit Notfall-Zeile (gemessen: öffnet, schließt) |
| Rückruf-Reiter | ok | Panel 300 px breit, Standort und Zeitfenster wählbar, Hinweis ohne Falldaten |
| 1 Hero | fixed | Namensschild lag hinter der Beleg-Karte: höher gesetzt; Karte auf 480 px verbreitert (Zeilenumbruch in den Zahlen) |
| 2 Beweis | ok | fünf Plaketten |
| 3 Mandanten | fixed | doppelte Beschriftung "Mandanten" entfernt; zwei Foto-Karten mit Link-Pfeil, ganze Karte ist Link |
| 4 Leistungen | fixed | Titel der schmalen Streifen waren abgeschnitten: senkrechte Schrift, Index-Code oben (überlappte vorher); Streifen öffnet und zeigt Text und Link |
| 5 Ablauf | ok | haftender Titel, große Ziffern, Linie füllt sich, Zähler zählt |
| 6 Über Dr. Stürzl | ok | Foto mit Salbei-Platte, Lead-Absatz füllt sich (33 von 50 Wörtern bei halber Strecke), Zeitleiste, Zitat |
| 7 Bewertungen | fixed | Karten waren Creme auf Creme (unsichtbar): weiß mit Haarlinie |
| 8 Vertraulich | ok | zwei Spalten mit Haken |
| 9 Fragen | ok | Geisterwort, nur eine Frage offen |
| 10 Standorte | fixed | Verbindungslinie über den Skylines zeigte nur Bogenreste: entfernt |
| 11 Abschluss | ok | Split, drei Kontaktwege, Formular wechselt Schritt (gemessen: Schritt 3 von 3, Button "Vertraulich anfragen") |
| Gruß, Fuß | fixed | "Mit freundlichen Grüßen" saß 32 px zu weit links: Einzug gleich der Spalte |

## Interaktion
Menü 8 Einträge (7 Ziele plus Notfall), alle Anker landen korrekt. Rückruf-Reiter öffnet und schließt. Streifen reagieren auf Hover, Fokus und Klick. FAQ: nur eine offen. `tel:` und `mailto:` korrekt. Formular: Felder ok, Absenden bewusst ohne Funktion (Prototyp).

## Ergebnis
Fixed: 11 (optische Größe der Schrift, H1-Umbruch, Namensschild, Beleg-Karte, doppelte Beschriftung, Streifentitel, Index-Überlappung, Bewertungskarten, Verbindungslinie, Gruß-Einzug, Textgrößen). Offen (nur Daten, als `[FEHLT]` markiert): Frankfurter Adresse, Notfallnummern-Freigabe, Rückruf-Zusage, Einwilligungstext, Preis und Dauer der Erstberatung, Parken, Karte mit Einwilligung, Kostenseite, FAQ-Antworten (kommen später), 14 `#`-Platzhalter (Leistungsseiten, Profilseiten, Impressum, Datenschutz, Cookie).

(erste Runde, vor dem Prüfer)

## Prüfer (frischer Agent, 2026-10-11)
21 Lücken, 2 Blocker. Behoben: Hero-Telefon wählte nur Frankfurt (jetzt zwei Links), Telefonnummern im Abschluss als Links, nicht freigegebene Angaben (anwalt.de, Zitat 2) mit [FEHLT]-Hinweis ("Dr." danach von Martin bestätigt, Hinweis entfernt), doppeltes Zitat entfernt, Kontrast der Streifen, Salbei-Ton der Skylines, Tastatur und Fokus für Menü und Panel, drei fehlende Abschluss-Zeilen, Rückruf-Reiter übergibt Standort und Rückruf an das Formular, Platzhalter und Maximallänge im Themenfeld, Textgrößen, Fotos (Streifen und Mandanten-Karten ohne Dopplung des Porträts), JSON-LD ohne Frankfurter Straße, Mandanten-Karten verlinken auf `#` statt Formular, Rückruf-Reiter in Anthrazit. Offen oder bewusst nicht geändert: Hero-Aufbau B ist näher an A als gewünscht (gleiche Reihenfolge und gleiche Texte, gesetzte Vorgabe der geprüften Kopie), nur sechs echte Fotos vorhanden, Tracking-Hooks fehlen im Prototyp (Spezifikation im Handoff), H1 ohne Kernwort "Steuerstrafrecht" (steht im Title).

**Visual check done in Chrome, 58 items checked, 26 fixed, 0 open**

## Nachtrag nach Martins Feedback (2026-10-11)
Hero ohne Telefon-Pille, Hinweise zu bestätigten Daten entfernt, Karten je Standort (Klick lädt Google Maps, im Chrome geprüft: beide Pins sichtbar), Text-Check 250 Segmente, 0 Abweichungen.
