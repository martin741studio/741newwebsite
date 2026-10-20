# Handoff — 741.studio Startseite, Track B, Prototyp v1, Desktop

Stand 2026-10-11. Pilot-Lauf von Track B (erstes Mal überhaupt), Kunde ist 741.studio selbst. Nichts ist live. Der Prototyp läuft nur lokal und trägt `noindex,nofollow`.

## 1. Pfade
- Prototyp: `00_project/assets/741studio/cro-b/07-prototype/index.html` (mit `assets/`). Generator `_build/build.py` und `_build/template.html`.
- Bewegung `07-prototype/motion.md`, Gewicht `07-prototype/perf.md`, Prüfdateien `07-prototype/visual-check.md` (58 Punkte, 7 fixed, 0 open), `07-prototype/self-check.md` (30 von 44, Begründung siehe dort).
- Brief `00-brief-b/brief-b.md`. Referenz-Board `02-data/references/board.md` (5 Referenzen + 2 Anti-Referenzen). Element-Pool `00-element-pool/` (24 Elemente, Martins Stimmen `votes-martin-2026-10-11.json`, Auswertung `votes-summary.md`). Konzept `05-gpt-design-doc/concept/concept.md`. Design-Doc und Prompt `05-gpt-design-doc/`. Mockup `06-gpt-assets/full-page-v1-final.png`. Text `04-copy/approved-copy.md`.

## 2. Was aus der Live-Seite bleibt, was neu ist
| | Live-Seite heute | Track B |
| --- | --- | --- |
| Hero | Vorher/Nachher-Bild direkt sichtbar, rotierender Headline-Karussell | dasselbe Bild, aber als Punkt-Formation (Signature Idea), eine feste Headline, Garantie-Pille und Zahl zählen hoch |
| Outcome | drei Spalten, echte Zahlen | inhaltlich unverändert, nur Farben/Typografie angepasst |
| Gründer | keine eigene Sektion | neu: echtes Foto, kurzer Ich-Form-Text, Unterschrift-Akzent (nach Martins Votum: kein Zitat-Großbuchstabe, keine Zeitleiste) |
| Professional-Tools | eigene interaktive Vorführung | im Prototyp stark vereinfacht (vier Platzhalter-Kacheln), Funktion unverändert für den Rebuild |
| Partner-Logos | Karussell | ruhiges, gestaffeltes Einblenden, Graustufen → Farbe beim Hover |
| Leistungen (dunkles Band) | Fremd-Video (Weavy-Demo-Material) im Hintergrund | eigenes, per CSS erzeugtes glänzendes Objekt, driftet leicht; Leistungszeilen zeigen beim Hover eine Kurzzeile |
| Giveaway-/Community-Promo | vorhanden | bewusst weggelassen (Martin: zeitlich begrenzte Aktionen passen nicht zu einem zeitlosen Showpiece) |

## 3. Text und Meta
- Title: 741.studio | Lokale Sichtbarkeit, Websites, Ads, Automatisierung
- Meta Description: 741.studio baut lokale Sichtbarkeit, Websites und Automatisierung für wachsende Unternehmen. 90-Tage-Top-3-Garantie.
- JSON-LD: `Organization` (Name, URL, Logo). Kein `LocalBusiness`-Schema, da 741.studio keine einzelne physische Adresse auf der Startseite nennt.

## 4. Komponentenliste (Track B)
| Komponente | Wo | Funktion |
| --- | --- | --- |
| Punkt-Formation | Hero, Funktion in `<script>` (IIFE, Canvas-freie DOM-Punkte) | Signature Idea: zeigt das Versprechen vor dem Lesen, mit echter Zahl |
| Bento Glide + Hochzählen | Outcome-Kennzahlen | macht Ergebnisse lesbar |
| Hop-Navigation | Kopf (CSS-Hover, kein JS nötig) | kleine Geste, Marke |
| Kopf-Schrumpfen | `#hd` + Scroll-Listener | poliert, ruhig |
| Leistungszeile-Hover, Objekt-Drift | dunkles Band | ersetzt das fremde Video, zeigt Leistungen als Aussage |
| Reveal-once | `.rv` + IntersectionObserver | Grundbewegung für alle übrigen Blöcke |

## 5. Marke
Logo echt (`assets/logo.png`, `logo-white.png`). Farben Anthrazit `#17160f`, Creme `#faf6ea`, Zitronengelb `#fac118`/`#e0ac0a` (einziger Akzent), Dunkelgrün-Anthrazit `#1c2622` (Leistungen-Band), Grün `#16a34a` (nur Kennzahlen, wie heute). Schrift Plus Jakarta Sans + Newsreader kursiv (Akzentwort) + Caveat (Gründer-Unterschrift). Siehe `02-data/brand.md`.

## 6. Bilder und Shoot-Liste
Alle Bilder echt (Live-Seite, siehe `01-input/INVENTORY.md`). Keine neuen KI-Bilder im Prototyp. Shoot-Liste fürs Rebuild: ein echtes "Website-Vorschau"-Bild für die Outcome-Mitte (der Prototyp zeigt dort bewusst nur ein abstraktes Muster statt eines erfundenen Kunden-Screenshots); ggf. ein zweites Gründer-Foto für Abwechslung, falls die Seite wächst.

## 7. Tracking-Spezifikation (Einrichtung gehört nicht zu diesem Workflow)
Events mit Parameter `section` (hero, outcome, gruender, tools, partner, services, abschluss, kopf): `cta_click` (Parameter `section`), `nav_click` (Parameter `target`), `logo_hover` (Partner-Leiste, optional). Bestehende Events der Live-Seite (`generate_lead`, `booking_click`, siehe [[741studio-analytics-conversions]]) bleiben gültig und sollten beim Rebuild wiederverwendet werden.

## 8. [FEHLT]-Liste (Martin entscheidet)
1. Gründer-Text: Gründungsjahr und Kundenzahl bewusst nicht genannt — mit echter Zahl ergänzen, falls gewünscht.
2. Service-Kurzzeilen 2, 4, 5, 6, 7 (Design, Bezahlte Werbung, KI-Automatisierungen, Conversion-Optimierung, Branding) sind Entwürfe, nicht aus der Live-Seite übernommen — zur Freigabe.
3. Outcome-Mitte: echtes "Website-Vorschau"-Bild statt des abstrakten Platzhalter-Musters.
4. Professional-Tools-Sektion: die echte interaktive Vorführung beim Rebuild wieder einbauen (im Prototyp nur vereinfacht dargestellt).
5. Menü- und Fuß-Links (Portfolio, Services, Über uns, Community): Ziel-URLs der bestehenden Unterseiten einsetzen (im Prototyp `#`-Platzhalter).

## 9. Hinweise für den Rebuild
Das bestehende Design-System (Webflow/Handlebars, `{{> header }}`/`{{> footer }}`/`{{> consent }}`, weavy.css) bleibt die Grundlage für jede Live-Umsetzung, siehe [[741studio-design-system]]. Dieser Prototyp ist ein eigenständiges Showpiece zur Entscheidung, keine fertige Vorlage zum Einfügen — eine Umsetzung müsste die Bewegungen in das bestehende System übertragen, nicht das System ersetzen. Schriften selbst hosten (DSGVO) statt über Google Fonts CDN.

## 10. Lernpunkte
- Der Element-Pool mit 24 live abstimmbaren Demos hat die Konzeptwahl getragen; reine Textbeschreibungen hätten nicht gereicht (bestätigtes Muster aus den Kunden-Läufen).
- Ein Bild, das als "Vorher/Nachher-Dot-Map" aussah, war bei genauerem Hinsehen ein größerer, dichterer Screenshot (Local-Falcon-Grid-Tool) — vor dem Bauen eines Wisch-/Vergleichsreglers lohnt sich ein Blick auf die echte Bildgröße und den Bildinhalt in voller Auflösung.
- Dunkle Sektionen brauchen eine eigene, explizite Textfarbe für Überschriften; eine globale `h1,h2,h3,h4{color:...}`-Regel reicht nicht.
- Überdimensionierte Bild-Dateien (ein Partner-Logo war mit 7572×3171 px eingebunden, angezeigt bei 76×32 px) früh im Gewicht-Check prüfen, nicht erst am Ende.
