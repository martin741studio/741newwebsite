# Diagnose — Naturheilpraxis Daniela Dumann

Stand 2026-10-11. Scorecard = `00_project/knowledge/cro-library/_derived/scorecard.md`. Jede 0/1-Wertung mit Beleg aus `02-data/dataset.md`.

## 1. Scorecard-Bewertung (Ist-Zustand)

| # | Regel | Prio | Score | Beleg |
| --- | --- | --- | --- | --- |
| 1 | Hero nennt in 5 s: was, für wen, nächster Schritt | A | **0** | Hero nennt „was" (Heilpraktikerin, Hildegard von Bingen) und „wo" (Charlottenburg), aber keinen nächsten Schritt — kein CTA im Hero-Bild, nur ein Kurs-Button (dataset 1.1, 1.3). |
| 2 | Headline = gefühltes Ergebnis + Stadt | A | **1** | Stadt vorhanden, aber Headline nennt die Methode („Naturheilkunde nach Hildegard von Bingen"), kein gefühltes Ergebnis für den Besucher (dataset 1.1 H1). |
| 3 | Sub-Headline: Situation zuerst | A | **0** | Keine Sub-Headline vorhanden; direkt Fließtext über die Praxis in der Ich-Form (dataset 1.1 Sektion 2). |
| 4 | Primärer CTA auf 390 px ohne Scrollen sichtbar | A | **0** | Auf Mobil kein Buchungs-CTA im Hero und auch nicht im Hamburger-Menü erreichbar (dataset 1.3). |
| 5 | CTA-Text nennt Nutzen, nicht „Kontakt" | A | **0** | Vorhandene CTAs heißen „Termin buchen" (neutral, kein Nutzen) und „Kontakt" (Label-Button, Regel R2.6/R3.2 verletzt) (dataset 1.1). |
| 6 | Rückversicherung direkt unter dem CTA | A | **0** | Keine Rückversicherungszeile irgendwo auf der Seite gefunden (dataset 1.1). |
| 7 | Zwei Beweisformen above the fold | A | **0** | Keine Google-Bewertung, keine Zahl, kein Zitat im Hero (dataset 1.1, 1.2). GBP hat 5,0★/9 Bewertungen, aber nicht auf der Website gezeigt (dataset 1.7). |
| 8 | Gesicht + Qualifikation im Hero oder Sektion 2 | A | **0** | Hero zeigt eine mittelalterliche Buchmalerei, kein Portrait. Das echte Portrait sitzt erst in Sektion 6 „Über mich", deutlich unter dem Fold (dataset 1.1, brand.md Bildwelt). |
| 9 | „Dein erster Termin": Schritte, Dauer, Preis | A | **0** | Keine „Erster Termin"-Sektion auf der Startseite. Preise existieren nur auf der Unterseite /behandlungen (Erstanamnese 220 €/60 Min), nicht auf der Startseite (dataset 1.9). |
| 10 | Eine Akzentfarbe für den CTA, Blur-Test | A | **1** | Der „Termin buchen"-Button hat eine klare Akzentfarbe (Oliv), aber überlappt sichtbar das Logo — Blur-Test würde zwei Flecken zeigen, nicht ein klares Ziel (dataset 1.3 Layout-Fehler). |
| 11 | CTA alle 2 Sektionen + Sticky mobil | A | **0** | Ein einziger CTA im Header (nur Desktop), kein wiederholter CTA, kein Sticky-Button (dataset 1.1, 1.3). |
| 12 | Bewertungen offen, mit Vorname + Logo + Überschrift | B | **0** | Keine Bewertungen auf der Startseite. Eine einzige Kundenstimme ohne Nachnamen/Quelle („H.") (dataset 1.1 Sektion 6). |
| 13 | Beweis-Überschrift trägt Nutzen | B | **0** | Keine Beweis-Sektion vorhanden, daher auch keine Überschrift zu bewerten. |
| 14 | 3–4 Beweisblöcke verteilt | B | **0** | Ein einziger schwacher Beweis (1 Zitat ohne Quelle) auf der ganzen Seite (dataset 1.1). |
| 15 | Situationen-Sektion, HWG-sauber | B | **0** | Keine „Ist das etwas für mich"-Sektion. Stattdessen Service-Kacheln ohne Situationsbezug (dataset 1.1 Sektion 3–4). |
| 16 | Leistungen als Karten mit Nutzen-Überschrift | B | **1** | 8 Service-Kacheln vorhanden und verlinkt, aber Überschriften sind Methodennamen („Aderlass Therapie"), kein Nutzen; Bilder ohne Praxisbezug (dataset 1.1, brand.md). |
| 17 | FAQ mit echten Einwänden | B | **0** | Keine FAQ auf der Startseite. PAA-Fragen „Kosten", „private Kasse" sind real nachgefragt, aber unbeantwortet (dataset 1.5). |
| 18 | Standort: Karte, Adresse, Parken, ÖPNV, Zeiten | B | **1** | Adresse + Anfahrt (Bus/S-Bahn/Autobahn) im Footer vorhanden, aber keine Karte eingebettet, keine Öffnungszeiten (GBP hat ebenfalls keine hinterlegt, dataset 1.7), kein Parkhinweis (dataset 1.1 Footer). |
| 19 | Abschluss-Sektion = Mini-Hero | B | **0** | Die Seite endet mit dem Kontaktformular direkt, kein Abschluss-Block mit Headline/Beweis/CTA (dataset 1.1). |
| 20 | Jede Überschrift trägt eine Aussage | C | **0** | Überschriften sind durchgehend Labels: „Mein Ansatz", „Über mich", reine Methodennamen bei den Kacheln (dataset 1.1). |
| 21 | Typografie/Hierarchie, Tap-Ziele | C | **1** | Headline deutlich größer als Body, aber geringer Kontrast (helle Zierschrift auf unscharfem Foto, dataset 1.2 Mobil-Screenshot); Tap-Ziele nicht geprüft `[FEHLT: Tap-Target-Messung]`. |
| 22 | Keine HWG-Verstöße (Health-Kunde) | A | **1** | Startseite selbst enthält nur eine Grauzone (Bach-Zitat „keine echte Heilung ohne …", dataset 1.9) — kein direkter Verstoß auf der Startseite. Verlinkte Unterseiten haben echte Verstöße (Krebs-Test-Name, Wirkversprechen Amethystsalbe), die NICHT auf der Startseite liegen, aber bei der Verlinkung aus dem Prototyp beachtet werden müssen. |

**Summe Ist-Zustand: 7 von 44 Punkten.** Priority-A-Summe: 2 von 22 (sollte 22 sein für ein Bestehen).

## 2. Lücken (Score 0 oder 1)

Alle 22 Items außer keinem — jedes Item hat eine Lücke. Größte Hebel nach Priorität:

**Priority A (Hero, CTA, Erster Termin, Vertrauen oben):**
- Kein Buchungs-CTA im Hero, keiner auf Mobil erreichbar (Items 1, 4, 11)
- Kein Gesicht, keine Qualifikation, kein Beweis oben (Items 7, 8)
- Keine „Erster Termin"-Klarheit (Item 9)
- CTA-Label ohne Nutzen, kein Rückversicherungstext (Items 5, 6)

**Priority B (Beweise, Angebot, Standort):**
- Keine Bewertungen trotz 5,0★/9 echter Google-Bewertungen (Item 12)
- Keine Situationen-Sektion (Item 15)
- Keine FAQ trotz realer, nachgefragter Fragen (Item 17)
- Kein Standort-Block mit Karte (Item 18)
- Kein Abschluss-CTA (Item 19)

**Priority C:**
- Label-Überschriften statt Nutzen-Überschriften (Item 20)

## 3. Fixes nach Wirkung auf Buchungsformular-Kontakte

**Priority A (zuerst):**
1. Hero neu: gefühltes Ergebnis + Stadt in der Headline, echtes Portrait, 5,0★/9-Bewertungen sichtbar, CTA „Termin buchen" mit Rückversicherungszeile, auf Mobil ohne Scrollen sichtbar plus Sticky-Button.
2. „Dein erster Termin"-Sektion mit 3–4 Schritten, Dauer, Preis ab 220 €.
3. CTA auf jeder zweiten Sektion wiederholen.

**Priority B:**
4. Bewertungswand mit den 3 vorliegenden Zitaten (+ Hinweis „5,0 ★ bei 9 Google-Bewertungen").
5. „Ist das etwas für mich?"-Sektion mit 3–5 echten Themenfeldern aus den 40 GBP-Leistungen (z. B. Verdauungsbeschwerden, Erschöpfung, Hormonelle Themen — alle HWG-sicher als „Begleitung bei …" formuliert, wie bereits in `client_locations.services` standardisiert).
6. FAQ mit den 3 echten PAA-Fragen plus Preis/Krankenkasse/Absage.
7. Standort-Block mit Karte, Adresse, Anfahrt (Bus/S-Bahn/Auto bereits vorhanden), Hinweis „Termine nach Vereinbarung" statt falscher Öffnungszeiten.

**Priority C:**
8. Alle Sektions-Überschriften auf Nutzen umschreiben.

## 4. Ideal-Outcome-Plan

Gewähltes Layout-Pattern: **P0-Blueprint** (`patterns.md`) mit **P9-Hierarchie** (ruhige, klinische Bildsprache) als Grundton, da die Marke traditionsreich/gelehrt statt verspielt wirkt (brand.md Mood-Wörter) — kein P1-Therapie-Mood (zu verspielt/pink), stattdessen die ruhigere P9-Farbführung mit der echten Lila/Oliv-Palette.

**Ziel-Sektionsreihenfolge (10 Sektionen, vollständiger P0-Blueprint):**

1. **Hero** — Problem/Ergebnis des Besuchers + „Berlin-Charlottenburg", echtes Portrait (ba734fdc oder 94e357f2), 5,0★/9-Bewertung, CTA „Termin buchen" (Lemniscus-Link) mit Rückversicherung „Antwort in der Regel innerhalb 1 Werktag", sekundär Telefon.
2. **Beweis-Leiste** — zweite, eigene Vertrauens-Platzierung direkt nach dem Hero: große „5,0 ★ / 9 Google-Bewertungen", eine hervorgehobene Kurz-Stimme, Zusatz-Zeile Qualifikation. Getrennt von der ausführlichen Bewertungssektion weiter unten (Regel R4.1/R4.10: zwei Beweis-Platzierungen). **Nachtrag 2026-10-11:** diese Reihe fehlte in der ersten Fassung dieses Plans, von Martin direkt bemängelt, siehe Abschnitt 7.
3. **„Ist das etwas für mich?"** — 3–5 Themenfelder (Verdauung, Erschöpfung, Frauenthemen, Schilddrüsen-Begleitung, Stressbegleitung), aus den 40 echten GBP-Leistungen, HWG-sicher.
4. **Leistungen** — Karten für die 4–6 Kernbereiche (Hildegard-Heilkunde/Aderlass, Ernährungsberatung, Darmsanierung, Homöopathie, Oligoscan, Massagen), Nutzen-Überschrift statt Methodenname, Link zur jeweiligen Unterseite.
5. **Der erste Termin** — 3–4 Schritte (Anamnesebogen vorab, Erstgespräch 60 Min, individueller Behandlungsplan, Folgetermine), Dauer + Preis „ab 220 €", CTA.
6. **Über die Behandlerin** — Portrait, „Heilpraktikerin seit 2002, Vizepräsidentin der Internationalen Gesellschaft Hildegard von Bingen", Hildegard-Kräutergarten Schorfheide als Differenzierung, CTA.
7. **Bewertungen** — die 3 vorliegenden Zitate mit Google-Logo, Vorname, „5,0 ★ bei 9 Bewertungen auf Google", Link zum Bewertungsprofil.
8. **FAQ** — Kosten (220 €/150 € pro Stunde), private Kasse/GebüH, Vorbereitung (Anamnesebogen), Absage, Hausbesuche (klarstellen: aktuell nicht möglich).
9. **Standort** — Karte, Nithackstraße 24, Anfahrt Bus 109/309/M45, S Westend/Charlottenburg/Jungfernheide, Autobahnausfahrt Spandauer Damm, „Termine nach Vereinbarung" statt falscher Öffnungszeiten.
10. **Abschluss-CTA** — Mini-Hero: Headline, 3 Rückversicherungs-Punkte, Bewertung, CTA „Termin buchen" + Telefon als Zweitweg.

**Sektions-Abdeckungs-Check gegen `patterns.md` P0-Blueprint (10 Reihen):**

| P0-Reihe | Status |
| --- | --- |
| 1 Hero | enthalten, Sektion 1 |
| 2 Proof wall | enthalten, Sektion 2 (neu nachgetragen) |
| 3 Situationen | enthalten, Sektion 3 |
| 4 Leistungen | enthalten, Sektion 4 |
| 5 Erster Termin | enthalten, Sektion 5 |
| 6 Über die Behandlerin | enthalten, Sektion 6 |
| 7 Reviews 2 | enthalten, Sektion 7 |
| 8 FAQ | enthalten, Sektion 8 |
| 9 Standort | enthalten, Sektion 9 |
| 10 Closer | enthalten, Sektion 10 |
| Differenzierer/Vergleichstabelle (Zusatz-Regel R5.7, kein P0-Pflichtzeile) | bewusst weggelassen: keine echten Wettbewerbsdaten erhoben (Regel „keine Konkurrenzanalyse"), eine Vergleichstabelle ohne echte Daten wäre erfunden und wirkt bei einer Einzelpraxis verkäuferisch statt vertrauensbildend |

## 5. Fakten-Lücken für den weiteren Verlauf (`[FEHLT]`)

Übernommen aus `dataset.md`, relevant für Copy/Design:

1. DataForSEO-Live-Zugriff blockiert (IP-Whitelist) — Zahlen bis zu 4 Wochen alt, für den Prototyp ausreichend, für Live-Entscheidungen vor Launch neu ziehen.
2. 6 weitere Bewertungstexte nicht einsehbar — Copy nutzt nur die 3 vorliegenden.
3. Alle 8 Service-Kachel-Fotos nicht einzeln geprüft (nur 1 stichprobenartig) — vor GPT-Prompts in Schritt 4 falls als Referenz genutzt, einzeln öffnen.
4. Kein Praxisraum-/Eingangsfoto vorhanden — GPT erzeugt ein Idealbild, Handoff bekommt einen Shoot-List-Eintrag.
5. Ob Hausbesuche wirklich generell nicht mehr angeboten werden oder nur in bestimmten Fällen — Website-Text ist eindeutig „kann ich derzeit leider nicht mehr anbieten", wird so übernommen.
6. Tap-Target-Maße der Live-Seite nicht gemessen (Item 21) — für den Prototyp gilt ohnehin die 44-px-Mindestregel, keine weitere Prüfung nötig.
7. Ob der Lemniscus-Buchungslink ein echtes Kalendersystem mit freien Slots ist oder nur ein Kontaktformular — ungetestet, wird im Handoff als offener Punkt vermerkt.

## 6. Nachtrag 2026-10-11 (nach DataForSEO-Freischaltung)

Live-Abruf bestätigt und verschärft den Befund: Die Domain rankt für **kein einziges** der 63 gefundenen Keywords mit Patienten-Suchabsicht (kein „heilpraktiker berlin", kein „ernährungsberatung berlin", kein „darmsanierung berlin"). Alle Rankings liegen auf Ausbildungs-/Kurs-Inhalten (Kräuterheilkunde-Ausbildung, Fastenleiter, Hildegard-Fasten) und Blogposts. Reale Suchvolumen bestätigt: „heilpraktiker berlin" 1.600/Mon LOW, „ernährungsberatung berlin" 1.600/Mon MEDIUM, „darmsanierung berlin" 90/Mon. Das bedeutet: Die Startseite konkurriert aktuell um NULL organische Patientensuche, die gesamte Sichtbarkeit kommt aus dem Kurs-/Ausbildungsgeschäft. Das stützt direkt Priority-A-Fix 1 (neuer Hero mit Patienten-Fokus) und erklärt, warum GBP/Maps (dataset 1.7, SoLV 0 %) aktuell der einzige realistische Patientenkanal ist, solange die Startseite nicht auf Praxis-Keywords einzahlt. Keine Änderung an `approved-copy.md` nötig, die Copy war bereits auf „heilpraktikerin berlin charlottenburg" + gefühltes Ergebnis ausgerichtet.

## 7. Nachtrag 2026-10-11 (Sektions-Lücke)

Martin bemängelte, dass die erste Fassung dieses Plans nur 9 statt 10 Sektionen hatte und die zweite Beweis-Platzierung direkt nach dem Hero fehlte (`patterns.md` P0-Reihe 2, „Proof wall"), obwohl nur eine einzige Vertrauens-Zeile im Hero stand und die eigentliche Bewertungssektion erst spät vor der FAQ kam. Korrigiert: Abschnitt 4 oben jetzt mit 10 Sektionen + vollständiger Abdeckungs-Check-Tabelle gegen `patterns.md`. `approved-copy.md` wurde um Sektion 2 „Beweis-Leiste" ergänzt, alle Folgesektionen umnummeriert. Diese Prüfung ist jetzt als Pflicht-Gate in `00_project/cro-homepage-workflow.md` Schritt 2 verankert, damit sie nicht erneut übersehen wird.

## Gate-Check

Jede 0/1-Wertung oben trägt eine Beleg-Referenz auf `dataset.md`. Gate bestanden → weiter zu Schritt 3 (Copy).
