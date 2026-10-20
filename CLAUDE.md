# Writing style: ASD-STE100 Simplified Technical English (STE)

Write all replies and all artifacts in ASD-STE100 Simplified Technical English.

Rules:

- Use the active voice.
- Keep sentences to 20 words or fewer.
- Give one idea in each sentence.
- Use simple tenses: present, past, and future.
- Use the same word for the same idea each time.
- Do not use idioms, slang, or jargon.
- Keep paragraphs to 6 sentences or fewer.

Keep technical items exact. Do not change file paths, function names, column names, prices, or numbers.

## Exception

Do not use STE when the user asks for an email, a message, a blog post, or other content that needs full natural prose. Write that content in normal full English.

# AI-slop check (hard rule)

Check every text with the AI-slop skill before you deliver it. This applies to messages, emails, page copy, documents and replies to Martin.

- German text: `python3 00_project/content-writing-skill/scripts/deslop_de.py <file>`. Add `--claims <file>` for numbers that have a source.
- English text: `python3 .claude/skills/slopmonster/tools/deslop.py --text "..."`.
- Deliver only at 5/5. Below 5/5, rewrite the text, cleanse it with `.claude/skills/slopmonster/tools/cleanse.sh`, and lint it again.
- Put messages for sending in one ```text block. Use the "•" character for bullets and "1." for numbered items.


# Pre-send sweep (hard rule)

Before every final reply: anything that waits on Martin (open points, go, his steps, a message to send, a login, a delete) is an AskUserQuestion card, never a prose list. See `~/.claude/CLAUDE.md` and memory `open-questions-as-grill-cards`.


# Marketing Data Backbone in Supabase (Source of Truth)

Query client marketing data through Supabase `execute_sql`.

Always use these unified tables:

- **Organic Search**: `public.gsc_daily_performance` contains daily clicks, impressions, CTR, and position. Do not state that GSC time-series data is missing.
- **Paid Ads**: `public.google_campaigns` contains client Google Ads spend, clicks, conversions, and CPA. `public.v_paid_campaigns` gives a unified ads view. `public.meta_campaigns` contains agency internal leads only.
- **Map Rankings**: `public.geo_grid_scans` contains Local Falcon spatial scans, ARP, ATRP, SoLV, and map screenshots.
- **Directory Citations**: `public.brightlocal_audits` contains NAP consistency scores, live citations, and review counts. `public.client_citations` contains individual listings.
- **Backlinks**: `public.client_backlinks` contains verified links, domain authority, and toxic disavow flags.
- **Client Deliverables**: `public.client_drive_assets` contains cataloged client reports, Excel sheets, and CRO prototypes.
- **Lead Intake**: `public.leads` and `public.site_form_submissions` contain inbound leads and intent scores.


# WordPress Client-Editable Text Boxes (Hard-Coded Rule)

Never put raw HTML tags (`<span>`, `<br>`, `<strong>`, `<div>`, inline style attributes, etc.) inside text boxes, headings, or fields where clients make text edits.

- Clients get confused by HTML tags, accidentally delete tags, or break layouts.
- Client-facing text inputs must remain strictly **plain text**.
- All styling, color accents, line breaks, and font settings must be handled natively through widget controls, theme styling, dedicated sub-fields, or CSS classes on the container/wrapper.


# Client Roadmap Pre-Flight (Hard-Coded Rule)

Before working on any client (Talkinfive, Praxis Suriya, Stürzl, Katharina Kisser), run:
`python3 .claude/skills/client-roadmap/scripts/get_roadmap.py <client>`
- Announce active milestone ($M_1 \to M_4$) and top constraint.
- Constrain all tasks strictly to the active milestone.
- Update telemetry `_run.json` and `roadmap.json` upon task completion.


