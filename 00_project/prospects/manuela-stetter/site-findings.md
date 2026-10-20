# Site findings: Manuela Stetter (agent B, 2026-10-14)

Site: https://heilpraktikerin-manuela-stetter.de/ (WordPress, Elementor, Yoast, Usercentrics). Evidence: `evidence/site.json`, `evidence/site-pages.json`, `evidence/comp-pages.json`. Read only, no browser, no paid call.

## 1. Technical checks (curl)
| Check | Result |
|---|---|
| http to https | OK: `http://heilpraktikerin-manuela-stetter.de/` returns 301 to https, final 200 |
| Server wait (3 runs) | 0.16 / 0.22 / 0.23 s |
| `tel:` link | OK: `tel:+4917652099985` on home (4x) and on every page checked: `/termine-buchen/`, `/leistungen/`, `/manuela/`, `/coaching/`, `/naturheilkunde/`, `/referenzen/` (4x each). No broken tel link. |
| Contact page | None. No page with "kontakt" in the URL or menu. Menu: Willkommen, Naturheilkunde, Coaching, Leistungen, Kurse, Referenzen, Manuela, Termine buchen. |
| Contact form | No own form. `/termine-buchen/` embeds a booking iframe `conversiontoolbox.net/book/iframe/1016893508682362` (online booking) and a Brevo newsletter iframe (`sibforms.com`). Text offers booking portal, e-mail, or WhatsApp. Home has only the Brevo newsletter iframe. |
| Booking | Yes: "Termine buchen" page with online booking widget. Free 15 minute Kennenlerngespräch is named on `/termine-buchen/` and `/coaching/`. |
| Duplicate pages | `/termine/` is not a duplicate. It returns 301 to `/termine-buchen/` (canonical is right). The home CTA buttons still link to `/termine/` (extra redirect hop). Real duplicates: 4 demo pages `/title-with-an-average-of-8-9-words/` (and `-2/`, `-3/`, `-4/`), same title "Title with an average of (8/9) words", all 242 words. |
| Sitemap | `/sitemap.xml`, 28 URLs, all measured. |
| Tracking | No GA4 and no GTM id in the home HTML. Usercentrics consent banner is present. |
| Schema | 1 JSON-LD block (Yoast graph: WebPage, WebSite, Organization, BreadcrumbList, ImageObject). No LocalBusiness, no Physician or MedicalBusiness type. |
| Headings | 6 pages with two H1, 10 pages with no H1 (sitemap pages). Home has 1 H1: "Naturheilpraxis für Frauenheilkunde (HPG), Live- und Online-Coachings in Landshut, Essenbach und Umgebung". |

## 2. Sitemap clutter (agency leftovers)
- 4 demo pages "Title with an average of (8/9) words" plus `/blog/` with the same H1, and 3 demo category archives `category-1/2/3` (131 to 177 words).
- 9 author archive pages that show agency e-mail names in the title: `drtolentino@spotzer.com`, `anoble@spotzer.com`, `tduong@spotzer.com`, `prodriguez@spotzer.com`, `kzmagay@spotzer.com`, plus users "migration", "siteowner", "partner", "copywriter", "wpthemedev", "design". They are in the sitemap (28 URLs: 14 real pages and 14 clutter pages).
- Her name search shows `/blog/` at rank 3 for "naturheilpraxis stetter" (demand.md). The page is demo text.

## 3. Titles and meta descriptions
- Each page has a title that names a different single keyword, not the page:
  - `/`: "Menstruationsbeschwerden | Essenbach | Naturheilpraxis Manuela Stetter"
  - `/leistungen/`: "Schmerztherapie | Essenbach | ..."
  - `/manuela/`: "Phytotherapie | Essenbach | ..."
  - `/naturheilkunde/`: "Ernahrungsberatung | Essenbach | ..." (typo, missing "ä")
  - `/referenzen/`: "Heilpraktik | Essenbach | ..."
  - `/coaching/`: "Lebensthemen | Essenbach | Manuela Stetter"
  - `/termine-buchen/`: "Online Beratung | Essenbach | ..."
- Home meta description: "Willkommen in der Naturheilpraxis Manueal Stetter in Essenbach. Ich helfe Ihnen Menstruationsbeschwerden und andere Beschwerden zu lindern." Problems: typo "Manueal", "Sie" form while the page uses "du", grammar ("helfe Ihnen ... zu lindern"), and "lindern" is a Werberecht word (see 5).
- Mixed address: the page mostly says "du" but `/termine-buchen/` and `/naturheilkunde/` switch to "Sie" and "Ihnen" in some sentences. Mixed "Dir/Du" capitalisation.
- Contact data: the footer shows `manuelastetter@manuela-stetter.de`. The mailto link on home and the Impressum use `kontakt@heilpraktikerin-manuela-stetter.de`. Two different addresses.

## 4. Prices (for the calculator)
| Service | Price | URL |
|---|---|---|
| Kennenlerngespräch, 15 min (video or phone) | 0 € (free) | `/termine-buchen/`, `/coaching/` |
| Naturheilpraxis, Stundensatz 60 min | 150 € ("Mein Stundensatz für 60 Minuten liegt bei € 150") | `/termine-buchen/` |
| Erster Termin (Anamnese), 90 to 120 min | 150 € per hour, so about 225 to 300 € (derived, the page says "pro Stunde € 150,00") | `/termine-buchen/` |
| Folgetermine, 60 to 80 min | 150 € per hour; "bei Erstellung eines Behandlungsplans kann sich dieser Betrag entsprechend erhöhen" | `/termine-buchen/` |
| Körperorientierte Traumabegleitung, 1 hour | 150 € incl. MwSt. | `/coaching/` |
| Personal Coaching, 1 hour | 150 € incl. MwSt. | `/coaching/` |
| Hormon-Selbsttest (Hormon-Quiz) | 0 € | `/leistungen/` |
| Hormonraum (monthly membership) | 24,99 € per month, monthly cancellable | `/leistungen/` |
| Kurse (Hormon-Check, Wechseljahre Wandelzeit, Energie & Balance, Lymphsystem) | No price on the site; sold on elopage.com and myablefy.com | `/`, `/leistungen/` |
| Hormonspeicheltest (lab) | No price on the site | `/naturheilkunde/` |

Calculator value: 150 € per session is the single price for all 1:1 services. Insurance note on the page: gesetzliche Kassen pay nothing in general, Selbstzahler can claim "außergewöhnliche Belastungen" for tax.

## 5. Werberecht (HWG) quotes (neutral, no claim of illegality)
Disease names and symptom lists (URL, quote):
- `/leistungen/` list: "Myome und Zysten", "Schilddrüsenerkrankungen", "Akute und chronische Blasenentzündung", "Endometriose", "PCO / Polyzystisches Ovarialsyndrom", "Kinderwunsch", "Schlafstörungen", "Post Pill Syndrom". Intro: "Hierzu zählen:".
- `/naturheilkunde/` list "Meine Fachbereiche": same list incl. "Endometriose", "Schilddrüsenerkrankungen", "Akute und chronische Blasenentzündung". Also "Herz- und Kreislaufprobleme", "Unruhe, Depressionen und Konzentrationsschwierigkeiten".
- `/` : "Ich konnte nicht mehr schlafen. Depressionen begleiteten meinen Zyklus." and "Hilfe bei Zyklus- und Menstruationsbeschwerden, Hormonschwankungen, Schmerzen im Bewegungsapparat, Schlafstörungen und mehr".
- `/leistungen/` (Lymph course): "Herpes simplex, verstopfte Nase oder dein Stoffwechsel ist langsam wie eine Schnecke?" and "Ohne eine gesunde Basis werden immer wieder dieselben Krankheitsthemen auftauchen."
- `/leistungen/`: "Magen-Darm/Leber Galle und was haben meine Gallensteine mit einer Östrogendominanz zu tun".
- `/referenzen/` (training list): "Rheuma / Arthrose / Gicht / Fibromyalgie", "Migräne / Kopfschmerz", "Lipödem, Lymphödem".

Healing promise or success claim:
- `/` meta description: "Ich helfe Ihnen Menstruationsbeschwerden und andere Beschwerden zu lindern."
- `/leistungen/` (Hormon-Quiz): "Es sind deine Hormone." / "Welche Hormonelle Disbalance deine Beschwerden erklärt" / client quote "Es war Progesteron-Mangel!" (testimonial that names a diagnosis).
- `/leistungen/` (Lymph course): "wenn du dir gezielte Anwendungen wünschst, um deine Müdigkeit zu reduzieren, deinen Schlaf zu verbessern, deine Zyklusphasen zu erleichtern, deinen Stoffwechsel anzukurbeln" and "Basisbausteine für deine Gesundheit – die ich seit Jahren mit Erfolg nutze".
- `/` (Kurs): "Die hormonelle Dysbalance meistern mit natürlichen Boostern" and "Bye-bye Erschöpfung".
- `/referenzen/` testimonials: "findet sie eine schnelle und hilfreiche und schmerzlindernde Lösung" (Schmerztherapie, Schilddrüse, Epstein Barr), "mit großem Erfolg", "sehr schnell bei den seelischen und körperlichen Sorgen Abhilfe schaffen können", "für alle kleineren Wehwechen als auch größere eine Lösung".
- `/coaching/`: "begleite ich dich ... wieder in deine Selbstheilungskräfte zu bringen".

Title use ("Heilpraktikerin" and others):
- "Heilpraktikerin" is used correctly and the Impressum has the required block: Berufsbezeichnung "Heilpraktiker/in (verliehen in Deutschland)", BDH, Aufsichtsbehörde Gesundheitsamt Landshut, Heilpraktikergesetz.
- "Heilpraktikerin für Frauenheilkunde (HPG)" and "Praxis für Frauenheilkunde (HPG)" (`/`, H1): "Frauenheilkunde" next to the title can read as a medical specialty. The page adds "(HPG)".
- `/manuela/`: "Ich bin körperorientierte Traumatherapeutin, Life Trust Coach, Hormonexpertin". "Traumatherapeutin" is not the same title as her trained "Körperorientierte Traumabegleiterin" (`/referenzen/`, `/coaching/`). Review wording on the new page; use "Traumabegleiterin".
- `/naturheilkunde/`: "Bioidentischen Hormonen" listed as therapy. `/manuela/`: "Ich nehme selbst seit über 10 Jahren bioidentische Hormone." Hormone are often prescription-only. Reason to keep this out of the new page copy.

For the review page: one neutral "Werberecht" row, for example "Einige Sätze nennen Krankheitsnamen und Erfolgsversprechen. Das lohnt eine Prüfung." No claim of illegality.

## 6. Claims that do not match on the site
- Client count: "über 600 Frauen" (`/manuela/`, `/leistungen/` "über 600 Frauen begleitet") against "Über 400 Frauen zu hormoneller Balance begleitet" (`/leistungen/`, Hormon-Quiz signature). Use neither number without Martin's check.
- Experience: "Seit 10 Jahren führe ich meine eigene Praxis" (`/manuela/`) and "10 Jahre Praxiserfahrung". "Das ist jetzt 15 Jahre her" refers to the start of the Heilpraktiker training.

## 7. Competitor page length (evidence: `evidence/comp-pages.json`, page_metrics.py)
| Competitor URL | Words | H1 |
|---|---|---|
| https://heilpraktikerin-silviahensel.de/ | 189 | Ihre TCM Heilpraktikerpraxis in Altdorf bei Landshut |
| https://www.praxis-funktionsmedizin.de/ | 248 | (none); H2 "Ganzheitliche Gesundheit durch funktionelle und orthomolekulare Medizin" |
| https://naturheilpraxis-eigl.de/therapien-fuer-kinder/ | 587 | Therapien für Kinder |
| https://www.heilpraxis-muehleninsel.de/leistungen/ | 749 | Leistungen |
| https://www.heilpraxis-muehleninsel.de/diagnostik/ | 805 | Diagnostik (plus 4 H1: Anamnesegespräch, Klassische Untersuchung, Applied Kinesiologie, Dunkelfelddiagnostik) |

- Mean of the 5: 515.6 words (2578 / 5), range 189 to 805. Without the two Mühleninsel pages the mean of the other 3 is 341.3 words (1024 / 3).
- Sidebar counting: `page_metrics.py` removes script, style, nav, footer, header, form, iframe. It does not remove `aside` or sidebar widgets. Both Mühleninsel pages show the H2 "AUCH INTERESSANT", so their counts (749, 805) likely include sidebar text. Treat them as upper bounds.
- Her pages for comparison (site-pages.json, same method): home 477, `/naturheilkunde/` 520, `/termine-buchen/` 521, `/coaching/` 620, `/leistungen/` 1346. Her home is close to the mean (477 against 515.6). Her `/leistungen/` is 2.6x the mean. Length is not her gap; page titles and a missing Landshut service page are.
- Of the 5 competitor pages: tel link on 3, form on 1, schema LocalBusiness on 1, price mention on 1, FAQ signal on 0. No competitor page has more than 805 words.

## 8. Summary for the writer (agent E)
1. Technical base is fine (https, tel links, fast server, booking widget). No contact page, no own form.
2. Titles name one random keyword per page. The home title names "Menstruationsbeschwerden" only.
3. 14 of 28 sitemap URLs are agency demo content and author archives with agency e-mail names.
4. One price: 150 € per hour. Free 15 minute call. Hormonraum 24,99 € per month.
5. Neutral Werberecht row. Quotes in section 5.
6. Do not repeat "600" or "400 Frauen" without a check.
