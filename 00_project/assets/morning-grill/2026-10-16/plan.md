# Plan 2026-10-16 (Morning Grill)

## Walk queue (1–5 min clicks for Martin)
- [ ] STÜRZL Steuerstrafrecht: Audit findings check — [findings.json](file:///Users/martindrendel/741website/00_project/assets/audit/stuerzl/2026-10-11-kickoff/findings.json)
- [ ] STÜRZL Steuerstrafrecht: CRO prototype check — [index.html](file:///Users/martindrendel/741website/00_project/assets/stuerzl/cro/07-prototype/index.html)
- [ ] STÜRZL Steuerstrafrecht: Content Pool report — [content-pool-report.html](file:///Users/martindrendel/741website/00_project/assets/stuerzl/content-pool/05-report/content-pool-report.html)
- [ ] STÜRZL Steuerstrafrecht: CRO Track B Briefbogen (Variante B 38/44)
- [ ] Praxis Hüwel: Content Pool report — [content-pool-report.html](file:///Users/martindrendel/741website/00_project/assets/huewel/content-pool/05-report/content-pool-report.html)
- [ ] Praxis Suriya: Content Pool report — [content-pool-report.html](file:///Users/martindrendel/741website/00_project/assets/suriya/content-pool/05-report/content-pool-report.html)
- [ ] 741 Night result 1: Brasse FAQ live check — [summary.md](file:///Users/martindrendel/741website/reporting/night-shift/2026-10-14/items/brasse-faq-live-check/summary.md)
- [ ] 741 Night result 2: Dumann dashboard draft — [summary.md](file:///Users/martindrendel/741website/reporting/night-shift/2026-10-14/items/dumann-dashboard-items-draft/summary.md)
- [ ] 741 Night result 3: Hüwel GBP round 2 draft — [summary.md](file:///Users/martindrendel/741website/reporting/night-shift/2026-10-14/items/huewel-gbp-round2-draft/summary.md)
- [ ] 741 Night result 4: Johni access replan — [summary.md](file:///Users/martindrendel/741website/reporting/night-shift/2026-10-14/items/johni-access-replan/summary.md)
- [ ] 741 Night result 5: Kamil Oberhausen audit — [summary.md](file:///Users/martindrendel/741website/reporting/night-shift/2026-10-14/items/kamil-oberhausen-audit/summary.md)
- [ ] 741 Night result 6: Suriya backlink checkpoint 1 — [summary.md](file:///Users/martindrendel/741website/reporting/night-shift/2026-10-14/items/suriya-backlink-checkpoint1/summary.md)

## Praxis Suriya — 28 Directory Confirmation Emails (Inspection List)
*Note: Inspection reveals automated regex captured SpamAssassin/unsubscribe headers for several rows; genuine verification links highlighted below.*

| # | Directory / Sender | Subject | Captured Link / Action | Status / Note |
|---|---|---|---|---|
| 1 | dtme.de | Anfragebestätigung | [Bestätigungslink](https://www.dtme.de/ihr-eintrag/bestaetigung-gewerblich/?optin=MTc4NzczNjI3OTQ2Nzk3Mzg0MA==) | Real verification token |
| 2 | trustpilot.com | Activate your Trustpilot account | [Activate](https://authenticate.trustpilot.com/activate-account/3_NR4dV4S5CftNOym_vlv=) | Real activation link |
| 3 | trustpilot.com | Activate your Trustpilot account | [Activate](https://authenticate.trustpilot.com/activate-account/4UCAQqnERpOEssKgEx9O9=) | Real activation link |
| 4 | yelp.com | Bestätigen Sie Ihre E-Mail-Adresse auf Yelp | [Yelp Confirm](https://biz.yelp.de/login/passwordless/redirect/MLA4c90867fd31144b0831b06561617f784?return_url=%2Fwelcome%2F642f733efd9f4c539ee8c2986070742a%2Fconfirm_new%3Futm_content%3D) | Real verification link |
| 5 | centralindex.com | Bitte bestätigen Sie Ihre E-Mail-Adresse | [Hotfrog Set Password](https://admin.hotfrog.de/login/set-password?token=3Df0f89355643582fdb5a98e8=) | Real verification token |
| 6 | centralindex.com | Bitte bestätigen Sie Ihre E-Mail-Adresse | [Hotfrog Set Password](https://admin.hotfrog.de/login/set-password?token=3Df0f89355643582fdb5a98e8=) | Duplicate/Second request |
| 7 | cylex.de | 025375 - Cylex ‘Benutzerregistrierung’Passcode | Passcode: `025375` (Mail body) | Email body contains passcode |
| 8 | cylex.de | Willkommen bei der Cylex Community! | Mandrill transactional mail | Needs body check |
| 9 | 11880.com | Ihr Eintrag auf unserem Portal 11880.com | Regex captured spamassassin header | Check raw body in Supabase |
| 10 | werkenntdenbesten.de | Ihr Eintrag auf unserem Portal werkenntdenBESTEN.de | Regex captured spamassassin header | Check raw body in Supabase |
| 11 | gelbeseiten.de | Bestätigen Sie Ihren Eintrag bei Gelbe Seiten | Unsubscribe help link captured | Check raw body in Supabase |
| 12 | opendi.com | Ihr Eintrag im Stadtbranchenbuch | RBL header captured | Check raw body in Supabase |
| 13 | opendi.com | Ihr Eintrag im Stadtbranchenbuch | DNSWL header captured | Check raw body in Supabase |
| 14 | foursquare.com | Here is your signup code! | Spamassassin header captured | Signup code in mail body |
| 15 | foursquare.com | Here is your signup code! | Spamassassin header captured | Duplicate signup mail |
| 16 | transactional.tomtom.com | Vorgang erfolgreich! Ihr TomTom-Konto aufrufen | Spamassassin header captured | Account created confirmation |
| 17 | emails.tomtom.com | Wie Blitzerwarnungen dich auf dem Laufenden halten | Unsubscribe link | Marketing mail (skip) |
| 18 | winlocal.de (x8) | Diverse Marketing & Webinare | Winlocal Hubspot Marketing | Marketing mails (skip/handle=true) |
| 19 | trustpilot.com (x4) | Sign in to Trustpilot Business | Generic sign-in notifications | Info mail |

## Today's Plans by Client

### 1. Praxis Hüwel
- **Today:** GA4 key events created & verified live (phone_click, email_click, whatsapp_click, generate_lead); portal dashboard deployed.
- **Next:** Martin eye-check on Content Pool report; GBP round 2 content draft review.

### 2. Maria Brasse
- **Today:** Copy & FAQ updates live on `/ueber-mich-maria-brasse/` and `/feng-shui-garten/` via Novamira REST API; desktop & mobile visual verification proofs attached; dashboard feed deployed.
- **Next:** Dispatch daily update email draft to `kontakt@shuiguru.de` (Martin in CC) upon final nod.

### 3. Praxis Suriya
- **Today:** Dinakar tasked via Resend with Footer Link fix (Impressum + Datenschutz); Tantri to be briefed on real directory verification links once Martin clears the list.
- **Next:** Monitor Dinakar execution; DataForSEO IP whitelist unblock for Backlink DACH.

### 4. Daniela Dumann
- **Today:** Release Wave 1 approval cards (E4, E8-E11, E22, E23 + E1-E3, E5-E7) to client dashboard in Supabase.
- **Next:** Waiting for Martin to click "Publish" in Wix for the 3 saved subpage fixes.

### 5. STÜRZL Steuerstrafrecht
- **Today:** 4 workflow results placed in Martin's walk queue.
- **Next:** 5 portal decision cards open (E1, E5, E7, E8); follow up on client Google Ads access.

### 6. Bali Healing
- **Today:** Monitor Google account identity verification review (NIB upload).
- **Next:** Reminder to top up Google Ads account with GoPay (~IDR 500,000).

### 7. Kamil Böyük
- **Today:** Clean up analysis of hacked `physiotherapiekraft.de` and full scan of Oberhausen site.
- **Next:** Review draft security/backup yearly offer (€500/yr).

### 8. Johni Jaya Motor
- **Today:** Re-plan of 25 overdue tasks; 7 decision cards open in portal.
