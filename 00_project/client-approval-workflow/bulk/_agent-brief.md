# Bulk decision cards — rules for every client agent (13 Oct 2026)

Goal: fact-checked DRAFT cards for the portal module "Entscheidungen" (table approval_items), so Martin can review them as grill cards in the Claude chat. Nothing is released. Nothing is visible to a client.

## Read first
- Memory dir: /Users/martindrendel/.claude/projects/-Users-martindrendel-741website/memory/ (MEMORY.md is the index). Read the client files for your client, plus: client-approval-workflow.md, release-decisions-from-chat.md, bali-client-facts-2026-10-13.md, no-tool-names-in-client-messages.md, feedback-no-invoice-talk.md, claims-need-real-data.md, page-content-qa-checklist.md, no-website-changes-without-go.md, no-method-sources-in-deliverables.md.
- /Users/martindrendel/741website/00_project/client-approval-workflow/brief.md and portal/01-migration.sql (table, guard trigger, field meanings).
- Models of a good card: portal/05-seed-suriya-drafts.sql and /Users/martindrendel/741website/00_project/assets/balihealing/status-2026-10-13/approval-drafts-bali.sql.
- The client's own folder in /Users/martindrendel/741website/00_project/assets/<client>/ and /Users/martindrendel/741website/ (grep for the client name; latest chat/WhatsApp notes, latest report under /r/<hash>/ if it exists, content pool, audit, keyword data, site tree, GBP plan).

## Lesson from Bali (important)
On 13 Oct 2026 Martin deleted all 7 Bali drafts: they were outdated (wording already live, profile name done, client had ruled out prices and doctor names). So VERIFY every candidate before it becomes a card:
1. Compare it with the live website (curl: title, H1, page text, `curl -sL`), the Google profile (Local Falcon free reads only, where connected; otherwise public Google/Maps page), the client's own rules in memory, the latest chat/WhatsApp notes in the client folder, and the latest reports.
2. Drop a candidate if it is already done, was ruled out, the client said no, or you cannot verify it. Write the reason in queue.md.
3. Keep only real choices with 2-3 variants, one marked recommended (portal label "741 empfiehlt"), each with source and date (why_source, why_date). The date is the date of the DATA (max. 3 months old, prefer < 4 weeks). No prices, no invoices, no fee talk, no contract talk, no deadlines the client did not ask for. No tool or provider names in client text (no Local Falcon, DataForSEO, BrightLocal, Moz, Apify, Supabase, Search Console is OK only as "deine Search Console" if the client uses it themself: avoid anyway, say "Google-Suchdaten"). No method sources.
4. A card is answerable in ONE click. Rank by impact on enquiries and rankings. Merge near-duplicates. Max 7 kept cards per client. Fewer good cards beat many weak ones. Zero kept cards is a valid result.

## Card shape (columns of public.approval_items)
client_id, code, kind (price|text|design|gbp|node|other), type_label (Preis|Text|Design|Google-Profil|Seitenbaum|... in the client's language), area (website|gbp), title, why (ONE sentence, **bold** allowed, real numbers), why_source (client language, no tool names), why_date (date), variants (jsonb array of 2-3: {key,value,label,design?}; for text items with a keyword use {kw} in value), recommended_key, before_value (current live text, for text items), keyword + seo_lock (seo_lock true needs keyword), lock_note, context (jsonb, e.g. {"page":"/slug/"} or {"node":..,"node_kind":..}), note, guide_text (Martin speech bubble, first person, max 2 sentences, optional), risk_class (none|price|health|treatment|legal), status = 'draft' ONLY.
- hwg_checked stays false (default). Do NOT set hwg_checked, released_at, remind_at, due_at, chosen_*.
- risk_class: price/health/treatment/legal force an active yes (no 7-day rule). Use it honestly.
- Codes: continue the client's existing numbering (query: select code from approval_items where client_id=...). If the client has no items yet, start at E1. Bali used B1-B7 (deleted): start at B8.
- Language: clients.lang. German clients: du-form unless the live site uses Sie (check it). English clients: "you", Martin in first person. German text with real umlauts.
- HWG (German law on health claims): applies to Hüwel, Suriya, Dumann, Kamil and any German practice with health claims: no healing promises, no success guarantees, no before/after claims, no "heilt/lindert" as promise. Does NOT apply to Bali Healing and Johni Jaya Motor (Indonesia).
- client_approval_settings: INSERT a settings row ONLY IF none exists (health_client true for German health clients, false otherwise; approver_user_id NULL, approver_name from clients.contact_person, auto_approve_consent false). Never change an existing row. (Without an approver the client cannot decide: list "approver missing" as an open gap in queue.md, do not invent a user id.)
- Internal files (queue.md, comments): ASD-STE100 style, short sentences, active voice. Client text: normal natural language in the client's language.
- Run every client-facing string through the slop check where practical: English `python3 /Users/martindrendel/741website/.claude/skills/slopmonster/tools/deslop.py --text "..."`, German `python3 /Users/martindrendel/741website/00_project/content-writing-skill/scripts/deslop_de.py <file>`. Need 5/5; rewrite below that.

## Hard limits
- Do NOT run INSERT/UPDATE/DELETE on the database. SELECT through Supabase MCP execute_sql (project galjmtozcgxcwtzkzbpi) is fine. The main session inserts the drafts.
- Do NOT release anything, do NOT touch the live or staging portal index.html, do NOT message any client, do NOT deploy anything, do NOT edit any client website.
- No paid calls (no DataForSEO, no Local Falcon scans, no ad spend, no Apify). Free reads only: curl on public pages, saved files, saved reports, Local Falcon free read endpoints if connected (no new scans).
- Do not print secrets (keys, tokens, passwords) anywhere.
- Do not change repo files outside your output folder.

## Output (your client folder: /Users/martindrendel/741website/00_project/client-approval-workflow/bulk/<client-slug>/)
1. queue.md: (a) one-line client facts (lang, form of address, live site, health or not, approver status in the DB); (b) table of ALL candidates: id, idea, verification (what you checked, source file/URL, date), result KEEP or DROP, reason; (c) the ranked KEEP list with the one-line reason why it ranks there; (d) "Dashboard readiness": can the new dashboard feed be filled today for this client from Search Console, GA4, Local Falcon free reads, the Ads account? For each source: yes/partial/no, evidence, gap, owner (Martin, Dinakar, Tantri, Gayo, agent). Read /Users/martindrendel/741website/00_project/client-dashboard-redesign/02-data-readiness-bali.md and the shared notes in "/Users/martindrendel/Library/Application Support/Claude/side-session-notes/local_4a40ac6d-2343-48c7-9c21-fc0c965acb78/" for the pattern and tools; memory file google-reporting-api-access.md explains the API access; (e) open data gaps.
2. drafts.sql: begin; [settings insert only if missing, with ON CONFLICT DO NOTHING]; INSERT of the kept cards, all status 'draft'; commit; Header comment: facts checked, dates, sources (same style as the Suriya seed). Valid Postgres (dollar-quoting not needed; escape single quotes by doubling). If nothing is kept, write a header-only file with a comment.
3. Final reply (max 12 lines): files written, candidates / kept / dropped counts, top 3 cards to ask first (code + title), data gaps, anything you could not verify.
