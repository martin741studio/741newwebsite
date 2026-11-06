#!/usr/bin/env python3
"""Git worktrees for a 741 agent team (Orchestrator, Task Manager, Workers).

    python3 team.py create <slug> worker1 worker2 [--base main]
        one worktree + branch per worker, plus an integration worktree for the Task Manager
    python3 team.py status <slug> [--contract <contract.json>]
        per worker: branch, commits ahead, uncommitted files, files outside its ownership,
        files that two workers both changed
    python3 team.py merge-check <slug>
        dry-run merge (git merge-tree) of every worker branch into integration and against each other
    python3 team.py integrate <slug> <worker>
        merge one worker branch into the integration worktree, only when merge-check is clean
    python3 team.py remove <slug>
        remove clean, merged worktrees and branches (never forced)

Paths:  .claude/worktrees/team-<slug>-<worker>   branch team/<slug>/<worker>
        .claude/worktrees/team-<slug>-integration branch team/<slug>/integration
The final merge of the integration branch into main is the lead's job, with Martin's go.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[4])
WT = ROOT / ".claude" / "worktrees"


def git(*args, cwd=ROOT, check=True):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed:\n{r.stderr.strip() or r.stdout.strip()}")
    return r


def wt_path(slug, name):
    return WT / f"team-{slug}-{name}"


def branch(slug, name):
    return f"team/{slug}/{name}"


def team_members(slug):
    prefix = f"team-{slug}-"
    out = []
    for line in git("worktree", "list", "--porcelain").stdout.splitlines():
        if line.startswith("worktree "):
            p = Path(line[9:])
            if p.name.startswith(prefix):
                out.append(p.name[len(prefix):])
    return out


def base_of(slug):
    f = WT / f"team-{slug}.json"
    return json.loads(f.read_text())["base"] if f.exists() else "main"


def changed_files(slug, name, base):
    p = wt_path(slug, name)
    committed = git("diff", "--name-only", f"{base}...{branch(slug, name)}").stdout.split()
    dirty = [l[3:] for l in git("status", "--porcelain", cwd=p).stdout.splitlines() if l.strip()]
    return committed, dirty


def owned_by(contract, owner):
    return [f for t in contract.get("tasks", []) if t.get("owner") == owner for f in t.get("files", [])]


def inside(path, globs):
    for g in globs:
        g = g.rstrip("*")
        if path == g.rstrip("/") or path.startswith(g if g.endswith("/") else g + "/") or path == g:
            return True
    return False


def cmd_create(slug, workers, base):
    if git("rev-parse", "--verify", "--quiet", base, check=False).returncode != 0:
        sys.exit(f"base {base} not found")
    dirty = git("status", "--porcelain").stdout.splitlines()
    if dirty:
        print(f"NOTE  main has {len(dirty)} uncommitted changes. Worktrees start from the last commit of {base};")
        print("      they do not see those changes. Commit what the team needs first.")
    WT.mkdir(parents=True, exist_ok=True)
    (WT / f"team-{slug}.json").write_text(json.dumps({"base": base, "workers": workers}) + "\n")
    for name in [*workers, "integration"]:
        p, b = wt_path(slug, name), branch(slug, name)
        if p.exists():
            print(f"exists  {p}")
            continue
        git("worktree", "add", "-b", b, str(p), base)
        print(f"created {p}  ({b})")
    return 0


def cmd_status(slug, contract_path):
    base = base_of(slug)
    contract = json.loads(Path(contract_path).read_text()) if contract_path else None
    touched, problems = {}, 0
    for name in team_members(slug):
        p = wt_path(slug, name)
        ahead = git("rev-list", "--count", f"{base}..{branch(slug, name)}").stdout.strip()
        last = git("log", "-1", "--format=%h %s (%cr)", cwd=p).stdout.strip()
        committed, dirty = changed_files(slug, name, base)
        print(f"== {name}  branch {branch(slug, name)}  ahead {ahead}  uncommitted {len(dirty)}")
        print(f"   last: {last}")
        if name == "integration":
            continue
        for f in set(committed) | set(dirty):
            touched.setdefault(f, set()).add(name)
        if contract:
            own = owned_by(contract, name)
            outside = sorted(f for f in set(committed) | set(dirty) if not inside(f, own))
            if outside:
                problems += 1
                print(f"   OUTSIDE OWNERSHIP ({len(outside)}): {', '.join(outside[:8])}")
    clash = {f: w for f, w in touched.items() if len(w) > 1}
    for f, w in sorted(clash.items()):
        print(f"CONFLICT RISK  {f} changed by {', '.join(sorted(w))}")
    if not clash:
        print("no file is changed by two workers")
    return 1 if clash or problems else 0


def merge_tree(a, b):
    r = git("merge-tree", "--write-tree", "--name-only", "--no-messages", a, b, check=False)
    lines = r.stdout.splitlines()[1:]
    return r.returncode == 0, [l for l in lines if l.strip()]


def cmd_merge_check(slug):
    members = [m for m in team_members(slug) if m != "integration"]
    integ = branch(slug, "integration")
    bad = 0
    for m in members:
        ok, files = merge_tree(integ, branch(slug, m))
        print(f"{'clean   ' if ok else 'CONFLICT'} integration <- {m}" + ("" if ok else f": {', '.join(files[:8])}"))
        bad += not ok
    for i, a in enumerate(members):
        for b in members[i + 1:]:
            ok, files = merge_tree(branch(slug, a), branch(slug, b))
            print(f"{'clean   ' if ok else 'CONFLICT'} {a} <-> {b}" + ("" if ok else f": {', '.join(files[:8])}"))
            bad += not ok
    return 1 if bad else 0


def cmd_integrate(slug, worker):
    integ_path = wt_path(slug, "integration")
    if git("status", "--porcelain", cwd=integ_path).stdout.strip():
        sys.exit("integration worktree has uncommitted changes; commit or stash them first")
    wdirty = git("status", "--porcelain", cwd=wt_path(slug, worker)).stdout.strip()
    if wdirty:
        sys.exit(f"{worker} has uncommitted changes; the worker commits first")
    ok, files = merge_tree(branch(slug, "integration"), branch(slug, worker))
    if not ok:
        sys.exit(f"conflict with {worker}: {', '.join(files)}. Send it back to the owner; do not resolve by deleting work.")
    git("merge", "--no-ff", "-m", f"team {slug}: integrate {worker}", branch(slug, worker), cwd=integ_path)
    print(f"merged {branch(slug, worker)} into {branch(slug, 'integration')}")
    return 0


def cmd_remove(slug):
    left = 0
    for name in team_members(slug):
        p, b = wt_path(slug, name), branch(slug, name)
        r = git("worktree", "remove", str(p), check=False)
        if r.returncode != 0:
            print(f"kept    {p}: {r.stderr.strip()}")
            left += 1
            continue
        r = git("branch", "-d", b, check=False)
        print(f"removed {p}" + ("" if r.returncode == 0 else f" (branch {b} kept: not merged)"))
    meta = WT / f"team-{slug}.json"
    if not left and meta.exists():
        meta.unlink()
    return 1 if left else 0


def main(a):
    if len(a) < 3:
        print(__doc__)
        return 2
    cmd, slug, rest = a[1], a[2], a[3:]
    if cmd == "create":
        base = "main"
        if "--base" in rest:
            i = rest.index("--base")
            base = rest[i + 1]
            rest = rest[:i] + rest[i + 2:]
        if not rest:
            sys.exit("name at least one worker")
        return cmd_create(slug, rest, base)
    if cmd == "status":
        cp = rest[rest.index("--contract") + 1] if "--contract" in rest else None
        return cmd_status(slug, cp)
    if cmd == "merge-check":
        return cmd_merge_check(slug)
    if cmd == "integrate" and rest:
        return cmd_integrate(slug, rest[0])
    if cmd == "remove":
        return cmd_remove(slug)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
