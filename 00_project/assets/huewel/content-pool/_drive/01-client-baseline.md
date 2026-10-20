# Client baseline: Praxis Hüwel (Martin Hüwel)

Date: 2026-10-11. Mode: existing site (`www.praxis-huewel.de`, GitHub Pages, live since 2026-10-06). Compliance mode: HWG.
Sources reused (not collected again): memory `huewel-client`, `huewel-nap`, `huewel-website-live-state`, `huewel-site-workflow`, `huewel-onlyinside-ersatz`. Live crawl of 2026-10-11 (28 URLs from the real `sitemap.xml`).

## 1. Services (ground truth for the fit test)

Hüwel says: exactly 6 offers on the site, nothing to add (memory `huewel-client`). Later confirmed for the Google profile: Bioresonanz (as search term only), Mikronährstoff-Begleitung, Schwermetallbelastung (only "abklären"), Nebennierenschwäche, PostVac and Long Covid support.

| Key | Service | Source |
| --- | --- | --- |
| frequenztherapie | Frequenztherapie (Ondamed / PEMF). Main term. Never change (warning of 2018) | live `/methoden-als-werkzeuge/frequenztherapie.html` |
| pse | Psychosomatische Energetik (PSE) | live page, 780 words |
| homoeopathie | Homöopathie | live page, 619 words |
| gesundheitscheck | Gesundheitscheck (Bioscan, about 240 parameters) | live page, 751 words |
| ursachenanalyse | Ursachen-Klarheitsanalyse (package) | live page, 181 words |
| wartezeit | Wartezeit-Vermeider (mini audit, PDF) | live page, 167 words |
| bioscan, vitalstoffe, mikronaehrstoffe | Bioscan, Vitalstoffanalyse, Mikronährstoff-Begleitung | live pages |
| nebenniere, erschoepfung, postvac | Nebennierenschwäche (as a naturopathic concept), chronic exhaustion (medical check first), PostVac / Long Covid support | live pages; GBP services |

Not offered: Ausleitung, Entgiftung, Darmsanierung (Hüwel, 2026-08-24), Heileurythmie. Package prices and the 90 EUR single session: on the live pages, not repeated here.
Rules from Hüwel's history: the VSW warned him in 2018, so "Frequenztherapie" stays the main term. "Bioresonanz" is a search term only, never a device or method promise. No healing promises. Do not copy wording from reference sites such as `schmerzpraxis-mannheim.de` (structure only).

## 2. Places

- Praxis: Gesundheitspraxis im Nürbanum, Allersberger Str. 185, Gebäude A7, 3. OG, 90461 Nürnberg (Südstadt). Phone 0911 6007651. Hours: Mo–Sa 08:00–20:00, So 10:00–22:00 (confirmed 2026-08-29). Source: memory `huewel-nap`.
- Neighbours seen in search data: Fürth, Erlangen, Schwabach (volumes 260, 320, 210). `[FEHLT]` Where do the patients come from?
- Local Falcon baseline of 2026-08-18 (7×7, 5 km): "frequenztherapie nürnberg" SoLV 87.8 %, "homöopathie nürnberg" 28.6 %, "naturheilpraxis nürnberg" 8.2 %, "heilpraktiker nürnberg" 6.1 %, "bioresonanz nürnberg" 0 %. Radius is the relevance limit, not the address (memory).
- NAP conflicts in directories: old address at Doctolib, "Geb. F, 1. OG" on four directories, a ghost name on two (citation audit 2026-08-31). `[FEHLT]` Release to correct them.

## 3. Brand

- Message: "Ursachen finden statt Symptome verwalten". Target group in his words: people with long, unclear complaints despite many doctor visits, and entrepreneurs, self-employed and managers aged 45 and older.
- Voice: formal Sie on the site. The PDF "Wartezeit-Vermeider" uses Du. `[FEHLT]` One form.
- Strategic turn: Hüwel wants B2B packages for entrepreneurs through LinkedIn. Local SEO does not solve that channel (memory). `[FEHLT]` The offer for entrepreneurs.
- Booking channel: contact form (primary), phone. Calendly is second. Forms run through an own edge function since 2026-10-06; the data-processing agreement (AVV) is open.

## 4. Proof (authority)

| Proof | Status | Source |
| --- | --- | --- |
| Google rating 4.9 with 10 reviews | seen in Local Pack 2026-10-11 | `02-competitors/serp-2.json` |
| Competitor reviews: Brahmer 50, Winter 51, Dr. Philipp 107, Helios 22 | Local Pack 2026-10-11 | serp-1, serp-2 |
| Patient quotes on the home page and a quotes page | live, HWG check needed (§ 11 HWG) | live site |
| Qualification page and "Über mich" (375 words) | live | `own-metrics.json` |
| Membership BVMID (since July 2026) | from Hüwel, no logo file | memory |
| Directory entries: 23 found (16 own entries confirmed in August) | audit 2026-08-31 | memory `huewel-nap` |
| ProvenExpert, Doctolib, jameda profiles | exist | memory |

## 5. Own site (measured 2026-10-11, 28 pages)

- Home page: 1,603 words, 1 H1, 12 H2, FAQPage and MedicalBusiness markup. Title "Heilpraktiker & Homöopath Nürnberg | Praxis im Nürbanum".
- Method pages: 540 to 780 words. Thin: Ondamed 220, Mikronährstoff 204, Ursachen-Klarheitsanalyse 181, Wartezeit-Vermeider 167, Bioscan 304, Contact 104.
- The old sub pages (Schmerzen und Verletzungen, Migräne, Psyche, Burnout, Stoffwechsel, chronic illness incl. cancer) are redirect stubs to anchors of one page `/was-ist-ihr-anliegen.html` (597 words).
- Structured data on the home page: MedicalBusiness has no opening hours, no sameAs, no service list, no price range (live check 2026-10-11). On the old site the hours had been corrected.
- Own rankings (DataForSEO 2026-10-11): only 2 keywords with volume ("heileurythmie nürnberg" #54, "apotheke nürbanum" #71). The relaunch on 2026-10-06 is the likely reason.
- Backlinks (DataForSEO 2026-10-11): 79 referring domains. Brahmer 104, Helios 123.

## 6. Search Console

The 741 service account has access to the property `https://www.praxis-huewel.de/` (Hüwel granted it; the `https://` without www and the `sc-domain:` forms still return 403, only `www` is needed). The export ran on 2026-10-11 through the API: 2026-07-11 to 2026-10-09 (90 days). Page rows: 72 clicks, 3,062 impressions. Query rows: 154 queries, 13 clicks, 1,581 impressions (GSC hides rare queries). The period mixes the old site and the new site (relaunch 2026-10-06). Files: `03-demand/gsc-api.json`, `gsc-queries-90d.tsv`, `gsc-pages-90d.tsv`. The first read by hand (UI, 2026-07-09 to 2026-10-08, 42 rows) is archived in `03-demand/_archiv/`.

## 7. [FEHLT] list for the client form

1. Parking (free?), barrier-free access, public transport stop.
2. Where do the patients come from (Fürth, Erlangen, Schwabach)?
3. Release to correct Doctolib and the directories.
4. Which 3 to 5 concerns may get own pages (only concerns, no diagnoses)? Same for PostVac and Long Covid: how exactly does he support?
5. Current packages and prices for the check.
6. Written consent for patient quotes, and a check of the existing quotes.
7. List of further training and associations with proof, and logo files.
8. Sie or Du for the PDF.
9. The offer for entrepreneurs (pivot talk with Martin Drendel).
10. Data-processing agreement for the forms.
11. Heavy-metal topic: only "abklären", no Ausleitung?
