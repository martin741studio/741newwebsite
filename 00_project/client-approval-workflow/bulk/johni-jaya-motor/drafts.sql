-- Johni Jaya Motor (b84427b9-57bc-4145-83fc-ec284d2de785): 7 decision cards as DRAFT for the portal module "Entscheidungen".
-- Status draft = the client sees nothing. Nothing is released. Facts checked on 13 Oct 2026 (Bali lesson: every card verified first).
-- Language: English, Martin in first person, "you", simple words. Indonesia: HWG does not apply. health_client = false. No tool names.
-- Codes start at E1 (the client had no items before).
--
-- Checks behind each card (details in queue.md):
--   E1 Hours: site footer + Yoast schema = Mon-Sat 09:00-16:30 (curl 13.10.); Google Maps (Chrome 13.10.) "Open, Closes 4.30 pm";
--      owner post dated 11 Aug 2026 on the Maps listing says "Buka setiap hari, 09.00-18.00"; competitor closing times from the Maps search
--      "bengkel mobil jakarta utara" (9 results, 13.10.): 7 close after 16.30 (Fortuna 5pm, Permata Gading 5pm, Quick Service 9pm,
--      Phoran 5pm, DOMO 5pm, Shop & Drive 8pm, Dokter Mobil 5pm), 2 close at 4.30pm (Nusantara, Leo Jaya).
--   E2 Form: WordPress table wp_e_submissions (read only, 13.10.): 1,603 rows 9 May 2025 to 13 Oct 2026, form on page 32 (home) = 1,598,
--      "Booking Overhaul" on page 992242 = 5. No row has an Indonesian phone number or an Indonesian email. All readable rows are spam
--      (ads, bots, medical text, "I wanted to know your price" bot template in many languages). First row is a test by the developer.
--      No captcha keys and no honeypot field are set. Email action goes to an address on johnijayamotor.com.
--   E3 Offers: home page text "EXP 01.03.2026" twice (Diskon 10% Tune Up akhir pekan, gratis Balancing for Overhaul); same offers without
--      end date on /tune-up-mobil-jakarta-utara/, /balancing-jakarta-utara/, /overhaul-mesin-jakarta-utara/ (curl of all 30 sitemap URLs, 13.10.).
--      "Lihat Semua Promo" href="#".
--   E4 WhatsApp: home page has 1 wa.me link (footer number text, "wa.me/+62..."), service pages have buttons with the text "Halo Johni Jaya Motor".
--      GBP booking link = wa.me/628176583223 (set 13.10., memory johnijayamotor-client).
--   E5 H1: live H1 "Servis Mobil Cepat, Berkualitas, dan Terpercaya di Jakarta Utara" (curl 13.10.); title already has "Bengkel & Servis Mobil".
--      Search Console, 90 days to 11 Oct 2026: 25 query rows, 65 impressions, 13 rows with "bengkel" = 38 impressions (58%), 1 row with "servis".
--      Small numbers, many terms are hidden by Google. All page impressions (408) and clicks (8) are on the home page.
--   E6 Prices: home page "Mulai dari" for all 5 jobs; service pages "Mulai Rp140.000", "Mulai Rp385.000", "Mulai Rp250.000", "Mulai Rp4.000.000",
--      but balancing page "Rp50.000 / ban" without "from". GBP side from Martin's dashboard pass of 13.10. (memory): Spooring, Tune Up, Carbon Clean
--      saved as FIXED prices, Balancing and Overhaul as "from". NOT visible in the public Maps view yet (pending Google review).
--      Confirm the GBP price type in the Business Profile Manager before release.
--   E7 Reviews: Maps shows 31 reviews, 5.0 (13.10.). Maps search results (13.10.): Leo Jaya 24, Phoran 45, Fortuna 69, Permata Gading 94,
--      Nusantara 131, Shop & Drive 141, Quick Service 255, DOMO 285, Dokter Mobil 406 (middle = 131). Owner replies to reviews himself.
-- Approver: no approver is set. A client login profile exists (user ccb8d800-a54e-4439-b74a-2b4c0273ba8d, "Johni Jaya Motor", created by SQL,
--   credentials not sent). Martin decides if this user becomes approver_user_id. Until then the client cannot decide.
-- Risk: E3 and E6 are price items (active yes, no 7-day rule). hwg_checked stays false (not a health client).

begin;
-- Settings: insert only if no row exists. approver_user_id stays NULL (see header).
insert into public.client_approval_settings (client_id, approver_user_id, approver_name, auto_approve_consent, health_client)
values ('b84427b9-57bc-4145-83fc-ec284d2de785', null, 'Pak Johni', false, false)
on conflict (client_id) do nothing;

insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class, status)
values
 ('b84427b9-57bc-4145-83fc-ec284d2de785','E1','gbp','Google profile','gbp','Opening hours: which ones are right?',
  'Your Google profile and your website say **Monday to Saturday, 09.00 to 16.30**, but your Google post of 11 August says **every day, 09.00 to 18.00**.',
  'Google profile, Google post and website, checked 13 Oct 2026','2026-10-13',
  '[{"key": "A", "value": "Monday to Saturday, 09.00 to 16.30, closed on Sunday", "label": "what your profile and website show today"}, {"key": "B", "value": "Every day, 09.00 to 18.00", "label": "what your post of 11 August says"}]','A',
  null,null,false,null,
  '{}','Customers should see the same hours on Google, on your website and in every new post. 7 of the 9 workshops that Google lists first for "bengkel mobil jakarta utara" close after 16.30. If your real hours are different, tell me in the note.','I want Google, your website and your posts to show the same hours. Please tell me what is true for your workshop.','none','draft'),
 ('b84427b9-57bc-4145-83fc-ec284d2de785','E2','other','Contact form','website','Booking form on your home page',
  'Your booking form received **1,603 messages since May 2025**, and none that we checked looks like a real customer enquiry, because the form has no spam check.',
  'Check of the messages stored by your website form, 9 May 2025 to 13 Oct 2026','2026-10-13',
  '[{"key": "A", "value": "Keep the form and add a spam check", "label": "customers can still book by form, bots are blocked"}, {"key": "B", "value": "Replace the form with a WhatsApp booking button", "label": "one clear way to book, with name, car and day already typed in"}]','A',
  null,null,false,null,
  '{"page": "/"}','The form messages go to an address on your own website domain, so a real enquiry can get lost between the junk.','I want every real customer to reach you. Today the bots fill the form, so I would keep it and block them.','none','draft'),
 ('b84427b9-57bc-4145-83fc-ec284d2de785','E3','price','Offer','website','Two offers on your home page ended on 1 March 2026',
  'Your home page still shows two offers marked **"EXP 01.03.2026"**, and three service pages promote the same offers with no end date.',
  'Check of your website, 13 Oct 2026','2026-10-13',
  '[{"key": "A", "value": "Keep both offers and set a new end date: 31 December 2026", "label": "same text on the home page and on the three service pages"}, {"key": "B", "value": "Keep both offers with no end date", "label": "customers can always ask for them"}, {"key": "C", "value": "Remove both offers for now", "label": "from the home page and from the three service pages"}]','A',
  null,null,false,null,
  '{"page": "/"}','The offers are 10% off Tune Up at the weekend and free Balancing with every Overhaul. You are closed on Sunday, so "weekend" means Saturday. The link "Lihat Semua Promo" on the home page has no target today.','An old end date tells customers the offer is over. Please tell me what is true today.','price','draft'),
 ('b84427b9-57bc-4145-83fc-ec284d2de785','E4','design','Design','website','WhatsApp button on your home page',
  'On your home page, **WhatsApp appears only once**, as a small phone number in the footer, while your Google profile now sends people to WhatsApp to book.',
  'Check of your website and Google profile, 13 Oct 2026','2026-10-13',
  '[{"key": "A", "value": "Green button under the main heading", "label": "the first thing visitors see", "design": "hero"}, {"key": "B", "value": "Round button at the bottom right on every page", "label": "always in reach, also on your service pages", "design": "float"}, {"key": "C", "value": "Both buttons", "label": "one under the heading and one at the bottom right", "design": "both"}]','B',
  null,null,false,null,
  '{"hero": "Servis Mobil Cepat, Berkualitas, dan Terpercaya di Jakarta Utara", "cta": "Chat WhatsApp"}','The WhatsApp number stays +62 817 658 3223, as on your website. The first message is already typed: "Halo Johni Jaya Motor".',null,'none','draft'),
 ('b84427b9-57bc-4145-83fc-ec284d2de785','E5','text','Text','website','Main heading of your home page',
  'Of the 65 search appearances that Google lists with a search term, **38 (58%) contain "bengkel"** and only 1 contains "servis", but your main heading says "Servis Mobil".',
  'Google search data for your website, 13 Jul to 11 Oct 2026','2026-10-11',
  '[{"key": "A", "value": "{kw} Cepat, Berkualitas, dan Terpercaya", "label": "keeps your own words and adds the search words"}, {"key": "B", "value": "{kw}, Dipercaya Lebih dari 30 Tahun", "label": "puts your 30 years in the heading"}, {"key": "C", "value": "{kw}: Spooring, Balancing, Tune Up & Overhaul", "label": "names your main services"}]','A',
  'Servis Mobil Cepat, Berkualitas, dan Terpercaya di Jakarta Utara','Bengkel Mobil Jakarta Utara',true,'The words "Bengkel Mobil Jakarta Utara" stay in the heading, because customers search for them. In your Google profile, only 741 changes the name, address, map pin, main category and website link.',
  '{"page": "/"}',null,'The yellow lock stays, because customers search for these words. You choose how the rest of the heading sounds.','none','draft'),
 ('b84427b9-57bc-4145-83fc-ec284d2de785','E6','price','Price','website','Prices: "from" price or fixed price?',
  'Your website shows **"from" prices** (Mulai) for Spooring, Tune Up, Carbon Clean and Overhaul, but your Google profile now lists three of these jobs as fixed prices.',
  'Check of your website and Google profile update, 13 Oct 2026','2026-10-13',
  '[{"key": "A", "value": "\"From\" prices everywhere: Spooring from Rp140.000, Balancing from Rp50.000 per tyre, Tune Up from Rp385.000, Carbon Clean from Rp250.000, Overhaul from Rp4.000.000", "label": "the same as your home page today"}, {"key": "B", "value": "Fixed prices for Spooring, Balancing, Carbon Clean. Tune Up and Overhaul stay \"from\" prices", "label": "a clear price for the simple jobs"}]','A',
  null,null,false,null,
  '{"page": "/"}','No price changes. This only decides if the number reads as a "from" price or as a fixed price, on your website and in Google.','The numbers stay the same. I only need to know if they are "from" prices or fixed prices.','price','draft'),
 ('b84427b9-57bc-4145-83fc-ec284d2de785','E7','gbp','Google profile','gbp','How do you ask customers for a Google review?',
  'Your profile has **31 reviews**, and 8 of the 9 workshops that Google lists first for "bengkel mobil jakarta utara" have more (the middle one has 131).',
  'Google Maps search for "bengkel mobil jakarta utara", 13 Oct 2026','2026-10-13',
  '[{"key": "A", "value": "A WhatsApp message after pick-up, with a direct review link", "label": "one tap for the customer"}, {"key": "B", "value": "A QR code card handed over with the receipt", "label": "the customer scans it at the counter"}, {"key": "C", "value": "Both the WhatsApp message and the QR code card", "label": "two chances to ask"}]','A',
  null,null,false,null,
  '{}','I write the message and make the review link and the QR card. You or your team send them. You reply to your reviews yourself, as you do now.',null,'none','draft');
commit;
