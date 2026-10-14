# Output template (always use this exact section order)

```markdown
# Call-Vorbereitung: <Name> (<Firma/Marke, wenn vorhanden>)

Termin: <Wochentag, Datum>, <Uhrzeit Prospect-Zone> (<Zone>), <Dauer>, <Call-Link>
Für Martin: <gleiche Zeit in Martins Zone>. Review-Seite: <review_url, falls vorhanden>

## Wer sie/er ist
<2-4 Sätze: Positionierung, Branche, Standort/Zielgruppe, Website, kurze Vorgeschichte
(wie der Kontakt entstand, was schon gezeigt wurde).>

## Ihr/Sein Ziel zuerst
Frage am Anfang des Calls: "<die Zielfrage, an das Geschäft angepasst>" Die Zahl notieren.
<1 Satz Vermutung, was realistisch als Erfolg zählt.>

## Lücke (Ist-Zustand, mit Quelle)
<3-5 Punkte, jeder mit Zahl + Quelle-Dateiname. Zuerst der eine neue, noch nicht gezeigte
Punkt, danach kurz die schon gezeigten Punkte.>

## Beweis (zeigen, nicht behaupten)
<1 Haupt-Case, der zu ihrer/seiner Situation passt, + 1 Case in Reserve für Rückfragen.>

## Empfehlung (zuerst das große Paket nennen)
1. <Premium-Paket>: nur nennen, wenn ...
2. <90-Tage-Paket> (empfohlen): ... trägt die Garantie ...
3. <Starter>: nur als Anker nennen, nicht empfehlen.

## Wahrscheinliche Einwände (741-Einwand-Raster, nach Wahrscheinlichkeit sortiert)
<2-4 Einwände mit Reframe-Satz jeweils, aus `00_project/sales-einwandbehandlung.md` ausgewählt
für dieses Profil, nicht die volle Liste.>

## Ablauf für die <Dauer> (741-Call-Raster, Kurzfassung)
1. Ziel quantifizieren
2. Lücke zeigen
3. Beweis bringen
4. Empfehlung aussprechen, Premium zuerst
5. Garantie vor dem Preis nennen
6. Preis öffnen, Einwand-Raster bei Bedarf
7. Abschlussfrage: "Sollen wir den Kick-off für nächste Woche fixieren?"

## Nicht vergessen
<Call-Link, Geräte-Tipp falls vorhanden, was NICHT wiederholt werden soll.>
```

## Worked example — style only, never copy its facts
See `00_project/workflow-builds/sales-call-prep/hand-run-output-korinna-heintze.md` for the
STYLE: short sentences, one number per claim with its source understood (not necessarily
printed inline), no outside method name anywhere, premium-first package order, objections
ranked for the specific profile rather than listed in full.

**Never copy its facts for a new run, even for the same prospect.** That file is a snapshot
from one point in time (14.10.2026). The functional test (2026-10-15) caught exactly this
trap: a fresh run for the SAME prospect found she had since added schema markup, which made
the example's "0 strukturierte Daten" gap stale. Always re-read the current
`booking/baseline.md` + `booking/claims.json` + the latest `booking/site-recheck.json` (if one
exists) for the real, current gap — the worked example shows HOW to write a section, not WHAT
to put in it.
