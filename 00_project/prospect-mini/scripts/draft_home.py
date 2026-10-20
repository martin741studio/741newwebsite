#!/usr/bin/env python3
"""Prospect mini workflow, step 6a: first-screen homepage draft in one command (proposal 30, 2026-10-12).

Usage: draft_home.py <slug|prospect_dir> [--out <dir>] [--force] [--service "<word>"]
Builds <dir>/index.html (default prospects/<slug>/draft/) on the model prospects/ana-violeta-fredel/draft/index.html:
the prospect's logo, portrait and room photo (downloaded, logo margins cropped), brand colours from the site CSS,
"Sie" or "du" as on the site, "ich" or "wir" as on the site, headline "<service> in <city>", stars + review count,
phone, address, trust row. Health: no healing or success promise in the text.
Agent C then only checks the draft, fixes what is wrong and takes the headless screenshot.
Reads intake.json|intake.md, evidence/site.json, evidence/home-images.txt, the Falcon report, the Google panel, the live homepage.
Standard library + PIL.
"""
import colorsys, html, io, json, os, re, sys, time, urllib.request
from collections import Counter
from urllib.parse import urljoin, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_lib as L
from evidence_lib import de

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
GENERIC = r'^(home|start|startseite|kontakt|impressum|datenschutz|über|ueber|about|team|kosten|preise|aktuelles|blog|news|anfahrt|termin|termine|links|faq|jobs|karriere|praxis|willkommen|mehr|menü|menu|landhaus|galerie|login|suche|de|en|therapien|leistungen|angebot|angebote|behandlungen|schwerpunkte|services|organisatorisches|therapeutinnen|therapeuten|skip|zum inhalt|see more|fallbeispiele|referenzen|fundus)\b'
WIDGET = {'3b5998', '4267b2', '1877f2', '1da1f2', '25d366', '4285f4', 'db4437', '0f9d58', 'f4b400', 'e1306c', '0077b5', 'ff0000'}  # social and Google widgets


def cm4all(u):
    """cm4all sites: '/.cm4all/uproc.php/0/<dir>/.<file>/picture-200?_=x' -> the original '/.cm4all/uproc.php/0/<dir>/<file>' (curl -L target)."""
    m = re.match(r'(.*/\.cm4all/(?:uproc\.php/0|mediadb)/(?:[^./][^/]*/)*)\.?([^/?]+?)(?:/picture-\d+)?/?(?:\?.*)?$', u)
    return m.group(1) + m.group(2) if m else u


def fetch(url, timeout=20):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=timeout) as r:
            return r.read(), r.geturl()
    except Exception:
        return b'', url


def colours(page, base):
    """Saturated brand colours from inline CSS and the first 4 stylesheets, most used first."""
    css = page
    for href in re.findall(r'<link[^>]+rel=["\']?stylesheet["\']?[^>]*href=["\']([^"\']+)', page, re.I)[:4] + \
            re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\'][^>]*rel=["\']?stylesheet', page, re.I)[:2]:
        css += fetch(urljoin(base, href), 10)[0].decode('utf-8', 'replace')
    c = Counter()
    for h in re.findall(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b', css):
        h = (''.join(x * 2 for x in h) if len(h) == 3 else h).lower()
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        hh, l, s = colorsys.rgb_to_hls(r, g, b)
        if s > 0.25 and 0.15 < l < 0.75 and h not in WIDGET: c[h] += 1
    for r, g, b in re.findall(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', css):
        hh, l, s = colorsys.rgb_to_hls(int(r) / 255, int(g) / 255, int(b) / 255)
        if s > 0.25 and 0.15 < l < 0.75 and '%02x%02x%02x' % (int(r), int(g), int(b)) not in WIDGET: c['%02x%02x%02x' % (int(r), int(g), int(b))] += 1
    return [h for h, _ in c.most_common(8)]


def shade(h, l_to=None, mix_white=None, factor=None):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    if mix_white is not None:
        r, g, b = (x + (1 - x) * mix_white for x in (r, g, b))
    else:
        hh, l, s = colorsys.rgb_to_hls(r, g, b)
        l = l_to if l_to is not None else l * factor
        r, g, b = colorsys.hls_to_rgb(hh, l, min(s, 0.6) if l_to is not None else s)
    return '#%02x%02x%02x' % tuple(round(x * 255) for x in (r, g, b))


def images(pdir, page, base, s, extra=()):
    """Image URLs: operator list, the <img> tags (src, data-src, srcset, alt text) of the homepage and extra pages, site.json, CSS backgrounds."""
    out = []
    page = page + ''.join(extra)
    f = os.path.join(pdir, 'evidence', 'home-images.txt')
    if os.path.exists(f): out += [(l.strip(), '') for l in open(f, encoding='utf-8') if l.strip().startswith('http')]
    for tag in re.findall(r'<img\b[^>]*>', page, re.I):
        src = re.search(r'(?:data-src|src)=["\']([^"\']+)', tag) or re.search(r'srcset=["\']([^"\'\s]+)', tag)
        alt = re.search(r'alt=["\']([^"\']*)', tag)
        cls = re.search(r'(?:class|id)=["\']([^"\']*)', tag)
        if src: out.append((urljoin(base, html.unescape(src.group(1))), ((alt.group(1) if alt else '') + ' ' + (cls.group(1) if cls else '')).lower()))
    for u in re.findall(r'srcset=["\']([^"\'\s]+)', page): out.append((urljoin(base, html.unescape(u)), ''))
    out += [(u, '') for u in s.get('images_home') or []]
    out += [(urljoin(base, u), '') for u in re.findall(r'url\(["\']?([^"\')]+\.(?:jpe?g|png|webp))', page, re.I)]
    seen, res = set(), []
    for u, a in out:
        u = cm4all(u)
        if u in seen or re.search(r'\.svg(\?|$)|data:|_pixel|pixel\.|tracking|/favicon', u, re.I): continue
        seen.add(u); res.append((u, a))
    return res[:24]


def load(urls):
    """Download in parallel (8 at a time); drop tiny files, broken images and byte-identical copies."""
    import hashlib
    from concurrent.futures import ThreadPoolExecutor
    from PIL import Image
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(lambda x: (x, fetch(x[0], 15)), urls))
    got, seen = [], set()
    for (u, alt), (b, final) in res:
        h = hashlib.md5(b).hexdigest()
        if len(b) < 2000 or h in seen: continue
        seen.add(h)
        try:
            im = Image.open(io.BytesIO(b)); im.load()
        except Exception:
            continue
        got.append({'url': final, 'alt': alt, 'im': im, 'w': im.width, 'h': im.height})
    return got


def crop_logo(im):
    from PIL import Image, ImageChops
    im = im.convert('RGBA')
    box = im.getchannel('A').getbbox()
    if box == (0, 0, im.width, im.height):  # no transparency: crop the white margin
        bg = Image.new('RGB', im.size, (255, 255, 255))
        box = ImageChops.difference(im.convert('RGB'), bg).convert('L').point(lambda x: 255 if x > 18 else 0).getbbox()
    return im.crop(box) if box else im


def main():
    t0 = time.time()
    args = sys.argv[1:]
    out = service = None
    if '--out' in args: i = args.index('--out'); out = args[i + 1]; del args[i:i + 2]
    if '--service' in args: i = args.index('--service'); service = args[i + 1]; del args[i:i + 2]
    force = '--force' in args
    if force: args.remove('--force')
    pdir = args[0] if os.path.isdir(args[0]) else os.path.join(L.ROOT, '00_project', 'prospects', args[0])
    out = out or os.path.join(pdir, 'draft')
    if os.path.exists(os.path.join(out, 'index.html')) and not force: raise SystemExit(f'{out}/index.html exists: use --out <dir> or --force')
    os.makedirs(out, exist_ok=True)
    it, F, s, pn = L.intake(pdir), L.facts(pdir), L.site(pdir), L.panel(pdir)
    sc = F.get('scan') or {}
    fr = L.falcon(pdir)
    website = it.get('website') or s.get('home_final_url') or s.get('home')
    raw, base = fetch(website)
    page = raw.decode('utf-8', 'replace')
    text = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style|noscript)\b.*?</\1>', ' ', page, flags=re.S | re.I))))

    # words: service, city, Sie/du, ich/wir
    kw = (sc.get('keyword') or '').split()
    city = it.get('city') or (kw[-1].title() if len(kw) > 1 else '')
    service = service or (kw[0].title() if kw else 'Praxis')
    if re.search(r'\b' + re.escape(service) + r'(?:in|/in)\b', text + ' ' + (it.get('home_title') or ''), re.I) and len(re.findall(r'\b' + re.escape(service) + r'in\b', text, re.I)) >= len(re.findall(r'\b' + re.escape(service) + r'\b', text, re.I)) / 2:
        service += 'in'  # the site uses the female form
    sie = (it.get('site_address') or 'Sie') != 'du'
    wir = len(re.findall(r'\b(wir|uns|unser|unsere|unserem|unseren)\b', text, re.I)) > len(re.findall(r'\b(ich|mich|mir|mein|meine|meinem|meinen)\b', text, re.I))
    who = it.get('name') or ''
    company = it.get('business') or pn.get('name') or sc.get('me_name') or who
    me = L.own_place(fr, it.get('place_id'), website, company) if fr else {}
    me = me or {}
    rating = pn.get('rating') or float(me.get('rating') or 0)
    reviews = pn.get('reviews') if pn.get('reviews') is not None else int(me.get('reviews') or 0)
    phone = pn.get('phone') or me.get('phone') or ''
    if not phone:
        tel = (re.findall(r'href=["\']tel:([^"\']+)', page) or [''])[0]
        phone = tel
    address = pn.get('address') or me.get('address') or ''
    district = (re.search(r'\d{4,5}\s+(.+)$', address) or [None, city])[1]
    years = re.search(r'(\d{1,2})\s*-?\s*(?:jährige|jährigen|Jahre|Jahren)\w*\s+(?:\w+\s+){0,2}(?:Erfahrung|Berufserfahrung)', text, re.I)
    nav = []
    for a in re.findall(r'<a\b[^>]*>(.*?)</a>', re.search(r'<nav\b.*?</nav>', page, re.S | re.I).group(0) if re.search(r'<nav\b.*?</nav>', page, re.S | re.I) else page[:20000], re.S | re.I):
        t = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', a))).strip()
        if 2 < len(t) < 32 and t not in nav and not re.search(r'skip to|zum inhalt|springen|see more', t, re.I): nav.append(t)
    brand = set(re.findall(r'\w{4,}', (L.domain(website) + ' ' + (it.get('business') or '')).lower()))
    services = [n for n in nav if not re.search(GENERIC, n, re.I) and not (set(re.findall(r'\w{4,}', n.lower())) & brand)][:3]

    # brand colours
    cols = colours(page, base) or ['84483f']
    acc = cols[0]
    head_c = next((c for c in cols[1:] if abs(colorsys.rgb_to_hls(*(int(c[i:i + 2], 16) / 255 for i in (0, 2, 4)))[0] - colorsys.rgb_to_hls(*(int(acc[i:i + 2], 16) / 255 for i in (0, 2, 4)))[0]) > 0.08), None)
    C = {'acc': '#' + acc, 'acc_d': shade(acc, factor=0.8), 'head': shade(acc, l_to=0.22), 'ink': '#2d2622', 'cream': shade(acc, mix_white=0.9), 'second': '#' + head_c if head_c else None}

    # images: logo, portrait, room
    got = load(images(pdir, page, base, s))
    if sum(1 for g in got if g['w'] * g['h'] >= 40000) < 3:  # few photos on the homepage: look at up to 4 more pages
        uf = os.path.join(pdir, 'evidence', 'site-page-urls.txt')
        more = [l.strip() for l in open(uf, encoding='utf-8')][1:5] if os.path.exists(uf) else []
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(4) as ex:
            extra = [b.decode('utf-8', 'replace') for b, _ in ex.map(lambda u: fetch(u, 12), more)]
        seen = {g['url'] for g in got}
        got += [g for g in load([x for x in images(pdir, '', base, {}, extra)][:16]) if g['url'] not in seen]
    seal = r'siegel|seal|mitglied|member|verband|vfp|award|zertifikat|badge|partner|qualit'  # membership seals are never the logo
    logo = next((g for g in got if 'logo' in (g['url'] + g['alt']).lower() and not re.search(seal, (g['url'] + g['alt']).lower())), None)
    rest = [g for g in got if g is not logo and g['w'] * g['h'] >= 40000 and not re.search(seal, (g['url'] + g['alt']).lower())]
    names = [w.lower() for w in re.findall(r'\w{3,}', who)]
    pic = lambda g: (g['url'] + ' ' + g['alt']).lower()
    portrait = next((g for g in rest if any(n in pic(g) for n in names) or re.search(r'portrait|portr|profil|ueber|über|about|\bich\b|inhaber', pic(g))), None) \
        or next((g for g in sorted(rest, key=lambda g: -g['h'] / g['w']) if g['h'] / g['w'] > 1.1), None)
    room = next((g for g in sorted([g for g in rest if g is not portrait], key=lambda g: -g['w'] * g['h']) if g['w'] / g['h'] > 1.2), None) \
        or next((g for g in rest if g is not portrait), None)
    files = {}
    if logo:
        crop_logo(logo['im']).save(os.path.join(out, 'logo.png')); files['logo'] = logo['url']
    if portrait:
        portrait['im'].convert('RGB').save(os.path.join(out, 'portrait.jpg'), quality=88); files['portrait'] = portrait['url']
    if room:
        room['im'].convert('RGB').save(os.path.join(out, 'praxis.jpg'), quality=88); files['praxis'] = room['url']

    E = html.escape
    last_w = re.split(r'[\s-]', service.strip())[-1].lower()
    fem = last_w.endswith(('in', 'ie', 'ung', 'heit', 'keit', 'schaft', 'praxis', 'kanzlei')) or last_w in ('beratung', 'therapie', 'physiotherapie', 'osteopathie')  # "Experte", "Coach", "Berater" stay masculine
    Y = ('Ihre' if fem else 'Ihr') if sie else ('Deine' if fem else 'Dein')
    sub = (f'Sie suchen {"eine" if fem else "einen"} {service} in {city}? ' if sie else f'Du suchst {"eine" if fem else "einen"} {service} in {city}? ') \
        + (('Wir nehmen uns Zeit für Ihr Anliegen' if wir else 'Ich nehme mir Zeit für Ihr Anliegen') if sie else ('Wir nehmen uns Zeit für dein Anliegen' if wir else 'Ich nehme mir Zeit für dein Anliegen')) \
        + (f': {", ".join(services[:-1])} und {services[-1]}.' if len(services) > 1 else '.')
    note = ('Rufen Sie an oder schreiben Sie uns. Wir melden uns persönlich bei Ihnen.' if wir else 'Rufen Sie an oder schreiben Sie mir. Ich melde mich persönlich bei Ihnen.') if sie else \
        ('Ruf an oder schreib uns. Wir melden uns persönlich bei dir.' if wir else 'Ruf an oder schreib mir. Ich melde mich persönlich bei dir.')
    stars = f'<div class="stars"><i>★★★★★</i> {f'{rating:.1f}'.replace('.', ',')} bei Google · {reviews} Bewertungen</div>' if rating >= 4.0 and reviews else ''
    trust = [(service, f'{"mit eigener Praxis" if not wir else "Praxis"} in {district}')]
    if years: trust.append((f'{years.group(1)} Jahre', 'Erfahrung'))
    if len(services) >= 2: trust.append((f'{len(services)} Schwerpunkte' if len(services) < 3 else services[0], ' · '.join(services[1:3]) if len(services) >= 3 else ' · '.join(services)))
    if rating >= 4.0 and reviews: trust.append((f'{f'{rating:.1f}'.replace('.', ',')} ★ bei Google', f'{reviews} Bewertungen'))
    if phone and len(trust) < 4: trust.append(('Telefon', phone))
    navh = ''.join(f'<span>{E(n)}</span>' for n in (nav[:5] if len(nav) >= 3 else ['Leistungen', 'Erster Termin', 'Kosten', 'Über mich', 'Anfahrt']))
    me_card = (f'<div class="me"><img src="portrait.jpg" alt="{E(who)}"><div><b>{E(who)}</b>{E(service)} in {E(district)}</div></div>' if portrait else '')
    doc = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Entwurf erster Bildschirm – {E(company)}</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{{--acc:{C['acc']};--acc-d:{C['acc_d']};--head:{C['head']};--ink:{C['ink']};--cream:{C['cream']};}}
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:Inter,system-ui,sans-serif;color:var(--ink);background:#fff;width:100%;height:100vh;overflow:hidden}}
  .bar{{background:var(--acc-d);color:#fff;font-size:15px;text-align:center;padding:10px}}
  .bar b{{font-weight:700}}
  header{{display:flex;align-items:center;justify-content:space-between;padding:14px 120px;border-bottom:1px solid #eee}}
  header img{{height:70px;max-width:300px;object-fit:contain}}
  header .brand{{font-family:Fraunces,serif;font-size:26px;color:var(--head)}}
  nav{{display:flex;gap:30px;font-size:16px;font-weight:500;color:#4a3f39}}
  .btn{{display:inline-block;background:var(--acc);color:#fff;font-weight:700;border-radius:999px;padding:14px 26px;font-size:16px}}
  .hero{{display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center;padding:52px 120px 36px;background:linear-gradient(180deg,#fff,var(--cream))}}
  .eyebrow{{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--acc);font-weight:700}}
  h1{{font-family:Fraunces,serif;font-weight:600;font-size:48px;line-height:1.08;margin:14px 0 18px;color:var(--head)}}
  h1 span{{color:var(--acc)}}
  .sub{{font-size:19px;line-height:1.55;color:#55493f;max-width:600px}}
  .stars{{display:flex;align-items:center;gap:10px;margin:20px 0 22px;font-size:15.5px;color:#55493f}}
  .stars i{{color:#f2b01e;font-style:normal;letter-spacing:2px;font-size:18px}}
  .ctas{{display:flex;gap:14px;align-items:center;margin-top:22px}}
  .stars + .ctas{{margin-top:0}}
  .ghost{{border:1.5px solid #d8cbbf;border-radius:999px;padding:13px 22px;font-size:16px;font-weight:600;color:var(--ink)}}
  .note{{font-size:14px;color:#7a6d63;margin-top:12px}}
  .pic{{position:relative;border-radius:22px;overflow:hidden;height:470px;box-shadow:0 20px 50px rgba(0,0,0,.12);background:var(--cream)}}
  .pic img.main{{width:100%;height:100%;object-fit:cover;object-position:50% 60%}}
  .me{{position:absolute;left:18px;bottom:18px;display:flex;align-items:center;gap:12px;background:#fff;border-radius:14px;padding:10px 16px 10px 10px;box-shadow:0 6px 20px rgba(0,0,0,.14);font-size:14.5px}}
  .me img{{width:56px;height:56px;border-radius:50%;object-fit:cover;object-position:50% 25%}}
  .me b{{display:block;font-size:15.5px}}
  .trust{{display:grid;grid-template-columns:repeat({len(trust)},1fr);gap:14px;padding:0 120px}}
  .trust div{{background:#fff;border:1px solid #eadbcd;border-radius:14px;padding:14px 16px;font-size:14.5px;color:#55493f}}
  .trust b{{display:block;color:var(--ink);font-size:16px;margin-bottom:2px}}
</style>
</head>
<body>
  <div class="bar">{('Termin vereinbaren: <b>' + E(phone) + '</b>') if phone else 'Termin vereinbaren'}{(' · ' + E(address)) if address else ''}</div>
  <header>
    {f'<img src="logo.png" alt="{E(company)}">' if logo else f'<span class="brand">{E(company)}</span>'}
    <nav>{navh}</nav>
    <span class="btn">Termin vereinbaren</span>
  </header>
  <section class="hero">
    <div>
      <div class="eyebrow">{E(' · '.join(services) if services else company)}</div>
      <h1>{Y} {E(service)} <span>in {E(city)}.</span></h1>
      <p class="sub">{E(sub)}</p>
      {stars}
      <div class="ctas"><span class="btn">{"Ersttermin vereinbaren" if sie else "Ersttermin vereinbaren"}</span><span class="ghost">{"Leistungen ansehen" if services else "Mehr erfahren"} →</span></div>
      <p class="note">{E(note)}</p>
    </div>
    <div class="pic">{'<img class="main" src="praxis.jpg" alt="">' if room else ''}{me_card}</div>
  </section>
  <div class="trust">
    {''.join(f'<div><b>{E(a)}</b>{E(b)}</div>' for a, b in trust)}
  </div>
</body>
</html>
'''
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(doc)
    if not logo: files['logo'] = 'NONE: no logo image on the site, text brand used'
    meta = {'out': out, 'colours': C, 'service': service, 'city': city, 'address_form': 'Sie' if sie else 'du', 'we': wir, 'images': files,
            'candidates': len(got), 'nav': nav[:8], 'services': services, 'trust': trust, 'secs': round(time.time() - t0, 1),
            'check': ['logo, portrait and room photo are the right pictures (stock photos out)', 'headline names a person or business, not only a field ("Ihr Soziokratie-Berater", not "Ihre Soziokratie")',
                      'practice words fit the branch (Praxis, Ersttermin)', 'headline follows the main advice of the page', 'no healing or success promise']}
    json.dump(meta, open(os.path.join(out, 'draft-home.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(meta, ensure_ascii=False))


if __name__ == '__main__':
    main()
