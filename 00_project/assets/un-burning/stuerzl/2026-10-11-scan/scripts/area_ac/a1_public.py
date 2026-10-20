import subprocess, sys
sys.path.insert(0, __file__.rsplit('/',1)[0])
from ub_lib import save_evidence
D = "stuerzl-steuerstrafrecht.de"
def run(cmd, timeout=60):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return (r.stdout + ("\n[stderr]\n" + r.stderr if r.stderr.strip() else "")), r.returncode
    except Exception as e:
        return f"ERROR: {e}", -1
jobs = [
 ("EV-A-whois", ["whois", D], "whois", "txt"),
 ("EV-A-whois-denic", ["whois","-h","whois.denic.de", D], "whois", "txt"),
 ("EV-A-rdap-denic", ["curl","-sS","-m","30","-H","Accept: application/rdap+json",f"https://rdap.denic.de/domain/{D}"], "curl-rdap", "json"),
 ("EV-A-dig-ns", ["dig","+noall","+answer","NS",D], "dig", "txt"),
 ("EV-A-dig-soa", ["dig","+noall","+answer","SOA",D], "dig", "txt"),
 ("EV-A-dig-a", ["dig","+noall","+answer","A",D], "dig", "txt"),
 ("EV-A-dig-a-www", ["dig","+noall","+answer","A","www."+D], "dig", "txt"),
 ("EV-A-dig-aaaa", ["dig","+noall","+answer","AAAA",D], "dig", "txt"),
 ("EV-A-dig-mx", ["dig","+noall","+answer","MX",D], "dig", "txt"),
 ("EV-A-dig-txt", ["dig","+noall","+answer","TXT",D], "dig", "txt"),
 ("EV-A-dig-caa", ["dig","+noall","+answer","CAA",D], "dig", "txt"),
 ("EV-A-dig-rdns", ["dig","+noall","+answer","-x","212.53.214.189"], "dig", "txt"),
 ("EV-A-headers-https", ["curl","-sSI","-m","30",f"https://{D}/"], "curl", "txt"),
 ("EV-A-headers-www", ["curl","-sSI","-m","30",f"https://www.{D}/"], "curl", "txt"),
 ("EV-A-headers-http", ["curl","-sSI","-m","30",f"http://{D}/"], "curl", "txt"),
 ("EV-A-whois-ip", ["whois","212.53.214.189"], "whois", "txt"),
]
for eid, cmd, tool, ext in jobs:
    out, rc = run(cmd)
    save_evidence(eid, out, ext, tool, " ".join(cmd), "area_a", note=f"rc={rc}")
    print(eid, "rc", rc, len(out))
# TLS certificate
out, rc = run(["bash","-c",f"echo | openssl s_client -connect {D}:443 -servername {D} 2>/dev/null | openssl x509 -noout -issuer -subject -dates -ext subjectAltName"])
save_evidence("EV-A-tls-cert", out, "txt", "openssl", f"openssl s_client -connect {D}:443 | openssl x509 -noout -issuer -subject -dates -ext subjectAltName", "area_a", note=f"rc={rc}")
print("tls", out)
