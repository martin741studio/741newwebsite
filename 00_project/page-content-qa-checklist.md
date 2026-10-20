# Master-Prompt: Content-Vollständigkeits-Gate + QA-Doppelcheck (741-intern)

**Zweck:** Kein Agent schreibt mehr Content, bevor die Datenbasis dafür vollständig und verifiziert vorliegt. Kein Agent markiert Content als fertig, ohne eine zweite, mechanische Prüfrunde. Beides ist hier ausgeschrieben — nicht als Prinzip, sondern als Schritt-für-Schritt-Verfahren mit exakten Methoden, Schwellenwerten und Abbruchbedingungen. Ziel: Martin muss nichts manuell nachprüfen, weil der Prozess selbst keine Lücke durchlässt.
**Entstanden aus:** Maria-Brasse-Vorfall 13.09.2026 — 8 von 9 Leistungsseiten gingen ohne echten Wettbewerber-Benchmark raus, weil fehlgeschlagene Datenabrufe stillschweigend übersprungen statt wiederholt wurden, und weil „Wortzahl fühlt sich richtig an" die programmatische Messung ersetzt hat.
**Gilt für:** jede Seite, jeder Kunde — Startseite, Leistungsseite, Spoke-Seite, Marken-/Mission-Seite, E-E-A-T-Seite, Kosten-/Conversion-Seite.

---

## PHASE 0 · PRE-FLIGHT-GATE — läuft VOR der ersten geschriebenen Zeile Content

Kein Wort Content wird geschrieben, bevor diese Phase mit ✅ abgeschlossen ist. Wenn ein Punkt nach den unten stehenden Retry-Regeln immer noch fehlt: **STOPPEN und Martin fragen** (Format siehe „Eskalation" unten) — niemals mit einer Lücke weiterschreiben und die Lücke stillschweigend durch eigene Einschätzung ersetzen.

### 0.1 · Seiten-Typ bestimmen (legt fest, welche Daten unten Pflicht sind)

| Typ | Beispiel | Bedeutet für Pre-Flight |
|---|---|---|
| **A · Money-/Leistungsseite** (echtes Such-Keyword mit Volumen ≥ 50/Mo) | Garten, Büro, Plancheck | Voller Datensatz unten Pflicht, inkl. Wettbewerber-Wortzahl-Benchmark |
| **B · Spoke-/Support-Seite** (Unterthema, kein eigenes Ziel-Keyword oder < 50/Mo) | Grundriss, Online-Beratung | Kein Wettbewerber-Benchmark nötig, aber Pillar-Verlinkung + Bestand-Check Pflicht |
| **C · Marken-/Mission-Seite** (kein Ranking-Ziel, dient Positionierung/E-E-A-T) | Über mich, Philosophie, Höfe (falls 0 Suchvolumen) | Kein Wettbewerber-Benchmark, aber Bestand-Vergleich Pflicht (nie dünner als Bestand) |
| **D · Kosten-/Conversion-Seite** (transaktional, kurz ist normal) | Kosten & Ablauf | Wettbewerber-Benchmark ja, aber kleiner Korridor erwartet (~400–700 W. typisch) |

### 0.2 · Pflicht-Datenpunkte je Typ — mit exakter Methode und Retry-Regel

**Für JEDEN Seiten-Typ (A–D) Pflicht:**

| # | Datenpunkt | Methode | Retry-Regel bei Fehlschlag |
|---|---|---|---|
| 1 | Source of Truth (Name, NAP, Kategorien, Leistungen, „mag/mag nicht") | gelocktes Stammdatenblatt des Kunden | Fehlt es komplett → Prompt `stammdatenblatt-rollout-prompt.md` zuerst, nicht diese Seite |
| 2 | Live-Bestandsseite (falls „Überarbeiten") | `curl`/Fetch der Live-URL, Text extrahieren, Wortzahl zählen (Methode 0.4) | Bei Fehlschlag (404/Timeout): 1× erneut versuchen, dann mit Wayback-Machine-Snapshot versuchen, sonst als „Bestand nicht abrufbar, Datum X" auf der Seite vermerken — NIE mit „vermutlich leer" weiterarbeiten |
| 3 | Google-Autocomplete-Themenbaum (min. 15 Varianten für Typ A/D) | `suggestqueries.google.com/complete/search?client=firefox&hl=de&gl=de&q=<seed>` mit 3–5 Seed-Varianten | Liefert ein Seed 0 Varianten → 2 weitere Seed-Formulierungen probieren, bevor „kein Autocomplete-Signal" akzeptiert wird |

**Zusätzlich für Typ A + D (Money-/Kosten-Seite):**

| # | Datenpunkt | Methode | Retry-Regel bei Fehlschlag |
|---|---|---|---|
| 4 | Ziel-Keyword + Suchvolumen | DataForSEO `keywords_data/google_ads/search_volume/live` | 40207 (IP-Whitelist) → Martin um Freischaltung bitten, NICHT per Browser/CAPTCHA umgehen (verboten). Sonst: Batch wiederholen, nie raten |
| 5 | SERP Top 10 fürs Ziel-Keyword | DataForSEO `serp/google/organic/live/advanced`, depth 15–20, 1 Task/Call | Leeres Ergebnis → Keyword-Schreibweise variieren (Singular/Plural, mit/ohne Ort), 1× erneut |
| 6 | **Echte PAA-Fragen (People-Also-Ask)** | aus demselben SERP-Call, `items type:people_also_ask` | 0 PAA → Keyword lockerer fassen (Oberbegriff statt Nische) und erneut, bevor „keine PAA" akzeptiert wird |
| 7 | **Wettbewerber-Wortzahl-Benchmark — MINDESTENS 2 erfolgreiche Messungen** | Aus SERP-Ergebnis die Top-6–10-URLs der Reihe nach fetchen (nicht nur die ersten 2!) und Wortzahl zählen (Methode 0.4) bis 2 Messungen erfolgreich sind | 403/404 auf eine URL → NICHT abbrechen, nächste URL aus derselben Liste probieren. Erst wenn ALLE 10 SERP-Treffer fehlschlagen, ist „kein Benchmark verfügbar, X/10 URLs geprüft, alle nicht erreichbar" eine ehrliche Meldung — dann Martin informieren, nicht schätzen |
| 8 | Lokalisierungs-Fakt, falls Stadt/Region Teil der Positionierung | Ein verifizierbarer, spezifischer lokaler Fakt (Kultur/Zahl/Institution) — per `WebSearch` mit Quelle, nicht aus Allgemeinwissen behauptet | Kein verifizierbarer Fakt gefunden → Stadt nur allgemein nennen, keinen erfundenen Fakt einsetzen |

**Zusätzlich für Typ C (Marken-/Mission-Seite):**

| # | Datenpunkt | Methode |
|---|---|---|
| 9 | Alle real vorhandenen Kunden-Texte zum Thema (auch von thematisch benachbarten Bestandsseiten) | Alle Live-Seiten des Kunden fetchen, die das Thema berühren — nicht nur die eine Zielseite |

### 0.3 · Gate-Entscheidung

Nach 0.1–0.2: Tabelle „Datenpunkt | Pflicht für Typ? | Vorhanden? | Quelle+Datum" für die konkrete Seite ausfüllen. **Nur wenn jede Pflichtzeile „Vorhanden: ja" mit echter Quelle zeigt, beginnt Phase 1 (Schreiben).** Fehlt etwas Behebbares (Retry nicht ausgeschöpft) → Retry-Regel anwenden. Fehlt etwas, das nur Martin/der Kunde liefern kann (Source of Truth, IP-Whitelist, Kunden-Fotos) → **Eskalation**, nicht weiterschreiben.

### 0.4 · Wortzahl-Messmethode (immer dieselbe, nie eyeballen)

Body-Text zwischen `class="pagetitle"` (bzw. der H1) und dem CTA-/Footer-Block extrahieren, HTML-Tags strippen, Wörter zählen — per Skript (`re.sub('<[^>]+>',' ',body).split()`-Muster), nicht durch Überfliegen oder Erinnerung an die eigene Schreibarbeit. Diese Methode für Bestand, eigenen Entwurf UND jede Wettbewerber-Seite identisch anwenden, sonst sind die Zahlen nicht vergleichbar.

### Eskalation — Format, wenn Phase 0 nicht durchläuft

Keine Seite mit Lücke ausliefern. Stattdessen kurz an Martin:
> „Kann [Seite] nicht vollständig vorbereiten — es fehlt: [Datenpunkt], weil [Grund, inkl. was probiert wurde]. Brauche von dir: [genau was]. Alles andere ist bereit, ich warte auf diesen einen Punkt."

---

## PHASE 1 · CONTENT-ERSTELLUNG — erst NACH bestandenem Gate

1. **Ziel-Wortzahl festlegen, bevor geschrieben wird**, nicht danach schätzen: Median der erfolgreich gemessenen Wettbewerber (Typ A/D) bzw. „mindestens X % über Bestand" (Typ B/C, wenn Bestand > 0) bzw. „deutlich über 0" (Typ B/C ohne Bestand).
2. **Bestandstexte/FAQ des Kunden 1:1 übernehmen und ausbauen**, nie ersetzen — sie sind bereits geprüfter, authentischer Content (siehe `startseite-money-page-standard.md` Schritt 2).
3. **Jede reale PAA-Frage, die zum Angebot passt, wird zur FAQ** — nicht nur 1 von 4, sondern geprüft, welche wirklich zum Kunden passen, mit kurzer Begründung, wenn eine PAA bewusst NICHT verwendet wird (z. B. weil sie am Angebot vorbeigeht).
4. **Lokalisierung ist echte Textur, kein Namedropping.** „Berlin" einmal in der Meta-Zeile erwähnen reicht nicht — der verifizierte lokale Fakt (0.2 Punkt 8) gehört in einen eigenen Absatz im Fließtext.
5. **Authentische Stimme:** wo immer die Kundin/der Kunde eigene Formulierungen, Methoden-Namen oder wiederkehrende Sätze hat (z. B. Marias „Fühlen, Erkennen, Loslegen", „Entweder wir finden einen Weg…"), diese aktiv in neue Seiten weben, auch wenn die Seite neu ist und nicht auf einer Bestandsseite basiert.
6. **Nach dem Schreiben sofort neu zählen** (Methode 0.4) — nicht am Ende der ganzen Session in einem Rutsch, sondern direkt nach jeder Seite, damit ein zu dünnes Ergebnis sofort auffällt und nachgebessert wird, statt am Schluss 9 Lücken auf einmal zu finden.
7. **Wortzahl-Urteil-Satz ist auf JEDER Seite Pflicht** — Tabelle (eigene Zahl · Bestand · Wettbewerber) + ein Satz „ausreichend/zu wenig" + Ziel-Korridor. Bei Typ B/C ohne Wettbewerber: ehrliches Urteil „kein Wettbewerbs-Keyword, Wortzahl ist hier nicht der Hauptfaktor" + trotzdem Bestand-Vergleich.
8. **Hard Stop:** liegt die neue Seite nach dem Zählen unter dem Bestand ODER unter 70 % des Wettbewerber-Medians (Typ A/D) → nicht ausliefern, sofort mit Schritt 1–7 nachbessern, bevor irgendetwas deployed wird.

---

## PHASE 2 · POST-HOC-QA-DOPPELCHECK — zweite, unabhängige Prüfrunde

Auch wenn Phase 0+1 sauber gelaufen sind: diese Runde fängt Fehler ab, die während des Schreibens entstehen (vergessene Links, kopierte Platzhalter, falsche Zahlen). Kann vom selben oder einem anderen Agenten laufen. Output ist ein Ampel-Report an Martin, **kein Kundendokument.**

### Block 1 · Vollständigkeit
1. Seitenbaum-HTML abrufen, alle `.node`-Elemente mit Tag `rev`/`new` auflisten.
2. Gegen die deployten `📄`-Text-Links abgleichen — 1:1, nicht ungefähr.
3. Fehlt ein Text → sofort nachschreiben (komplettes Phase-0+1-Verfahren durchlaufen, nicht abkürzen), deployen, verlinken.
4. `keep`/`idea`-Knoten bleiben unangetastet — das ist korrekt, nicht unvollständig.

### Block 2 · Content-Qualität — jede Zeile mit echtem Beleg, nicht Erinnerung
Für jede Seite, per Skript (Methode 0.4) frisch nachgezählt — NICHT die beim Schreiben behauptete Zahl übernehmen:

| Prüfpunkt | Ist | Beleg |
|---|---|---|
| Wortzahl (frisch gezählt) | Zahl | Skript-Output, nicht Erinnerung |
| ≥ Bestand? | ✓/✗ | Bestand-Zahl aus Phase 0.2 |
| ≥ 70 % Wettbewerber-Median (Typ A/D)? | ✓/✗ | Benchmark aus Phase 0.2 |
| H1-Anzahl | genau 1? | — |
| Wortzahl-Urteil-Satz vorhanden? | ✓/✗ | jede Seite, ausnahmslos |
| Lokaler Fakt echt/verifiziert (falls Typ A/D mit Ort-Bezug)? | ✓/✗ | Quelle nennen |
| Reale Kunden-Fakten übernommen, keine erfunden? | ✓/✗ | konkret markieren |
| Interne Links zu Pillar/Schwester-Seite tatsächlich im Fließtext (nicht nur im Technik-Block behauptet)? | ✓/✗ | `grep href` gegen den sichtbaren Body, nicht den ganzen HTML-Quelltext |
| Schema kein Duplikat zu Schwester-Seiten? | ✓/✗ | Namen vergleichen |
| Kannibalisierung mit anderer Seite? | ✓/✗ | gleiches Haupt-Keyword? |

**Jede ✗-Zeile wird direkt gefixt, nicht nur gemeldet — dann Block 2 erneut prüfen.**

### Block 3 · Design/CI-Konformität
Zwei Schichten trennen: Freigabe-Layer (Portal-Report, aktuell 741-CI — **Stand 13.09. widersprüchlich zum `behandler-seite`-Skill, der Kunden-CI vorschreibt; ungeklärt, Martins Entscheidung ausstehend, nicht eigenmächtig wechseln**) vs. Umsetzungs-Layer (echte Website, MUSS Kunden-CI).

CI-Steckbrief-Checkliste (falls noch nicht vorhanden, jetzt per `getComputedStyle` auf der Live-Seite erstellen, nie raten oder aus Content-Regex ableiten):
- [ ] Primär-/Akzentfarbe(n) — von echten Elementen (H2, CTA-Button), nicht Content-Bildern
- [ ] Font-Stack Headline + Fließtext
- [ ] Logo-Assets **dauerhaft im Repo gesichert** (nicht nur Scratchpad — das wird bei Session-Wechsel gelöscht)
- [ ] Header-Nav-Struktur + Footer-Inhalt dokumentiert (inkl. Prüfung: steht NAP im Footer? Falls nein → als Lücke gegen den Local-SEO-Standard vermerken)
- [ ] CMS/Builder bekannt
- [ ] Bild-/Foto-Bestand geprüft (wie viele Bilder hat die Live-Seite wirklich? Nicht raten)

### Block 4 · Verbleibende Voraussetzungen fürs Ergebnis
- Interne Verlinkung real im Text (siehe Block 2)
- Echte Bilder vom Kunden vorhanden oder Access-Grant offen?
- Tracking (GA4/GSC) startklar oder blockiert (z. B. Website-Login)?
- URL-Kollision neuer Slugs mit Bestand? (`curl -o /dev/null -w "%{http_code}"` auf jede neue URL — 404 = frei)
- Rollout-Reihenfolge sinnvoll nach Suchvolumen/Ranking-Stand/Programmphase?
- Post-Launch-Messplan (Baseline + Folge-Scan) pro Seite vorgesehen?

**Output an Martin:** 🟢/🟡/🔴 je Block, was direkt gefixt wurde, was seine Entscheidung braucht.

---

## Änderungsprotokoll (jede Lektion, die zu einer neuen Regel geführt hat)

- **13.09.2026, Maria Brasse:** 8/9 Seiten ohne Benchmark (Fetch-Fehler nicht retried) → Phase 0.2 Punkt 7 (Retry-Pflicht bis 2 Messungen oder alle 10 SERP-Treffer geprüft).
- **13.09.2026:** Wortzahl aus Erinnerung/Schätzung statt Skript-Zählung, Abweichungen bis 150 Wörter → Phase 0.4 (feste Messmethode) + Phase 1.6 (sofort nach jeder Seite zählen).
- **13.09.2026:** überarbeitete Seite landete unter dem Bestand (Philosophie 268 vs. 294 W.) trotz dokumentierter Suriya-Lektion → Phase 1.8 (Hard Stop, kein „weiter, wird schon passen").
- **13.09.2026:** Lokalisierung nur als Namedropping in der Meta-Zeile → Phase 0.2 Punkt 8 + Phase 1.4 (echter, verifizierter Fakt im Fließtext Pflicht).
- **13.09.2026:** Logo-Assets nur im Scratchpad, bei Session-Wechsel verloren → Block 3 Checkliste („dauerhaft im Repo").
- **13.09.2026:** Interne Links im Technik-Block versprochen, aber nie im sichtbaren Text gesetzt → Block 2 (`grep` gegen sichtbaren Body, nicht nur Technik-Block-Text glauben).
- **13.09.2026:** Dateien versehentlich in den Base-Repo-Checkout statt den aktiven Worktree geschrieben → **Regel für jede Session:** vor dem ersten Schreib-/Deploy-Befehl `pwd` prüfen; nie `cd` in einen absoluten Repo-Root-Pfad, der nicht der eigene Worktree ist.
