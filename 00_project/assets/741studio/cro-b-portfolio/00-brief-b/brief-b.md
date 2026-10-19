# Brief B — 741.studio Portfolio-Seite (Track B)

Start 2026-10-19. Kunde ist 741.studio selbst. Ziel: die bestehende Portfolio-Seite ersetzen, nicht die Startseite (die Startseite bleibt unverändert — ein früherer Track-B-Versuch dafür wurde am 12.10. verworfen, siehe [[741studio-cro-track-b-pilot]], das ist ein anderer Auftrag).

## Bereits bekannt (aus Dateien, nicht erneut gefragt)
- **A1 Seite:** `04_site/de/pages/portfolio_full.html` (DE) und `04_site/pages/portfolio_full.html` (EN). Live, Vite/Handlebars-Baustein (siehe [[741studio-design-system]]).
- **A2 Conversion-Ziel:** die bestehende Sichtbarkeits-Analyse (Quiz, `data-qz`-Knöpfe, `sichtbarkeits-analyse.html`). Lieferung der Analyse per WhatsApp und E-Mail. Kein Calendly/cal.com auf der Haupt-Seite (siehe [[booking-link-convention]]).
- **A6 Branche/Grenzen:** keine HWG-Regeln für 741.studio selbst. Die SEO-Case-Studies zeigen teils Gesundheitspraxen (Bernd Laserstein, Veronika Schlirf) — nur bereits veröffentlichte Zahlen von deren eigenen, freigegebenen Case-Study-Seiten übernehmen, keine neuen Heilaussagen.
- **B8 Marke:** Logo `assets/images/logo_white.png` / `logo_black.png`. Akzentfarbe `--brand--lemon #fac118`, Grauton `--brand--ash-grey #8c8c8c`, warmer Creme-Grund. Schrift: Plus Jakarta Sans (Fließtext).
- **Bestehendes Design-System:** gilt für die Live-Seite. Track-B-Prototyp bleibt lokal mit eigenem Look, bis Martin ihn freigibt (dann Umbau auf das Partial-System vor Go-Live).
- **H31 Technik:** eigene Vite-Website, voll bau-/codebar, keine CMS-Grenze.
- **Inhalt bereits vorhanden, nicht neu erfunden:**
  - SEO-Band: 4 Case Studies mit echten, bereits veröffentlichten Zahlen (siehe `02-data/dataset.md`).
  - Website-Band: 17 echte Kundenprojekte mit Mockup-Bildern und Beschreibungstexten, aus dem aktuellen Portfolio-Code übernommen (`02-data/dataset.md`).

## Runde 1 (2026-10-19)
- **B10 Stimmung (5 Wörter):** bewiesen / selbstbewusst.
- **B10 Nie (3 Wörter):** verkäuferisch / reißerisch.
- **A7 Prozess:** Stop nur an den 2 festen Gates (Element-Pool-Abstimmung, fertiger Prototyp). Dazwischen arbeitet der Agent autonom durch.
- **H35 Rote Linie:** zu lange Ladezeit / ruckelig auf Mobile ist der klarste Fehlerfall. Zusätzlich gilt aus den Projektregeln: erfundene Zahlen, Bewegung ohne Grund, eigenes Mini-Design-System statt des echten — alles vermeiden, auch ohne dass Martin es einzeln angekreuzt hat.

## Runde 2 (2026-10-19)
- **C11 Referenzen:** Martin hat keine eigenen Vorbilder genannt. Agent schlägt 5–8 vor (siehe `02-data/references/board.md`), mit Begründung.
- **E22 Hero-Video:** nein. Bild und Zahlen reichen, dazu eine ruhige Zahlen-Animation beim Scrollen statt Video.
- **G30 Haupt-CTA:** die bestehende Sichtbarkeits-Analyse (Quiz). Kein neues Pop-up.
- **SEO-Band-Inhalt (überholt am 19.10., siehe decisions.md):** ursprünglich nur die 4 bestehenden Case Studies. Nach Checkpoint 1 erweitert um Suriya und Hüwel (6 Case Studies), weil Martin die 4 als nicht beeindruckend genug bewertete und für beide Kunden öffentliche Zustimmung bestätigt hat.

## Runde 3 (2026-10-19)
- **Kontakt-Pop-up-Frage geklärt:** Martin meinte die bestehende Sichtbarkeits-Analyse, kein separates Pop-up. Kein Zusatzaufwand nötig.

## Noch offen für die Umsetzung (Agent entscheidet, Martin sieht es an den Gates)
- Signature Idea (D17–20): wird in B4 formuliert, nachdem die Element-Pool-Abstimmung (Checkpoint 1) vorliegt.
- Max. 4 interaktive Komponenten: aus den "Ja"/"Vielleicht"-Stimmen des Element-Pools.
- Zwei Bänder, eine Seite (Martins Entscheidung aus dem Chat): oben ein Umschalter "SEO-Erfolge" / "Website-Projekte", jede Karte mit Bild, Ergebnis-Zahl (SEO-Band) bzw. kurzem Projekttext (Website-Band).

## Lieferformat
Lokaler HTML-Prototyp (1440 px Desktop, danach Mobile), Drive-Mirror nach B9. Kein Go-Live ohne Martins Freigabe am zweiten Gate.
