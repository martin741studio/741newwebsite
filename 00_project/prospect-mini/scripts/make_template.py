#!/usr/bin/env python3
"""One-time: turn the reference page 04_site/review/anja-stuerzl-v2/index.html into prospect-mini/template.html.

Every prospect-specific section becomes a slot <!--SLOT:name-->. Section CSS moves into <head>, so the
renderers in build_page.py only write HTML. Run again only when the reference page changes.
"""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SRC = os.path.join(ROOT, '04_site', 'review', 'anja-stuerzl-v2', 'index.html')
DST = os.path.join(ROOT, '00_project', 'prospect-mini', 'template.html')
s = open(SRC, encoding='utf-8').read()

# 1. move section CSS (grid, system, calculator) into <head>
moved = []
for start, end in [('<!-- 741 Maps-Scan Beweis START -->', '<!-- 741 Maps-Scan Beweis END -->'),
                   ('<!-- 741 System-Vorschau START', '<!-- 741 System-Vorschau END -->'),
                   ('<!-- 741 Wachstums-Rechner (Karte + Google-Anzeigen) START -->', '<!-- 741 Wachstums-Rechner (Karte + Google-Anzeigen) END -->')]:
    a = s.index(start); b = s.index(end, a)
    block = s[a:b]
    for m in re.finditer(r'<style>.*?</style>', block, re.S):
        moved.append(m.group(0))
s = s.replace('</head>', '\n'.join(moved) + '\n</head>', 1)


def slot(s, start, end, name, keep_end=True):
    a = s.index(start)
    b = s.index(end, a)
    if not keep_end:
        b += len(end)
    return s[:a] + f'<!--SLOT:{name}-->\n' + (s[b:] if keep_end else s[b:])


s = slot(s, '<section class="section-hero-audit">', '<!-- Personal Message Section -->', 'hero')
s = slot(s, '<!-- 741 Maps-Scan Beweis START -->', '<!-- 741 Maps-Scan Beweis END -->', 'grid', keep_end=False)
s = slot(s, '<!-- 741 System-Vorschau START', '<!-- 741 System-Vorschau END -->', 'system', keep_end=False)
s = slot(s, '<!-- 741 Wachstums-Rechner (Karte + Google-Anzeigen) START -->', '<!-- 741 Wachstums-Rechner (Karte + Google-Anzeigen) END -->', 'calc', keep_end=False)
s = slot(s, '<!-- Detailed Audit Breakdown Section (Klavier) -->', '<!-- Quick Wins Section -->', 'check')
s = slot(s, '<!-- Quick Wins Section -->', '<!-- Action Roadmap Section -->', 'quickwins')
s = slot(s, '<!-- Action Roadmap Section -->', '<!-- Client Proof (individualisiert', 'roadmap')
s = slot(s, '<!-- Client Proof (individualisiert', '<!-- Final CTA Section -->', 'proof')
s = slot(s, '<!-- Final CTA Section -->', '<!-- Official 741.Studio Footer -->', 'final')

# 2. head meta
s = re.sub(r'<title>.*?</title>', '<title>%%TITLE%%</title>', s, count=1, flags=re.S)
s = re.sub(r'<meta content="[^"]*" name="description"/>', '<meta content="%%DESC%%" name="description"/>', s, count=1)
s = re.sub(r'<meta property="og:title" content="[^"]*"/>', '<meta property="og:title" content="%%TITLE%%"/>', s, count=1)
s = re.sub(r'<meta property="og:description" content="[^"]*"/>', '<meta property="og:description" content="%%DESC%%"/>', s, count=1)
s = re.sub(r'<meta property="og:url" content="[^"]*"/>', '<meta property="og:url" content="https://741.studio/review/%%SLUG%%/"/>\n  <meta property="og:image" content="https://741.studio/review-assets/%%SLUG%%/scan-grid.webp"/>', s, count=1)

# 2b. Martin guide (character callouts), rules: 00_project/assets/brand/martin-guide/README.md
if 'martin-guide.css' not in s:
    s = s.replace('</head>', '  <link rel="stylesheet" href="/review-assets/martin-guide/martin-guide.css">\n  <style>.mg{font-family:"Plus Jakarta Sans",system-ui,sans-serif}.mg__bubble{font-size:15px}.mg__bubble p{font-size:15px;line-height:1.5}@media(max-width:600px){.mg__bubble,.mg__bubble p{font-size:14px}}.rvw-hero-grid{grid-template-areas:"head video" "actions video";grid-template-rows:auto auto}.rvw-hero-head{grid-area:head;align-self:end}.rvw-hero-video{grid-area:video}.rvw-hero-actions{grid-area:actions;align-self:start}@media(max-width:900px){.rvw-hero-grid{grid-template-columns:1fr;grid-template-areas:"head" "video" "actions";gap:22px}.section-hero-audit{padding-top:calc(var(--rvw-hdr,100px) + 24px)!important}}.rvw-facts{padding:56px 5%;background:#fff}.rvw-facts h2{text-align:center;font-size:28px;font-weight:800;margin:0 0 24px}.sys-shot{cursor:zoom-in}.sys-zoom-hint{display:block;font-size:12.5px;color:#888;margin-top:8px}.rvw-lb{position:fixed;inset:0;background:rgba(15,15,15,.88);display:none;align-items:center;justify-content:center;z-index:99999;padding:20px;cursor:zoom-out}.rvw-lb.on{display:flex}.rvw-lb img{max-width:100%;max-height:100%;border-radius:10px;box-shadow:0 20px 60px rgba(0,0,0,.5)}.rvw-lb b{position:absolute;top:14px;right:20px;color:#fff;font-size:30px;font-weight:400;line-height:1}.cs-sec.cs-top-proof{padding:52px 5% 56px}.cs-sec.cs-top-proof .cs-head{margin-bottom:22px}.cs-sec.cs-top-proof .cs-head h2{font-size:30px}.cs-teaser{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.cs-tz{background:#fff;border:1px solid #eceadf;border-radius:14px;padding:12px 14px;display:flex;gap:10px;align-items:center}.cs-tz img{width:40px;height:40px;border-radius:50%;object-fit:cover;flex-shrink:0}.cs-tz b{display:block;font-size:14px;line-height:1.25}.cs-tz small{display:block;color:#777;font-size:12px}.cs-tz em{display:block;font-style:normal;color:#136c2e;font-weight:800;font-size:14px;margin-top:2px}.cs-fold{max-width:1100px;margin:18px auto 0}.cs-fold>summary{list-style:none;cursor:pointer;display:flex;justify-content:center}.cs-fold>summary::-webkit-details-marker{display:none}.cs-fold>summary span{display:inline-flex;align-items:center;gap:10px;background:#252525;color:#fff;font-weight:700;font-size:15px;border-radius:999px;padding:13px 24px}.cs-fold>summary span i{font-style:normal;transition:transform .25s}.cs-fold[open]>summary span i{transform:rotate(180deg)}.cs-fold[open]>summary span .o{display:none}.cs-fold:not([open])>summary span .c{display:none}.cs-fold .cs-grid{margin-top:22px}@media(max-width:900px){.cs-teaser{grid-template-columns:1fr 1fr}.cs-sec.cs-top-proof .cs-head h2{font-size:24px}}@media(max-width:420px){.cs-teaser{gap:8px}.cs-tz{padding:10px}.cs-tz img{display:none}.cs-tz b{font-size:13px}}</style>\n</head>', 1)
    s = s.replace('</body>', '  <script src="/review-assets/martin-guide/martin-guide.js" defer></script>\n</body>', 1)

# 3. sanity: no Stürzl text left outside slots
left = [w for w in ['Stürzl', 'STÜRZL', 'Steuerstraf', 'Kanzlei', 'Mandant', 'stuerzl'] if w in re.sub(r'<style>.*?</style>', '', s, flags=re.S)]
open(DST, 'w', encoding='utf-8').write(s)
print('template written', len(s), 'slots', s.count('<!--SLOT:'), 'leftover words:', left)
