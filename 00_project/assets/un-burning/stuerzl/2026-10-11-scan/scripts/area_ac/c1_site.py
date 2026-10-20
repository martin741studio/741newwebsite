import sys, subprocess, re, json, html
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import save_evidence, now
BASE = "https://www.stuerzl-steuerstrafrecht.de"
PAGES = {
 "home": "/", "impressum": "/index.php/impressum", "kontakt": "/index.php/kontakt", "datenschutz": "/index.php/datenschutz",
 "team": "/index.php/team", "kanzlei": "/index.php/kanzlei", "leistungen": "/index.php/leistungen", "faq": "/index.php/faq",
 "steuerstrafrecht": "/index.php/steuerstrafrecht", "lea-wimmer": "/index.php/lea-wimmer", "dr-anja-stuerzl": "/index.php/dr-anja-stuerzl",
 "aktuelles": "/index.php/aktuelles", "selbstanzeigen": "/index.php/selbstanzeigen-steuerliche-korrekturen",
}
out = {}
for key, path in PAGES.items():
    r = subprocess.run(["curl","-sS","-m","40","-L","-A","Mozilla/5.0 741-unburning-scan/1.0","-w","\n__HTTP__%{http_code}",BASE+path],capture_output=True)
    body = r.stdout
    code = body.rsplit(b"\n__HTTP__",1)[-1].decode()
    body = body.rsplit(b"\n__HTTP__",1)[0]
    save_evidence(f"EV-C-site-{key}", body, "html", "curl", f"curl -sSL {BASE+path}", "area_c", note=f"http={code}")
    out[key]=(path,code,len(body))
    print(key, code, len(body))
