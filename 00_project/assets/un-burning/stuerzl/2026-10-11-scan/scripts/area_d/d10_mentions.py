"""D10: confirm unlinked mentions live (LTO, JUVE, ZRI): page mentions the firm, no link to the firm's domain. GET only."""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ub_lib import *
from bs4 import BeautifulSoup
U=[("LTO","https://www.lto.de/kanzleien-unternehmen/transfermarkt/detail/198-dr-anja-stuerzl-wechselt-zu-stuerzl-steuerstrafrecht"),
   ("JUVE","https://www.juve.de/markt-und-management/bekannte-steuerstrafrechtlerin-von-rettenmaier-gruendet-eigene-boutique/"),
   ("ZRI","https://www.zri-online.de/aktuell/stuerzl-steuerstrafrecht-eroeffnet-buero-in-muenchen-79764/")]
rows=[]
for name,u in U:
    chain,r,err=fetch_chain(u)
    row={"outlet":name,"url":u,"final_status":r.status_code if r is not None else None,"error":err,"chain":[c.get("status") for c in chain]}
    if r is not None and r.status_code==200:
        soup=BeautifulSoup(r.text,"html.parser")
        txt=soup.get_text(" ",strip=True)
        row["mentions_firm_in_text"]=len(re.findall(r"St(?:ü|ue)rzl",txt))
        row["firm_name_text_hits"]=len(re.findall(r"St(?:ü|ue)rzl Steuerstrafrecht",txt,re.I))
        links=[a["href"] for a in soup.find_all("a",href=True) if "stuerzl-steuerstrafrecht" in a["href"].lower()]
        row["links_to_firm_domain"]=links
        row["html_bytes"]=len(r.content)
        row["evidence_id"]=save_evidence(f"EV-D-mention-{name.lower()}", r.content,"html","requests GET",f"GET {u}")
    rows.append(row); print(name,row.get("final_status"),row.get("mentions_firm_in_text"),row.get("links_to_firm_domain"),row.get("error"))
save_evidence("EV-D-mentions-summary", json.dumps({"collected_at":now(),"rows":rows},ensure_ascii=False,indent=1),"json","requests GET + BeautifulSoup","3 outlet pages: firm mention in text vs link to the firm's domain")
