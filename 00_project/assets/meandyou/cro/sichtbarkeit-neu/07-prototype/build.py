"""Build the me&you VSL page "Sichtbarkeit Neu" (desktop 1440 px) as a close functional copy of the
live https://www.meandyou.de/sichtbarkeit-neu (Framer). Design system = homepage + seminar + Michael +
Rhetorik + termin pages (imported). This is continuity for running Meta ads, not a redesign:
content, video and CTA target match the live page as closely as possible.
Live page facts (Firecrawl, 2026-10-24, maxAge 0):
- Wistia video media-id wb51mevk7b (read out of the saved live HTML /tmp/sn_sichtbarkeit-neu.html).
- The live CTA "Kostenloses persönliches Gespräch buchen" links OUT to https://www.meandyou.de/sichtbarkeit-termin,
  which is Calendly event "sichtbarkeit-neu" (calendly.com/me-you/sichtbarkeit-neu) -- exactly the page already
  built in cro/termin (-> gespraech-buchen.html). So this page does NOT embed Calendly inline itself; it links
  to the booking page, matching the live site. Use the already-approved termin page, do not re-embed the widget here.
Run: python3 build.py"""
import importlib.util, json, os
HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


tm = load('tm_build', os.path.join(HERE, '..', '..', 'termin', '07-prototype', 'build.py'))
rh = tm.rh
mic, sem, home = rh.mic, rh.sem, rh.home
e, CHECK, PLAY = home.e, home.CHECK, home.PLAY
TEL = tm.TEL
ICON = tm.ICON
BOOK = 'gespraech-buchen.html'
WISTIA_ID = 'wb51mevk7b'


def btn(cls='btn'):
    return f'<a class="{cls}" href="{BOOK}">Kostenloses persönliches Gespräch buchen</a>'


CSS = tm.CSS + r"""
/* sichtbarkeit-neu VSL page */
.vsl{padding:100px 0 72px;background:var(--paper)}
.vsl__in{max-width:900px;margin:0 auto;text-align:center;display:flex;flex-direction:column;gap:22px;align-items:center}
.vsl h1{font-size:46px;line-height:1.15}
.vsl .sub{font-size:20px;color:var(--muted);max-width:40em}
.vsl__video{width:100%;max-width:860px;margin-top:8px}
.wistia-radius-12{border-radius:16px;overflow:hidden;box-shadow:0 18px 50px rgba(42,38,34,.14)}
.wistia-radius-12 wistia-player[media-id]{display:block;width:100%}
.vsl .authority{font-size:18px;color:var(--muted);max-width:38em;margin-top:8px}
.vsl .cta-row{margin-top:6px}
.sec--umsetzung h2{text-align:center;max-width:36em;margin:0 auto}
.sec--umsetzung .body{text-align:center;max-width:34em;margin:18px auto 0}
.sec--bestandsaufnahme{background:var(--navy);color:var(--on-dark)}
.sec--bestandsaufnahme .wrap{max-width:760px;text-align:center;display:flex;flex-direction:column;gap:18px;align-items:center}
.sec--bestandsaufnahme h2{color:var(--on-dark)}
.sec--bestandsaufnahme p{color:rgba(242,237,228,.86);font-size:18.5px}
"""


def header():
    return f'''<header class="hdr hdr--min"><div class="hdr__in">
 <a class="hdr__logo" href="#top"><img src="assets/logo-dark.png" alt="Michael Ehlers &amp; You Communication" width="1794" height="647"></a>
 <a class="tel" href="{TEL}">{ICON['phone']}+49 15888367664</a>
</div></header>'''


def s_hero():
    return f'''
<section class="vsl" id="top">
 <div class="wrap vsl__in">
  <h1 class="rv">Nicht mehr überhört – sondern unübersehbar.</h1>
  <p class="sub rv">So gewinnst du Aufmerksamkeit und Vertrauen – ohne laut zu werden oder dich zu verbiegen.</p>
  <div class="cta-row rv">{btn()}</div>
  <div class="vsl__video rv">
   <div class="wistia-radius-12"><wistia-player media-id="{WISTIA_ID}" aspect="1.7777777777777777"></wistia-player></div>
  </div>
  <p class="authority rv">In meine Arbeit fließen über 30 Jahre Erfahrung mit Executives, Unternehmern, Politikern und Profisportlern.</p>
  <p class="body rv">Im persönlichen Vorgespräch klären wir, ob du für eine gemeinsame Zusammenarbeit geeignet bist – und ob es tatsächlich der richtige Schritt für deine Situation ist.</p>
  <div class="cta-row rv">{btn()}</div>
 </div>
</section>'''


def s_umsetzung():
    return f'''
<section class="sec sec--cream sec--umsetzung" id="umsetzung">
 <div class="wrap">
  <h2 class="rv">Die Theorie hast du geschafft – aber wie schaffst du die Umsetzung?</h2>
  <p class="body rv">In den meisten Fällen wird erst im persönlichen Austausch deutlich, wo du tatsächlich Wirkung verlierst oder an den Menschen vorbeiredest.</p>
  <div class="ctabar rv">{btn()}</div>
 </div>
</section>'''


def s_bestandsaufnahme():
    return f'''
<section class="sec sec--bestandsaufnahme" id="bestandsaufnahme">
 <div class="wrap">
  <h2 class="rv">Am Anfang steht ein kurzes Gespräch – eine ehrliche Bestandsaufnahme.</h2>
  <p class="rv">Wir klären, ob und wie eine Zusammenarbeit wirklich etwas für dich verändert: bei der Wirkung auf andere, beim Durchsetzen von Ideen oder dabei, wie du in relevanten Situationen wahrgenommen wirst. Je länger diese Fragen offen bleiben, desto mehr kosten sie – an Energie, Chancen und Klarheit.</p>
  <div class="ctabar rv">{btn('btn btn--light')}</div>
 </div>
</section>'''


def footer():
    return f'''<footer class="foot foot--min">
 <div class="wrap foot__in">
  <div><img src="assets/logo-light.png" alt="Michael Ehlers &amp; You Communication" width="1794" height="647"></div>
  <nav class="legal" aria-label="Rechtliches"><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a><a href="agb.html">AGB</a></nav>
  <div class="kon"><h4>Kontakt</h4><a href="{TEL}">+49 15888367664</a><a href="mailto:management@meandyou.de">management@meandyou.de</a><a href="https://www.instagram.com/michael_ehlers_rhetorik/">Instagram</a><a href="https://de.linkedin.com/in/rhetoriktrainer">LinkedIn</a></div>
 </div>
</footer>'''


def schema():
    ORG = 'https://www.meandyou.de/#organization'
    g = [{"@type": "WebPage", "@id": "https://www.meandyou.de/sichtbarkeit-neu#webpage", "url": "https://www.meandyou.de/sichtbarkeit-neu",
          "name": "Sichtbarkeit Neu – VSL · me&you Michael Ehlers", "inLanguage": "de", "publisher": {"@id": ORG}},
         {"@type": "EducationalOrganization", "@id": ORG, "name": "Me&You Communication FZCO", "alternateName": "me&you Communication",
          "url": "https://www.meandyou.de/", "email": "management@meandyou.de"}]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False)


JS_EXTRA = r"""
document.querySelectorAll('[data-jump]').forEach(function(a){a.addEventListener('click',function(ev){ev.preventDefault();var k=document.getElementById(a.getAttribute('href').slice(1));if(k){scrollTo({top:k.getBoundingClientRect().top+scrollY-96,behavior:'smooth'});}});});
"""


def page():
    body = header() + '<main>' + s_hero() + s_umsetzung() + s_bestandsaufnahme() + '</main>' + footer() + '<div class="proto">Prototyp · nicht live · gelb = [FEHLT]</div>'
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Sichtbarkeit Neu – VSL · me&amp;you Michael Ehlers</title>
<meta name="description" content="So gewinnst du Aufmerksamkeit und Vertrauen, ohne laut zu werden oder dich zu verbiegen. Kostenloses persönliches Gespräch buchen.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{schema()}</script>
<script src="https://fast.wistia.com/player.js" async></script>
<script src="https://fast.wistia.com/embed/{WISTIA_ID}.js" async type="module"></script>
</head><body>{body}<script>{home.JS}</script><script>{JS_EXTRA}</script></body></html>'''


if __name__ == '__main__':
    out = page()
    open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out))
