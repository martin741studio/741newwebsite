import subprocess, sys, json
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import save_evidence
def run(cmd, timeout=60):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return (r.stdout + ("\n[stderr]\n" + r.stderr if r.stderr.strip() else "")), r.returncode
    except Exception as e:
        return f"ERROR: {e}", -1
jobs = [
 ("EV-A-whois", ["whois","suriya-praxis.de"], "whois", "txt"),
 ("EV-A-whois-www", ["whois","-h","whois.denic.de","suriya-praxis.de"], "whois", "txt"),
 ("EV-A-dig-ns", ["dig","+noall","+answer","NS","suriya-praxis.de"], "dig", "txt"),
 ("EV-A-dig-a", ["dig","+noall","+answer","A","suriya-praxis.de"], "dig", "txt"),
 ("EV-A-dig-a-www", ["dig","+noall","+answer","A","www.suriya-praxis.de"], "dig", "txt"),
 ("EV-A-dig-aaaa", ["dig","+noall","+answer","AAAA","suriya-praxis.de"], "dig", "txt"),
 ("EV-A-dig-mx", ["dig","+noall","+answer","MX","suriya-praxis.de"], "dig", "txt"),
 ("EV-A-dig-txt", ["dig","+noall","+answer","TXT","suriya-praxis.de"], "dig", "txt"),
 ("EV-A-dig-soa", ["dig","+noall","+answer","SOA","suriya-praxis.de"], "dig", "txt"),
 ("EV-A-headers-root", ["curl","-sSI","-m","30","https://suriya-praxis.de/"], "curl", "txt"),
 ("EV-A-headers-www", ["curl","-sSI","-m","30","https://www.suriya-praxis.de/"], "curl", "txt"),
 ("EV-A-headers-http", ["curl","-sSI","-m","30","http://suriya-praxis.de/"], "curl", "txt"),
 ("EV-A-rdap-denic", ["curl","-sS","-m","30","-H","Accept: application/rdap+json","https://rdap.denic.de/domain/suriya-praxis.de"], "curl-rdap", "json"),
 ("EV-A-rdap-iana-bootstrap", ["curl","-sS","-m","30","https://data.iana.org/rdap/dns.json"], "curl-rdap", "json"),
]
for eid, cmd, tool, ext in jobs:
    out, rc = run(cmd)
    save_evidence(eid, out, ext, tool, " ".join(cmd), subdir="area_a", note=f"rc={rc}")
    print(eid, "rc", rc, len(out))
