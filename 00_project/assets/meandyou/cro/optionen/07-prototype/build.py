"""Build the me&you page "Optionen ansehen" (all ways to work with Michael), 2026-10-13.
Shell (head, header, footer, CSS) comes from the built Terminseite, so the design system stays the same.
Text = 04-copy/copy.md (passed the slop check 5/5). Run: python3 build.py"""
import os, re, shutil, html
HERE = os.path.dirname(os.path.abspath(__file__))
CRO = os.path.abspath(os.path.join(HERE, '..', '..'))
SHELL = open(os.path.join(CRO, 'termin', '07-prototype', 'index.html'), encoding='utf-8').read()
V2 = 'https://clients.741.studio/meandyou/v2/'
UTM = 'utm_source=optionen&utm_content='

# images reused from the approved pages
IMG = {'vsl-poster.webp': 'rhetorik', 'talk-to-me-cover.webp': 'lp-replayers/07-prototype/v2', 'michael-door.webp': 'termin',
       'city-mallorca.webp': 'seminare', 'closer-terrace.webp': 'seminare', 'einstieg-group.webp': 'seminare'}
os.makedirs(os.path.join(HERE, 'assets'), exist_ok=True)
for f in ('logo-dark.png', 'logo-light.png', 'logo-provenexpert.png'):
    shutil.copy(os.path.join(CRO, 'termin', '07-prototype', 'assets', f), os.path.join(HERE, 'assets', f))
for f, d in IMG.items():
    src = os.path.join(CRO, d, 'assets', f) if d.endswith('/v2') else os.path.join(CRO, d, '07-prototype', 'assets', f)
    shutil.copy(src, os.path.join(HERE, 'assets', f))

# parse copy.md
md = open(os.path.join(CRO, 'optionen', '04-copy', 'copy.md'), encoding='utf-8').read().strip().split('\n')
h1 = md[2].strip(); intro = md[4].strip()
blocks, cur = [], None
for line in md[5:]:
    line = line.strip()
    if line.startswith('## '):
        cur = {'title': line[3:], 'lines': []}; blocks.append(cur)
    elif line and cur is not None:
        cur['lines'].append(line)
opts, closing = blocks[:-1], blocks[-1]

LINKS = [('https://www.meandyou.de/sichtbarkeit-neu?' + UTM + 'video', 'vsl-poster.webp', 'Standbild aus dem Video-Training mit Michael Ehlers', 'Kostenlos'),
         ('https://www.skool.com/talk-to-me-9409/about?' + UTM + 'community', 'talk-to-me-cover.webp', 'Titelbild der Community Talk to ME', '44 US-Dollar im Monat'),
         ('https://www.meandyou.de/videokurs/start?' + UTM + 'kurs', 'michael-door.webp', 'Michael Ehlers', 'Online, in deinem Tempo'),
         (V2 + 'seminare.html', 'city-mallorca.webp', 'Seminarort Mallorca', 'Drei Tage plus Get Together'),
         (V2 + 'termin.html?' + UTM + 'gespraech', 'einstieg-group.webp', 'Gruppe im Seminar', '30 Minuten, kostenlos')]
ext = lambda u: '' if 'clients.741.studio' in u else ' target="_blank" rel="noopener"'
cards = []
for i, (b, (url, img, alt, tag)) in enumerate(zip(opts, LINKS)):
    who, body, btn = b['lines'][0], ' '.join(b['lines'][1:-1]), b['lines'][-1].replace('Button: ', '')
    primary = 'btn' if i == 4 else 'btn btn--ghost'
    cards.append(f'''<article class="opt rv"><div class="opt__img"><img src="assets/{img}" alt="{html.escape(alt)}" loading="lazy"></div>
<div class="opt__txt"><p class="opt__n">0{i+1} · {html.escape(tag)}</p><h2>{html.escape(b["title"])}</h2><p class="opt__who">{html.escape(who)}</p><p>{html.escape(body)}</p>
<a class="{primary}" href="{url}"{ext(url)} data-event="options_click" data-option="{i+1}">{html.escape(btn)}</a></div></article>''')

CSS = '''<style>
.opts-hero{padding:clamp(150px,20vh,200px) 0 clamp(40px,6vh,64px)}
.opts-hero h1{font:400 clamp(36px,4.2vw,58px)/1.12 "Libre Baskerville",Georgia,serif;margin:0 0 18px;max-width:16em}
.opts-hero p.lead{max-width:38em;font-size:clamp(17px,1.25vw,19px)}
.opts{display:grid;gap:clamp(18px,2.6vh,26px);padding-bottom:clamp(60px,9vh,110px)}
.opt{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);background:var(--cream,#F2EDE4);border-radius:22px;overflow:hidden;min-height:300px}
.opt:nth-child(even){grid-template-columns:minmax(0,7fr) minmax(0,5fr)}
.opt:nth-child(even) .opt__img{order:2}
.opt__img img{width:100%;height:100%;object-fit:cover;display:block}
.opt__txt{padding:clamp(26px,3.4vw,48px);display:flex;flex-direction:column;justify-content:center;gap:10px}
.opt__txt h2{font:400 clamp(26px,2.3vw,34px)/1.2 "Libre Baskerville",Georgia,serif;margin:0}
.opt__n{font:600 11.5px/1 Inter,sans-serif;letter-spacing:.18em;text-transform:uppercase;color:var(--dove,#64809E);margin:0}
.opt__who{font-style:italic;margin:0}
.opt__txt .btn{align-self:flex-start;margin-top:10px}
@media (max-width:820px){.opt,.opt:nth-child(even){grid-template-columns:minmax(0,1fr)}.opt:nth-child(even) .opt__img{order:0}.opt__img{aspect-ratio:16/9}}
</style>'''

main = f'''<main>
<section class="opts-hero" id="top"><div class="wrap"><p class="ov rv">Optionen ansehen</p><h1 class="rv">{html.escape(h1)}</h1><p class="lead rv">{html.escape(intro)}</p></div></section>
<section id="optionen"><div class="wrap opts">{"".join(cards)}</div></section>
</main>
<section class="closer closer--plain" id="abschluss">
 <div class="wrap"><div class="closer__in">
  <h2 class="rv">{html.escape(closing["lines"][0])}</h2>
  <p class="rv">{html.escape(closing["lines"][1])}</p>
  <div class="btns rv"><a class="btn" href="{V2}termin.html?{UTM}abschluss" data-event="options_click" data-option="5">Gespräch buchen</a></div>
 </div></div>
</section>'''

i = SHELL.find('<main'); j = SHELL.find('</main>')
k = SHELL.find('</section>', SHELL.find('id="abschluss"', j)) + len('</section>')
head = SHELL[:i]
head = re.sub(r'<title>.*?</title>', '<title>Optionen ansehen: Wege mit Michael Ehlers | me&amp;you</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Kostenloses Video, Community, Online-Kurs, Seminar oder Gespräch: alle Wege, mit Michael Ehlers an deiner Wirkung zu arbeiten.">', head)
head = head.replace('</head>', CSS + '</head>', 1)
# header button on this page points to the call, the page itself is the options overview
# full navigation header from the Michael page (the Terminseite has a minimal header)
MIC = open(os.path.join(CRO, 'michael', '07-prototype', 'index.html'), encoding='utf-8').read()
hdr = re.search(r'<header.*?</header>', MIC, re.S).group(0)
hdr = hdr.replace('<a href="#top" aria-current="page" style="color:var(--cta)">Michael</a>', f'<a href="{V2}michael.html">Michael</a>')
hdr = hdr.replace('<a href="#stimmen">Stimmen</a>', f'<a href="{V2}index.html#stimmen">Stimmen</a>').replace('<a href="#faq">FAQ</a>', f'<a href="{V2}faq.html">FAQ</a>')
hdr = re.sub(r'utm_source=michael', 'utm_source=optionen', hdr)
head = re.sub(r'<header.*?</header>', lambda m: hdr, head, flags=re.S)
out = head + main + SHELL[k:]
out = re.sub(r'utm_source=termin', 'utm_source=optionen', out)
open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
print('index.html', len(out), 'cards', len(cards))
