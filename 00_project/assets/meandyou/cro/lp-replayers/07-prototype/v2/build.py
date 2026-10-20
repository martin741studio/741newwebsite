"""Build the CRO prototype v2 of the me&you landing page "The Replayers" (desktop 1440 px), community version (Martin 2026-10-12: sell the 39 € community, no sales call). Text = 04-copy/approved-copy.md (parsed, never retyped).
Design system = homepage + seminar + Michael + rhetorik page (imported). Main CTA = Community beitreten (Skool Talk to ME, utm_source=lp-replayers),
no call button anywhere, the free video only as a quiet text link. Persona rule: only one button visible per screen (header button hides while a section button is in view).
Run: python3 build.py"""
import importlib.util, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


rh = load('rh_build', os.path.join(HERE, '..', '..', '..', 'rhetorik', '07-prototype', 'build.py'))
mic, sem, home = rh.mic, rh.sem, rh.home
V2 = sem.V2
SKOOL = 'https://www.skool.com/talk-to-me-9409/about?utm_source=lp-replayers&utm_content='
TRAIN = 'https://www.meandyou.de/sichtbarkeit-neu?utm_source=lp-replayers&utm_content='
PODCAST = 'https://podcasts.apple.com/de/podcast/un%C3%BCbersehbar-der-rhetorik-podcast-mit-michael-ehlers/id286899257'
TEL = sem.TEL
e, STARS, CHECK, PLAY, t = home.e, home.STARS, home.CHECK, home.PLAY, sem.t
LINKS = {'/seminare': V2 + 'seminare.html', '/seminare#frei-sprechen': V2 + 'seminare.html#frei-sprechen',
         '/seminare#ruhig-bleiben': V2 + 'seminare.html#ruhig-bleiben', '/michael': V2 + 'michael.html',
         '/stimmen': V2 + 'index.html#stimmen', '/rhetorik': V2 + 'rhetorik.html', '/faq': V2 + 'faq.html',
         }


def btn(utm, cls='btn'):
    return f'<a class="{cls}" href="{SKOOL}{utm}" data-event="community_click" data-section="{utm}">Community beitreten</a>'


# ---------- read the approved copy ----------
SRC = open(os.path.join(HERE, '..', '..', '04-copy', 'approved-copy.md'), encoding='utf-8').read()
FM = dict(re.findall(r'(?m)^(title|meta): (.+)$', SRC.split('---', 2)[1]))
BODY = SRC.split('---', 2)[2].split('<!-- TECH -->')[0]
SEC = {m.group(1): [l.strip() for l in re.sub(r'<!--.*?-->', '', m.group(2), flags=re.S).splitlines() if l.strip()]
       for m in re.finditer(r'<!-- (S\d\d) .*?-->(.*?)<!-- /\1 -->', BODY, re.S)}


def md(s):
    """Inline markdown to HTML: **bold**, links mapped to the v2 preview, placeholders yellow."""
    s = re.sub(r'^- ', '', s)
    out, pos = '', 0
    for m in re.finditer(r'\[([^\]]+)\]\(([^)\s]+)\)', s):
        out += t(s[pos:m.start()])
        label, url = m.group(1), m.group(2)
        href = url if url.startswith('http') or url.startswith('#') else LINKS[url]
        out += f'<a class="tlink" href="{e(href)}">{e(label)}</a>'
        pos = m.end()
    out += t(s[pos:])
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', out)


def h(line):
    return e(re.sub(r'^#+\s*', '', line))


def cta(sid, utm, cls='btn'):
    """Button + reassurance line taken from the approved copy (the line after **Gespräch buchen**)."""
    L = SEC[sid]
    i = [x.strip('*').startswith('Community beitreten') for x in L].index(True)
    return f'<div class="cta-row rv">{btn(utm, cls)}<p class="assure">{CHECK}{t(L[i + 1])}</p></div>'


CSS = rh.CSS + r"""
/* lp-replayers additions (persona: warm, patient, one idea per screen, no hard lines, one CTA visible) */
:root{--dove-soft:#DFE6EE}
.sec--dove{background:var(--dove-soft)}
.hdr .btn{transition:opacity .25s,transform .25s}
.hdr.cta-off .btn{opacity:0;transform:translateY(-6px);pointer-events:none}
.hero--rp{background:var(--dove-soft);min-height:0;height:auto;max-height:none;padding:118px 0 70px;display:block}
.hero--rp .hero__img{width:52%}
.hero--rp .hero__img img{height:112%;margin-top:-4%;object-position:50% 30%}
.hero--rp .hero__img::after{background:linear-gradient(90deg,var(--dove-soft) 0%,rgba(223,230,238,.75) 14%,rgba(223,230,238,0) 42%)}
.hero--rp .hero__in{position:relative;z-index:2}
.hero--rp .hero__txt{max-width:640px;padding-top:0;gap:14px}
.hero--rp h1{gap:8px}
.hero--rp h1 .kicker{font:400 30px/1.2 var(--serif);letter-spacing:0;color:var(--cta)}
.hero--rp h1 .big{font-size:58px;line-height:1.1}
.hero--rp .body{font-size:18px;line-height:1.6;color:var(--muted);max-width:33em}
.hero--rp .proofline{color:var(--muted);font-size:16px}
.rp-proof{padding:76px 0;background:var(--cream)}
.rp-proof__in{display:grid;grid-template-columns:1.4fr .6fr;gap:64px;align-items:center}
.rp-proof .rp-h2{font-size:34px;margin-bottom:18px}
.rp-proof blockquote{font-size:26px}
.rp-proof blockquote{margin:0;font:italic 400 30px/1.42 var(--serif);color:var(--ink)}
.rp-proof cite{display:block;margin-top:18px;font:500 16px/1.4 var(--sans);font-style:normal;color:var(--muted)}
.rp-who{display:flex;align-items:center;gap:18px}
.rp-who img{width:96px;height:96px;border-radius:50%;object-fit:cover;object-position:50% 22%;flex:none}
.rp-who p{font-size:16px;line-height:1.5;color:var(--muted)}
.rp-who b{display:block;color:var(--ink);font-size:17px}
.rp-answer{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center}
.rp-answer h2{font-size:46px}
.rp-answer .ans{font:400 21px/1.62 var(--sans);color:var(--ink);max-width:30em}
.rp-answer .ans2{font-size:19px;color:var(--muted);max-width:32em}
.rp-photo{border-radius:var(--r);overflow:hidden;aspect-ratio:4/3}
.rp-photo img{width:100%;height:100%;object-fit:cover}
.moments{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:46px}
.moment{background:#fff;border-radius:var(--r);padding:32px 30px;display:flex;flex-direction:column;gap:12px}
.moment h3{font-size:24px}
.moment p{font-size:17.5px;line-height:1.6;color:var(--muted)}
.moment .tlink{margin-top:auto;align-self:flex-start;font-size:16px}
.narrow{max-width:760px;margin:0 auto}
.narrow h2{font-size:44px}
.narrow p{font-size:19px;line-height:1.7}
.narrow .pod{display:grid;grid-template-columns:44px 1fr;gap:16px;align-items:start;background:var(--cream);border-radius:var(--r);padding:26px 28px}
.narrow .pod svg{width:28px;height:28px;color:var(--cta);margin-top:4px}
.narrow .rpq{font:italic 400 24px/1.5 var(--serif);color:var(--ink)}
.cols01 div{border-top:0;padding-top:0}
.rp-meth{display:grid;grid-template-columns:1.05fr .95fr;gap:72px;align-items:start}
.rp-meth .cols01{grid-template-columns:1fr;gap:26px;margin-top:6px}
.rp-meth .cols01 div{display:grid;grid-template-columns:64px 1fr;column-gap:16px}
.rp-meth .cols01 i{grid-row:span 2}
.rp-meth .cols01 h3{margin:2px 0 4px;font-size:22px}
.rp-learn .ex3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.rp-learn .ex3 .exc{grid-template-columns:1fr;gap:8px;padding:22px 20px;align-content:start}
.rp-learn .learn{grid-template-columns:.8fr 1.2fr}
.rp-steps{display:grid;grid-template-columns:1.1fr .9fr;gap:64px;align-items:start}
.rp-steps .soft3{margin-top:30px}
.rp-steps .side{background:rgba(255,255,255,.55);border-radius:var(--r);padding:30px 32px;margin-top:30px}
.rp-steps .semline{margin-top:0}
.acc2c{display:grid;grid-template-columns:1fr 1fr;column-gap:36px;align-items:start;margin-top:36px}
.acc2c .acc{margin-top:0}
.closer--plain .closer__in{max-width:none;display:grid;grid-template-columns:1.1fr .9fr;gap:20px 64px;align-items:start}
.closer--plain{padding:120px 0 110px}
.rp-learn .exc{background:#fff}
.rp-learn h3.exh{font:600 20px/1.3 var(--sans);color:var(--ink)}
.rp-video{background:var(--dove-soft);border-radius:28px;padding:44px}
.rp-video .vsl{gap:52px}
.rl{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:44px}
.rlc{background:var(--cream);border-radius:var(--r);padding:30px;display:grid;grid-template-columns:140px 1fr;gap:26px;align-items:start}
.rlc .cov{width:140px;height:190px;border-radius:10px;background:linear-gradient(160deg,#F7F2E8,#E9DFCC);display:flex;align-items:flex-end;padding:14px;font:400 16px/1.25 var(--serif);color:var(--ink);box-shadow:0 10px 24px rgba(42,38,34,.12)}
.rlc .cov.sq{height:140px;width:140px;font-size:16px;background:linear-gradient(160deg,#2B3C52,#4F6D90);color:#fff}
.rlc h3{font-size:23px;margin-bottom:10px}
.rlc p{font-size:17px;line-height:1.6;color:var(--muted)}
.rlc .tlink{display:inline-block;margin-top:12px}
.rp-mic{display:grid;grid-template-columns:.85fr 1.15fr;gap:72px;align-items:center}
.rp-mic .pic{border-radius:var(--r);overflow:hidden;height:600px}
.rp-mic .pic img{width:100%;height:100%;object-fit:cover;object-position:50% 25%}
.facts4{display:grid;grid-template-columns:1fr 1fr;gap:18px 28px;margin:6px 0 4px}
.facts4 p{font-size:17px;color:var(--muted)}.facts4 b{display:block;font:400 26px/1.2 var(--serif);color:var(--cta)}
.quotes4{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:44px}
.qc{background:#fff;border-radius:var(--r);padding:32px 32px 28px;box-shadow:0 1px 0 var(--line)}
.qc blockquote{margin:0;font:italic 400 20px/1.55 var(--serif);color:var(--ink)}
.qc cite{display:block;margin-top:14px;font:500 16px/1.4 var(--sans);font-style:normal;color:var(--muted)}
.qfoot{margin-top:28px;font-size:17px;color:var(--muted)}
.soft3{display:flex;flex-direction:column;gap:26px;margin-top:40px;max-width:760px}
.soft3 li{list-style:none;display:grid;grid-template-columns:64px 1fr;gap:18px;align-items:start}
.soft3 i{font:400 44px/1 var(--serif);font-style:normal;color:var(--cta)}
.soft3 p{font-size:18.5px;line-height:1.6;color:var(--muted)}.soft3 b{display:block;color:var(--ink);font-size:20px;margin-bottom:2px}
.soft3{padding:0;margin-left:0}
.semline{margin-top:34px;max-width:52em;font-size:18px;line-height:1.7}
.rp-faq{max-width:900px}
.rp-faq .acc{margin-top:36px}
.closer--plain{background:var(--navy)}
.rp-comm{display:grid;grid-template-columns:1fr 1fr;gap:52px;align-items:start}
.comm-l{display:flex;flex-direction:column;gap:22px}
.comm-cover{display:block;border-radius:var(--r);overflow:hidden;box-shadow:0 14px 34px rgba(43,60,82,.14)}
.comm-cover img{width:100%;height:auto;display:block}
.comm-q{margin:0;background:rgba(255,255,255,.6);border-radius:18px;padding:22px 24px}
.comm-q blockquote{margin:0;font:italic 400 18px/1.55 var(--serif);color:var(--ink)}
.comm-q figcaption{margin-top:10px;font:500 16px/1.4 var(--sans);color:var(--muted)}
.comm-list{list-style:none;margin:4px 0 0;padding:0;display:flex;flex-direction:column;gap:12px}
.comm-list li{display:grid;grid-template-columns:22px 1fr;gap:10px;font-size:17.5px;line-height:1.55;color:var(--muted)}
.comm-list li svg{width:20px;height:20px;color:var(--cta);margin-top:3px}
.comm-list b{color:var(--ink)}
.rp-steps .side .semline+.semline{margin-top:14px}
.closer--plain::after{background:radial-gradient(120% 140% at 85% 0%,rgba(79,109,144,.35) 0%,rgba(43,60,82,0) 60%)}
"""


def header():
    return f'''<header class="hdr"><div class="hdr__in">
 <a class="hdr__logo" href="{V2}index.html"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication, Startseite" width="1794" height="647"></a>
 <nav aria-label="Hauptnavigation"><a href="{V2}seminare.html">Seminare</a><a href="{V2}michael.html">Michael</a><a href="{V2}rhetorik.html">Was ist Rhetorik</a><a href="{V2}index.html#stimmen">Stimmen</a><a href="{V2}faq.html">FAQ</a></nav>
 {btn('header')}
</div></header>'''


def s01():
    L = SEC['S01']
    h1 = L[1][2:]
    kick, big = h1.split('. ', 1)
    return f'''
<section class="hero hero--rp" id="top">
 <div class="hero__img"><img data-plx src="assets/hero-heimweg.webp" alt="Eine Frau sitzt abends am Fenster einer Bahn, ein Notizbuch auf dem Schoß, und schaut nachdenklich hinaus" width="1024" height="1536"></div>
 <div class="wrap hero__in"><div class="hero__txt">
  <p class="ov rv">{e(L[0])}</p>
  <h1 class="rv"><span class="kicker">{e(kick)}.</span><span class="big">{e(big)}</span></h1>
  <p class="body rv">{e(L[2])}</p>
  <p class="proofline rv">{STARS} {e(L[3])}</p>
  <div class="cta-row rv">{btn('hero', 'btn cta--breathe')}<p class="assure">{CHECK}{t(L[5])}</p></div>
 </div></div>
</section>'''


def s02():
    L = SEC['S02']
    q = L[1]
    who = L[3].split(' · ')
    return f'''
<section class="rp-proof" id="stimme">
 <div class="wrap rp-proof__in">
  <div class="rv"><h2 class="rp-h2">{h(L[0])}</h2><blockquote>{e(q)}</blockquote><cite>{e(L[2])}</cite></div>
  <div class="rp-who rv"><img src="assets/michael-cafe.webp" alt="Michael Ehlers" width="1130" height="1600"><p><b>{e(who[0])}</b>{e(who[1])}<br>{e(who[2])}</p></div>
 </div>
</section>'''


def s03():
    L = SEC['S03']
    return f'''
<section class="sec" id="treppenwitz">
 <div class="wrap rp-answer">
  <div class="stack"><h2 class="rv">{h(L[0])}</h2><p class="ans rv">{e(L[1])}</p><p class="ans2 rv">{e(L[2])}</p></div>
  <div class="rp-photo rv"><img src="assets/sit-replayers.webp" alt="Eine Frau schreibt abends am Schreibtisch in ein Notizbuch" width="1536" height="1024"></div>
 </div>
</section>'''


def s04():
    L = SEC['S04']
    cards, i = [], 1
    while L[i].startswith('### '):
        cards.append(f'<div class="moment rv"><h3>{h(L[i])}</h3><p>{md(L[i + 1])}</p></div>'); i += 2
    # the link sits at the end of the third paragraph: move it to the card foot
    html = ''.join(cards).replace(' <a class="tlink"', '</p><a class="tlink"').replace('</a></p></div>', '</a></div>')
    return f'''
<section class="sec sec--dove" id="momente">
 <div class="wrap">
  <h2 class="rv">{h(L[0])}</h2>
  <div class="moments">{html}</div>
  <div class="center" style="margin-top:40px"><p class="lead rv" style="margin:0 auto 22px">{e(L[i])}</p>{cta('S04', 'momente')}</div>
 </div>
</section>'''


def s05():
    L = SEC['S05']
    q = re.match(r'(„.+?“)(.*)', L[3])
    return f'''
<section class="sec" id="warum">
 <div class="wrap narrow stack">
  <h2 class="rv">{h(L[0])}</h2>
  <p class="rv">{e(L[1])}</p>
  <div class="pod rv">{mic.ICON_MIC}<p>{t(L[2])}</p></div>
  <p class="rv"><span class="rpq">{e(q.group(1))}</span>{e(q.group(2))}</p>
 </div>
</section>'''


def s06():
    L = SEC['S06']
    c = ''.join(f'<div class="rv"><i>{n:02d}</i>{md(x).replace("<b>", "<h3>", 1).replace("</b>", "</h3><p>", 1)}</p></div>' for n, x in enumerate(L[2:5], 1))
    return f'''
<section class="sec sec--navy" id="methode">
 <div class="wrap">
  <div class="rp-meth">
   <div><h2 class="rv" style="color:#fff">{h(L[0])}</h2>
    <p class="lead rv" style="color:rgba(242,237,228,.85);margin-top:22px">{e(L[1])}</p></div>
   <div class="cols01">{c}</div>
  </div>
  <div class="center" style="margin-top:44px"><p class="lead rv" style="color:rgba(242,237,228,.85);margin:0 auto 22px">{e(L[5])}</p>
   {cta('S06', 'methode', 'btn btn--light').replace('class="assure"', 'class="assure" style="color:rgba(242,237,228,.8)"')}</div>
 </div>
</section>'''


def s07():
    L = SEC['S07']
    ex = [x for x in L if re.match(r'^\d\. ', x)]
    c = ''.join(f'<div class="exc rv"><i>{x[0]}</i><p>{md(x[3:])}</p></div>' for x in ex)
    ph = [x for x in L if x.startswith('[von Kunde')][0]
    return f'''
<section class="sec sec--cream rp-learn" id="uebungen">
 <div class="wrap learn">
  <div class="stack"><h2 class="rv">{h(L[0])}</h2><p class="lead rv">{e(L[1])}</p></div>
  <div class="ex"><h3 class="exh rv">{h(L[2])}</h3><p class="lead rv" style="margin:0">{e(L[3])}</p><div class="ex3">{c}</div><p class="rv">{t(ph)}</p><p class="lead rv" style="margin:0">{e(L[-1])}</p></div>
 </div>
</section>'''


def s08():
    L = SEC['S08']
    items = [x for x in L if x.startswith('- ')]
    li = ''.join(f'<li>{CHECK}<span>{md(x)}</span></li>' for x in items)
    qi = [i for i, x in enumerate(L) if x.startswith('„')][0]
    return f'''
<section class="sec" id="community">
 <div class="wrap"><div class="rp-video rp-comm">
  <div class="comm-l">
   <a class="comm-cover rv" href="{SKOOL}community-bild" data-event="community_click" data-section="community-bild"><img src="assets/talk-to-me-cover.webp" alt="Titelbild der Community Talk to ME: Die Rhetorik-Community, mit Michael Ehlers" width="1084" height="576"></a>
   <figure class="comm-q rv"><blockquote>{e(L[qi])}</blockquote><figcaption>{e(L[qi + 1])}</figcaption></figure>
  </div>
  <div class="stack"><h2 class="rv">{h(L[0])}</h2><p class="lead rv">{e(L[1])}</p>
   <ul class="comm-list rv">{li}</ul>
   {cta('S08', 'community')}</div>
 </div></div>
</section>'''


def s09():
    L = SEC['S09']
    book_t, book_p, pod_t, pod_p, more = L[1], L[2], L[3], L[4], L[5]
    return f'''
<section class="sec sec--cream" id="lesen-hoeren">
 <div class="wrap">
  <h2 class="rv">{h(L[0])}</h2>
  <div class="rl">
   <div class="rlc rv"><div class="cov" aria-hidden="true">Nie wieder sprachlos!</div><div><h3>{h(book_t)}</h3><p>{md(book_p)}</p></div></div>
   <div class="rlc rv"><div class="cov sq" aria-hidden="true">Unübersehbar</div><div><h3>{h(pod_t)}</h3><p>{md(pod_p).replace(' <a class="tlink"', '</p><a class="tlink"')}</div></div>
  </div>
  <p class="lead rv" style="margin-top:30px">{md(more)}</p>
 </div>
</section>'''.replace('</a></div></div>', '</a></div></div>')


def s10():
    L = SEC['S10']
    facts = ''.join(f'<p>{md(x).replace("<b>", "<b>", 1)}</p>' for x in L[2:6])
    return f'''
<section class="sec" id="michael">
 <div class="wrap rp-mic">
  <div class="pic rv"><img src="assets/michael-door.webp" alt="Michael Ehlers, Rhetoriktrainer, lächelnd im weißen Hemd an einem Türrahmen" width="1200" height="1800"></div>
  <div class="stack"><h2 class="rv">{h(L[0])}</h2><p class="lead rv">{e(L[1])}</p>
   <div class="facts4 rv">{facts}</div>
   <p class="rv">{md(L[6])}</p>
   {cta('S10', 'michael')}</div>
 </div>
</section>'''


def s11():
    L = SEC['S11']
    qs = ''.join(f'<div class="qc rv"><blockquote>{e(L[i])}</blockquote><cite>{e(L[i + 1])}</cite></div>' for i in range(1, 9, 2))
    return f'''
<section class="sec sec--cream" id="stimmen">
 <div class="wrap">
  <h2 class="rv">{h(L[0])}</h2>
  <div class="quotes4">{qs}</div>
  <p class="qfoot rv">{STARS} {md(L[9])}</p>
 </div>
</section>'''


def s12():
    L = SEC['S12']
    steps = [x for x in L if re.match(r'^\d\. ', x)]
    li = ''.join(f'<li class="rv"><i>{x[0]}</i><p>{md(x[3:])}</p></li>' for x in steps)
    paras = [x for x in L[1:] if not re.match(r'^\d\. ', x) and not x.startswith('**') and not L.index(x) > [i for i, y in enumerate(L) if y.startswith('**Community')][0]]
    side = ''.join(f'<p class="semline">{md(x)}</p>' for x in paras)
    return f'''
<section class="sec sec--dove" id="start">
 <div class="wrap">
  <h2 class="rv">{h(L[0])}</h2>
  <div class="rp-steps">
   <ol class="soft3">{li}</ol>
   <div class="side rv">{side}<div style="margin-top:26px">{cta('S12', 'start')}</div></div>
  </div>
 </div>
</section>'''


def s13():
    L = SEC['S13']
    qa, i = [], 1
    while i < len(L) and L[i].startswith('### '):
        qa.append((h(L[i]), L[i + 1])); i += 2
    det = lambda n, q, a: f'<details{" open" if n == 0 else ""}><summary>{q}</summary><div class="a">{md(a)}</div></details>'
    half = (len(qa) + 1) // 2
    items = '<div class="acc">' + ''.join(det(n, q, a) for n, (q, a) in enumerate(qa)) + '</div>'
    return f'''
<section class="sec" id="faq">
 <div class="wrap">
  <h2 class="rv">{h(L[0])}</h2>
  <div class="rv" style="margin-top:36px">{items}</div>
  <p class="morelinks rv" style="margin-top:26px">{md(L[i])}</p>
 </div>
</section>'''


def s14():
    L = SEC['S14']
    li = ''.join(f'<li>{CHECK}<span>{t(x[2:])}</span></li>' for x in L[2:5])
    foot = home.section_closer().split('<footer', 1)[1]
    foot = '<footer' + foot.replace('href="#termine"', f'href="{V2}seminare.html#termine"')
    foot = re.sub(r'<a href="[^"]*">Gespräch buchen</a>', f'<a href="{SKOOL}footer" data-event="community_click" data-section="footer">Community Talk to ME</a>', foot)
    assert 'Gespräch buchen' not in foot
    mail = L[-1].split(': ', 1)
    return f'''
<section class="closer closer--plain" id="abschluss">
 <div class="wrap"><div class="closer__in">
  <div class="stack"><h2 class="rv">{h(L[0])}</h2>
  <p class="rv">{e(L[1])}</p></div>
  <div class="stack"><ul class="rv">{li}</ul>
  <p class="proofline rv">{e(L[5])}</p>
  <div class="cta-row rv">{btn('abschluss', 'btn btn--light cta--breathe')}<p class="tel">{e(mail[0])}: <a href="mailto:{e(mail[1])}">{e(mail[1])}</a></p></div></div>
 </div></div>
</section>
{foot}'''


JS = home.JS + r"""
;(function(){
 if(/shot=1/.test(location.search)){ var pr = document.querySelector('.proto'); if(pr) pr.style.display = 'none'; }
 // persona rule: one button visible at a time. The header button hides while any section button is on screen.
 var hdr = document.querySelector('.hdr'), btns = [].slice.call(document.querySelectorAll('main .btn, .closer .btn'));
 function chk(){ var vh = innerHeight, on = btns.some(function(b){ var r = b.getBoundingClientRect(); return r.bottom > 80 && r.top < vh; });
  hdr.classList.toggle('cta-off', on); }
 addEventListener('scroll', chk, {passive:true}); addEventListener('resize', chk); chk();
})();
"""


def schema():
    ORG = 'https://www.meandyou.de/#organization'
    URL = 'https://www.meandyou.de/schlagfertigkeit-lernen'
    person = {"@type": "Person", "@id": "https://www.meandyou.de/michael#person", "name": "Michael Ehlers", "url": "https://www.meandyou.de/michael",
              "jobTitle": "Rhetoriktrainer und Executive Coach", "knowsAbout": ["Rhetorik", "Schlagfertigkeit"],
              "sameAs": ["https://institut-ehlers.de/michael-ehlers", "https://de.linkedin.com/in/rhetoriktrainer", PODCAST]}
    g = [{"@type": "WebPage", "@id": URL + "#webpage", "url": URL, "name": FM['title'], "description": FM['meta'], "inLanguage": "de",
          "about": {"@type": "Thing", "name": "Schlagfertigkeit"},
          "mentions": [{"@type": "DefinedTerm", "name": "Treppenwitz", "sameAs": "https://de.wikipedia.org/wiki/Treppenwitz"}, {"@id": person["@id"]}],
          "publisher": {"@id": ORG}},
         person,
         {"@type": "PodcastSeries", "name": "Unübersehbar – Der Rhetorik Podcast mit Michael Ehlers", "url": PODCAST, "startDate": "2008", "author": {"@id": person["@id"]}},
         {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Startseite", "item": "https://www.meandyou.de/"}, {"@type": "ListItem", "position": 2, "name": "Schlagfertigkeit lernen", "item": URL}]},
         {"@type": "EducationalOrganization", "@id": ORG, "name": "Institut Michael Ehlers GmbH", "alternateName": "me&you Communication", "url": "https://www.meandyou.de/", "email": "management@meandyou.de"}]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False)


def page():
    body = header() + '<main>' + s01() + s02() + s03() + s04() + s05() + s06() + s07() + s08() + s09() + s10() + s11() + s12() + s13() + '</main>' + s14() + '<div class="proto">Prototyp · nicht live · gelb = [FEHLT]</div>'
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
