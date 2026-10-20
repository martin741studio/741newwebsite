"""Bali Healing roadmap v3 (13.10.2026): insert the 'Status 13 October' section into the live roadmap page.
Input: the live page (fetched fresh, never an old copy). Output: roadmap-v3.html next to this script.
Usage: python3 build_roadmap_v3.py <live_roadmap.html>
Sources for every number are listed in SOURCES.md next to this script."""
import re, sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
GUIDE = '/Users/martindrendel/741website/00_project/assets/brand/martin-guide'
src = open(sys.argv[1], encoding='utf-8').read()

def st(cls, txt): return f'<span class="status {cls}" style="margin-left:0">{txt}</span>'

STATUS = f"""
  <div class="bigsect" id="status-13-oct">
    <div class="bigsect-h">Status · 13 October 2026 <span class="badge2">Where we stand</span></div>
    <p class="bigsect-lead">A lot happened in the background since the last update on 23 September, but too little of it reached your website. This section shows where we stand today, what holds us back, what happened with each of your requests, and the plan for the next four weeks.</p>

    <div class="kpis">
      <div class="kpi k-rev"><div class="l">Google Search clicks</div><div class="n">599</div><div class="d">September. July 653, August 609. 1–12 Oct: 191 (same days in Sep: 229)</div></div>
      <div class="kpi k-keep"><div class="l">Average position</div><div class="n">10.8</div><div class="d">1–12 Oct. July 15.9. We move up, clicks have not grown yet</div></div>
      <div class="kpi k-new"><div class="l">WhatsApp clicks from the site</div><div class="n">313</div><div class="d">September. August 321. 1–12 Oct: 116</div></div>
      <div class="kpi k-pend"><div class="l">Google Ads</div><div class="n">Paused</div><div class="d">Since 1 Oct: verification open. 61 clicks, 14 WhatsApp clicks since August</div></div>
    </div>

    <div class="subh">What holds us back</div>
    <table class="mtable">
      <tr><th>Blocker</th><th>Effect</th><th>Fix</th><th>Who</th></tr>
      <tr><td>Your IV drip page and your acupuncture page are hidden from Google</td><td>"iv drip bali" has 1,300 searches a month. Your visibility for it in Maps is 0 %. In the last 30 days no search with "iv drip" showed your site</td><td>Make both pages visible again, with the name "IV Drip" in the title</td><td>741, after your OK on the name</td></tr>
      <tr><td>Google Ads are paused</td><td>No ads since the verification deadline on 1 October</td><td>Upload your business license (NIB) for Google's check. The check takes 1 to 10 days</td><td>741 (Martin), this week</td></tr>
      <tr><td>Ozone visibility in Maps fell</td><td>Your share of the top 3 for "ozone therapy" fell from 57 % to 35 % between 21 September and 5 October</td><td>Check the profile name and categories with you (see decisions below)</td><td>You and 741</td></tr>
      <tr><td>No prices and no doctor names on the site</td><td>None of your 58 pages names a price. Visitors cannot see who treats them</td><td>Price ranges and short doctor profiles on the treatment pages</td><td>You (facts), 741 (pages)</td></tr>
      <tr><td>No replies to reviews</td><td>None of the reviews we checked has a reply from the clinic</td><td>Reply to new reviews and ask happy patients for a review. We give you short reply templates</td><td>You</td></tr>
    </table>

    <div class="subh">Are the ads tracked?</div>
    <p style="font-size:13.5px;color:var(--ink-soft);max-width:82ch">Yes. Since 2 August every WhatsApp click from an ad counts as a result. The ozone campaign brought 61 clicks and 14 WhatsApp clicks for IDR 571,785 in total, so one WhatsApp click cost IDR 40,842. One limit: we see the click, not the conversation. Please tell us from WhatsApp Business how many of these chats became bookings.</p>

    <div class="subh">Your requests and where they stand</div>
    <table class="mtable">
      <tr><th>Request</th><th>Status</th><th>Next step</th></tr>
      <tr><td>Backlinks through LinkedIn</td><td>{st('progress','Running')}</td><td>Since 25 Sep: 149 connection requests, 38 personal messages, 14 businesses in conversation, 9 with a concrete article offer. Links live: 0. The first ones come when the articles are published in October</td></tr>
      <tr><td>Google profile name</td><td>{st('done','Done')}</td><td>Changed as you asked. Google wants the name to match your sign, so we check the official name with you (decisions below)</td></tr>
      <tr><td>IV Drip on the website</td><td>{st('pending','Open')}</td><td>Rename the page to IV Drip, add the needle-based ozone treatments, keep Ozone Insufflation as its own page. Needs Peggy's OK on the name "IV Drip by Bali Healing"</td></tr>
      <tr><td>Similar treatments on each page</td><td>{st('progress','Started')}</td><td>Live on the Microneedling page. The other Beauty pages follow this week from Pasha's sheet. The Wellness list is still open on your side</td></tr>
      <tr><td>Treatment videos</td><td>{st('pending','Open')}</td><td>Embed one video per treatment page this week. Pasha sends the links with the page for each</td></tr>
      <tr><td>Articles</td><td>{st('pending','Waiting for drafts')}</td><td>Your drafts go into the Wix Blog. We check title, headings and links before they go live</td></tr>
      <tr><td>Google Ads</td><td>{st('pending','Paused')}</td><td>Restart after Google's check. Then the skin tag and mole removal campaign goes live (it is built)</td></tr>
    </table>

    <div class="subh">What we built for you in the background</div>
    <table class="mtable">
      <tr><th>Piece</th><th>What it gives you</th></tr>
      <tr><td>Visibility check</td><td>Your profile and site measured against the clinics that rank above you: 45 of 100. Full page follows after this update</td></tr>
      <tr><td>Content plan</td><td>45 topics from real searches, 19 of them top priority. IV drip, skin tag removal, ozone, prices, osteopathy and facials lead</td></tr>
      <tr><td>New site structure</td><td>35 key pages in two clear paths, Wellness and Beauty, with one shared consultation. Most exist already and get better text, prices and proof. Two are new (doctors, questions), and two are finished pages that Google cannot see yet</td></tr>
    </table>

    <div class="subh">The next four weeks</div>
    <table class="mtable">
      <tr><th>Week</th><th>What happens</th><th>Who</th></tr>
      <tr><td>13 Oct</td><td>License to Google. IV drip and acupuncture pages visible again (after your OK). Similar treatments on the Beauty pages. Videos on the treatment pages</td><td>741, you (OK and links)</td></tr>
      <tr><td>20 Oct</td><td>Ads restart once Google approves, plus the skin tag campaign. Prices and doctor names on the first pages. You start replying to reviews with our templates</td><td>741, you (prices, names, replies)</td></tr>
      <tr><td>27 Oct</td><td>A prototype of a new homepage with the two paths, for you to review before anything changes on the live site</td><td>741</td></tr>
      <tr><td>3 Nov</td><td>First partner articles live. New visibility measurement against today's numbers</td><td>741, partners</td></tr>
    </table>
    <aside class="mg mg--right mg--flip" data-reveal style="margin-top:18px"><img class="mg__img" src="poses/martin-insight.webp" alt="Martin from 741 with an idea" width="112"><div class="mg__bubble"><span class="mg__name">Martin</span><p>The fastest lever: two finished pages are hidden from Google. Once you say yes, they go live this week.</p></div></aside>

    <div class="subh">Decisions we need from you</div>
    <table class="mtable">
      <tr><th>Decision</th><th>Why it matters</th></tr>
      <tr><td>Name of the IV page</td><td>"IV Drip by Bali Healing" uses the words people search for</td></tr>
      <tr><td>Official business name in the Google profile</td><td>Google can object to names that differ from your sign</td></tr>
      <tr><td>Category "Medical clinic"</td><td>The leading profiles for ozone and IV drips use it. It fits only if your licences allow it</td></tr>
      <tr><td>Naturopathy and live blood analysis</td><td>You stopped them on 30 July, but the site and profile still show them</td></tr>
      <tr><td>Breathwork, sound healing, IV at home, general doctor</td><td>People search for them. Only if you offer them</td></tr>
      <tr><td>Prices and doctor names</td><td>Visitors look for both before they book</td></tr>
    </table>
    <p style="font-size:12.5px;color:var(--grey);margin-top:10px">Sources: Google Search Console (data to 10 Oct), Google Analytics, your Google profiles and your Google Ads account, read 11–13 October 2026.</p>
  </div>
"""

out = src
# 1 header meta and lead
out = out.replace('roadmap updated 23 Sep 2026 · v2 — reviewed with Martin', 'roadmap updated 13 Oct 2026 · v3 — status added', 1)
lead_old = re.search(r'<p class="lead">.*?</p>', out, re.S).group(0)
out = out.replace(lead_old, '<p class="lead"><b>New on 13 October:</b> the status section below shows where we stand, what holds us back and the plan for the next four weeks. The tracks further down are the full roadmap from 23 September.</p>\n' + STATUS, 1)
# 2 tool names out of client view
out = out.replace('Findings — approved, checked via DataForSEO', 'Findings — approved, checked with backlink data', 1)
out = out.replace("(DataForSEO's own scale)", '(on a 0 to 1,000 scale)', 1)
# 2b LinkedIn track: real numbers instead of "pending"
out = out.replace('<p class="todo">🔲 Pending reply data.</p>', '<p class="live">Status 13 Oct: 149 connection requests since 25 Sep, 38 accepted plus 10 people Peggy already knew. 38 businesses got a personal message, 14 replied and are in conversation, 9 have a concrete article offer. Links live: 0. The first articles go live in October.</p>', 1)
# 3 Martin guide assets
out = out.replace('</head>', '<link rel="stylesheet" href="/review-assets/martin-guide/martin-guide.css">\n</head>', 1)
out = out.replace('</body>', '<script src="/review-assets/martin-guide/martin-guide.js" defer></script>\n</body>', 1)
tmp = os.path.join(HERE, '_v3_src.html'); open(tmp, 'w', encoding='utf-8').write(out)
subprocess.run(['python3', os.path.join(GUIDE, 'inline.py'), tmp, os.path.join(HERE, 'roadmap-v3.html')], check=True); os.remove(tmp)
assert 'DataForSEO' not in re.sub(r'<(script|style)[^>]*>.*?</\1>', '', open(os.path.join(HERE, 'roadmap-v3.html')).read(), flags=re.S)
