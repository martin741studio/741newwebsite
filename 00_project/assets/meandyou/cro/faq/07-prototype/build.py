"""Build the CRO prototype of the me&you page "FAQ" (desktop 1440 px). Text = 04-copy/approved-copy.md (parsed, never retyped).
Design system = homepage + seminar + Michael + rhetorik page (imported). CTA = Gespräch buchen (termin.html, utm_source=faq). Run: python3 build.py"""
import importlib.util, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


rh = load('rh_build', os.path.join(HERE, '..', '..', 'rhetorik', '07-prototype', 'build.py'))
mic, sem, home = rh.mic, rh.sem, rh.home
V2 = sem.V2
BOOK = V2 + 'termin.html?utm_source=faq&utm_content='
TEL = sem.TEL
e, STARS, CHECK, t = home.e, home.STARS, home.CHECK, sem.t
LINKS = {'/': V2 + 'index.html', '/seminare': V2 + 'seminare.html', '/seminare#termine': V2 + 'seminare.html#termine',
         '/michael': V2 + 'michael.html', '/rhetorik': V2 + 'rhetorik.html', '/stimmen': V2 + 'index.html#stimmen',
         '/gespraech-buchen': BOOK + 'textlink'}
GROUPS = [('S03', 'seminar', '01'), ('S04', 'orte', '02'), ('S05', 'ablauf', '03'), ('S06', 'kosten', '04'),
          ('S07', 'gespraech', '05'), ('S08', 'michael', '06'), ('S09', 'rhetorik', '07')]


def btn(utm, cls='btn'):
    return f'<a class="{cls}" href="{BOOK}{utm}">Gespräch buchen</a>'


# ---------- read the approved copy ----------
SRC = open(os.path.join(HERE, '..', '04-copy', 'approved-copy.md'), encoding='utf-8').read()
FM = dict(re.findall(r'(?m)^(title|meta): (.+)$', SRC.split('---', 2)[1]))
BODY = SRC.split('---', 2)[2].split('<!-- TECH -->')[0]
SEC = {m.group(1): [re.sub(r'^- ', '', l.strip()) for l in re.sub(r'<!--.*?-->', '', m.group(2), flags=re.S).splitlines() if l.strip()]
       for m in re.finditer(r'<!-- (S\d\d) .*?-->(.*?)<!-- /\1 -->', BODY, re.S)}


def md(s):
    """Inline markdown of the approved copy to HTML: placeholders yellow, links mapped to the v2 preview."""
    out, pos = '', 0
    for m in re.finditer(r'\[([^\]]+)\]\(([^)\s]+)\)', s):
        out += t(s[pos:m.start()])
        label, url = m.group(1), m.group(2)
        href = url if url.startswith('http') or url.startswith('#') else LINKS[url]
        out += f'<a class="tlink" href="{e(href)}">{e(label)}</a>'
        pos = m.end()
    return out + t(s[pos:])


def group(sid):
    L = SEC[sid]
    title = L[0][3:]
    qa, tail, i = [], [], 1
    while i < len(L):
        if L[i].startswith('### '):
            qa.append((L[i][4:], L[i + 1])); i += 2
        else:
            tail.append(L[i]); i += 1
    return title, qa, tail


# ---------- page parts ----------
CSS = rh.CSS + r"""
/* faq page additions */
.hero--faq{min-height:0;height:auto;max-height:none;padding:118px 0 60px;display:block}
.hero--faq .hero__in{display:grid;grid-template-columns:1.5fr .62fr;gap:52px;align-items:stretch}
.hero--faq .hero__txt{max-width:none;padding-top:0;gap:13px}
.hero--faq .body{max-width:40em}
.hero--faq h1{gap:6px}
.hero--faq h1 .big{font-size:62px;line-height:1.05}
.hero--faq h1 .kicker{font:400 34px/1.18 var(--serif);letter-spacing:-.01em;color:var(--ink)}
.hero__frame{border-radius:var(--r);overflow:hidden;min-height:480px;box-shadow:0 18px 40px rgba(42,38,34,.12)}
.hero__frame img{width:100%;height:112%;object-fit:cover;object-position:50% 18%}
.hero--faq .assure svg{color:var(--cta)}
.ftopics{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:6px 0 4px}
.chip{display:flex;align-items:center;gap:12px;padding:10px 14px;border:1.5px solid rgba(79,109,144,.28);border-radius:16px;font:500 16px/1.25 var(--sans);color:var(--ink);text-decoration:none;background:#fff;transition:background .18s,border-color .18s,color .18s,transform .18s}
.chip i{font:400 24px/1 var(--serif);font-style:normal;color:var(--cta)}
.chip:hover{border-color:var(--cta);color:var(--cta);transform:translateY(-1px)}
.chip.on{background:var(--cta);border-color:var(--cta);color:#fff}.chip.on i{color:#fff}
.subnav{position:fixed;top:96px;left:0;right:0;z-index:45;pointer-events:none;opacity:0;transform:translateY(-10px);transition:opacity .25s,transform .25s}
.subnav.show{opacity:1;transform:none}
.subnav .ftopics{pointer-events:auto;max-width:var(--w);margin:0 auto;display:flex;justify-content:center;gap:2px;padding:6px 8px;border-radius:999px;width:max-content;background:rgba(250,248,244,.9);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);box-shadow:0 6px 22px rgba(42,38,34,.07)}
.subnav .chip{padding:7px 14px;font-size:16px;border-radius:999px;background:transparent;white-space:nowrap;gap:6px;border-color:transparent}.subnav .chip:hover{border-color:rgba(79,109,144,.35)}.subnav .chip.on{background:var(--cta);border-color:var(--cta);color:#fff}.subnav .chip.on i{color:#fff}.subnav .chip i{display:none}
.subnav.show .ftopics{pointer-events:auto}
.subnav:not(.show) *{pointer-events:none}
.badges4{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.badges4 .badge b{font-size:30px;color:var(--cta)}
.fgrp{padding:88px 0}
section.fgrp[id]{scroll-margin-top:150px}
.grpgrid{display:grid;grid-template-columns:.42fr 1fr;gap:72px;align-items:start}
.grphead{position:sticky;top:170px;display:flex;flex-direction:column;gap:18px}
.grphead .num{font:400 76px/1 var(--serif);color:var(--cta)}
.grphead .numrow{display:flex;align-items:flex-end;gap:22px}
.grphead h2{font-size:42px;line-height:1.12}
.grphead .more{font-size:17px;color:var(--muted)}
.grphead .stand{margin:0;color:var(--muted);font:italic 400 17px/1.4 var(--serif)}
.grphead .mini{background:#fff;border-radius:18px;padding:22px 22px 24px;display:flex;flex-direction:column;gap:14px;font:400 19px/1.35 var(--serif)}
.grphead .fpt{width:150px;height:190px;border-radius:18px;overflow:hidden}
.grphead .fpt img{width:100%;height:100%;object-fit:cover;object-position:50% 20%}
.places6{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px}
.places6 span{padding:7px 15px;border-radius:999px;background:var(--paper);font-size:16px;color:var(--muted)}
.acc1{background:#fff;border-radius:var(--r);padding:6px 28px;box-shadow:0 1px 0 var(--line)}
.sec--cream .acc1{box-shadow:none}
.acc1 details{border-bottom:1px solid var(--line)}
.acc1 details:last-child{border-bottom:0}
.acc1 summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:18px 1fr 24px;align-items:center;gap:14px;padding:19px 0;font:600 18px/1.45 var(--sans);color:var(--ink)}
.acc1 summary::-webkit-details-marker{display:none}
.acc1 summary::before{content:"";width:0;height:0;border-left:7px solid var(--cta);border-top:5px solid transparent;border-bottom:5px solid transparent;transition:transform .25s}
.acc1 summary::after{content:"+";font:300 28px/1 var(--sans);color:var(--cta);text-align:right;transition:transform .25s}
.acc1 summary:hover{color:var(--cta)}
.acc1 details[open] summary::before{transform:rotate(90deg)}
.acc1 details[open] summary::after{content:"\2212"}
.acc1 .a{padding:0 40px 24px 32px;color:var(--muted);font-size:18px;line-height:1.65}
.acc1 .a .tlink{font-weight:600}
.acc2{display:grid;grid-template-columns:1fr 1fr;column-gap:22px;align-items:start}
.acc2 .acc1{padding:6px 24px}
.acc2 summary{font-size:17px}
.acc2 .a{padding:0 18px 22px 32px;font-size:17px}
.places6 span{background:#fff;border:1.5px solid rgba(79,109,144,.2)}
.sec--cream .places6 span{background:#fff}
.closer .links{color:rgba(255,255,255,.85);font-size:17px}.closer .links a{color:#fff}
#kurz .ans{font:400 20px/1.6 var(--sans);color:var(--ink);max-width:32em}
"""


def header():
    return f'''<header class="hdr"><div class="hdr__in">
 <a class="hdr__logo" href="{V2}index.html"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication, Startseite" width="1794" height="647"></a>
 <nav aria-label="Hauptnavigation"><a href="{V2}seminare.html">Seminare</a><a href="{V2}michael.html">Michael</a><a href="{V2}rhetorik.html">Was ist Rhetorik</a><a href="{V2}index.html#stimmen">Stimmen</a><a href="#top" aria-current="page" style="color:var(--cta)">FAQ</a></nav>
 {btn('header')}
</div></header>'''


def chips():
    names = re.findall(r'\[([^\]]+)\]\(#([a-z]+)\)', SEC['S01'][3])
    return ''.join(f'<a class="chip" href="#{a}" data-t="{a}"><i>{n:02d}</i>{e(x)}</a>' for n, (x, a) in enumerate(names, 1))


def s01():
    L = SEC['S01']
    h1 = L[1][2:]
    return f'''
<section class="hero hero--faq" id="top">
 <div class="wrap hero__in"><div class="hero__txt">
  <p class="proofline rv">{STARS} {e(L[0])}</p>
  <h1 class="rv"><span class="big">{e(h1[:14])}</span><span class="kicker">{e(h1[15:])}</span></h1>
  <p class="body rv">{e(L[2])}</p>
  <nav class="ftopics rv" aria-label="Themen">{chips()}</nav>
  <div class="cta-row rv">{btn('hero', 'btn cta--breathe')}<p class="assure">{CHECK}{e(L[5])}</p></div>
 </div>
 <div class="hero__frame rv"><img data-plx src="assets/michael-door.webp" alt="Michael Ehlers, Rhetoriktrainer, lächelnd im weißen Hemd an einem Türrahmen" width="1200" height="1800"></div>
 </div>
</section>
<div class="subnav" aria-hidden="true"><nav class="ftopics">{chips()}</nav></div>'''


def s02():
    L = SEC['S02']
    tiles = []
    for x in L[2:6]:
        m = re.match(r'\*\*(.+?)\*\*:?\s*(.*)', x) or re.match(r'(\S+ \S+)\s*(.*)', x)
        tiles.append(m.groups())
    b = ''.join(f'<div class="badge"><b>{e(k.rstrip(":"))}</b><span>{e(v)}</span></div>' for k, v in tiles)
    qm = re.match(r'(„.+“) (.+)', L[6])
    return f'''
<section class="proof" id="kurz">
 <div class="wrap"><div class="proof__grid">
  <div class="stack rv"><h2>{e(L[0][3:])}</h2><p class="ans">{e(L[1])}</p></div>
  <div class="rv" data-in><div class="badges4">{b}</div>
   <p class="pquote">{e(qm.group(1))}<small>{e(qm.group(2))}</small></p></div>
 </div></div>
</section>'''


def s_group(sid, anchor, num, cream):
    title, qa, tail = group(sid)
    def det(i, q, a):
        return f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><div class="a">{md(a)}</div></details>'
    if anchor in ('ablauf', 'rhetorik'):
        h = (len(qa) + 1) // 2
        acc = f'<div class="acc2" data-grp="{anchor}"><div class="acc1">' + ''.join(det(i, q, a) for i, (q, a) in enumerate(qa[:h])) + '</div><div class="acc1">' + ''.join(det(1, q, a) for q, a in qa[h:]) + '</div></div>'
    else:
        acc = f'<div class="acc1" data-grp="{anchor}">' + ''.join(det(i, q, a) for i, (q, a) in enumerate(qa)) + '</div>'
    items = acc
    pt = '<div class="fpt"><img src="assets/michael-jacket.webp" alt="Michael Ehlers im braunen Sakko" width="787" height="1122"></div>' if anchor == 'michael' else ''
    head = [f'<div class="numrow"><span class="num" aria-hidden="true">{num}</span>{pt}</div>', f'<h2>{e(title)}</h2>']
    after = ''
    for x in tail:
        if x == '**Gespräch buchen**':
            if anchor == 'gespraech':
                head.append(f'<div class="mini">30 Minuten, kostenlos, per Video.{btn(anchor)}</div>')
            else:
                head.append(f'<div class="cta-row">{btn(anchor)}</div>')
        elif x.startswith('Stand der Termine'):
            after += f'<p class="stand" style="margin-top:22px;font:italic 400 17px/1.4 var(--serif);color:var(--muted)">{e(x)}</p>'
        else:
            head.insert(2, f'<p class="more">{md(x)}</p>')
    pre = ''
    if anchor == 'orte':
        pre = '<div class="places6">' + ''.join(f'<span>{p}</span>' for p in ['Mallorca', 'Barcelona', 'Dubai', 'Zypern', 'Frankfurt', 'Berlin']) + '</div>'
    return f'''
<section class="fgrp{' sec--cream' if cream else ''}" id="{anchor}">
 <div class="wrap grpgrid">
  <div class="grphead rv">{''.join(head)}</div>
  <div class="rv">{pre}{items}{after}</div>
 </div>
</section>'''


def s10():
    L = SEC['S10']
    li = ''.join(f'<li>{CHECK}<span>{md(x)}</span></li>' for x in L[2:5])
    foot = home.section_closer().split('<footer', 1)[1]
    foot = '<footer' + foot.replace(home.BOOK, BOOK).replace('href="#termine"', f'href="{V2}seminare.html#termine"').replace(f'href="{V2}faq.html">FAQ', 'href="#top">FAQ')
    return f'''
<section class="closer" id="abschluss">
 <div class="closer__bg"><img data-plx src="assets/closer-terrace.webp" alt="Abendstimmung auf einer Steinterrasse über dem Meer, Menschen im Gespräch" width="1536" height="1024"></div>
 <div class="wrap"><div class="closer__in">
  <h2 class="rv">{e(L[0][3:])}</h2>
  <p class="rv">{e(L[1])}</p>
  <ul class="rv">{li}</ul>
  <p class="proofline rv">{STARS} {e(L[5])}</p>
  <div class="cta-row rv">{btn('abschluss', 'btn btn--light cta--breathe')}<p class="tel">Lieber anrufen: <a href="{TEL}">+49 15888367664</a></p></div>
  <p class="links rv">Zurück zur <a href="{V2}index.html">Startseite</a></p>
 </div></div>
</section>
{foot}'''


JS = home.JS.replace(""" // one FAQ open at a time
 var ds = document.querySelectorAll('.acc details');
 ds.forEach(function(d){ d.addEventListener('toggle', function(){ if(d.open){ ds.forEach(function(o){ if(o!==d) o.open=false; }); } }); });""",
""" // one answer open per group (user clicks only; the first answer of each group starts open)
 document.querySelectorAll('[data-grp]').forEach(function(g){ var ds = g.querySelectorAll('details');
  ds.forEach(function(d){ d.querySelector('summary').addEventListener('click', function(){ if(!d.open){ ds.forEach(function(o){ if(o!==d) o.open=false; }); } }); }); });
 // sticky topic bar after the hero, active topic marked
 var bar = document.querySelector('.subnav'), hero = document.querySelector('.hero');
 var end = document.querySelector('#abschluss');
 function sb(){ var show = hero.getBoundingClientRect().bottom < 90 && end.getBoundingClientRect().top > 220; bar.classList.toggle('show', show); bar.setAttribute('aria-hidden', show ? 'false' : 'true'); }
 addEventListener('scroll', sb, {passive:true}); sb();
 var secs = [].slice.call(document.querySelectorAll('section.fgrp'));
 function act(){ var cur = ''; secs.forEach(function(s){ if(s.getBoundingClientRect().top < 220) cur = s.id; });
  document.querySelectorAll('.subnav .chip').forEach(function(c){ c.classList.toggle('on', c.getAttribute('data-t') === cur); }); }
 addEventListener('scroll', act, {passive:true}); act();""")
assert 'one answer open per group' in JS


def schema():
    ORG = 'https://www.meandyou.de/#organization'
    g = [{"@type": "WebPage", "@id": "https://www.meandyou.de/faq#webpage", "url": "https://www.meandyou.de/faq", "name": FM['title'], "description": FM['meta'], "inLanguage": "de", "about": {"@id": ORG}},
         {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://www.meandyou.de/"}, {"@type": "ListItem", "position": 2, "name": "FAQ", "item": "https://www.meandyou.de/faq"}]},
         {"@type": "EducationalOrganization", "@id": ORG, "name": "Institut Michael Ehlers GmbH", "alternateName": "me&you Communication", "url": "https://www.meandyou.de/", "email": "management@meandyou.de"}]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False)


def page():
    grp = ''.join(s_group(sid, a, n, i % 2 == 1) for i, (sid, a, n) in enumerate(GROUPS))
    body = header() + '<main>' + s01() + s02() + grp + '</main>' + s10() + '<div class="proto">Prototyp · nicht live · gelb = [FEHLT]</div>'
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{e(FM['title'])}</title>
<meta name="description" content="{e(FM['meta'])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{schema()}</script>
</head><body>{body}<script>{JS}</script></body></html>'''


if __name__ == '__main__':
    out = page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out))
