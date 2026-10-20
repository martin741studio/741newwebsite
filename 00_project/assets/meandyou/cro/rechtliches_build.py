"""Shared builder for the three legal pages (Impressum, Datenschutz, AGB), 2026-10-19.
Design system = homepage prototype (07-prototype/build.py). Text = rechtliches_quelltext.py, copied
verbatim from the live pages; the only wording change is the Impressum's Geschäftsführer name (Martin's go).
These are statutory pages, not marketing copy, so they skip the content-writing gates and the CRO
diagnosis/mockup steps on purpose: nothing here is written or optimised, only reproduced.
Called by cro/impressum/07-prototype/build.py, cro/datenschutz/07-prototype/build.py, cro/agb/07-prototype/build.py.
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


home = load('home_build', os.path.join(HERE, '07-prototype', 'build.py'))
src = load('rechtliches_quelltext', os.path.join(HERE, 'rechtliches_quelltext.py'))
e = home.e

LEGAL_CSS = """
.legal-hero{padding:clamp(150px,20vh,196px) 0 56px}
.legal-hero h1{font:400 clamp(32px,3.6vw,48px)/1.16 var(--serif);margin:0}
.legal{padding:0 0 clamp(72px,10vh,120px)}
.legal .wrap{max-width:820px}
.legal h2{font-size:26px;margin:48px 0 14px}
.legal h2:first-child{margin-top:0}
.legal h3{font-size:19px;margin:28px 0 10px}
.legal p{margin:0 0 16px;color:var(--char);max-width:none}
.legal ul{margin:0 0 16px;padding-left:22px;color:var(--char)}
.legal li{margin:0 0 6px}
.legal .stand{margin-top:48px;padding-top:20px;border-top:1px solid var(--line);color:var(--muted);font-size:15px}
"""


def body_html(doc):
    out = []
    for kind, val in doc['blocks']:
        if kind == 'p':
            out.append(f'<p>{val}</p>')
        elif kind == 'h2':
            out.append(f'<h2>{val}</h2>')
        elif kind == 'h3':
            out.append(f'<h3>{val}</h3>')
        elif kind == 'ul':
            out.append('<ul>' + ''.join(f'<li>{e(x)}</li>' for x in val) + '</ul>')
    return ''.join(out)


def footer():
    return f'''<footer class="foot">
 <div class="wrap foot__in">
  <div><img src="assets/logo-light.png" alt="Michael Ehlers &amp; You Communication" width="1794" height="647"><p class="addr">Institut Michael Ehlers GmbH<br>Landsknechtstraße 50<br>96103 Hallstadt</p></div>
  <div><h4>Seminare</h4><a href="https://clients.741.studio/meandyou/v2/seminare.html">Seminare</a><a href="https://clients.741.studio/meandyou/v2/termin.html">Gespräch buchen</a></div>
  <div><h4>Michael</h4><a href="https://clients.741.studio/meandyou/v2/michael.html">Über Michael</a><a href="https://clients.741.studio/meandyou/v2/rhetorik.html">Was ist Rhetorik</a><a href="https://clients.741.studio/meandyou/v2/faq.html">FAQ</a></div>
  <div><h4>Rechtliches</h4><a href="https://www.meandyou.de/impressum">Impressum</a><a href="https://www.meandyou.de/datenschutz">Datenschutz</a><a href="https://www.meandyou.de/agb">AGB</a></div>
  <div><h4>Kontakt</h4><a href="tel:+4915888367664">+49 15888367664</a><a href="mailto:management@meandyou.de">management@meandyou.de</a><a href="https://www.instagram.com/michael_ehlers_rhetorik/">Instagram</a><a href="https://de.linkedin.com/in/rhetoriktrainer">LinkedIn</a></div>
 </div>
</footer>'''


def header():
    return f'''<header class="hdr"><div class="hdr__in">
 <a class="hdr__logo" href="https://clients.741.studio/meandyou/v2/index.html"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication, Startseite" width="1794" height="647"></a>
 <nav aria-label="Hauptnavigation"><a href="https://clients.741.studio/meandyou/v2/seminare.html">Seminare</a><a href="https://clients.741.studio/meandyou/v2/michael.html">Michael</a><a href="https://clients.741.studio/meandyou/v2/rhetorik.html">Was ist Rhetorik</a><a href="https://clients.741.studio/meandyou/v2/index.html#stimmen">Stimmen</a><a href="https://clients.741.studio/meandyou/v2/faq.html">FAQ</a></nav>
 <a class="btn" href="https://clients.741.studio/meandyou/v2/termin.html?utm_source=rechtliches&utm_content=header">Gespräch buchen</a>
</div></header>'''


def page(doc):
    body = header() + f'''<main>
<section class="legal-hero" id="top"><div class="wrap"><p class="ov rv">Rechtliches</p><h1 class="rv">{e(doc['title'])}</h1></div></section>
<section class="legal"><div class="wrap">{body_html(doc)}<p class="stand">Stand: {e(doc['stand'])}</p></div></section>
</main>''' + footer()
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{e(doc['title'])} | me&amp;you Communication</title>
<meta name="description" content="{e(doc['title'])} von me&amp;you Communication / Michael Ehlers.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">
<style>{home.CSS}{LEGAL_CSS}</style>
</head><body>{body}<script>{home.JS}</script></body></html>'''
