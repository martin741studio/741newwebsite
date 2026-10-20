"""ShuiGuru page generator v2 - real website sections instead of one text column.

Layout per page:
  Hero      full-width photo, H1 + Direkt-Antwort + contact line + button
  Sections  full-width bands, alternating white / light teal
            - text-only section      -> 2 columns (heading left, text right)
                                        or image + text split when an image is assigned
            - section with component -> centred heading + intro, component full width
            - section with H3 rows   -> each H3 becomes an image/text row (Startseite pillars)
            - FAQ                    -> heading left, accordions right
            - "Aktuelle Aktion"      -> highlighted yellow band
  CTA band  dark teal
Text is taken 1:1 from the approved source file. 741-only parts are dropped.

Usage: python3 build_v2.py <page-key>      (config in pages.json, media in media.json)
"""
import json, re, sys, os
from bs4 import BeautifulSoup, NavigableString

HERE = os.path.dirname(os.path.abspath(__file__))
KEY = sys.argv[1]
CFG = json.load(open(f'{HERE}/pages.json'))[KEY]
MEDIA = json.load(open(f'{HERE}/media.json'))
SRC = f'{HERE}/../{CFG["src"]}'
SKIP_BLOCKS = {'Wortzahl-Urteil'}

soup = BeautifulSoup(re.sub(r'data:image/[^"\')]+', 'DATAURI', open(SRC).read()), 'html.parser')

# ---------- block helpers (core blocks only) ----------
def inner(el):
    return ''.join(str(c) for c in el.contents).strip()

def p(html, cls=None):
    if cls:
        return f'<!-- wp:paragraph {{"className":"{cls}"}} -->\n<p class="{cls}">{html}</p>\n<!-- /wp:paragraph -->'
    return f'<!-- wp:paragraph -->\n<p>{html}</p>\n<!-- /wp:paragraph -->'

def h(level, html, cls=None):
    attrs = {}
    if level != 2: attrs['level'] = level
    if cls: attrs['className'] = cls
    a = (' ' + json.dumps(attrs, ensure_ascii=False)) if attrs else ''
    c = 'wp-block-heading' + (f' {cls}' if cls else '')
    return f'<!-- wp:heading{a} -->\n<h{level} class="{c}">{html}</h{level}>\n<!-- /wp:heading -->'

def ul(items, cls='sg-check'):
    li = '\n'.join(f'<!-- wp:list-item -->\n<li>{i}</li>\n<!-- /wp:list-item -->' for i in items)
    return f'<!-- wp:list {{"className":"{cls}"}} -->\n<ul class="wp-block-list {cls}">{li}</ul>\n<!-- /wp:list -->'

def group(content, cls, tag='div', anchor=None):
    attrs = {'className': cls}
    if tag != 'div': attrs['tagName'] = tag
    if anchor: attrs['anchor'] = anchor
    idattr = f' id="{anchor}"' if anchor else ''
    return (f'<!-- wp:group {json.dumps(attrs)} -->\n<{tag}{idattr} class="wp-block-group {cls}">'
            f'{content}</{tag}>\n<!-- /wp:group -->')

def columns(cols, cls):
    """cols = [(width or None, content), ...]"""
    out = []
    for w, content in cols:
        if w:
            out.append(f'<!-- wp:column {{"width":"{w}"}} -->\n<div class="wp-block-column" style="flex-basis:{w}">{content}</div>\n<!-- /wp:column -->')
        else:
            out.append(f'<!-- wp:column -->\n<div class="wp-block-column">{content}</div>\n<!-- /wp:column -->')
    return (f'<!-- wp:columns {{"className":"{cls}"}} -->\n<div class="wp-block-columns {cls}">'
            + '\n'.join(out) + '</div>\n<!-- /wp:columns -->')

def image(mid, alt):
    m = MEDIA[str(mid)]
    return (f'<!-- wp:image {{"id":{mid},"sizeSlug":"large","linkDestination":"none","className":"sg-img"}} -->\n'
            f'<figure class="wp-block-image size-large sg-img"><img src="{m["large"]}" alt="{alt}" class="wp-image-{mid}"/></figure>\n'
            '<!-- /wp:image -->')

def button(text, href, cls='sg-btn'):
    return ('<!-- wp:buttons -->\n<div class="wp-block-buttons">'
            f'<!-- wp:button {{"className":"{cls}"}} -->\n<div class="wp-block-button {cls}">'
            f'<a class="wp-block-button__link wp-element-button" href="{href}">{text}</a></div>\n'
            '<!-- /wp:button --></div>\n<!-- /wp:buttons -->')

def faq_block(el):
    return (f'<!-- wp:details {{"className":"sg-faq"}} -->\n<details class="wp-block-details sg-faq"><summary>{el.select_one(".q").get_text()}</summary>'
            f'{p(inner(el.select_one(".a")))}</details>\n<!-- /wp:details -->')

def cols_cls(cards):
    """4 short cards -> one row of 4; 4 long cards -> 2x2; otherwise auto."""
    if len(cards) != 4:
        return ''
    avg = sum(len(c.get_text(' ', strip=True)) for c in cards) / 4
    return ' sg-cols-4' if avg < 200 else ' sg-cols-2'

def component(el):
    """Rich element -> block markup, or None if it is plain text."""
    cls = el.get('class') or []
    if el.name == 'ul':
        return ul([inner(li) for li in el.find_all('li', recursive=False)])
    if 'step-flow' in cls:
        return group('\n'.join(group(p(f'<strong>{st.select_one("b").get_text()}</strong>', 'sg-step-title') + '\n'
                                     + p(inner(st.select_one('p'))), 'sg-step') for st in el.select('.step')), 'sg-steps')
    if 'el-grid' in cls:
        cards = []
        for c in el.select('.el-card'):
            ic = c.select_one('.ic')
            body = p((f'<span class="sg-ic">{ic.get_text()}</span>' if ic else '') + f'<strong>{inner(c.select_one("b"))}</strong>', 'sg-card-title')
            if c.select_one('p'):
                body += '\n' + p(inner(c.select_one('p')))
            cards.append(group(body, 'sg-card'))
        return group('\n'.join(cards), 'sg-cards' + cols_cls(el.select('.el-card')))
    if 'price-grid' in cls:
        return group('\n'.join(group(p(f'<strong>{inner(c.select_one(".ttl"))}</strong>', 'sg-card-title') + '\n'
                                     + p(inner(c.select_one('.amt')), 'sg-price') + '\n' + p(inner(c.select_one('p'))), 'sg-card')
                               for c in el.select('.price-card')), 'sg-cards' + cols_cls(el.select('.price-card')))
    if el.name == 'div' and not cls and el.select('.stat-badge'):
        return p(' '.join(f'<span class="sg-badge"><strong>{b.b.get_text()}</strong>{"".join(str(x) for x in b.contents[1:])}</span>'
                          for b in el.select('.stat-badge')), 'sg-badges')
    return None

# ---------- hero ----------
blocks = [b for b in soup.select('main .block') if b.get('data-fb') not in SKIP_BLOCKS]
lead_html = None
for b in blocks:
    kids = [k for k in b.children if not isinstance(k, NavigableString)]
    if len(kids) == 1 and 'answer' in (kids[0].get('class') or []):
        lead_html = inner(kids[0])
        blocks.remove(b)
        break

hero = soup.select_one('section.hero')
hm = MEDIA[str(CFG['hero'])]
hero_parts = [p(CFG.get('eyebrow', 'ShuiGuru · Feng Shui Beratung · Maria Brasse'), 'sg-eyebrow'),
              h(1, inner(hero.select_one('h1')), 'sg-h1')]
if lead_html:
    hero_parts.append(p(lead_html, 'sg-hero-lead'))
hero_parts.append(p(' · '.join(inner(s) for s in hero.select('.hero-sub span')), 'sg-hero-line'))
cta = hero.select_one('.cta-btn')
if cta:
    hero_parts.append(button(cta.get_text(), cta['href']))
out = [group(group('\n'.join(hero_parts), 'sg-hero-box'), 'sg-hero alignfull' + (' sg-hero-split' if CFG.get('hero_split') else ''), tag='section')]

# ---------- sections ----------
imgs = list(CFG.get('images', []))           # [[media id, alt], ...] for text/image splits
rows_imgs = list(CFG.get('row_images', []))  # for H3 rows (Startseite pillars)
band = 0
img_side = 0
text_n = 0
for b in blocks:
    kids = [k for k in b.children if not isinstance(k, NavigableString)]
    head = kids[0] if kids and kids[0].name == 'h2' else None
    body = kids[1:] if head else kids
    h2 = h(2, inner(head)) if head else ''
    note = bool(b.get('style'))
    faqs = [k for k in body if 'faq' in (k.get('class') or [])]
    h3s = [k for k in body if k.name == 'h3']
    comps = [k for k in body if component(k) is not None]

    if note:
        content = h2 + '\n' + '\n'.join(p(inner(k)) for k in body)
        out.append(group(group(content, 'sg-inner sg-narrow'), 'sg-band sg-band-note alignfull', tag='section'))
        continue

    headless_text = not head and not faqs and not h3s and not comps
    if not headless_text:
        band += 1
    tone = 'sg-band-tint' if band % 2 == 0 else 'sg-band-white'
    if headless_text:
        out.append(group(group('\n'.join(p(inner(k)) for k in body), 'sg-inner sg-narrow sg-follow'),
                         f'sg-band sg-band-follow {tone} alignfull', tag='section'))
        continue

    if faqs:
        intro = '\n'.join(p(inner(k)) for k in body if k.name == 'p')
        content = columns([('38%', h2 + intro), (None, '\n'.join(faq_block(k) for k in faqs))], 'sg-split sg-split-faq')
    elif h3s:
        # intro paragraphs before the first H3, then one row per H3
        first = body.index(h3s[0])
        intro = '\n'.join(p(inner(k)) for k in body[:first])
        rows, cur = [], None
        for k in body[first:]:
            if k.name == 'h3':
                cur = [k, []]; rows.append(cur)
            else:
                cur[1].append(k)
        row_html = []
        h3_links = list(CFG.get('h3_links', []))
        for n, (h3, ps) in enumerate(rows):
            h3_html = inner(h3)
            if h3_links:
                h3_html = f'<a href="{h3_links.pop(0)}">{h3_html}</a>'
            text = h(3, h3_html) + '\n' + '\n'.join(component(k) or p(inner(k)) for k in ps)
            if rows_imgs:
                mid, alt = rows_imgs.pop(0)
                cols = [('45%', image(mid, alt)), (None, text)]
                if n % 2: cols.reverse()
                row_html.append(columns(cols, 'sg-split sg-row'))
            else:
                row_html.append(group(text, 'sg-row-plain'))
        content = group(h2 + intro, 'sg-head-center') + '\n' + '\n'.join(row_html)
    elif comps:
        pre, post, seen = [], [], False
        for k in body:
            c = component(k)
            if c is not None:
                seen = True; post.append(c)
            elif not seen:
                pre.append(p(inner(k)))
            else:
                post.append(p(inner(k)))
        content = group(h2 + '\n' + '\n'.join(pre), 'sg-head-center') + '\n' + '\n'.join(post)
    else:
        text = '\n'.join(p(inner(k)) for k in body)
        text_n += 1
        if imgs and text_n % 2 == 1:
            mid, alt = imgs.pop(0)
            cols = [('45%', image(mid, alt)), (None, h2 + '\n' + text)]
            if img_side % 2: cols.reverse()
            img_side += 1
            content = columns(cols, 'sg-split sg-split-img')
        else:
            content = columns([('38%', h2), (None, text)], 'sg-split sg-split-text')
    out.append(group(group(content, 'sg-inner'), f'sg-band {tone} alignfull', tag='section', anchor=CFG.get('anchors', {}).get(b.get('data-fb'))))

# ---------- closing CTA ----------
c = soup.select_one('div.cta')
if c:
    lines = [s.strip() for s in c.get_text('\n').split('\n') if s.strip()]
    a = c.select_one('a')
    out.append(group(group('\n'.join([h(2, lines[0])] + ([p(' '.join(lines[1:-1]))] if lines[1:-1] else []) + [button(a.get_text(), a['href'], 'sg-btn sg-btn-light')]),
                           'sg-inner sg-narrow'), 'sg-band sg-band-cta alignfull', tag='section'))

# ---------- schema (+ map on Startseite) ----------
tech = soup.select_one('details.tech').get_text('\n')
schemas = []
m = re.search(r'Schema \(JSON-LD\)\s*(\{)', tech)
if m:
    obj, _ = json.JSONDecoder().raw_decode(tech[m.start(1):])
    if obj.get('@type') != 'FAQPage':
        schemas.append(obj)
faqs = soup.select('main .faq')
if faqs:
    schemas.append({'@context': 'https://schema.org', '@type': 'FAQPage',
                    'mainEntity': [{'@type': 'Question', 'name': f.select_one('.q').get_text(),
                                    'acceptedAnswer': {'@type': 'Answer', 'text': f.select_one('.a').get_text(' ', strip=True)}}
                                   for f in faqs]})
html_tail = ''
if CFG.get('map'):
    html_tail += ('<div class="sg-map"><iframe title="ShuiGuru auf Google Maps" src="https://www.google.com/maps?q=ShuiGuru+Feng+Shui+Beratung,+Warthestra%C3%9Fe+29,+12051+Berlin&amp;output=embed" '
                  'width="100%" height="380" style="border:0" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>\n')
html_tail += '\n'.join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
out.append('<!-- wp:html -->\n' + html_tail + '\n<!-- /wp:html -->')

css = open(f'{HERE}/page_v2.css').read().replace('%HERO%', hm['full']).replace('%HPOS%', CFG.get('hero_pos', 'center'))
for url in CFG.get('unlink', []):
    out = [re.sub(r'<a href="' + re.escape(url) + r'"[^>]*>(.*?)</a>', r'\1', o) for o in out]
page = '<!-- wp:html -->\n<style>' + css + '</style>\n<!-- /wp:html -->\n\n' + group('\n\n'.join(out), 'sg-page')
open(f'{HERE}/out/{KEY}.html', 'w').write(page)

title = re.search(r'Title[^:\n]*:\s*(.+)', tech).group(1).strip()
desc = re.search(r'Meta-Description[^:\n]*:\s*(.+)', tech).group(1).strip()
left = len(imgs) + len(rows_imgs)
print(json.dumps({'key': KEY, 'title': title, 'desc': desc, 'bands': band, 'unused_images': left, 'len': len(page)}, ensure_ascii=False))
