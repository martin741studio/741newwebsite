"""Build 07-prototype/index.html from the approved copy (content-writing page.md). Text is never typed here."""
import re, html, pathlib

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
PAGE = (RUN / '../../content-writing/ki-website/05-final/page.md').resolve().read_text(encoding='utf8')
FM = dict(re.findall(r'^(title|meta): (.*)$', PAGE.split('---', 2)[1], re.M))
SEC = {m.group(1): re.sub(r'<!--.*?-->\n?', '', m.group(2)).strip()
       for m in re.finditer(r'<!-- (S\d\d) [^>]*-->\n(.*?)<!-- /\1 -->', PAGE, re.S)}
BOOK = 'https://cal.com/741-studio-simjzw/30min'
PH = re.compile(r'\[von Kunde bestätigen: ([^\]]+)\]')


def inl(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'(\d) €', '\\1&nbsp;€', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = PH.sub(lambda m: f'<span class="fehlt">[FEHLT: {m.group(1)}]</span>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{m.group(2)}"' + (' target="_blank" rel="noopener"' if m.group(2).startswith('http') else '') + f'>{m.group(1)}</a>', t)
    return t


def L(sid):
    return [l for l in SEC[sid].split('\n') if l.strip()]


def h(sid, lvl=2):
    return next(l for l in L(sid) if l.startswith('#' * lvl + ' '))[lvl + 1:]


def bullets(sid):
    return [l[2:] for l in L(sid) if l.startswith('- ')]


def paras(sid):
    return [l for l in L(sid) if not re.match(r'(#|- |\d+\. |\||\*\*Kostenloses)', l) and not l.startswith('Dauer 30') and not l.startswith('Live') and not l.startswith('Martin Drendel,') and not l.startswith('Vorher (') and not l.startswith('Heute (') and not l.startswith('Beispiel: ') and not l.startswith('Bitte auf der Startseite') and not l.startswith('Erledigt in einer Kopie') and not l.startswith('Prüfung bestanden') and not l.startswith('741 gibt frei') and not l.startswith('Live in ein bis zwei') and not l.startswith('„Hey,') and not l.startswith('Martin Hüwel, Heilpraktiker') and not l.startswith('So fühlt sich')]


REASSURE = 'Dauer 30 Minuten. Kostenlos und unverbindlich.'
ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<span class="ck" aria-hidden="true"><svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="#1c1c1a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>'


def cta(cls='', breathing=False, section=''):
    return f'<a class="btn {cls}{" breathe" if breathing else ""}" href="{BOOK}" target="_blank" rel="noopener" data-section="{section}">Kostenloses Gespräch buchen {ARROW}</a>'


ICON = {
    'cal': '<path d="M4 6h16v14H4zM4 10h16M8 3v4M16 3v4"/>',
    'coins': '<ellipse cx="9" cy="7" rx="5" ry="2.5"/><path d="M4 7v4c0 1.4 2.2 2.5 5 2.5s5-1.1 5-2.5V7M4 11v4c0 1.4 2.2 2.5 5 2.5"/><ellipse cx="15" cy="15" rx="5" ry="2.5"/><path d="M10 15v3c0 1.4 2.2 2.5 5 2.5s5-1.1 5-2.5v-3"/>',
    'warn': '<path d="M12 3l9.5 17h-19z"/><path d="M12 10v4M12 17.5v.5"/>',
    'gauge': '<path d="M4 17a8 8 0 1 1 16 0"/><path d="M12 17l4-5"/>',
    'tool': '<path d="M14.5 6.5a4 4 0 0 0-5 5L4 17l3 3 5.5-5.5a4 4 0 0 0 5-5l-2.5 2.5-2.5-.5-.5-2.5z"/>',
    'chat': '<path d="M4 5h11v8H8l-4 3z"/><path d="M15 9h5v8l-3-2.5h-6V13"/>',
    'shield': '<path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    'bars': '<path d="M5 20v-5M10 20V9M15 20v-8M20 20V4"/>',
    'mail': '<path d="M3 6h18v12H3z"/><path d="M3 7l9 7 9-7"/>',
}


def icon(k):
    return f'<svg class="ic" viewBox="0 0 24 24" width="34" height="34" fill="none" stroke="#e0ac0a" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[k]}</svg>'


# ---------- sections ----------
def s01():
    l = L('S01')
    badge, h1 = l[0], l[1][2:]
    head, tail = h1.split(': ', 1)
    ans = paras('S01')[1]
    live = next(x for x in l if x.startswith('Live-Beispiel'))
    fline = next(x for x in l if x.startswith('Martin Drendel,'))
    k0 = next(n for n,x in enumerate(l) if x.startswith('Beispiel: '))
    ex = [x for x in l[k0:k0+6]]
    stat = bullets('S02')[0]
    num, rest = re.match(r'\*\*(.+?)\*\*,? ?(.*)', stat).groups()
    return f'''
<section class="hero" id="s01">
 <div class="wrap hero-grid">
  <div class="hero-txt">
   <span class="pill rv">{inl(badge)}</span>
   <h1 class="rv"><span class="h1a">{inl(head)}:</span> <em>{inl(tail)}</em></h1>
   <p class="lead rv">{inl(ans)}</p>
   <div class="cta-row rv">{cta(breathing=True, section='hero')}</div>
   <p class="reassure rv">{REASSURE}</p>
   <ul class="checks rv">{''.join(f'<li>{CHECK}{inl(b)}</li>' for b in bullets('S01'))}</ul>
   <div class="founder rv"><img src="assets/martin-avatar.jpg" alt="Martin Drendel" width="112" height="112"><div class="fl"><span>{inl(fline)}</span><p class="live">{inl(live)}</p></div></div>
  </div>
  <div class="hero-vis rv">
   <div class="app">
    <div class="app-bar"><i></i><i></i><i></i><span class="app-t">{inl(ex[0])}</span></div>
    <div class="chat">
     <div class="msg me">{inl(ex[1])}</div>
     <div class="msg ai"><span class="ai-dot2"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#1c1c1a" stroke-width="1.7"><circle cx="12" cy="12" r="8"/><path d="M8 12h8M12 8v8"/></svg></span>{inl(ex[2])}</div>
    </div>
    <ul class="steps-ui">
     <li><span class="dot ok"></span>{inl(ex[3])}</li>
     <li><span class="dot wait"></span>{inl(ex[4])}</li>
     <li><span class="dot live"></span>{inl(ex[5])}</li>
    </ul>
   </div>
   <div class="float stat"><svg viewBox="0 0 24 24" width="34" height="34" fill="#16a34a" aria-hidden="true"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg><div><b>{inl(num)}</b><span>{inl(rest)}</span></div></div>
  </div>
 </div>
</section>'''


def s02():
    l = L('S02')
    items = ''
    for b in bullets('S02'):
        num, rest = re.match(r'\*\*(.+?)\*\*,? ?(.*)', b).groups()
        items += f'<div class="stat-i rv"><i class="bar"></i><b>{inl(num)}</b><span>{inl(rest)}</span></div>'
    return f'''
<section class="proof" id="s02"><div class="wrap">
 <h2 class="h-sm rv">{inl(h("S02"))}</h2><p class="sub rv">{inl(paras("S02")[0])}</p>
 <div class="stats">{items}</div>
</div></section>'''


def s03():
    ic = ['cal', 'coins', 'warn', 'gauge']
    cards = ''.join(f'<div class="sit rv">{icon(ic[i])}<p>{inl(b)}</p></div>' for i, b in enumerate(bullets('S03')))
    return f'''
<section class="cream" id="s03"><div class="wrap two">
 <div><h2 class="rv">{inl(h("S03"))}</h2><p class="rv">{inl(paras("S03")[0])}</p><div class="cta-row rv">{cta(section='situationen')}</div><p class="reassure rv">{REASSURE}</p></div>
 <div class="sit-grid">{cards}</div>
</div></section>'''


def s04():
    l = L('S04')
    ic = ['tool', 'chat', 'shield', 'bars', 'mail']
    cards, i = [], 0
    for j, x in enumerate(l):
        if x.startswith('### '):
            cards.append(f'<div class="card rv">{icon(ic[i])}<h3>{inl(x[4:])}</h3><p>{inl(l[j + 1])}</p></div>')
            i += 1
    return f'''
<section class="white" id="s04"><div class="wrap">
 <h2 class="center rv">{inl(h("S04"))}</h2>
 <div class="cards3">{"".join(cards[:3])}</div><div class="cards2">{"".join(cards[3:])}</div>
</div></section>'''


def s05():
    steps = [x for x in L('S05') if re.match(r'\d+\. ', x)]
    out = ''
    for n, s in enumerate(steps, 1):
        t, body = re.match(r'\d+\. \*\*(.+?)\*\* ?(.*)', s).groups()
        out += f'<div class="step rv"><span class="num">{n}</span><h3>{inl(t)}</h3><p>{inl(body)}</p></div>'
    return f'''
<section class="cream" id="s05"><div class="wrap">
 <h2 class="center rv">{inl(h("S05"))}</h2>
 <div class="steps"><i class="track"><i class="fill"></i></i>{out}</div>
 <div class="center cta-row rv">{cta(section='start')}</div><p class="reassure center rv">{REASSURE}</p>
</div></section>'''


def s06():
    return f'''
<section class="dark" id="s06"><div class="wrap person">
 <div class="ph rv-l"><img src="assets/martin-drendel.jpg" alt="Martin Drendel, CEO und Gründer von 741.Studio" width="1000" height="1269" loading="lazy"></div>
 <div class="rv-r"><h2>{inl(h("S06"))}</h2><p>{inl(paras("S06")[0])}</p><div class="cta-row">{cta('light', section='person')}</div></div>
</div></section>'''


def s07():
    l = L('S07')
    rows = [r for r in l if r.startswith('|') and not r.startswith('| ---')]
    head = [c.strip() for c in rows[0].strip('|').split('|')]
    body = ''.join('<tr>' + ''.join(f'<td>{inl(c.strip())}</td>' for c in r.strip('|').split('|')) + '</tr>' for r in rows[1:])
    quote = next(x for x in l if x.startswith('„Hey,'))
    qby = next(x for x in l if x.startswith('Martin Hüwel, Heilpraktiker'))
    feel = next(x for x in l if x.startswith('So fühlt sich'))
    live = next(x for x in l if x.startswith('Live ansehen'))
    cols = []
    cur = None
    for x in l:
        if x.startswith('### '):
            cur = [x[4:], []]; cols.append(cur)
        elif cur is not None and re.match(r'\d+\. ', x):
            cur[1].append(re.sub(r'^\d+\. ', '', x))
    colhtml = ''
    for ci, (t, items) in enumerate(cols):
        lis = ''.join(f'<li><span class="n">{n}</span>{inl(it)}</li>' for n, it in enumerate(items, 1))
        colhtml += f'<div class="flow {"old" if ci == 0 else "new"} rv"><h3>{inl(t)}</h3><ol>{lis}</ol></div>'
    return f'''
<section class="white" id="s07"><div class="wrap">
 <h2 class="center rv">{inl(h("S07"))}</h2>
 <p class="center narrow rv">{inl(paras("S07")[0])}</p>
 <figure class="quote real rv"><span class="qm">“</span><blockquote>{inl(quote)}</blockquote><figcaption>{inl(qby)}</figcaption></figure>
 <h3 class="center feel rv">{inl(feel)}</h3>
 <div class="flows">{colhtml}</div>
 <table class="ba rv"><thead><tr><th>{inl(head[0])}</th><th class="today">{inl(head[1])}</th></tr></thead><tbody>{body}</tbody></table>
 <div class="case-foot rv"><p class="live">{inl(live)}</p>{cta(section='fallbeispiel')}</div>
</div></section>'''


def acc_items(sid):
    l = L(sid)
    items, cur = [], None
    for x in l:
        if x.startswith('### '):
            cur = [x[4:], []]; items.append(cur)
        elif cur is not None:
            cur[1].append(x)
    return items


def acc_body(lines):
    out, tbl = '', [r for r in lines if r.startswith('|') and not r.startswith('| ---')]
    for x in lines:
        if not x.startswith('|'):
            out += f'<p>{inl(x)}</p>'
    if tbl:
        hd = [c.strip() for c in tbl[0].strip('|').split('|')]
        out += '<table class="cost"><thead><tr>' + ''.join(f'<th>{inl(c)}</th>' for c in hd) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{inl(c.strip())}</td>' for c in r.strip('|').split('|')) + '</tr>' for r in tbl[1:]) + '</tbody></table>'
    return out


def accordion(sid, cls):
    items = acc_items(sid)
    half = (len(items) + 1) // 2
    cols = [items[:half], items[half:]]
    html_cols = ''
    for ci, col in enumerate(cols):
        html_cols += '<div class="acc-col">'
        for k, (q, a) in enumerate(col):
            op = ci == 0 and k == 0
            html_cols += f'<details class="acc rv"{" open" if op else ""}><summary>{inl(q)}<span class="chev" aria-hidden="true"></span></summary><div class="acc-b">{acc_body(a)}</div></details>'
        html_cols += '</div>'
    return f'<section class="{cls}" id="{sid.lower()}"><div class="wrap"><h2 class="rv">{inl(h(sid))}</h2><div class="acc-grid">{html_cols}</div></div></section>'


def s10():
    return f'<section class="lemon" id="s10"><div class="wrap center narrow"><h2 class="rv">{inl(h("S10"))}</h2><p class="rv">{inl(paras("S10")[0])}</p></div></section>'


def s11():
    proof = next(x for x in L('S11') if x.startswith('Praxis Hüwel'))
    return f'''
<section class="dark closer" id="s11"><div class="wrap center">
 <h2 class="rv">{inl(h("S11"))}</h2>
 <ul class="checks inline rv">{''.join(f'<li>{CHECK}{inl(b)}</li>' for b in bullets('S11'))}</ul>
 <p class="proofline rv">{inl(proof)}</p>
 <div class="cta-row rv">{cta('light big', breathing=True, section='abschluss')}</div>
 <p class="reassure rv">{REASSURE}</p>
</div></section>'''


CSS = (HERE / 'style.css').read_text(encoding='utf8')
JS = (HERE / 'motion.js').read_text(encoding='utf8')
body = s01() + s02() + s03() + s04() + s05() + s06() + s07() + accordion('S08', 'cream') + accordion('S09', 'white') + s10() + s11()
NAV = ['Home', 'Portfolio', 'Services', 'Über uns', 'Blog', 'Kontakt']
ld = '''{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://741.studio/#741studio","name":"741.Studio","url":"https://741.studio/","email":"hello@741.studio"},{"@type":"Service","name":"741 KI-CMS","provider":{"@id":"https://741.studio/#741studio"},"serviceType":"Website mit KI-gestütztem Content-Management","url":"https://741.studio/de/pages/ki-website.html"},{"@type":"Person","name":"Martin Drendel","jobTitle":"CEO und Gründer","worksFor":{"@id":"https://741.studio/#741studio"}},{"@type":"WebPage","name":"''' + FM['title'] + '''","url":"https://741.studio/de/pages/ki-website.html"}]}'''
out = f'''<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(FM["title"])}</title><meta name="description" content="{html.escape(FM["meta"])}"><meta name="robots" content="noindex,nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Fraunces:ital,opsz,wght@1,9..144,500;1,9..144,600&display=swap" rel="stylesheet">
<script type="application/ld+json">{ld}</script>
<style>{CSS}</style></head>
<body>
<header class="hd" id="hd"><div class="wrap hd-in"><a class="logo" href="#"><img src="assets/logo-741-black.png" alt="741.Studio" width="70" height="48"></a>
<nav>{"".join(f'<a href="#">{n}</a>' for n in NAV)}</nav><a class="hd-btn" href="{BOOK}" target="_blank" rel="noopener">Start Now</a></div></header>
<main>{body}</main>
<footer class="ft"><div class="wrap ft-in"><img src="assets/logo-741-white.png" alt="741.Studio" width="60" height="41" loading="lazy"><nav>{"".join(f'<a href="#">{n}</a>' for n in NAV)}</nav><span>© 2026 741.Studio</span></div></footer>
<script>{JS}</script></body></html>'''
(RUN / '07-prototype/v3/index.html').write_text(out, encoding='utf8')
print('built', len(out))
