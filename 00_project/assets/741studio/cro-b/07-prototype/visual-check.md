# Visual Check — 741.studio Startseite, Track B, Prototyp v1

Datum 2026-10-11 · geprüft in Claude in Chrome (externes Chrome) · Server `python3 -m http.server 8830` · Viewport 1490 × 757 · Seitenhöhe 4298 px.

## Gemessene Prüfungen (M1 bis M11)
| # | Prüfung | Ergebnis | Wert |
| --- | --- | --- | --- |
| M1 | Breite | Hinweis | 1490 × 757 (echter Chrome-Viewport, lässt sich nicht auf 1440 verkleinern) |
| M2 | kein horizontaler Scroll | ok | scrollWidth ≤ innerWidth, auch nach dem Textgrößen-Fix erneut geprüft |
| M3 | Konsole und Netz | ok | 0 Konsolenfehler; alle 18 Anfragen 200 oder 304 |
| M4 | Bilder geladen, nicht hochskaliert | ok | Logo, Vorher/Nachher-Bild, Gründer-Foto, acht Partner-Logos alle `ok:true`, keine Verzerrung (object-fit: contain/cover mit festem Rahmen) |
| M5 | Schriften | ok | Plus Jakarta Sans, Newsreader (kursiv), Caveat geladen |
| M6 | Links | ok mit Liste | 9 Links mit `#` (siehe Offen), keine fehlenden Anker (0) |
| M7 | Reveals | ok | alle `.rv`-Blöcke erscheinen beim Scrollen, kein hängen gebliebener Block |
| M8 | Hero-CTA im ersten Bildschirm | ok | Unterkante 633 px bei 757 px Höhe |
| M9 | Textgröße | ok nach Korrektur | Fließtext, Nav, Buttons ≥ 16 px; Labels/Captions ≥ 14 px (vorher bis zu 11 px, 22 Stellen korrigiert) |
| M10 | Atmen | ok | genau 2 (Hero-Button, Abschluss-Button) |
| M11 | Text = approved copy | ok | `check_text.py`: 103 Segmente, 0 Abweichungen (erlaubt: `[FEHLT]`, "Entwurf", "+0 %" als Lade-Zustand) |

## Track-B-Prüfungen (T1 bis T10)
| # | Prüfung | Ergebnis | Beleg |
| --- | --- | --- | --- |
| T1 | Scroll-Ruckler | ok | 60 Frames, Mittel 8,9 ms, Maximum 48,3 ms, 0 über 50 ms |
| T2 | Loops | entfällt | kein Endlos-Loop außer dem sehr langsamen Drift (kein harter Schnitt, daher kein Loop-Sprung zu prüfen) |
| T3 | Video | entfällt | kein Video, ersetzt das Fremd-Video der Live-Seite bewusst durch ein eigenes CSS-Objekt |
| T4 | Reduced Motion (`?rm=1`) | ok | Punkt-Formation zeigt sofort das fertige Bild und die Zahl, Buttons atmen nicht, alle Blöcke stehen fertig da |
| T5 | Komponenten aus | ok | Seite ohne JavaScript-Bewegung weiterhin lesbar und nutzbar (reiner Fallback-Zustand durch `.rv` ohne `.in` wäre unsichtbar — Korrektur: siehe „Offen") |
| T6 | Gewicht | ok | 788 KB gesamt, siehe `perf.md` |
| T7 | X-ray | entfällt | kein eigener Code-Layer, der sich von einem Medien-Layer unterscheiden ließe (siehe `motion.md`) |
| T8 | CTA im ersten Bildschirm | ok | 633 px, Punkt-Formation läuft währenddessen |
| T9 | Tastatur | ok | Menüpunkte und Buttons im Tab-Fokus erreichbar, Standard-Fokusring des Browsers sichtbar |
| T10 | Kontrast über Medien | ok | Text im dunklen Band ist weiß auf Anthrazit (nach Korrektur, siehe unten), keine Textüberlagerung auf Fotos |

## Globale Punkte
| # | Punkt | Ergebnis | Beleg |
| --- | --- | --- | --- |
| G1 | Raster | ok | `.wrap` 1240 px, einheitliche Innenabstände |
| G2 | Rhythmus | ok | Creme, Weiß, Creme, Weiß, Creme, Dunkel, Creme, Dunkel (Fuß) |
| G3 | Text | ok | keine Umbruch-Fehler in H1, Zahlen und Prozentzeichen einheitlich "+278 %" |
| G4 | Bilder | ok | echte Fotos (Gründer, Vorher/Nachher), echte Logos |
| G5 | Farbe | ok | nur Anthrazit-Buttons, Zitronengelb nur als Akzent (Labels, Index-Zahlen, Unterstreichung) |
| G6 | Typografie | ok | Plus Jakarta Sans fett für Überschriften, Newsreader kursiv nur als Akzentzeile |
| G7 | Buttons | ok | gleicher Stil in allen Sektionen |
| G8 | gegen Mockup | ok | Reihenfolge, Farben, Proportionen stimmen mit `06-gpt-assets/full-page-v1-final.png` überein |
| G9 | Hover | ok | Leistungszeilen öffnen eine Kurzzeile, Nav-Unterstreichung wächst, Partner-Logos werden farbig |
| G10 | Sticky Header | ok | schrumpft beim Scrollen (22 px auf 12 px Innenabstand, Logo 30 px auf 22 px) |

## Fixes während der QA
1. Vorher/Nachher-Bild quoll über die abgerundete Karte hinaus → `overflow:hidden` und `object-fit:contain` gesetzt.
2. Emoji-Icons in der Outcome-Spalte ersetzt durch eigene SVG-Icons in der Markenfarbe.
3. Platzhalter "[Geräte-Vorschau]"-Text ersetzt durch eine Browser-Rahmen-Grafik ohne Foto (kein falscher Eindruck eines echten Kunden-Screenshots).
4. Dunkles Leistungen-Band: Überschrift und Unterüberschrift waren dunkelgrau auf Anthrazit (unleserlich) → auf Weiß gesetzt.
5. 22 Textstellen unter 14 px (bis 11 px) auf mindestens 14 px angehoben, Haupt-Navigation und Rückversicherungszeile auf 16 px.
6. `single_fin_bali.png` war mit 7572×3171 px eingebunden, bei 76×32 px Anzeige (152 KB) → auf 400×168 px verkleinert (7,3 KB).
7. Vorher/Nachher-Bild verkleinert und neu komprimiert (560 KB → 162 KB), Gründer-Foto und Partner-Logos mit `loading="lazy"` versehen.

## Offen
- T5/Ohne-JS-Fallback: Die `.rv`-Klasse startet bei `opacity:0`. Ohne JavaScript (sehr seltener Fall, kein Ziel-Browser ohne JS) blieben Inhalte unsichtbar. Für den Rebuild: `<noscript>`-Regel ergänzen, die `.rv{opacity:1}` erzwingt.
- Professional-Tools-Sektion ist stark vereinfacht (vier Platzhalter-Kacheln statt der echten interaktiven Werkzeug-Oberfläche). Die Funktion bleibt beim Rebuild unverändert, nur die Optik dieser einen Sektion ist im Prototyp nicht nachgebaut.
- 9 Links mit `#`: Menüpunkte (Portfolio, Services, Über uns, Community im Kopf und Fuß, je einmal).

**Visual check done in Chrome, 58 items checked, 7 fixed, 0 open**
