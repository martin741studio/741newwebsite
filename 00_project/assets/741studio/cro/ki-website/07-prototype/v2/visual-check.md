# Visual Check — Landingpage 741 KI-CMS (Prototyp v2)

Datum 2026-10-13 (v2 nach Checkpoint 2: Gründer-Foto im Hero, Vorher als Symbolbild; v1-Prüfung unverändert gültig für alle übrigen Punkte) · Geprüft in Claude in Chrome (externes Chrome) · Server `python3 -m http.server 8991` (launch.json `kicms-proto`) · echter Viewport 1471 × 863 (Fenster lässt sich auf diesem Mac nicht schmaler stellen; Layout ist auf max. 1200 px Inhalt begrenzt, Messwerte gelten für 1440) · ohne `?shot=1`, Seite einmal ganz durchgescrollt.

## Gemessene Prüfungen (M1 bis M11, M4b)
| # | Prüfung | Ergebnis | Wert |
| --- | --- | --- | --- |
| M1 | Breite | ok | 1471 (siehe oben) |
| M2 | kein seitliches Scrollen | ok | scrollWidth ≤ innerWidth |
| M3 | Konsolenfehler | ok | keine |
| M4 | Bilder geladen, nicht hochskaliert | ok | 7 Bilder: Logo 300→59 px, Avatar 224→52 px, Hüwel 1200→473/552 px, Foto 1000→500 px, Symbolbild 1200→552 px |
| M4b | Verzerrung | ok | keine (object-fit cover bei Fotos/Screens) |
| M5 | Schriften | ok | DM Sans und Fraunces geladen (`document.fonts.check` true) |
| M6 | Links | ok | 6 CTAs → https://cal.com/741-studio-simjzw/30min (neuer Tab); Live-Link praxis-huewel.de; 13 × `#` nur in Kopf/Fuß-Menü (Seitenrahmen, im Rebuild die echten Partials) |
| M7 | nach Scrollen sichtbar | ok | 0 versteckt |
| M8 | Hero-CTA im ersten Bildschirm | ok | Unterkante 620 px (Grenze 701 px); Gründer-Foto Unterkante 842 px < 863 px |
| M9 | Text ≥ 16 px | fixed | 3 Stellen mit 15,2 px (Badge, Kennzahl-Karte, FEHLT-Markierung) auf 16 px gehoben, jetzt 0 |
| M10 | Atmen nur Hero + Abschluss | ok | genau 2 |
| M11 | Text = freigegebene Copy | ok | 156 Segmente, 0 Abweichungen außer der bewusst sichtbaren Markierung [FEHLT: Stimme Hüwel] und dem Seitenrahmen (Menü, "Start Now", © 2026 741.Studio) |

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
| G8 | Vergleich Mockup | ok | Reihenfolge, Layout, Farben wie Mockup; Unterschiede: Chat-Karte ohne erfundenen Text (gewollt), FAQ zweispaltig wie Mockup |
| G9 | Hover | fixed | Karten hoben sich nicht (Einblend-Regel blockierte `transform`); behoben, gemessen −4 px; CTA-Hover hebt 2 px, Pfeil 4 px |
| G10 | Sticky Header | ok | 73 px, verdeckt keine Überschrift; Menü-Links sind Platzhalter (siehe offen) |

## Sektionen
| Sektion | Ergebnis | Notiz |
| --- | --- | --- |
| Kopf | ok | echtes Logo scharf, Menü einzeilig |
| 1 Hero | ok, neu | Gründer-Foto (rund, 56 px) mit "Martin Drendel, CEO und Gründer von 741.Studio" und Live-Link in einer Zeile, im ersten Bildschirm; H1 4 Zeilen, Antwort, CTA, Rückversicherung, 3 Häkchen, Live-Link; Laptop mit echter Hüwel-Seite, Chat-Karte, Kennzahl-Karte |
| 2 Beweis-Leiste | ok | 4 Kennzahlen einzeilig, Linien zeichnen sich |
| 3 Kennst du das | ok | 4 Karten gleich hoch, Icons scharf, CTA sichtbar |
| 4 Paket | ok | 3 + 2 Karten, Links unterstrichen |
| 5 Schritte | ok | Linie zeichnet einmal, Nummern füllen sich, Dauern vollständig |
| 6 Person | ok | Foto mit Gesicht, Text weiß auf Dunkel, Kontrast gut |
| 7 Fallbeispiel | fixed, neu | links KI-generiertes Symbolbild einer veralteten Seite, beschriftet "Vorher (Symbolbild, keine Abbildung der Hüwel-Seite)", rechts echter Screenshot "Heute (echte Seite, Stand 13.10.2026)"; vorher zeigte der Vergleich zwei fast gleiche Screens; Tabelle, Zitat-Platzhalter sichtbar markiert |
| 8 Vertiefung | ok | erste Frage offen, Kosten-Tabelle im Akkordeon |
| 9 FAQ | ok | nur eine offen (gemessen), Pfeil dreht |
| 10 Hilfe | ok | Portfolio-Link |
| 11 Abschluss | ok | Häkchen in einer Reihe, Beweiszeile, atmender CTA |
| Fuß | ok | Logo weiß, Menü, © |

## Interaktion
CTA in 6 Sektionen öffnet cal.com im neuen Tab (nichts gebucht). Kein tel:-Link (Kanal ist der Buchungslink). FAQ und Vertiefung: Öffnen und Schließen funktioniert, immer nur eine offen. Zurückscrollen: nichts animiert erneut.

## Ergebnis
Fixed: M9 (3 Textgrößen), G3 (H1-Umbruch, Kennzahlen, Abschluss-Häkchen), G9 (Karten-Hover), Sektion 7 (Vorher/Heute zeigte zweimal fast dasselbe), Hero (Gründer-Foto unter dem Bildschirmrand, nach oben gezogen).
Offen: [FEHLT: Stimme Hüwel] (Kundendaten); Menü-/Fuß-Links `#` (Seitenrahmen, im Rebuild die echten Partials `{{> header_de }}` / `{{> footer_de }}`).

Konsole: nur ein Fehler einer Chrome-Erweiterung, keiner der Seite.

**Visual check done in Chrome, 36 items checked, 9 fixed, 2 open**
