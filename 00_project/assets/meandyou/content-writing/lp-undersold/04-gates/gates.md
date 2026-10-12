# Gate report 2026-10-12
Page: `page.md`. Result: **PASS**

| Gate | Result | Findings |
| --- | --- | --- |
| G1 facts | PASS | none |
| G2 legal | PASS | none |
| G3 seo | PASS | none |
| G4 style | PASS | none |
| G5 slop (lint) | PASS | none |
| G6 seo/geo coverage + schema | PASS | none |

## Warnings (angenommen, mit Grund)

- G1: Claim M08 (Methode, kein Schauspiel) nicht als eigener Claim verwendet; Inhalt steht über R04 und S07.
- G4: Sprecher „ich 7, wir 3“ stammen aus Zitaten, der FAQ-Frage „Ich habe wenig Zeit“ und der Copy-Deck-Zeile „Wir starten davor“. Seitenstimme bleibt dritte Person.
- G6: Direkt-Antwort zählt 5 Sätze, weil Fakten-Liste und Zitat im Block stehen. Der Absatz selbst hat 3 Sätze.
- G6 mit `--fetch`: Begriffs-Abdeckung 52 % (Hinweis). Ergänzt: Sofort-Feedback, Körpersprache. Nicht ergänzt: Inhouse, Coaching, München, Reisekosten (nicht im Angebot oder gestrichen, Auftrag).

## Slop-Schleife (G5)

Runde 1 (draft-v2 → cleansed): 4 Änderungen, 3 übernommen. Abgelehnt: Umbau der freigegebenen Zeile „Die Substanz stimmt. Der Auftritt bleibt darunter. Nach außen wirkt das Unternehmen kleiner, als es ist.“ (Copy Deck, Startseite).
Runde 2 (draft-v4 → cleansed): 2 Änderungen, 1 übernommen („Das Mikrofon“). Abgelehnt: Satzfragment im Michael-Absatz.
`diff_claims.py`: PASS in beiden Runden. `deslop_de.py`: 5/5 CLEAN.

## Frischer Reviewer (Subagent, 2026-10-12)

Score 78/100 auf draft-v3, 16 Lücken. Behoben in draft-v4: „an jedem Trainingstag“ gestrichen (kein Beleg); „Ein weiterer Tag gehört dem Get Together“ (freigegebener Wortlaut); Dauer als „drei Trainingstage plus ein Tag Get Together“ (Bundle hat zwei Tage); Einstieg „Wenn du noch kein Seminar … besucht hast“; Leistungen „Bei den dreitägigen Seminaren“; „Hotelfrühstück und Abendessen sind nicht enthalten“; Escher-Überschrift „40 Jahren Medienerfahrung“; H2 „Was Teilnehmer mitnehmen“; Zielgruppe mit Beraterinnen und Beratern, Vertrieb nur beim Bundle; „8.000“ ohne „seit 1990“; Beweiszeile „Rhetoriktrainer seit 1990“; „Rhetorik-Analysten“; Formate mit Rhetorik I, II, III; Auslassungszeichen. Nicht geändert: Titel Sarna Röser (Live-Seite, auf Geschwisterseiten freigegeben, Flag U12); CTA-Rhythmus (Persona-Regel K3).

## SEO-Audit (Subagent, seo-page-optimizer AUDIT, 2026-10-12)

Gesamt 77/100 auf draft-v3 (Intent 88, Tiefe 80, GEO 76, E-E-A-T 86, NAP 80, Technik 80, Schema 45, Links 82). Umgesetzt: Definitionssatz in S02; FAQ Führungskraft ohne „Ein Rezept gibt es nicht“; „Kommunikationstraining für Führungskräfte“ und „Executive Presence“ im Text; H3 „Drei Seminare zur Wahl“; Link `/rhetorik`; Schema mit drei `Course` und elf `CourseInstance`, Adresse, Breadcrumb mit drei Stufen, `Person` (ohne `instructor` bis Bestätigung). Nicht umgesetzt: Copy-Deck-Satz „Die meisten Rhetoriktrainings …“ bleibt wörtlich; H1-Aufteilung (gleiche Bauweise wie Seminare, Startseite); FAQPage (Brief `schema_faq: false`, Geschwister ebenso). Offen an Martin: Slug mit Keyword vor Indexierung, eine Telefonnummer (`nap.json`), `noindex` solange gelbe Marken offen.

## Link-Netz und Ähnlichkeit (G6c)

`link_network.py --final`: lp-undersold 6 ausgehende Links, 1 eingehender. FAIL für eingehende Links bei beiden Persona-LPs: Die Startseiten-Karte „Dein Unternehmen ist größer …“ muss auf `/lp-undersold` zeigen. Das macht die Hauptsitzung beim Einbinden (fremder Lauf, hier nicht geändert).
Ähnlichkeit (5-Wort-Shingles): Seminare 21,1 %, Startseite 14,0 %, lp-overlooked 7,0 %, Michael 6,6 %, FAQ 5,8 %, Stimmen 5,6 %, Rhetorik 3,5 %, Gespräch buchen 3,2 % (Grenze 25 %). Seminare hoch wegen gleicher Termin- und Formatfakten.

Wörter: 1.440 (Bestand v2 446 inkl. dreifachem Laufband, Benchmark-Median 1.194, Untergrenze 836, Ziel 900 bis 1.450).
