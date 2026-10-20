-- Bali Healing (d0519d13-0bfc-4dfb-b512-57bf550387e6): 7 decisions as DRAFT for the portal decision module.
-- EXECUTED 13.10.2026 after Martin's go (drafts, hidden). Status draft = the client sees nothing. Visible only after "An Kunde geben".
-- BLOCKER before release: the client-facing module UI is German only ("Passt so", "Deine Entscheidungen"). Bali reads English.
-- Facts checked 11.-13.10.2026: audit run balihealing/2026-10-11-kickoff, content pool 04-pool/pool.json, live site (curl 13.10.), CRM.
-- Health client: every item with risk_class <> 'none' needs an active yes (no 7-day rule). hwg_checked stays false until Martin's check.
-- Language: English, Martin in first person, "you". No tool names.

begin;
-- approver: shared login info@balihealing.com. approver_name 'Bali Healing Team' (Martin 13.10.: whoever has access).
insert into public.client_approval_settings (client_id, approver_user_id, approver_name, auto_approve_consent, health_client)
values ('d0519d13-0bfc-4dfb-b512-57bf550387e6', '99d8d495-f746-4d33-9fb4-c5df120b4351', 'Bali Healing Team', false, true)
on conflict (client_id) do update set approver_user_id = excluded.approver_user_id, approver_name = excluded.approver_name, health_client = true;

insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class, status)
values
 ('d0519d13-0bfc-4dfb-b512-57bf550387e6','B1','text','Text','website',
  'Name of your IV drip page',
  '**"iv drip bali" is searched 1,300 times a month.** Your page says "Infusions", and Google does not show it for IV drip searches today.',
  'Google search data and your Search Console', '2026-10-12',
  '[{"key":"A","value":"IV Drip by Bali Healing","label":"the name you suggested, uses the search words"},
    {"key":"B","value":"IV Drip & Infusions in Canggu","label":"adds the place"},
    {"key":"C","value":"Infusions by Bali Healing Beauty","label":"stays as it is"}]', 'A',
  'Infusions by Bali Healing Beauty', 'IV Drip', true, null, '{"page":"/iv-drip-therapy-infusions"}',
  'The needle-based ozone treatments move onto this page. Ozone Insufflation keeps its own page.',
  'I need your OK on the name. Then the page goes live for Google this week.',
  'none', 'draft'),

 ('d0519d13-0bfc-4dfb-b512-57bf550387e6','B2','gbp','Google profile','gbp',
  'Business name in your Google profile',
  'Your profile name is **"Bali Healing Natural Health Center and IV Drip Therapy"**. Google wants the name to match your sign. Service words in the name can lead to a suspension.',
  'Your Google profile and Google''s name rules', '2026-10-11',
  '[{"key":"A","value":"The name on your sign","label":"please write it in the comment field"},
    {"key":"B","value":"Keep the current name","label":"with the service words"}]', 'A',
  'Bali Healing Natural Health Center and IV Drip Therapy', null, false, null, '{}',
  'Your visibility for "ozone therapy" fell from 57 % to 35 % after the last name change. A link is not proven.',
  'This one protects your profile. Tell me the exact name on your sign.',
  'legal', 'draft'),

 ('d0519d13-0bfc-4dfb-b512-57bf550387e6','B3','gbp','Google profile','gbp',
  'Add the category "Medical clinic"?',
  'The **leading profiles for ozone and IV drips use "Medical clinic"**. Your main profile does not have it.',
  'Comparison with the leading clinics in Canggu', '2026-10-11',
  '[{"key":"A","value":"Add it","label":"only if your licences allow a medical clinic"},
    {"key":"B","value":"Do not add it","label":"the profile stays as it is"}]', 'A',
  null, null, false, null, '{}',
  'Google can check licences for medical categories.',
  'I recommend it only if your clinic licence covers it. Please confirm.',
  'health', 'draft'),

 ('d0519d13-0bfc-4dfb-b512-57bf550387e6','B4','node','Site structure','website',
  'Naturopathy and live blood analysis',
  'You stopped both services on 30 July, but **your site and your profile still show them**.',
  'Your website and Google profile', '2026-10-13',
  '[{"key":"A","value":"Remove them from site and profile","label":"the pages forward to the Wellness page"},
    {"key":"B","value":"Bring them back","label":"pages and profile stay"}]', 'A',
  null, null, false, null, '{"page":"/naturopathyconsultations"}',
  'Nothing changes before your answer.',
  'I want your site to show only what you offer today.',
  'treatment', 'draft'),

 ('d0519d13-0bfc-4dfb-b512-57bf550387e6','B5','other','Services','website',
  'Do you offer these services?',
  'People find your site with **"sound healing canggu" (210 searches a month), "breathwork canggu" (70) and "bali belly treatment" (1,300)**.',
  'Google search data', '2026-10-11',
  '[{"key":"A","value":"No, we do not offer them","label":"we leave them out"},
    {"key":"B","value":"Yes, some of them","label":"please name them in the comment field"}]', 'A',
  null, null, false, null, '{}',
  'Also asked: IV drip at home and a general doctor for walk-ins.',
  'Only services you really offer get a page.',
  'none', 'draft'),

 ('d0519d13-0bfc-4dfb-b512-57bf550387e6','B6','price','Prices','website',
  'Prices on your treatment pages',
  '**None of your 58 pages names a price.** People search for "skin tag removal bali price" and "iv drip bali cost".',
  'Your website and Google search data', '2026-10-11',
  '[{"key":"A","value":"Price ranges (from – to)","label":"for example IDR 500,000 – 900,000"},
    {"key":"B","value":"Starting prices only","label":"\"from IDR …\""},
    {"key":"C","value":"No prices","label":"consultation first"}]', 'A',
  null, null, false, null, '{}',
  'You give us the numbers. We only show prices you confirm.',
  'I need your yes here, and then your price list.',
  'price', 'draft'),

 ('d0519d13-0bfc-4dfb-b512-57bf550387e6','B7','other','Team','website',
  'Show your doctors with names?',
  'Your pages show **no doctor and no team**. For medical treatments, visitors look for who treats them.',
  'Your website', '2026-10-11',
  '[{"key":"A","value":"Profiles with name, licence and photo","label":"one short profile per doctor and practitioner"},
    {"key":"B","value":"Team without names","label":"\"our Indonesian doctors and nurses\""}]', 'A',
  null, null, false, null, '{}',
  'Photos only with consent. No title without a valid licence.',
  'Real names build trust fastest. I write the profiles, you check them.',
  'legal', 'draft');
commit;
