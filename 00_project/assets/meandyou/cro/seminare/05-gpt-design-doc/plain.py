#!/usr/bin/env python3
"""Visible text units per section from approved-copy.md. Inner quotes become ‚‘."""
import re,sys,json
src=open(sys.argv[1],encoding='utf-8').read()
src=src.split('---',2)[2] if src.startswith('---') else src
src=src.split('<!-- TECH')[0]
secs={}
for m in re.finditer(r'<!-- (S\d\d) [^>]*-->(.*?)<!-- /\1 -->',src,re.S):
    body=re.sub(r'<!--.*?-->','',m.group(2),flags=re.S)
    units=[]
    for line in body.split('\n'):
        l=line.strip()
        if not l or re.match(r'^\|[-| ]+\|$',l): continue
        l=re.sub(r'^#+\s*','',l); l=re.sub(r'^\d+\.\s+','',l); l=re.sub(r'^-\s+','',l)
        l=l.replace('**','')
        l=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',l)
        l=l.replace('„','‚').replace('“','‘')
        if l.startswith('|'):
            units+= [c.strip() for c in l.strip('|').split('|') if c.strip()]
        else: units.append(l)
    secs[m.group(1)]=units
json.dump(secs,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
open(sys.argv[3],'w').write('\n'.join(u for s in secs.values() for u in s))
print({k:len(v) for k,v in secs.items()})
