# Output template: Blogbeitrag (Markdown-Master `05-final/page.md`)

Gleiche Regeln wie die Seiten-Vorlage. Zusätzlich: Autor, Datum, Prüfdatum, Quellen. Regeln: `content-writing-skill/references/blog-rules.md`.

```markdown
---
client: <Kunde>
page: <Titel>
type: blog
language: de
address: sie
speaker: ich
keyword: <Haupt-Keyword>
url_slug: /ratgeber/<slug>/
title: <max. 60 Zeichen>
meta: <max. 155 Zeichen>
legal_mode: BRAO
author: <Name, Titel nur mit Beleg>
author_page: /<person-seite>/
published: <Datum nach Freigabe des Kunden>
last_checked: 2026-10-11
review_due: 2027-10-11
money_page_link: /<leistungsseite>/
status: Entwurf          # Entwurf | wartet auf Kundenprüfung | freigegeben
words: <von wordcount.py>
---

<!-- S01 byline | element: hero -->
# <H1: Frage oder klare Aussage mit Keyword>
Von <Name>, <Titel>. Veröffentlicht am <Datum>. Zuletzt geprüft am <Datum>.
<!-- /S01 -->

<!-- S02 answer | element: answer -->
## Kurz beantwortet
<2 bis 4 Sätze.>
<!-- /S02 -->

<!-- S03 text | element: text -->
## <Grundlage: Gesetz, Verfahren oder Methode>
<Text mit Quellenangabe im Satz. Link zur Leistungsseite im ersten Drittel: [Ankertext](/pfad/).>
<!-- /S03 -->

<!-- S04 text | element: text -->
## <Was das für Sie bedeutet>
<Text. Keine Einzelfall-Bewertung.>
<!-- /S04 -->

<!-- S05 step-flow | element: step-flow | cta: secondary -->
## <Was Sie jetzt tun können>
1. …
2. …
<!-- /S05 -->

<!-- S06 faq | element: faq -->
## Häufige Fragen
### <Frage 1?>
<Antwort.>
### <Frage 2?>
<Antwort.>
### <Frage 3?>
<Antwort.>
<!-- /S06 -->

<!-- S07 text | element: text -->
## Quellen
- <Quelle 1, gelesen am …>
<!-- /S07 -->

<!-- S08 person | element: person | cta: primary -->
## <Über die Autorin / den Autor>
<2 bis 3 Sätze, Titel mit Beleg, Link zur Personenseite.>
**<CTA-Text>**
<Beruhigungszeile.> Allgemeine Information, ersetzt keine Beratung im Einzelfall.
<!-- /S08 -->

<!-- TECH -->
## Technik
- Schema: Article (author, datePublished, dateModified) + FAQPage + Person
- Alt-Texte: …
- Wortzahl-Urteil: …
```

Pflicht vor Veröffentlichung: Prüfung durch den Autor (Kunde). Ohne sie bleibt der Status `wartet auf Kundenprüfung`.
