#!/usr/bin/env python3
"""Read-only Local Falcon client over the MCP endpoint (works when no MCP is configured in the session).
Usage: python3 -I falcon_read.py tools\n       python3 -I falcon_read.py schema <toolName>
       python3 -I falcon_read.py call <toolName> '<json args>' [out.json]
Only tools that start with list, get or search are allowed. Scans (run*, save*, delete*) are refused.
Key: LF_API_KEY from <repo>/.env. The key is never printed."""
import json, os, re, sys, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
def key():
    for l in open(os.path.join(ROOT, ".env"), encoding="utf-8"):
        m = re.match(r"^LF_API_KEY=(.*)$", l.strip())
        if m: return m.group(1).strip().strip("\"'")
    sys.exit("LF_API_KEY not found in .env")

K = key()
URL = f"https://mcp.localfalcon.com/mcp?local_falcon_api_key={K}"
HDR = {"Authorization": f"Bearer {K}", "Content-Type": "application/json", "Accept": "application/json, text/event-stream"}

def rpc(payload, sid=None):
    h = dict(HDR)
    if sid: h["Mcp-Session-Id"] = sid
    req = urllib.request.Request(URL, data=json.dumps(payload).encode(), headers=h, method="POST")
    with urllib.request.urlopen(req, timeout=120) as r:
        body = r.read().decode()
        sid2 = r.headers.get("mcp-session-id") or sid
    if body.lstrip().startswith("event:") or "\ndata:" in body or body.startswith("data:"):
        body = [l[5:].strip() for l in body.splitlines() if l.startswith("data:")][-1]
    return json.loads(body), sid2

def session():
    _, sid = rpc({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "maps-playbook", "version": "0.1"}}})
    try: rpc({"jsonrpc": "2.0", "method": "notifications/initialized"}, sid)
    except Exception: pass
    return sid

def main():
    cmd = sys.argv[1]; sid = session()
    if cmd == "tools":
        r, _ = rpc({"jsonrpc": "2.0", "id": 2, "method": "tools/list"}, sid)
        for t in r["result"]["tools"]: print(t["name"])
        return
    if cmd == "schema":
        r, _ = rpc({"jsonrpc": "2.0", "id": 2, "method": "tools/list"}, sid)
        for t in r["result"]["tools"]:
            if t["name"] == sys.argv[2]: print(json.dumps(t, ensure_ascii=False)[:2500])
        return
    name, args = sys.argv[2], json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
    if not re.match(r"^(list|get|search|view)", name): sys.exit(f"refused: {name} is not a read-only tool")
    r, _ = rpc({"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": name, "arguments": args}}, sid)
    out = json.dumps(r, ensure_ascii=False, indent=1)
    if len(sys.argv) > 4: open(sys.argv[4], "w", encoding="utf-8").write(out); print("wrote", sys.argv[4], len(out))
    else: print(out[:6000])

if __name__ == "__main__":
    main()
