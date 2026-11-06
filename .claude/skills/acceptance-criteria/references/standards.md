# Module types and standards to check

For each module type in the contract, check the listed sources. Fetch the page and confirm the current version before you cite it. The URLs were correct on 2026-11-06. If a page moved or a newer version exists, cite the newer one.

Every contract also gets the **base** set.

| Type | What it covers | Check these (primary first) |
|---|---|---|
| base | every module | ISO/IEC 25010 quality model (categories), OWASP Top 10 https://owasp.org/www-project-top-ten/ , project rules in CLAUDE.md and memory |
| auth | login, sessions, roles, password reset | OWASP ASVS (V2 auth, V3 session, V4 access) https://owasp.org/www-project-application-security-verification-standard/ ; NIST SP 800-63B https://pages.nist.gov/800-63-4/sp800-63b.html ; OWASP Authentication and Session Management cheat sheets https://cheatsheetseries.owasp.org/ |
| form | contact forms, lead intake, booking requests | DSGVO Art. 5, 6, 13 https://eur-lex.europa.eu/eli/reg/2016/679/oj ; OWASP Input Validation cheat sheet ; WCAG 2.2 forms (1.3.1, 3.3.x) https://www.w3.org/TR/WCAG22/ ; spam protection without tracking (honeypot, rate limit) |
| landing-page | public web page, service page | Core Web Vitals https://web.dev/articles/vitals ; WCAG 2.2 AA ; Google Search Essentials https://developers.google.com/search/docs/essentials ; schema.org ; DDG § 5 Impressum https://www.gesetze-im-internet.de/ddg/ ; 741 page rules in memory (CRO workflow, no HTML in client edit fields) |
| tracking | analytics, pixels, consent banner, conversion tracking | TDDDG § 25 (consent for device access, formerly TTDSG) https://www.gesetze-im-internet.de/ttdsg/ ; DSGVO ; Google Consent Mode v2 docs https://developers.google.com/tag-platform/security/guides/consent ; memory 741studio-tracking-consent |
| api | REST/MCP endpoints, webhooks, integrations | OWASP API Security Top 10 https://owasp.org/API-Security/ ; RFC 9110 HTTP semantics https://www.rfc-editor.org/rfc/rfc9110 ; token auth, rate limits, idempotency for webhooks |
| data | database tables, migrations, reports | normal forms and indexes (vendor docs, e.g. PostgreSQL https://www.postgresql.org/docs/current/ ), Supabase RLS https://supabase.com/docs/guides/database/postgres/row-level-security , backups and restore test, DSGVO Art. 17 deletion, memory db-write-needs-isolated-confirmation |
| upload | file upload, media library | OWASP File Upload cheat sheet ; size and type limits ; malware scan ; storage outside webroot |
| email | transactional or marketing mail | UWG § 7 (consent for advertising mail) https://www.gesetze-im-internet.de/uwg_2004/ ; SPF, DKIM, DMARC (RFC 7208, 6376, 7489) ; Google and Yahoo bulk sender rules https://support.google.com/a/answer/81126 ; unsubscribe one-click (RFC 8058) |
| payment | checkout, invoices, subscriptions | PCI DSS v4.0.1 https://www.pcisecuritystandards.org/ ; provider docs (Stripe https://docs.stripe.com/security ) ; never store card data ; webhooks signed and idempotent |
| ai-feature | chatbot, AI text or image generation, agents | EU AI Act Art. 50 transparency (labels for AI content, applies from 2026-08-02) https://eur-lex.europa.eu/eli/reg/2024/1689/oj ; OWASP Top 10 for LLM Applications https://genai.owasp.org/llm-top-10/ ; fallback model and status monitoring, prompt-injection tests, EU data location |
| health-content | anything for Heilpraktiker, Physio, Ärzte, Therapeuten | HWG https://www.gesetze-im-internet.de/heilmwerbg/ ; memory hwg-fallstudien-guideline ; no healing promises, no before/after claims |
| accessibility | any user interface that sells to consumers | WCAG 2.2 AA ; BFSG (in force since 2025-06-28 for many B2C services) https://www.gesetze-im-internet.de/bfsg/ ; EN 301 549 |
| wordpress | plugin, theme, Elementor work | WordPress security APIs https://developer.wordpress.org/apis/security/ (nonces, escaping, capabilities) ; WordPress Coding Standards ; memory only-inside-cms-build, no-html-in-client-edit-fields |
| automation | Zapier, Make, n8n, scheduled scripts | idempotency, retries with limits, alerting (canary skill), secrets not in logs, a dry-run mode |
| infra | server, deploy, backups, DNS | backup + restore test, staging before live, rollback step, TLS, memory website-security-checklist and minimal-change-website-work |

## Gap list (what a plain request forgets)

Ask yourself for each module: What happens on wrong input? On double submit? On a timeout of a third-party service? When the user has no JavaScript, a slow phone, a screen reader? Who may see the data, and how is it deleted? How do we know it broke (monitoring)? How do we roll back?
