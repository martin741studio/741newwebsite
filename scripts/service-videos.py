#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Baut den Service-Video-Block unter das persoenliche Intro-Video ein.

Rendert nur Videos, die eine loomId haben — leere Slots erscheinen nicht.
Wird der Block schon gefunden, wird er ersetzt (idempotent).

Nutzung:
    python3 scripts/service-videos.py thomas-darda
    python3 scripts/service-videos.py --alle-de
"""
import re, os, sys, glob

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
REVIEW = os.path.join(ROOT, '04_site', 'review')

MARK_START = '<!-- 741 Service-Videos START -->'
MARK_END = '<!-- 741 Service-Videos END -->'

# loomId leer lassen, solange das Video nicht existiert
VIDEOS = [
    {
        'loomId': 'affb1c0588134daa86e129c6bdb8f4f3',
        'thumb': 'thumb-01',
        'dauer': '5:42',
        'nr': '01',
        'titel': 'Local SEO: Das Fundament',
        'text': 'Wie das Raster funktioniert und was es kostet, nicht in den ersten drei '
                'Plätzen zu stehen. Warum deine Website wie ein Buch gelesen wird und du '
                'der Autor bist. Was Branchenverzeichnisse mit einem Kredit-Score zu tun '
                'haben — und warum ohne ein sauberes Google-Profil rund 90 Prozent der '
                'Anfragen verloren gehen.',
    },
    {
        'loomId': 'dedd6ad6120d44a197fc55c48f590fdb',
        'thumb': 'thumb-02',
        'dauer': '3:51',
        'nr': '02',
        'titel': 'Paid Ads &amp; Retargeting',
        'text': 'Was passiert, wenn lokal schon alles läuft. Warum die wenigsten die '
                'Menschen wiedererreichen, die bereits auf ihrer Seite waren — und '
                'warum genau das der günstigste Hebel überhaupt ist.',
    },
    {
        'loomId': 'ea7703d36c094ea7aed08c44f5da1d2d',
        'thumb': 'thumb-03',
        'dauer': '4:18',
        'nr': '03',
        'titel': 'Die Website: Wie sie konvertiert',
        'text': 'Der ganze Traffic nützt nichts, wenn die Seite ihn nicht aufnimmt. '
                'Wie du ein Bild vom Ergebnis zeichnest statt vom Weg dorthin, warum '
                'Bewertungen, Qualifikationen und echte Gesichter die stärksten Hebel '
                'sind — und warum jemand, der drei Anbieter vergleicht, bei dir '
                'aufhören soll zu suchen.',
    },
]

CSS = """
<style>
 .svc-videos{padding:72px 5%;background:#0d0d0d;color:#fff;}
 .svc-head{max-width:760px;margin:0 auto 40px;text-align:center;}
 .svc-kick{color:var(--brand--lemon);font-weight:800;text-transform:uppercase;font-size:12.8px;letter-spacing:0.1em;}
 .svc-head h2{font-size:35.2px;font-weight:800;margin-top:8px;}
 .svc-head p{color:#aaa;font-size:16px;margin-top:10px;}
 .svc-grid{display:grid;gap:28px;max-width:1080px;margin:0 auto;}
 .svc-item{background:#151515;border:1px solid #262626;border-radius:18px;overflow:hidden;
           display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);}
 .svc-media{position:relative;padding-bottom:56.25%;height:0;background:#000;}
 .svc-media iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:0;}
 .svc-poster{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;}
 .svc-play{position:absolute;inset:0;border:0;padding:0;margin:0;width:100%;height:100%;
           background:rgba(0,0,0,.28);cursor:pointer;display:flex;align-items:center;justify-content:center;
           transition:background .18s;}
 .svc-play:hover{background:rgba(0,0,0,.14);}
 .svc-play span{width:70px;height:70px;border-radius:50%;background:var(--brand--lemon);
                display:flex;align-items:center;justify-content:center;box-shadow:0 8px 26px rgba(0,0,0,.45);
                transition:transform .18s;}
 .svc-play:hover span{transform:scale(1.08);}
 .svc-play span::before{content:'';border-style:solid;border-width:13px 0 13px 21px;
                        border-color:transparent transparent transparent #111;margin-left:5px;}
 .svc-dauer{position:absolute;right:12px;bottom:12px;background:rgba(0,0,0,.78);color:#fff;
            font-size:12px;font-weight:700;padding:4px 9px;border-radius:6px;}
 .svc-body{padding:26px 28px;display:flex;flex-direction:column;justify-content:center;}
 .svc-nr{font-family:'Anton',sans-serif;font-size:13px;letter-spacing:.12em;color:var(--brand--lemon);}
 .svc-body h3{font-size:20px;font-weight:800;margin:6px 0 10px;line-height:1.25;}
 .svc-body p{color:#a8a8a8;font-size:14.5px;line-height:1.6;margin:0;}
 @media(max-width:860px){.svc-item{grid-template-columns:1fr;}.svc-videos{padding:52px 5%;}}
</style>
"""


def render():
    live = [v for v in VIDEOS if v['loomId']]
    if not live:
        return ''
    items = []
    for v in live:
        items.append(
            '   <div class="svc-item">\n'
            '    <div class="svc-media">\n'
            f'     <img class="svc-poster" src="/review-assets/service-videos/{v["thumb"]}.webp" '
            f'alt="{v["titel"]}" loading="lazy" width="800" height="450">\n'
            f'     <span class="svc-dauer">{v["dauer"]}</span>\n'
            f'     <button class="svc-play" type="button" data-loom="{v["loomId"]}" '
            f'aria-label="{v["titel"]} abspielen"><span></span></button>\n'
            '    </div>\n'
            '    <div class="svc-body">\n'
            f'     <span class="svc-nr">{v["nr"]}</span>\n'
            f'     <h3>{v["titel"]}</h3>\n'
            f'     <p>{v["text"]}</p>\n'
            '    </div>\n'
            '   </div>'
        )
    sub = ('Kurze Erklärungen zu den Themen, die in fast jeder Analyse vorkommen. '
           'Du musst sie nicht ansehen — sie liegen hier, falls du wissen willst, '
           'warum ich das so mache.')
    return (
        f'{MARK_START}\n{CSS}\n'
        '  <section class="svc-videos" id="service-videos">\n'
        '   <div class="svc-head">\n'
        '    <span class="svc-kick">Zum Hintergrund</span>\n'
        '    <h2>Wie ich arbeite</h2>\n'
        f'    <p>{sub}</p>\n'
        '   </div>\n'
        '   <div class="svc-grid">\n'
        + '\n'.join(items) +
        '\n   </div>\n'
        '  </section>\n'
        '  <script>\n'
        '  document.querySelectorAll(".svc-play").forEach(function(b){\n'
        '    b.addEventListener("click", function(){\n'
        '      var m=b.parentNode, id=b.getAttribute("data-loom");\n'
        '      var f=document.createElement("iframe");\n'
        '      f.src="https://www.loom.com/embed/"+id+"?autoplay=1";\n'
        '      f.setAttribute("allow","autoplay; fullscreen");\n'
        '      f.setAttribute("allowfullscreen","");\n'
        '      m.innerHTML=""; m.appendChild(f);\n'
        '    });\n'
        '  });\n'
        '  </script>\n'
        f'{MARK_END}'
    )


def apply(slug):
    p = os.path.join(REVIEW, slug, 'index.html')
    if not os.path.exists(p):
        return f'  !! keine Seite: {slug}'
    t = open(p, encoding='utf-8').read()
    block = render()
    if not block:
        return f'  !! kein Video definiert'

    # vorhandenen Block ersetzen
    if MARK_START in t:
        t = re.sub(re.escape(MARK_START) + r'.*?' + re.escape(MARK_END), block, t, flags=re.S)
        open(p, 'w', encoding='utf-8').write(t)
        return f'  {slug:20} aktualisiert'

    # sonst hinter der Intro-Video-Sektion einfuegen
    i = t.find('id="loom-video"')
    if i < 0:
        return f'  !! keine Intro-Video-Sektion in {slug}'
    j = t.find('</section>', i)
    if j < 0:
        return f'  !! Sektion nicht abgeschlossen in {slug}'
    j += len('</section>')
    t = t[:j] + '\n\n  ' + block + t[j:]
    open(p, 'w', encoding='utf-8').write(t)
    return f'  {slug:20} eingefuegt'


DE_SLUGS_SKIP = {'house-of-eluma', 'maria-linden', 'umair-zaman', 'tobias-kunkel',
                 'island-vet-bali', 'adda-yoga-canggu', 'bali-healing'}


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    if args[0] == '--alle-de':
        slugs = []
        for p in sorted(glob.glob(os.path.join(REVIEW, '*', 'index.html'))):
            s = os.path.basename(os.path.dirname(p))
            if s in DE_SLUGS_SKIP:
                continue
            t = open(p, encoding='utf-8').read(4000)
            if 'lang="de"' in t or 'lang="de-DE"' in t:
                slugs.append(s)
    else:
        slugs = args
    for s in slugs:
        print(apply(s))


if __name__ == '__main__':
    main()
