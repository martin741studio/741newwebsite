# Night Shift 2026-09-22 — 6 planned · 4 pass · 0 needs_martin · 0 skipped · 2 not executed

## Praxis Suriya

- [ ] freigeben  **GBP Öffnungszeiten & Termin-Button** (FEEDBACK) — pass
      → feedback/praxis-suriya/5bea6cb2-688d-4c24-b436-1a576e7ade75.md
      Alle Punkte des Kundenkommentars gedeckt. Wochenend-Öffnungszeiten offen: `[fehlt: vom Kunden zu bestätigen]`.
- [ ] freigeben  **GBP Barrierefreiheit** (FEEDBACK, Folge zu 5bea6cb2) — pass
      → feedback/praxis-suriya/61abce05-2b04-49b4-b4ab-420ab4374080.md
      Neuer Punkt aus Folge-Kommentar (28s später): Toilette nicht barrierefrei. GBP-Attribut-Empfehlung enthalten.
- [ ] freigeben  **NAP / Citations / Domains** (FEEDBACK) — pass
      → feedback/praxis-suriya/d1c58471-eafc-4ef9-8418-1611a2345445.md
      Interne Empfehlung zu Domain-Ideen (Ingelheim/Mainz) und bestehender Domain "Femalecare". Keine Kunden-Kopie.

## Rabenmütter Shop

- [ ] freigeben  **Zusätzliche Verkaufskanäle** (FEEDBACK) — pass
      → feedback/rabenmuetter-shop/66478f5c-02a4-4076-b1c3-ad9d211e3533.md
      Etsy gestrichen, Pinterest als unbestätigt markiert, TikTok Shop ergänzt. De-Slop-Check von Hand geprüft (Sandbox blockierte `deslop.py`) — sauber.
- **nicht ausgeführt** — **Trauerkarten-Pillar Antwort** (FEEDBACK, feedback_id `801d4d7d-1a22-4d45-a08e-e0b213dff2ec`)
      → kein Entwurf. Planner-Item 4, Executor nie gestartet. Kunde wartet seit 2026-08-30 auf Antwort zur Frage "handschriftliche Karte — wie umsetzen?".
- **nicht ausgeführt** — **Ratgeber: Trauerkarte schreiben** (CREATE, task_id `4fc4c019-7e99-4ca5-a5b2-6ec233120705`)
      → kein Entwurf. Planner-Item 5, Executor nie gestartet. Volumen-Hinweis aus Task-Titel: 90.500/Mo.

## Root-Cause-Befund: warum nur 4 von 6 Punkten liefen

`reporting/night-shift.sh` Zeile 113 zählt die geplanten Seiten so:
```
PAGES=$(python3 -c "import json;p=json.load(open('$OUT/plan.json'));print(len(p))")
```
`plan.json` ist ein Objekt mit 4 Top-Level-Schlüsseln (`date`, `clients_selected`, `plan`,
`skipped`), nicht die Plan-Liste selbst. `len(p)` zählt die Schlüssel des Objekts (4), nicht die
Einträge in `p["plan"]` (6). Das Log zeigt exakt diesen Fehler: **"planned pages: 4"**, obwohl der
Planner sichtbar 6 Punkte in `plan.json.plan` geschrieben hat. Der Runner brach die Schleife nach
Index 3 ab — nicht wegen des Budgets (nur 9 von 14 Invocations verbraucht, Fenster noch offen),
sondern wegen dieses Zählfehlers. Das ist eine Script-Änderung, keine Spec — der Reviewer nimmt
hier keine Korrektur vor, sondern meldet den Fund nur.
**Empfehlung:** `len(p["plan"])` statt `len(p)` in Zeile 113 von `night-shift.sh`.

## Wiederkehrender Befund: `processed-feedback.json` bleibt leer

`reporting/night-shift/processed-feedback.json` enthält weiterhin `[]`. Dieser Befund wurde
bereits in `LOG.md` für die Nächte vom 16.09. und 18.09. vermerkt und ist noch nicht behoben.
Folge: erledigtes Feedback wird nie aus `context.json.feedback_open` entfernt und erscheint
Nacht für Nacht erneut im Plan. Alle vier heute bearbeiteten Feedback-Punkte könnten bereits aus
einer früheren Nacht stammen — ohne den Ledger-Eintrag lässt sich das nicht ausschließen. Die
Entscheidung, wann ein `feedback_id` als „processed" gilt, liegt laut SKILL.md beim Tagesablauf
(nach Freigabe durch Martin), nicht beim Nachtlauf selbst — trotzdem lohnt sich eine Prüfung, ob
dieser Schritt im Tagesablauf tatsächlich implementiert ist.

## Zusammenfassung für Martin

- 4 Entwürfe bereit zur Freigabe, alle Critic-Checks grün, keine `needs_martin`.
- 2 Punkte aus dem Plan wurden diese Nacht nicht bearbeitet (Script-Zählfehler, siehe oben) —
  bleiben automatisch morgen früh in der Warteschlange, sofern das Feedback-Ledger-Problem sie
  nicht erneut verdeckt.
- Zwei technische Befunde oben sind Hinweise für eine Script-Korrektur, keine Content-Freigabe-Fragen.
