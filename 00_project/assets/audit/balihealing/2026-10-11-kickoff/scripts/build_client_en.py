"""Build report/client.html in English for the Bali Healing kickoff run (client_lang en). Draft until Go-C.
Reuses CSS and helpers from audit-workflow/scripts/build_report.py. Client texts below use only facts from findings.json.
Usage: python3 build_client_en.py [--guide]   --guide adds the Martin callouts and inlines them (martin-guide/inline.py)."""
import json, os, sys, html, re, subprocess, importlib.util
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEN = '/Users/martindrendel/741website/00_project/audit-workflow/scripts/build_report.py'
GUIDE = '/Users/martindrendel/741website/00_project/assets/brand/martin-guide'
CSS = re.search(r'CSS = """(.*?)"""', open(GEN).read(), re.S).group(1)
L = lambda n: json.load(open(os.path.join(RUN, n)))
run, F, KW = L('run.json'), L('findings.json'), L('keywords.json')
FB = {f['field_id']: f for f in F}
e = lambda s: html.escape(str(s if s is not None else ''), quote=True)
guide = '--guide' in sys.argv

# Client texts in English (facts from findings.json, field dates in brackets are the collection dates).
TXT = {
    'B05.03': 'Your profile has 100 reviews with a 4.7 rating. Three new reviews came in during the last two weeks.',
    'B05.04': 'None of the 7 reviews we checked has a reply from the clinic.',
    'B05.06': 'For "naturopath" and some niche treatments, your profile is highly visible in Canggu. For "iv drip therapy bali", "skin tag removal bali" and "acupuncture bali", visibility is between 0 and 2 %.',
    'B06.03': 'Two important service pages, IV drips and acupuncture, are hidden from Google. We check with you whether this is intended.',
    'B10.01': 'Your profile has 9 categories. The leading profiles for ozone and IV drips also use the category "Medical clinic". We check with you whether it fits your clinic.',
    'B12.01': 'ChatGPT and Google\'s AI Mode name your clinic for ozone searches. Gemini does not.',
    'B13.03': 'The profile name contains service words. We agree with you on the official name as it appears on your sign, because Google can object to names that differ from it.',
}
LABEL = {'B05.03': 'Reviews', 'B05.04': 'Review replies', 'B05.06': 'Visibility per search term', 'B06.03': 'Pages hidden from Google',
         'B10.01': 'Profile categories', 'B12.01': 'AI answers', 'B13.03': 'Profile name'}
BLOCKS = [('Google profile and Maps', ['B05.06', 'B05.03', 'B05.04', 'B10.01', 'B13.03']), ('Website', ['B06.03']), ('AI answers', ['B12.01'])]
ACTIONS = [('Make the IV drip and acupuncture pages visible to Google again, once you confirm that this is intended.', 5, 'S', '741'),
           ('Agree on the official business name and use exactly that name in the profile.', 5, 'S', 'You and 741'),
           ('Check the profile categories together, for example "Medical clinic".', 4, 'S', 'You and 741')]
DOT = {'green': ('●', 'good'), 'yellow': ('●', 'needs work'), 'red': ('●', 'urgent')}
def dot(st): g, t = DOT.get(st, ('○', 'open')); return f'<span class="dot {st}" title="{t}"><b aria-hidden="true">{g}</b><span class="sr">{t}</span></span>'
def date_of(f): d = f['collected_at']; return f"{int(d[8:10])} {['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][int(d[5:7])-1]}"
def mg(pose, alt, text, mod=''):
    if not guide: return ''
    return f'<aside class="mg {mod}" data-reveal><img class="mg__img" src="poses/martin-{pose}.webp" alt="Martin from 741 {alt}" width="112"><div class="mg__bubble"><span class="mg__name">Martin</span><p>{e(text)}</p></div></aside>'
def kw_rows():
    r = []
    for k in KW:
        if k['priority'] != 1: continue
        g = k['falcon']['google'] or {}; s = g.get('solv'); lead = k.get('leader'); vol = k.get('volume_indonesia')
        r.append(f'<div class="kw"><div><b>{e(k["keyword"])}</b><div class="note">Searches per month in Indonesia: {vol if vol else "no data"}</div></div>'
                 f'<div><div class="bar" role="img" aria-label="Top-3 share {s} percent"><i style="width:{max(2, s or 0)}%"></i></div><div class="note">Top-3 share in Maps {s:.0f} % · average rank {g.get("arp") if g.get("arp") is not None else "–"}</div></div>'
                 f'<div class="note">{("Leading: " + e(lead["name"][:34]) + f" {lead["solv"]:.0f} %") if lead else ""}</div></div>')
    return ''.join(r)
def rows(ids):
    out = []
    for i in ids:
        f = FB[i]; assert f['client_safe'], i
        out.append(f'<tr><td>{dot(f["status"])}</td><td>{e(LABEL[i])}</td><td>{e(TXT[i])}</td><td><span class="badge">Google data · {date_of(f)}</span></td></tr>')
    return '<div style="overflow-x:auto"><table><thead><tr><th></th><th>Area</th><th>Finding</th><th>Source</th></tr></thead><tbody>' + ''.join(out) + '</tbody></table></div>'
acts = ''.join(f"<tr><td><b>{n}</b></td><td>{e(t)}</td><td>{'●' * i}{'○' * (5 - i)}</td><td>{e(eff)}</td><td>{e(who)}</td></tr>" for n, (t, i, eff, who) in enumerate(ACTIONS, 1))
head_guide = '<link rel="stylesheet" href="martin-guide.css">' if guide else ''
tail_guide = '<script src="martin-guide.js" defer></script>' if guide else ''
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Your visibility on Google Maps</title><style>{CSS}</style>{head_guide}</head><body><div class="wrap">
<div class="top"><h1>{e(run['subject_name'])} · Visibility on Google Maps</h1><div class="meta">As of 11 October 2026</div></div><span class="draft">Draft – not released yet</span>
<div class="grid2"><div class="card"><div class="meta">Maps readiness</div><div class="score">{run['score_total']}<small> / 100</small></div><div class="note">First measurement. It is the starting point for the next months.</div></div>
<div class="card"><h3>What the result says</h3><p>Your clinic has strong reviews and is very visible for some treatments. For IV drips, skin tag removal and acupuncture, your profile is hardly visible in Maps yet. The biggest levers are two service pages that Google cannot see, the profile name, and the categories in the profile.</p></div></div>
{mg('point', 'points at the score', f"{run['score_total']} of 100 is your starting point. I measure the same way again, so you see every change.")}
<h2>Where you stand</h2><div class="card">{kw_rows()}<p class="note">Google Maps, grid of 49 points around Canggu, radius 5 miles. Ozone measured on 5 October, the other terms on 10 October 2026.</p></div>
<h2>The first steps</h2><div class="card"><table><thead><tr><th></th><th>Step</th><th>Effect</th><th>Effort</th><th>Who</th></tr></thead><tbody>{acts}</tbody></table><p class="note">We change the profile, the website or directory entries only after your approval.</p></div>
{mg('insight', 'with an idea', 'The fastest lever: two of your service pages are hidden from Google. That is a quick fix once you say yes.', 'mg--right mg--flip')}
<h2>Details</h2>{''.join(f'<h3 style="margin:14px 0 6px">{e(t)}</h3><div class="card">{rows(ids)}</div>' for t, ids in BLOCKS)}
<footer>Source: Google data. Measurements from 23 September to 11 October 2026.</footer></div>{tail_guide}</body></html>"""
os.makedirs(os.path.join(RUN, 'report'), exist_ok=True)
out = os.path.join(RUN, 'report', 'client.html')
if guide:
    tmp = os.path.join(RUN, 'report', '_client_guide_src.html'); open(tmp, 'w').write(page.replace('href="martin-guide.css"', 'href="/review-assets/martin-guide/martin-guide.css"').replace('src="martin-guide.js"', 'src="/review-assets/martin-guide/martin-guide.js"'))
    subprocess.run(['python3', os.path.join(GUIDE, 'inline.py'), tmp, out], check=True); os.remove(tmp)
else:
    open(out, 'w').write(page); print('written', out)
