# Visual Check — Landingpage 741 KI-CMS (Prototyp v3)

Datum 2026-10-13 (v3 nach Martins Feedback: Hero = Produkt in Aktion, Fallbeispiel mit echtem Zitat, Vorher/Heute als Pflege-Ablauf, kein Symbolbild; Punkte der Sektionen 2 bis 6 und 8 bis Fuß unverändert gegenüber v2) · Geprüft in Claude in Chrome (externes Chrome) · Server `python3 -m http.server 8991` (launch.json `kicms-proto`) · echter Viewport 1440 × 813 (Layout auf max. 1200 px Inhalt begrenzt) · ohne `?shot=1`, Seite einmal ganz durchgescrollt.

## Gemessene Prüfungen (M1 bis M11, M4b)
| # | Prüfung | Ergebnis | Wert |
| --- | --- | --- | --- |
| M1 | Breite | ok | 1440 |
| M2 | kein seitliches Scrollen | ok | scrollWidth ≤ innerWidth |
| M3 | Konsolenfehler | ok | keine |
| M4 | Bilder geladen, nicht hochskaliert | ok | 4 Bilder: Logo 300→59 px, Avatar 224→52 px, Foto 1000→500 px, Logo weiß 300→50 px (Hüwel-Screenshots und Symbolbild entfernt) |
| M4b | Verzerrung | ok | keine (object-fit cover bei Fotos/Screens) |
| M5 | Schriften | ok | DM Sans und Fraunces geladen (`document.fonts.check` true) |
| M6 | Links | ok | 6 CTAs → https://cal.com/741-studio-simjzw/30min (neuer Tab); Live-Link praxis-huewel.de; 13 × `#` nur in Kopf/Fuß-Menü (Seitenrahmen, im Rebuild die echten Partials) |
| M7 | nach Scrollen sichtbar | ok | 0 versteckt |
| M8 | Hero-CTA im ersten Bildschirm | ok | Unterkante 596 px (Grenze 701 px); Gründer-Foto Unterkante 808 px < 813 px |
| M9 | Text ≥ 16 px | fixed | v3: Nummern-Kreise in den Abläufen 15,2 → 16 px; früher: | 3 Stellen mit 15,2 px (Badge, Kennzahl-Karte, FEHLT-Markierung) auf 16 px gehoben, jetzt 0 |
| M10 | Atmen nur Hero + Abschluss | ok | genau 2 |
| M11 | Text = freigegebene Copy | ok | 174 Segmente, 0 Abweichungen außer dem Seitenrahmen (Menü, "Start Now", © 2026 741.Studio) |

## Globale Punkte (G1 bis G10)
| # | Punkt | Ergebnis | Notiz |
| --- | --- | --- | --- |
| G1 | Ausrichtung | ok | ein 1200-px-Raster, gleiche linke Kanten |
| G2 | Abstände | ok | 96 px Sektionen, Hero 56/72 px |
| G3 | Text | fixed | H1-Zeile "Deine Website mit KI-CMS:" brach um, jetzt einzeilig wie im Mockup; Kennzahlen brachen um ("0 fremde Skripte"), jetzt einzeilig; Abschluss-Häkchen auf zwei Zeilen, jetzt eine Reihe |
| G4 | Bilder | ok | echte Screens und Foto scharf, kein Halo; Foto-Ausschnitt zeigt Gesicht |
| G5 | Farbe | ok mit Hinweis | eine CTA-Farbe im Seiteninhalt (Dunkelgrün-Anthrazit); der gelbe "Start Now"-Button gehört zum Seitenrahmen der Live-Seite |
| G6 | Typografie | ok | DM Sans + Fraunces kursiv nur im H1-Akzent; Zeilenlänge Fließtext < 75 Zeichen |
| G7 | Buttons gleich | ok | gleiche Pille in allen Sektionen, hell auf Dunkel |
| G8 | Vergleich Mockup | ok | Reihenfolge, Layout, Farben wie Mockup; Unterschiede (gewollt, Martin 13.10.): Hero zeigt statt der Hüwel-Seite im Laptop das Chat-Fenster, Sektion 7 zeigt Zitat und Pflege-Ablauf statt zweier Browser-Rahmen; das Mockup `full-page-v1-final.png` ist dort überholt. FAQ zweispaltig wie Mockup |
| G9 | Hover | fixed | Karten hoben sich nicht (Einblend-Regel blockierte `transform`); behoben, gemessen −4 px; CTA-Hover hebt 2 px, Pfeil 4 px |
| G10 | Sticky Header | ok | 73 px, verdeckt keine Überschrift; Menü-Links sind Platzhalter (siehe offen) |

## Sektionen
| Sektion | Ergebnis | Notiz |
| --- | --- | --- |
| Kopf | ok | echtes Logo scharf, Menü einzeilig |
| 1 Hero | fixed, neu | rechts statt der Hüwel-Seite jetzt ein Chat-Fenster "Beispiel: so läuft eine Änderung" mit Wunsch, Antwort und drei Statuszeilen (Prüfung bestanden, 741 gibt frei, Live in ein bis zwei Minuten) plus Kennzahl-Karte; Kennzahl-Karte verdeckte zuerst die letzte Statuszeile, jetzt darunter; Gründer-Foto mit Titel und Live-Link im ersten Bildschirm |
| 2 Beweis-Leiste | ok | 4 Kennzahlen einzeilig, Linien zeichnen sich |
| 3 Kennst du das | ok | 4 Karten gleich hoch, Icons scharf, CTA sichtbar |
| 4 Paket | ok | 3 + 2 Karten, Links unterstrichen |
| 5 Schritte | ok | Linie zeichnet einmal, Nummern füllen sich, Dauern vollständig |
| 6 Person | ok | Foto mit Gesicht, Text weiß auf Dunkel, Kontrast gut |
| 7 Fallbeispiel | fixed, neu | echtes Zitat von Martin Hüwel (Quelle: Martin Drendel, 13.10.2026) in großer Karte; "So fühlt sich die Pflege an": links "Vorher, typisch bei Baukasten und Agentur", rechts "Heute, mit dem 741 KI-CMS" je 3 Schritte; kurze Tabelle; keine erfundenen Bilder, keine Hüwel-Screenshots mehr |
| 8 Vertiefung | ok | erste Frage offen, Kosten-Tabelle im Akkordeon |
| 9 FAQ | ok | nur eine offen (gemessen), Pfeil dreht |
| 10 Hilfe | ok | Portfolio-Link |
| 11 Abschluss | ok | Häkchen in einer Reihe, Beweiszeile, atmender CTA |
| Fuß | ok | Logo weiß, Menü, © |

## Interaktion
CTA in 6 Sektionen öffnet cal.com im neuen Tab (nichts gebucht). Kein tel:-Link (Kanal ist der Buchungslink). FAQ und Vertiefung: Öffnen und Schließen funktioniert, immer nur eine offen. Zurückscrollen: nichts animiert erneut.

## Ergebnis
Fixed: M9 (Nummern 16 px), G3 (H1-Umbruch, Kennzahlen, Abschluss-Häkchen), G9 (Karten-Hover), Hero (Hüwel-Seite durch Produkt in Aktion ersetzt, Kennzahl-Karte überlappte), Sektion 7 (willkürliches Symbolbild und Hüwel-Screens ersetzt).
Offen: Einverständnis von Martin Hüwel, das WhatsApp-Zitat zu veröffentlichen (kein Platzhalter im Text); Menü-/Fuß-Links `#` (Seitenrahmen, im Rebuild die echten Partials).

Konsole: nur ein Fehler einer Chrome-Erweiterung, keiner der Seite.

**Visual check done in Chrome, 36 items checked, 11 fixed, 2 open**
