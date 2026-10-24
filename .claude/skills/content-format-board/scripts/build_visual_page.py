#!/usr/bin/env python3
"""Build the client-facing visual board page from <visual_dir>/visual.json.

Usage: build_visual_page.py <visual_dir> [--out board.html]

Writes <visual_dir>/board.html (relative image links), copies the Martin guide
assets into <visual_dir>/mg/, and makes 900 px JPG web copies of every image it
shows into <visual_dir>/images/web/. Then run verify_board-style checks by eye:
shot the page at 1440 and 390 px before it is shown to anyone.
"""
import html, json, os, shutil, subprocess, sys

ROOT = '/Users/martindrendel/741website'
MG = os.path.join(ROOT, '00_project', 'assets', 'brand', 'martin-guide')
GUIDES = {
    'martin': {'name': 'Martin', 'alt': 'Martin von 741', 'poses': os.path.join(MG, 'poses'), 'prefix': 'martin'},
    'celine': {'name': 'Céline', 'alt': 'Céline von TALKNFIVE', 'poses': os.path.join(ROOT, '04_site', 'public', 'review-assets', 'celine-guide'), 'prefix': 'celine'},
}
GUIDE = GUIDES['martin']

CSS = """
:root{--red:#DB4A2B;--coral:#FF644E;--cream:#FFF4EF;--ink:#2b2420;--grey:#6b625d;--line:#eadfd8}
*{box-sizing:border-box}body{margin:0;font-family:Poppins,system-ui,sans-serif;color:var(--ink);background:#fff;line-height:1.5}
.wrap{max-width:1200px;margin:0 auto;padding:32px 16px}
h1{font-size:34px;line-height:1.15;margin:0 0 6px}h2{font-size:24px;margin:48px 0 8px;color:var(--red)}h3{font-size:17px;margin:0 0 6px}
.sub{color:var(--grey);font-size:14px}.tag{display:inline-block;background:var(--cream);color:var(--red);padding:3px 10px;border-radius:999px;font-size:12px;font-weight:600;margin-right:6px}
img{max-width:100%;height:auto}html,body{overflow-x:hidden}
.brand{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.4fr);gap:20px;align-items:start;background:var(--cream);border-radius:16px;padding:20px;margin-top:20px}
.brand img.grid{width:100%;border-radius:10px;border:1px solid var(--line)}.brand img.logo{height:60px;margin-bottom:10px}
.sw{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0}.sw span{display:inline-flex;align-items:center;gap:6px;font-size:12px}.sw i{width:18px;height:18px;border-radius:50%;display:inline-block;border:1px solid var(--line)}
.idea{margin-top:10px}.idea p.lead{font-size:17px;max-width:760px}
.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:14px}
.card{border:1px solid var(--line);border-radius:14px;overflow:hidden;background:#fff}
.card .frame{aspect-ratio:2/3;background:#111;overflow:hidden}.card .frame img{width:100%;height:100%;object-fit:cover;display:block}
.card .body{padding:14px}.card .why{font-size:14px;margin:6px 0 10px}
.ref{display:flex;gap:10px;align-items:flex-start;border-top:1px dashed var(--line);padding-top:10px}.ref img{width:84px;border-radius:6px;border:1px solid var(--line);flex:none}.ref p{font-size:12px;color:var(--grey);margin:0}
.base{display:flex;gap:10px;margin-top:14px;align-items:center}.base img{width:72px;border-radius:6px;border:1px solid var(--line)}.base p{font-size:12px;color:var(--grey);margin:0 0 0 6px}
.compare{display:flex;gap:14px;align-items:center;margin-top:12px}.compare img{width:120px;border-radius:8px}.compare p{font-size:13px;color:var(--grey);margin:0}
.open{background:var(--cream);border-radius:14px;padding:18px 20px;margin-top:20px}.open li{margin:4px 0}
footer{margin:48px 0 20px;font-size:12px;color:var(--grey);border-top:1px solid var(--line);padding-top:14px}
@media(max-width:800px){.brand,.cards{grid-template-columns:minmax(0,1fr)}h1{font-size:26px}.wrap{padding:20px 16px}.base,.compare{flex-wrap:wrap}}
"""


def web_copy(vdir, rel):
    src = os.path.join(vdir, rel)
    outdir = os.path.join(vdir, 'images', 'web')
    os.makedirs(outdir, exist_ok=True)
    name = os.path.splitext(rel)[0].replace('images/', '').replace('/', '-') + '.jpg'
    out = os.path.join(outdir, name)
    if not os.path.exists(out):
        subprocess.run(['sips', '-Z', '900', '-s', 'format', 'jpeg', '-s', 'formatOptions', '82', src, '--out', out],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return 'images/web/' + name


def mg(pose, text, mod=''):
    g = GUIDE
    return (f'<aside class="mg {mod}" data-reveal><img class="mg__img" src="mg/{g["prefix"]}-{pose}.webp" '
            f'alt="{g["alt"]}, {pose}" width="112"><div class="mg__bubble"><span class="mg__name">{g["name"]}</span>'
            f'<p>{html.escape(text)}</p></div></aside>')


def main(vdir, out='board.html'):
    global GUIDE
    d = json.load(open(os.path.join(vdir, 'visual.json'), encoding='utf-8'))
    GUIDE = GUIDES[d.get('guide', 'martin')]
    os.makedirs(os.path.join(vdir, 'mg'), exist_ok=True)
    for f in ('martin-guide.css', 'martin-guide.js'):
        shutil.copy(os.path.join(MG, f), os.path.join(vdir, 'mg', f))
    poses = ('hello', 'point', 'think', 'present') + (('insight',) if GUIDE['prefix'] == 'martin' else ('strategy',))
    for p in poses:
        shutil.copy(os.path.join(GUIDE['poses'], f'{GUIDE["prefix"]}-{p}.webp'), os.path.join(vdir, 'mg', f'{GUIDE["prefix"]}-{p}.webp'))
    bub = d.get('bubbles', {})
    e = html.escape
    b = d['brand']
    parts = [f'<!doctype html><html lang="{d.get("lang","en")}"><head><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             f'<title>Video content concepts: {e(d["client"])}</title>',
             '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">',
             '<link rel="stylesheet" href="mg/martin-guide.css">', f'<style>{CSS}</style></head><body><div class="wrap">',
             f'<span class="tag">Proposal</span><span class="tag">{e(d["date"])}</span>',
             f'<h1>Video content concepts for {e(d["client"])}</h1>',
             f'<p class="sub">{e(d["place"])} · what the first two formats could look like in your own visual language · a proposal for discussion, not a promise of results</p>',
             mg('hello', bub.get('hello', 'Two formats, six concept frames. Each one shows what pulls attention and why, built from your own feed.')),
             '<div class="brand"><div>', f'<img class="logo" src="{b["logo"]}" alt="{e(d["client"])} logo">',
             '<h3>Your visual language</h3>', '<div class="sw">' + ''.join(f'<span><i style="background:{c[1]}"></i>{e(c[0])} {c[1]}</span>' for c in b['colors']) + '</div>',
             f'<p class="sub">{e(b["mood"])}</p><p style="font-size:14px">{e(b["grid_note"])}</p></div>',
             f'<div><img class="grid" src="{web_copy(vdir, b["grid"])}" alt="Instagram grid today"></div></div>']
    for idea in d['ideas']:
        parts.append(f'<section class="idea"><h2>Idea {idea["n"]}: {e(idea["label"])}</h2><p class="lead">{e(idea["idea"])}</p>')
        if idea['n'] == 1:
            parts.append(mg('point', bub.get('idea1', 'Look at the second frame. It is your own red flat lay, used as a video cover. That is the one I would shoot first.')))
        else:
            parts.append(mg('strategy' if GUIDE['prefix'] == 'celine' else 'insight', bub.get('idea2', 'Five cuts, five words, one sentence. The viewer stays to finish the sentence. That is the whole trick.')))
        parts.append('<div class="cards">')
        for c in idea['concepts']:
            parts.append(f'<article class="card"><div class="frame"><img src="{web_copy(vdir, c["file"])}" alt="{e(c["title"])}"></div>'
                         f'<div class="body"><h3>{e(c["title"])}</h3><p class="why">{e(c["mechanism"])}</p>'
                         f'<div class="ref"><img src="{web_copy(vdir, c["ref"])}" alt="reference"><p><strong>Why we believe it:</strong> {e(c["proof"])}</p></div></div></article>')
        parts.append('</div>')
        parts.append('<div class="base">' + ''.join(f'<img src="{web_copy(vdir, x)}" alt="base frame">' for x in idea['base']) +
                     '<p>The plain base frames the concepts were built on. Correct, but without a concept they are just food.</p></div>')
        if idea.get('too_polished'):
            parts.append(f'<div class="compare"><img src="{web_copy(vdir, idea["too_polished"])}" alt="too polished"><p>First attempt, rejected: too polished, looks like an advert. The concepts above are made to look like a guest filmed them on a phone.</p></div>')
        parts.append('</section>')
    if d.get('open'):
        parts.append('<div class="open"><h3>What we need from you before shooting</h3>' + mg('think', bub.get('open', 'Four answers from you, then we can shoot the first two in one morning.'), 'mg--small') +
                     '<ul>' + ''.join(f'<li>{e(q)}</li>' for q in d['open']) + '</ul></div>')
    parts.append('<footer>Prepared by 741 Studio. Concept frames are illustrations of the idea, made from your real photos and logo. The real videos get shot at your venue. Reference numbers are the likes shown on the public posts on the day we looked.</footer>')
    parts.append('</div><script src="mg/martin-guide.js" defer></script></body></html>')
    p = os.path.join(vdir, out)
    open(p, 'w', encoding='utf-8').write('\n'.join(parts))
    print('wrote', p)
    # Artifact variant: no document skeleton, Martin guide inlined, side gutter per the artifact contract.
    import base64
    body = '\n'.join(parts)
    body = body.split('<body>', 1)[1].rsplit('</body>', 1)[0]
    body = body.replace('<script src="mg/martin-guide.js" defer></script>', '')
    mgcss = open(os.path.join(MG, 'martin-guide.css'), encoding='utf-8').read()
    mgjs = open(os.path.join(MG, 'martin-guide.js'), encoding='utf-8').read()
    for pose in poses:
        b64 = base64.b64encode(open(os.path.join(GUIDE['poses'], f'{GUIDE["prefix"]}-{pose}.webp'), 'rb').read()).decode()
        body = body.replace(f'src="mg/{GUIDE["prefix"]}-{pose}.webp"', f'src="data:image/webp;base64,{b64}"')
    art = (f'<title>{e(d["client"])} Video Concepts</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
           '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">\n'
           f'<style>{mgcss}\n{CSS}\n.wrap{{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px}}'
           '\n:root{color-scheme:light}body{background:#fff;color:#2b2420}</style>\n' + body + f'\n<script>{mgjs}</script>')
    pa = os.path.join(vdir, 'board-artifact.html')
    open(pa, 'w', encoding='utf-8').write(art)
    print('wrote', pa)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[3] if '--out' in sys.argv else 'board.html')
