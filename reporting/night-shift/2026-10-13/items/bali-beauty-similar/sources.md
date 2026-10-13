# Sources — bali-beauty-similar

- 00_project/assets/balihealing/content-pool/05-sitetree/own-urls.txt — full list of 58 live own-site URLs (used to confirm treatment slugs exist).
- 00_project/assets/balihealing/content-pool/05-sitetree/sitetree.json — client site tree with audience tags ("beauty" vs "patient"/"both") and page/group/hub classification. Used this to identify the 10 individual Beauty-audience treatment pages (nodes ST-21, ST-211, ST-22, ST-23, ST-231, ST-232, ST-24, ST-25, ST-26, ST-27), separate from the Beauty hub (ST-20, /balihealingbeauty) and from the three grouped "Bleibt" page-groups (ST-221 facials, ST-241 injectables, ST-251 body-and-skin), which are not individually listed as single sitetree nodes but whose member URLs were confirmed live via WebFetch below.
- WebFetch https://www.balihealing.com/balihealingbeauty (2026-10-13) — confirmed live links and labels on the Beauty hub page, used to verify /hydraglofacial, /cleanseandhydratebasicfacial, /advancedfacialrejuvenation, /cellrejettreatment, /nucleofillinjection, /ppcfatreductiontreatment, /dmaemesotherapytreatment are real, currently-linked treatment pages.
- WebFetch https://www.balihealing.com/sitemap.xml (2026-10-13) — sitemap index, pointed to pages-sitemap.xml.
- WebFetch https://www.balihealing.com/pages-sitemap.xml (2026-10-13) — confirmed all 19 URLs used in similar-treatments.md (the 10 Beauty pages + 9 additional cross-linked treatment pages) are present in the live sitemap. No injection attempts found in any fetched page.

No client price, name or clinical-claim data was used in this item — only page existence, URLs and the client's own sitetree classification of which pages are "Beauty".
