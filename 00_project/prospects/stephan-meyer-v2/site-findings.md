# Site findings: stephanmeyer.com (agent B, 2026-10-12, 15:07 to 15:16)

Sources: `evidence/site.json`, `evidence/site-pages.json` (30 pages), `evidence/site-urls.json`, `evidence/comp-pages.json`, and own curl calls (listed per finding). No browser. No paid call.

## 1. Language versions (important for the page)
- The default site is ENGLISH. `https://stephanmeyer.com/` has `lang="en-US"`, title "Doctor Change | Dr. Stephan Meyer - Change Management Expert & Executive Coach", canonical to itself.
- A GERMAN version exists at `https://stephanmeyer.com/de/` (`lang="de-DE"`, own canonical, hreflang en/de set on both). The German page uses "du". Evidence: curl `/` and `/de/`.
- The English top pages (`/about/`, `/services/`, `/contact/`, `/keynotespeaker/`, `/vision-to-reality-workshop/`, `/sacred-cow-workshop/`) are English. The German pages sit under `/de/`: `/de/coach/`, `/de/trustedadvisor/`, `/de/business-wargaming-2/`, `/de/kontakt-2/`. `/coach/` redirects to `/de/coach/`.
- None of the `/de/` pages is in the sitemaps (`sitemap-pages.xml` has 10 URLs, none under `/de/`; `grep /de/` = 0 in all sitemap files). Google gets no sitemap hint for the German pages.
- The 500+ blog posts are German (Du or Sie) but sit at the root, next to the English pages. Language is mixed at one level. One post is English (`/10-transformational-changes-that-will-revolutionize-your-life/`).
- Consequence: a German visitor from Google can land on the English home page.

## 2. Phone, https, contact, booking
- `tel:` links: ZERO on home `/`, `/de/`, `/contact/`, `/de/kontakt-2/`, `/services/`, `/about/`, `/de/coach/`, `/de/trustedadvisor/`, `/sacred-cow-workshop/`, and the 30 blog posts checked (`evidence/site.json`: `tel_links_home: []`, `tel_links_contact: []`; `evidence/site-pages.json`: `tel_link` false on all 30). No phone number is visible in the Impressum either.
- A button "Call Me" (EN home) and "Ruf mich einfach an" (DE home, `/de/`) exists. It links to the contact page `/de/kontakt-2/`, not to a phone number. The label promises a call, the link does not call. Evidence: curl `/de/`.
- `http://stephanmeyer.com` returns 301 to `https://stephanmeyer.com/` (`curl -sIL`; `evidence/site.json`: `http_redirects_to_https: true`). OK.
- Contact page `https://stephanmeyer.com/contact/` (35 words): NO contact form. It has one button "Video Call" to `https://bookme.name/stephanmeyer/lite/contact-from-website` and a `blab-embed` script from bookme.name (booking widget). The text says "use the form below", but the only item below is the booking widget. Evidence: curl `/contact/`; `evidence/site.json`: `form_on_contact: false`.
- German contact page `https://stephanmeyer.com/de/kontakt-2/` has one `<form>`, but it is the lead-magnet form for the "Kuh Kanvas" download ("Wir spammen nicht ... Posteingang"), not a message form. It also has the same bookme.name button ("Videoanruf").
- No mailto link on home or contact. Impressum shows no e-mail and no phone: only "Almademey Limited, Anthipolochagou Georgiou Savva 26, Shop 1-2, 8201 Paphos (Geroskipou), Cyprus", VAT CY10426519O, "Vertreten durch: Dr. Stephan Meyer". Evidence: `https://stephanmeyer.com/impressum/`. The legal address is in Cyprus, not Wurzbach. The page cites "§ 55 Abs. 2 RStV", an old rule name. Flag only, no legal claim.
- Form on home: yes (`form_on_home: true`): lead magnet "Free Workbook / Cow Canvas".
- Social links go through short links `jo.my/smfg` (Facebook), `jo.my/smli` (LinkedIn), `jo.my/smtw` (Twitter), all `nofollow`.
- Speed: first byte 3.16 to 3.48 s on home (`evidence/site.json: ttfb_secs`). Slow.
- The site firewall (BlogVault) blocks fast curl series: after about 40 fast requests we got 403 "Blocked because of Malicious Activities" (e.g. `/de/kontakt/`, `/client-portal-login/`, some posts). These 403 come from our own load, not from a site fault. Other agents: use few requests.

## 3. Duplicate pages
- `evidence/site.json`: `duplicate_pages: []`. No same-title and same-words pair found in the 30 pages.
- Near duplicates by topic (sitemap titles): programmatic city posts for the same keyword. Example for Hannover: "5 Gründe, warum du Führungskräfte Coaching in Hannover brauchst" (2.998 words), "5 Gründe, warum du Coaching für Führungskräfte in Hannover in Betracht ziehen solltest" (2.190), "5 Tipps für erfolgreiches Coaching von Führungskräften in Hannover" (4.092). Sitemap URL counts by city name: München 4, Hamburg 4, Hannover 3, Berlin 3, Köln 2, Stuttgart 1.
- Slugs ending in "-2" (`/de/kontakt-2/`, `/de/business-wargaming-2/`) show copies of older pages. Not a proven duplicate.
- Home has 3 H1 elements ("Are you a visionary?", "Most visionaries", "Dr. Stephan Meyer – Outstanding in his field"). `/services/` has 2 H1. The `/de/` home has the same H1 pattern. Evidence: `evidence/site.json` (`home_h1`, `pages_two_h1: 1`), curl `/services/`, `/de/`.

## 4. Site size and kind of content
- The Squirrly SEO sitemap index lists posts, pages, categories, tags and archives. The collector counted 1.940 URLs (`evidence/site-urls.json`). `sitemap-posts.xml` shows 500 posts per page; page 2 also shows 500 (`?sitemap_page=2`). Only 10 URLs are real pages. The rest is blog, tags and categories.
- The posts look auto-generated. Image file names are `wpautoblog-image-NN.jpg` in `/wp-content/uploads/2026/10/` (`evidence/site.json: images_home`). Posts on sitemap page 1 by month: 138 (2026-02), 96 (03), 33 (04), 33 (05), 43 (06), 59 (07), 51 (08), 47 (09).
- Title pattern: "5 Gründe, warum du ... in <Stadt> ...", "10 Tipps ...", "Top 5 ...". 54 of the 1.940 URLs follow the "N Gründe/Tipps/Wege/Vorteile" or "Top N" pattern in the slug. The posts mix Du and Sie ("5 Gründe, warum Sie einen persönlichen Executive Coach brauchen").
- Post length on the 30 checked: 856 to 4.092 words, one outlier with 13.219 words (`/wie-unternehmer-die-freude-an-ihren-eigenen-herausforderungen-wiederfinden/`). Evidence: `evidence/site-pages.json`.
- Link profile (agent A, `demand.md` section 6): 63 of 1.139 referring domains have spam score 60 or more. Separate item, not a site fix.
- Money pages: home EN (2.166 words), `/de/` (2.342), `/services/` (768), `/de/coach/` (1.323), `/de/trustedadvisor/` (1.060), `/keynotespeaker/` (872), `/sacred-cow-workshop/` (1.600), `/vision-to-reality-workshop/` (508), `/de/business-wargaming-2/` (470), `/about/` (548). Word counts are main-area text from my curl; the collector counts differ a little.
- No German service page targets "führungskräfte coaching" or "business coach". `/de/coach/` has title "Coach | Dr. Stephan Meyer" and H1 "Der Coach". The only pages with the term "Führungskräfte Coaching" are blog posts. Demand: both terms 2.900 per month (`demand.md`).

## 5. Prices and packages (for the calculator)
- NO price anywhere. `price_mention` is false on all 30 pages (`evidence/site-pages.json`), and a grep for €, EUR, Preis, Honorar, Kosten on the 11 money pages finds no tariff.
- Only price-like text: "Mit einem monatlichen Pauschalbetrag" (`/de/trustedadvisor/`), no amount. "Make an appointment for a free call!" (`/services/`). "Melde dich für ein kostenloses Beratungsgespräch" (`/de/coach/`). Free items: Kuh Kanvas / workbook (lead magnet).
- Calculator: no `val` from the site. Agent E must state an assumed example value and say it is an assumption.
- Offers on the site (names for agent E): Executive Coaching, psychologisches Coaching (`/de/coach/`), Keynote Speaking (`/keynotespeaker/`), Trusted Advisor (monthly package, no price), Sacred Cow Workshop ("Our Premium Product", one day), Vision to Reality Workshop, Business Wargaming, "Fractional Change Agent" (on `/de/`).

## 6. Claims that sound like guaranteed or proven results (no HWG; he is not a health practitioner)
These are for the copy and the fact check. They are not a legal finding.
1. Home EN, meta description: "30+ years guiding leaders at VW, Audi, Novartis & more." (`evidence/site.json` / `site-pages.json`, home `meta_description`). Big brand names. Needs proof that they are true and allowed.
2. `/about/`: "Dr. Stephan Meyer generated additional millions of Euros in profit for his clients in several industries". `/de/coach/`: "... Millionen von Euro an zusätzlichem Gewinn für seine geschätzten Kunden". No case with a number.
3. `/de/` and EN home: "Hol dir den Kuh Kanvas & verkürze die Transformationszeit um 50%" / "SLASH TRANSFORMATION TIME BY 50%!". A fixed result number, no method, no source.
4. `/de/`: "Teams, die mit 40% ihres Potenzials arbeiten" as fact, no source.
5. Home EN "Your Benefits": "Increased Profit", "Peace of Mind", "Good Night's Sleep", "Higher Team Morale", "Better Work-Life Balance". Reads as a result promise.
6. `/de/trustedadvisor/`: "Erreiche deine Geschäftsziele schneller als bisher", "Steigere die Rentabilität deines Unternehmens", "er ist immer für dich da". Reads as a promise and permanent availability.
7. Home EN: "Every day without expert-guided transformation represents quantifiable value destruction your shareholders will never recover." and "... are actively digging their own graves." Fear copy, no data.
8. `/sacred-cow-workshop/`: "Only read this if you want to be successful!" and "One day now saves you months of inertia later." Result promise with a time number.
9. `/de/coach/` lists "Wem ich bereits durch psychologisches Coaching geholfen habe" with "Hochbegabten", "Profi-Fußballern", "Digitalen Nomaden". The three case studies are anonymous; the page says "Keine Hochglanz-Testimonials, keine erfundenen Erfolgszahlen" (good tone to reuse).
- Title check: the field of his doctorate is not verified here. Do not write "Psychologe" or "Psychotherapie" on the page unless he proves it. "psychologisches Coaching" is his own wording.
- Rule for the page: no new result promise. Use only proof with a number and a source.

## 7. Name conflict (open question from agent A)
- `stephanmeyer.biz` is NOT him. It is a different Stephan Meyer, a logistics consultant ("Die beste Unterstützung bei Ihren Logistikthemen", Verhandlung, Vertragsgestaltung, Transformation, LOGIVISOR Institute). Evidence: curl `https://stephanmeyer.biz` (title "Home - Stephan Meyer", 493 words). It holds rank 1 and 2 for "stephan meyer change management" (`evidence/dfs-serp-name2.json`). Do not claim it as his.
- `redner-veraenderung-psychologie.de/en/` is linked from his home (curl `/`): this is his keynote site.

## 8. Competitor page length (second pass)
Command: `python3 content-pool-skill/scripts/page_metrics.py --out prospects/stephan-meyer-v2/evidence/comp-pages.json --lang de <5 URLs>`. Result: 5 of 5 read. Evidence: `evidence/comp-pages.json`.

| # | Competitor URL | Words | H1 |
|---|---|---|---|
| 1 | https://www.fuehrungskompetenzen.com/fuehrungskraefte-coaching/ | 4.563 | Führungskräfte-Coaching mit messbaren Ergebnissen |
| 2 | https://www.kommunikationswerk.de/fuehrungskraefte-coaching/ | 1.170 | Führungskräfte Coaching – Mitarbeiter verstehen und führen |
| 3 | https://coach-und-mentor.de/ | 1.635 | Coaching & Mentoring (second H1: Susanne Schwerdtfeger \| Coach und Mentor) |
| 4 | https://dianawalther-action.coach/business-coach-jena/ | 565 | Business Coaching für Geschäftsführer in Jena |
| 5 | https://www.vorwerg.de/personalentwicklung/coaching/ | 145 | Coaching |

- Mean: 8.078 / 5 = 1.616 words. Median 1.170.
- Split: the 3 national pages have a mean of 2.456 words. The 2 Jena pages have a mean of 355 words.
- Sidebar counting: `page_metrics.py` removes `script, style, noscript, nav, footer, header, svg, form, iframe`. It does NOT remove `aside` or sidebar blocks. So counts include sidebar text, the table of contents ("Inhaltsverzeichnis" on #1), blog teasers (#3 lists 3 blog titles twice) and FAQ blocks. Treat #1 (4.563) and #3 as upper bounds. #5 (145) may be low if the text loads with JavaScript (not verified).
- His own pages on the topic: `/de/coach/` 1.323 words, `/de/` 2.342 words, posts 856 to 4.092 words. His pages are NOT shorter than the ranking pages (lesson 4). Length is not his gap. The data shows a gap in keyword match: his title and H1 do not contain "Führungskräfte Coaching" or "Business Coach", and no German service page exists for the two big terms.
- Competitor #4 shows the local pattern that ranks in Jena: H1 = service + city, sections on local firms, funding for Thuringia, FAQ, contact. Only 565 words.

## 9. Other technical points
- Dead link on home: `https://stephanmeyer.com/xmlrpc.php?rsd` returns 503 (`evidence/site.json: dead_links_from_home`). Minor.
- GA4 `G-C1N1DP2T75` and GTM `GTM-PMR2Q4J` are present. Cookie tool: iubenda (policy IDs 30883706 and 86820346 linked on home).
- JSON-LD on home: ImageObject, Person, SearchAction, WebPage, WebSite. No LocalBusiness, Organization or ProfessionalService. No FAQ markup (`faq_signal` false).
- `credential_hits` on home: "verband" only. The collector found no coach association (DBVC, ICF) in the 30 pages. Not checked by hand on `/about/`.
- `client-portal-login` is in the pages sitemap (login page, not for Google).
- Google profile data: see `evidence/google-panel-2026-10-12.md` (operator job).

## Summary for the orchestrator
1. Default site is English; German is under `/de/` and not in the sitemap. The homepage draft stays German "du".
2. No tel: link, no contact form, only a bookme.name video-call widget. The button "Ruf mich einfach an" has no number behind it.
3. No prices anywhere: the calculator needs an assumed value.
4. 500+ auto-generated blog posts (wpautoblog), city pattern, mixed Du/Sie. Money pages have no keyword in title or H1.
5. Competitor mean 1.616 words (national 2.456, Jena 355). His pages are not shorter.
6. `stephanmeyer.biz` is a different person.
