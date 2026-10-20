import re, html
B='/Users/martindrendel/741website/00_project/assets/dumann/cro-b/'
copy=open(B+'04-copy/approved-copy.md',encoding='utf8').read()
def clean(t): return re.sub(r'\s*\[(FEHLT|ZU BESTÄTIGEN)[^\]]*\]','',t).strip()
T=lambda s: html.escape(s,quote=False)
sec8=copy[copy.index('## 8. Häufige Fragen'):copy.index('## 9. Standort')]
faq=[(q.strip(),clean(a)) for q,a in re.findall(r'\*\*F\d · ([^*]+)\*\* (.+)',sec8)]
PL='<svg class="pl" viewBox="0 0 24 24" aria-hidden="true" style="fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round"><path d="M12 5v14M5 12h14"/></svg>'
fh=''.join(f'<details class="qa rv"{" open" if k==0 else ""}><summary><span>{T(q)}</span>{PL}</summary><div class="ans"><p>{T(a)}</p></div></details>\n' for k,(q,a) in enumerate(faq))
STAR='<svg class="st" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.2l2.7 5.6 6.1.8-4.5 4.2 1.1 6-5.4-3-5.4 3 1.1-6L3.2 9.6l6.1-.8z"/></svg>'
stars='<span class="stars" aria-hidden="true">'+STAR*5+'</span>'
ARR='<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
G='<svg class="g" viewBox="0 0 24 24" aria-label="Google"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 0 1-2.2 3.32v2.77h3.57c2.08-1.92 3.27-4.74 3.27-8.1z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.1a6.6 6.6 0 0 1 0-4.2V7.06H2.18a11 11 0 0 0 0 9.88l3.66-2.84z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84C6.71 7.31 9.14 5.38 12 5.38z"/></svg>'
page=open(B+'_build/template.html',encoding='utf8').read()
CHK='<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
for k,v in {'FAQ':fh,'STARS':stars,'ARR':ARR,'G':G,'CHK':CHK}.items(): page=page.replace('{{'+k+'}}',v)
assert '{{' not in page
open(B+'07-prototype/index.html','w',encoding='utf8').write(page); print('built',len(page),len(faq),'faqs')
