# Praxis Suriya – Interne Verlinkung: Audit (Stand 10.10.2026)

Nur Analyse. Keine Änderung an der Website ohne Go.

## Methodik

- Crawl aller 89 URLs aus der XML-Sitemap (23 Beiträge, 53 Seiten, 13 Kategorie-Archive).
- Gezählt werden nur Content-Links (Fließtext, Karten, Buttons). Header-Menü und Footer zählen nicht.
- Die 16 Alt-Seiten im Enfold-Layout haben eine Sidebar mit 77–81 Links pro Seite. Diese Links sind in der Spalte "echte Inbound" herausgerechnet.
- Alle 22 "nicht in der Sitemap"-Ziele antworten mit 200. Es gibt keine toten internen Links.

## Kurzfassung – die 6 wichtigsten Punkte

1. **Blog-Artikel verlinken auf keine Leistungsseite.** Die 3 neuen Migräne-/Nervensystem-Artikel haben 0 ausgehende Links. Das ist der größte Hebel für Migräne.
2. **Stadtseiten Mainz/Wiesbaden hängen nur am Footer.** 8 Stadtseiten haben je 1 Content-Inbound. Sie bilden kein Cluster.
3. **/massage-ingelheim/ ist nicht im Menü** und hat 9 echte Inbound-Links. Für die Ads-Ziele (Massage, Ayurveda) ist das die wichtigste Lücke.
4. **Ayurveda-Massage (WP 1511, /ayurveda-therapie/) hat nur 5 echte Inbound-Links.** Die Seite bleibt unangetastet. Links ZU ihr fehlen aber.
5. **Die Enfold-Sidebar auf 16 Alt-Seiten** verlinkt 58 Seiten, 13 Kategorien und 14 Datums-Archive. Darunter: 404-Seite, Login, Shop (82 Wörter), HTML-Sitemap. Das verwässert den Linkgraph.
6. **Doppelte und dünne Seiten** hängen im Graph: 2× Darmgesundheit, 2× Behandlungsangebot, 4 Terminseiten, Home-Duplikat.

## A. Blog → Leistungsseiten (0 ausgehende Links)

| Artikel | Wörter | Out-Links | Empfohlene Links (Anker → Ziel) |
|---|---|---|---|
| /migraene-ist-oft-mehr-als-kopfschmerz/ | 649 | 0 | "Migränebehandlung in Ingelheim" → /suriya-neuro-migraene/ · "Cranio-Neuro-Analyse" → /suriya-cranio-neuro-analyse/ · "Nervensystem beruhigen" → /nervensystem-vagus-beruhigen/ |
| /nackenspannung-migraene/ | 532 | 0 | "Nacken- und Schulterschmerzen behandeln" → /nacken-schulter/ · "Migränebehandlung" → /suriya-neuro-migraene/ · "Nervenregulationsmassage" → /nervenregulationsmassage/ |
| /nervenregulation-vagusnerv/ | 457 | 0 | "SURIYA Nervenregulation" → /nervensystem-vagus-beruhigen/ · "Craniosacrale Therapie" → /craniosacrale-therapie/ · "Nervenregulationsmassage" → /nervenregulationsmassage/ |
| /migraene-und-nackenverspannungen-verstehen-…/ | 824 | nur Sidebar | "Migränebehandlung in Ingelheim" → /suriya-neuro-migraene/ · "Nacken & Schulter" → /nacken-schulter/ |
| /5-ayurveda-rituale-fuer-den-winter-…/ | 808 | nur Sidebar | "Ayurveda in Ingelheim" → /ayurveda-ingelheim/ · "Ayurveda-Massage" → /ayurveda-therapie/ · "Ayurveda-Beratung" → /ayurveda-beratung/ |
| /ayurveda-kochworkshops-2026-…/ | 338 | 1 | "Ayurveda-Beratung" → /ayurveda-beratung/ · "Ayurveda in Ingelheim" → /ayurveda-ingelheim/ |
| /soulistic-reset-free5tage/ | 364 | 1 | "Nervensystem beruhigen" → /nervensystem-vagus-beruhigen/ · "SURIYA Neuro Self-Care" → /suriya-neuro-self-care/ |

Regel für neue Artikel: jeder Artikel bekommt 2–3 Links auf Leistungsseiten, im ersten Drittel des Textes und am Ende als CTA.

## B. Stadt-Cluster Mainz und Wiesbaden

Alle 8 Stadtseiten haben 1 echten Inbound-Link. Sie liegen nur im Footer ("Einzugsgebiete").

| Seite | Wörter | echte Inbound | von |
|---|---|---|---|
| /heilpraktiker-mainz/ | 2777 | 1 | /heilpraktikerin-ingelheim/ |
| /heilpraktiker-wiesbaden/ | 2947 | 1 | /heilpraktikerin-ingelheim/ |
| /schmerztherapie-mainz/ | 1987 | 1 | /ganzheitliche-schmerztherapie/ |
| /schmerztherapie-wiesbaden/ | 2148 | 1 | /ganzheitliche-schmerztherapie/ |
| /massage-mainz/ | 1762 | 1 | /massage-ingelheim/ |
| /massage-wiesbaden/ | 1784 | 1 | /massage-ingelheim/ |
| /massage-mainz/ayurveda/ | 623 | 1 | /massage-mainz/ |
| /massage-wiesbaden/ayurveda/ | 1154 | 1 | /massage-wiesbaden/ |
| /schmerztherapie-mainz/akupunktur/ | 1264 | 1 | /schmerztherapie-mainz/ |

Empfehlung: ein Block "Für Patientinnen aus Mainz" bzw. "… aus Wiesbaden" am Ende jeder Stadtseite mit Links auf die anderen Seiten der gleichen Stadt.

**Cluster Mainz (jede Seite verlinkt die anderen 4):**
- /heilpraktiker-mainz/ → "Schmerztherapie für Mainz", "Massage für Mainz", "Ayurveda-Massage für Mainz", "Akupunktur für Mainz"
- /schmerztherapie-mainz/ → "Heilpraktikerin für Mainz", "Massage für Mainz", "Akupunktur für Mainz" (vorhanden)
- /massage-mainz/ → "Heilpraktikerin für Mainz", "Schmerztherapie für Mainz", "Ayurveda-Massage für Mainz" (vorhanden)
- /massage-mainz/ayurveda/ → "Massage in Mainz" (zurück), "Heilpraktikerin für Mainz", "Ayurveda in Ingelheim" → /ayurveda-ingelheim/
- /schmerztherapie-mainz/akupunktur/ → "Schmerztherapie für Mainz" (zurück), "Akupunktur in Ingelheim" → /akupunktur-ingelheim-praxis/, "Heilpraktikerin für Mainz"

**Cluster Wiesbaden (gleiches Muster):**
- /heilpraktiker-wiesbaden/ → "Schmerztherapie für Wiesbaden", "Massage für Wiesbaden", "Ayurveda-Massage für Wiesbaden"
- /schmerztherapie-wiesbaden/ → "Heilpraktikerin für Wiesbaden", "Massage für Wiesbaden"
- /massage-wiesbaden/ → "Heilpraktikerin für Wiesbaden", "Schmerztherapie für Wiesbaden"
- /massage-wiesbaden/ayurveda/ → "Massage in Wiesbaden" (zurück), "Heilpraktikerin für Wiesbaden", "Ayurveda in Ingelheim"

Lücke: Es gibt /schmerztherapie-mainz/akupunktur/, aber keine Akupunktur-Seite für Wiesbaden. Optional später.

Zusätzlich: /heilpraktikerin-ingelheim/ (Über mich) verlinkt bereits beide Heilpraktiker-Stadtseiten. Die Startseite verlinkt keine Stadtseite im Content. Ein Satz im Lokal-Band der Startseite ("Patientinnen aus Mainz, Wiesbaden und Bingen") mit 2 Links wäre sinnvoll.

## C. Money-Pages für die Ads-Ziele (Massage, Ayurveda, Migräne)

| Seite | Im Menü | Wörter | echte Inbound | Befund |
|---|---|---|---|---|
| /massage-ingelheim/ | **nein** | 1421 | 9 | Hub für alle Massagen, fehlt im Menü |
| /ayurveda-therapie/ (WP 1511) | ja | 988 | 5 | H1 leer, 3 Out-Links; Seite bleibt unangetastet |
| /ayurveda-ingelheim/ | ja | 1279 | 13 | gut |
| /nervenregulationsmassage/ | nein | 1226 | 5 | wenig Inbound |
| /ayurveda-regenerationstherapie-ingelheim/ | ja | 2084 | 3 | wenig Inbound |
| /ayurveda-beratung/ | ja | 1626 | 1 | nur von Ayurveda-Hub |
| /ayurveda-darm-test/ | ja | 373 | 1 | nur von Ayurveda-Hub |
| /suriya-neuro-migraene/ | ja | 2152 | 11 | gut |
| /suriya-cranio-neuro-analyse/ | nein | 2126 | 7 | ok |
| /migraene-analyse-ingelheim/ | nein | 2364 | 3 | Zusammenlegung geplant (Umbau-Plan 06.10.) |
| /suriya-migraene-kompass/ | nein | 1125 | 3 | wenig Inbound |
| /suriya-neuro-self-care/ | nein | 1517 | 3 | wenig Inbound |
| /akupunktur-ingelheim-praxis/ | nein | 2042 | 13 | gut, aber nicht im Menü |
| /ohrakupunktur-ingelheim/ | nein | 1398 | 8 | ok |
| /schroepftherapie-ingelheim/ | nein | 934 | 9 | ok |
| /lymphdrainage-lipoedem-ingelheim/ | nein | 1802 | 4 | wenig Inbound |
| /craniosacrale-therapie/ | nein | 1906 | 5 | wenig Inbound |
| /hnc-human-neuro-cybrainetics/ | nein | 2386 | 3 | wenig Inbound |
| /thetahealing/ | nein | 1736 | 3 | wenig Inbound |
| /mikronaehrstoffe-hormone-wechseljahre/ | nein | 1955 | 7 | ok |

**Konkrete neue Links (Quelle → Ziel, Anker):**

Ziel /massage-ingelheim/:
- /ayurveda-ingelheim/ → "alle Massagen in Ingelheim mit Preisen"
- /ayurveda-regenerationstherapie-ingelheim/ → "Massage in Ingelheim"
- /nervensystem-vagus-beruhigen/ → "Nervenregulationsmassage und weitere Massagen"
- /heilpraktiker-mainz/ und /heilpraktiker-wiesbaden/ → "Massage in Ingelheim"
- / (Startseite) → vorhanden, gut

Ziel /ayurveda-therapie/ (WP 1511, Ayurveda-Massage):
- /ayurveda-regenerationstherapie-ingelheim/ → "Ayurveda-Massage in Ingelheim"
- /ayurveda-ausleitung-7-tage/ → "Ayurveda-Massage"
- /ayurveda-beratung/ → "Ayurveda-Massage in der Praxis"
- /suriya-neuro-migraene/ → "Ayurveda-Massage bei Migräne" (laut Umbau-Plan Karte "So kannst du starten")
- /massage-wiesbaden/ → "Ayurveda-Massage in Ingelheim" (Mainz hat den Link schon, Wiesbaden nicht)
- /heilpraktikerin-ingelheim/ → "Ayurveda-Massage"

Ziel /ayurveda-beratung/ und /ayurveda-darm-test/:
- /ayurveda-ausleitung-7-tage/ → "Ayurveda-Beratung" und "Ayurveda Darm-Check"
- /ayurveda-regenerationstherapie-ingelheim/ → "Ayurveda-Beratung"
- /mikronaehrstoffe-hormone-wechseljahre/ → "Ayurveda Darm-Check"
- /ayurveda-therapie/ (1511) → nicht ändern

Ziel /nervenregulationsmassage/:
- /suriya-neuro-migraene/ → "Nervenregulationsmassage"
- /nacken-schulter/ → "Nervenregulationsmassage"
- /craniosacrale-therapie/ → "Nervenregulationsmassage"

Ziel Migräne-Cluster:
- /nervensystem-vagus-beruhigen/ → "Migränebehandlung in Ingelheim" → /suriya-neuro-migraene/ (fehlt!)
- /craniosacrale-therapie/ → "Migränebehandlung" → /suriya-neuro-migraene/
- /ohrakupunktur-ingelheim/ → "Migräne" → /suriya-neuro-migraene/
- /kiefer-cmd/ → "Migräne und Kiefer" → /suriya-neuro-migraene/
- /ayurveda-bei-migraene-…/ (WP 3622, 806 Wörter, 3 Out-Links) → "Migränebehandlung" → /suriya-neuro-migraene/, "Ayurveda-Massage" → /ayurveda-therapie/, "Ayurveda in Ingelheim" → /ayurveda-ingelheim/

Ziel /ayurveda-regenerationstherapie-ingelheim/:
- /ayurveda-ingelheim/ → "Regenerationstherapie" (fehlt im Hub!)
- /nervensystem-vagus-beruhigen/ → "Ayurveda Regenerationstherapie"
- /ayurveda-therapie/ (1511) → nicht ändern

**Menü-Lücken (Dinakar, separates Go):** /massage-ingelheim/, /akupunktur-ingelheim-praxis/, /ohrakupunktur-ingelheim/, /schroepftherapie-ingelheim/, /lymphdrainage-lipoedem-ingelheim/, /nervenregulationsmassage/, /craniosacrale-therapie/, /suriya-cranio-neuro-analyse/, /mikronaehrstoffe-hormone-wechseljahre/ fehlen im Hauptmenü. Dafür steht /behandlungsangebot/ (176 Wörter) und /feelgoodhealingkitchenoktober/ (Workshop Herbst, Alt-Beitrag) im Menü.

## D. Enfold-Sidebar auf 16 Alt-Seiten

Betroffen (Enfold-Layout mit rechter Sidebar): /feelgoodhealingkitchenoktober/, /innere-arbeit-theta-healing-meditation/, /allergiebehandlung/, /darmgesundheit-2/, /hormongesundheit/, /ayurveda-workshop-januar/, /die-heilkraft-von-reinigenden-ritualen/, /1742-2/, /1524/, /back-to-the-roots-…/, /1428/, /ayurveda-ganzkoerpermassage/, /suriya-praxis-fuer-naturheilkunde-ingelheim/, /praxis-suriya-ingelheim-nervenregulation-…/, /5-ayurveda-rituale-…/, /migraene-und-nackenverspannungen-…/.

Widgets in der Sidebar: "Seiten" (58 Links), "Kategorien" (13), "Archiv" (14 Datums-Archive), "Einzugsgebiete" (8).

Problem:
- Jede dieser Seiten gibt 77–81 Links ab. Jeder Link trägt fast nichts.
- Das Widget "Seiten" verlinkt /404-error-page/, /login/, /happy-health/, /wpms-html-sitemap/, /shop/ (82 Wörter), /termin-vereinbaren-direkt/ (86 Wörter), /contact-2/, /meinayurvedaangebot/ (136 Wörter), /link-instagram/. Diese Seiten stehen nicht in der Sitemap, antworten aber mit 200.
- Das Widget "Archiv" erzeugt 14 Datums-Archive, die sonst niemand verlinkt.

Empfehlung (WP → Design → Widgets, Enfold-Sidebar):
1. Widget "Seiten" entfernen.
2. Widget "Archiv" entfernen.
3. Widget "Kategorien" behalten oder durch "Neueste Beiträge" ersetzen.
4. Widget "Einzugsgebiete" behalten (8 Stadt-Links, passt).
Das ist eine Einstellung, keine Seitenänderung. Braucht trotzdem Go.

## E. Doppelte und dünne Seiten im Linkgraph

| Seite | Wörter | Problem | Vorschlag |
|---|---|---|---|
| /praxis-fuer-naturheilkunde-ingelheim/ | 2146 | 1:1-Kopie der Startseite, canonical zeigt auf / | 301 → / |
| /darmgesundheit/ | 247 | gleicher Title wie /darmgesundheit-2/ (1407 Wörter) | 301 → /darmgesundheit-2/ |
| /behandlungsangebot/ | 176 | im Menü, 7× "Mehr erfahren", 0 Inbound | Inhalt von /behandlungsangebot-2/ übernehmen oder /behandlungsangebot-2/ 301 → /behandlungsangebot/ |
| /behandlungsangebot-2/ | 672 | 26 Links, 0 Inbound, 6× "weiter" | siehe oben |
| /contact-2/ | 105 | Kontakt-Duplikat zu /termin-buchen/ | 301 → /termin-buchen/ |
| /termin-vereinbaren-direkt/ | 86 | Termin-Duplikat | 301 → /termin-buchen/ |
| /massage-buchen/ | 423 | 4. Terminseite, nur von 1511 verlinkt | behalten (1511 verlinkt sie), aber nicht weiter stärken |
| /meinayurvedaangebot/ | 136 | Alt-Übersicht, Anker "hier" ×2 | 301 → /ayurveda-ingelheim/ |
| /suriya-praxis-fuer-naturheilkunde-ingelheim/ | 379 | Alt-Startseite | 301 → / |
| /shop/ | 82 | leer | noindex oder 301 → / |
| /link-instagram/ | 172 | Linktree-Seite | noindex, aus Sidebar raus |
| /ayurveda-fortbildung/ | 480 | B2B (Hotels/Spas), 0 Inbound | behalten, ggf. von /heilpraktikerin-ingelheim/ verlinken |
| /kosten-abrechnung/ | 537 | im Menü, 0 Content-Inbound | von /termin-buchen/ und FAQ-Blöcken verlinken: "Kosten & Abrechnung" |

Kategorie-Archive: 13 Archive mit 97–396 Wörtern, alle index/follow. Die Kategorie "SEO" (Slug /category/ayurveda-heilkunde-ingelheim/) ist öffentlich sichtbar als "Archiv für die Kategorie: SEO". Empfehlung: Kategorie umbenennen (z. B. "Praxis-Wissen") und alle Kategorie-Archive in Yoast auf noindex.

## F. Kochworkshop-Beitrag als Link-Senke

/ayurveda-kochworkshops-2026-im-hoefchen-stadecken-elsheim/ (338 Wörter) bekommt 30 Content-Links von praktisch allen Leistungsseiten (Promo-Block). Er gibt 1 Link zurück (Datenschutz).

- Kurzfristig: im Beitrag 2 Links ergänzen: "Ayurveda-Beratung" → /ayurveda-beratung/, "Ayurveda in Ingelheim" → /ayurveda-ingelheim/.
- Nach den Workshops: Promo-Block von den Leistungsseiten entfernen. Sonst bleibt ein Event-Beitrag die am stärksten verlinkte Seite der Website.

## G. Generische Ankertexte

| Quelle | Anker | Anzahl | Ersatz |
|---|---|---|---|
| /behandlungsangebot-2/ | "weiter" | 6 | Name der Leistung, z. B. "Ganzheitliche Schmerztherapie" |
| /behandlungsangebot/ | "Mehr erfahren" | 7 | "Craniosacrale Therapie in Ingelheim", "Akupunktur in Ingelheim" usw. |
| /nervensystem-vagus-beruhigen/ | "Erfahre mehr" | 2 | "Nervenregulationsmassage", "hnc – Human Neuro Cybrainetics" |
| /suriya-neuro-migraene/ | "Erfahre mehr" | 1 | "SURIYA Cranio-Neuro-Analyse" |
| /meinayurvedaangebot/ | "hier" | 2 | entfällt bei 301 |

"Weiterlesen" in den Kategorie-Archiven ist Theme-Standard. Kein Handlungsbedarf.

## H. Hub-Seiten: fehlende Rücklinks

- /ayurveda-ingelheim/ (Hub) verlinkt nicht auf /ayurveda-regenerationstherapie-ingelheim/ und nicht auf /massage-ingelheim/. Beide ergänzen.
- /ganzheitliche-schmerztherapie/ (Hub) verlinkt nicht auf /nacken-schulter/ und /hexenschuss-ruecken/. Nur Frozen Shoulder und Kiefer sind verlinkt. Beide ergänzen.
- /nervensystem-vagus-beruhigen/ (Hub) verlinkt nicht auf /suriya-neuro-migraene/ und nicht auf /ayurveda-regenerationstherapie-ingelheim/. Beide ergänzen.
- /blog/ hat 1 Content-Inbound (Startseite). Jede Leistungsseite könnte am Ende 1–2 passende Artikel verlinken ("Zum Weiterlesen").

## Prioritäten

| Prio | Maßnahme | Aufwand | Go nötig |
|---|---|---|---|
| 1 | Blog-Artikel: je 2–3 Links auf Leistungsseiten (Abschnitt A) | 1 h | ja |
| 2 | Hub-Rücklinks ergänzen (Abschnitt H) | 30 min | ja |
| 3 | Links zu /massage-ingelheim/ und /ayurveda-therapie/ (Abschnitt C) | 1 h | ja |
| 4 | Stadt-Cluster-Blöcke Mainz/Wiesbaden (Abschnitt B) | 2 h | ja |
| 5 | Sidebar-Widgets "Seiten" + "Archiv" entfernen (Abschnitt D) | 10 min | ja |
| 6 | 301-Konsolidierung dünner Seiten (Abschnitt E) | 1 h | ja |
| 7 | Kategorie "SEO" umbenennen, Archive noindex | 15 min | ja |
| 8 | Menü: /massage-ingelheim/ + Akupunktur rein, /behandlungsangebot/ + Workshop raus | Dinakar | ja, separat |
| 9 | Kochworkshop-Promo nach Event entfernen | später | ja |
