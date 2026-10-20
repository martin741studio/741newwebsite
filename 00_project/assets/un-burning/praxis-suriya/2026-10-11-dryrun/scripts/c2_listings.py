"""Fetch candidate listing URLs (read-only GET) and save raw HTML as evidence."""
import sys, json, re, requests, time
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import save_evidence, now
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", "Accept-Language": "de-DE,de;q=0.9"}
L = {
 "cylex": "https://web2.cylex.de/firma-home/praxis-suriya---ayurveda-_-naturheilkunde-10733378.html",
 "infobel-1": "https://www.infobel.com/de/germany/heilpraktiker_ingelheim_i_praxis_suriya_ayurveda_naturheilkunde/ingelheim_am_rhein/DE109349224/businessdetails.aspx",
 "infobel-2": "https://www.infobel.com/de/germany/suriya_heilpraktikerin/ingelheim_am_rhein/DE111780212-061329795890/businessdetails.aspx",
 "theralupa-10902": "https://www.theralupa.de/heilpraktiker/ayurveda-praxis-suriya-ingelheim-10902",
 "theralupa-11505": "https://www.theralupa.de/heilpraktiker/suriya-ingelheim-11505",
 "golocal": "https://www.golocal.de/ingelheim/heilpraktiker/praxis-suriya-YUWGl/",
 "goyellow": "https://www.goyellow.de/home/heilpraktiker-fuer-naturheilkunde-praxis-suriya-ingelheim--4pwghb.html",
 "jameda": "https://www.jameda.de/profil/coralie-suriyapperuma",
 "aerzte-de": "https://www.aerzte.de/ingelheim-am-rhein/rheinland-pfalz/heilpraktiker/coralie-suriyapperuma",
 "mapquest-suriya-praxis": "https://www.mapquest.com/de/rheinland-pfalz/suriya-praxis-804350293",
 "xing": "https://www.xing.com/profile/Coralie_Suriyapperuma",
 "work5": "https://work5.de/kategorien/dienstleister/gesundheit-und-schoenheit/heilpraktiker",
 "11880": "https://www.11880.com/suche/heilpraktiker/heidesheim",
 "branchen-info": "https://ingelheim-am-rhein.branchen-info.net/schuetten-iris/3170134/",
 "maptons": "https://zw.maptons.com/p/3112170407",
 "facebook": "https://www.facebook.com/coraliesuriyapperuma/",
 "linkedin": "https://de.linkedin.com/in/coralie-suriyapperuma-coach",
 "instagram": "https://www.instagram.com/suriya.praxis/",
 "wildcrumble-impressum": "https://wildcrumble.com/policies/legal-notice",
 "allgemeine-zeitung": "https://www.allgemeine-zeitung.de/lokales/kreis-mainz-bingen/ingelheim/wiedereroeffnung-ayurveda-und-naturheilpraxis-in-ingelheim-2891615",
}
res = {}
for k, u in L.items():
    try:
        r = requests.get(u, headers=UA, timeout=40, allow_redirects=True)
        res[k] = {"url": u, "status": r.status_code, "final": r.url, "bytes": len(r.content)}
        save_evidence(f"EV-C-listing-{k}", r.content, "html", "requests GET", f"GET {u} (browser UA, follow redirects)", subdir="area_c/listings", note=f"status={r.status_code}")
    except Exception as e:
        res[k] = {"url": u, "status": None, "error": f"{type(e).__name__}: {e}"}
    print(k, res[k].get("status"), res[k].get("bytes"), res[k].get("error", ""), flush=True)
    time.sleep(0.5)
json.dump(res, open("evidence/area_c/listing-fetch-status.json", "w"), indent=1)
