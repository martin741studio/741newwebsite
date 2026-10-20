# CI-Steckbrief: shuiguru.de (ermittelt 13.09.2026, per Browser-Computed-Style, nicht geraten)

**Theme/CMS:** WordPress 7.0.4 · GeneratePress + GenerateBlocks (Child-Theme `generatepress_child`) — NICHT Enfold/Elementor.

**Font:** durchgehend `"Open Sans", sans-serif` (Body, H1, H2, Buttons).

**Farben (real, per getComputedStyle):**
- Marken-Akzent: **`#10595B`** (dunkles Petrol/Teal) — genutzt für H2-Überschriften UND alle CTA-Buttons. Das ist ihre echte Marke, nicht die Navy-Logo-Farbe aus dem Wordmark-JPEG.
- H1: weiß (`#fff`), 35px, Weight 400 (leicht) — liegt auf farbigem/Bild-Hero.
- H2: `#10595B`, Weight **900** (sehr fett), 43px.
- Body-Text: schwarz auf weiß.
- Nav-Link-Hover: `rgba(36,149,212,0.96)` (helles Blau, sekundär).

**CTA-Button-Stil:** eckig (`border-radius: 0`), weißer Text auf Petrol-Hintergrund, Padding `10px 20px` (Haupt-CTA) bzw. `7px 20px` (Text-Link-Buttons).

**Header/Nav:** Willkommen · Hi! · Angebote · Plancheck vor Baubeginn · Feng Shui in der Arbeitswelt · Feng Shui in Schule und Institutionen · Höfe und Hofgemeinschaften · Philosophie · Erfolge · Kontakt (identisch Desktop/Mobile-Menü).

**Footer:** nur Impressum · Datenschutz · © 2026 ShuiGuru — **keine NAP (Adresse/Telefon) im Footer!** Lücke gegen den Local-SEO-Mindeststandard (`startseite-money-page-standard.md`, Abschnitt E: „NAP im Header/Footer"). Bei der Umsetzung ergänzen.

**Bild-/Foto-Stil:** Die gesamte Startseite hat aktuell **genau 1 Bild — das Logo selbst.** Keine Fotos von Maria, keine Projektfotos, keine Illustrationen. Kein Stil-Statement, sondern schlicht: es gibt noch keine Bilder. Deckt sich mit dem offenen Access-Grant „Material hochladen" im Portal.

**Logo-Assets gesichert:** `00_project/maria-brasse-pages/assets/shuiguru-logo-wordmark.jpg` (1313×339, dunkelblaues Wordmark) + `shuiguru-icon-palace.png` (192×192, Palast-Icon) — permanent im Repo, nicht nur im flüchtigen Scratchpad (Gotcha: eine erste Kopie dieser Dateien ging beim vorherigen Durchlauf durch Scratchpad-Bereinigung verloren, jetzt fest im Repo).

**Gotcha:** Eine erste Farbextraktion (04.09., simple Regex über den HTML-Quelltext) lieferte 12 Hex-Werte, von denen 2 exakt mit WordPress-Gutenberg-Standardpalette übereinstimmen (`#cf2e2e`, `#0693e3`) — das war Rauschen aus Blockinhalten, nicht die echte Marke. Erst der Live-Computed-Style-Check (13.09., via Browser-Tool) lieferte den echten Marken-Akzent `#10595B`.

**Für die spätere WordPress-Umsetzung:** Neue Blöcke/Abschnitte sollten `#10595B` als Akzent + Open Sans nutzen, damit sie sich nahtlos einfügen — nicht das 741-Dashboard-Gelb. Die Freigabe-Seiten im Portal bleiben bewusst im 741-CI (siehe Punkteplan Block 3) — nur die echte Umsetzung auf shuiguru.de übernimmt dieses Steckbrief.
