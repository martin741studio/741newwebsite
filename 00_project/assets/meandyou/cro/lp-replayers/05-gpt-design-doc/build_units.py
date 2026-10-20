import re,json
s=open('../04-copy/approved-copy.md').read()
s=s.split('<!-- TECH -->')[0]
U={}
for m in re.finditer(r'<!-- (S\d\d) [^>]*-->(.*?)<!-- /\1 -->',s,re.S):
    lines=[]
    for l in m.group(2).split('\n'):
        l=l.strip()
        if not l or l.startswith('<!--'): continue
        l=re.sub(r'^#+\s*','',l); l=re.sub(r'^-\s+','',l); l=re.sub(r'^(\d+)\.\s+',r'\1. ',l)
        l=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',l); l=l.replace('**','')
        lines.append(l)
    U[m.group(1)]=lines
json.dump(U,open('units.json','w'),ensure_ascii=False,indent=1)
print({k:len(v) for k,v in U.items()})
