# Client baseline: STÜRZL Steuerstrafrecht (Dr. Anja Stürzl)

Date: 2026-10-11. Mode: existing site (Joomla, `stuerzl-steuerstrafrecht.de`). Compliance mode: BRAO (law firm).
Rule: facts only. Every fact has a source. A gap carries `[FEHLT]`.
Sources reused (not collected again): `stuerzl-woche1-befunde-2026-10-01.md`, `stuerzl-wettbewerber-analyse-2026-10-09.md`, `stuerzl-umsetzung-backlog.md`, `stuerzl-localfalcon-kampagne-2026-10-09.md` (all in worktree `.claude/worktrees/unruffled-darwin-e68a19/00_project/`), memory `anja-stuerzl-client`. The Source-of-Truth sheet could not be read by cell (the Drive tool returns only its structure).

## 1. Services (ground truth for the fit test)

From the live site (crawl of 2026-10-11, no sitemap exists) and the onboarding call of 2026-10-06.

| Key | Service | Source |
| --- | --- | --- |
| steuerstrafrecht | Steuerstrafrecht: Verteidigung im Steuerstrafverfahren | site `/steuerstrafrecht/verteidigung-im-steuerstrafverfahren` |
| selbstanzeige | Selbstanzeigen und steuerliche Korrekturen: Beratung, Begleitung, vorherige Prüfung steuerstrafrechtlicher Risiken | site `/selbstanzeigen-steuerliche-korrekturen/…` |
| durchsuchung | Steuerfahndung: Durchsuchungsbegleitung und Schulung | site `/steuerstrafrecht/durchsuchungsbegleitung-schulung` |
| gutachten | Gutachten und Risikobewertung | site `/steuerstrafrecht/gutachten-risikobewertung` |
| zoll | Zollstrafrecht | site `/zollstrafrecht` |
| wirtschaftsstrafrecht | Sonstiges Wirtschaftsstrafrecht | site `/sonstiges-wirtschaftsstrafrecht` |
| arbeitsstrafrecht | Arbeitsstrafrecht (as search terms: Schwarzarbeit, Sozialversicherungsbetrug, unzulässige Arbeitnehmerüberlassung; "Begleitdelikte" are the USP) | site `/arbeitsstrafrecht`; call 2026-10-06 |
| korruption | Korruptionsstrafrecht | site `/korruptionsstrafrecht` |
| owi | Ordnungswidrigkeiten (Unternehmensgeldbußen, Organisationsverschulden, Steuerordnungswidrigkeiten) | site `/ordnungswidrigkeiten/…` |
| unternehmensvertretung | Unternehmensvertretung (Strafanzeigen, OWi-Verfahren gegen das Unternehmen, Verfahren gegen Mitarbeiter und Leitungspersonen, Zeugenbegleitung) | site `/unternehmensvertretung/…` |
| individualpersonen | Verteidigung von Individualpersonen (OWi, Strafanzeige, Zeugenbegleitung) | site `/verteidigung-von-individualpersonen/…` |
| compliance | Compliance (new service and tile, text from Dr. Glogger, no page yet) | call 2026-10-06 |

Most valuable mandates (call): company matters, opened proceedings, search and arrest, compliance, large Selbstanzeigen. Ads wish: Selbstanzeige, Durchsuchungsbeschluss, Steuerstrafverfahren. "Strafverteidiger" is acceptable ("wir sind ja auch Strafverteidiger").
Cost model (client text received 2026-10-11, not yet live): billing by time in six-minute units, hourly rates EUR 350 to 500 by seniority, flat fee possible in single cases, advance usually EUR 1,000 to 5,000, first consultation flat EUR 250 to 350, four-eyes principle (two lawyers per mandate), monthly invoice with activity record, no RVG. The live FAQ still shows other rates (380 to 450, 330 to 400, 280 to 350 by role). Source: `01-client/client-texte/kosten.txt`.
Compliance text received 2026-10-11 (370 words): advice on compliance systems, codes of conduct, duties of management, whistleblower protection, regulation, training; after a breach internal investigations and support towards authorities. It does not mention tax or tax compliance. Source: `01-client/client-texte/compliance.txt`.
AI use (client text received 2026-10-11): AI tools built for lawyers for file review, document analysis, research and administration. Strategy, personal care and responsibility stay with the lawyers. Place on the site is open. Source: `01-client/client-texte/ki-baustein.txt`.

Not proven as practice areas: general criminal defence, Fachanwalt für Strafrecht (not proven), general tax advice as a service. These stay out or become adjacent items.

## 2. Places

- Frankfurt: new address Untermainkai 26, 60329 Frankfurt am Main (proposed canonical, final confirmation by Florentine Jilg open). Old address Wiesenhüttenstraße 17 is outdated (move on 2026-10-05). Post and reception: Wilhelm-Leuschner-Straße 23. Garage: Wilhelm-Leuschner-Straße 27–29. Phone +49 69 298028870.
- München: Oberanger 32 (Lea Wimmer, location lead). Phone +49 89 72444170. Confirmed as a location by Martin on 2026-10-11 (the package question is closed).
- Target area: nationwide, plus London, Switzerland, Austria. Few mandates come from Frankfurt itself. Main markets: München, Frankfurt, Düsseldorf (call).
- Search volume for the city is small (about 110 per month for tax-lawyer terms in Frankfurt, memory `anja-stuerzl-client`). Local pages need more than a city name.

## 3. Brand

- Firm name: "STÜRZL Steuerstrafrecht". Keep (it is the real name).
- Team (site): Dr. Anja Stürzl, Dr. Monika Glogger, Florentine Jilg, Lea Wimmer, Jessica Weyel, Lenka Schlütter, Maria Bruckmeier, Nina Güldenring, Thorben Hoppe. The team page ranks for names of other people (Pösl, Kellner, Brunzel, Euler, Fenzl, Scherübel). `[FEHLT]` Are these former colleagues?
- Two mandate groups: private persons (Selbstanzeige, Verfahren) and companies (Unternehmensvertretung, Compliance).
- Brand voice: formal Sie. Client confidentiality is central (communication mainly by e-mail).
- Booking channel: phone and e-mail. No form, no WhatsApp. WhatsApp needs a legal check (§ 203 StGB, GDPR). Phone Monday to Friday 09:30 to 14:30 on the site. GBP says 09:00. Schema says 09:00 to 18:00. `[FEHLT]` One valid opening time.

## 4. Proof (authority)

| Proof | Status | Source |
| --- | --- | --- |
| Dr. Anja Stürzl: Fachanwältin für Steuerrecht since 2021; Zertifizierte Beraterin für Steuerstrafrecht (DAA) since 2022 | public sources, **not confirmed by her** | memory `anja-stuerzl-client` (LTO, Fürstenberg, R&W) |
| Fachanwalt für Strafrecht | not proven. Do not use | backlog 2026-10-09 |
| anwalt.de profile: 5.0 with 79 reviews | seen 2026-10-09 | backlog |
| Google Frankfurt: 5.0 with 14 reviews. München: 5.0 with 1 review | Maps 2026-10-09 | competitor analysis |
| Press mentions: 15 unlinked (LTO ×4, JUVE ×2, ZRI ×2, RWS, azur, Capital, BMF-PDF, IWW, C.F. Müller, R&W, others) | found, no link yet | findings section 10 |
| Strong FAQ: 6 pages, about 2,555 words (own site) | live, structure poor (6×H1) | `own-metrics.json` |
| Testimonials | none, and anonymity matters. No incentives, no fake reviews. The client answers reviews herself or not at all | call 2026-10-06 |

## 5. Own site (measured 2026-10-11, 25 pages)

- 49 URLs found by crawl. No `sitemap.xml` (404). Structure: 9 service areas with 17 sub pages (142 to 291 words each, all with 2×H1 and 0 H2), one strong FAQ page, team and person pages, contact, news (no H1).
- Homepage: 358 words, 1 H1 ("Kanzlei"), title "Stürzl Steuerstrafrecht – Home". `/index.php/schwerpunkte` is a 404 that the home page links to.
- Structured data: ContactPoint and GeoCoordinates on every page, LegalService on the home page (Frankfurt only). No Person, no FAQPage.
- Own rankings (DataForSEO 2026-10-11): only 18 keywords with volume. Brand and names rank #1. "anwalt steuerrecht frankfurt" #17. No service term in the top 10 except the brand. SERP check 2026-10-08: "anwalt steuerstrafrecht" #27.
- Local Falcon baseline 2026-10-01 (7×7, 5 km): "anwalt steuerhinterziehung" SoLV 63.3 %, "steuerfahndung anwalt" 22.5 %, "anwalt steuerstrafrecht" 2.0 %, others 0 to 2 %. No new scan in this run.
- Backlinks (analysis 2026-10-09): rank 122, 100 backlinks, 58 referring domains, about 40 spam domains since 07/2026.

## 6. Search Console

The 741 service account has no access (HTTP 403 on `https://`, `https://www.` and `sc-domain:`). Probably held by the IT contact. `[FEHLT: GSC access]` Old agency report of 2025-05-27: 320 clicks, 5,150 impressions in 28 days, average position 33 (from the findings file, not re-verified).

## 7. [FEHLT] list for the client form

1. Fachanwalt title: confirm "Fachanwältin für Steuerrecht" and "Zertifizierte Beraterin für Steuerstrafrecht (DAA)". Fachanwalt Strafrecht: no.
2. München is confirmed as a location (Martin, 2026-10-11). Open: contact person and services at München.
3. Final address and one valid opening time. Emergency numbers.
4. Compliance text and costs text: RECEIVED 2026-10-11. Open: tax link in the compliance text, a paragraph on legal expenses insurance (the FAQ heading says "Kosten/Versicherung", the new text is silent), wording checks (reputation, data protection claim, liability wording), place for the AI paragraph.
5. Which real topics may become advice pages? Who writes them (Dr. Stürzl or Dr. Glogger)?
6. Are the names on the team page (Pösl, Kellner, Brunzel, Euler, Fenzl) former colleagues?
7. Does the firm offer Betriebsprüfung support and general tax-law advice, or only tax-criminal matters?
8. Cases without client reference for the site (with Berufsrecht check). Sources for press mentions.
9. Opening of a contact form and a callback: consent text (GDPR, § 203 StGB).
10. GSC access for the 741 service account.
