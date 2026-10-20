# Master-Prompt: Vorher/Nachher-Story (Local-Falcon-Ergebnis, 1080×1920)

> Für jeden neuen Kunden diesen Prompt nutzen (in einer Claude-Code-Session im Repo `~/741website`).
> Das Template existiert bereits: `07_social/templates/before_after_story.html` — NICHT neu bauen, nur CONFIG anpassen.

---

Erstelle eine Vorher/Nachher-Story (1080×1920) für einen 741-Kunden aus dem bestehenden Template `07_social/templates/before_after_story.html`.

**Input, den ich dir gebe (mehr brauchst du nicht):**
1. Kunde/Branche + Stadt (z. B. „Versicherung in Wilster")
2. Das gescannte Keyword (z. B. „versicherung wilster")
3. Scan-Geometrie aus dem Local-Falcon-Report: **Center-Koordinaten** (stehen im Report, z. B. „53.9229195, 9.3752509"), Grid-Größe (9×9) und Pin-Abstand („0.75 kilometers between map pins") — alternativ Report-Link/Screenshot, dann liest du das selbst ab
4. Vorher-Ränge und Nachher-Ränge — als Local-Falcon-Screenshot, Report-Link oder kurz beschrieben („vorher überall 15–20+, Mitte 7", „nachher überall 2")
5. Eine echte Ergebnis-Zahl fürs zweite Stat-Feld (z. B. „+63 % mehr Anfragen", „+41 Anrufe/Monat") — wenn ich keine gebe, FRAG NACH statt eine zu erfinden
6. Scan-Datum

**Was du tust:**
1. Nur den `CONFIG`-Block im Template anpassen: `title`, `keyword`, `scanDate`, `stat1`/`stat2`, `center` (lat/lng), `cityLabel` („Stadt, Bundesland"), `rows`, `spacingKm`, `before`, `after`.
   - Die Karten sind ECHTE Karten (Leaflet + CARTO-Voyager-Tiles, zentriert auf die Scan-Koordinaten) — Straßen/Orte laden automatisch, nichts manuell croppen.
   - Grids: `"uniform:X"` für einheitliche Karten, oder 81er-Array (9×9, zeilenweise) wenn ich exakte Werte/einen Screenshot liefere — dann Werte vom Screenshot ablesen. `21` = „20+".
   - Farben/Logik nicht anfahren: Farbskala entspricht Local Falcon (grün ≤3 … rot >15).
2. Als PNG rendern (30s Budget, damit Karten-Tiles laden): `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1080,1920 --virtual-time-budget=30000 --screenshot=07_social/output/before_after_<kunde>_story.png file://…/before_after_story.html`
3. PNG mit Read ansehen: Karten-Tiles wirklich geladen (Straßen sichtbar, nicht grau), nichts abgeschnitten, Headline max. 2 Zeilen (sonst Titel kürzen), keine Pins von Labels verdeckt.
4. Fertige Datei per SendUserFile an Martin schicken.

**Design-Regeln (stehen schon im Template, nicht ändern):**
- 741-CI: Schwarz #111, Gelb #fac118, Anton-Headlines, DM Sans, Halftone-Textur
- „VORHER" = graues Label + rote/orange Pins; „NACHHER" = gelbes Label + grüne Pins — beide auf echter Karte
- Aufbau: Titel, Keyword-Pill + Orts-Pill, 2 Karten, 2 Stats, **Proof-Zeile „Mehr echte Ergebnisse unserer Kunden"** (3 Chips aus `CONFIG.proof` — Standard: Naturheilpraxis #85→#1, Heilpraktiker Freiburg Platz 1, Praxis Stuttgart 0→100 % Top-3; nur durch echte Cases von der Website ersetzen), CTA „Dein Business auch? → Alle Cases auf 741.studio" (`CONFIG.ctaSub`)
- Legal-Zeile „Echter Kunde · Local-Falcon-Scan · Karte © OpenStreetMap/CARTO" + Scan-Datum bleibt immer drauf

**Ehrlichkeits-Regel:** Nur echte Ränge und echte Zahlen verwenden. Wenn Vorher-Daten fehlen (kein alter Scan), sag mir das — dann lassen wir das Vorher-Panel weg oder machen einen neuen Scan, aber wir erfinden keins.
