"""Tiny Supabase helper for the morning grill (admin login of the standup bot, same pattern as reporting/daily-standup.sh).
Only two tables are written: grill_snapshots (insert) and nothing else. Reads: grill_answers."""
import json, os, urllib.request

# Framework python (python.org install) ships without a wired CA bundle; plain urllib then fails
# with CERTIFICATE_VERIFY_FAILED. Point it at certifi before any HTTPS call (goals-data-architecture, 2026-10-15).
try:
    import certifi
    os.environ.setdefault("SSL_CERT_FILE", certifi.where())
except ImportError:
    pass

REPO = os.environ.get("MG_REPO", "/Users/martindrendel/741website")


def _env():
    env = {}
    for line in open(os.path.join(REPO, ".secrets", "standup.env"), encoding="utf-8"):
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.strip().split("=", 1)
            env[k] = v.strip().strip('"')
    return env


_CACHE = {}


def login():
    if "t" in _CACHE:
        return _CACHE["t"]
    env = _env()
    body = json.dumps({"email": env["STANDUP_EMAIL"], "password": env["STANDUP_PASSWORD"]}).encode()
    req = urllib.request.Request(f"{env['SUPABASE_URL']}/auth/v1/token?grant_type=password", data=body,
                                 headers={"apikey": env["SUPABASE_ANON"], "Content-Type": "application/json"})
    token = json.load(urllib.request.urlopen(req, timeout=30))["access_token"]
    _CACHE["t"] = (env["SUPABASE_URL"], env["SUPABASE_ANON"], token)
    return _CACHE["t"]


def request(method, path, payload=None, prefer=None):
    url, anon, token = login()
    h = {"apikey": anon, "Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    if prefer:
        h["Prefer"] = prefer
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(f"{url}/rest/v1/{path}", data=data, headers=h, method=method)
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read()
    return json.loads(raw) if raw else None
