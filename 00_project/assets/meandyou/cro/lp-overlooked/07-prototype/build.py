"""Build the CRO prototype of the me&you landing page "The Overlooked" (desktop 1440 px).
Text = 04-copy/approved-copy.md, read through 05-gpt-design-doc/units.json (no retyped copy).
Design system = homepage + seminar + Michael page (imported), persona theme cool/navy. CTA = Gespräch buchen.
Run: python3 build.py"""
import importlib.util, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


mic = load('mic_build', os.path.join(HERE, '..', '..', 'michael', '07-prototype', 'build.py'))
sem, home = mic.sem, mic.home
V2 = sem.V2
TEL = sem.TEL
BOOK = V2 + 'termin.html?utm_source=lp-overlooked&utm_content='
e, STARS, CHECK, PLAY, t = home.e, home.STARS, home.CHECK, home.PLAY, sem.t
U = json.load(open(os.path.join(HERE, '..', '05-gpt-design-doc', 'units.json'), encoding='utf-8'))
HERO_IMG = 'hero-glass.webp' if os.path.exists(os.path.join(HERE, 'assets', 'hero-glass.webp')) else 'hero-temp.webp'


def btn(utm, cls='btn'):
    return f'<a class="{cls}" href="{BOOK}{utm}">Gespräch buchen</a>'


def assure(txt, dark=False):
    return f'<p class="assure{" assure--dark" if dark else ""}">{CHECK}{e(txt)}</p>'


def row(u):
    return [c.strip() for c in u.split(' | ')]


def lead_bold(u):
    """'01 Titel. Rest' or 'Titel. Rest' -> (num, title, rest)"""
    m = re.match(r'^(\d\d )?([^.]+\.)\s(.*)$', u)
    return (m.group(1) or '').strip(), m.group(2), m.group(3)


def links(s, pairs):
    s = t(s)
    for word, href in pairs:
        s = s.replace(word, f'<a class="tlink" href="{href}">{word}</a>', 1)
    return s


CSS = mic.CSS + r"""
/* lp-overlooked: persona theme (cool, structured) */
:root{--cool:#F6F6F4;--grey:#E7E8E8;--hair:rgba(126,153,182,.28);--on-navy-2:rgba(242,237,228,.78);--dove-l:#A9BED3}
body{background:var(--cool)}
.sec--cool{background:var(--cool)}.sec--grey{background:var(--grey)}
.gridded{position:relative}
.gridded>.wrap{position:relative}
.gridded>.wrap::before{content:"";position:absolute;top:-120px;bottom:-120px;left:40px;right:40px;pointer-events:none;z-index:0;
 background:repeating-linear-gradient(90deg,var(--gl) 0 1px,transparent 1px calc(100%/6));border-right:1px solid var(--gl)}
.gridded>.wrap>*{position:relative;z-index:1}
.sec--navy.gridded,.hero--ov.gridded,.closer--ov.gridded{--gl:rgba(169,190,211,.10)}
.hero--ov.gridded>.wrap::before{right:48%;border-right:0}
.sec--cool.gridded{--gl:rgba(126,153,182,.09)}
.fstep .fehlt,.tb .fehlt,.below .fehlt,.mnote .fehlt{display:inline;-webkit-box-decoration-break:clone;box-decoration-break:clone}
/* hero */
.hero--ov{background:var(--navy);color:var(--on-dark);height:auto;min-height:700px;max-height:none;padding:118px 0 64px;display:block;position:relative;overflow:hidden}
.hero--ov .hgrid{display:block;z-index:2}
.hero--ov .hero__txt{max-width:640px}
.hero--ov .hero__txt{padding-top:0;gap:16px}
.hero--ov h1{display:flex;flex-direction:column;gap:12px}
.hero--ov h1 .kicker{font:400 22px/1.3 var(--serif);letter-spacing:0;color:var(--dove-l)}
.hero--ov h1 .big{font-size:58px;line-height:1.07;color:#fff}
.hero--ov .sub{font:500 20px/1.45 var(--sans);font-style:normal;color:var(--on-dark)}
.hero--ov .body{font-size:18px;color:var(--on-navy-2);max-width:31em}
.hero--ov .proofline{color:var(--on-navy-2)}
.hero--ov .assure,.assure--dark{color:var(--on-navy-2)}.assure--dark svg,.hero--ov .assure svg{color:var(--sand)}
.hfig{position:absolute;top:0;right:0;bottom:0;width:47%;margin:0;z-index:1}
.hfig__img{position:absolute;inset:0;overflow:hidden}
.hfig__img img{width:100%;height:110%;margin-top:-3%;object-fit:cover;object-position:66% 40%;filter:saturate(.85) contrast(1.03)}
.hfig__img::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,var(--navy) 0%,rgba(43,60,82,0) 14%)}
/* proof strip */
.pstrip{background:var(--grey);padding:40px 0}
.pstrip__in{display:grid;grid-template-columns:auto 1.9fr .9fr;gap:32px;align-items:center}
.pstrip__face{width:96px;height:96px;border-radius:50%;overflow:hidden}
.pstrip__face img{width:100%;height:100%;object-fit:cover}
.nums{display:grid;grid-template-columns:.75fr .62fr .95fr 1.45fr}
.nums div{padding:4px 18px;border-left:1px solid var(--hair);display:flex;flex-direction:column;gap:4px}
.nums div:first-child{border-left:0;padding-left:0}
.nums b{font:400 25px/1.15 var(--serif);color:var(--navy);white-space:nowrap}
.nums span{font-size:16px;color:var(--muted);line-height:1.35}
.pstrip blockquote{margin:0;padding-left:24px;border-left:3px solid var(--dove);font:italic 400 20px/1.45 var(--serif)}
.pstrip blockquote small{display:block;margin-top:8px;font:500 16px/1.4 var(--sans);font-style:normal;color:var(--muted)}
/* answer */
.ansgrid{display:grid;grid-template-columns:.9fr 1.1fr;gap:64px;align-items:start}
.ansgrid h2{font-size:42px}
.ansgrid .ans{font:400 22px/1.55 var(--serif);color:var(--ink)}
.parts-h{margin-top:56px;font:600 14px/1.2 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--cta)}
.parts{display:grid;grid-template-columns:repeat(3,1fr);margin-top:18px;border-top:1px solid var(--hair)}
.parts div{padding:24px 28px 6px 0;display:flex;flex-direction:column;gap:8px}
.parts div+div{padding-left:28px;border-left:1px solid var(--hair)}
.parts i{font:400 36px/1 var(--serif);color:var(--dove);font-style:normal}
.parts h3{font-size:22px}.parts p{font-size:17px;color:var(--muted)}
.pull{margin-top:48px;display:grid;grid-template-columns:44px 1fr;gap:16px;align-items:start;background:#fff;border-radius:var(--r);padding:28px 32px}
.pull svg{width:30px;height:30px;color:var(--cta)}
.pull p{font:italic 400 21px/1.5 var(--serif)}
/* situations */
.scards{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:44px}
.scard{background:#fff;border-radius:var(--r);padding:28px 28px 30px;display:grid;grid-template-columns:58px 1fr;column-gap:16px;row-gap:12px;align-content:start}
.scard i{font:400 44px/1 var(--serif);color:var(--cta);font-style:normal;grid-row:1/3}
.scard h3{font-size:22px}.scard p{font-size:17px;color:var(--muted)}
.ssum{margin-top:36px;display:grid;grid-template-columns:1fr auto;gap:48px;align-items:end}
.ssum>div:first-child{display:flex;flex-direction:column;gap:8px}
.ssum .strong{font:600 19px/1.4 var(--sans)}
.ssum .cta-row{align-items:flex-end;margin-top:0}
.ssum p.aud{font-size:18px;color:var(--muted)}
/* method diagram */
#methode h2{font-size:42px;color:#fff}
.mgrid2{display:grid;grid-template-columns:390px 1fr;gap:56px;align-items:start}
.mgrid2 .diag{margin-top:0}
.mintro{color:var(--on-navy-2);font-size:19px;max-width:40em;margin-top:18px}
.diag{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:44px;margin-top:56px;position:relative}
.diag::before{display:none}
.dbox{position:relative;display:flex;flex-direction:column;gap:14px;margin:0}
.dbox__b{background:#34475F;border:1px solid rgba(169,190,211,.4);border-radius:18px;padding:26px 26px 24px;display:flex;flex-direction:column;gap:8px;min-height:158px}
.dbox__b i{font:400 34px/1 var(--serif);color:var(--sand);font-style:normal}
.dbox__b h3{color:#fff;font-size:22px;hyphens:manual}
.dbox__b p{color:var(--on-dark);font-size:17px}
.dbox figcaption{font:italic 400 17px/1.5 var(--serif);color:var(--on-navy-2);padding:0 6px}
.diag .dbox:not(:last-child)::after{content:"";position:absolute;right:-29px;top:56px;border:7px solid transparent;border-left:10px solid rgba(169,190,211,.75)}
.mnote{margin-top:36px;text-align:center}
/* intro column beside table */
.tgrid{display:grid;grid-template-columns:330px 1fr;gap:48px;align-items:start;margin-top:30px}
.tgrid .lead{font-size:18px}
.tgrid .tblw{margin-top:0}
.ctarow{display:flex;justify-content:space-between;align-items:center;gap:32px;margin-top:30px}
.ctarow .qline{margin-top:0}
/* tables */
.tblw{margin-top:40px;border-radius:var(--r);overflow:hidden;background:#fff;box-shadow:0 1px 0 var(--hair)}
table.tb{width:100%;border-collapse:collapse;font-size:17px}
.tb th,.tb td{text-align:left;vertical-align:top;padding:20px 24px;border-bottom:1px solid var(--hair)}
.tb tr:last-child td{border-bottom:0}
.tb thead th{font:600 16px/1.3 var(--sans);letter-spacing:.06em;color:var(--navy);background:#F0F2F4;border-bottom:1px solid rgba(126,153,182,.5)}
.tb tbody th{font:400 18px/1.35 var(--serif);color:var(--ink);width:19%}
.tb td{color:var(--muted)}
.tb--cmp td.hl,.tb--cmp th.hl{background:#EEF2F7;color:var(--ink)}
.tb--cmp thead th.hl{border-top:3px solid var(--cta);color:var(--cta)}
.tb--fmt td.hl,.tb--fmt th.hl{background:#E6ECF3;color:var(--ink)}
.tb--fmt thead th.hl{border-top:3px solid var(--cta);color:var(--cta)}
.tb--top .n{font:400 22px/1 var(--serif);color:var(--dove);width:56px}
.tb--top td.sitc{font:400 18px/1.4 var(--serif);color:var(--ink)}
.tag{display:inline-block;background:#E6ECF3;color:var(--cta);font:600 16px/1.35 var(--sans);padding:7px 12px;border-radius:10px;text-decoration:none}
.tag:hover{background:#D8E2EE}
.tb--top td:last-child{width:190px}
.tb--top td.sitc{width:28%}
.below{margin-top:26px;font-size:18px;color:var(--muted);max-width:52em}
.qline{margin-top:28px;padding-left:22px;border-left:3px solid var(--dove);max-width:46em}
.qline p{font-size:16px;color:var(--muted)}
.qline blockquote{margin:6px 0 0;font:italic 400 20px/1.5 var(--serif)}
.qline small{display:block;margin-top:8px;font-size:16px;color:var(--muted)}
/* first step */
.costline{margin-top:40px;font:400 22px/1.4 var(--serif)}
/* michael */
.mgrid{display:grid;grid-template-columns:.85fr 1.15fr;gap:64px;align-items:start}
.mgrid .portrait{height:680px}
.mgrid .portrait img{filter:saturate(.85)}
.ev{width:100%;border-collapse:collapse;margin-top:26px;font-size:17px}
.ev th,.ev td{text-align:left;padding:15px 0;border-bottom:1px solid var(--hair);vertical-align:top}
.ev thead th{font:600 14px/1.2 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--cta)}
.ev tbody th{font:400 18px/1.4 var(--serif);width:38%;padding-right:20px}
.ev td{color:var(--muted)}
/* voices */
.q2{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:44px}
.q2 .q blockquote{font-style:italic}
/* closing */
.closer--ov{background:var(--navy);padding:130px 0 120px}
.shot .proto{display:none}
.closer--ov::after{display:none}
.closer--ov .closer__in{max-width:none;display:grid;grid-template-columns:1.2fr .85fr 1.1fr;gap:48px;align-items:center}
.closer--ov .closer__in>div{display:flex;flex-direction:column;gap:18px}
.closer--ov h2{font-size:44px}
.closer--ov .cta-row{margin-top:0}
.closer--ov li svg{color:var(--sand)}
"""


def header():
    return f'''<header class="hdr"><div class="hdr__in">
 <a class="hdr__logo" href="{V2}index.html"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication, Startseite" width="1794" height="647"></a>
 <nav aria-label="Hauptnavigation"><a href="{V2}seminare.html">Seminare</a><a href="{V2}michael.html">Michael</a><a href="{V2}rhetorik.html">Was ist Rhetorik</a><a href="{V2}index.html#stimmen">Stimmen</a><a href="#faq">FAQ</a></nav>
 {btn('header')}
</div></header>'''


def s01():
    u = U['S01']
    kick, big = u[0].split(': ', 1)
    big = big.replace('Recht zu haben war', 'Recht zu haben<br>war')
    return f'''
<section class="hero hero--ov gridded" id="top">
 <div class="wrap hgrid">
  <div class="hero__txt">
   <h1 class="rv"><span class="kicker">{e(kick)}:</span><span class="big">{big}</span></h1>
   <p class="sub rv">{e(u[1])}</p>
   <p class="body rv">{e(u[2])}</p>
   <p class="proofline rv">{STARS} {e(u[3])}</p>
   <div class="cta-row rv">{btn('hero', 'btn btn--light cta--breathe')}{assure(u[5])}</div>
  </div>
 </div>
 <figure class="hfig"><div class="hfig__img"><img data-plx src="assets/{HERO_IMG}" alt="Michael Ehlers an einem Glastisch in einem Büro mit Glaswänden, kühles Tageslicht" width="1536" height="1024"></div></figure>
</section>'''


def s02():
    u = U['S02']
    nums = [('Seit 1990', 'Rhetoriktrainer'), ('8.000+', 'Teilnehmer'), ('Neun Bücher', 'als Autor oder Herausgeber'), ('Top 100', 'Trainer laut ERFOLG Magazin (Ausgabe 2017)')]
    for (a, b), src in zip(nums, u[:4]):
        assert src == f'{a} {b}', src
    n = ''.join(f'<div><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in nums)
    q, rest = u[4].split('“ ', 1)
    return f'''
<section class="pstrip" aria-label="Belege">
 <div class="wrap pstrip__in">
  <div class="pstrip__face rv"><img src="assets/michael-face.webp" alt="Michael Ehlers, Porträt" width="360" height="360"></div>
  <div class="nums rv">{n}</div>
  <blockquote class="rv">{e(q)}“<small>{t(rest)}</small></blockquote>
 </div>
</section>'''


def s03():
    u = U['S03']
    parts = ''
    for i, x in enumerate(u[3:6], 1):
        _, h, p = lead_bold(x)
        parts += f'<div class="rv"><i>0{i}</i><h3>{e(h)}</h3><p>{e(p)}</p></div>'
    return f'''
<section class="sec sec--cool gridded" id="gehoer-verschaffen">
 <div class="wrap">
  <div class="ansgrid"><h2 class="rv">{e(u[0])}</h2><p class="ans rv">{e(u[1])}</p></div>
  <p class="parts-h rv">{e(u[2])}</p>
  <div class="parts">{parts}</div>
  <div class="pull rv">{mic.ICON_MIC}<p>{e(u[6])}</p></div>
 </div>
</section>'''


def s04():
    u = U['S04']
    titles = ['Dein Argument stimmt. Entschieden wird anders.', 'Deine Idee kommt über einen anderen an.', 'Mehr Detail, weniger Aufmerksamkeit.']
    c = ''
    for x, title in zip(u[1:4], titles):
        n, rest = x[:2], x[3:]
        assert rest.startswith(title), rest
        c += f'<article class="scard rv"><i>{n}</i><h3>{e(title)}</h3><p>{e(rest[len(title):].strip())}</p></article>'
    return f'''
<section class="sec sec--grey" id="situationen">
 <div class="wrap">
  <h2 class="rv">{e(u[0])}</h2>
  <div class="scards">{c}</div>
  <div class="ssum"><div><p class="strong rv">{e(u[4])}</p><p class="aud rv">{e(u[5])}</p></div>
   <div class="cta-row rv">{btn('situationen')}{assure(u[7])}</div></div>
 </div>
</section>'''


def s05():
    u = U['S05']
    boxes = ''
    for x in u[2:5]:
        n, h, rest = lead_bold(x)
        line, q = rest.split(' Die Frage dahinter: ')
        boxes += f'<figure class="dbox rv"><div class="dbox__b"><i>{n}</i><h3>{e(h)}</h3><p>{e(line)}</p></div><figcaption>Die Frage dahinter: {e(q)}</figcaption></figure>'
    return f'''
<section class="sec sec--navy gridded" id="methode">
 <div class="wrap">
  <div class="mgrid2"><div><h2 class="rv">{e(u[0])}</h2>
  <p class="mintro rv">{e(u[1])}</p></div>
  <div class="diag">{boxes}</div></div>
  <p class="mnote rv">{t(u[5])}</p>
 </div>
</section>'''


def s06():
    u = U['S06']
    hd = row(u[2])
    body = ''.join(f'<tr><th scope="row">{e(r[0])}</th><td>{e(r[1])}</td><td class="hl">{e(r[2])}</td></tr>' for r in map(row, u[3:6]))
    intro, quote = u[7].split(' „', 1)
    qtxt, who = quote.split('“ ')
    return f'''
<section class="sec sec--cool" id="vergleich">
 <div class="wrap">
  <h2 class="rv">{e(u[0])}</h2>
  <div class="tgrid"><p class="lead rv">{e(u[1])}</p>
  <div class="tblw rv"><table class="tb tb--cmp"><thead><tr><td aria-hidden="true"></td><th scope="col">{e(hd[1])}</th><th scope="col" class="hl">{e(hd[2])}</th></tr></thead><tbody>{body}</tbody></table></div></div>
  <p class="below rv">{e(u[6])}</p>
  <div class="ctarow"><div class="qline rv"><p>{e(intro)}</p><blockquote>„{e(qtxt)}“</blockquote><small>{e(who)}</small></div>
  <div class="cta-row rv">{btn('vergleich')}</div></div>
 </div>
</section>'''


def s07():
    u = U['S07']
    hd = row(u[2])
    anchors = {'Ruhig bleiben, wenn es eng wird': 'ruhig-bleiben', 'Frei sprechen': 'frei-sprechen', 'Mit Sprache führen': 'mit-sprache-fuehren'}
    body = ''
    for i, r in enumerate(map(row, u[3:8]), 1):
        body += f'<tr><td class="n">0{i}</td><td class="sitc">{e(r[0])}</td><td>{e(r[1])}</td><td><a class="tag" href="{V2}seminare.html#{anchors[r[2]]}">{e(r[2])}</a></td></tr>'
    return f'''
<section class="sec sec--grey" id="training">
 <div class="wrap">
  <h2 class="rv">{e(u[0])}</h2>
  <div class="tgrid"><p class="lead rv">{e(u[1])}</p>
  <div class="tblw rv"><table class="tb tb--top"><thead><tr><td aria-hidden="true"></td><th scope="col">{e(hd[0])}</th><th scope="col">{e(hd[1])}</th><th scope="col">{e(hd[2])}</th></tr></thead><tbody>{body}</tbody></table></div></div>
  <p class="below rv">{links(u[8], [('Seminare.', V2 + 'seminare.html')]).replace('Seminare.</a>', 'Seminare</a>.')}</p>
 </div>
</section>'''


def s08():
    u = U['S08']
    hd = row(u[2])
    body = ''
    for r in map(row, u[3:8]):
        body += f'<tr><th scope="row">{e(r[0])}</th><td>{t(r[1])}</td><td>{e(r[2])}</td><td class="hl">{e(r[3])}</td></tr>'
    return f'''
<section class="sec sec--cool" id="formate">
 <div class="wrap">
  <h2 class="rv">{e(u[0])}</h2>
  <div class="tgrid"><p class="lead rv">{e(u[1])}</p>
  <div class="tblw rv"><table class="tb tb--fmt"><thead><tr><td aria-hidden="true"></td><th scope="col">{e(hd[1])}</th><th scope="col">{e(hd[2])}</th><th scope="col" class="hl">{e(hd[3])}</th></tr></thead><tbody>{body}</tbody></table></div></div>
  <div class="ctarow"><p class="below rv" style="margin-top:0">{t(u[8])}</p>
  <div class="cta-row rv" style="align-items:flex-end">{btn('formate')}{assure(u[10])}</div></div>
 </div>
</section>'''


def s09():
    u = U['S09']
    steps = ''
    for i, x in enumerate(u[1:4], 1):
        _, h, p = lead_bold(x)
        steps += f'<div class="fstep rv"><span class="n">{i}</span><div class="fstep__t"><h3>{e(h)}</h3><p>{t(p)}</p></div></div>'
    return f'''
<section class="sec sec--grey" id="ablauf">
 <div class="wrap">
  <h2 class="rv">{e(u[0])}</h2>
  <div class="flow" data-in><div class="flow__line"><i></i></div>{steps}</div>
  <p class="costline rv">{e(u[4])}</p>
  <div class="cta-row rv" style="margin-top:22px">{btn('ablauf')}</div>
 </div>
</section>'''


def s10():
    u = U['S10']
    hd = row(u[2])
    body = ''.join(f'<tr><th scope="row">{e(r[0])}</th><td>{e(r[1])}</td></tr>' for r in map(row, u[3:9]))
    last = u[9].replace('Mehr über Michael', f'<a class="tlink" href="{V2}michael.html">Mehr über Michael</a>')
    return f'''
<section class="sec sec--cool" id="michael">
 <div class="wrap mgrid">
  <div class="portrait rv"><img data-plx src="assets/michael-jacket.webp" alt="Michael Ehlers im braunen Sakko, sitzend in einem hellen Raum" width="1122" height="1600"></div>
  <div class="stack">
   <h2 class="rv">{e(u[0])}</h2>
   <p class="lead rv">{e(u[1])}</p>
   <table class="ev rv"><thead><tr><th scope="col">{e(hd[0])}</th><th scope="col">{e(hd[1])}</th></tr></thead><tbody>{body}</tbody></table>
   <p class="lead rv" style="margin-top:8px">{last}</p>
  </div>
 </div>
</section>'''


def s11():
    u = U['S11']
    cards = ''
    for i in range(2, 10, 2):
        q, who = u[i + 1].rsplit('“ ', 1)
        name, src = who.split(', ', 1)
        cards += f'<article class="q rv"><h3>{e(u[i])}</h3><blockquote>{e(q)}“</blockquote><div class="who"><span>{e(name)}</span><span class="src">{e(src)}</span></div></article>'
    v = ''.join(f'<div class="vid"><img src="assets/v-stimme-{i}.webp" alt="Teilnehmer-Video {i}" width="540" height="960"><b>{PLAY}</b><span>{d}</span></div>' for i, d in [(1, '1:00'), (2, '1:12'), (3, '1:23')])
    cap = u[10].replace('Stimmen.', f'<a class="tlink" href="{V2}index.html#stimmen">Stimmen</a>.')
    return f'''
<section class="sec sec--grey" id="stimmen">
 <div class="wrap">
  <div class="stack"><h2 class="rv">{e(u[0])}</h2><p class="lead rv">{e(u[1])}</p></div>
  <div class="q2">{cards}</div>
  <div class="vids rv">{v}</div>
  <p class="vcap center rv">{cap}</p>
  <div class="center" style="margin-top:36px"><div class="cta-row">{btn('stimmen')}</div></div>
 </div>
</section>'''


def s12():
    u = U['S12']
    items = ''
    for i in range(1, 19, 2):
        items += f'<details{" open" if i == 1 else ""}><summary>{e(u[i])}</summary><div class="a">{e(u[i + 1])}</div></details>'
    more = u[19].replace('häufigen Fragen.', f'<a class="tlink" href="{V2}faq.html">häufigen Fragen</a>.').replace('Was ist Rhetorik?', f'<a class="tlink" href="{V2}rhetorik.html">Was ist Rhetorik?</a>')
    return f'''
<section class="sec sec--cool" id="faq">
 <div class="wrap faqgrid">
  <div class="stack" style="position:sticky;top:120px"><h2 class="rv">{e(u[0])}</h2><p class="morelinks rv">{more}</p></div>
  <div class="acc rv">{items}</div>
 </div>
</section>'''


def s13():
    u = U['S13']
    li = ''.join(f'<li>{CHECK}<span>{e(x)}</span></li>' for x in u[2:5])
    foot = home.section_closer().split('<footer', 1)[1]
    foot = '<footer' + foot.replace(home.BOOK, BOOK).replace('href="#termine"', f'href="{V2}seminare.html#termine"')
    tel = u[7].replace('+49 15888367664', f'<a href="{TEL}">+49 15888367664</a>')
    return f'''
<section class="closer closer--ov gridded" id="abschluss">
 <div class="wrap"><div class="closer__in">
  <div><h2 class="rv">{e(u[0])}</h2>
  <p class="rv">{e(u[1])}</p></div>
  <div><ul class="rv">{li}</ul></div>
  <div><p class="proofline rv">{STARS} {e(u[5])}</p>
  <div class="cta-row rv">{btn('abschluss', 'btn btn--light cta--breathe')}<p class="tel">{tel}</p></div></div>
 </div></div>
</section>
{foot}'''


def schema():
    base = 'https://www.meandyou.de/lp-overlooked'
    ORG = 'https://www.meandyou.de/#organization'
    faq = [{"@type": "Question", "name": U['S12'][i], "acceptedAnswer": {"@type": "Answer", "text": U['S12'][i + 1]}} for i in range(1, 19, 2)]
    g = [{"@type": "WebPage", "@id": base + "#webpage", "url": base, "name": "Sich Gehör verschaffen: Rhetorik mit Michael Ehlers", "inLanguage": "de", "about": {"@id": "https://www.meandyou.de/michael#person"}},
         {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://www.meandyou.de/"}, {"@type": "ListItem", "position": 2, "name": "Sich Gehör verschaffen", "item": base}]},
         {"@type": "EducationalOrganization", "@id": ORG, "name": "Institut Michael Ehlers GmbH", "alternateName": "me&you Communication", "url": "https://www.meandyou.de/",
          "address": {"@type": "PostalAddress", "streetAddress": "Landsknechtstraße 50", "postalCode": "96103", "addressLocality": "Hallstadt", "addressCountry": "DE"}},
         {"@type": "Person", "@id": "https://www.meandyou.de/michael#person", "name": "Michael Ehlers", "jobTitle": "Rhetoriktrainer und Executive Coach", "worksFor": {"@id": ORG}, "url": "https://www.meandyou.de/michael", "sameAs": ["https://institut-ehlers.de/michael-ehlers"]},
         {"@type": "Service", "@id": base + "#service", "name": "Rhetoriktraining: sich Gehör verschaffen", "serviceType": "Rhetoriktraining", "provider": {"@id": ORG}, "url": base},
         {"@type": "FAQPage", "@id": base + "#faq", "mainEntity": faq}]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False)


def page():
    body = header() + '<main>' + s01() + s02() + s03() + s04() + s05() + s06() + s07() + s08() + s09() + s10() + s11() + s12() + '</main>' + s13() + '<div class="proto">Prototyp · nicht live · gelb = [FEHLT]</div>'
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Sich Gehör verschaffen: Rhetorik mit Michael Ehlers</title>
<meta name="description" content="Fachlich recht und trotzdem überhört? So verschaffst du dir Gehör: Rhetorikkurs mit Michael Ehlers, seit 1990. Seminar oder erst ein Gespräch.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">
<style>{CSS}
.sr{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}}</style>
<script type="application/ld+json">{schema()}</script>
</head><body>{body}<script>{home.JS}</script></body></html>'''


if __name__ == '__main__':
    out = page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out), 'hero:', HERO_IMG)
