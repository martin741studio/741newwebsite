-- 13.10.2026 (Martin): Bali does NOT offer acupuncture. B8 was rewritten without acupuncture. Never create acupuncture cards for Bali.
-- Bali Healing (d0519d13-0bfc-4dfb-b512-57bf550387e6): 3 NEW decisions as DRAFT (codes B8-B10).
-- B10 draft (Bali belly page) was DELETED by the main session on 13.10.2026: another session had already released B10 'Which new page do we write first?' (Bali belly vs breathwork, status open, 13.10. 06:33 UTC). Only B8 and B9 are drafts.
-- Do NOT recreate B1-B7. They were deleted on 13.10.2026 (facts outdated). Nothing here repeats them.
-- Status draft = the client sees nothing. Visible only after "An Kunde geben".
-- Language: English, Martin in first person, "you". No tool names, no prices, no doctor names.
-- Settings row: EXISTS (checked 13.10.2026 by select). approver = shared client login, "Bali Healing Team", health_client = true,
--   auto_approve_consent = false. Not changed here. health_client = true forces hwg_checked at release, although HWG does not apply
--   to Bali. At release Martin sets hwg_checked = true with a note such as "741 check: HWG n/a, Indonesia and Google health policy checked".
-- Facts checked 13.10.2026:
--   B8  curl on balihealing.com: /iv-drip-therapy-infusions, /acupuncture, /breathwork all return 200 with <meta name="robots" content="noindex">.
--       Sitemap (pages-sitemap.xml, lastmod 13.10.) lists none of the three. Search Console pages export (11.07.-09.10.2026, 56 pages)
--       has no row for any of the three. Volume "iv drip bali" 1,300 per month (volume.json, 11.10.). IV title and H1 are already
--       "IV Drip ..." (done, not a question). Acupuncture status is NOT proven: the roadmap of 23.09. calls the old acupuncture scan
--       "service dropped", the roadmap of 13.10. and the site tree say show it. Variant B covers this. Breathwork is offered (Martin 13.10.).
--   B9  Review list read 13.10. (feed data reviews-nhc.json): 100 reviews, 4.7; new in 2026: Jan 7, Feb 2, Jun 1, Jul 2, Sep 3 = 15.
--       GA4 contact_whatsapp: Aug 321, Sep 313. Leader for "ozone therapy" 128 reviews (scan 12.10.). WhatsApp is the only booking path (audit B08.01).
--       741 does not reply to reviews (rule 25.08.2026). This card is about asking patients, a client task.
--   B10 "bali belly treatment" 1,300, "bali belly doctor" 720 (volume2.json, 11.10.). Sitemap has no Bali belly page. Search Console 90 days has no Bali belly query.
--       Martin 13.10.: Bali belly treatment is offered, a page is possible. Page text needs the doctor's wording. No cure claims.

begin;

insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class, status)
values
 ('d0519d13-0bfc-4dfb-b512-57bf550387e6','B8','node','Site structure','website',
  'Show your hidden pages on Google?',
  'Google has **not shown your IV drip or breathwork page** in search in the last 90 days. The pages are hidden from search, while "iv drip bali" is searched 1,300 times a month.',
  'Your website and your Google search data', '2026-10-11',
  '[{"key":"A","value":"Show both pages","label":"IV drip and breathwork appear in Google after we check the wording"},
    {"key":"B","value":"Show the IV drip page, keep breathwork hidden","label":"breathwork waits until its page is ready"},
    {"key":"C","value":"Keep both hidden","label":"nothing changes"}]', 'A',
  null, null, false, null,
  '{"node":"/iv-drip-therapy-infusions, /breathwork","node_kind":"Hidden pages"}',
  'We check the wording of each page before it appears in Google. Nothing changes before your answer.',
  'Your best pages are invisible to Google today. Tell me which ones should appear.',
  'health', 'draft'),

 ('d0519d13-0bfc-4dfb-b512-57bf550387e6','B9','other','Reviews','gbp',
  'How should patients be asked for a review?',
  'Your main profile got **15 new reviews in 2026**, more than 300 people click WhatsApp every month, and the leading ozone profile has 128 reviews against your 100.',
  'Your Google profile and your website visits', '2026-10-13',
  '[{"key":"A","value":"A short WhatsApp message after each visit","label":"your team sends it, I write the text"},
    {"key":"B","value":"A QR code card at the front desk","label":"patients scan it before they leave"},
    {"key":"C","value":"Both","label":"message first, card as backup"}]', 'A',
  null, null, false, null, '{}',
  'Reviews that name the treatment help most. No gifts or discounts for reviews.',
  'You decide what feels right for your patients. I write the wording.',
  'none', 'draft');

commit;
