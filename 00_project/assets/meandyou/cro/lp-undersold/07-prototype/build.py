"""Build the CRO prototype of the me&you landing page "The Undersold" (desktop 1440 px).
Text = 04-copy/approved-copy.md (parsed, never retyped). Design system = homepage + seminar page (imported).
Persona rules: wide golden images, few elements per screen, places and dates as headings, ONE button in the content (S11),
header button stays. CTA = Gespräch buchen (termin.html, utm_source=lp-undersold; site-build maps it to gespraech-buchen.html).
Run: python3 build.py  ->  index.html"""
import importlib.util, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


sem = load('sem_build', os.path.join(HERE, '..', '..', 'seminare', '07-prototype', 'build.py'))
home = sem.home
V2 = sem.V2
BOOK = V2 + 'termin.html?utm_source=lp-undersold&utm_content='
TEL = sem.TEL
e, STARS, CHECK, t = home.e, home.STARS, home.CHECK, sem.t
LINKS = {'/': V2 + 'index.html', '/seminare': V2 + 'seminare.html', '/michael': V2 + 'michael.html',
         '/rhetorik': V2 + 'rhetorik.html', '/stimmen': V2 + 'stimmen.html', '/faq': V2 + 'faq.html',
         '/gespraech-buchen': BOOK + 'abschluss'}


def btn(utm, cls='btn'):
    return f'<a class="{cls}" href="{BOOK}{utm}">Gespräch buchen</a>'


# ---------- read the approved copy ----------
SRC = open(os.path.join(HERE, '..', '04-copy', 'approved-copy.md'), encoding='utf-8').read()
FM = dict(re.findall(r'(?m)^(title|meta): (.+)$', SRC.split('---', 2)[1]))
BODY = SRC.split('---', 2)[2].split('<!-- TECH -->')[0]
SEC = {m.group(1): [l.strip() for l in re.sub(r'<!--.*?-->', '', m.group(2), flags=re.S).splitlines() if l.strip()]
       for m in re.finditer(r'<!-- (S\d\d) .*?-->(.*?)<!-- /\1 -->', BODY, re.S)}


def md(s):
    """Inline markdown to HTML: **bold**, links mapped to the v2 preview, placeholders yellow."""
    s = re.sub(r'^(- |\d+\. )', '', s)
    out, pos = '', 0
    for m in re.finditer(r'\*\*(.+?)\*\*|\[([^\[\]]+)\]\(([^)\s]+)\)', s):
        out += t(s[pos:m.start()])
        if m.group(1) is not None:
            out += f'<b>{t(m.group(1))}</b>'
        else:
            url = m.group(3)
            href = url if url.startswith(('http', '#')) else LINKS[url]
            out += f'<a class="tlink" href="{e(href)}">{e(m.group(2))}</a>'
        pos = m.end()
    return out + t(s[pos:])


def plain(s):
    return re.sub(r'\*\*', '', re.sub(r'^(- |\d+\. )', '', s))


def bold_split(s):
    """'- **Title.** Rest' -> ('Title.', 'Rest')"""
    m = re.match(r'(?:- |\d+\. )?\*\*(.+?)\*\*:?\s*(.*)', s)
    return (m.group(1), m.group(2)) if m else ('', s)


def quote_split(s):
    m = re.match(r'(„.+“)\s+(.+)$', s)
    return m.groups() if m else (s, '')


CSS = sem.CSS + r"""
/* lp-undersold additions: wide, warm, golden, few elements */
.hdr nav a[aria-current]{color:var(--cta)}
.u-hero{position:relative;height:100vh;min-height:760px;max-height:860px;overflow:hidden;color:var(--on-dark)}
.u-hero__bg{position:absolute;inset:0}.u-hero__bg img{width:100%;height:114%;object-fit:cover;object-position:50% 46%;margin-top:-3%}
.u-hero::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(32,26,20,.78) 0%,rgba(32,26,20,.5) 38%,rgba(32,26,20,0) 66%),linear-gradient(0deg,rgba(32,26,20,.35) 0%,rgba(32,26,20,0) 30%)}
.u-hero__in{position:relative;z-index:2;height:100%;display:flex;align-items:center;padding-top:70px}
.u-hero__txt{max-width:900px;display:flex;flex-direction:column;gap:16px}
.u-hero .proofline{color:rgba(242,237,228,.92);white-space:nowrap}
.u-hero h1{display:flex;flex-direction:column;gap:16px}
.u-hero h1 .kicker{font:600 16px/1.3 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--sand)}
.u-hero h1 .big{font-size:58px;line-height:1.12;color:#fff;max-width:15.5em}
.u-hero .sub{font:italic 400 22px/1.45 var(--serif);color:var(--on-dark);max-width:34em}
.u-hero .body{font-size:18px;color:rgba(242,237,228,.86);max-width:32em}
.u-hero .anchor{display:inline-flex;align-items:center;gap:10px;margin-top:6px;font:600 17px/1 var(--sans);color:#fff;text-decoration:none;border-bottom:1.5px solid rgba(216,204,183,.6);padding-bottom:6px;align-self:flex-start}
.u-hero .anchor span{transition:transform .2s}.u-hero .anchor:hover span{transform:translateY(3px)}
.gold{color:var(--gold)}
.u-format .fehlt,.u-incl .fehlt,.u-cstep .fehlt,.u-bundle .fehlt{display:inline;padding:1px 6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.hair{border-top:1px solid rgba(201,162,74,.45)}
/* S02 */
.u-kurz{padding:120px 0 110px}
.u-kurz__grid{display:grid;grid-template-columns:1fr 1.12fr;gap:72px;align-items:start}
.u-kurz h2{font-size:40px;margin-bottom:26px}
.u-kurz .ans{font:400 21px/1.62 var(--serif);color:var(--ink)}
.u-facts{display:grid;grid-template-columns:1fr 190px;gap:34px;align-items:start}
.u-facts ul{list-style:none;margin:0;padding:0}
.u-facts li{display:grid;grid-template-columns:150px 1fr;gap:20px;align-items:center;padding:16px 0;border-top:1px solid rgba(201,162,74,.45)}
.u-facts li:last-child{border-bottom:1px solid rgba(201,162,74,.45)}
.u-facts b{font:400 34px/1.05 var(--serif);color:var(--gold);white-space:nowrap}
.u-facts span{font-size:16px;color:var(--muted)}
.u-facts .pt{border-radius:18px;overflow:hidden;height:290px}
.u-facts .pt img{width:100%;height:100%;object-fit:cover;object-position:50% 20%}
.u-facts .pt-cap{font-size:15px;color:var(--muted);margin-top:8px;line-height:1.35}
.u-q{margin-top:56px;padding-top:30px;border-top:1px solid var(--line);font:italic 400 22px/1.5 var(--serif);max-width:46em}
.u-q small{display:block;margin-top:10px;font:500 16px/1.3 var(--sans);font-style:normal;color:var(--muted)}
/* S03 dark */
.u-dark{background:var(--char);color:var(--on-dark);padding:130px 0}
.u-dark h2{color:#fff;font-size:44px;max-width:16em}
.u-dark .lead{color:rgba(242,237,228,.85);margin-top:22px}
.u-dtop{display:grid;grid-template-columns:.9fr 1.1fr;gap:80px;align-items:start}
.u-sits{display:grid;grid-template-columns:1fr 1fr;gap:40px 48px}
.u-sit{padding-top:22px;border-top:1px solid rgba(216,204,183,.35)}
.u-sit h3{font-size:24px;color:var(--sand);margin-bottom:10px}
.u-sit p{font-size:18px;color:rgba(242,237,228,.86)}
.u-dark .close{margin:72px auto 0;font:italic 400 24px/1.5 var(--serif);color:#fff;max-width:40em;text-align:center}
/* S04 method */
.u-method{display:grid;grid-template-columns:.95fr 1.25fr;gap:80px;align-items:start}
.u-method .lead{margin-top:22px}
.u-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:34px;position:relative;padding-top:8px}
.u-steps::before{content:"";position:absolute;top:30px;left:0;right:0;height:1px;background:rgba(201,162,74,.5)}
.u-step{position:relative;display:flex;flex-direction:column;gap:12px}
.u-step i{font:400 46px/1 var(--serif);font-style:normal;color:var(--gold);background:var(--cream);padding-right:14px;align-self:flex-start;position:relative}
.u-step h3{font-size:25px}.u-step p{color:var(--muted);font-size:17px}
/* S05 places */
.u-places{padding:120px 0 110px}
.u-places .head{text-align:center;max-width:760px;margin:0 auto}
.u-places .head .lead{margin:20px auto 0}
.u-pgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;margin-top:56px;align-items:start}
.u-place{background:#fff;border-radius:var(--r);overflow:hidden;box-shadow:0 1px 0 var(--line)}
.u-place__img{overflow:hidden;aspect-ratio:16/9}
.u-place__img img{width:100%;height:100%;object-fit:cover;transition:transform .6s cubic-bezier(.22,1,.36,1)}
.u-place:hover .u-place__img img{transform:scale(1.03)}
.u-place h3{font-size:32px;margin:22px 26px 0}
.u-place .fm{font:500 16px/1.3 var(--sans);color:var(--muted);margin:6px 26px 0}
.u-place .ds{list-style:none;margin:12px 26px 26px;padding:0;display:flex;flex-direction:column;gap:6px}
.u-place .ds li{font:400 18px/1.4 var(--serif);color:var(--ink);display:flex;gap:10px;align-items:baseline}
.u-place .ds li::before{content:"";flex:none;width:6px;height:6px;border-radius:50%;background:var(--gold);transform:translateY(-3px)}
.u-places .after{display:block;margin:64px auto 0;max-width:760px;text-align:center}
.u-places .after p{font-size:18px;color:var(--muted)}
.u-places .after .u-q{margin:30px auto 0;border-top:0;padding-top:0}
/* S06 format */
.u-band{position:relative;height:500px;overflow:hidden}
.u-band__bg{position:absolute;inset:0}.u-band__bg img{width:100%;height:116%;object-fit:cover;object-position:50% 40%;margin-top:-4%}
.u-band::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(32,26,20,.72) 0%,rgba(32,26,20,.2) 50%,rgba(32,26,20,0) 75%)}
.u-band .wrap{position:relative;z-index:2;height:100%;display:flex;align-items:flex-end;padding-bottom:70px}
.u-band h2{color:#fff;font-size:50px;max-width:15em}
.u-format{padding:84px 0 120px}
.u-format .lead1{font:italic 400 24px/1.4 var(--serif);color:var(--ink)}
.u-cols{display:grid;grid-template-columns:repeat(4,1fr);gap:34px;margin-top:44px}
.u-col{border-top:2px solid var(--gold);padding-top:20px;display:flex;flex-direction:column;gap:10px}
.u-col h3{font:600 18px/1.35 var(--sans)}
.u-col p{font-size:17px;color:var(--muted)}
.u-fmts{margin-top:80px}
.u-fmts .intro{max-width:52em;margin-bottom:24px}
.u-bi{display:grid;grid-template-columns:1fr 1fr;gap:48px;margin-top:34px;align-items:start}
.u-fmts h3.big{font-size:34px;margin-bottom:18px}
.u-fmts .intro{font-size:18px;color:var(--muted)}
.u-rows{list-style:none;margin:0;padding:0}
.u-rows li{display:grid;grid-template-columns:.75fr 1.4fr;gap:40px;padding:22px 0;border-top:1px solid var(--line);align-items:baseline}
.u-rows li:last-child{border-bottom:1px solid var(--line)}
.u-rows .n{font:400 22px/1.3 var(--serif);color:var(--ink)}
.u-rows .n small{display:block;margin-top:6px;font:500 16px/1.3 var(--sans);color:var(--muted);letter-spacing:.02em}
.u-rows .d{font-size:17px;color:var(--muted)}
.u-bundle{font-size:17px;color:var(--muted)}
.u-incl{background:var(--cream);border-radius:var(--r);padding:26px 30px;font-size:17px;color:var(--muted)}
.u-incl b{display:block;font:600 14px/1.2 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--ink);margin-bottom:10px}
/* S07 who */
.u-who{display:grid;grid-template-columns:1.05fr .95fr;gap:88px;align-items:start}
.u-who ul{list-style:none;margin:30px 0 0;padding:0;display:flex;flex-direction:column}
.u-who li{display:flex;gap:14px;padding:16px 0;border-top:1px solid var(--line);font-size:18px}
.u-who li:last-child{border-bottom:1px solid var(--line)}
.u-who li svg{width:20px;height:20px;color:var(--gold);flex:none;margin-top:4px}
.u-who .bline{margin-top:20px;font-size:17px;color:var(--muted)}
.u-bigq{font:italic 400 30px/1.45 var(--serif);color:var(--ink);padding:30px 0 0 40px;border-left:1px solid rgba(201,162,74,.6);margin-top:70px}
.u-bigq .lead2{display:block;font:400 18px/1.55 var(--sans);font-style:normal;color:var(--muted);margin-bottom:22px}
.u-bigq small{display:block;margin-top:16px;font:500 16px/1.3 var(--sans);font-style:normal;color:var(--muted)}
.u-not{margin-top:56px;padding-top:26px;border-top:1px solid var(--line);font-size:18px;color:var(--muted)}
.u-not em{font:italic 400 19px/1.5 var(--serif);color:var(--ink)}
/* S08 michael */
.u-mic{display:grid;grid-template-columns:.8fr 1.2fr;gap:84px;align-items:center}
.u-mic .portrait{height:600px}
.u-mic h2{font-size:40px}
.u-mic p{font-size:18px;color:var(--muted)}
.u-cred{list-style:none;margin:8px 0 0;padding:0}
.u-cred li{display:block;padding:15px 0;border-top:1px solid rgba(201,162,74,.45);font-size:17.5px;color:var(--muted)}
.u-cred li:last-child{border-bottom:1px solid rgba(201,162,74,.45)}
.u-cred b{font:400 21px/1.3 var(--serif);color:var(--ink);margin-right:6px}
/* S09 voices */
.u-voices .qgrid{grid-template-columns:repeat(3,1fr)}
.u-voices .q h3{font:400 22px/1.3 var(--serif)}
.u-voices .q blockquote{font:italic 400 19px/1.55 var(--serif)}
.u-voices .more{margin-top:34px;font-size:17px;color:var(--muted)}
/* S10 faq */
.u-faq h2{font-size:38px;margin-bottom:34px}
.u-faq .morelinks{text-align:right}
/* S11 closer */
.u-closer{position:relative;overflow:hidden;color:var(--on-dark);padding:150px 0 130px}
.u-closer__bg{position:absolute;inset:0}.u-closer__bg img{width:100%;height:116%;object-fit:cover;margin-top:-4%}
.u-closer::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(28,24,20,.9) 0%,rgba(28,24,20,.78) 50%,rgba(28,24,20,.62) 100%)}
.u-closer .wrap{position:relative;z-index:2}
.u-closer h2{color:#fff;font-size:40px}
.u-closer .intro{font-size:19px;color:rgba(255,255,255,.9);max-width:34em;margin-top:22px}
.u-cgrid{display:grid;grid-template-columns:.85fr 1.35fr;gap:64px;align-items:start}
.u-csteps{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:8px}
.u-cstep{border-top:1px solid rgba(201,162,74,.6);padding-top:20px;display:flex;flex-direction:column;gap:10px}
.u-cstep i{font:400 34px/1 var(--serif);font-style:normal;color:var(--gold)}
.u-cstep h3{color:#fff;font-size:23px}
.u-cstep p{font-size:17px;color:rgba(242,237,228,.86)}
.u-closer .cta-row{margin-top:36px}
.u-closer .tel{color:rgba(255,255,255,.88);font-size:17px}.u-closer .tel a{color:#fff}
.u-closer .proofline{margin-top:56px;padding-top:24px;border-top:1px solid rgba(242,237,228,.18);color:rgba(255,255,255,.85)}
"""


def header():
    return f'''<header class="hdr"><div class="hdr__in">
 <a class="hdr__logo" href="{V2}index.html"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication, Startseite" width="1794" height="647"></a>
 <nav aria-label="Hauptnavigation"><a href="{V2}seminare.html">Seminare</a><a href="{V2}michael.html">Michael</a><a href="{V2}rhetorik.html">Was ist Rhetorik</a><a href="{V2}stimmen.html">Stimmen</a><a href="{V2}faq.html">FAQ</a></nav>
 {btn('header')}
</div></header>'''


def s01():
    L = SEC['S01']
    kicker, big = L[1][2:].split(': ', 1)
    link = re.match(r'\[(.+?)\]\((#\w+)\)', L[4])
    return f'''
<section class="u-hero" id="top">
 <div class="u-hero__bg"><img data-plx src="assets/hero-coast.webp" alt="Steinterrasse einer Finca über dem Meer auf Mallorca in der goldenen Stunde, eine kleine Gruppe im Gespräch" width="1536" height="1024"></div>
 <div class="wrap u-hero__in"><div class="u-hero__txt">
  <p class="proofline rv">{STARS} {e(L[0])}</p>
  <h1 class="rv"><span class="kicker">{e(kicker)}</span><span class="big">{e(big)}</span></h1>
  <p class="sub rv">{e(L[2])}</p>
  <p class="body rv">{e(L[3])}</p>
  <a class="anchor rv" href="{link.group(2)}">{e(link.group(1))} <span aria-hidden="true">&#8595;</span></a>
 </div></div>
</section>'''


def s02():
    L = SEC['S02']
    facts = []
    for x in L[2:6]:
        k, v = bold_split(x)
        m = re.match(r'([\d+ ]+(?:bis \d+)?)\s*(.*)', k)
        num, unit = (m.group(1).strip(), m.group(2)) if m else (k, '')
        lab = (unit + ' ' + v).strip() if unit else v
        lab = lab.replace(',:', ':')
        facts.append(f'<li><b>{e(num)}</b><span>{e(lab)}</span></li>')
    q, who = quote_split(L[6])
    return f'''
<section class="u-kurz" id="kurz">
 <div class="wrap u-kurz__grid">
  <div class="rv"><h2>{e(L[0][3:])}</h2><p class="ans">{e(L[1])}</p></div>
  <div class="u-facts rv" data-in><ul>{''.join(facts)}</ul>
   <div><div class="pt"><img src="assets/michael-jacket.webp" alt="Michael Ehlers, Rhetoriktrainer, im braunen Sakko" width="787" height="1122"></div></div></div>
 </div>
 <div class="wrap"><p class="u-q rv">{e(q)}<small>{e(who)}</small></p></div>
</section>'''


def s03():
    L = SEC['S03']
    sits = []
    for x in L[2:6]:
        k, v = bold_split(x)
        sits.append(f'<div class="u-sit rv"><h3>{e(k.rstrip("."))}</h3><p>{e(v)}</p></div>')
    return f'''
<section class="u-dark" id="lage">
 <div class="wrap">
  <div class="u-dtop"><div><h2 class="rv">{e(L[0][3:])}</h2>
  <p class="lead rv">{e(L[1])}</p></div>
  <div class="u-sits">{''.join(sits)}</div></div>
  <p class="close rv">{e(L[6])}</p>
 </div>
</section>'''


def s04():
    L = SEC['S04']
    st = []
    for i, x in enumerate(L[2:5], 1):
        k, v = bold_split(x)
        st.append(f'<div class="u-step"><i>0{i}</i><h3>{e(k.rstrip("."))}</h3><p>{e(v)}</p></div>')
    return f'''
<section class="sec sec--cream" id="methode">
 <div class="wrap u-method">
  <div class="rv"><h2>{e(L[0][3:])}</h2><p class="lead">{e(L[1])}</p></div>
  <div class="u-steps rv" data-in>{''.join(st)}</div>
 </div>
</section>'''


PLACE_IMG = {'Mallorca': 'city-mallorca.webp', 'Barcelona': 'city-barcelona.webp', 'Zypern': 'city-zypern.webp',
             'Dubai': 'city-dubai.webp', 'Frankfurt': 'city-frankfurt.webp', 'Berlin': 'city-berlin.webp'}


def s05():
    L = SEC['S05']
    cards, i = [], 2
    while i < len(L) and L[i].startswith('### '):
        name = L[i][4:]
        fm, rest = L[i + 1].split('. ', 1)
        ds = ''.join(f'<li>{e(d)}</li>' for d in rest.split(' · '))
        cards.append(f'<article class="u-place rv"><div class="u-place__img"><img src="assets/{PLACE_IMG[name]}" alt="Seminarort {e(name)}" width="1536" height="1024"></div>'
                     f'<h3>{e(name)}</h3><p class="fm">{e(fm)}</p><ul class="ds">{ds}</ul></article>')
        i += 2
    after, quote = L[i], L[i + 1]
    q, who = quote_split(quote)
    return f'''
<section class="u-places" id="orte">
 <div class="wrap">
  <div class="head"><h2 class="rv">{e(L[0][3:])}</h2><p class="lead rv">{e(L[1])}</p></div>
  <div class="u-pgrid">{''.join(cards)}</div>
  <div class="after"><p class="rv">{e(after)}</p><p class="u-q rv">{e(q)}<small>{e(who)}</small></p></div>
 </div>
</section>'''


def s06():
    L = SEC['S06']
    cols = []
    for x in L[2:6]:
        k, v = bold_split(x)
        cols.append(f'<div class="u-col"><h3>{e(k)}</h3><p>{t(v)}</p></div>')
    h3 = L[6][4:]
    intro = L[7]
    rows = []
    for x in L[8:11]:
        m = re.match(r'- \*\*(.+?)\*\* \((.+?)\): (.+)', x)
        rows.append(f'<li><div class="n">{e(m.group(1))}<small>{e(m.group(2))}</small></div><div class="d">{e(m.group(3))}</div></li>')
    return f'''
<section class="u-band" id="format">
 <div class="u-band__bg"><img data-plx src="assets/format-terrace.webp" alt="Kleine Seminargruppe auf einer Steinterrasse über dem Meer, eine Teilnehmerin spricht" width="1536" height="1024"></div>
 <div class="wrap"><h2 class="rv">{e(L[0][3:])}</h2></div>
</section>
<section class="u-format">
 <div class="wrap">
  <p class="lead1 rv">{e(L[1])}</p>
  <div class="u-cols rv" data-in>{''.join(cols)}</div>
  <div class="u-fmts">
   <div class="rv"><h3 class="big">{e(h3)}</h3><p class="intro">{t(intro)}</p></div>
   <ul class="u-rows rv">{''.join(rows)}</ul>
   <div class="u-bi rv"><p class="u-bundle">{md(L[11])}</p>
    <div class="u-incl"><b>Enthalten</b>{t(L[12])}</div></div>
  </div>
 </div>
</section>'''


def s07():
    L = SEC['S07']
    li = ''.join(f'<li>{CHECK}<span>{e(plain(x))}</span></li>' for x in L[1:5])
    pre, rest = L[6].split(': ', 1)
    q, = re.match(r'(„.+“)$', rest).groups()
    return f'''
<section class="sec sec--cream" id="fuer-wen">
 <div class="wrap">
  <div class="u-who">
   <div class="rv"><h2>{e(L[0][3:])}</h2><ul>{li}</ul><p class="bline">{e(L[5])}</p></div>
   <p class="u-bigq rv">{e(L[7])}</p>
  </div>
  <p class="u-not rv">{e(pre)}: <em>{e(q)}</em></p>
 </div>
</section>'''


def s08():
    L = SEC['S08']
    cred = []
    for x in L[2:6]:
        k, v = bold_split(x)
        cred.append(f'<li><b>{e(k)}</b>{e(v)}</li>')
    return f'''
<section class="sec" id="michael">
 <div class="wrap u-mic">
  <div class="portrait rv"><img data-plx src="assets/michael-olive.webp" alt="Michael Ehlers, Rhetoriktrainer, in olivgrüner Jacke" width="1066" height="1600"></div>
  <div class="stack">
   <h2 class="rv">{e(L[0][3:])}</h2>
   <p class="rv">{e(L[1])}</p>
   <ul class="u-cred rv">{''.join(cred)}</ul>
   <p class="rv">{md(L[6])}</p>
  </div>
 </div>
</section>'''


def s09():
    L = SEC['S09']
    cards, i = [], 2
    while i < len(L) and L[i].startswith('### '):
        q, who = quote_split(L[i + 1])
        cards.append(f'<article class="q rv"><h3>{e(L[i][4:])}</h3><blockquote>{e(q)}</blockquote><div class="who"><span>{e(who)}</span></div></article>')
        i += 2
    return f'''
<section class="sec sec--cream u-voices" id="stimmen">
 <div class="wrap">
  <h2 class="rv">{e(L[0][3:])}</h2>
  <p class="lead rv" style="margin-top:18px">{e(L[1])}</p>
  <div class="qgrid">{''.join(cards)}</div>
  <p class="more rv">{md(L[i])}</p>
 </div>
</section>'''


def s10():
    L = SEC['S10']
    qa, i = [], 1
    while i < len(L) and L[i].startswith('### '):
        qa.append((L[i][4:], L[i + 1])); i += 2
    det = ''.join(f'<details{" open" if n == 0 else ""}><summary>{e(q)}</summary><div class="a">{md(a)}</div></details>' for n, (q, a) in enumerate(qa))
    return f'''
<section class="sec u-faq" id="faq">
 <div class="wrap">
  <h2 class="rv">{e(L[0][3:])}</h2>
  <div class="rv"><div class="acc">{det}</div><p class="morelinks">{md(L[i])}</p></div>
 </div>
</section>'''


def s11():
    L = SEC['S11']
    st = []
    for n, x in enumerate(L[2:5], 1):
        k, v = bold_split(x)
        st.append(f'<div class="u-cstep"><i>0{n}</i><h3>{e(k.rstrip("."))}</h3><p>{t(v)}</p></div>')
    reassure, tel = L[6].split('. Lieber anrufen: ')
    foot = home.section_closer().split('<footer', 1)[1]
    foot = ('<footer' + foot.replace(home.BOOK, BOOK).replace('href="#termine"', f'href="{V2}seminare.html#termine"'))
    return f'''
<section class="u-closer" id="abschluss">
 <div class="u-closer__bg"><img data-plx src="assets/closer-terrace.webp" alt="Abendstimmung auf einer Steinterrasse über dem Meer, Menschen im Gespräch" width="1536" height="1024"></div>
 <div class="wrap">
  <div class="u-cgrid"><div><h2 class="rv">{e(L[0][3:])}</h2>
  <p class="intro rv">{e(L[1])}</p>
  <div class="cta-row rv">{btn('abschluss', 'btn btn--light cta--breathe')}<p class="tel">{CHECK.replace('<svg', '<svg style="width:18px;height:18px;color:var(--sand);vertical-align:-3px;margin-right:6px"')}{e(reassure)}. Lieber anrufen: <a href="{TEL}">{e(tel)}</a></p></div>
  </div>
  <div class="u-csteps rv" data-in>{''.join(st)}</div></div>
  <p class="proofline rv">{STARS} {e(L[7])}</p>
 </div>
</section>
{foot}'''


def schema():
    path = os.path.join(HERE, '..', '..', '..', 'content-writing', 'lp-undersold', '05-final', 'schema.jsonld')
    d = json.load(open(path, encoding='utf-8'))
    d.pop('_note', None)
    return json.dumps(d, ensure_ascii=False)


def page():
    body = (header() + '<main>' + s01() + s02() + s03() + s04() + s05() + s06() + s07() + s08() + s09() + s10() + '</main>'
            + s11() + '<div class="proto">Prototyp · nicht live · gelb = [FEHLT]</div>')
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{e(FM['title'])}</title>
<meta name="description" content="{e(FM['meta'])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{schema()}</script>
</head><body>{body}<script>{home.JS}</script></body></html>'''


if __name__ == '__main__':
    out = page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out))
