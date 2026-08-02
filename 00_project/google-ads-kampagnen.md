# Google Ads Kampagnen-Setup — Kostenlose Sichtbarkeits-Analyse

Stand: 24.07.2026 · Landingpages live & getestet:
- **DE:** https://741.studio/pages/sichtbarkeits-analyse.html (Praxen & lokale Betriebe)
- **EN:** https://741.studio/pages/visibility-audit.html (Bali / internationale Local Businesses)

Beide Pages: eigenes Quiz → Supabase (`quelle` unterscheidet LP/Sprache) → automatische Lead-Mail (Resend). Meta Pixel: PageView / QuizOpened / Lead. Google-Ads-Conversion-Tag-Platzhalter ist im `<head>` beider Seiten markiert.

---

## Kampagne 1 — DE „Sichtbarkeits-Analyse"

**Settings**
- Typ: Nur Suchnetzwerk (Display-Netzwerk & Suchnetzwerk-Partner **AUS**)
- Geo: Nürnberg + 50 km Umkreis (Roth, Schwabach, Fürth, Erlangen) — Search-Console beweist hier reale Nachfrage („seo nürnberg" Pos. 5.8). Später auf DACH erweitern.
- Sprache: Deutsch · Budget: **15 €/Tag**
- Gebote: Start „Klicks maximieren" mit **CPC-Limit 2,50 €** → nach ~15–30 Conversions auf „Conversions maximieren" umstellen
- Conversion-Aktion: „Lead – Sichtbarkeits-Analyse" (Website), Tag in beide LPs einbauen (Platzhalter vorhanden)

**Anzeigengruppe A — Google-Sichtbarkeit (Phrase/Exact)**
```
"bei google gefunden werden"
"google maps ranking verbessern"
"google unternehmensprofil optimieren"
"google eintrag optimieren lassen"
"local seo agentur"
"google bewertungen mehr bekommen"
"warum finde ich mein unternehmen nicht bei google"
```

**Anzeigengruppe B — Praxismarketing (Phrase/Exact)**
```
"praxismarketing"
"mehr patienten gewinnen"
"zahnarzt marketing"
"physiotherapie marketing"
"patientengewinnung praxis"
"praxis bei google optimieren"
```

**Anzeigengruppe C — Region (Phrase/Exact)**
```
"seo nürnberg"  ·  "seo agentur nürnberg"
"online marketing nürnberg"
"seo schwabach"  ·  "seo roth"
"webdesign nürnberg"  ·  "webdesign roth"
```

**Negativ-Keywords (Kampagnen-Ebene)**
```
job, jobs, stelle, stellenangebot, gehalt, ausbildung, praktikum, studium,
kurs, seminar, weiterbildung, definition, was ist, selber machen, anleitung,
tutorial, tool, software, kostenlos tool, login, agentur werden, freelancer werden
```

**Responsive Search Ad — Headlines (je ≤30 Zeichen)**
1. Gratis Sichtbarkeits-Check
2. Wo steht Ihr Google-Ranking?
3. Mehr Kunden über Google
4. In Google Maps nach oben
5. Analyse als persönliches Video
6. Local SEO vom Spezialisten
7. 200+ Betriebe analysiert
8. Antwort in ca. 2 Stunden
9. Für Praxen & lokale Betriebe
10. Jetzt kostenlos prüfen lassen
11. Wer verdrängt Sie bei Google?
12. Mehr Patienten für Ihre Praxis
13. Sichtbar, wo Kunden suchen

**Descriptions (je ≤90 Zeichen)**
1. Kostenlose Analyse mit Video: Maps-Ranking, Wettbewerber & 3 konkrete Maßnahmen.
2. In 60 Sekunden angefordert – kostenlos & unverbindlich. Zustellung per WhatsApp & E-Mail.
3. Manuell erstellt statt Automat: Ihr persönlicher Sichtbarkeits-Check vom Analysten.
4. Local-SEO-Analyst mit 200+ analysierten Betrieben. Antwort werktags in ca. 2 Std.

**Erweiterungen:** Anruf-Erweiterung (Praxen rufen gern an) · Sitelinks (Analyse anfordern / So funktioniert's / Über 741.Studio) · Zusatzinfos („100 % kostenlos", „Persönliches Video", „DSGVO-konform")

---

## Kampagne 2 — EN „Visibility Audit" (Bali) — **ÜBERHOLT (29.07.2026)**

> Dieser Abschnitt ist ersetzt durch **`00_project/bali-campaign-build-sheet.md`**.
>
> Was sich geändert hat: eigene Landingpage je Leistung statt einer gemeinsamen
> (`/pages/bali-local-seo.html` und `/pages/bali-web-design.html`), Suchnetzwerk-only ohne Maps,
> Negativliste um indonesische Begriffe erweitert, komplett neue Anzeigentexte ohne Kundennamen,
> alle Assets gegen Googles Zeichenlimits geprüft. Die hier ursprünglich notierte LP
> `/pages/visibility-audit.html` wird für die Bali-Kampagne nicht mehr verwendet.

## Nach dem Kampagnen-Anlegen (To-do)
1. **Conversion-Aktion** in Google Ads anlegen → `AW-…`-Tag an mich → ich baue ihn an den markierten Platzhalter beider LPs (Conversion feuert beim Quiz-Submit, parallel zum Meta-Lead-Event).
2. 7–14 Tage laufen lassen, dann: Suchbegriffs-Bericht prüfen → Negativliste erweitern.
3. Nach 15–30 Conversions: Gebotsstrategie auf „Conversions maximieren".
