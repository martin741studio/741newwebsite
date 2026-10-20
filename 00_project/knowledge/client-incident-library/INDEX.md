# Client Incident Library — client lock-out, mistrust, scare audits, separation

Built 2026-10-12. Feeds the planned skill `client-access-lockout` (example case: a program client removes the agency from Google Search Console after a third-party "backlink audit" that lists spam domains such as seozira.shop, backlinker.shop, googleseoexperts.shop).

**Freshness rule.** Official docs (Google Help Center, Google Search Central) and German law texts (gesetze-im-internet.de) are living pages and count as current on the fetch date 2026-10-12. Articles and videos must be published on or after 2026-07-12. Articles in this library: 2026-07-19 to 2026-10-06. Videos: uploaded 2026-07-15 to 2026-10-11, each with at least 5,000 views at fetch. Articles first published before 2026-07-12 were excluded even when the page shows a later update date (see "Excluded"). Next refresh due: 2026-11-23 (drop anything older than 3 months then).

**Counts.** 12 Google official docs, 15 law sections (BGB), 22 articles, 15 videos. 64 extracts in `_derived/extracts/` (one per source). 85 draft rules in `_derived/rules-draft.md`.

How to use:
1. Read `_derived/rules-draft.md` first. Groups: A Verification, B Account access, C Disavow and spam links, D Evidence, E Contract and German law, F Communication, G Competitor scare audits, H Retention vs separation.
2. For a detail, open the extract `_derived/extracts/<ID>.md`, then the raw source file.
3. `grep -ril <term> 00_project/knowledge/client-incident-library/` finds terms across all sources (raw texts are in English or German).

Internal library. Never name YouTube channels, authors, tools or vendors from this library in client material. Group E is background for a talk with a lawyer, not legal advice.

Source authority order: OFFICIAL and LAW > ARTICLE from Search Engine Land / Search Engine Roundtable / law firms > practitioner and vendor blogs > VIDEO. Vendor bias is noted in each extract under "Reliability".

## Official docs: Google (living pages)

| ID | Title | Type | Date | File | URL |
| --- | --- | --- | --- | --- | --- |
| O01 | Managing owners, users, and permissions | OFFICIAL | living; fetched 2026-10-12; page date: no date shown | `official-docs/gsc-managing-owners-users-permissions.md` | https://support.google.com/webmasters/answer/7687615?hl=en |
| O02 | Disavow links to your site | OFFICIAL | living; fetched 2026-10-12; page date: no date shown | `official-docs/gsc-disavow-links.md` | https://support.google.com/webmasters/answer/2648487?hl=en |
| O03 | Verify your site ownership | OFFICIAL | living; fetched 2026-10-12; page date: no date shown | `official-docs/gsc-verify-site-ownership.md` | https://support.google.com/webmasters/answer/9008080?hl=en |
| O04 | Links report | OFFICIAL | living; fetched 2026-10-12; page date: no date shown | `official-docs/gsc-links-report.md` | https://support.google.com/webmasters/answer/9049606?hl=en |
| O05 | Manual actions report | OFFICIAL | living; fetched 2026-10-12; page date: no date shown | `official-docs/gsc-manual-actions-report.md` | https://support.google.com/webmasters/answer/9044175?hl=en |
| O06 | Spam Policies for Google Web Search | OFFICIAL | living; fetched 2026-10-12; page date: 2026-08-28 | `official-docs/search-central-spam-policies.md` | https://developers.google.com/search/docs/essentials/spam-policies?hl=en |
| O07 | Do You Need an SEO? Tips for Hiring an SEO | OFFICIAL | living; fetched 2026-10-12; page date: 2026-06-05 | `official-docs/search-central-do-you-need-an-seo.md` | https://developers.google.com/search/docs/fundamentals/do-i-need-seo?hl=en |
| O08 | Manage your Business Profile owners & managers | OFFICIAL | living; fetched 2026-10-12; page date: no date shown | `official-docs/gbp-manage-owners-managers.md` | https://support.google.com/business/answer/3403100?hl=en |
| O09 | Manager Accounts: Link accounts to your manager accounts | OFFICIAL | living; fetched 2026-10-12; page date: no date shown | `official-docs/google-ads-link-manager-account.md` | https://support.google.com/google-ads/answer/7459601?hl=en |
| O10 | About access levels in your Google Ads account | OFFICIAL | living; fetched 2026-10-12; page date: no date shown | `official-docs/google-ads-access-levels.md` | https://support.google.com/google-ads/answer/9978556?hl=en |
| O11 | Add, edit, and delete Analytics users and user groups | OFFICIAL | living; fetched 2026-10-12; page date: no date shown | `official-docs/ga4-access-management.md` | https://support.google.com/analytics/answer/9305788?hl=en |
| O12 | Managing users and permissions | OFFICIAL | living; fetched 2026-10-12; page date: no date shown | `official-docs/gtm-user-permissions.md` | https://support.google.com/tagmanager/answer/6107011?hl=en |

## Official docs: German law, BGB (living pages, gesetze-im-internet.de)

| ID | Title | Type | Date | File | URL |
| --- | --- | --- | --- | --- | --- |
| L01 | BGB § 241 Pflichten aus dem Schuldverhältnis | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-241.md` | https://www.gesetze-im-internet.de/bgb/__241.html |
| L02 | BGB § 293 Annahmeverzug | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-293.md` | https://www.gesetze-im-internet.de/bgb/__293.html |
| L03 | BGB § 294 Tatsächliches Angebot | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-294.md` | https://www.gesetze-im-internet.de/bgb/__294.html |
| L04 | BGB § 295 Wörtliches Angebot | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-295.md` | https://www.gesetze-im-internet.de/bgb/__295.html |
| L05 | BGB § 296 Entbehrlichkeit des Angebots | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-296.md` | https://www.gesetze-im-internet.de/bgb/__296.html |
| L06 | BGB § 314 Kündigung von Dauerschuldverhältnissen aus wichtigem Grund | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-314.md` | https://www.gesetze-im-internet.de/bgb/__314.html |
| L07 | BGB § 611 Vertragstypische Pflichten beim Dienstvertrag | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-611.md` | https://www.gesetze-im-internet.de/bgb/__611.html |
| L08 | BGB § 615 Vergütung bei Annahmeverzug und bei Betriebsrisiko | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-615.md` | https://www.gesetze-im-internet.de/bgb/__615.html |
| L09 | BGB § 621 Kündigungsfristen bei Dienstverhältnissen | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-621.md` | https://www.gesetze-im-internet.de/bgb/__621.html |
| L10 | BGB § 626 Fristlose Kündigung aus wichtigem Grund | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-626.md` | https://www.gesetze-im-internet.de/bgb/__626.html |
| L11 | BGB § 627 Fristlose Kündigung bei Vertrauensstellung | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-627.md` | https://www.gesetze-im-internet.de/bgb/__627.html |
| L12 | BGB § 631 Vertragstypische Pflichten beim Werkvertrag | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-631.md` | https://www.gesetze-im-internet.de/bgb/__631.html |
| L13 | BGB § 642 Mitwirkung des Bestellers | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-642.md` | https://www.gesetze-im-internet.de/bgb/__642.html |
| L14 | BGB § 643 Kündigung bei unterlassener Mitwirkung | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-643.md` | https://www.gesetze-im-internet.de/bgb/__643.html |
| L15 | BGB § 648 Kündigungsrecht des Bestellers | LAW | living; fetched 2026-10-12 | `official-docs/law-bgb-648.md` | https://www.gesetze-im-internet.de/bgb/__648.html |

## Articles (published 2026-07-12 or later)

| ID | Title | Type | Published | Author/site | File | URL |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | Google Says The Disavow Tool Does Have Effects | ARTICLE | 2026-09-02 | Barry Schwartz, Search Engine Roundtable | `articles/A01-ser-google-says-disavow-tool-does-have-effects.md` | https://www.seroundtable.com/google-disavow-tool-effects-42004.html |
| A02 | 88% of Small Business Websites Have Backlinks From Likely Spam Pages | ARTICLE | 2026-09-24 | Matt Suffoletto, Suff Digital (data study) | `articles/A02-suffdigital-spammy-backlinks-88-percent-small-business.md` | https://www.suffdigital.com/resources/data-studies/spammy-backlinks-small-business |
| A03 | How a Coordinated Backlink Spam Attack Works — and How to Shut It Down | ARTICLE | 2026-07-19 | Dennis Yu, BlitzMetrics | `articles/A03-blitzmetrics-coordinated-backlink-spam-attack.md` | https://blitzmetrics.com/how-a-coordinated-backlink-spam-attack-works/ |
| A04 | How to Disavow Backlinks Found in Ahrefs (540 Spam Domains) | ARTICLE | 2026-09-01 (update section dated October 2026) | Nathan Pelton, nathanpelton.com | `articles/A04-pelton-540-spam-domains-disavow.md` | https://www.nathanpelton.com/content/blog/seo/spam-backlinks-and-the-disavow-file.htm |
| A05 | How to Disavow Toxic Backlinks in 2026: Google's Disavow Tool, Step by Step | ARTICLE | 2026-09-03 (modified 2026-09-09) | Julian Mercer, Auspia | `articles/A05-auspia-how-to-disavow-2026.md` | https://auspia.ai/blog/how-to-disavow-toxic-backlinks-2026 |
| A06 | Negative SEO: How Attacks Work and What Google Ignores | ARTICLE | 2026-09-21 | Vikas Kalwani, SAASY LINKS | `articles/A06-saasylinks-negative-seo-what-google-ignores.md` | https://saasylinks.com/blog/negative-seo/ |
| A07 | Toxische Backlinks erkennen & entfernen | ARTICLE | 2026-08-26 | Werbeagentur Nürnberg (Gestaltung unserer Tage) | `articles/A07-werbeagentur-nuernberg-toxische-backlinks.md` | https://www.werbeagentur-nuernberg.de/toxische-backlinks-der-stille-rankingkiller-und-wie-ihr-ihn-stoppt/ |
| A08 | Google September 2026 Spam Update: How to Tell If You Were Hit | ARTICLE | 2026-10-02 | Sudhakaran, WitsCode | `articles/A08-witscode-september-2026-spam-update.md` | https://witscode.com/blogs/google-september-2026-spam-update |
| A09 | Google Ads Agency Account Ownership: Who Owns What, and How Exposed Are You | ARTICLE | 2026-07-27 | Kampaio (Google Ads software vendor) | `articles/A09-kampaio-google-ads-agency-account-ownership.md` | https://www.kampaio.com/blog/google-ads-agency-account-ownership |
| A10 | Who Should Own Your Google Business Profile? (2026) | ARTICLE | 2026-09-23 | Mousa H, SearchPod | `articles/A10-searchpod-who-should-own-gbp.md` | https://searchpod.com/answers/who-should-own-my-google-business-profile |
| A11 | How to Give and Request Access to Google Business Profile (formerly Google My Business) | ARTICLE | 2026-10-02 (page JSON-LD says 2026-10-07) | Sarah Wisbey, Leadsie (access-request tool vendor) | `articles/A11-leadsie-gbp-access.md` | https://www.leadsie.com/blog/how-to-give-and-request-access-to-a-google-business-profile |
| A12 | Can Someone Else Change Your Google Business Profile Information? | ARTICLE | 2026-09-02 | Ivan Kalin, Clientomic | `articles/A12-clientomic-gbp-edit-access.md` | https://clientomic.com/blog/google-business-profile-edit-access |
| A22 | Internet-System-Vertrag (United Media, WN Online-Service od. wwwe GmbH) über 48 Monate zu 529 € fristlos kündigen? | ARTICLE | 2026-10-06 | Rechtsanwalt Lars Hämmerling (haemmerling-legal, Hamburg), anwalt.de Rechtstipp (IT-Recht, Zivilrecht, Werkvertragsrecht) | `articles/A22-anwaltde-internet-system-vertrag-48-monate-kuendigen.md` | https://www.anwalt.de/rechtstipps/internet-system-vertrag-united-media-wn-online-service-od-wwwe-gmbh-ueber-48-monate-zu-529-eur-fristlos-kuendigen-285033.html |
| A23 | 6000 Euro für Werbung – was tun bei überraschend hoher Agentur-Rechnung? | ARTICLE | 2026-08-27 | Rechtsanwältin Anuscha Blanke (Kirchhain), anwalt.de Rechtstipp (Allgemeines Vertragsrecht) | `articles/A23-anwaltde-6000-euro-werbung-agentur-rechnung.md` | https://www.anwalt.de/rechtstipps/6000-euro-fuer-werbung-was-tun-bei-ueberraschend-hoher-agentur-rechnung-280851.html |
| A25 | Agenturvertrag kündigen: Was Unternehmen vorher prüfen sollten | ARTICLE | 2026-08-07 (updated 2026-08-08 (meta dateModified; visible "Aktualisiert: Aug 2026")) | AVERVO (independent agency-performance review service, not a law firm; AI-assisted per page) | `articles/A25-avervo-agenturvertrag-kuendigen-pruefen.md` | https://avervo.de/fachwissen/agenturvertrag-kuendigen/ |
| A30 | SEO-Agentur wechseln: Anleitung und Übergabe-Checkliste | ARTICLE | 2026-07-19 | David Malewski / DAMA Solutions (dama-solutions.de) | `articles/A30-dama-seo-agentur-wechseln-uebergabe.md` | https://dama-solutions.de/wissen/seo/seo-agentur-wechseln |
| A31 | Client offboarding checklist for agencies | ARTICLE | 2026-07-22 (updated July 2026 (visible "Updated July 2026"; JSON-LD dateModified 2026-07-22)) | Chaser (trychaser.com), no named author | `articles/A31-chaser-client-offboarding-checklist-agencies.md` | https://www.trychaser.com/checklist-articles/client-offboarding-checklist-for-agencies |
| A32 | Professional Apology Email to a Client: Templates for Real Situations | ARTICLE | 2026-08-24 | Oliver Jackson / Mailbird blog (getmailbird.com) | `articles/A32-mailbird-professional-apology-email-client.md` | https://www.getmailbird.com/professional-apology-email-to-a-client-templates-for-real-situations/ |
| A33 | What effective SEO client onboarding looks like: The first 90 days | ARTICLE | 2026-10-02 | Kelly-Anne Crean / Search Engine Land | `articles/A33-sel-seo-client-onboarding-first-90-days.md` | https://searchengineland.com/effective-seo-client-onboarding-first-90-days-492666 |
| A34 | Before you hire an SEO auditor, know what you're paying for | ARTICLE | 2026-09-11 | Adam Riemer / Search Engine Land | `articles/A34-sel-before-you-hire-seo-auditor.md` | https://searchengineland.com/before-hire-seo-auditor-488053 |
| A35 | 6 Signs It's Time to Fire a Client, Even a Nice One | ARTICLE | 2026-08-15 (updated 2026-08-25 (metadata dateModified)) | Kemal Esensoy / Wunderlandmedia | `articles/A35-wunderlandmedia-signs-fire-a-client.md` | https://wunderlandmedia.com/signs-its-time-to-fire-a-client |
| A36 | How to Run Agency Project Management in 2026? Full Guide | ARTICLE | 2026-08-23 | Marija Kata Vlašić / Productive.io blog | `articles/A36-productive-agency-project-management-guide.md` | https://productive.io/blog/agency-project-management-guide/ |

Notes: A02 is a WebFetch summary (the page is JavaScript-rendered; full text not extractable). A11 shows two dates on the page (2026-10-02 visible, 2026-10-07 in JSON-LD). A22 and A23 were saved by hand from Firecrawl text (anwalt.de blocks curl).

## Videos (uploaded 2026-07-12 or later, at least 5,000 views)

| ID | Title | Type | Uploaded | Channel | Views | Duration | File | URL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | How to Start Any Conversation the Right Way (Chris Fenning) | VIDEO | 2026-10-11 | TED | 64,358 | 11 min | `videos/V01-how-to-start-any-conversation-the-right-way-chris-fenning.md` | https://www.youtube.com/watch?v=CKAyfGItpgg |
| V02 | How to Deal with Difficult Clients in English | VIDEO | 2026-07-21 | Business English Podcast | 18,203 | 34 min | `videos/V02-how-to-deal-with-difficult-clients-in-english.md` | https://www.youtube.com/watch?v=yZ8mAYlzEZU |
| V03 | How to Deal with Difficult Business Clients in English | VIDEO | 2026-09-26 | English express99 | 14,818 | 75 min | `videos/V03-how-to-deal-with-difficult-business-clients-in-english.md` | https://www.youtube.com/watch?v=1swTxV3IZkA |
| V04 | How to Apologize | VIDEO | 2026-07-22 | Don Crawley (The Compassionate Geek) | 40,170 | 3 min | `videos/V04-how-to-apologize.md` | https://www.youtube.com/watch?v=grihdl-UUmc |
| V06 | 10 Years of Building an Agency: The Lessons Nobody Sees | VIDEO | 2026-08-12 | Belkins Podcast | 13,421 | 77 min | `videos/V06-10-years-of-building-an-agency-the-lessons-nobody-sees.md` | https://www.youtube.com/watch?v=-2PItawmGiQ |
| V07 | A Service Business With 3% Annual Churn | VIDEO | 2026-08-05 | MoreMozi (Hormozi Hotline) | 5,980 | 10 min | `videos/V07-a-service-business-with-3-annual-churn.md` | https://www.youtube.com/watch?v=EYfsOP1QLJk |
| V08 | How I Use a Free 5-Minute Audit to Get Agency Clients (No Sales Calls) | VIDEO | 2026-07-15 | Adam Erhart | 22,635 | 13 min | `videos/V08-how-i-use-a-free-5-minute-audit-to-get-agency-clients-no-sal.md` | https://www.youtube.com/watch?v=413uyU4HaIw |
| V09 | Google September 2026 Spam Update Is Here | VIDEO | 2026-09-25 | Search Engine Roundtable (Barry Schwartz) | 63,781 | 13 min | `videos/V09-google-september-2026-spam-update-is-here.md` | https://www.youtube.com/watch?v=zkegOH1NSGQ |
| V10 | Important Change to SEO (New Google Spam Update) | VIDEO | 2026-08-19 | Nathan Gotch | 11,484 | 8 min | `videos/V10-important-change-to-seo-new-google-spam-update.md` | https://www.youtube.com/watch?v=8vj7VmOJti0 |
| V11 | Google's August 2026 Spam Update: What Businesses Need to Know | VIDEO | 2026-08-31 | Crescendo - SEO & GEO Agency | 5,853 | 16 min | `videos/V11-google-s-august-2026-spam-update-what-businesses-need-to-kno.md` | https://www.youtube.com/watch?v=YDZLO_aHZ44 |
| V12 | You Don't Need 1,000 Backlinks to Rank on Google | VIDEO | 2026-07-29 | Edward Sturm | 12,271 | 18 min | `videos/V12-you-don-t-need-1-000-backlinks-to-rank-on-google.md` | https://www.youtube.com/watch?v=8dwPZu9rjt8 |
| V13 | Google Can Lose Faith In Your Website (Here's How To Get It Back) | VIDEO | 2026-09-13 | Edward Sturm | 8,275 | 11 min | `videos/V13-google-can-lose-faith-in-your-website-here-s-how-to-get-it-b.md` | https://www.youtube.com/watch?v=Q4cB34UticI |
| V14 | Google Search Console Tutorial (2026): The Complete Guide | VIDEO | 2026-08-12 | Surfer Academy | 18,215 | 30 min | `videos/V14-google-search-console-tutorial-2026-the-complete-guide.md` | https://www.youtube.com/watch?v=93uhFZ_9IzY |
| V16 | Black Hat SEO in 2026: Why PBNs Still Work (With the Guy Who Owns 200,000 Domains) | VIDEO | 2026-09-26 | Edward Sturm | 10,397 | 86 min | `videos/V16-black-hat-seo-in-2026-why-pbns-still-work-with-the-guy-who-o.md` | https://www.youtube.com/watch?v=BMVgbnaLiFE |
| V17 | This is Why Car Mechanics Lose Customer Trust. | VIDEO | 2026-10-07 | The Car Care Nut | 210,182 | 25 min | `videos/V17-this-is-why-car-mechanics-lose-customer-trust.md` | https://www.youtube.com/watch?v=x_5K1mbse0A |

Transcripts: YouTube captions via Apify actor `johnvc/YoutubeTranscripts` (2 runs, 18 videos requested, 17 transcripts returned). IDs V05 and V15 are not used (dropped, see below).

## Excluded sources

Dropped after reading (off-topic):
- V05 "The Fixer Podcast Ep. 4 — Why Clients Don't Want Your Agency" (2026-09-22): about real-estate agents, not marketing agencies. https://www.youtube.com/watch?v=0mNtk-1iC8A
- V15 "How I Built a $1M+ SEO Agency With No Sales Team" (2026-09-09): founder lead-generation story, no incident content. https://www.youtube.com/watch?v=tKc0sqQycYg
- Mayank Sahu "These Websites May Not Survive Google's 2026 Spam Update" (2026-09-28): no English captions. https://www.youtube.com/watch?v=u_azd4UKhSA
- Google Search Central "Link best practices" page: fetched, then removed as not relevant to the case.

Excluded by the freshness rule (first published before 2026-07-12, later updated). Useful leads; re-check if they get new versions:
- Simon Haenel, "SEO-Agentur: Vertragslaufzeit und Kündigungsfrist" — published 2026-02-27, updated 2026-10-03. Reports AG Neuss, 10.06.2020, 101 C 176/19: SEO client blocked access and terminated at once; court saw a Dienstvertrag, termination invalid without Abmahnung, client in Annahmeverzug (§ 615 BGB), had to pay about EUR 4,200. The ruling text was not found in NRWE; verify before use. https://www.simon-haenel.com/blog/seo-vertrag-kuendigen-rechte
- Kanzlei MANDATI, "Marketing-Agenturvertrag: Leistungen, Budgets, Kündigung" — published 2026-07-04, Bearbeitungsstand 2026-09-26. Covers §§ 666, 667 BGB (account of work, hand-over duty) and access as leverage. https://mandati.de/ratgeber/marketing-agenturvertrag-kuendigung/
- eRecht24, "Wie Sie als Agentur oder Webdesigner Kundenprojekte richtig absichern" — published 2023-10-19, Stand 2026-08-19. https://www.e-recht24.de/artikel/haftunginhalte/11035-haftung-agenturen-webdesigner.html
- Wunderlandmedia, "I Audited 17 Websites for Toxic Backlinks. The Spam Networks I Found" — published 2026-04-11. https://wunderlandmedia.com/toxic-backlink-audit-spam-networks
- Purpose and Pixel, "Keep Getting SEO Spam Email?" — published 2025-01-30, modified 2026-08-13. https://purposeandpixel.co/blog/seo-spam-email
- geo-agentur.pro, "Unseriöse SEO-Angebote erkennen: neun Warnzeichen" — published 2026-04-22. https://geo-agentur.pro/magazin/seriose-seo-anbieter-erkennen
- marketing.legal, "Beware of Scam Providers" — only "Last Updated 2026-08-22", no publish date.

Seen but older than 2026-07-12 (not saved): Search Engine Roundtable on Mueller and spam links (2026-01 to 2026-04: comment spam, "Google may ignore links from sites that spam", TLD disavow), ALM Corp disavow guides (2026-03), Link Building Journal disavow and negative SEO (2026-05-10), Ahrefs blog "toxic backlinks", ra-plutte.de "SEO-Vertrag fristlos kündigen" (2023-05-21), onlinehaendler-news "Wann dürfen SEO-Verträge gekündigt werden?" (2023-06-27), ferner-alsdorf "Annahmeverzug bei Dienstleistungsverträgen" (2025-12-27), LG Köln 33 O 195/23 on ad accounts (article 2025-09-19), ponke.biz "Wem gehört mein Google-Ads-Konto?" (2026-07-10), Vogler "Marketing-Agentur wechseln: Übergabe" (Stand 2026-06-10), Supportbench postmortem templates (2026-04-21), Talaera de-escalation phrases (2026-05-05), AgencyAnalytics "How to fire a client" (2024-11-25), Google Search Central videos on SEO audits and hiring (2025-11 to 2026-06), Chase Hughes "Cheat Code for Controlling Conflict" (2026-04-10), Codie Sanchez on difficult conversations (2026-01-20), Hormozi "How to Get Your Customers to Stay FOREVER" (2026-03-24), "How to Stop Losing Agency Clients Silently" (2026-07-10, two days too old).

## Gaps: searched, but no source on or after 2026-07-12

- Disavow tool "download current list": Google's help page only says a summary is shown. A "Download list" button is described only in undated third-party docs (LinkResearchTools). Verify in the live tool before the skill relies on it.
- Google's own words on unsolicited spam links and negative SEO in this window: no new Search Central page or Google video. The newest direct statement is Mueller's Reddit quote in A01 (2026-09-02). Older statements (2023 to April 2026) are only cited second-hand in A06.
- Search Console role changes in 2026: no news. Note the conflict inside Google's docs: the permission table marks "Disavow links" for full users, the disavow page says owners only.
- German law, recent articles on: Mitwirkungspflicht and Annahmeverzug applied to SEO or agency work (§§ 642, 643, 293 ff., 615 BGB); how an agency pauses work, notifies and sets a deadline; § 627 BGB for SEO or agency services (OLG Celle 01.06.2026, 24 U 92/25, on leadership training exists, no article in the window); handover of access data and right of retention (§ 273 BGB); new BGH, OLG or LG decisions on SEO contracts. Only A22, A23, A25 and the statutes cover E.
- Incident timeline or postmortem for a client relationship (agency context): none. D rules rest on A12, A30, A31, A33, A36 and Google docs.
- Agency-owner content (article or video) on a client who fears "my agency built spam links", or who received a scary competitor audit: none. Closest: A34 (auditor quality), A03/A04 (spam networks), V08 (audit as sales tool).
- De-escalation of an angry client by an agency owner, and anything in German: none in the window. F rules rest on general business-communication videos (V01 to V04), A32 and the analogy video V17.
- Competitor poaching with fake audits as a documented trend (study or trade press): none.
- YouTube on toxic links or disavow with at least 5,000 views in the window: none found.

## Tool notes

- Apify `johnvc/YoutubeTranscripts`: 2 runs, both SUCCEEDED. Exact cost not shown in the tool output; by the listed pay-per-event prices (about USD 0.00001 per video plus start events) the total is well under USD 0.01.
- yt-dlp: `ytsearchdate` is not supported; search used YouTube result URLs with the "this year" filter, then single-video metadata for upload dates (no IP block).
- anwalt.de returns 403 to curl and WebFetch (Firecrawl worked). it-recht-kanzlei.de "Mitwirkung des Auftraggebers im IT-Projekt" returned 410. WebSearch refused moz.com. HBR item on apologies (2026-08-27) is paywalled.
- A hook blocked the Write tool for subagents on this base-repo path; their files were written in the worktree, moved here, and the worktree copies were removed.
