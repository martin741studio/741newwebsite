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

Quote these sentences as items to review. They are not a claim that the page is illegal.

1. Serious disease named with a treatment link, `https://www.therapie-sasch.com/besuch.html`: "Weltweit gesehen, ist REIKI vor allem in der Nachsorge bei Krebserkrankungen / REHA und bei der Versorgung von Schmerzpatienten etabliert."
2. Cancer study, same page: "Aktuell läuft in Zusammenarbeit mit dem Reiki Verband Deutschland und der Technischen Universität München eine Studie zur Wirksamkeit von Reiki bei Brustkrebspatienten."
3. Efficacy claim, same page: "Reiki gilt als alternative Heilmethode und wird im Unfallkrankenhaus der Charite Berlin bereits als unterstützende REHA-Methode angeboten".
4. Healing-type promise, same page: "Reiki dient der Erhaltung der Gesundheit von Mensch, Tier und Pflanzen", "aktiviert die Selbstgesundungskräfte".
5. Pain claim, same page: "Reiki fördert die Tiefenentspannung und kann bei Stress- und Schmerzsymptomen hilfreich unterstützen." and for animals: "Reiki entspannt Dein Tier und lindert Schmerzen." (Intro: "Dein Tier hatte eine OP oder ist krank, schwach oder liegt im Sterben?")
6. Spiritual healing method, same page: "Die Energetische Wirbelsäulenaufrichtung ist eine Methode des Geistigen Heilens ... löst Blockaden (falsche Haltung aber auch unverarbeitete Traumata etc.)" (the page adds: "Bei Erkrankung der Wirbelsäule und Schmerzen sollte ein Arzt konsultiert werden.")
7. Efficacy claim, same page: "Eine „Aufstellung" ist ein sehr wirksames therapeutisches Werkzeug in der Psychotherapie".
8. Mental illnesses named, `https://www.therapie-sasch.com/praxis.html`: "Mein Schwerpunkt liegt auf der Verhaltenstherapie (ACT – Akzeptanz- und Commitment-Therapie), um Sie gezielt bei Depressionen, Ängsten und Erschöpfung zu unterstützen." Also a list: Depression, Angst / Panikattacken, Erschöpfung & Burnout, Traumata, Zwang.
9. Same wording on `https://www.therapie-sasch.com/about.html`: "psychisch erkrankte Patienten bei Depressionen, Ängsten und Erschöpfung gezielt zu ..." (sentence continues on the page).
10. Home `https://www.therapie-sasch.com/`: "Ob bei Ängsten, Depressionen oder Stress – mein Ziel ist es, Sie auf dem Weg zu mehr Wohlbefinden zu begleiten." and "... energetische Blockaden zu lösen und die Selbstheilungskräfte zu aktivieren".
11. Home, Paar block: "Folgen von psychischer Erkrankung (Bindungsstörungen, Trauma) auf die Beziehung".

Mild or good: most wording says "unterstützen", "begleiten", "kann ... fördern". The page has no explicit "heilt" or guarantee. One safe point: `Buchung.html` "Vertraulichkeit garantiert" refers to data, not a cure.

Title check: she names herself "Heilpraktikerin für Psychotherapie" (home H1, `praxis.html`, `about.html`, `online.html`, footer, `Buchung.html`). The Impressum says "Heilpraktikerin beschränkt auf das Gebiet der heilkundlichen Psychotherapie". No use of "Psychotherapeutin" or "Psychologin" as her own title in any page. Two weak spots:
- Wording "die Therapeutin" (home and `praxis.html` FAQ) and "Paartherapeutin" (home H1): not protected, not wrong.
- `about.html` lists "Psychologische Beraterin (Schule für Gesundheitsberufe)": a school certificate title, not a protected title. Do not shorten it to "Psychologin".
- The page title of `about.html` is "Über mich | Psychotherapie-SASCH" and the brand is "Psychotherapie Sasch". The word "Psychotherapie" in the brand is allowed for HPG. No fix needed, but never write "Psychotherapeutin" on the review page.

## 4. Competitor page lengths (`evidence/comp-pages.json`, run 2026-10-12)

URLs from `demand.md` section 3 (query "paartherapie coburg"). All 5 readable.

| Competitor | Words (page_metrics) | H1 |
|---|---|---|
| https://praxis-bernklau.de/paartherapie/ | 279 | "Paartherapie" |
| https://praxisnoranebel.de/paartherapie/ | 619 (about 556 without the address sidebar) | "Paartherapie und Beziehungscoaching: Verständnis fördern. Verbindung stärken. Beziehung gestalten." |
| http://www.eheberatung-coburg.de/eheberatung-ehetherapie.html | 207 | "Eheberatung, Familienberatung und Teamberatung" |
| https://coburg-psychotherapie.de/ | 596 | "Psychotherapie Coburg" |
| https://www.psychotherapie-nuechterlein.de/ | 405 (about 355 without the aside text) | none in the static HTML. The script took "Cookie-Einstellungen" (cookie banner heading) as H1. |

Mean words: 421 (sorted: 207, 279, 405, 596, 619). Median 405.
Her own `Paar.html`: 614 words, H1 "Online-Paarberatung & Paartherapie". Her page is longer than 4 of 5 competitors. Length is NOT her gap (lesson 4). The data shows that the ranking pages are short, so the gap is not word count.

Caveats on the tool (`content-pool-skill/scripts/page_metrics.py`):
- It does NOT skip `<aside>` blocks. A sidebar counted: `praxisnoranebel.de` has one aside of 63 words (address, phone, Instagram); `psychotherapie-nuechterlein.de` has asides of 28 and 20 words. Cookie-banner text can also be counted (Nüchterlein: its H1 is the cookie heading).
- `praxisnoranebel.de` is in Würzburg (aside: "Lengfelder Straße 58, 97078 Würzburg"), not in Coburg. It ranks for "paartherapie coburg" but is not a local competitor in the map. Use it for page length only.
- `psychotherapie-nuechterlein.de` and `coburg-psychotherapie.de` are home pages (psychotherapy), not Paar pages.
- Only `praxisnoranebel.de` has a price mention ("Honorar"). Her `Paar.html` has a price table (150 EUR / 100 EUR), so she is more open on price than 4 of 5.

## 5. Other points for the writer

- The site says "Sie" (46 Sie-forms, 0 du-forms, `intake.md`). Homepage draft = "Sie", review page = "du".
- No JSON-LD on the home page, but a full LocalBusiness block on `Paar.html` with the Coburg studio address. The Google profile uses Ahorn-Schorkendorf. Agent D should check the scan centre against this.
- Two places on the site: Home practice Krebsmühle 5, Ahorn-Schorkendorf, and Studio FRIEDA, Zinkenwehr 5, Coburg (couples sessions). Source: home page "Praxisstandorte & Termine"; `Paar.html` "Preise & Konditionen".
- Free first talk (15 min) is on the price page, `Paar.html`, `Buchung.html`, and a `Buchung.html` booking flow (Zoom link after payment).
- `Buchung.html` has a calendar widget ("Verfügbare Termine am", month grid) plus a form. The calendar is filled by script; we did not test whether it shows live slots (no browser).
