import re, html
B='/Users/martindrendel/741website/00_project/assets/stuerzl/cro/'
copy=open(B+'04-copy/approved-copy.md',encoding='utf8').read()
def sec(n):
    m=re.search(r'\n## %s\. .*?(?=\n## |\n---)'%n,copy,flags=re.S); return m.group(0)
def clean(t): return re.sub(r'\s*\[(FEHLT|ZU BESTÄTIGEN)[^\]]*\]','',t).strip()
def fld(n,label):
    m=re.search(r'\*\*%s:\*\*\s*(.+)'%re.escape(label),sec(n)); return clean(m.group(1))
e=html.escape
def T(s): return e(s,quote=False)
sec1=sec(1)
SUB=fld(1,'Sub-Headline')
faq=re.findall(r'\*\*F\d · ([^*]+)\*\* (.+)',sec(9))
faq=[(q.strip(),clean(a)) for q,a in faq]
txt6=fld(6,'Text')
cards4=re.findall(r'\*\*Karte (\d\d) · ([^:*]+):\*\* (.+)',sec(4))
steps=re.findall(r'\*\*Schritt (\d) · ([^:*]+):\*\* (.+)',sec(5))
steps=[(n,t,clean(d)) for n,t,d in steps]
def listblock(n,start,stop):
    s=sec(n); i=s.index(start); j=s.index(stop,i+len(start)) if stop else len(s)
    return [x[2:].strip() for x in s[i:j].splitlines() if x.startswith('- ')]
priv=listblock(3,'**Karte 1','**Karte 2'); unt=listblock(3,'**Karte 2','**Abschluss-Zeile')
tl=listblock(6,'**Zeitleiste:**','**Engagement')
def tlparts(x):
    a,b=x.split(' · ',1); return a,b
v1=listblock(8,'**Spalte 1','**Spalte 2'); v2=listblock(8,'**Spalte 2','**Link')
IC={
'star':'<path d="M12 3.2l2.7 5.6 6.1.8-4.5 4.2 1.1 6-5.4-3-5.4 3 1.1-6L3.2 9.6l6.1-.8z"/>',
'chat':'<path d="M4 5h16v11H9l-5 4z"/>',
'award':'<circle cx="12" cy="9" r="5"/><path d="M8.5 13.5L7 21l5-2.6 5 2.6-1.5-7.5"/>',
'doc':'<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
'pin':'<path d="M12 21s7-6.2 7-11.5A7 7 0 005 9.5C5 14.800 12 21 12 21z"/><circle cx="12" cy="9.500" r="2.500"/>',
'user':'<circle cx="12" cy="8" r="4"/><path d="M4.500 20c.8-4 4-6 7.500-6s6.700 2 7.500 6"/>',
'building':'<path d="M5 21V4h9v17M14 9h5v12M8 8h3M8 12h3M8 16h3M3 21h18"/>',
'shield':'<path d="M12 3l8 3v6c0 5-3.500 8-8 9-4.500-1-8-4-8-9V6z"/><path d="M8.500 12l2.500 2.500 4.500-5"/>',
'search':'<circle cx="11" cy="11" r="6.500"/><path d="M16 16l5 5"/>',
'folder':'<path d="M3 6h7l2 2h9v11H3z"/>',
'people':'<circle cx="9" cy="8" r="3.500"/><path d="M3 20c.6-3.500 3-5.500 6-5.500s5.400 2 6 5.500M16 5.500a3.500 3.500 0 010 6.500M18 14.800c1.800.7 3 2.600 3.400 5.200"/>',
'phone':'<path d="M5 4h4l2 5-2.500 1.500a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A15 15 0 013 6a2 2 0 012-2z"/>',
'arrow':'<path d="M5 12h14M13 6l6 6-6 6"/>',
'plus':'<path d="M12 5v14M5 12h14"/>',
'check':'<path d="M5 12.500l4.500 4.500L19 7.500"/>',
}
def ic(n,cls='i'): return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{IC[n]}</svg>'
STAR='<svg class="st" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.2l2.7 5.6 6.1.8-4.5 4.2 1.1 6-5.4-3-5.4 3 1.1-6L3.2 9.6l6.1-.8z"/></svg>'
def stars(): return '<span class="stars" aria-hidden="true">'+STAR*5+'</span>'
G='<svg class="g" viewBox="0 0 24 24" aria-label="Google"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 0 1-2.2 3.32v2.77h3.57c2.08-1.92 3.27-4.74 3.27-8.1z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.1a6.6 6.6 0 0 1 0-4.2V7.06H2.18a11 11 0 0 0 0 9.88l3.66-2.84z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84C6.71 7.31 9.14 5.38 12 5.38z"/></svg>'
def flag(t): return f'<span class="flag">[FEHLT] {T(t)}</span>'
PH='tel:+496929802887'
priv_ic=['doc','search','folder','user']; unt_ic=['building','shield','doc','search']
faqhtml=''
for k,(q,a) in enumerate(faq):
    op=' open' if k==0 else ''
    faqhtml+=f'<details class="qa rv"{op}><summary><span>{T(q)}</span>{ic("plus","pl")}</summary><div class="ans"><p>{T(a)}</p></div></details>\n'
cards4h=''.join(f'<article class="svc rv"><div class="no">{n}</div><h3>{T(t)}</h3><p>{T(d)}</p><a class="more" href="#">Mehr erfahren {ic("arrow","ar")}</a></article>' for n,t,d in cards4)
stepsh=''.join(f'<li class="rv"><span class="num"><b>{n}</b></span><h3>{T(t)}</h3><p>{T(d)}</p></li>' for n,t,d in steps)
tlh=''.join(f'<li><b>{T(tlparts(x)[0])}</b><span>{T(tlparts(x)[1])}</span></li>' for x in tl)
v1h=''.join(f'<li>{ic("check","ck")}{T(x)}</li>' for x in v1); v2h=''.join(f'<li>{ic("check","ck")}{T(x)}</li>' for x in v2)
privh=''.join(f'<li>{ic(priv_ic[i],"li")}<span>{T(x)}</span></li>' for i,x in enumerate(priv))
unth=''.join(f'<li>{ic(unt_ic[i],"li")}<span>{T(x)}</span></li>' for i,x in enumerate(unt))
rev=[('Selina M.','Die Beratung war von Anfang an sehr professionell, verständlich und zuverlässig. Man fühlt sich wirklich ernst genommen und gut aufgehoben.'),('Milad','Frau Stürzl arbeitet äußerst professionell, kompetent und nimmt sich wirklich Zeit, alles verständlich zu erklären.'),('J. S.','komplexe Sachverhalte verständlich erklärt')]
revh=''.join(f'<figure class="rev rv">{stars()}<blockquote>„{T(q)}“</blockquote><figcaption>{G}<span>{T(n)}</span></figcaption></figure>' for n,q in rev)
proof=['5,0 bei Google · 14 Bewertungen','5,0 bei anwalt.de · 79 Bewertungen','Fachanwältin für Steuerrecht seit 2021','Zertifizierte Beraterin für Steuerstrafrecht (DAA) seit 2022','Zwei Büros: Frankfurt und München']
proof_ic=['star','chat','award','doc','pin']
proofh=''.join(f'<li class="rv">{ic(proof_ic[i],"pi")}<span>{T(x)}</span></li>' for i,x in enumerate(proof))
page=open(B+'_build/template.html',encoding='utf8').read()
rep={'SUB':T(SUB),'FAQ':faqhtml,'CARDS4':cards4h,'STEPS':stepsh,'TL':tlh,'V1':v1h,'V2':v2h,'PRIV':privh,'UNT':unth,'REV':revh,'PROOF':proofh,'TXT6':T(txt6),'STARS':stars(),'ARR':ic('arrow','ar'),'PHONEIC':ic('phone','ph'),'CHK':ic('check','ck')}
for k,v in rep.items(): page=page.replace('{{'+k+'}}',v)
assert '{{' not in page, re.findall(r'\{\{\w+\}\}',page)
open(B+'07-prototype/index.html','w',encoding='utf8').write(page)
print('built',len(page))
