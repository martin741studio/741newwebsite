"""Convert one approved ShuiGuru page text (maria-text-*.html) into Gutenberg core blocks.

Text is taken 1:1 from the source file; only the markup changes.
Internal 741-only parts ("Wortzahl-Urteil", review toolbar, Technik block) are dropped.

Usage: python3 build_page.py <source.html> <hero-image-url or ''> <out.html>
Prints a JSON line with title / meta description / hero alt for the WP import.
"""
import json, re, sys, hashlib, base64
from bs4 import BeautifulSoup, NavigableString

SRC, IMG, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
SKIP_BLOCKS = {'Wortzahl-Urteil'}

raw = open(SRC).read()
soup = BeautifulSoup(re.sub(r'data:image/[^"\')]+', 'DATAURI', raw), 'html.parser')

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

def ul(items, cls):
    li = '\n'.join(f'<!-- wp:list-item -->\n<li>{i}</li>\n<!-- /wp:list-item -->' for i in items)
    return f'<!-- wp:list {{"className":"{cls}"}} -->\n<ul class="wp-block-list {cls}">{li}</ul>\n<!-- /wp:list -->'

def group(content, cls, tag='div'):
    attrs = {'className': cls}
    if tag != 'div': attrs['tagName'] = tag
    return (f'<!-- wp:group {json.dumps(attrs)} -->\n<{tag} class="wp-block-group {cls}">'
            f'{content}</{tag}>\n<!-- /wp:group -->')

def button(text, href, cls='sg-btn'):
    return ('<!-- wp:buttons -->\n<div class="wp-block-buttons">'
            f'<!-- wp:button {{"className":"{cls}"}} -->\n<div class="wp-block-button {cls}">'
            f'<a class="wp-block-button__link wp-element-button" href="{href}">{text}</a></div>\n'
            '<!-- /wp:button --></div>\n<!-- /wp:buttons -->')

def convert(el):
    """One child element of a content block -> block markup."""
    cls = el.get('class') or []
    if el.name == 'h2':
        return h(2, inner(el))
    if el.name == 'h3':
        return h(3, inner(el))
    if el.name == 'p':
        if 'todo' in cls:
            raise SystemExit('placeholder paragraph found - page not ready')
        return p(inner(el), 'sg-lead' if 'answer' in cls else None)
    if el.name == 'ul':
        return ul([inner(li) for li in el.find_all('li', recursive=False)], 'sg-check')
    if 'step-flow' in cls:
        steps = [group(p(f'<strong>{st.select_one("b").get_text()}</strong>', 'sg-step-title') + '\n'
                       + p(inner(st.select_one('p'))), 'sg-step') for st in el.select('.step')]
        return group('\n'.join(steps), 'sg-steps')
    if 'el-grid' in cls:
        cards = []
        for c in el.select('.el-card'):
            ic = c.select_one('.ic')
            title = (ic.get_text() + ' ' if ic else '') + f'<strong>{inner(c.select_one("b"))}</strong>'
            body = p(title, 'sg-card-title')
            if c.select_one('p'):
                body += '\n' + p(inner(c.select_one('p')))
            cards.append(group(body, 'sg-card'))
        return group('\n'.join(cards), 'sg-cards')
    if 'price-grid' in cls:
        cards = []
        for c in el.select('.price-card'):
            body = (p(f'<strong>{inner(c.select_one(".ttl"))}</strong>', 'sg-card-title') + '\n'
                    + p(inner(c.select_one('.amt')), 'sg-price') + '\n' + p(inner(c.select_one('p'))))
            cards.append(group(body, 'sg-card'))
        return group('\n'.join(cards), 'sg-cards')
    if 'faq' in cls:
        q = el.select_one('.q').get_text()
        a = inner(el.select_one('.a'))
        return (f'<!-- wp:details {{"className":"sg-faq"}} -->\n<details class="wp-block-details sg-faq"><summary>{q}</summary>'
                f'{p(a)}</details>\n<!-- /wp:details -->')
    if el.name == 'div' and not cls and el.select('.stat-badge'):
        badges = ' '.join(f'<span class="sg-badge"><strong>{b.b.get_text()}</strong>{"".join(str(x) for x in b.contents[1:])}</span>'
                          for b in el.select('.stat-badge'))
        return p(badges, 'sg-badges')
    raise SystemExit(f'unhandled element {el.name} {cls}: {str(el)[:120]}')

out = []

# ---- Hero ----
hero = soup.select_one('section.hero')
hero_parts = [h(1, inner(hero.select_one('h1')), 'sg-h1')]
hero_parts += [p(inner(s), 'sg-hero-line') for s in hero.select('.hero-sub span')]
cta = hero.select_one('.cta-btn')
if cta:
    hero_parts.append(button(cta.get_text(), cta['href']))
out.append(group('\n'.join(hero_parts), 'sg-hero alignfull', tag='section'))

# ---- Content blocks ----
sections = []
for blk in soup.select('main .block'):
    if blk.get('data-fb') in SKIP_BLOCKS:
        continue
    parts = [convert(el) for el in blk.children if not isinstance(el, NavigableString)]
    cls = 'sg-sec sg-note' if blk.get('style') else 'sg-sec'
    sections.append(group('\n'.join(parts), cls, tag='section'))
out.append(group('\n'.join(sections), 'sg-wrap'))

# ---- Closing CTA ----
c = soup.select_one('div.cta')
if c:
    lines = [s.strip() for s in c.get_text('\n').split('\n') if s.strip()]
    a = c.select_one('a')
    out.append(group('\n'.join([h(2, lines[0]), p(' '.join(lines[1:-1])), button(a.get_text(), a['href'], 'sg-btn sg-btn-light')]),
                     'sg-cta alignfull', tag='section'))

# ---- Schema from the Technik block + FAQPage from the visible FAQ ----
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
if schemas:
    out.append('<!-- wp:html -->\n' + '\n'.join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
                                                for s in schemas) + '\n<!-- /wp:html -->')

css = open(__file__.replace('build_page.py', 'page.css')).read().replace('%IMG%', IMG) if IMG else \
      open(__file__.replace('build_page.py', 'page.css')).read().replace(
          'url(%IMG%) center 30%/cover no-repeat', 'linear-gradient(135deg,#10595b,#0b3a3b)')
page = '<!-- wp:html -->\n<style>' + css + '</style>\n<!-- /wp:html -->\n\n' + group('\n\n'.join(out), 'sg-home-page')
open(OUT, 'w').write(page)

title = re.search(r'Title[^:\n]*:\s*(.+)', tech).group(1).strip()
desc = re.search(r'Meta-Description[^:\n]*:\s*(.+)', tech).group(1).strip()
alt = re.search(r'Hero:\s*„([^“"]+)', tech)
print(json.dumps({'title': title, 'desc': desc, 'alt': alt.group(1) if alt else '',
                  'h1': soup.select_one('h1').get_text(), 'sections': len(sections), 'len': len(page)}, ensure_ascii=False))
