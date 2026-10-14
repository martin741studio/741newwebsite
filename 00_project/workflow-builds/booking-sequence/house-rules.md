# 3.6 741 house rules applied — booking-sequence (2026-10-14)

| Rule (memory / CLAUDE.md) | Where in the skill |
|---|---|
| Never send without Martin (email-sending-rules, deliver-messages-ready) | Critical #1; reminder prompt line 1 "Do NOT send"; step 8 = show only |
| Messages in ```text blocks, full message (message-format-copy-safe, always-full-message-draft) | step 8 + reminder prompt step 6 |
| du with prospects, Ich-Form (always-du-with-prospects, client-emails-ich-form) | check_sequence FORMAL check; templates |
| AI-slop 5/5 for every German text (CLAUDE.md) | check_sequence runs deslop_de.py --claims per message |
| No booking link in messages (no-booking-link-in-messages) | BOOKING regex; the meeting link in m3 is the call link, required |
| https:// links (message-links-https) | link check |
| No tool names (no-tool-names-in-client-messages) | TOOLS regex (DataForSEO, Falcon, BrightLocal, Moz, Loom …) |
| Plain language (review-page-plain-language) | JARGON regex (H1, SoLV, NAP, Schema, Canonical, SERP …) |
| Claims need real data (claims-need-real-data) | claims.json with source file; numbers checked against the file |
| HWG for health (hwg-fallstudien-guideline) | HWG regex when booking.health; story = visibility only (insight-menu §4) |
| Never "unclaimed" (Martin's brief) | UNCLAIMED regex + insight-menu §1 |
| No process framing (video-message-transcript-and-email-ask) | PROCESS regex |
| No method sources (no-method-sources-in-deliverables) | messages name only 741 cases; TOOLS regex |
| Questions only as cards (questions-as-grill-me, open-questions-as-grill-cards) | step 2 card, step 8 "waits on Martin = card" |
| Replies in STE (CLAUDE.md) | step 8; reminder prompt last line |
| Claude in Chrome only (always-external-chrome-browser) | no browser needed; curl + API only |
| Spend cap (prospect workflow: dfs.py cap) | 0,30 USD per booking, booking/ ledger |
| Registry visible (F6) | check_sequence --write → booking/_run.json, workflow id booking-sequence |
| Drive link (always-give-drive-link) | n/a: the deliverable is WhatsApp text that Martin sends, no document for the prospect |
