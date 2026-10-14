# 741 Digital Solutions — Full External-Access Inventory
Compiled 2026-10-14 from every client memory file, workflow skill, and `.secrets`/`.env` filename. For granting/logging in once on 741-agents-01 instead of hitting blockers one at a time.

## Section 1 — Per-client platforms needing a login (18 clients)

| # | Client | Platform/CMS | GBP Google account used | Other logins needed | Access method |
|---|---|---|---|---|---|
| 1 | Praxis Hüwel (Nürnberg) | Only Inside KMS (`system.only-inside.de`, login `info@praxis-huewel.de`) — site content; live site now on GitHub Pages (`martin741studio/martihuewel`) | 741studio18@gmail.com | GA4 (2 IDs: G-1HNCRNLJD4, G-4FP95Y92XY), GSC, Resend domain key, Supabase portal login `info@praxis-huewel.de` | Only Inside = browser-login-only (password not yet filled in vault); GitHub Pages = git push; GA4/GSC = browser + partial API |
| 2 | Praxis Suriya / Coralie (Ingelheim) | WordPress via Novamira MCP `novamira-suriya-praxis-de` — currently **Connection Failed**, blocks work on day one | 741studio18@gmail.com | GTM-K9MDDN7P, GA4 G-B93S7ZWNNR, Local Falcon, BrightLocal citations (Campaign 994242), Supabase vault | Novamira = MCP (broken, reconnect needed); GA4/GTM/GBP = browser |
| 3 | Anja Stürzl / STÜRZL Steuerstrafrecht (Frankfurt) | Joomla (SP Page Builder), hosting Artfiles (`.secrets/stuerzl-artfiles.env`) | 741studio18@gmail.com | GTM-WFPFSTK2, GA4 G-FCG9RTJ1YQ, GSC (reporting-bot API), Google Ads (new account to create under anja.stuerzl@googlemail.com), Joomla Super-User | Artfiles = .env creds; Joomla/GA4/GTM/GBP = browser; GSC = API |
| 4 | Daniela Dumann (Berlin) | Wix (site-id fcffbbcc-f49e-4a44-a024-f18305120464) — Wix MCP + browser editor | 741studio18@gmail.com | GA4 G-3NTQVLCFG0, GSC, BrightLocal campaign 1006954, Local Falcon, Supabase login `daniela.dumann@live.de` | Wix = partial API + browser editor; GBP = Local Falcon write-API; BrightLocal = browser |
| 5 | Aydan Adel (Bonn, prospect) | Jimdo (live site) — CRO prototype only | n/a | n/a | No production access held |
| 6 | Maria Brasse / ShuiGuru (Berlin) | WordPress + Novamira MCP `novamira-shuiguru-de` | Not yet confirmed/invited — unverified, no GA4 tag found | Supabase login `kontakt@shuiguru.de`; WP admin login never actually handed over | Novamira = MCP; WP admin = browser, pending handover |
| 7 | Rabenmütter Shop / Franziska Poerschmann | Shopify (`rabenmuetter-shop.myshopify.com`) | not central to this business | Shopify Admin API token (write_products,write_content), GA4 (Editor-only, no API grant), GSC domain property, Supabase login `fp@rocket-libri.com` | Shopify = **API key exists** (`SHOPIFY_ADMIN_TOKEN`); GA4/GSC = browser |
| 8 | Rocket Libri / Franziska Poerschmann (2nd brand) | Migrating Jimdo → Wix (`rocket-libri.com`) | n/a yet | n/a yet | Browser-login-only once live |
| 9 | Kamil — Physio Anatomie GmbH (Oberhausen) | WordPress via Novamira CLI profile (OAuth token in macOS keychain) | 741studio18@gmail.com (GA4 "741 Clients") | Google Ads 992-981-4693 "Kamil Physio", GA4 G-LGVVEBHS8D (shared), GTM-TBPCSH3W | Novamira = CLI/OAuth token (keychain); Ads/GA4/GTM = browser |
| 10 | Kamil — Physiotherapie Kraft (Gelsenkirchen) | WordPress — **second Novamira connection NOT yet set up**; site had an active casino-spam injection to clean | 741studio18@gmail.com | Shares Ads account + GA4 property above, GTM-TBPCSH3W | Novamira connection missing; browser-only until then |
| 11 | Johni Jaya Motor (Jakarta) | WordPress (Elementor v4) via Novamira MCP `novamira-johnijayamotor-c` | 741studio18@gmail.com | GA4 G-XVWBX0VCMM, old tag G-XZCKK6Z6BJ (not ours), GSC (zero-UI API pattern), Supabase login `hello@johnijayamotor.com` | Novamira = **MCP/API key exists**; GA4/GSC = API; GBP = browser |
| 12 | Bali Healing Center (Canggu) | Wix | 741studio18@gmail.com (Local Falcon) | GA4 G-773QRR6N6H (**service-account has NO access** — gap), Google Ads, Meta Pixel 988920643729775, GTM-NML2TSVQ, Local Falcon | Wix = Chrome-automation, partly blocked; Ads/GBP = browser |
| 13 | Taxi-Zentrale Nürnberg | Joomla 5 (Helix Ultimate + SP Page Builder), hosting via Werbeagentur Bamberger | n/a | **Plaintext FTP creds in a non-.secrets script** (`~/.gemini/antigravity-ide/.../upload_preisrechner.py` — flag: migrate to `.secrets/`), Akeeba Backup Pro + Admin Tools Pro (akeeba.com, license keys Martin-only), GDPR plugin (storejextensions.org), RSForm! Pro (rsjoomla.com, Daniel's license) | FTP = credential file exists but in the wrong place; Joomla admin = browser; 3 vendor accounts = browser, license keys only |
| 14 | Tacheles (white-label via Denise/dlackner.com, end client Miriam) | WordPress/Elementor + WooCommerce, ~55 pages | n/a | WP admin (Dinakar's, white-label — client never told) | Browser-login-only |
| 15 | Marcel Rosenbach — NLP Practitioner funnel | Skool (skool.com/deep-nlp), deep-nlp.com on Thrive Architect/WordPress | n/a (not local-SEO) | Skool, Pipedrive, Zapier (paid, Zap 378535838), KlickTipp Enterprise (341498) — all via **LastPass-shared creds**; Pipedrive now via Zapier-MCP; Tally forms | Browser-login-only via LastPass, except Pipedrive via Zapier-MCP |
| 16 | Pauspapier / Michael Ehlers / me&you | WordPress (`der-rhetoriktrainer.de`) + Framer (`meandyou.de` — **no access yet, requested from Tajan**) | GBP "Institut Michael Ehlers GmbH" — not yet 741-managed | Close CRM + Airtable, ActiveCampaign, Ablefy + Memberspot, Skool, Superchat + ManyChat, Calendly, ProvenExpert, 2× Typeform, Meta Ads Manager (**gap, requested**), Wistia (**gap, requested**) — all in a shared "Zugänge" Google Doc with plaintext passwords | Browser-login-only; 741 explicitly does not log in without Martin's go each time |
| 17 | Meerblick / Klaus-Dieter Sachs (partner prospect) | Only Inside Baukasten (`agentur-meerblick.de`) | n/a | n/a | No access held — prototypes only |
| 18 | Talkinfive / Celine Rosalina Herry | Static site, hosted on 741's own cPanel VPS | n/a | FTP (`deploy@talkinfive.com`, in `.env`), GoDaddy DNS (owner unclear), Meta Pixel 1056153443797320 (**owned by "Billy", not 741**), Calendly (**owned by Celine**) | FTP = .env creds; Pixel/Calendly = not 741-owned, no login held |

## Section 2 — Shared/internal tools needing one login each

| Tool | Used for | Account / login | Access method |
|---|---|---|---|
| Google Workspace master account | GBP management (37+ profiles), GA4 "741 Clients" (36 properties), Google Ads manager, Local Falcon, Search Console switching | `741studio18@gmail.com`, `authuser=` check required every time (hard rule) | Browser-login-only |
| **Local Falcon** | Maps-rank scans + GBP read/write for almost every local client | `741studio18@gmail.com`, Starter plan | **MCP key exists** (`LF_API_KEY`); REST API not on this plan |
| **ChatGPT** | CRO Homepage mockup generation | Martin's personal ChatGPT, via Claude in Chrome | Browser-login-only |
| **LinkedIn** | Outreach pipeline / LinkedIn CRM | Martin's own login; claude-in-chrome hard-blocks linkedin.com navigation | Browser-login-only, constrained |
| **BrightLocal** | Citation-builder submissions (Coralie, Dumann, more planned) | Martin's own account, paid personally | Browser-login-only |
| **DataForSEO** | SERP/keyword/backlink data, almost every workflow | `.secrets/dataforseo.env`, IP-whitelist required | **API key exists** |
| ~~Zapmail~~ | RETIRED (Martin 14.10.: "we are not even using anymore") | n/a | n/a |
| **Smartlead** | Cold-email sending/warmup | user_id 14511 + API key | **API key exists** (needs a User-Agent workaround) |
| **Porkbun** | Domain registrar, 12 cold-email domains | Martin's account | Dedicated MCP connector, API available |
| **Zapier** | Several client automations | Zapier-MCP, OAuth | **MCP/OAuth** once authorized |
| **LastPass** | Shared vault for Marcel Rosenbach's stack | Browser extension | Browser-login-only |
| **Airmailer** (desktop app) | ALL outbound email except portal-transactional (hard rule) | Native macOS app | App login, computer-use only |
| **Resend** | Transactional/portal email | `RESEND_API_KEY` + per-client keys | **API key(s) exist** |
| **cPanel** (741's own VPS) | Talkinfive, 741.studio, listings catch-all, FTP | `.secrets/cpanel.env` | **API token exists** |
| **Supabase** (portal + leads) | Client portal, newsletter, citations | `.secrets/standup.env` + service-role keys | **API/service-role key exists** |
| **GSC/GA4 service account** | Automated reporting (where granted) | `.secrets/ga-sc-reporting-bot.json` | **API key exists** |
| **PageSpeed Insights** | Site performance checks | `.env` key | **API key exists** |
| **YouTube API** | 741 channel / thumbnails | `.secrets/youtube-api.env` | **API key exists** |
| **Telegram** (741 bot) | Canary alerts, standup | `.secrets/telegram-741.env`, `.secrets/canary-telegram.env` | **API token exists** |
| **Meta/Facebook** (741-side) | Ads reporting access | `.secrets/meta-741.env` | **API credentials exist** |
| **Apify** | Transcript/scraping workflows | `.secrets/apify.env` | **API key exists** |
| **IMAP listings inbox** | Citation confirmation-email polling | `.secrets/listings-imap.env` | **IMAP credentials exist** |
| **Desktop SSH** (`madredao@192.168.0.3`) | Martin's desktop dev machine | Key-based, local network only | No browser needed |

## Section 3 — Already has an API key (no browser login needed, ever)

From `.secrets/`: `apify.env` · `canary-telegram.env` · `cpanel.env` · `dataforseo.env` · `ga-sc-reporting-bot.json` · `kraft-ftp.env` · `listings-imap.env` · `meta-741.env` · `standup.env` · `stuerzl-artfiles.env` · `telegram-741.env` · `youtube-api.env`

From `.env` (variable names): `CLIENTS_FTP_*` · `FTP_*` · `LF_API_KEY` · `PAGESPEED_API_KEY` · `PORTAL_TEST_*` · `RESEND_API_KEY` · `SHOPIFY_ADMIN_TOKEN` / `SHOPIFY_STORE`

## What this means, ranked by impact

1. **Grant these 2 first — unblocks the most work for the least effort**: Local Falcon MCP key + DataForSEO key. Both already exist as keys, just need copying to the server (Section 3 pattern, zero browser work).
2. **One browser login covers 10+ clients**: the `741studio18@gmail.com` Google Workspace account (GBP, GA4, Google Ads, Local Falcon's own login). Do this one first among the browser logins.
3. **3 real gaps already known, not new work I'm inventing**: Bali Healing's GA4 service-account access, Framer/Meta Ads/Wistia for Pauspapier (requested from Tajan, never granted), Maria Brasse's WordPress handover.
4. **1 security finding, worth fixing regardless of the server move**: a plaintext FTP password for Taxi-Zentrale Nürnberg sits outside `.secrets/` in a script at `~/.gemini/antigravity-ide/.../upload_preisrechner.py`.
5. **2 clients depend on accounts 741 doesn't own**: Talkinfive's Meta Pixel (Billy's) and Calendly (Celine's) — nothing to grant, just a dependency to know about.
6. **Novamira reconnects needed on day one**: Suriya shows "Connection Failed" now; Kraft (Kamil's 2nd site) was never connected at all.
