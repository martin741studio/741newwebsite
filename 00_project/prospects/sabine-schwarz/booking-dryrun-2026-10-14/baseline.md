# Baseline: what Sabine already saw (https://741.studio/review/sabine-schwarz/, page file 2026-10-13)

```json
{
 "status": "OK",
 "slug": "sabine-schwarz",
 "review_url": "https://741.studio/review/sabine-schwarz/",
 "page_date": "2026-10-13",
 "website": "https://www.therapie-sasch.com/",
 "first_name": "Sabine",
 "company": "Sabine Schwarz Heilpraktikerin",
 "city": "Coburg",
 "country": "DE",
 "branch": "health",
 "health": true,
 "health_reason": "branch=health",
 "data_files": [
  "prospect.json",
  "intake.json",
  "demand.md",
  "site-findings.md",
  "homepage.md",
  "competitors.md",
  "scan-search.md",
  "evidence/site.json",
  "evidence/loom-transcript.md",
  "evidence/dfs-volumes-ads.json"
 ],
 "version": "v2.1 (prospect.json)"
}
```

## demand.md (first 60 lines)

# Demand: Sabine Schwarz (agent A, 2026-10-12)

Title rule: she is "Heilpraktikerin für Psychotherapie" (HPG). Never write "Psychotherapeutin".
Evidence folder: `prospects/sabine-schwarz/evidence/`. Cost: 0.1504 USD (cap 0.30), see `cost_ledger.jsonl`.
Her real menu (curl of the homepage, 2026-10-12): Psychotherapie (HPG) `praxis.html`, Online-Paartherapie `Paar.html`, Coaching / Beratung `online.html`, Alternativmedizin / Energiearbeit (Reiki) `besuch.html`, Seminare, Preise. The page `praxis.html` lists the training "Mobbing-Beratung", "EMDR - Traumatherapie", "Burnout-Beratung". The homepage keywords meta lists "Mobbing Beratung".

## 1. Search volume (Germany, location_code 2276, Google Ads)

Evidence: `evidence/dfs-volumes-ads.json`. Numbers are per month, latest value. Series = last 12 months, oldest first.

| Term | Volume | CPC (EUR) | 12-month series |
|---|---|---|---|
| paartherapie kosten | 1900 | 1.77 | 1600, 1900, 1600, 1900, 1900, 1900, 1900, 2400, 1900, 1900, 1900, 1900 |
| mobbing am arbeitsplatz was tun | 1300 | 1.02 | 880, 880, 1000, 1000, 1000, 1600, 1300, 1300, 1000, 1600, 1300, 1300 |
| heilpraktiker coburg | 260 | 1.92 | 140, 210, 170, 210, 210, 480, 260, 260, 210, 260, 260, 260 |
| paartherapie coburg | 110 | 1.96 | 90, 90, 90, 90, 90, 140, 90, 140, 90, 110, 110, 70 |
| mobbing beratung | 110 | no CPC | 30, 90, 110, 90, 90, 110, 170, 90, 90, 140, 140, 140 |
| reiki coburg | 10 | no CPC | 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 10 |
| heilpraktiker psychotherapie coburg | Google gibt keine Zahl heraus | | |
| heilpraktikerin psychotherapie coburg | Google gibt keine Zahl heraus | | |
| psychotherapie coburg | Google gibt keine Zahl heraus | | |
| mobbing coburg | Google gibt keine Zahl heraus | | |
| traumatherapie coburg | Google gibt keine Zahl heraus | | |
| emdr coburg | Google gibt keine Zahl heraus | | |
| burnout beratung coburg | Google gibt keine Zahl heraus | | |
| psychologische beratung coburg | Google gibt keine Zahl heraus | | |

Merged variants: none. No two terms share the same volume, CPC and monthly series, so nothing is merged and nothing is added up. (The eight terms without a number have no series to compare.)
"Google gibt keine Zahl heraus" means: no demand claim for these terms. Do not write "0 searches".

## 2. Gap keyword (proposal)

**paartherapie coburg, 110 searches per month** (evidence: `dfs-volumes-ads.json`).
- Real main service: yes. She has the page `Paar.html` ("Online-Paartherapie / Beziehungsberatung", H1 "Online-Paarberatung & Paartherapie").
- Has demand: yes, 110 per month, CPC 1.96 EUR, competition MEDIUM.
- Her site is not in the organic top 20: `evidence/dfs-serp-1.json` (query "paartherapie coburg", Coburg centre 50.2586,10.9640, depth 20) lists 20 organic results (absolute positions 8 to 31). `therapie-sasch.com` is not among them. One Instagram post at organic rank 15 (absolute 26) only mentions her web address in its text.
- Scan centre: Coburg (the town the keyword names).
- Check for agent D: her Google profile address is Krebsmühle 5, 96482 Ahorn-Schorkendorf (`intake.md`). Her homepage also lists a second place, Zinkenwehr 5, 96450 Coburg (Studio FRIEDA). The scan can show her far from the Coburg centre. Agent D decides with `google-panel` data.
- The SERP shows 8 paid ads (absolute positions 4 to 7, 19 to 20, 32 to 34, e.g. annaholfeld.de, trustlocal.de, betterhelp.com). Paid competition is present.

Second query: "psychotherapie coburg" (`evidence/dfs-serp-2.json`, depth 20). Her site is not in the top 20 here either, but Google gives no volume number for this term. It is not a demand claim. The results are nearly all directories (jameda, therapie.de, arzt-auskunft).

Other terms with real demand, for the writer: "paartherapie kosten" 1900 (national, matches her Preise section on `Paar.html`), "mobbing am arbeitsplatz was tun" 1300 (national, matches "Mobbing-Beratung"), "heilpraktiker coburg" 260. These terms carry no town in the first two cases. Do not use them as the map-scan keyword.

## 3. Competitor provider URLs for the page-length check (no directories)

Source: `evidence/dfs-serp-1.json`, query "paartherapie coburg".
1. https://praxis-bernklau.de/paartherapie/ (organic 8, absolute 16)
2. https://praxisnoranebel.de/paartherapie/ (organic 11, absolute 22)
3. http://www.eheberatung-coburg.de/eheberatung-ehetherapie.html (organic 4, absolute 12)
4. https://coburg-psychotherapie.de/ (organic 2, absolute 9)
5. https://www.psychotherapie-nuechterlein.de/ (organic 10, absolute 18, homepage, not a Paar page)

Skipped as directories or platforms: therapie.de, doctolib.de, dasoertliche.de, instagram.com. Also skipped: loesungsraum-coburg.de (the ranking pages are "Konditionen" and a "Kontakt" page, not a service page).

## 4. Name searches (Coburg centre, depth 10)

- "therapie sasch" (`evidence/dfs-serp-name.json`): `therapie-sasch.com` is NOT in the 9 organic results. The results are unrelated pages (jameda Psychosomatiker Coburg, doctolib listings from other regions, theralupa, findedeinentherapeuten.de). Google shows the item types `knowledge_graph` and `google_reviews` for this query, but the result file holds no detail for them. Do not claim a panel text from this file. Her brand name alone does not bring up her site in this test. Read as: the brand term "Sasch" is not yet connected to her by Google in this location. Treat as a finding to check, not as proof.
- "sabine schwarz heilpraktikerin coburg" (`evidence/dfs-serp-name2.json`): her site is rank 1 (homepage) and rank 7 (`kontakt.html`). Other hits: therapie.de profile (2), theralupa (3), jameda profile (4), LinkedIn (5), Facebook (6), starofservice (8), heilnetz (9), Instagram (10). Item types include `knowledge_graph`, `google_reviews`, `third_party_reviews`. Google also lists her theralupa title "S. Schwarz Heilprakt. Psychotherapie Coburg u. SASCH ... Paartherapie online in Coburg". The full-name search works. The brand search "therapie sasch" does not.



## site-findings.md (first 60 lines)

# Site findings: Sabine Schwarz (agent B, 2026-10-12)

Site: https://www.therapie-sasch.com/ (static HTML on Cloudflare, 17 URLs measured, no sitemap).
Evidence: `evidence/site.json`, `evidence/site-pages.json`, `evidence/site-page-urls.txt`, `evidence/comp-pages.json`. curl checks run 2026-10-12.
Title rule: she is "Heilpraktikerin für Psychotherapie" (HPG). Never write "Psychotherapeutin".

## 1. Technical checks

| Check | Result | Evidence |
|---|---|---|
| tel: link, home | yes, `tel:+4915112489890` | `https://www.therapie-sasch.com/` |
| tel: link, contact | yes, 2 links, same number | `https://www.therapie-sasch.com/kontakt.html` |
| tel: link, service pages | yes on `praxis.html`, `Paar.html`; also `preise.html`, `online.html`, `about.html`, `besuch.html` | curl of each URL |
| Broken tel: links | none | `evidence/site.json` (`pages_with_broken_tel: []`) |
| http to https | NO redirect. `http://www.therapie-sasch.com/`, `http://therapie-sasch.com/` and `http://www.therapie-sasch.com/kontakt.html` all answer 200 on http. Only `https://therapie-sasch.com/` (apex) redirects 301 to `https://www.therapie-sasch.com/`. | `curl -sI http://...` 2026-10-12; `evidence/site.json` (`http_redirects_to_https: false`) |
| Contact form on contact page | yes: name, email, message, consent checkbox, honeypot field | `https://www.therapie-sasch.com/kontakt.html` line 75 (`data-contact-form`) |
| Other forms | home (same form), `Paar.html` (email form for a free couples quiz), `Buchung.html` | curl |
| Contact page content | thin: 56 words by `page_metrics` (177 incl. nav and footer). H1 "Kontaktieren Sie uns" (she works alone; "uns" does not fit). | `evidence/site-pages.json` |
| Duplicate pages | YES: `/` and `/index.html` both return 200, same title "Psychotherapie Sasch \| Sabine Schwarz", same 1040 words. No canonical tag on either. Internal links point to `index.html`. | `evidence/site.json` (`duplicate_pages`); `grep canonical` = 0 |
| Canonical tags | none on home or index | curl |
| Sitemap | `/sitemap.xml` returns 404 ("Nicht gefunden"). `robots.txt` has no Sitemap line. | `curl https://www.therapie-sasch.com/sitemap.xml` |
| Structured data | home: 0 JSON-LD blocks. `Paar.html`: LocalBusiness + Service + Offer. `blog-paartherapie.html`: BlogPosting. | `evidence/site-pages.json` |
| NAP mismatch in schema | `Paar.html` JSON-LD gives address Zinkenwehr 5, 96450 Coburg (Studio FRIEDA). Impressum and Google profile give Krebsmühle 5, 96482 Ahorn-Schorkendorf. The schema URL has no `www` (`https://therapie-sasch.com`), the live host has `www`. | `Paar.html` JSON-LD; `https://www.therapie-sasch.com/impressum.html`; `intake.md` |
| Tracking | no GA4, no GTM found on home | `evidence/site.json` |
| Speed | TTFB 0.35 to 0.51 s | `evidence/site.json` |
| Page without H1 | 2 URLs are fonts (not pages). All real pages have one H1. | `evidence/site-pages.json` |
| Titles/H1 | Home H1: "Willkommen bei Sabine Schwarz, Paartherapeutin & Heilpraktikerin für Psychotherapie" (no town, no service keyword in the H1). `praxis.html` H1 "Psychotherapie (HPG)" (no town). `Paar.html` H1 "Online-Paarberatung & Paartherapie" (no town in H1; the title has no town either). | `evidence/site-pages.json` |
| Mobbing | no Mobbing page. The word appears on `about.html` (3x), `online.html`, `praxis.html`, home (1x each) and in the keywords meta. | grep of each URL |
| Paar page vs. keyword | `Paar.html` is a strong page (614 words, FAQ-like sections, price table, schema) but is framed as "Online". The H1 and title do not say "Coburg". Keyword "paartherapie coburg" (110/month, see `demand.md`). | `evidence/site-pages.json` |

## 2. Price page: `https://www.therapie-sasch.com/preise.html`

There is a price page. All prices with the service (for the calculator):

| Service | Price | Note |
|---|---|---|
| Psychotherapie (HPG), Einzelsitzung "Gesprächstherapeutische Sitzung" | ca. 1 EUR per minute | Plus test costs if needed; admin fee 6,00 EUR per month; invoice for private insurance |
| Paar: Erstgespräch / Kennenlernen | 0 EUR (15 min, free) | |
| Paar: Orientierungsgespräch, one partner | 100,00 EUR (60 min) | Also on `Paar.html` |
| Paar: Beratungsgespräch for 2 persons | 150,00 EUR (1 x 75 min) | Also on `Paar.html` |
| Paar: Intensiv-Setting Paket | 666,00 EUR (value 700,00 EUR; 360 min) | 2 x Einzel 75 min, 3 x Paar 75 min, 1 x Analyse |
| Paar: Begleitung über 6 Monate | 966,00 EUR (value 1000,00 EUR) | 2 x Einzel 75 min, 5 x Paar 75 min, 1 x Analyse 60 min |
| Reiki: per minute | 1 EUR per minute | Ganzkörper 50-60 min; Schmerzbehandlung ca. 20 min |
| Reiki mit Ohrkerzen | 50 EUR | Kopfbehandlung + 2 Ohrkerzen |
| Reiki Kindertarif (3-12 Jahre) | 40 EUR | incl. 1 Ohrkerze |
| Reiki am Tier mit Hausbesuch | 40 EUR + Anfahrt | |
| Energetische Wirbelsäulenaufrichtung | 150 EUR (1,5 h) | |
| Reiki-Seminar Grad I | 280 EUR (2 days) | |
| Reiki-Seminar Grad II | 450 EUR (2,5 days) | |
| Reiki-Seminar Grad III (Meister) | Preis auf Anfrage | |
| Reiki-Übungstreffen | 180 EUR (8 x 2-3 h); single date 25 EUR | |
| Systemische Aufstellung | 100 EUR | |
| Naturcoaching / Waldspaziergang (1-3 h) | Preis auf Anfrage | |
| Tierkommunikation | 50 EUR (up to 3 questions); holiday/weekend 70 EUR; combined with Reiki am Tier 80 EUR | |
| Anfahrt | 1 EUR per km; free inside the municipality of Ahorn | |

For the calculator: the main service for the gap keyword is the couples session. Use 150 EUR (75 min) as the single-session value, or 100 EUR for the first one-partner talk. A 60-minute single psychotherapy session is about 60 EUR (1 EUR/min x 60; the page gives only "ca. 1 EUR / 1 Minute", the 60 is our calculation).

## 3. Health branch (HWG): neutral "Werberecht" row



## homepage.md (first 60 lines)

# Homepage: therapie-sasch.com (agent C, 2026-10-12)

## Score

- Today: **22 / 44** (evidence/scorecard-today.md). Item 22 (HWG) = 0, so the hard gate fails.
- Screenshots: evidence/home-today-1440.jpg (operator), evidence/home-draft-1440.jpg (our draft).
- Review assets: 04_site/public/review-assets/sabine-schwarz/startseite-heute.webp, startseite-entwurf.webp, foto-1.webp, foto-2.webp, foto-3.webp.

## 5-second test

| Question | Today (first screen) | Draft (first screen) |
| --- | --- | --- |
| Was? | "Paartherapeutin & Heilpraktikerin für Psychotherapie" in the H1 sub-line. Services hide in the "Angebote" dropdown. | "Ihre Heilpraktikerin für Psychotherapie in Coburg und Ahorn." plus Psychotherapie (HPG), Paartherapie, Coaching in the sub-line. |
| Wo? | Not visible. Ahorn and Coburg appear only in the Standorte section further down. | Coburg and Ahorn in the H1. "2 Praxisorte: Ahorn-Schorkendorf · Coburg" in the trust row, "oder online" in the sub-line. |
| Warum du? | Membership logos at the fold (Reiki-Verband, VFP, Heilnetz). Google 5,0 with 15 reviews is not on the site. | 5,0 bei Google · 15 Bewertungen, Erlaubnis seit 2019, Mitglied im VFP e.V. und Heilnetz e.V. |
| Wie zum Termin? | Button "Kontakt". The floating "Erstgespräch buchen · kostenlos · 15 Min." is semi-transparent and covers the Heilnetz text. No phone in the first screen. | Button "Kostenloses Erstgespräch buchen", line "15 Minuten, kostenlos. Online buchen, anrufen oder schreiben.", phone 0151 124 8989 0 in the top bar and the trust row. |
| Wer? | Real photo of her in the practice room, name in the H1. | Same room photo as the hero image, name card with face photo and "Heilpraktikerin für Psychotherapie · Paartherapeutin". |

Notes for the review page:
- Her strongest asset is unused: 15 of 15 Google reviews are 5 stars, and she answered all of them. The site shows none.
- She already has an online booking page (Buchung.html, "Erstgespräch buchen, kostenlos, 15 Min."). The hero button still says only "Kontakt".
- HWG risk on the homepage: "Selbstheilungskräfte zu aktivieren", "schnell spürbare Fortschritte", "nachhaltige Veränderungen zu ermöglichen".
- The Google category is "Alternativmediziner". Her main service is Psychotherapie (HPG) and Paartherapie. Agent D/E must check this against the keyword.
- Mobbing-Beratung appears only on about.html (training 2016-2018, Fachausbildung). It is not a service on the homepage.
- Imprint: "Heilpraktikerin beschränkt auf das Gebiet der heilkundlichen Psychotherapie", Erlaubnis vom 18.11.2019 (Stadt Nürnberg). Never write "Psychotherapeutin".

## Test of draft_home.py

Run: `python3 prospect-mini/scripts/draft_home.py sabine-schwarz --service "Heilpraktikerin für Psychotherapie"`, 3 s wall time (script reports 2.8 s).

What I had to fix by hand in draft/index.html:
1. **Wrong logo.** logo.png was Logo_Verband.png, the VFP membership seal. Her site has no logo image, only the text brand "Psychotherapie Sasch" (green "Sasch"). Replaced with that text brand. File removed.
2. **Wrong second photo.** praxis.jpg was Paar1_Sasch.jpg, a love-lock on a bridge in Würzburg (decorative, not her room). Removed. The room photo with her (HeroSectionSASCH2.jpeg) is now the main hero image.
3. **Portrait card used the room photo.** A full-room photo does not work as a 56 px face. New badge.jpg = face crop from Brett_SASCH.jpeg (her real photo, from her site).
4. **Phone format.** "+4915112489890" in the top bar and the trust row. Changed to her imprint format, "0151 124 8989 0".
5. **City.** Script used only "Coburg" and "mit eigener Praxis in Coburg". Her own practice is in Ahorn-Schorkendorf, Coburg is Studio FRIEDA, Zinkenwehr 5 (Thursday 9-18 Uhr). H1 now "in Coburg und Ahorn", trust card "2 Praxisorte".
6. **Sub-headline.** "Sie suchen eine Heilpraktikerin für Psychotherapie in Coburg? Ich nehme mir Zeit …" repeated the H1. Rewritten: situation (Krise, allein oder als Paar) + 3 helps + 3 places (Ahorn, Coburg, online).
7. **Nav.** "Alternativmedizin" removed (HWG risk, not the main offer). "Preise" added (her real nav item). "Online-Paartherapie" shortened to "Paartherapie".
8. **CTA and reassurance.** "Ersttermin vereinbaren" / "Termin vereinbaren" → "Kostenloses Erstgespräch buchen" / "Erstgespräch buchen", from her real booking offer (15 Min., kostenlos). Note line now has facts. Ghost button "Leistungen ansehen" → "Angebote ansehen" (her menu word).
9. **No stars.** The script had no rating. Added "5,0 bei Google · 15 Bewertungen" from evidence/google-panel-2026-10-12.md.
10. **Trust row.** 3 cards, one repeated the eyebrow. Replaced by 4 cards with facts: Erlaubnis seit 2019 (imprint), 2 Praxisorte, Mitglied im VFP e.V. und Heilnetz e.V., Telefon.
11. **Colours and font.** Script cream #edf2ee and Fraunces serif. Changed to her site: Poppins, sand #f6f3ed, line #e9e4da, ink #333333. Green #4a7c59 kept.
12. **Layout at 1440.** Nav items and the header button wrapped to two lines. Fixed with nowrap, a header gap and a smaller nav gap.

Checks passed: form of address "Sie" (her site uses "Sie"). No healing or success promise in the draft. No "Psychotherapeutin". No skip link or info page in nav, eyebrow or trust row.

Strip photos (all from therapie-sasch.com, opened and checked):
- foto-1 = HeroSectionSASCH2.jpeg, her in the practice room (1200 px).
- foto-2 = Brett_SASCH.jpeg, her portrait with the systemic board (1000 px).
- foto-3 = praxis_header.jpeg, her hands writing notes in a session (1000 px).
Not used: Rutengehen and Reiki photos (alternative methods, HWG risk next to psychotherapy), Paar1/Paar2 (love-locks, not her).


## Visible review-page text

Private Website- & Sichtbarkeits-Analyse | Sabine Schwarz Heilpraktikerin, Coburg | 741.Studio {{> header_de}} 🔒 PRIVATE WEBSITE- & SICHTBARKEITS-ANALYSE Sabine, so finden Paare aus ganz Coburg deine Praxis bei Google. Bei „paartherapie coburg“ stehst du an 5 von 49 Messpunkten unter den ersten drei, in der Stadtmitte nicht unter den ersten 20. Hier ist dein Plan. Du hast 5,0 Sterne bei 15 Bewertungen, deine Website steht für deinen Namen auf Platz 1. Doch dein Eintrag mit den Bewertungen steht in der Stadtmitte von Coburg nicht unter den ersten 20. 🎯 Persönlich aufgenommen für: Sabine Schwarz Zeig mir meinen Markt → 30 Minuten, kostenlos: Ich zeige dir live, wer in deinem Markt oben steht – und warum. Martin Ich habe mir therapie-sasch.com und deinen Google-Eintrag genau angesehen. Hier zeige ich dir, was ich gefunden habe. Google-Karte · Sichtbarkeits-Check Unter den ersten drei an 5 von 49 Punkten, alle im Südwesten. In der Stadtmitte nicht unter den ersten 20. Wir haben gemessen, wo deine Praxis bei der Suche „paartherapie coburg“ in der Google-Karte erscheint: an 49 Punkten im 5-km-Umkreis um die Stadtmitte von Coburg (Messung vom 12.10.2026). Jede Zahl ist dein Platz an genau diesem Ort. ● Heute – echte Messung Unter den ersten drei an 5 von 49 Punkten. Alle fünf liegen im Südwesten, rund um Schorkendorf und Witzmannsberg, nahe deiner Praxis. In der Stadtmitte und im ganzen Nordosten steht „20+“: An 23 Punkten bist du nicht unter den ersten 20. Praxis Rudi Bernklau steht auf rund 61,2 % der Karte unter den ersten drei. ● Das Ziel – so kann es aussehen 4 3 3 3 3 3 4 3 2 2 2 2 2 3 3 2 1 1 1 2 3 3 2 1 1 1 2 3 3 2 1 1 1 2 3 3 2 2 2 2 2 3 4 3 3 3 3 3 4 Ziel-Szenario (Simulation) Ziel: unter den ersten drei auch in der Stadtmitte von Coburg. Die vier Praxen mit dem größten Anteil der Karte haben 0 bis 11 Bewertungen, du hast schon 15. Martin Deine 15 Bewertungen stehen auf deinem Eintrag in Ahorn, den Google in der Stadtmitte nicht unter den ersten 20 zeigt. In Coburg sichtbar ist dein Eintrag im Studio FRIEDA, ohne eine Bewertung. 📞 Anrufe direkt aus der Google-Karte 🧭 Paare aus ganz Coburg finden dich 🤝 Mehr Anfragen für ein Erstgespräch Wer in der Google-Karte unter den ersten drei steht, bekommt den Großteil aller Klicks, Anrufe und Routen. Ist der Sprung realistisch? Andere Praxen hatten ähnliche Lücken im Google-Eintrag. So hat sich ihr Platz verändert. Ausgewählt nach deiner Lage: Heilpraktiker in Freiburg und Regensburg, eine Familienberatung bei Stuttgart und ein Betrieb aus Wien. Bei jedem fehlte etwas, das auch bei dir fehlt: die passende Einordnung bei Google oder Leistungen im Eintrag. Bernd Laserstein Heilpraktiker · Freiburg → Platz 1 Nachher: echte Kartenmessung · → Platz 1 Maria Abel Familienberatung · Raum Stuttgart 0 → 100 % Nachher: echte Kartenmessung · 0 → 100 % Naturheilpraxis Veronika Schlirf Heilpraktikerin · Regensburg Platz 85 → 1 Nachher: echte Kartenmessung · Platz 85 → 1 Astrid Lengauer Innenarchitektur · Wien Platz 18 → 1 Wer dahintersteht Martin Drendel Gründer und CEO von 741.Studio Ich leite 741.Studio, ein kleines Remote-Team aus Designern, Entwicklern, Media Buyern und Growth Marketern in Indonesien, Deutschland und Australien. Mein Grundsatz: Komplexität ist der Feind der Ausführung. Wir suchen die wenigen Schritte, die bei dir am meisten bewirken. 10+ Jahre Erfahrung mit lokaler Sichtbarkeit bei Google 250+ Unternehmen unterstützt Martin So sieht es aus, wenn es klappt: Bernd Laserstein, auch Heilpraktiker, kam bei „Körperpsychotherapie“ auf Platz 1. So haben wir es gemacht – 4 Fälle ansehen Fälle schließen ▾ Bernd Laserstein Heilpraktiker · Freiburg → Platz 1 „Körperpsychotherapie“, vorher um Platz 6 Auch Heilpraktiker mit Psychotherapie, vorher: Ungenaue Einordnung bei Google, Leistungen nicht eingetragen, keine Bewertungen, keine Messung. Einordnung im Google-Eintrag präzisiert Leistungen eingetragen: Körperpsychotherapie, Biosynthese, Hakomi Bewertungs-Routine von null aufgebaut Leistungsseiten untereinander verlinkt Ergebnis: an 91 % der Karte sichtbar – bei 109 Mitbewerbern Vorher Nachher Ganze Fallstudie → Maria Abel Familienberatung · Raum Stuttgart 0 → 100 % der Karte unter den ersten 3, in 8 Wochen Vorher: In der Karte unsichtbar, Einordnung und Leistungen unvollständig, langsame Website, keine Einträge in Branchenbüchern. Richtige Einordnung: Erziehungs-, Psychologische und Beziehungsberaterin Website schneller gemacht, klare Überschriften mit Suchbegriffen Einträge in Branchenbüchern von null aufgebaut Bewertungs-Routine eingeführt Ergebnis: im Schnitt Platz 1,8 im ganzen Gebiet Nachher Ganze Fallstudie → Naturheilpraxis Veronika Schlirf Heilpraktikerin · Regensburg Platz 85 → 1 „Heilpraktikerin“, 5.400 Suchen/Monat Vorher: Leistungen nicht im Google-Eintrag, keine Bewertungen, Website nicht fürs Handy gebaut. Name und Beschreibung im Google-Eintrag mit den echten Suchbegriffen Alle Leistungen eingetragen, je mit passender Seite Bewertungen von 0 auf 5,0 Sterne – mit Nachfass-Vorlage, jede beantwortet Website fürs Handy gebaut, neue Hauptüberschrift Gleiche Adresse in allen Branchenbüchern, Apple Karten und Bing Vorher Nachher Ganze Fallstudie → Astrid Lengauer Innenarchitektur · Wien Platz 18 → 1 „Interior Design Wien“ Vorher: Google ordnete den Betrieb unvollständig ein, Leistungen fehlten, keine Seiten für die einzelnen Leistungen und Orte. Zusätzliche Einordnungen im Google-Eintrag ergänzt Sechs Leistungen eingetragen (Moodboard, Konzept, 3D-Darstellung …) Eigene Seiten je Leistung und je Einzugsgebiet Rund 100 Verweise von lokalen Seiten aus der Region Feste Routine für Bewertungen und Antworten Ganze Fallstudie → Weitere Ergebnisse Claudia Irmscher Heilpraktikerin Psychotherapie ▲ Platz 11 → 2 Torsten Menge Psychotherapie ▲ Platz 117 → 3 Nachher: echte Kartenmessung · ▲ Platz 117 → 3 Angelina Everitt Hypnosetherapie · Stuttgart ▲ Platz 21 → 3 Karoline Hengst Homöopathie ▲ Platz 28 → 2 Nachher: echte Kartenmessung · ▲ Platz 28 → 2 Sven Böhme Heilpraktiker · Stuttgart ▲ Platz 17 → 4 Nachher: echte Kartenmessung · ▲ Platz 17 → 4 Was nach der Karte kommt Drei Hebel für mehr Termine, und bei jedem fehlt heute ein Schritt Für deine Praxis haben wir drei Dinge geprüft: wonach Menschen bei Google suchen, warum andere Praxen in der Karte vor dir stehen und ob deine Startseite aus Besuchern Termine macht. Jede Zahl unten stammt aus echten Messungen, die Werte im Rechner sind Annahmen. Schritt 1 Wonach deine Patienten suchen Welche Leistungen sie bei Google eingeben und welche Fragen deine Seite noch nicht beantwortet. 1.900 Suchen/Monat: paartherapie kosten Schritt 2 Damit das Telefon klingelt Warum andere Praxen in der Google-Karte vor dir stehen. unter den ersten 20 an 26 von 49 Punkten Schritt 3 Startseite, die Termine bringt Ob ein Besucher in 5 Sekunden versteht, was du anbietest und wie er einen Termin bekommt. heute 22 von 44 Punkten Schritt 1 · Wonach deine Patienten suchen Deine Paar-Seite hat 614 Wörter und klare Preise. Coburg fehlt in ihrem Titel und ihrer Überschrift. Wir haben deine Website mit den Seiten verglichen, die bei „paartherapie coburg“ oben stehen, und mit dem, was Menschen in Deutschland wirklich eingeben. Was Menschen bei Google eingeben Suchen pro Monat in ganz Deutschland (Mittel der letzten 12 Monate, Abruf 12.10.2026) paartherapie kosten 1.900 mobbing am arbeitsplatz was tun 1.300 heilpraktiker coburg 260 paartherapie coburg 110 mobbing beratung 110 reiki coburg 10 Gelb = Fragen und Themen, grün = Suche nach einer Praxis. „paartherapie kosten“ und „mobbing am arbeitsplatz was tun“ sind Fragen ohne Ort, gezählt in ganz Deutschland. Mit dem Ort im Suchbegriff zeigt Google „heilpraktiker coburg“ mit 260 und „paartherapie coburg“ mit 110 Suchen im Monat. Für Psychotherapie, Traumatherapie, EMDR und Burnout-Beratung in Coburg gibt Google keine Zahl heraus. Ohne Zahl bei Google: „heilpraktiker psychotherapie coburg“, „heilpraktikerin psychotherapie coburg“, „psychotherapie coburg“, „mobbing coburg“, „traumatherapie coburg“, „emdr coburg“, „burnout beratung coburg“, „psychologische beratung coburg“. Google gibt für viele Begriffe keine Suchzahlen heraus – das heißt nicht, dass niemand sucht. Die Chance ist nicht die Länge, sondern Coburg in der Überschrift Deine Paar-Seite ist länger als die Seiten vorn. Es fehlt der Satz, der Google und Besuchern sagt: Paartherapie in Coburg. 614 Wörter auf deiner Paar-Seite 0 Mal „Coburg“ in Titel und Hauptüberschrift deiner Paar-Seite Deine Paar-Seite 614 Seiten vorn zu „paartherapie coburg“ (Mittel aus 5) 421 Keine der fünf Seiten vorn nennt Paartherapie und Coburg zusammen in der Hauptüberschrift. Deine Startseite beginnt mit „Willkommen bei Sabine Schwarz“, deine Paar-Seite mit „Online-Paarberatung & Paartherapie“. Martin Für Psychotherapie, Traumatherapie und Burnout-Beratung in Coburg gibt Google keine Suchzahl heraus. Im Gespräch schauen wir, welche Anfragen bei dir am häufigsten kommen. Die 6 wichtigsten neuen Inhalte für deine Website 1 Startseite „Heilpraktikerin für Psychotherapie in Coburg und Ahorn“ Ort Heute beginnt deine Startseite mit „Willkommen bei Sabine Schwarz“. Coburg und Ahorn fehlen in der Hauptüberschrift. 2 Seite „Paartherapie in Coburg und online“ Leistung „paartherapie coburg“: 110 Suchen pro Monat. Deine Paar-Seite heißt „Online-Paarberatung“ und steht dafür nicht unter den ersten 20 Treffern. 3 Seite „Was kostet Paartherapie?“ Leistung „paartherapie kosten“: 1.900 Suchen pro Monat in Deutschland. Deine Preise stehen schon da (150 € für 75 Minuten zu zweit), aber keine Seite beantwortet genau diese Frage. 4 Seite „Mobbing am Arbeitsplatz: was tun?“ Leistung „mobbing am arbeitsplatz was tun“: 1.300 Suchen pro Monat in Deutschland. Du hast eine Ausbildung in Mobbing-Beratung, aber dazu keine eigene Seite. 5 Seite „Psychotherapie (HPG) in Coburg“ Leistung „heilpraktiker coburg“: 260 Suchen pro Monat. Deine Seite heißt heute „Psychotherapie (HPG)“, ohne Ort in der Hauptüberschrift. 6 Deine Bewertungen auf der Website Profil Alle 15 Bewertungen bei Google haben 5 Sterne. Auf deiner Website steht keine davon. Schritt 2 · Damit das Telefon klingelt Deine 15 Bewertungen stehen auf dem Eintrag, den Google in der Stadtmitte nicht unter den ersten 20 zeigt. Dein Eintrag in Coburg hat keine. Wir haben die Google-Einträge der Praxen verglichen, die bei „paartherapie coburg“ in der Karte oben stehen. Die vier vorn sind an allen 49 Messpunkten unter den ersten 20 zu sehen, dein Eintrag mit den Bewertungen an 26. Praxis So ordnet Google sie ein Google-Bewertungen Oben in der Karte bei „paartherapie coburg“ Sabine Schwarz (dein Eintrag mit 15 Bewertungen) Alternativmediziner 15 10,2 % Praxis Rudi Bernklau Berater 11 61,2 % Sexual- und Paartherapie Franziska Bartsch Berater 3 49 % Lösungsraum Coburg Familienberater, Ehe- und Paarberater 0 49 % Praxis für systemische Beratung und Therapie, Michaela Wittmann Familienberater, Berater, Ehe- und Paarberater 1 26,5 % ← Tabelle seitwärts wischen → Prozent = an wie vielen von 49 Messpunkten im 5-km-Umkreis um die Stadtmitte die Praxis unter den ersten drei der Google-Karte steht. Gemessen am 12.10.2026. Was das heißt: Bewertungen sind nicht deine Lücke: Die vier Praxen mit dem größten Anteil der Karte haben 0 bis 11, du hast 15. Diese Praxen liegen rund 1 bis 2,7 km von der Stadtmitte, deine Praxis in Ahorn-Schorkendorf 4,3 km. Doch Franziska Bartsch sitzt auch in Ahorn und steht mit 3 Bewertungen an allen 49 Punkten unter den ersten 20, die Entfernung allein erklärt die Lücke also nicht. Der Eintrag, den Google in Coburg zeigt, ist dein Eintrag „Sabine Schwarz Paartherapie“ im Studio FRIEDA: an allen 49 Punkten unter den ersten 20, in der Stadtmitte auf Platz 4, aber ohne Bewertung. Martin Der größte Hebel sind deine drei Google-Einträge: Der Eintrag, den Google in Coburg zeigt, braucht Einordnung, Zeiten und Bewertungen. Deine 15 Bewertungen mit 5 Sternen zeigen, dass deine Klienten gern bewerten. Was wir an de
