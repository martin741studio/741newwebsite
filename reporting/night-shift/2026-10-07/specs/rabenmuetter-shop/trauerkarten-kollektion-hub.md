# Content Spec — Trauerkarten-Kollektion (Hub) · Rabenmütter Shop

**Task:** `77261080-f295-4d5e-877f-07245cba28f7` · Woche 4 · „Trauerkarten-Kollektion (Hub) aufbauen + interne Verlinkung"
**Modus:** CREATE · **Versuch:** 2 von max. 2 (letzter Versuch) · **Plan-Index:** 5 · **Nacht:** 2026-10-07

## Status: BLOCKIERT — `needs_martin: no_dataforseo_tool` (Executor-Einschätzung; formale pass/retry-Entscheidung trifft der Critic)

**Versuch 2 — Ergebnis vorab:** Der Blocker aus Versuch 1 ist unverändert. Siehe Abschnitt
„Versuch 2" am Ende der Datei für den unabhängigen Re-Check. Da keine der vier unter 80
liegenden Rubrik-Dimensionen (2, 3, 4, 7) ohne echte Daten ehrlich auf ≥80 gehoben werden kann
— jede Behebung würde erfundene Kategorienamen, PAA-Fragen oder ein JSON-LD mit erfundenen
URLs bedeuten, was gegen die Regel „real data only" verstößt — bleibt diese Seite nach Versuch
2 auf `needs_martin`. Dies ist der letzte der max. 2 Versuche.

Diese Seite braucht laut `seo-page-optimizer` echte Keyword-, Wettbewerbs- und PAA-Daten
(DataForSEO). In dieser Session steht kein DataForSEO-Tool zur Verfügung (kein passendes
MCP-Tool im Werkzeug-Satz dieser Executor-Instanz). Zusätzlich geprüft: ein Live-Fetch von
`https://rabenmuetter-verlag.de`, um wenigstens die echte Seitenstruktur (Kategorienamen, Preise,
FAQ) ohne DataForSEO zu bekommen — der Aufruf scheiterte an einem Tool-internen API-Fehler dieser
Session (`API Error: 404, model: claude-3-5-haiku-20241022`), bevor überhaupt Seiteninhalt geladen
wurde. **Kein einziges Zeichen echten Seiteninhalts erhalten.**

Das deckt sich mit den Befunden aller bisherigen Nächte zu genau diesem Plan-Item (2026-09-16:
nicht ausgeführt; 2026-09-22: nicht ausgeführt; 2026-09-28: zwei Versuche, beide am selben
Blocker gescheitert, Ergebnis `needs_martin`; 2026-10-06: zwei Versuche, identisches Ergebnis).
Diese Session bestätigt den Befund ein weiteres (siebtes) Mal, unabhängig geprüft, nicht aus
früheren Läufen übernommen.

Laut Night-Shift-Skill (Abschnitt „Executor", Hinweis zu „no_dataforseo_tool") gilt: **nicht
raten, sondern blockieren.** Diese Datei liefert daher nur das, was aus echten, bereits
vorhandenen Quellen (`context.json`, Roadmap-Tasks, Kundenfeedback) gesichert ist. Alle
Keyword-/Wettbewerbs-/PAA-/Site-Struktur-Felder sind mit `[fehlt: …]` markiert statt geraten.

---

## Datenpaket (Executor-Check vor dem Schreiben)

| Feld | Quelle | Status |
|---|---|---|
| Primary keyword | Plan-Item (Planner) | „Trauerkarten" — laut Planner-Notiz ein Themen-Label, keine verifizierte DataForSEO-Metrik |
| Primary-Volumen + Difficulty | DataForSEO `keyword_suggestions/live` / `ranked_keywords/live` | **[fehlt: DataForSEO-Tool in dieser Session nicht erreichbar — geprüft, kein passendes MCP-Tool im Werkzeug-Satz]** |
| Sekundär-/Cluster-Keywords + Volumen | DataForSEO `keyword_suggestions/live` | **[fehlt: DataForSEO-Tool nicht erreichbar]** — siehe „Bereits bekannte Cluster-Zahlen" unten, aus der Roadmap, nicht neu verifiziert |
| Was die Domain schon rankt | DataForSEO `ranked_keywords/live` | **[fehlt: DataForSEO-Tool nicht erreichbar]** |
| Top-3–5-SERP-Wettbewerber + Subthemen | DataForSEO SERP + Seiten-Fetch | **[fehlt: DataForSEO-Tool nicht erreichbar; WebFetch auf `https://rabenmuetter-verlag.de` ebenfalls fehlgeschlagen — Tool-API-Fehler 404, kein Seiteninhalt erhalten]** |
| People-Also-Ask / echte Fragen | DataForSEO SERP `people_also_ask` | **[fehlt: DataForSEO-Tool nicht erreichbar]** |
| Kunden-Leistungen / echte Fakten | `context.json.feedback_open` (Kundenkommentare) | vorhanden, siehe unten |
| Kanonische NAP | `context.json.nap_locked` | **nicht zutreffend** — kein `nap_locked`-Eintrag für `client_id fbcc70d1-4c56-437c-b5fb-8056e48d3f62` (bundesweiter Online-Shop, kein stationärer Standort im Datensatz; geprüft gegen die drei vorhandenen `nap_locked`-Einträge, keiner passt zu dieser `client_id`) |
| Ansprechperson / E-E-A-T | Brief / Impressum | **[fehlt: nicht in `context.json`; Site-Fetch fehlgeschlagen]** |
| Stadt / Einzugsgebiet | GBP / Local Falcon | **nicht zutreffend** — bundesweiter Online-Shop, kein lokales Grid |
| Marktsprache | `context.json` / Planner | `de`, bestätigt |

### Bereits bekannte Cluster-Zahlen (aus der Roadmap, nicht neu verifiziert)

Stehen bereits in den Task-Titeln der Kundenroadmap (`context.json.tasks`,
`client_id fbcc70d1-4c56-437c-b5fb-8056e48d3f62`). Vermutlich aus einer früheren Session mit
echten DataForSEO-Daten ermittelt, in dieser Executor-Session nicht erneut geprüft. Gleiches
Themencluster wie der Hub, aber **keine Volumen-Angabe für „Trauerkarten" selbst**:

- Ratgeber „Trauerkarte schreiben" — 90.500/Mo (Woche 5, Task `4fc4c019-7e99-4ca5-a5b2-6ec233120705`)
- Ratgeber „Trauersprüche & Texte" — 49.500/Mo (Woche 6, Task `f2ef0f93-7eea-49e6-8eda-2ed5d454f604`)
- (anderes Cluster, nur zur Einordnung) Ratgeber „Glückwünsche zum Geburtstag" — 165.000/Mo (Woche 9, Task `1413b70d-8916-4c2d-b9a8-153505aff65e`)

### Kundenfakten aus echten Feedback-Kommentaren

- Feedback `66478f5c` (2026-08-30): Kundin hat sich **bewusst gegen Etsy** entschieden — eigene
  Begründung: Etsy wirkt bei Trauerkarten „gruselig, handgemacht, Künstler"; dazu passt ihr Shop
  nicht. Bereits vorhandene Kanäle: eigener Shop, Pinterest-Business-Konto mit Shop, TikTok-Shop.
  → Positionierung des Hubs sollte sich bewusst von der Etsy-Handmade-Ästhetik abgrenzen
  (professioneller „Verlag"-Anspruch, kein Bastel-Look).
- Feedback `801d4d7d` (2026-08-30): Kundin **stimmt dem Pillar-Konzept „Trauerkarten" ausdrücklich
  zu** („super, super Vorschläge"). Offene Frage: wie eine „handschriftliche Karte" praktisch
  umgesetzt würde. Diese Frage ist über Feedback-Item `801d4d7d` in einem separaten
  FEEDBACK-Draft (Plan-Index 4, diese Nacht) beantwortet — **Martin muss noch bestätigen, welches
  Modell gemeint war**, bevor der Hub das Feature fest verspricht.
  → **[fehlt: vom Kunden/von Martin zu bestätigen — konkretes Umsetzungsmodell]**. Bis zur
  Klärung: Hub erwähnt die Option vorsichtig, ohne ein Modell zu fixieren.
- Task `4577d1d6` (Woche 3, offen): Navigation soll „nach Anlass & Motiv" geordnet werden — die
  vorgesehene Filterlogik für diesen Hub (z. B. Anlass: Beerdigung, Trauerfeier, Kondolenz; Motiv:
  floral, schlicht, religiös, modern). Finale Kategorienamen sind **[fehlt: Site-Struktur nicht
  abrufbar in dieser Session]**.
- Task `ce794633` (Woche 5, offen): „Intern zu allen Trauerkarten-Produkten verlinken" — bestätigt,
  dass der Hub die zentrale interne Verlinkungsseite für alle Trauerkarten-Produkte werden soll.

---

## Target

- **Primary keyword:** Trauerkarten (Volumen/Difficulty: **[fehlt: DataForSEO-Tool nicht
  erreichbar]**)
- **Secondary/Cluster-Keywords:** Trauerkarten kaufen, Trauerkarten online bestellen,
  Beileidskarten, Kondolenzkarten — plausible Themen-Ableitung aus dem Produktnamen, **keine
  verifizierten DataForSEO-Begriffe**: [fehlt: Volumen/Difficulty je Begriff]
- **Search intent:** transaktional/kommerziell (Nutzer will Trauerkarten kaufen), mit
  informationalem Einstieg über die Ratgeber-Seiten im Cluster (Trauerkarte schreiben,
  Trauersprüche & Texte)
- **URL slug (Vorschlag):** `/trauerkarten` — vorbehaltlich der bestehenden Shop-URL-Struktur
  (kein Site-Zugriff in dieser Session zur Prüfung bestehender URLs möglich)

## Meta

- **Title (Entwurf, ≤60 Zeichen):** „Trauerkarten online kaufen | Rabenmütter Verlag" (44 Zeichen)
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
- **H2 · Kategorien nach Motiv** (floral, schlicht, religiös, modern — **[fehlt: finale
  Motiv-Namen aus der Site-Struktur]**)
- **H2 · Handschriftliche Karten** (vorsichtige Formulierung, kein festes Modell versprechen,
  solange **[fehlt: Umsetzungsmodell]** offen ist)
- **H2 · Häufige Fragen zu Trauerkarten** (FAQ-Block — Fragen **[fehlt: echte PAA-Daten nicht
  abrufbar]**, siehe GEO-Layer)
- **H2 · Weiterlesen** (interne Verlinkung zu den Ratgeber-Seiten im Cluster)

Die Subthemen der Top-Wettbewerber sind **[fehlt: SERP-Daten nicht abrufbar]** — vor
Fertigstellung nachholen, sonst ist die Themen-Tiefe (Rubrik-Dimension 2) nicht geprüft.

## GEO / AI-answer layer

- **Direkt-Antwort-Block (Entwurf, 2–4 Sätze):** „Trauerkarten drücken Anteilnahme in Worten und
  Gestaltung aus. Bei Rabenmütter Verlag finden Sie Trauerkarten für Beerdigung, Trauerfeier und
  Kondolenz, sortiert nach Anlass und Motiv. Jede Karte lässt sich online bestellen und direkt
  verschicken." — erster Entwurf auf Basis bekannter Fakten, kein Zitat aus echten Suchdaten.
- **Definitionsbox:** „Eine Trauerkarte ist eine Grußkarte, mit der Beileid zum Tod eines
  Menschen ausgedrückt wird." — Standarddefinition, sachlich korrekt, keine Quelle nötig.
- **FAQ:** **[fehlt: echte PAA-Fragen nicht abrufbar in dieser Session]**. Kein Platzhalter-FAQ
  eingesetzt, um keine erfundenen „echten Nutzerfragen" vorzutäuschen.
- **Extrahierbare Fakten:** Preis-Beispiele, Lieferzeit, Kartenformate — **[fehlt: keine Angaben
  in `context.json`, Site-Fetch fehlgeschlagen]**.
- **Zu nennende Entitäten:** „Trauerkarte", „Beileidskarte", „Kondolenzkarte", „Rabenmütter
  Verlag" — Städte/Region entfällt (bundesweiter Online-Shop, kein lokaler Fall).

## Body content

Noch nicht ausformuliert — hängt an den offenen Datenpunkten oben (Kategorienamen, Umsetzungsmodell
handschriftliche Karte, Wettbewerber-Tiefe). Sobald diese vorliegen:
- Abschnitt „Kategorien nach Anlass" mit echten Kategorienamen, je 2–3 Sätzen Einordnung
- Abschnitt „Handschriftliche Karten" erst nach Klärung des Umsetzungsmodells
- E-E-A-T-Absatz: **[fehlt: keine Ansprechperson/Impressum-Daten in `context.json`]** — für einen
  Shop ohne Gesundheits-/YMYL-Bezug weniger kritisch als bei den Praxis-Clients, aber ein
  „Über uns"-Absatz mit echtem Namen stärkt Dimension 4 trotzdem.

## Structured data (JSON-LD)

**[fehlt: kein JSON-LD-Entwurf in dieser Datei.]** Ein `CollectionPage` + `ItemList` mit
Kategorie-URLs und ein `FAQPage` mit echten Fragen wären passend (kein `LocalBusiness`/
`MedicalBusiness` — dieser Client hat keinen `nap_locked`-Eintrag und ist kein lokaler Fall). Ohne
echte Kategorie-URLs und echte FAQ-Fragen wäre ein jetzt geschriebenes JSON-LD leer oder erfunden
— beides gegen die Regel „real data only". Erst nach Klärung der offenen Punkte nachreichen.

## Internal links

Real, aus der Roadmap bekannt (`context.json.tasks`, gleiche `client_id`):
- Hoch zu: **[fehlt: Seitenbaum-Hierarchie oberhalb „Trauerkarten" nicht in `context.json`]**
- Quer zu (Sibling-Cluster-Seiten, sobald live):
  - Ratgeber „Trauerkarte schreiben" (Woche 5, Task `4fc4c019-7e99-4ca5-a5b2-6ec233120705`)
  - Ratgeber „Trauersprüche & Texte" (Woche 6, Task `f2ef0f93-7eea-49e6-8eda-2ed5d454f604`)
- Task `ce794633-7a58-4415-9236-e30c0783be11` (Woche 5) verlangt zusätzlich: von diesem Hub aus
  auf **alle** einzelnen Trauerkarten-Produktseiten verlinken, sobald deren URLs bekannt sind.

## Local signals

Nicht zutreffend. Bundesweiter Online-Shop, kein `nap_locked`-Eintrag, kein Local-Falcon-Grid für
diesen Client in `context.json`.

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

Dimensionen 2, 3, 4 und 7 liegen unter 80. Das ist erwartet und richtig markiert, nicht
schöngerechnet.

## De-slop-Hinweis

Der einzige ausformulierte Fließtext ist der Direkt-Antwort-Entwurf (3 Sätze). Kurz, aktiv, ohne
Blähwörter — kein `deslop.py`-Lauf nötig für diesen Umfang; bei Fertigstellung der vollen
Body-Copy nachholen.

---

## Versuch 1 — was geprüft wurde (2026-10-07)

- **DataForSEO:** kein passendes MCP-Tool im Werkzeug-Satz dieser Executor-Instanz (Tool-Liste
  dieser Session geprüft, keine `dataforseo_labs`-Werkzeuge vorhanden).
- **WebFetch** (`https://rabenmuetter-verlag.de`): der Aufruf scheiterte an einem Tool-internen
  Session-Fehler (`API Error: 404, model: claude-3-5-haiku-20241022`), bevor Seiteninhalt geladen
  wurde. Kein Seiteninhalt erhalten.
- Beide Blocker sind identisch mit den in den Nächten 2026-09-16, 2026-09-22, 2026-09-28 (zwei
  Versuche) und 2026-10-06 (zwei Versuche) dokumentierten Befunden für exakt dieses Plan-Item.
  Diese Session bestätigt den Befund unabhängig ein weiteres Mal (siebte Bestätigung insgesamt).

## Versuch 2 — Fail-Liste des Critics geprüft, Re-Check durchgeführt (2026-10-07, selbe Nacht)

Fail-Liste aus `critic/rabenmuetter-shop/trauerkarten-hub.json` (Versuch 1, Verdict: `retry`):

1. „JSON-LD field required by the hard check is entirely missing (only a `[fehlt:]` placeholder)
   — hard check 1 and hard check 3 (jsonld_valid) both fail on this."
2. „Rubric dimensions 2 (Topical depth), 3 (GEO-extractability/FAQ), 4 (E-E-A-T), and 7 (Schema)
   are all below the required 80, by the Executor's own self-check."

**Vor dem erneuten Schreiben: unabhängiger Re-Check der Blocker, nicht aus Versuch 1 übernommen.**

- **DataForSEO:** Werkzeug-Satz dieser (neuen) Executor-Instanz erneut geprüft — weiterhin kein
  `dataforseo_labs`-Tool vorhanden. Unverändert.
- **WebFetch** (`https://rabenmuetter-verlag.de`) — erneut versucht, mit einem gezielten Prompt
  nach genau den fehlenden Feldern (Kategorienamen, FAQ, Preise, Ansprechperson). Ergebnis:
  identischer Fehler, `API Error: 404 {"type":"error","error":{"type":"not_found_error",
  "message":"model: claude-3-5-haiku-20241022"}}`. Wieder kein einziges Zeichen echten
  Seiteninhalts erhalten. Das ist die achte unabhängige Bestätigung dieses exakten Blockers für
  dieses Plan-Item.

**Warum die Fail-Liste nicht durch Umschreiben behoben werden kann:**

Beide Fail-Punkte hängen direkt an fehlenden Primärdaten (Kategorie-URLs, echte PAA-Fragen,
Wettbewerber-Subthemen, Ansprechperson), nicht an der Formulierung der Seite:

- **Fail 1 (JSON-LD):** Ein `CollectionPage`/`ItemList`/`FAQPage`-Schema ohne echte Kategorie-URLs
  und echte FAQ-Fragen wäre entweder leer (fällt weiter unter den `[fehlt:]`-Hard-Check) oder mit
  erfundenen URLs/Fragen gefüllt (verstößt gegen „real data only", Regel 2 der SKILL.md, die über
  allem steht). Keine der beiden Optionen ist zulässig.
- **Fail 2 (Rubrik-Dimensionen 2/3/4/7):** Dimension 2 (Themen-Tiefe) braucht die Wettbewerber-
  Subthemen aus der SERP — nicht verfügbar. Dimension 3 (GEO/FAQ) braucht echte PAA-Fragen — nicht
  verfügbar. Dimension 4 (E-E-A-T) braucht eine echte Ansprechperson aus Impressum/Über-uns — nicht
  verfügbar (Site-Fetch schlägt fehl). Dimension 7 (Schema) hängt direkt an Fail 1.

Alle vier Lücken sind Dateneingaben, keine Schreibqualität. Diese Executor-Instanz hält sich an
die Regel „nicht raten, sondern blockieren" (SKILL.md, Abschnitt Executor) und erfindet daher
keine Kategorienamen, FAQ-Fragen oder ein Schema, nur um den Rubrik-Score künstlich über 80 zu
heben.

**Ergebnis Versuch 2:** Identischer Blocker, unabhängig zweimal in dieser Nacht bestätigt (vor
Versuch 1 und erneut vor Versuch 2). Dies war der letzte zulässige Versuch (max. 2). Der formale
`needs_martin`-Status wird vom Critic/Runner nach dessen zweitem Verdict gesetzt; aus Executor-
Sicht ist jedoch klar: ohne DataForSEO-Zugriff oder einen funktionierenden Site-Fetch für
`rabenmuetter-verlag.de` kann diese Seite nicht regelkonform fertiggestellt werden.

**Empfehlung an Martin:**
1. DataForSEO-Zugriff für dieses Item klären (über sieben frühere Versuche/Nächte plus diese
   Nacht durchgehend nicht erreichbar — acht Bestätigungen insgesamt).
2. Site-Struktur von rabenmuetter-verlag.de einmal manuell prüfen (WebFetch scheitert in jeder
   bisherigen Session, inkl. eines gezielten zweiten Versuchs in dieser Nacht) — für: finale
   Kategorienamen (Anlass/Motiv), bestehende URLs, Preisbeispiele, Ansprechperson/Impressum.
3. Umsetzungsmodell für „handschriftliche Karte" bestätigen (hängt an Feedback-Item `801d4d7d`,
   siehe `feedback/rabenmuetter-shop/801d4d7d-1a22-4d45-a08e-e0b213dff2ec.md` dieser Nacht).
4. Danach: diesen Spec vervollständigen (Body-Copy, FAQ mit echten PAA-Fragen, JSON-LD) — ein
   dritter automatischer Versuch ist laut Skill-Regel nicht vorgesehen; die Fertigstellung ist ab
   hier eine manuelle/Tages-Aufgabe, sobald die Datenzugänge stehen.

Titel/Meta/H1-Entwurf und Seitenstruktur oben sind bereits nutzbar als Ausgangspunkt. Kein
Datenpunkt wurde erfunden, um die Blockade künstlich zu lösen.
