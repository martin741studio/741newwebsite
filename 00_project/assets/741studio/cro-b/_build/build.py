import html
B='/Users/martindrendel/741website/00_project/assets/741studio/cro-b/'
def T(s): return html.escape(s, quote=False)
STAR='<svg viewBox="0 0 24 24" fill="#e0ac0a"><path d="M12 2.5l3 6.4 7 .9-5.1 4.8 1.4 7-6.3-3.5-6.3 3.5 1.4-7-5.1-4.8 7-.9z"/></svg>'
STARS=STAR*5
STAT=[('Neue Anrufe','278','in 90 Tagen'),('Mehr Buchungen','195','in 90 Tagen'),('Mehr Anfragen','233','in 90 Tagen'),('Wachstum',None,'Kontinuierlicher Umsatzanstieg')]
def statcard(t,n,s):
    if n:
        return f'<div class="statcard"><div class="t">{T(t)}</div><div class="n" data-to="{n}">+0 %</div><div class="s">{T(s)}</div></div>'
    return f'<div class="statcard"><div class="t">{T(t)}</div><div class="s" style="font-size:15px;font-weight:700;margin-top:6px;color:var(--ink)">{T(s)}</div></div>'
STATCARDS=''.join(statcard(*x) for x in STAT)
BADGES=''.join(f'<span class="badge">{T(x)}</span>' for x in ['Google Partner','WordPress Experten'])
LOGOS_F=['karin_lorenz.svg','marina_development.svg','marugame-udon-logo.png','tacheles_logo.svg','thelawncanggu1.png','avli_moderngreek.png','talkinfive.png','single_fin_bali.png']
LOGOS=''.join(f'<img src="assets/{f}" alt="Partner-Logo" loading="lazy">' for f in LOGOS_F)
SERV=[('01','Webentwicklung','Conversion-orientierte Websites, die Vertrauen schaffen und verkaufen.'),
      ('02','Design','Marke und Interface aus einem Guss.'),
      ('03','SEO','Top Rankings in Google Suche und Google Maps.'),
      ('04','Bezahlte Werbung','Kampagnen, die sich rechnen.'),
      ('05','KI-Automatisierungen','Workflows, die Zeit sparen.'),
      ('06','Conversion-Optimierung','Mehr Anfragen aus denselben Besuchern.'),
      ('07','Branding','Eine Marke, die im Kopf bleibt.'),
      ('08','Strategie','Wir analysieren Ihre Ziele, Zielgruppe und den Markt.')]
def servrow(ix,t,s):
    return f'<div class="serv-row"><span class="ix">{ix}</span><h4>{T(t)}</h4><i class="ln"></i><div class="sub">{T(s)} <span class="fehlt" style="color:var(--lemon);border-color:var(--lemon)">Entwurf</span></div></div>'
SERVICES=''.join(servrow(*x) for x in SERV)
page=open(B+'_build/template.html',encoding='utf8').read()
rep={'STARS':STARS,'STATCARDS':STATCARDS,'BADGES':BADGES,'LOGOS':LOGOS,'SERVICES':SERVICES}
for k,v in rep.items(): page=page.replace('{{'+k+'}}',v)
assert '{{' not in page, __import__('re').findall(r'\{\{\w+\}\}',page)
open(B+'07-prototype/index.html','w',encoding='utf8').write(page)
print('built',len(page))
