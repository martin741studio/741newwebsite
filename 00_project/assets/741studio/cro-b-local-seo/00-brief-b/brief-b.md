# Brief B — 741.studio Local-SEO-Seite (Track B)

Start 2026-10-19, direkt im Anschluss an die Portfolio-Seite (gleiches Muster, gleiche Lehren). Kunde ist 741.studio selbst.

## Auftrag (Martins Worte, 19.10.2026)
„Das Nächste ist die Local-SEO-Seite für Deutsch und Englisch. Die müssen wir überarbeiten. Das wird unsere neue Landing Page Review, auf die wir auch den Traffic ziehen, hauptsächlich mit den 300 Videos. Die Leute können und sollen dort eine kostenlose Analyse machen, was das Hauptding ist. Wir präsentieren, was wir da von der Arbeit selber machen. Das muss durch ein Track-B-Workflow-Setup."

## Bereits bekannt (aus Dateien, nicht erneut gefragt)
- **A1 Seiten:** `04_site/de/pages/local-seo.html` (DE, 1244 Zeilen) und `04_site/pages/local-seo.html` (EN, 1145 Zeilen). Beide live.
- **A2 Conversion-Ziel:** die bestehende Sichtbarkeits-Analyse — hier NICHT nur ein Link wie auf der Portfolio-Seite, sondern das vollständige Quiz-Overlay ist **direkt in dieser Seite eingebaut** (`#qzOverlay`, 6 Schritte, Supabase-Insert in `advertorial_leads`, WhatsApp+E-Mail-Zustellung, FB-Pixel-Event, UTM-Erfassung). **Dieses Overlay samt Script bleibt unverändert** — es ist die echte Lead-Erfassung, kein Mockup.
- **Traffic-Quelle:** haupsächlich die "300 Videos" (vermutlich YouTube-Content-Programm). Seite muss als Landing Page für kalten Video-Traffic funktionieren — starker, schneller Hook, eine klare CTA (die Analyse), keine Ablenkung.
- **Ziel laut Martin:** „präsentieren, was wir da von der Arbeit selber machen" — die Seite muss den echten Prozess/die echte Arbeit zeigen, nicht nur Behauptungen.
- **Bereits echte, verifizierte Inhalte auf der heutigen Seite (DE), wiederverwenden statt neu erfinden:**
  - Roadmap/Prozess: 3 Schritte (Status-Quo-Analyse, Google-Profil-Optimierung, Bewertungen & Zitate).
  - Proof-Wall: 29 echte Vorher/Nachher-Ranking-Sprünge aus verschiedenen Branchen (Gesundheit, Gastgewerbe, Recht, Agentur), siehe `02-data/dataset.md`.
  - Echtes Beispiel: Google-Maps-Sichtbarkeits-Scan Agnes Speidel/Olching (81 Messpunkte, Suchbegriff „heilpraktiker"), mit Ziel-Simulation daneben.
  - 7 Vorher/Nachher-Analytics-Screenshots (`/assets/local-seo/images/analytics_1-7.webp`).
  - 5 Video-Testimonials (YouTube-Embeds).
  - Gründer-Statement (Martin, Foto + Zitat).
  - Wachstums-Potenzial-Vergleich: explizit als „Illustrative Potenzialwerte" gekennzeichnet (keine Einzelfall-Garantie) — diese Kennzeichnung bleibt.
- **EN-Lücke:** die EN-Seite hat aktuell KEINE Proof-Wall und KEIN Maps-Vergleichsbeispiel (nur Roadmap, Testimonials, Gründer). Für Track B auf DE-Parität bringen (gleiche echten Fakten, übersetzt) statt die Lücke zu übernehmen.
- **Hero:** aktuell gemeinsame Partial `{{> hero-slider_de }}` / `{{> hero-slider }}` — wird auch von der Startseite benutzt. **Diese Partial wird NICHT verändert** (würde die Startseite mitverändern). Local-SEO bekommt stattdessen einen eigenen, seiten-spezifischen Hero, wie schon bei der Portfolio-Seite.
- **B8 Marke:** wie Portfolio-Seite — Logo, Lemon `#fac118`, Ash-Grey `#8c8c8c`, **heller Creme-Grund `#f7f6f2`** (Pflicht seit Martins Feedback zur Portfolio-Seite, kein dunkler Hintergrund), Plus Jakarta Sans / PP Neue Montreal.
- **Bestehendes Design-System:** Prototyp wird wie bei Portfolio direkt im echten Live-Template gebaut (keine getrennte Mockup-Phase), Freigabe vor Go-Live trotzdem nötig.

## Prozess-Entscheidung (aus dem laufenden Chat, nicht erneut gefragt)
- **A7 Prozess:** Stop nur an den 2 festen Gates (Element-Pool-Abstimmung, fertiger Prototyp). Dazwischen arbeitet der Agent autonom durch — Martin hat ausdrücklich gesagt, er will keine weiteren Rückfragen/Entscheidungskarten während der Umsetzung.
- **B10 Stimmung:** wie Portfolio-Seite — bewiesen/selbstbewusst, nicht verkäuferisch/reißerisch.
- **H35 Rote Linie:** lange Ladezeit/Ruckeln auf Mobile, erfundene Zahlen, Bewegung ohne Grund, eigenes Mini-Design-System statt des echten.

## Noch offen für die Umsetzung (Agent entscheidet, Martin sieht es an den Gates)
- Signature Idea (B4): wird nach der Element-Pool-Abstimmung formuliert.
- Genaue Reihenfolge/Gruppierung der Sektionen (Hero → Prozess → Beweis-Beispiel → Proof-Wall → Testimonials → Gründer → CTA).
- Wie die Proof-Wall visuell neu dargestellt wird (aktuell: einfaches Grid aus Avatar-Karten).

## Lieferformat
Direkt im echten Live-Template (wie Portfolio-Seite), DE + EN. Kein Go-Live ohne Martins Freigabe am zweiten Gate. Das Quiz-Overlay-Script bleibt unangetastet.
