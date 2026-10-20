# Content Spec — Trauerkarten-Kollektion (Hub) · Rabenmütter Shop

**Task:** `77261080-f295-4d5e-877f-07245cba28f7` · Woche 4 · „Trauerkarten-Kollektion (Hub) aufbauen + interne Verlinkung"
**Modus:** CREATE · **Versuch:** 2 von max. 2 · **Plan-Index:** 5

## Status: ENDGÜLTIG BLOCKIERT — `needs_martin: no_dataforseo_tool`

Diese Seite braucht laut `seo-page-optimizer` echte Keyword-, Wettbewerbs- und PAA-Daten
(DataForSEO). In dieser Session steht kein DataForSEO-Tool zur Verfügung (kein passendes
MCP-Tool im Werkzeug-Satz dieser Executor-Instanz). Laut Night-Shift-Skill (Abschnitt
„Executor", Zeile zu „no_dataforseo_tool") gilt in diesem Fall: **nicht raten, sondern
blockieren.** Diese Datei liefert daher nur das, was aus echten, bereits vorhandenen Quellen
(`context.json`, Roadmap-Tasks, Kundenfeedback) gesichert ist. Alle Keyword-/Wettbewerbs-/
PAA-Felder sind mit `[fehlt: …]` markiert statt geraten.

### Versuch 2 — was neu geprüft wurde (Critic-Fail-Liste zuerst gelesen)

Die Critic-Datei (`critic/rabenmuetter-shop/trauerkarten-kollektion-hub.json`, Versuch 1)
listet drei Fails: (1) `[fehlt:]`-Marker im JSON-LD-Feld, (2) kein JSON-LD vorhanden, (3) vier
Rubrik-Dimensionen (2 Themen-Tiefe, 3 GEO, 4 E-E-A-T, 7 Schema) unter 80. Alle drei Fails hängen
an denselben fehlenden Datenquellen. Für Versuch 2 wurde geprüft, ob mindestens die
Site-Struktur von rabenmuetter-verlag.de (echte Kategorienamen/URLs, Preise, ggf. vorhandene
FAQ) diesmal per Web-Fetch erreichbar ist, um wenigstens ein reales, nicht-erfundenes
`CollectionPage`-JSON-LD zu ermöglichen — auch ohne DataForSEO-Keyworddaten:

- **DataForSEO:** weiterhin kein passendes MCP-Tool im Werkzeug-Satz dieser Session. Unverändert
  zu Versuch 1.
- **Web-Fetch von `rabenmuetter-verlag.de`:** zweimal versucht. Erster Versuch lieferte einen
  Tool-internen Fehler der Session (API-Fehler beim Abruf-Modell, kein Seiteninhalt erhalten).
  Zweiter Versuch (leicht andere URL) wurde von der Session-Berechtigung blockiert, bevor
  überhaupt ein Abruf stattfand. In beiden Fällen: **kein einziges Zeichen echten Seiteninhalts
  erhalten.** Das bestätigt unabhängig, was die Critic-Datei in Versuch 1 bereits vorhergesagt
  hatte („ein zweiter Executor-Versuch wird sehr wahrscheinlich nicht bestehen, solange
  DataForSEO/Site-Fetch nicht erreichbar wird").
- **Konsequenz:** Kein einziges der drei Fails aus Versuch 1 lässt sich mit echten Daten
  schließen — JSON-LD würde weiterhin entweder leer bleiben oder erfundene Kategorie-URLs/FAQ-
  Fragen enthalten. Beides verstößt gegen die Regel „real data only". Es wurde **nichts
  erfunden**, um die Rubrik-Werte künstlich anzuheben.
- Laut Night-Shift-Skill: „On fail → the Executor re-runs once with the fail list. Second fail →
  page marked needs_martin … Never a third attempt." Dieser Versuch 2 ist damit der letzte
  automatische Versuch für diese Seite. Sie bleibt `needs_martin` bis ein Mensch die
  Datenlücke schließt.

**Empfehlung an Martin:** DataForSEO-Zugriff und Site-Fetch für diese Seite manuell nachholen
(siehe Datenpaket-Tabelle unten), dann Rest der Seite fertigstellen. Titel/Meta/H1-Entwurf und
Seitenstruktur unten sind bereits nutzbar als Ausgangspunkt — sie haben sich zwischen Versuch 1
und 2 inhaltlich nicht geändert, da keine neuen echten Daten verfügbar wurden.

---

## Datenpaket (Executor-Check vor dem Schreiben)

| Feld | Quelle | Status |
|---|---|---|
| Primary keyword | Plan-Item (Planner) | „Trauerkarten" — laut Planner-Notiz „ein Themen-Label, keine verifizierte DataForSEO-Metrik" |
| Primary-Volumen + Difficulty | DataForSEO `keyword_suggestions/live` / `ranked_keywords/live` | **[fehlt: DataForSEO-Tool in dieser Session nicht erreichbar]** |
| Sekundär-/Cluster-Keywords + Volumen | DataForSEO `keyword_suggestions/live` | **[fehlt: DataForSEO-Tool nicht erreichbar]** — siehe aber „Bereits bekannte Cluster-Zahlen" unten, diese stammen aus der bestehenden Roadmap, nicht aus einem neuen Pull |
| Was die Domain schon rankt | DataForSEO `ranked_keywords/live` | **[fehlt: DataForSEO-Tool nicht erreichbar]** |
| Top-3–5-SERP-Wettbewerber + Subthemen | DataForSEO SERP + Seiten-Fetch | **[fehlt: DataForSEO-Tool nicht erreichbar; Web-Fetch-Tool in dieser Session ebenfalls fehlerhaft (API-Fehler beim Aufruf von rabenmuetter-verlag.de)]** |
| People-Also-Ask / echte Fragen | DataForSEO SERP `people_also_ask` | **[fehlt: DataForSEO-Tool nicht erreichbar]** |
| Kunden-Leistungen / echte Fakten | `context.json.feedback_open` (Kundenkommentare) | vorhanden, siehe unten |
| Kanonische NAP | `context.json.nap_locked` | **nicht zutreffend** — kein `nap_locked`-Eintrag für `client_id fbcc70d1-4c56-437c-b5fb-8056e48d3f62` (Online-Shop, kein stationärer Standort im Datensatz) |
| Ansprechperson / E-E-A-T | Brief / Impressum | **[fehlt: nicht in `context.json` vorhanden; Site-Fetch fehlgeschlagen]** |
| Stadt / Einzugsgebiet | GBP / Local Falcon | **nicht zutreffend** — bundesweiter Online-Shop, kein lokales Grid |
| Marktsprache | `context.json` / Planner | `de`, bestätigt |

### Bereits bekannte Cluster-Zahlen (aus der Roadmap, nicht neu verifiziert)

Diese Zahlen stehen bereits in den Task-Titeln der Kundenroadmap (`context.json.tasks`,
`client_id fbcc70d1-4c56-437c-b5fb-8056e48d3f62`). Sie wurden vermutlich in einer früheren
Session mit echten DataForSEO-Daten ermittelt, aber in dieser Executor-Session nicht erneut
geprüft. Sie gehören zum selben Themencluster wie der Hub, sind aber **keine Volumen-Angabe
für „Trauerkarten" selbst**:

- Ratgeber „Trauerkarte schreiben" — 90.500/Mo (Woche 5, Task `4fc4c019-…`)
- Ratgeber „Trauersprüche & Texte" — 49.500/Mo (Woche 6, Task `f2ef0f93-…`)
- (Anderes Cluster, nur zur Einordnung) Ratgeber „Glückwünsche zum Geburtstag" — 165.000/Mo (Woche 9, Task `1413b70d-…`)

### Kundenfakten aus echten Feedback-Kommentaren

- Feedback `66478f5c` (2026-08-30): Kundin hat sich **bewusst gegen Etsy** entschieden. Ihre
  eigene Begründung: Etsy wirkt bei Trauerkarten „gruselig, handgemacht, Künstler" — dazu passt
  ihr Shop nicht. Verkaufskanäle, die sie **bereits** hat: eigener Shop, Pinterest-Business-Konto
  mit Shop, TikTok-Shop. → Positionierung des Hubs sollte sich bewusst **von der Etsy-Handmade-
  Ästhetik abgrenzen** (professioneller „Verlag"-Anspruch, nicht Bastel-Look).
- Feedback `801d4d7d` (2026-08-30): Kundin **stimmt dem Pillar-Konzept „Trauerkarten" ausdrücklich
  zu** („super, super Vorschläge"). Offene Frage von ihr: wie eine „handschriftliche Karte"
  praktisch umgesetzt würde. Diese Frage ist mit Feedback-Item `801d4d7d` bereits in einem
  separaten FEEDBACK-Draft beantwortet (zwei Modelle vorgeschlagen: Handschrift-Schriftart vs.
  echte Handschrift), **aber Martin muss noch bestätigen, welches Modell ursprünglich gemeint
  war**, bevor der Hub das Feature fest verspricht. → **[fehlt: vom Kunden/von Martin zu
  bestätigen — Modell A oder B, bevor „handschriftliche Karte" als festes Merkmal auf dem Hub
  beworben wird]**. Bis zur Klärung: Hub erwähnt die Option vorsichtig, ohne ein Modell zu
  fixieren.
- Task `4577d1d6` (Woche 3, offen): Navigation soll „nach Anlass & Motiv" geordnet werden — das
  ist die vorgesehene Filterlogik für diesen Hub (z. B. Anlass: Beerdigung, Trauerfeier,
  Kondolenz; Motiv: floral, schlicht, religiös, modern). Konkrete finale Kategorienamen sind
  **[fehlt: Site-Struktur nicht abrufbar in dieser Session]**.
- Task `ce794633` (Woche 5, offen): „Intern zu allen Trauerkarten-Produkten verlinken" — bestätigt,
  dass der Hub die zentrale interne Verlinkungsseite für alle Trauerkarten-Produkte werden soll.

---

## Target

- **Primary keyword:** Trauerkarten (Volumen/Difficulty: [fehlt: DataForSEO-Tool nicht
  erreichbar])
- **Secondary/Cluster-Keywords:** Trauerkarten kaufen, Trauerkarten online bestellen,
  Beileidskarten, Kondolenzkarten — Liste ist eine plausible Themen-Ableitung aus dem
  Produktnamen, **keine verifizierten DataForSEO-Begriffe**: [fehlt: Volumen/Difficulty je
  Begriff]
- **Search intent:** transaktional / kommerziell (Nutzer will Trauerkarten kaufen), mit
  informationalem Einstieg über die Ratgeber-Seiten im Cluster (Trauerkarte schreiben,
  Trauersprüche & Texte)
- **URL slug (Vorschlag):** `/trauerkarten` — vorbehaltlich der bestehenden Shop-URL-Struktur
  (kein Site-Zugriff in dieser Session zur Prüfung bestehender URLs möglich)

## Meta

- **Title (Entwurf, ≤60 Zeichen):** „Trauerkarten online kaufen | Rabenmütter Verlag" (44
  Zeichen)
- **Meta description (Entwurf, ≤155 Zeichen):** „Trauerkarten für jeden Anlass — würdevoll
  gestaltet, einfach online bestellt. Jetzt die passende Karte bei Rabenmütter Verlag finden."
  (135 Zeichen)

Beide Felder sind mit dem bekannten Primary Keyword und dem bekannten Markennamen vollständig
geschrieben, ohne erfundene Zahlen oder Ansprüche.

## Page outline (H1 → H2/H3)

- **H1:** Trauerkarten — die passende Karte für jeden Anlass
- **H2 · Direkt-Antwort** (siehe GEO-Layer unten)
- **H2 · Kategorien nach Anlass** (Task `4577d1d6`: Beerdigung, Trauerfeier, Kondolenz —
  **[fehlt: finale Kategorienamen aus der Site-Struktur]**)
- **H2 · Kategorien nach Motiv** (floral, schlicht, religiös, modern —
  **[fehlt: finale Motiv-Namen aus der Site-Struktur]**)
- **H2 · Handschriftliche Karten** (vorsichtige Formulierung, kein festes Modell versprechen,
  solange `[fehlt: Modell A/B]` offen ist)
- **H2 · Häufige Fragen zu Trauerkarten** (FAQ-Block — Fragen **[fehlt: echte PAA-Daten nicht
  abrufbar]**, siehe GEO-Layer)
- **H2 · Weiterlesen** (interne Verlinkung zu den Ratgeber-Seiten im Cluster)

Die Subthemen der Top-Wettbewerber, die zusätzlich abgedeckt werden müssten, sind
**[fehlt: SERP-Daten nicht abrufbar]** — vor Fertigstellung nachholen, sonst ist die
Themen-Tiefe (Rubrik-Dimension 2) nicht geprüft.

## GEO / AI-answer layer

- **Direkt-Antwort-Block (Entwurf, 2–4 Sätze):** „Trauerkarten drücken Anteilnahme in Worten
  und Gestaltung aus. Bei Rabenmütter Verlag finden Sie Trauerkarten für Beerdigung, Trauerfeier
  und Kondolenz, sortiert nach Anlass und Motiv. Jede Karte lässt sich online bestellen und
  direkt verschicken." — Hinweis: dieser Text ist ein **erster Entwurf auf Basis bekannter
  Fakten**, kein Zitat aus echten Suchdaten.
- **Definitionsbox:** „Eine Trauerkarte ist eine Grußkarte, mit der Beileid zum Tod eines
  Menschen ausgedrückt wird." — Standarddefinition, keine Quelle nötig, sachlich korrekt.
- **FAQ:** **[fehlt: echte PAA-Fragen nicht abrufbar in dieser Session]**. Kein Platzhalter-FAQ
  eingesetzt, um keine erfundenen „echten Nutzerfragen" vorzutäuschen. Vor Fertigstellung:
  DataForSEO PAA oder Google-Autocomplete nachholen.
- **Extrahierbare Fakten:** Preis-Beispiele, Lieferzeit, Kartenformate — **[fehlt: keine Angaben
  in `context.json`, Site-Fetch fehlgeschlagen]**.
- **Zu nennende Entitäten:** „Trauerkarte", „Beileidskarte", „Kondolenzkarte", „Rabenmütter
  Verlag" — Städte/Region entfällt (bundesweiter Online-Shop, kein lokaler Fall).

## Body content

Noch nicht ausformuliert — hängt an den offenen Datenpunkten oben (Kategorienamen, Modell
handschriftliche Karte, Wettbewerber-Tiefe). Sobald diese vorliegen, hier:
- Abschnitt „Kategorien nach Anlass" mit echten Kategorienamen und je 2–3 Sätzen Einordnung
- Abschnitt „Handschriftliche Karten" erst nach Klärung Modell A/B
- E-E-A-T-Absatz: **[fehlt: keine Ansprechperson/Impressum-Daten in `context.json`]** — für
  einen Shop ohne Gesundheits-/YMYL-Bezug weniger kritisch als bei den Praxis-Clients, aber ein
  „Über uns"-Absatz mit echtem Namen stärkt Dimension 4 trotzdem.

## Structured data (JSON-LD)

**[fehlt: Kein JSON-LD-Entwurf in dieser Datei.]** Ein `CollectionPage` + `ItemList` mit
Kategorie-URLs und ein `FAQPage` mit echten Fragen wären hier passend (kein
`LocalBusiness`/`MedicalBusiness` — dieser Client hat keinen `nap_locked`-Eintrag und ist kein
lokaler Fall). Ohne echte Kategorie-URLs und echte FAQ-Fragen würde ein jetzt geschriebenes
JSON-LD entweder leer oder erfunden sein — beides gegen die Regel „real data only". Erst nach
Klärung der offenen Punkte oben nachreichen.

## Internal links

Real, aus der Roadmap bekannt (`context.json.tasks`, gleicher `client_id`):
- Hoch zu: (noch keine übergeordnete Pillar-Seite über dem Hub bekannt — **[fehlt: Seitenbaum-
  Hierarchie oberhalb „Trauerkarten" nicht in `context.json`]**)
- Quer zu (Sibling-Cluster-Seiten, sobald live):
  - Ratgeber „Trauerkarte schreiben" (Woche 5, Task `4fc4c019-…`)
  - Ratgeber „Trauersprüche & Texte" (Woche 6, Task `f2ef0f93-…`)
- Task `ce794633` (Woche 5) verlangt zusätzlich: von diesem Hub aus auf **alle** einzelnen
  Trauerkarten-Produktseiten verlinken, sobald deren URLs bekannt sind.

## Local signals

Nicht zutreffend. Bundesweiter Online-Shop, kein `nap_locked`-Eintrag, kein Local-Falcon-Grid
für diesen Client in `context.json`.

---

## Self-Check gegen `references/scoring-rubric.md`

| # | Dimension | Einschätzung |
|---|---|---|
| 1 | Search-intent match | Seitentyp (Kategorie-/Kollektionsseite) passt zur transaktionalen Absicht — ok, sobald Kategorien final sind |
| 2 | Topical depth | **nicht geprüft** — Wettbewerber-Subthemen fehlen |
| 3 | GEO-extractability | Direkt-Antwort + Definition vorhanden; FAQ fehlt komplett |
| 4 | E-E-A-T | schwach — keine Ansprechperson bekannt |
| 5 | Local signals | nicht zutreffend (kein lokaler Fall) |
| 6 | Technical on-page | Title/Meta/H1 vollständig und im Limit |
| 7 | Schema | **nicht vorhanden** — bewusst nicht erfunden |
| 8 | Internal links | Cluster-Links bekannt und benannt; Aufwärts-Link zur Pillar-Hierarchie fehlt |

Diese Seite würde in der jetzigen Form auf den Dimensionen 2, 3, 4 und 7 unter 80 punkten. Das
ist erwartet und richtig markiert, nicht schöngerechnet — sie ist als `needs_martin` vorgesehen,
nicht als fertiger Spec zur Freigabe.

## De-slop-Hinweis

Der einzige bereits ausformulierte Fließtext ist der Direkt-Antwort-Entwurf oben (3 Sätze).
Kurz, aktiv, ohne Blähwörter — kein `deslop.py`-Lauf nötig für diesen Umfang; bei der
Fertigstellung der vollen Body-Copy nachholen.

---

## Empfehlung / nächste Schritte für Martin

1. DataForSEO-Zugriff für dieses Item klären — in **beiden** automatischen Versuchen (Nacht vom
   2026-09-28) nicht erreichbar. Gleiche offene Frage wie im Skill unter „Unverified as of
   2026-09-15" vermerkt, jetzt zweimal bestätigt.
2. Site-Struktur von rabenmuetter-verlag.de einmal manuell prüfen — Web-Fetch lieferte in
   **beiden** Versuchen keinen Seiteninhalt (Versuch 1: API-Fehler; Versuch 2: Tool-Fehler bzw.
   Berechtigungs-Block) — für: finale Kategorienamen (Anlass/Motiv), bestehende URLs,
   Preisbeispiele.
3. Modell A/B für „handschriftliche Karte" bestätigen (hängt an Feedback-Item `801d4d7d`).
4. Danach: diesen Spec vervollständigen (Body-Copy, FAQ mit echten PAA-Fragen, JSON-LD).

## Ergebnis nach 2 Versuchen

Beide vom Night-Shift-Skill erlaubten automatischen Versuche sind abgeschlossen. Die Seite
bleibt `needs_martin` — kein dritter automatischer Versuch (Skill-Regel: „Never a third
attempt"). Kein Datenpunkt wurde in Versuch 2 erfunden, um die Blockade künstlich zu lösen.
