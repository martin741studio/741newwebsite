# Source of the 7 cards. Generates drafts.sql and the slop-check text. Run: python3 cards.py
import json
CID='b84427b9-57bc-4145-83fc-ec284d2de785'
cards=[
dict(code='E1',kind='gbp',type_label='Google profile',area='gbp',
 title='Opening hours: which ones are right?',
 why="Your Google profile and your website say **Monday to Saturday, 09.00 to 16.30**, but your Google post of 11 August says **every day, 09.00 to 18.00**.",
 why_source='Google profile, Google post and website, checked 13 Oct 2026', why_date='2026-10-13',
 variants=[dict(key='A',value='Monday to Saturday, 09.00 to 16.30, closed on Sunday',label='what your profile and website show today'),
           dict(key='B',value='Every day, 09.00 to 18.00',label='what your post of 11 August says')],
 rec='A', before=None, keyword=None, seo_lock=False, lock_note=None, context={},
 note="Customers should see the same hours on Google, on your website and in every new post. 7 of the 9 workshops that Google lists first for \"bengkel mobil jakarta utara\" close after 16.30. If your real hours are different, tell me in the note.",
 guide="I want Google, your website and your posts to show the same hours. Please tell me what is true for your workshop.",
 risk='none'),
dict(code='E2',kind='other',type_label='Contact form',area='website',
 title='Booking form on your home page',
 why="Your booking form received **1,603 messages since May 2025**, and none of them looks like a real customer enquiry, because the form has no spam check.",
 why_source="Check of the messages stored by your website form, 9 May 2025 to 13 Oct 2026", why_date='2026-10-13',
 variants=[dict(key='A',value='Keep the form and add a spam check',label='customers can still book by form, bots are blocked'),
           dict(key='B',value='Replace the form with a WhatsApp booking button',label='one clear way to book, with name, car and day already typed in')],
 rec='A', before=None, keyword=None, seo_lock=False, lock_note=None, context={"page":"/"},
 note="The form messages go to an address on your own website domain, so a real enquiry can get lost between the junk.",
 guide="I want every real customer to reach you. Today the bots fill the form, so I would keep it and block them.",
 risk='none'),
dict(code='E3',kind='price',type_label='Offer',area='website',
 title='Two offers on your home page ended on 1 March 2026',
 why="Your home page still shows two offers marked **\"EXP 01.03.2026\"**, and three service pages promote the same offers with no end date.",
 why_source='Check of your website, 13 Oct 2026', why_date='2026-10-13',
 variants=[dict(key='A',value='Keep both offers and set a new end date: 31 December 2026',label='same text on the home page and on the three service pages'),
           dict(key='B',value='Keep both offers with no end date',label='customers can always ask for them'),
           dict(key='C',value='Remove both offers for now',label='from the home page and from the three service pages')],
 rec='A', before=None, keyword=None, seo_lock=False, lock_note=None, context={"page":"/"},
 note="The offers are 10% off Tune Up at the weekend and free Balancing with every Overhaul. You are closed on Sunday, so \"weekend\" means Saturday. The link \"Lihat Semua Promo\" on the home page has no target today.",
 guide="An old end date tells customers the offer is over. Please tell me what is true today.",
 risk='price'),
dict(code='E4',kind='design',type_label='Design',area='website',
 title='WhatsApp button on your home page',
 why="On your home page, **WhatsApp appears only once**, as a small phone number in the footer, while your Google profile now sends people to WhatsApp to book.",
 why_source='Check of your website and Google profile, 13 Oct 2026', why_date='2026-10-13',
 variants=[dict(key='A',value='Green button under the main heading',label='the first thing visitors see',design='hero'),
           dict(key='B',value='Round button at the bottom right on every page',label='always in reach, also on your service pages',design='float'),
           dict(key='C',value='Both buttons',label='one under the heading and one at the bottom right',design='both')],
 rec='B', before=None, keyword=None, seo_lock=False, lock_note=None,
 context={"hero":"Servis Mobil Cepat, Berkualitas, dan Terpercaya di Jakarta Utara","cta":"Chat WhatsApp"},
 note="The WhatsApp number stays +62 817 658 3223, as on your website. The first message is already typed: \"Halo Johni Jaya Motor\".",
 guide=None, risk='none'),
dict(code='E5',kind='text',type_label='Text',area='website',
 title='Main heading of your home page',
 why="Of the 65 search appearances that Google lists with a search term, **38 (58%) contain \"bengkel\"** and only 1 contains \"servis\", but your main heading says \"Servis Mobil\".",
 why_source='Google search data for your website, 13 Jul to 11 Oct 2026', why_date='2026-10-11',
 variants=[dict(key='A',value='{kw} Cepat, Berkualitas, dan Terpercaya',label='keeps your own words and adds the search words'),
           dict(key='B',value='{kw}, Dipercaya Lebih dari 30 Tahun',label='puts your 30 years in the heading'),
           dict(key='C',value='{kw}: Spooring, Balancing, Tune Up & Overhaul',label='names your main services')],
 rec='A', before='Servis Mobil Cepat, Berkualitas, dan Terpercaya di Jakarta Utara',
 keyword='Bengkel Mobil Jakarta Utara', seo_lock=True,
 lock_note='The words "Bengkel Mobil Jakarta Utara" stay in the heading, because customers search for them. In your Google profile, only 741 changes the name, address, map pin, main category and website link.',
 context={"page":"/"}, note=None,
 guide="The yellow lock stays, because customers search for these words. You choose how the rest of the heading sounds.",
 risk='none'),
dict(code='E6',kind='price',type_label='Price',area='website',
 title='Prices: "from" price or fixed price?',
 why="Your website shows **\"from\" prices** (Mulai) for Spooring, Tune Up, Carbon Clean and Overhaul, but your Google profile now lists three of these jobs as fixed prices.",
 why_source='Check of your website and Google profile update, 13 Oct 2026', why_date='2026-10-13',
 variants=[dict(key='A',value='"From" prices everywhere: Spooring from Rp140.000, Balancing from Rp50.000 per tyre, Tune Up from Rp385.000, Carbon Clean from Rp250.000, Overhaul from Rp4.000.000',label='the same as your home page today'),
           dict(key='B',value='Fixed prices for Spooring, Balancing, Carbon Clean. Tune Up and Overhaul stay "from" prices',label='a clear price for the simple jobs')],
 rec='A', before=None, keyword=None, seo_lock=False, lock_note=None, context={"page":"/"},
 note="No price changes. This only decides if the number reads as a \"from\" price or as a fixed price, on your website and in Google.",
 guide="The numbers stay the same. I only need to know if they are \"from\" prices or fixed prices.",
 risk='price'),
dict(code='E7',kind='gbp',type_label='Google profile',area='gbp',
 title='How do you ask customers for a Google review?',
 why="Your profile has **31 reviews**, and 8 of the 9 workshops that Google lists first for \"bengkel mobil jakarta utara\" have more (the middle one has 131).",
 why_source='Google Maps search for "bengkel mobil jakarta utara", 13 Oct 2026', why_date='2026-10-13',
 variants=[dict(key='A',value='A WhatsApp message after pick-up, with a direct review link',label='one tap for the customer'),
           dict(key='B',value='A QR code card handed over with the receipt',label='the customer scans it at the counter'),
           dict(key='C',value='Both the WhatsApp message and the QR code card',label='two chances to ask')],
 rec='A', before=None, keyword=None, seo_lock=False, lock_note=None, context={},
 note="I write the message and make the review link and the QR card. You or your team send them. You reply to your reviews yourself, as you do now.",
 guide=None, risk='none'),
]
def q(s): return 'null' if s is None else "'"+s.replace("'","''")+"'"
def js(o): return "'"+json.dumps(o,ensure_ascii=False).replace("'","''")+"'"
hdr=open('/Users/martindrendel/741website/00_project/client-approval-workflow/bulk/johni-jaya-motor/_header.sql').read()
rows=[]
for c in cards:
    v=[dict(key=x['key'],value=x['value'],label=x['label'],**({'design':x['design']} if 'design' in x else {})) for x in c['variants']]
    rows.append("(%s,%s,%s,%s,%s,%s,\n  %s,\n  %s,%s,\n  %s,%s,\n  %s,%s,%s,%s,\n  %s,%s,%s,%s,'draft')"%(
      q(CID),q(c['code']),q(c['kind']),q(c['type_label']),q(c['area']),q(c['title']),q(c['why']),q(c['why_source']),q(c['why_date']),
      js(v),q(c['rec']),q(c['before']),q(c['keyword']),'true' if c['seo_lock'] else 'false',q(c['lock_note']),
      js(c['context']),q(c['note']),q(c['guide']),q(c['risk'])))
sql=hdr+"""
begin;
-- Settings: insert only if no row exists. approver_user_id stays NULL (see header).
insert into public.client_approval_settings (client_id, approver_user_id, approver_name, auto_approve_consent, health_client)
values ('%s', null, 'Pak Johni', false, false)
on conflict (client_id) do nothing;

insert into public.approval_items
  (client_id, code, kind, type_label, area, title, why, why_source, why_date, variants, recommended_key,
   before_value, keyword, seo_lock, lock_note, context, note, guide_text, risk_class, status)
values
 %s;
commit;
"""%(CID,",\n ".join(rows))
open('/Users/martindrendel/741website/00_project/client-approval-workflow/bulk/johni-jaya-motor/drafts.sql','w').write(sql)
# slop text dump
with open('/private/tmp/claude-501/-Users-martindrendel-741website/0d991c89-d222-4753-8b45-fd40f1c857f2/scratchpad/jjm/slop.json','w') as f:
    out=[]
    for c in cards:
        for k in ('title','why','note','guide','lock_note'):
            if c.get(k): out.append((c['code']+'.'+k,c[k]))
        for x in c['variants']: out.append((c['code']+'.'+x['key'],x['value']+'. '+x['label']))
    json.dump(out,f,ensure_ascii=False)
print(len(cards),'cards')
