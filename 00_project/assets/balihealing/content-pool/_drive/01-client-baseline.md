# Client baseline: Bali Healing (Natural Health Center and Beauty Clinic, Canggu)

Date: 2026-10-11. Mode: existing site (Wix, `www.balihealing.com`, 58 URLs in the sitemap). Compliance mode: none. Reason: Indonesia has no HWG. The client rules and the Google health policy apply instead (section 3).
Rule: facts only. Every fact has a source. A gap carries `[FEHLT]`.
Sources reused (not collected again): the client audit of 2026-10-11 (`01-client/audit-reused/`: `findings.json`, `keywords.json`, `competitors.json`, `gbp-read-2026-10-11.json`, `backlinks-summary-2026-10-11.json`). Field ids like B05.06 point to `findings.json`.

## 1. Services (ground truth for the fit test)

Source: the sitemap of 2026-10-11 and the Google profile (about 19 services under the main category).

| Key | Service | Pages (own site) |
| --- | --- | --- |
| skintag | Skin tag, wart and mole removal | `/skintagandmoleremoval` (740 words) |
| dermatoscopy | Dermatoscopy (skin and mole check) | `/dermatoscopy` (175 words) |
| ozone | Ozone therapy: major and minor autohemotherapy, insufflation, hyperbaric | `/ozonetherapy`, `/ozone-hyperbaric-major-autohemotherapy`, `/ozone-minor-autohemotherapy`, `/ozone-insufflation` |
| iv | IV infusions | `/infusions`, `/infusionstreatment` (the pages `/iv-drip-therapy-infusions` and `/acupuncture` are set to noindex, B06.03) |
| acupuncture | Acupuncture and Traditional Chinese Medicine | `/traditional-chinese-medicine-consultations`, `/about-traditional-chinesemedicine` |
| osteopathy | Osteopathy | `/osteopathy-treatment`, `/about-osteopathy` |
| physio | Physiotherapy (incl. prenatal) | `/physiotherapy`, `/about-physiotherapy` |
| cranio | Craniosacral therapy | `/craniosacral-therapy`, `/about-craniosacraltherapy` |
| theta | ThetaHealing | `/thetahealing-treatment` |
| naet | NAET allergy treatment | `/naet-allergytreatment`, `/about-naet-allergy-treatment` |
| hypnotherapy | Clinical hypnotherapy | `/clinical-hypnotherapy`, `/about-clinicalhypnotherapy` |
| reiki | Reiki, Access Bars | `/reiki-sessions`, `/access-bars-therapy` |
| neural | Neural therapy, Prolozone | `/neural-therapy`, `/prolozone-injection` |
| womens | Women's health, gyneco-aesthetic consultation | `/gyneco-aesthetic` |
| facials | HydraGlo, basic facial, advanced rejuvenation | `/hydraglofacial`, `/facial`, `/cleanseandhydratebasicfacial`, `/advancedfacialrejuvenation` |
| microneedling | Microneedling, PRP face and hair | `/microneedling-collageninductiontherapy`, `/plateletrichplasma-face`, `/plateletrichplasma-hair` |
| injectables | Hyaluronic acid, Nucleofill, DMAE mesotherapy, intramuscular shots | several |
| bodyskin | Acid peeling, CellreJet, PPC fat reduction | several |
| beautyhub | Beauty clinic with dermatologist consultations | `/balihealingbeauty`, `/beauty-consultations` |

**Given up by the client on 2026-07-30 (B01.05):** naturopathy and live blood analysis (reason: the licence question for foreign practitioners). The pages `/naturopathyconsultations` and `/about-naturopathy` are still live and the Google profile still lists both (B13.05). This conflict goes to Martin as a decision.
**Priorities from the client notes (B01.05):** ozone, IV, skin tag and mole removal. On 2026-08-27 the focus moved from ozone to skin tag and mole removal.
**Not proven as services:** Botox and fillers, sound healing, screaming therapy, a mobile IV home service, general practice, Bali belly care. They stay out or become adjacent items.

## 2. Places and audience

- One address: Jalan Pantai Batu Bolong No.117X, Canggu, Kuta Utara, Badung, Bali 80361. Apple Maps shows "No. 117" and the old domain `balihealing.org` (B13.02, B12.03).
- Two Google profiles at the same address by design: "Bali Healing Natural Health Center and IV Drip Therapy" (4.7 stars, 100 reviews) and "Bali Healing Beauty Clinic" (5.0, 10 reviews). A third profile "Bali ThetaHealing" (5.0, about 20 reviews) lists `balihealing.com` as its website. Ownership is open (B05.02).
- Audience: English-speaking expats and visitors in Canggu, Uluwatu, Seminyak, Ubud (B04.01). GA4 top countries over 7 days: Indonesia, Australia, USA, Singapore.
- One location, so no area pages (B06.04). Areas are named in text.
- Hours: Mon-Fri 09:00-17:00, Sat 09:00-13:00, Sun closed (profile and site agree, B10.09). Booking: WhatsApp only. The site shows no phone number (B06.02).

## 3. Brand and rules

- Name: "Bali Healing". Two sides: Wellness and Beauty. Google name and site name differ and the profile name changed twice in two months (B13.03, B06.05).
- Brand search is large: 47 listed queries with 6,005 impressions and 582 clicks in 90 days (`gsc_groups.brand`).
- Taboos from the notes (B08.03): no country references (no "German", no "CE-certified German"), no disease promises (Google health policy). Frame the team as "Indonesian doctors and nurses" and "certified medical professionals".
- Contacts on the client side: Peggy and Pasha. Approver is not set (B08.02).

## 4. Proof (authority)

| Proof | Status | Source |
| --- | --- | --- |
| Google 4.7 stars, 100 reviews (Natural Health Center) | seen 2026-10-11 | B05.03 |
| "Over 20 years of serving Bali", "serving Bali since 2006" | on the home page and about page | page measures; profile opening date 20 May 2006 |
| Testimonials block | on the home page and about page, no source named | page headings |
| Team, doctors, licences | not on the home or about page, `[FEHLT]` | page headings |
| Reviews that name a service | 5 of 7 inspected | B10.10 |
| Owner replies to reviews | none in 7 inspected | B05.04 |
| Press mentions | none checked | `[FEHLT]` |
| Directory listings | none recorded in the portal | B07.02 |

## 5. Own site (measured 2026-10-11, 58 pages)

- Home page: 452 words, the same H1 twice, title "Holistic Health & Beauty in Bali | Bali Healing Center". No FAQ block, no price, no phone link.
- 58 own pages measured. None of them states a price. Pages come in pairs: a short "about" page and a long "treatment" page (for example `/about-osteopathy` 396 words and `/osteopathy-treatment` 899 words). Several short pages are under 200 words.
- Index status (Search Console, URL prefix, 2026-10-08): 43 pages indexed, 52 not (24 noindex, 4 not found, 3 redirects, 21 crawled or found but not indexed) (B06.06).
- Own rankings (DataForSEO 2026-10-11): 48 keywords with volume. Mostly brand and generic "healing" terms.
- Local Falcon (7x7, 5 miles, Canggu): ozone therapy 34.7 percent (down from 57.1 on 21.09), IV drip 0, skin tag removal 0, acupuncture 2.0, naturopath 71.4 (B05.06, B05.08). No new scan in this run.

## 6. Search Console

The 741 service account reads the property `https://www.balihealing.com/` (the non-www and the domain forms return 403). Export of 2026-10-11 covers 2026-07-11 to 2026-10-09: 300 queries (874 clicks, 12,876 impressions) and 56 pages (1,838 clicks, 49,078 impressions). Files: `03-demand/gsc-api.json`, `gsc-queries-90d.tsv`, `gsc-pages-90d.tsv`. Page clicks exceed query clicks because Google hides rare queries.

## 7. [FEHLT] list for the client form

1. Price range per treatment (skin tag, IV drip, ozone, acupuncture, facials). No page shows a price today.
2. Doctors and practitioners: names, licence type, years, photos with consent (the licence topic makes this the most sensitive point).
3. Is EBOO the same as the hyperbaric major autohemotherapy?
4. Home visits for IV drips: yes or no. Bali belly service: yes or no. General care: yes or no.
5. Breathwork, sound healing, screaming therapy: offered or not?
6. Botox and fillers: offered or not?
7. Naturopathy and live blood analysis: remove from site and profile, or reinstate?
8. Is "Bali ThetaHealing" a profile of the client?
9. Typical WhatsApp reply time, one phone number, parking and step-free access.
10. Payment methods, languages spoken, insurance receipts.
