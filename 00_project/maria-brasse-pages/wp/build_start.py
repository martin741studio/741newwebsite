"""Convert the approved Startseite text (maria-text-startseite.html) into Gutenberg core blocks.
Text is taken 1:1 from the source file; only the markup changes."""
import json, re
from bs4 import BeautifulSoup, NavigableString

SRC = '/private/tmp/claude-501/-Users-martindrendel-741website/d3651008-1f1c-4cc5-a2f7-2c294c09568f/scratchpad/start-clean.html'
OUT = '/private/tmp/claude-501/-Users-martindrendel-741website/d3651008-1f1c-4cc5-a2f7-2c294c09568f/scratchpad/start-blocks.html'
IMG = 'https://shuiguru.de/wp-content/uploads/2026/09/maria-brasse-feng-shui-beraterin-berlin.jpg'

soup = BeautifulSoup(open(SRC).read(), 'html.parser')

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

out = []

# ---- Hero (text 1:1 from source hero) ----
hero = soup.select_one('section.hero')
h1 = hero.select_one('h1')
spans = hero.select('.hero-sub span')
cta = hero.select_one('.cta-btn')
out.append(group('\n'.join([
    h(1, inner(h1), 'sg-h1'),
    p(inner(spans[0]), 'sg-hero-line'),
    p(inner(spans[1]), 'sg-hero-line'),
    button(cta.get_text(), cta['href']),
]), 'sg-hero alignfull', tag='section'))

# ---- Content blocks ----
sections = []
for blk in soup.select('main .block'):
    parts = []
    for el in blk.children:
        if isinstance(el, NavigableString):
            continue
        cls = el.get('class') or []
        if el.name == 'h2':
            parts.append(h(2, inner(el)))
        elif el.name == 'h3':
            parts.append(h(3, inner(el)))
        elif el.name == 'p':
            parts.append(p(inner(el), 'sg-lead' if 'answer' in cls else None))
        elif el.name == 'ul':
            parts.append(ul([inner(li) for li in el.find_all('li', recursive=False)], 'sg-check'))
        elif 'step-flow' in cls:
            steps = []
            for st in el.select('.step'):
                steps.append(group(p(f'<strong>{st.select_one("b").get_text()}</strong>', 'sg-step-title') + '\n'
                                   + p(inner(st.select_one('p'))), 'sg-step'))
            parts.append(group('\n'.join(steps), 'sg-steps'))
        elif 'faq' in cls:
            q = el.select_one('.q').get_text()
            a = inner(el.select_one('.a'))
            parts.append(f'<!-- wp:details {{"className":"sg-faq"}} -->\n<details class="wp-block-details sg-faq"><summary>{q}</summary>'
                         f'{p(a)}</details>\n<!-- /wp:details -->')
        else:
            raise SystemExit(f'unhandled element {el.name} {cls}')
    sections.append(group('\n'.join(parts), 'sg-sec', tag='section'))
out.append(group('\n'.join(sections), 'sg-wrap'))

# ---- Closing CTA (text 1:1) ----
c = soup.select_one('div.cta')
lines = [s.strip() for s in c.get_text('\n').split('\n') if s.strip()]
# lines: ['Bereit für den ersten Schritt?', 'Lassen Sie uns ...', 'Käffchen vereinbaren']
a = c.select_one('a')
out.append(group('\n'.join([
    h(2, lines[0]),
    p(lines[1]),
    button(a.get_text(), a['href'], 'sg-btn sg-btn-light'),
]), 'sg-cta alignfull', tag='section'))

# ---- Map + schema (from the source "Technik" block) ----
tech = soup.select_one('details.tech')
metas = tech.select('.meta')
schema_lb = re.match(r'\s*(\{.*\})', metas[1].get_text(), re.S).group(1)
json.loads(schema_lb)  # must be valid JSON
faq_schema = {
    '@context': 'https://schema.org', '@type': 'FAQPage',
    'mainEntity': [{'@type': 'Question', 'name': f.select_one('.q').get_text(),
                    'acceptedAnswer': {'@type': 'Answer', 'text': f.select_one('.a').get_text()}}
                   for f in soup.select('.faq')]}
map_iframe = ('<iframe title="ShuiGuru auf Google Maps" src="https://www.google.com/maps?q=ShuiGuru+Feng+Shui+Beratung,+Warthestra%C3%9Fe+29,+12051+Berlin&amp;output=embed" '
              'width="100%" height="360" style="border:0" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>')
out.append('<!-- wp:html -->\n<div class="sg-map">' + map_iframe + '</div>\n'
           f'<script type="application/ld+json">{schema_lb}</script>\n'
           f'<script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False)}</script>\n<!-- /wp:html -->')

# ---- Scoped styles (CI: accent #10595B, Open Sans from theme, square buttons) ----
css = f"""<style>
.sg-home-page .sg-hero{{min-height:560px;display:flex;flex-direction:column;justify-content:flex-end;padding:120px 8% 70px;
 background:linear-gradient(180deg,rgba(11,58,59,.25),rgba(11,58,59,.82)),url({IMG}) center 30%/cover no-repeat;color:#fff;margin-top:0}}
.sg-home-page .sg-hero .sg-h1{{color:#fff;font-size:clamp(28px,4vw,46px);line-height:1.2;max-width:900px;margin:0 0 18px}}
.sg-home-page .sg-hero .sg-h1 em{{font-style:normal;opacity:.9}}
.sg-home-page .sg-hero-line{{margin:0 0 6px;font-size:17px;color:#fff}}
.sg-home-page .sg-hero .wp-block-buttons{{margin-top:18px}}
.sg-home-page .sg-btn .wp-block-button__link{{background:#10595B;color:#fff;border-radius:0;padding:12px 26px;font-weight:600}}
.sg-home-page .sg-btn .wp-block-button__link:hover{{background:#e87010;color:#fff}}
.sg-home-page .sg-btn-light .wp-block-button__link{{background:#fff;color:#10595B}}
.sg-home-page .sg-wrap{{max-width:900px;margin:0 auto;padding:40px 20px 10px}}
.sg-home-page .sg-sec{{margin:0 0 42px}}
.sg-home-page .sg-sec h2{{color:#10595B;font-size:clamp(24px,3vw,32px);margin:0 0 14px}}
.sg-home-page .sg-sec h3{{font-size:21px;margin:26px 0 8px}}
.sg-home-page .sg-lead{{font-size:19px;line-height:1.7;border-left:4px solid #10595B;padding-left:18px}}
.sg-home-page ul.sg-check{{list-style:none;margin:10px 0 0;padding:0}}
.sg-home-page ul.sg-check li{{position:relative;padding:0 0 10px 30px}}
.sg-home-page ul.sg-check li:before{{content:"✓";position:absolute;left:0;top:0;color:#10595B;font-weight:700}}
.sg-home-page .sg-steps{{counter-reset:sgstep;display:grid;gap:14px;margin:10px 0 16px}}
.sg-home-page .sg-step{{counter-increment:sgstep;position:relative;padding:14px 16px 12px 64px;background:#f3f7f7;border-left:4px solid #10595B}}
.sg-home-page .sg-step:before{{content:counter(sgstep);position:absolute;left:16px;top:14px;width:34px;height:34px;border-radius:50%;background:#10595B;color:#fff;
 display:flex;align-items:center;justify-content:center;font-weight:700}}
.sg-home-page .sg-step p{{margin:0 0 4px}}
.sg-home-page .sg-faq{{border-bottom:1px solid #d9e3e3;padding:12px 0}}
.sg-home-page .sg-faq summary{{cursor:pointer;font-weight:600;color:#10595B}}
.sg-home-page .sg-faq p{{margin:10px 0 0}}
.sg-home-page .sg-cta{{background:#10595B;color:#fff;text-align:center;padding:60px 20px}}
.sg-home-page .sg-cta h2{{color:#fff;margin:0 0 10px}}
.sg-home-page .sg-cta p{{max-width:640px;margin:0 auto 20px}}
.sg-home-page .sg-cta .wp-block-buttons{{justify-content:center}}
.sg-home-page .sg-map{{line-height:0}}
.sg-home-page .wp-block-group__inner-container>*{{margin-block-start:0}}
.sg-home-page .sg-wrap .wp-block-group__inner-container,.sg-home-page .sg-cta .wp-block-group__inner-container,.sg-home-page .sg-hero .wp-block-group__inner-container{{padding:0}}
.sg-home-page .sg-sec h3{{color:#222!important}}
.sg-home-page .sg-steps>.wp-block-group__inner-container{{display:grid;gap:14px}}
.sg-home-page .sg-step p{{margin:0!important}}
.sg-home-page .sg-step p.sg-step-title{{margin:4px 0 2px!important}}
.sg-home-page .sg-sec p{{margin:0 0 14px!important}}
.sg-home-page .sg-sec p.sg-lead{{margin:0!important}}
.sg-home-page .sg-sec .sg-faq p{{margin:10px 0 0!important}}
.sg-home-page .sg-lead{{font-size:19px!important;color:#222}}
.sg-home-page .sg-hero p.sg-hero-line{{margin:0 0 6px!important}}
.sg-home-page .sg-cta p{{margin:0 auto 20px!important}}
@media(max-width:768px){{.sg-home-page .sg-hero{{min-height:460px;padding:90px 20px 40px}}.sg-home-page .sg-wrap{{padding:28px 4px 0}}.sg-home-page .sg-step{{padding:12px 12px 10px 50px}}.sg-home-page .sg-step:before{{left:10px;width:30px;height:30px}}}}
</style>"""
page = '<!-- wp:html -->\n' + css + '\n<!-- /wp:html -->\n\n' + group('\n\n'.join(out), 'sg-home-page')
open(OUT, 'w').write(page)
print('ok', len(page), 'sections', len(sections))
