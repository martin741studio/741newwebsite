# Mobile-Check Variante B (Stürzl Steuerstrafrecht)

Stand: 11.10.2026. Quelle: `_build/template.html` (nur dort geändert), gebaut mit `python3 _build/build.py`.
Breakpoints: Handy und kleines Tablet bis 900 px, Tablet quer / kleiner Laptop 901 bis 1099 px, Desktop ab 1100 px unverändert.

Messmethode: Chrome headless (Google Chrome 154) per Playwright mit echter Viewport-Emulation. Grund: `--headless=new --window-size` kann in diesem Chrome nicht unter etwa 500 px Breite rendern, die Messung bei 360 und 390 wäre damit falsch. Die Messfunktion ist dieselbe Idee wie gefordert (Overflow, breite Elemente, Tap-Ziele, Schriftgrößen), nur per `page.evaluate` statt `--dump-dom`. Screenshots liegen in `07-prototype/screenshots/mobile/`.

## Ergebnistabelle

| Prüfpunkt | 360 | 390 | 430 | 768 | Ergebnis |
|---|---|---|---|---|---|
| Viewport-Meta vorhanden | ja | ja | ja | ja | OK |
| Horizontales Überlaufen (`scrollWidth` <= `innerWidth`) | 360 | 390 | 430 | 768 | OK. Auch mit entfernter `overflow-x:hidden`-Klammer (Body/HTML) kein Überlauf |
| Elemente breiter als Viewport | 0 | 0 | 0 | 0 | OK (auch bei 320: 0) |
| Tap-Ziele unter 44 x 44 px (ohne Links im Fließtext) | 0 von 56 | 0 von 56 | 0 von 56 | 0 von 56 | OK. Checkbox zählt über ihr Label. Auch bei geöffnetem Menü und Rückruf-Panel: 0 |
| Textknoten unter 16 px | nur 14 px | nur 14 px | nur 14 px | nur 14 px | OK. Es sind ausschließlich Labels/Captions (`.lab`, `.ix`, `.tg2`, `.way b`, `.sl`) bei 14 px. Nichts unter 14 px. Buttons, Eingaben, Fließtext: alle >= 16 px |
| Fließtext / H1 | 17 px / 33 px | 17 px / 36 px | 17 px / 40 px | 17 px / 52 px | OK (H1 fluid per `clamp`) |
| Erster Screen (390 x 844): Notfallleiste, Header, H1, Sub-Text, grüner Button | Button endet bei y=623 (Viewport 740) | Button endet bei y=618 | y=608 (932) | y=504 (1024) | OK. Header 64 px, Notfallleiste 65 px (2 Zeilen) |
| Menü-Overlay (Tippen) | OK | OK | n. g. | n. g. | Öffnet/schließt. Schließen-Button oben rechts (48 px, mit Rahmen), 7 Links je 58 px hoch, Notfallnummer unten sichtbar (Ende y=824 von 844). Body-Scroll gesperrt, solange offen |
| Rückruf-Reiter | OK | OK | n. g. | OK | Auf Handy kleine Pille unten rechts (48 px hoch). Panel öffnet vollständig im Screen (390: 56..376 x 438..768), mit `max-height` und Scroll. Schließt per Tipp außerhalb. Wird ausgeblendet, solange der Closer (`#anfrage`) im Bild ist, überlappt das Formular also nicht |
| Leistungs-Streifen | OK | OK | n. g. | OK | Vertikales Akkordeon. Titel horizontal, Plus-Symbol (nur CSS, kein Text). Antippen öffnet, voller Text lesbar (max-height 600 px), geöffneter Streifen springt in die Bildmitte. Lange Titel trennen per Silbentrennung ("Unternehmens-vertretung") |
| Ablauf (`#stepsb`) | OK | OK | n. g. | OK | Einfache vertikale Liste, alle Schritte voll sichtbar. Lead-Absatz (Scroll-Füllung) läuft weiter |
| Standorte | OK | OK | n. g. | OK | Skylines gestaffelt ohne Überlappung (Handy: untereinander, 86 % Breite, versetzt; ab 600 px nebeneinander). Spalten untereinander. Karten-Box 16:9 in voller Breite. Nach "Karte laden": iframe 348 x 195 bei 390, 318 x 178 bei 360 |
| Closer + Formular | OK | OK | n. g. | OK | Text, Wege, 3-Schritt-Formular zuerst, Foto danach als 4:3. Felder 16 px, mind. 52 px hoch. Buttons 52 px, volle Breite, "Weiter" über "Zurück". Schritt 3 (Einwilligung) umbricht jetzt sauber |
| Reviews, Zeitleiste, Vertrauen, FAQ, Footer | OK | OK | n. g. | OK | Einspaltig. FAQ-Zeilen mind. 56 px. Ghost-Wort "Fragen" verkleinert |
| Reduced motion `?rm=1` | OK | | | | Keine Animation (Atmen: `none`) |
| `?client=1`, `?shot=1` | OK | OK | OK | OK | `.flag`/`.proto` ausgeblendet bzw. alle Reveal-Zustände sichtbar |
| Atmender CTA | | | | | Nur Hero-Button und Formular-Button (`.breathe`) |
| Text unverändert | | | | | `check_text.py` mit `--allow "[fehlt]" --allow "Fotos und Logo sind"`: 249 Segmente, 0 nicht gefunden |
| Desktop Pixel-Diff (Original gegen neu) | | | | | Original = Template ohne meinen Mobile-Block, gleiche Kopie. 1100, 1280, 1440, 1920 px, `?shot=1&rm=1`, Viewport für Viewport gescrollt: 0 abweichende Pixel. Zusätzlich 633 Elemente mit je 36 berechneten Stilen und Geometrie bei 1100, 1280, 1440, 1920: 0 Unterschiede. (Ein Full-Page-Screenshot bei 1440/1920 zeigt Rasterrauschen im Frankfurt-Bild. Das ist ein Resampling-Effekt von Chrome beim Full-Page-Screenshot, keine Layout-Änderung) |

n. g. = nicht gesondert geklickt. Overflow, Tap-Ziele und Textgrößen sind bei 430 gemessen, die Interaktionen bei 360 und 390 getestet.

## Was ich geändert habe

- Neuer CSS-Block am Ende von `_build/template.html`, nur in Media Queries. Kleine JS-Ergänzungen (Menü sperrt Body-Scroll, Rückruf-Pille schließt bei Tipp außerhalb und blendet im Closer aus, Streifen: Tap statt Hover auf Handy und Scroll in Sicht).
- Hero: Text zuerst, Foto als ruhiger Block darunter (oben weich ausgeblendet), Namensschild unten im Foto, Proof-Karte statisch darunter ohne Überlappung.
- Header sticky 64 px, Adressen ausgeblendet. Notfall-Nummern, Logo und Menü haben mind. 44 px Tippfläche.
- Mandanten-Karten: Pfeil oben rechts statt eigener Spalte, damit die Listen die volle Breite haben.
- Tablet quer (901 bis 1099 px): Desktop-Layout, aber engere Abstände, Hero-Text und Proof-Karte überlappen nicht mehr.
- Aufgefallen und behoben: Das `height`-Attribut des Über-mich-Bildes überschrieb auf Handy das Seitenverhältnis.

## Offene Punkte (Inhalts- oder Desktop-Entscheidung, nicht von mir entschieden)

1. Platzhalter im Formularfeld "Thema" (`z. B. Durchsuchung, Selbstanzeige, Ermittlungsverfahren`) ist auf Handy abgeschnitten. Kürzerer Text nötig, oder ein mehrzeiliges Feld.
2. Einwilligungs-Label im Formular (Schritt 3): Auf Desktop liegt der Link "Datenschutzerklärung" als eigene Flex-Spalte neben dem Text, weil das Label `display:flex` hat. Auf Handy ist das behoben. Auf Desktop habe ich es nicht angefasst (Vorgabe: Desktop unverändert). Bitte entscheiden, ob dort auch gefixt wird.
3. Zähler "1 : 4" im Ablauf ist auf Handy ausgeblendet (dekorativ, Liste ist statisch). Falls er sichtbar bleiben soll, bitte melden.
4. Reihenfolge Hero auf Handy: Text, Foto, Proof-Karte. Alternativ Proof-Karte direkt unter dem Text, vor dem Foto. Das wäre eine Reihenfolge-Entscheidung.
5. Bei 320 px Breite (und 640 px Höhe) liegt der Hero-Button knapp unter der Falz. Bei 360 bis 430 px ist er sichtbar.
6. Die Streifen im Tablet-Querformat (901 bis 1099 px) zeigen den Titel des ersten geschlossenen Streifens ("Selbstanzeige und steuerliche Korrekturen") gekürzt, wie auf Desktop.
