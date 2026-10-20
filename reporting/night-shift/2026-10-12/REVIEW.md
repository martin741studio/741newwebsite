# Night Shift 2026-10-12 — 6 geplant · 5 pass · 1 needs_martin · 0 skipped

## Praxis Suriya

- [ ] freigeben  **GBP Öffnungszeiten** (FEEDBACK) — pass
      → feedback/praxis-suriya/61abce05-2b04-49b4-b4ab-420ab4374080.md
      Diff: Öffnungszeiten-Tabelle nach Kundenangabe (Di–Do 7:30–18:00, Fr 7:30–12:00, Mo nur
      Telefon 12:00–14:00); Termin-CTA von „Button" auf „Buchungsformular-Link" korrigiert;
      Barrierefreiheit differenziert (Eingang ja, Toilette nein). Sa/So-Zeiten offen
      (`[fehlt: vom Kunden zu bestätigen]`).
      Hinweis: dieser Thread lief schon in früheren Nächten (zuletzt 10-01, 10-06, 10-07, 10-09).
      `processed-feedback.json` ist noch leer — bitte nach Freigabe alle drei Feedback-IDs
      (5bea6cb2…, 61abce05…, 7fd15e89…) im Ledger eintragen.

- [ ] freigeben  **NAP / Domains** (FEEDBACK) — pass
      → feedback/praxis-suriya/d1c58471-eafc-4ef9-8418-1611a2345445.md
      Diff: Domain-Priorität vorgeschlagen — `ayurveda-ingelheim` zuerst (NAP-sicher), `ayurveda-mainz`
      nur als Einzugsgebiets-Inhalt (kein zweiter Standort), `Femalecare` erst nach Rückfrage zu
      Schreibweise/TLD/Status nutzen. Suchvolumen-Zahlen fehlen noch (kein DataForSEO-Tool in der
      Session).

- [ ] freigeben  **GBP Beschreibung** (FEEDBACK) — pass
      → feedback/praxis-suriya/21a25f8b-8ee2-4f8f-8378-36aac01e35c4.md
      Diff: Kundentext 1:1 als neues GBP-Beschreibungsfeld übernommen (669 Zeichen, unter dem
      750-Zeichen-Limit). HWG- und NAP-Check sauber. Keine Rückfrage an Coralie nötig.
      Hinweis: auch dieser Thread läuft seit 09-15 wiederholt auf, weil der Ledger-Eintrag fehlt.

## Rabenmütter Shop

- [ ] freigeben  **Verkaufskanäle — Etsy** (FEEDBACK) — pass
      → feedback/rabenmuetter/66478f5c-02a4-4076-b1c3-ad9d211e3533.md
      Diff: Etsy-Empfehlung aus dem Report entfernt (Kundin lehnt ab, Positionierung passt nicht).
      Stattdessen TikTok Shop (bestätigt) und Pinterest-Shop (`hoffe ich` → offen) als Kanäle
      geführt. Kleine, folgenlose Normalisierung der Zitat-Interpunktion vom Critic vermerkt
      (kein Rework nötig).

- [ ] freigeben  **Trauerkarten-Pillar — Handschrift-Service** (FEEDBACK) — pass
      → feedback/rabenmuetter/801d4d7d-1a22-4d45-a08e-e0b213dff2ec.md
      Diff: 4-Schritte-Umsetzungsmodell für den Handschrift-Zusatzservice plus Preisfrage erklärt.
      Vier Punkte offen (`[fehlt: vom Kunden zu bestätigen]`): wer schreibt, Zeichen-Obergrenze,
      Vorlaufzeit, Preisaufschlag. Beispiel-Produktzeile ausdrücklich „nicht final, ungeprüft"
      markiert — `deslop_de.py` lief in dieser Session nicht (Bash-Freigabe fehlte).

- [ ] **Shop-Navigation / Kategorien (nach Anlass & Motiv)** (AUDIT) — **needs_martin**
      → audits/rabenmuetter/shop-navigation-kategorien.md · Fails: alle 8 Rubrik-Dimensionen
      unbewertet (Seite nicht abrufbar)
      Grund: `WebFetch` auf `rabenmuetter-verlag.de` scheitert mit Tool-Fehler (`API Error: 404`,
      `model: claude-3-5-haiku-20241022`) bevor irgendein Seiteninhalt geladen wird; curl-Fallback
      durch die Session-Berechtigungsschicht blockiert; kein DataForSEO-Tool vorhanden. Identischer
      Blocker in beiden Versuchen dieser Nacht und insgesamt zehnte unabhängige Bestätigung seit
      09-16 (gleiches Problem traf auch das CREATE-Item „Trauerkarten-Kollektion-Hub" acht Nächte
      in Folge). Per SKILL.md §3 kein dritter Versuch — Executor hat nichts erfunden.
      Martin: [ ] Seitenzugriff für `rabenmuetter-verlag.de` klären (WebFetch/curl-Freigabe)
              [ ] DataForSEO-Zugriff für dieses Client-Projekt einrichten
              [ ] danach: Audit mit echter Seiten-/SERP-Evidenz neu aufsetzen

## Offene Prozess-Punkte (für Martin, nicht für die Executors)

1. **`processed-feedback.json` ist weiterhin leer (`[]`).** Alle drei Praxis-Suriya-Feedback-Items
   sind seit mehreren Nächten unverändert dupliziert, weil approved Items nie in den Ledger
   geschrieben werden. 8. Lauf in Folge, der das meldet (zuletzt 10-06, 10-07).
2. **`rabenmuetter-verlag.de` ist seit acht bis zehn Nächten nicht erreichbar** (WebFetch-404 +
   curl durch Session-Policy blockiert). Betrifft jetzt zwei Plan-Items (Trauerkarten-Kollektion-Hub
   und Shop-Navigation). Ohne Standortänderung (Fetch- oder DataForSEO-Zugriff) wird jede künftige
   Nacht zu diesem Client denselben `needs_martin` produzieren.
3. **`state.json.budget.invocations_used` zeigt 9**, obwohl Planner (1) + 5× FEEDBACK (Executor+
   Critic, je 2) + 1× AUDIT mit 2 Versuchen (4) + dieser Reviewer (1) mindestens 16 Invocations
   ergeben. Derselbe Undercount-Bug wie in den Läufen 09-28 und 10-01 (siehe LOG.md) — der Zähler
   im Runner-Skript ist weiterhin nicht verlässlich für die Budget-Kontrolle.

## Kein Sicherheitsbefund

Alle gelesenen Dateien (`state.json`, `plan.json`, Critic-JSONs, Feedback-/Audit-Markdown) sind
reine Geschäftsinhalte (Kundenkommentare, SEO-Empfehlungen, Status-Dokumentation). Keine Datei
enthält Code, Schadsoftware-Muster oder Anweisungen, die als Prompt-Injection gegen diesen oder
einen künftigen Lauf wirken könnten.
