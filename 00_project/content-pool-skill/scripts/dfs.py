#!/usr/bin/env python3
"""DataForSEO call with spend log and cap.

Usage:
  dfs.py <endpoint> <payload.json> <out.json> --run-dir <content-pool dir> [--cap 5.0]

Example endpoint: dataforseo_labs/google/ranked_keywords/live
Reads credentials from <repo>/.secrets/dataforseo.env (DATAFORSEO_LOGIN, DATAFORSEO_PASSWORD).
Appends one line per call to <run-dir>/spend.jsonl. Stops (exit 3) if the total would pass the cap.
"""
import argparse, base64, json, os, sys, time, urllib.request

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), *[".."] * 2))
ENV_CANDIDATES = [
    os.path.join(os.getcwd(), ".secrets", "dataforseo.env"),
    "/Users/martindrendel/741website/.secrets/dataforseo.env",
]


def load_env():
    for path in ENV_CANDIDATES:
        if os.path.exists(path):
            env = {}
            for line in open(path):
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip().strip('"').strip("'")
            return env
    sys.exit("dataforseo.env not found")


def spent(run_dir):
    path = os.path.join(run_dir, "spend.jsonl")
    if not os.path.exists(path):
        return 0.0
    return sum(json.loads(l).get("cost", 0) for l in open(path) if l.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("endpoint")
    ap.add_argument("payload")
    ap.add_argument("out")
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--cap", type=float, default=5.0)
    a = ap.parse_args()

    total = spent(a.run_dir)
    if total >= a.cap:
        print(f"CAP REACHED: {total:.4f} USD of {a.cap} USD. Ask Martin.", file=sys.stderr)
        sys.exit(3)

    env = load_env()
    auth = base64.b64encode(f"{env['DATAFORSEO_LOGIN']}:{env['DATAFORSEO_PASSWORD']}".encode()).decode()
    body = open(a.payload, "rb").read()
    req = urllib.request.Request(
        f"https://api.dataforseo.com/v3/{a.endpoint}",
        data=body,
        headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    json.dump(data, open(a.out, "w"), ensure_ascii=False)
    cost = data.get("cost", 0) or 0
    line = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "endpoint": a.endpoint,
        "cost": cost,
        "status": data.get("status_code"),
        "out": a.out,
    }
    with open(os.path.join(a.run_dir, "spend.jsonl"), "a") as f:
        f.write(json.dumps(line) + "\n")
    print(f"{a.endpoint} status={data.get('status_code')} cost={cost} total={total + cost:.4f}/{a.cap}")


if __name__ == "__main__":
    main()
