# Runbooks per measure group

Each runbook turns a gap into one approved task. 21 runbooks cover the 77 measures. The catalogue field `runbook` points here.
How to use: a measure with status `missing`, `partly` or `unknown` gets a task. The agent follows the steps up to the line "STOP: approval". After Checkpoint C it continues with the steps below that line.
"Close evidence" is the proof that moves the measure to `done`. A finished task alone is not proof.

## Contents

P1: RB01 Profil-Fundament · RB02 Kategorien und Leistungen · RB03 Bilder · RB04 Beiträge · RB05 Bewertungen · RB06 Konkurrenz-Abwehr
P2: RB07 Fundament · RB08 Startseite · RB09 Dienstleistungsseiten · RB10 Standortseiten · RB11 Tools · RB12 Interne Verlinkung · RB13 Conversion · RB14 Kaufentscheidende Inhalte · RB15 Lokale Texturen · RB16 Technik
P3: RB17 Verzeichnisse · RB18 Lokales Ökosystem · RB19 Backlink-Kauf · RB20 Digitale PR · RB21 KI-Zitierung

---

## RB01 Profil-Fundament (G01 to G05)
Trigger: G01 to G05 gap. Check first: un-burning list for name, address, duplicates.
1. Read the master NAP record and the legal proof (imprint, Gewerbeanmeldung). Compare with the live GBP name and address.
2. G01: if extra words exist and no proof: write a rename task back to the legal name. If proof exists: record it, status `done`.
3. G02: confirm the address is real and eligible. Service-area firms: confirm the setting. No change otherwise.
4. G03: compare the GBP service area with the approved catchment list. Draft the new list.
5. G04: draft the tracking number plan (secondary number, consent text). Mark gate 9.
6. G05: draft the description (max 750 characters, counted by script). HWG or advertising-law check.
STOP: approval (Checkpoint C). Then Chrome edit with the manager account, one field at a time.
Close evidence: GBP read after the edit (live, dated). Gate: 1, 8, 9, 5. Hand-off: un-burning for any harm found.

## RB02 Kategorien und Leistungen (G06 to G08)
Trigger: G06 to G08 gap. Needs the audit driver result (B11.09) or a Falcon report with category lift.
1. Read the driver result. If none exists, compute category lift from the newest Falcon report (free).
2. G06: pick the primary category = driver category and main service. Write the change with the reason.
3. G07: list secondary categories for real services only. Drop extras.
4. G08: match each service to demand and to a live page. Services without a page wait on W09. Coverage beats volume.
5. Draft the service texts. HWG check for health.
STOP: approval. Then edit in Chrome (services need two save clicks, Google may rate-limit).
Close evidence: Falcon list or Maps read after the edit. Re-scan only with Martin's go. Gate: 5 (health).

## RB03 Bilder (G09 to G11)
Trigger: photo gap or last upload older than 30 days.
1. Check the client photo intake folder and the GBP photo list.
2. Write the photo brief: team, signage, lettered vehicle, real jobs. File name rule `service-district-brand.jpg`, geotag, caption loop (LOOP section 1).
3. G10: health: default `n/a` (HWG). Trades: consent log, blur plates and house numbers.
4. Prepare the upload batch (renamed files, captions).
STOP: approval and client photos. Then upload by Chrome.
Close evidence: GBP photo count and date. Gate: 5 (health).

## RB04 Beiträge (G12, G13)
1. Build a post calendar: 8 posts per quarter, own texts, no tool that posts alone.
2. Write the next 4 posts. Legal check (HWG, advertising law).
3. G13: offers only for trades. Health, law and tax: use information posts.
STOP: approval. Then post by Chrome on the calendar dates. Martin or the team posts.
Close evidence: GBP posts list with dates. Gate: 5.

## RB05 Bewertungen (G14 to G18)
1. Read B05.03, B05.04, B13.07. Read how the client asks today (client form).
2. G14: write the review request process: ask every customer, no filter. Channel: in person or paper by default. Mail or SMS only with consent.
3. G15: design the QR or NFC card with the review link. Check the link opens the form.
4. G16: OUT. If the client has a star bonus, write the replacement (goal on asks per job).
5. G17: set the target (2x leader) and the monthly check.
6. G18: write reply templates (thanks, exact service, place, brand). Health: neutral thanks only.
STOP: approval. Then the team gives the cards and the client answers reviews.
Close evidence: process document, card photo, then review pace and reply rate in the next refresh. Gate: 2, 5.

## RB06 Konkurrenz-Abwehr (G19 to G22)
1. G19, G20: open the evidence log. Only a genuine violation with a screenshot, date and the rule broken. Otherwise `n/a`.
2. G21: check that each location is real, has an address and staff. No second profile for a covered area.
3. G22: search Maps by old names and old addresses. Prove the profile is the client's own.
STOP: approval per case. Then the report or claim is filed by Martin's team.
Close evidence: filing receipt or screenshot. Gate: 6, 7. Hand-off: un-burning for own duplicates.

## RB07 Fundament (W01 to W05)
1. Run PageSpeed (mobile), the mobile screenshot check and the live-site script.
2. List fixes (plugins, images, cache). One task per fix with effort.
3. W04, W05: set up the daily canary run and the uptime check. Alerts go to Martin.
STOP: approval. Then site edits per batch (staging first when it exists).
Close evidence: new PageSpeed and a green canary log of 7 days. Gate: none.

## RB08 Startseite (W06 to W08)
1. Check the homepage against SMP section E. List gaps.
2. If the homepage needs a rebuild: hand off to `cro-homepage` with the content pool items.
3. Small gaps: write the exact text and link changes.
STOP: approval. No in-place edit of a live page for a swap (memory `page-swap-never-edit-live`).
Close evidence: live scan with all SMP E points. Gate: 5 (health).

## RB09 Dienstleistungsseiten (W09 to W12)
1. Match services and sub-services to pages (keyword to page table).
2. Missing pages: take the content pool items. Hand off to `seo-page-optimizer` (mode CREATE). Weak pages: mode AUDIT.
3. Check H1 and H2, FAQ, proof, CTA after the page exists.
STOP: approval of the page spec. Night shift may draft specs. It never publishes.
Close evidence: live page scan. Gate: 5 (health).

## RB10 Standortseiten (W13 to W15)
1. Read the catchment report and the content pool. A place page needs demand, a catchment signal and unique local facts.
2. Run the similarity check. Hand off to `seo-page-optimizer` for the spec.
3. Check the funnel depth against the approved tree.
STOP: approval. Close evidence: live scan and similarity result. Gate: none.

## RB11 Tools (W16, W17)
1. Take tool ideas from the content pool demand data. Pick one tool.
2. Write the tool spec: inputs, outputs, formula source (verified), tracking events.
3. Health: information tools only. Law and tax: public tariff only.
STOP: approval. Close evidence: tool page live, tracked, indexed. Gate: 5.

## RB12 Interne Verlinkung (W18, W19)
1. Crawl the site. Build the link graph. Compare with the board rule (home on top, service and place up to home, sub-service to both, blog to service and contact).
2. List missing and wrong links. One task per page group.
3. Set the monthly crawl diff after new pages.
STOP: approval. Close evidence: crawl graph after the change. Gate: none.

## RB13 Conversion (W20 to W25)
1. Check form, sticky CTA, tap-to-call, proof and CRM link on every money page.
2. W24: only with consent flow. Health, law and tax: off by default. Offer a callback button instead.
3. W25: map each form and call to a CRM source field.
STOP: approval. Close evidence: live test (form submit, call click, CRM row). Gate: 10, 5.

## RB14 Kaufentscheidende Inhalte (W26 to W29)
1. Collect verified prices or fee ranges from the client. Never invent a number.
2. Take decision-page topics from the content pool.
3. W29: write criteria first. Publish a guide, not a ranking of named firms, unless Martin accepts gate 11.
STOP: approval and client data. Close evidence: live page, source of each number. Gate: 5, 11.

## RB15 Lokale Texturen (W30 to W32)
1. Get real project facts from the client: place, date, result in plain words. Written consent.
2. Health: follow `hwg-fallstudien-guideline`. No healing claim, no identifiable health data.
3. W31: check each landmark on Maps. W32: rating summary and link by default.
STOP: approval and consent. Close evidence: live page with consent log reference. Gate: 5.

## RB16 Technik (W33 to W35)
1. Run the schema test and the live-site script.
2. Write the exact JSON-LD (same data as GBP). Alt texts, canonical, breadcrumbs, meta lists.
3. W35: write `llms.txt` (low priority).
STOP: approval. Close evidence: schema test and crawl. Gate: none.

## RB17 Verzeichnisse (O01 to O05)
1. Read `client_citations` and the master NAP. The master record wins over any old pack.
2. Plan by tier: core and map data first, then local, then niche. Health niche portals by hand.
3. Hand off to the Citations module (BrightLocal, aggregator pack). Check name, address and phone on each entry.
4. O05: after live, search name plus town to confirm each entry is found.
STOP: approval. Humans submit. Close evidence: `client_citations` status `live` and the search check. Gate: none.

## RB18 Lokales Ökosystem (O06 to O12)
1. Hand off to `backlink-dach` (pillar B). Fixed local priority: IHK or HWK only if the trade needs a licence, then association, then others by distance.
2. Sponsoring: the client agrees, 741 writes the mail, a human sends by Airmailer. Sponsor page carries the partner label.
3. O10: donation for a link counts as paid (gate 4).
STOP: approval per mail. Close evidence: live link with date (backlink table). Gate: 4.

## RB19 Backlink-Kauf (O13 to O16)
1. Check readiness: review pace and on-page are solid. If not, `blocked`.
2. Hand off to the `backlink-dach` buy path (pillar C). Label on every paid article. No subscription.
3. O14: monthly DataForSEO rank snapshot for client and 3 competitors. O15, O16: anchor mix and source filter.
STOP: Martin's go before any money moves. Close evidence: live paid link with label, order log. Gate: 4.

## RB20 Digitale PR (O17 to O19)
1. O17: test one channel set (Featured HARO email is English; test DACH channels and mark each verified or not).
2. O18: run the brand mention search (DataForSEO content analysis, Google quotes, Firecrawl). Draft one short reclaim mail per mention.
3. O19: run the watch on gutefrage.net, Reddit and jameda. Write a reply plan. No burying.
STOP: approval per mail or reply. Humans send. Close evidence: search log, mail log, link gained. Gate: 3. Hand-off: un-burning for harm.

## RB21 KI-Zitierung (O20)
1. Read B12 fields and the fixed prompt list (10 to 30).
2. Check entity match across site, GBP and directories. Check definition block, FAQ schema, sources block on service pages.
3. Run the monthly AI scan by rhythm (Martin's go for credits).
STOP: approval for page changes. Close evidence: scan report (scan, 60 days). Gate: none.
