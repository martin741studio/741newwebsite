# Recherche 3: Hervorhebungs-Techniken pro Sektion (2026-10-12)

Tiles in `references/highlights/`. Grenzen des Rechercheurs: Firecrawl zeigt Ruhezustände, keine Scroll- oder Hover-Bewegung (bei Bewegung wurde Code gelesen). Der Ronas-Code zeigt nur einen Einblend-Effekt (`opacity`+`transform`, 1 s, einmal). Der aufhellende Absatz und die Wellenkante wurden dort im CSS nicht gefunden. Ich habe beides am 2026-10-10 selbst live in Chrome gesehen (siehe Adel-Lauf). Nicht gefunden: Beispiel für versetzte Farbplatte, Akkordeon mit Vorschaubild, geprüfte Hover-Bildliste, Spotlight.

| # | Technik | Besucherin versteht | Beispiel (Sektion) | Passt zu | Rezept | Aufwand | ruhig-sicher |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | Handgezeichnete Wellen-Unterstreichung | diese Phrase ist die Aussage | ronasit.com Hero | Hero, Abschluss | SVG-Pfad unter einem Wort, `scaleX` 0 zu 1 einmal | S | ja |
| H2 | Haftender Seitentitel (sticky) | ein geordneter Weg | ronasit.com/how-we-work, dabbit.app FAQ | Erster Termin, FAQ | 2 Spalten, links `position:sticky; top:120px` | S | ja |
| H3 | Nummer und Kicker | Reihenfolge und Anzahl | ronasit.com, aprilleihuanani.com, zperinatal.com | Leistungen, Schritte | kleines Label über dem Titel | S | ja |
| H4 | Aufleuchtende Aussage | lies diese Zeile zuerst | solreader.com/about (GSAP scrub) | Über mich oder Abschluss, nur einmal | Wörter in Spans, `opacity` .25 zu 1; CSS-only `animation-timeline:view()` | M | ja, wenn langsam |
| H5 | Randnotiz | Nebenbemerkung einer Person | studyhall.design/about, Tufte CSS | Über mich, Standort, Leistungen | Spalte 3 mit kleiner Mono-Schrift | S | ja |
| H6 | Übergroßes Typo-Wort | Sektions-Landmarke | flshfrm.com ("FAQ"), aprilleihuanani.com | FAQ, Abschluss, Leistungen | ein riesiges Wort in Lila bei 6 bis 10 % Deckkraft | S | ja, kontrastarm |
| H7 | Geister-Ziffer | Kapitelnummer, leise | sheets.works/data-viz/the-queue | Für wen, Über mich | Pseudo-Element, Serif, Deckkraft .06 | S | ja |
| H8 | Zahlen mit Linie | Beleg in Zahlen | thoughtbot.com Report, builderstable.net | Beweis-Leiste | statische große Serif-Zahlen, Linie `scaleX` einmal | S/M | ja, ohne Hochzählen |
| H9 | Farbwort in der Überschrift | dieses Wort trägt das Versprechen | btay.ca | Hero, Abschluss | `<em>` in #783ca0 | S | ja |
| H10 | Gestrichelter Ring um ein Wort | Schlüsselwort | aprilleihuanani.com | Über mich, Hero | SVG-Ellipse, `stroke-dashoffset` einmal | S | ja |
| H11 | Foto-Maske in Form | weich, menschlich, eine Signatur-Form | zperinatal.com | Über mich, Für wen | `mask-image` oder `clip-path`, Einblenden per `opacity` | S/M | ja |
| H12 | Überlappendes Zweitfoto | Tiefe, ein Ort | schlosshotel-kitzbuehel.com/en | Über mich | zweites Bild `translate(10%,18%)`; Farbplatte als `::before` | S | ja |
| H13 | Mono-Labels um ein Foto | Stimme der Besucherin | zperinatal.com | Für wen, Über mich | 3 bis 4 absolute Labels | S | ja |
| H14 | Dünnes Laufband | eine Linie, die weitergeht | cosiestudio.com, safestep.org.uk | Beweis-Leiste, Trenner | `translateX` 40 s oder langsamer, statisch bei Reduced Motion | S | nur sehr langsam |
| H15 | Farbblock-Wechsel | neues Kapitel | cosiestudio.com | Über mich, Abschluss | Hintergrund wechselt, keine Bewegung | S | ja |
| H16 | Schrittlinie mit Knoten | Weg in Reihenfolge | ronasit.com/how-we-work | Erster Termin | Linie `scaleX` mit `view()`; Knoten blenden ein | M | ja |
| H17 | Linien-Illustration als Begleiterin | freundliche Führerin | zperinatal.com | Erster Termin, FAQ | statisches Inline-SVG | M (Kunst nötig) | ja |
| H18 | Kursiver Serif-Akzent | Unter-Aussage | zperinatal.com, cosiestudio.com | Leistungen, Bewertungen | `font-style:italic` | S | ja |
| H19 | Ein großes Zitat | eine Stimme statt einer Wand | cosiestudio.com | Bewertungen | ein Slide, Pfeile tauschen `opacity` | S | ja |
| H20 | Plus-Zeichen-Haarlinien-FAQ | kompakte Antworten | cosiestudio.com | FAQ | `<details>`, Plus dreht 45° | S | ja |
| H21 | Einblenden von unten, einmal | ruhige Ankunft | ronasit.com (CSS gelesen) | alle | IntersectionObserver setzt Klasse einmal | S | ja |
| H22 | Hover-Bildliste | Vorschau bei Absicht | unionconstruction.ca, duo-studio.co (nicht gesehen) | Leistungen | verstecktes Bild folgt dem Zeiger | M | nur mit Touch-Ersatz |

**Vorschlag Zuordnung (Rechercheur):** Hero H1 (zweite Wahl H11) · Beweis-Leiste H8 (H14) · Für wen H13 (H7) · Leistungen H3 (H2) · Erster Termin H2+H16 (H3) · Über mich H11+H12 (H5) · Bewertungen H19 (H18) · FAQ H6+H20 (H2) · Standort H5 (H12) · Abschluss H6 auf dunklem Lila, ein Oliv-Button (H15). H4 nur einmal.
**Meiden:** Scroll-Hijacking und horizontales Pinning · Cursor-Spotlight und eigene Cursor · diagonale Clip-Keile und 3D/WebGL-Schrift · schnelle Laufbänder und Schreibmaschinen-Text · Neon-Farben mit großen dunklen Blöcken.
