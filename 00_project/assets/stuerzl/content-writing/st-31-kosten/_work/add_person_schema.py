#!/usr/bin/env python3
"""Append the Person node of Dr. Stürzl (from nap.json) to 05-final/schema.jsonld, because schema_tool.py make writes Person only on practitioner pages.
Run AFTER run_gates.py: python3 _work/add_person_schema.py <run_dir>. The node uses the same @id as the person page (/dr-anja-stuerzl/#person) and is referenced as 'mentions' by the WebPage."""
import json,sys
from pathlib import Path
run=Path(sys.argv[1]); nap=json.load(open('/Users/martindrendel/741website/00_project/assets/stuerzl/nap.json',encoding='utf-8'))
f=run/'05-final/schema.jsonld'; d=json.load(open(f,encoding='utf-8'))
g=d['@graph']
if not any(x.get('@type')=='Person' for x in g):
    base=nap['base_url']; p=nap['people']['dr-anja-stuerzl']; url=base+p['url_slug']
    g.append({"@type":"Person","@id":url+"#person","name":p['name'],"jobTitle":p['jobTitle'],"url":url,"worksFor":{"@id":base+"/"+nap['organization']['id']},
      "hasCredential":[{"@type":"EducationalOccupationalCredential","name":c} for c in p['credentials']]})
    for x in g:
        if x.get('@type')=='WebPage': x['mentions']={"@id":url+"#person"}
json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('person schema ok')
