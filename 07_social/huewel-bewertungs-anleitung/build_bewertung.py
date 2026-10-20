# -*- coding: utf-8 -*-
import base64, io, segno, os

OUT = os.path.dirname(os.path.abspath(__file__))
PLACE = "ChIJP9pcB-1Wn0cREo1vNZHFGC8"
URL = f"https://search.google.com/local/writereview?placeid={PLACE}"

# QR: segno, error h, dunkle Markenfarbe, transparent
qr = segno.make(URL, error='h')
b = io.BytesIO()
qr.save(b, kind='png', scale=12, dark='#2E4B00', light=None, border=2)
QR64 = base64.b64encode(b.getvalue()).decode()

LOGO64 = base64.b64encode(open(os.path.join(OUT, 'reviews-kit', 'huewel-logo.jpg'), 'rb').read()).decode()

BODY = """
<div class="page">
  <header class="top">
    <div class="brand"><img class="logo" src="data:image/jpeg;base64,__LOGO__" alt="Praxis Hüwel"><div class="wordmark">Gesundheitspraxis<br><span>im Nürbanum</span></div></div>
  </header>

  <div class="badge">IHRE GOOGLE-BEWERTUNG&nbsp;·&nbsp;IN 60 SEKUNDEN</div>
  <h1>Wer · Wo · Wie — so einfach geht’s 💚</h1>
  <p class="intro"><b>Wer:</b> Ich bin Martin Hüwel (Gesundheitspraxis im Nürbanum) — Ihre Erfahrung hilft anderen, den passenden Heilpraktiker zu finden, und macht mich bei Google sichtbar.</p>

  <section class="step">
    <div class="s-text">
      <div class="s-kicker">SCHRITT 1 · WO</div>
      <h2>Mein Profil öffnen</h2>
      <p>Kamera auf den <b>QR-Code unten</b> — oder bei Google <b>„Praxis Hüwel Nürnberg“</b> suchen und auf <b>„Rezension schreiben“</b> tippen.</p>
    </div>
    <div class="phone">
      <div class="p-notch"></div>
      <div class="p-search">🔍&nbsp; Praxis Hüwel Nürnberg</div>
      <div class="p-card">
        <div class="p-name">Gesundheitspraxis im Nürbanum</div>
        <div class="p-sub">Heilpraktiker · Nürnberg</div>
        <div class="p-stars">★★★★★ <span>4,9 · 9 Rezensionen</span></div>
        <div class="p-btn glow">✎&nbsp; Rezension schreiben</div>
      </div>
    </div>
  </section>

  <section class="step">
    <div class="s-text">
      <div class="s-kicker">SCHRITT 2 · WIE</div>
      <h2>Sterne + 2–3 Sätze</h2>
      <div class="wbox">
        <div class="w-title">So wird Ihr Text richtig wertvoll — die W-Fragen:</div>
        <div class="w-row"><span class="w-k">WAS</span><span>habe ich für Sie gemacht? Nennen Sie die Leistung: <b>Frequenztherapie, Homöopathie oder Gesundheitscheck.</b></span></div>
        <div class="w-row"><span class="w-k">WIE</span><span>war Ihre Erfahrung? 1–2 Sätze reichen völlig — z.&nbsp;B. wie viel Zeit ich mir genommen habe.</span></div>
        <div class="w-row"><span class="w-k">WO</span><span>war das? Am besten mit Ort — z.&nbsp;B. „in der Nürnberger Südstadt“.</span></div>
      </div>
    </div>
    <div class="phone">
      <div class="p-notch"></div>
      <div class="p-title">Gesundheitspraxis im Nürbanum bewerten</div>
      <div class="p-bigstars">★★★★★</div>
      <div class="p-textarea">Herr Hüwel hat sich beim <b>Gesundheitscheck</b> in der <b>Nürnberger Südstadt</b> richtig viel Zeit genommen und alles verständlich erklärt. Klare Empfehlung!</div>
      <div class="p-post">Posten</div>
    </div>
  </section>

  <section class="qrline">
    <img class="qr" src="data:image/png;base64,__QR__" alt="QR-Code zur Google-Bewertung">
    <div class="q-text">
      <p class="q-strong">Schritt 3 · Fertig: auf „Posten“ tippen.</p>
      <p class="q-strong">Kamera drauf → Bewertungsfenster öffnet sich direkt.</p>
      <p class="q-thanks">Danke Ihnen! — Martin Hüwel</p>
      __LINKLINE__
    </div>
  </section>
  __FOOTER__
</div>
"""

CSS = """
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Roboto:wght@400;500;700&display=swap">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--g:#426C00;--gd:#2E4B00;--gold:#E2A400;--sand:#FBF7EC;--line:#E8E2D2;--ink:#2b2b2b;--soft:#5f5f5f}
body{font-family:'Roboto',Arial,sans-serif;color:var(--ink);background:#fff}
.page{display:flex;flex-direction:column;padding:52px 56px 44px;background:#fff}
.top{display:flex;align-items:center;justify-content:space-between;margin-bottom:22px}
.brand{display:flex;align-items:center;gap:16px}
.logo{width:84px;height:84px;border-radius:50%;object-fit:cover}
.wordmark{font-family:'Montserrat',sans-serif;font-weight:800;font-size:26px;line-height:1.05;color:var(--g)}
.wordmark span{font-weight:600;font-size:20px;color:var(--ink)}
.badge{align-self:flex-start;background:var(--g);color:#fff;font-family:'Montserrat',sans-serif;font-weight:700;font-size:15px;letter-spacing:2px;padding:9px 18px;border-radius:24px;margin-bottom:16px}
h1{font-family:'Montserrat',sans-serif;font-weight:800;font-size:41px;color:var(--gd);margin-bottom:10px}
.intro{font-size:19.5px;color:var(--soft);line-height:1.5;margin-bottom:26px}
.intro b{color:var(--ink)}
.step{display:grid;grid-template-columns:1fr 300px;gap:26px;align-items:center;border:1px solid var(--line);border-radius:18px;padding:24px 26px;margin-bottom:22px;background:#fff}
.s-kicker{font-family:'Montserrat',sans-serif;font-weight:700;font-size:13.5px;letter-spacing:2px;color:var(--gold)}
.step h2{font-family:'Montserrat',sans-serif;font-weight:800;font-size:27px;color:var(--g);margin:5px 0 9px}
.s-text p{font-size:18px;line-height:1.5;color:var(--soft)}
.s-text b{color:var(--ink)}
.phone{background:#fff;border:3.5px solid var(--gd);border-radius:26px;padding:16px 14px 18px;box-shadow:0 10px 26px rgba(46,75,0,.14)}
.p-notch{width:64px;height:6px;border-radius:4px;background:var(--gd);margin:0 auto 12px}
.p-search{border:1.5px solid #d7d2c4;border-radius:22px;padding:8px 13px;font-size:14px;color:var(--ink);margin-bottom:11px;background:#fff}
.p-card{border:1.5px solid var(--line);border-radius:12px;padding:12px}
.p-name{font-weight:700;font-size:14.5px}
.p-sub{font-size:12.5px;color:var(--soft);margin:2px 0 4px}
.p-stars{font-size:13px;color:var(--gold);margin-bottom:9px}
.p-stars span{color:var(--soft);font-size:11.5px}
.p-btn{border:2px solid var(--g);color:var(--g);font-weight:700;font-size:13.5px;text-align:center;border-radius:20px;padding:7px}
.glow{box-shadow:0 0 0 5px rgba(226,164,0,.35)}
.p-title{font-weight:700;font-size:14px;text-align:center;margin-bottom:8px}
.p-bigstars{font-size:30px;letter-spacing:5px;color:var(--gold);text-align:center;margin-bottom:9px}
.p-textarea{border:1.5px solid var(--line);border-radius:10px;padding:10px 12px;font-size:12.8px;line-height:1.45;color:var(--ink);background:#fff}
.p-post{margin-top:11px;background:var(--g);color:#fff;font-weight:700;font-size:13.5px;text-align:center;border-radius:20px;padding:8px}
.wbox{background:var(--sand);border-left:4px solid var(--gold);border-radius:10px;padding:14px 17px}
.w-title{font-weight:700;font-size:16.5px;margin-bottom:9px;color:var(--gd)}
.w-row{display:grid;grid-template-columns:52px 1fr;gap:9px;font-size:16px;line-height:1.42;margin-bottom:7px;color:var(--soft)}
.w-k{font-family:'Montserrat',sans-serif;font-weight:800;color:var(--gold)}
.w-row b{color:var(--g)}
.qrline{margin-top:auto;display:flex;align-items:center;gap:28px;border:1.5px solid var(--gold);background:var(--sand);border-radius:18px;padding:22px 26px}
.qr{width:190px;height:190px}
.q-strong{font-family:'Montserrat',sans-serif;font-weight:800;font-size:21px;color:var(--gd);line-height:1.45}
.q-thanks{font-size:19px;font-style:italic;color:var(--g);margin-top:7px}
.q-link{font-size:11px;color:#9a937f;margin-top:9px;word-break:break-all}
.footer{margin-top:18px;text-align:center;font-size:12.5px;color:#9a937f}
</style>
"""

def build(kind):
    body = BODY.replace('__LOGO__', LOGO64).replace('__QR__', QR64)
    if kind == 'a4':
        body = body.replace('__LINKLINE__', f'<p class="q-link">{URL}</p>')
        body = body.replace('__FOOTER__', '<div class="footer">Gesundheitspraxis im Nürbanum – Martin Hüwel · Heilpraktiker · Nürnberg &amp; Umgebung&nbsp;|&nbsp;www.praxis-huewel.de</div>')
        extra = '<style>@page{size:A4;margin:0}html{zoom:0.62}body{width:1080px}.page{min-height:1350px}</style>'
    else:
        body = body.replace('__LINKLINE__', '').replace('__FOOTER__', '')
        extra = '<style>body{width:1080px;height:1350px;overflow:hidden}.page{width:1080px;height:1350px}</style>'
    html = f'<!doctype html><html lang="de"><head><meta charset="utf-8">{CSS}{extra}</head><body>{body}</body></html>'
    fn = os.path.join(OUT, f'huewel-bewertung-{kind}.html')
    open(fn, 'w', encoding='utf-8').write(html)
    print('written', fn)

build('whatsapp')
build('a4')
