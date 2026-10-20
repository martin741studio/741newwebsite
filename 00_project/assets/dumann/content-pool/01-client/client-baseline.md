# Client baseline: Naturheilpraxis Daniela Dumann

Date: 2026-10-11. Mode: existing site (danieladumann.de, Wix). Compliance mode: HWG.
Rule: this file lists facts only. Every fact has a source. A gap carries `[FEHLT]`.
Source of truth for facts: `00_project/assets/dumann/cro/02-data/dataset.md` (CRO Step 1, verified live on 2026-10-11). This run reuses it. It does not collect the same facts again.

## 1. Services (ground truth for the fit test)

| Key | Service | Source |
| --- | --- | --- |
| hildegard-heilkunde | Hildegard-Heilkunde (hub, method) | dataset.md 1.1, 1.9 |
| aderlass | Aderlass Therapie | dataset.md 1.1 |
| darmsanierung | Darm Sanierung (not Colon-Hydro-Therapie) | dataset.md 1.1 |
| ernaehrung-fasten | Ernährungsberatung and Fasten | dataset.md 1.1 |
| pflanzenheilkunde | Pflanzenheilkunde | dataset.md 1.1 |
| oligoscan | Oligoscan and Mikronährstoffe | dataset.md 1.1 |
| schilddruese | Schilddrüsen Behandlung | dataset.md 1.1 |
| homoeopathie | Homöopathie | dataset.md 1.1 |
| massage | Massagen and Anwendungen | dataset.md 1.1 |
| viriditas | Viriditas, Schule für Naturheilweisen: courses and training (second audience) | dataset.md 1.9; sitemap of danieladumann.de (122 URLs) |

Not offered: house visits (dataset.md 1.9), Colon-Hydro-Therapie, HPU, Blutegel, infusions (no source lists them).

## 2. Two audiences

- Patient audience: the practice (Berlin-Charlottenburg).
- Trainee audience: Viriditas courses and training.
- Evidence of the split: 0 of 63 rankings are for patient searches (dataset.md 1.6). All 3 visible Google reviews talk about courses (dataset.md 1.8).
- Decision for this pool: the homepage serves patients. Training items carry `audience: trainee` and `page_tag: later`.

## 3. Places

- Core place: Berlin-Charlottenburg. Address Nithackstraße 24, 10585 Berlin. Phone 030 36430358 (dataset.md 1.9).
- Neighbours seen in search data: Wilmersdorf, Westend, Schöneberg, Spandau. Volume 10, 10, no data, 70 (`03-demand/volume.json`).
- `[FEHLT]` Catchment area confirmed by the client.
- `[FEHLT]` Parking and barrier-free access.
- Conflict to resolve: herb garden in Schorfheide (dataset.md 1.9) or Schöneberg (Memory dumann-ueber-mich-page).

## 4. Brand

- Method: Hildegard von Bingen (Heilkunde, Fasten, Aderlass, Kräuter).
- Voice and visual brand: `00_project/assets/dumann/cro/02-data/brand.md`.
- Booking channel: Lemniscus booking form (primary), phone (secondary).
- Name variants: website "Naturheilpraxis Daniela Dumann", Google profile "Hildegard von Bingen Berlin Naturheilpraxis Daniela Dumann".

## 5. Proof inventory (authority)

| Proof | Status | Source |
| --- | --- | --- |
| Heilpraktikerin since 2002; Dipl.-Sozialpädagogin (FH) since 1985; Psychologische Beraterin 2011; Entspannungstherapeutin 2018 | verified | dataset.md 1.9 (/lebenslauf) |
| Vizepräsidentin Internationale Gesellschaft Hildegard von Bingen since 2023; board since 2015 | verified | dataset.md 1.9 |
| Training with Dr. Wighard Strehlow, Phytaro Heilpraktikerschule; Medizinischer Arbeitskreis Engelberg since 2004 | verified | dataset.md 1.9 |
| Memberships: Fachverband Freie Heilpraktiker, FET, MeGeMit | verified, no logo files | dataset.md 1.9 |
| Google rating 5.0, 9 reviews | verified 2026-10-11 | dataset.md 1.7 |
| Review texts | 3 of 9 visible, all about courses | dataset.md 1.8 |
| Patient testimonials with consent | none | dataset.md 1.1 (one anonymous "H.") |
| Herb garden | location unclear | dataset.md 1.9 |

Local Pack for "heilpraktiker berlin charlottenburg" (DataForSEO, 2026-10-11): Manuela Lemke 4.9 (51 reviews), Betty Timpe 5.0 (36), Angela Käßner 5.0 (13). File: `02-competitors/serp-1.json`.

## 6. Prices (verified on /behandlungen, 2026-10-11)

First consultation (60 min): 220 EUR. General consultation: 150 EUR per hour started. Homeopathic first consultation: 220–380 EUR. Billing by GebüH. Private and supplementary insured clients may get partial refund, no guarantee. Source: dataset.md 1.9.

## 7. Own search data

- Own rankings: 59 to 63 keywords, none for a patient search (`03-demand/ranked-danieladumann.de.json`, dataset.md 1.6).
- Google Search Console: the 741 service account had no access at the start (HTTP 403). Martin added `reporting-bot@studio-apis-503306.iam.gserviceaccount.com` on 2026-10-11. The export works for the property `https://www.danieladumann.de/` (not for the non-`www` address). 90 days, 2026-07-10 to 2026-10-08: 287 queries (113 clicks, hidden rare queries excluded), 63 pages (375 clicks). Files: `03-demand/gsc-api.json` (raw), `gsc-queries-90d.tsv`, `gsc-pages-90d.tsv`. A hand read in Chrome the same day (`gsc-*-chrome-2026-10-11.tsv`) matches within about 4 %.
- Local Falcon: existing scan of 2026-10-01 (SoLV 0 % for "heilpraktiker charlottenburg" and "ernährungsberatung charlottenburg"). No new scan in this run.

## 8. [FEHLT] list for the client form

1. Catchment area: which districts do patients come from?
2. Parking and barrier-free access.
3. Garden location (Schorfheide or Schöneberg) and real photos.
4. Which complaints does she want to serve? Her ideal patient.
5. Price and duration of an Aderlass. Cancellation rule. Preparation for the first visit.
6. What exactly is the Schilddrüse service?
7. Does she guide fasting for patients, or only courses?
8. Written consent for at least 3 patient quotes.
9. Release of the method text ("Mein Ansatz").
10. Logo files of the associations.
11. Six more Google review texts and the German originals.
12. One brand name for website, Google profile and directories.
13. GSC access: done on 2026-10-11 (service account added by Martin).
