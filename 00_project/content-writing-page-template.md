# Output template: Seite (Markdown-Master `05-final/page.md`)

Immer dieses Gerüst. Abschnitts-IDs kommen aus dem Briefing (`brief.json` → `sections`). Das Skript `validate_page.py` prüft Reihenfolge, Marken und Pflichtelemente. Technik-Block am Ende ist für 741 und den Entwickler, nicht Teil des sichtbaren Textes.

```markdown
---
client: <Kunde>
page: <Seitenname>
type: service            # homepage | service | location | practitioner | cost | faq
language: de
address: sie             # du | sie
speaker: wir             # ich | wir | dritte
keyword: <Haupt-Keyword>
url_slug: /<slug>/
title: <max. 60 Zeichen, Keyword vorn>
meta: <max. 155 Zeichen>
legal_mode: BRAO         # HWG | BRAO | none
status: Entwurf          # Entwurf | Outline freigegeben | Final freigegeben
date: 2026-10-11
words: <von wordcount.py>
gates: G1 pass, G2 pass, G3 pass, G4 pass, G5 5/5
---

<!-- S01 hero | element: hero | cta: primary -->
<!-- design: Hero links Text, rechts Foto der Person. Beruhigungszeile direkt unter dem Button. -->
# <H1 mit Haupt-Keyword>
<Unterüberschrift: erst die Situation, dann wie wir helfen. 30 bis 40 Wörter.>

**<CTA-Text>**
<Beruhigungszeile.>
<!-- /S01 -->

<!-- S02 answer | element: answer -->
## <Überschrift, die den Anspruch trägt>
<Direkt-Antwort in 2 bis 4 Sätzen. Eigenständig zitierbar.>
<!-- /S02 -->

<!-- S03 check-list | element: check-list -->
## <Überschrift>
- <Situation 1>
- <Situation 2>
- <Situation 3>
<!-- /S03 -->

<!-- S04 step-flow | element: step-flow | cta: primary -->
## <So läuft es ab>
1. <Schritt 1>
2. <Schritt 2>
3. <Schritt 3>
<!-- /S04 -->

<!-- S09 faq | element: faq -->
## <Häufige Fragen>
### <Frage 1?>
<Antwort in 2 bis 3 Sätzen.>
### <Frage 2?>
<Antwort.>
<!-- /S09 -->

<!-- S10 cta | element: cta | cta: primary -->
## <Abschluss-Überschrift, spiegelt den Hero>
<3 bis 5 Häkchen-Punkte, Beweis, Beruhigungszeile.>
**<CTA-Text>**
<!-- /S10 -->

<!-- TECH -->
## Technik (für 741, nicht Teil des sichtbaren Textes)
- Title: …
- Meta: …
- Schema: LegalService + FAQPage + Person (JSON-LD unten)
- Alt-Texte: …
- Interne Links: …
- Wortzahl-Urteil: <X Wörter eigene Seite · Y Bestand · Z Wettbewerber-Median · Quelle · Datum · ausreichend / zu wenig>
- Platzhalter: siehe placeholders.md
```

## Regeln für das Gerüst

1. Platzhalter heißen `[von Kunde bestätigen: <was genau>]`, gelb markiert in der Vorschau. Jeder steht auch in `placeholders.md` (Frage, wer antwortet).
2. Kein HTML im Text. Markdown nur für Überschriften, Listen, Fett, Links.
3. Interne Links als `[Ankertext](/pfad/)` im sichtbaren Text.
4. Designhinweise stehen nur in `<!-- design: … -->`.
5. `cms-blocks.txt` entsteht aus diesem Master: pro Abschnitt ein Block `=== S01 | hero | headline ===`, reiner Text, Feldnamen wie im CMS (Titel, Untertitel, Text, Button).
6. Reihenfolge beim Lesen für Martin: Übersicht (Seite, Typ, Wortzahl gegen Benchmark, Gate-Tabelle, offene Platzhalter, Entscheidungen), dann Text nach Abschnitten.

## `placeholders.md`

| # | Platzhalter | Abschnitt | Frage an den Kunden | Wer antwortet |
| --- | --- | --- | --- | --- |
| 1 | [von Kunde bestätigen: Preis Erstberatung] | S08 | Was kostet die Erstberatung, nach welcher Grundlage? | Kanzlei |
