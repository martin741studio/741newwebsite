#!/usr/bin/env python3
"""PreToolUse: block destructive commands (741 adaptation of the "Codeguard" bash parser).

Idea from the TokenMade podcast (Alexander Weipprecht, 2026-11-05): every command the
model sends goes through a parser first. Destructive commands are blocked, so agents can
run in bypass-permissions mode without wiping files, git history or databases.

What it blocks (each segment of a command line is checked on its own):
  files   rm -r / rm -rf (unless every target is a throwaway path), find -delete,
          find -exec rm, xargs rm, shred, srm
  git     reset --hard, clean -f, push --force / -f / --force-with-lease / +refspec,
          branch -D, checkout -- . / checkout . / restore . (discard all changes),
          stash drop / clear, worktree remove --force, filter-branch, filter-repo,
          update-ref -d, reflog expire, gc --prune=now
  sql     DROP (TABLE|DATABASE|SCHEMA|VIEW|FUNCTION|INDEX), TRUNCATE,
          DELETE FROM / UPDATE ... SET without WHERE, ALTER TABLE ... DROP
          (in Bash via psql/mysql/sqlite3, and in Supabase execute_sql / apply_migration)
  system  mkfs, dd of=/dev/, > /dev/disk, diskutil erase, chmod/chown -R on / or ~,
          shutdown, reboot, halt, fork bomb, curl|wget piped into a shell,
          killall / pkill of Chrome (memory rule: never kill Chrome), launchctl remove,
          crontab -r, sudo with any of the above

A go from Martin (marker written by go_marker.py / go_card.py) lets the lead session pass.
Teammates and subagents run as their own sessions, so they never hold a go:
destructive commands stay blocked for workers, always.

Limits: this is a parser over shell text, not a sandbox. Obfuscated commands
(base64 | sh, variables that hold "rm") can pass. The deny list targets accidents,
not an attacker.
"""
import json
import os
import re
import shlex
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _go  # noqa: E402

# Paths where a recursive delete is a normal cleanup, not a risk.
THROWAWAY_RE = re.compile(
    r"^(?:/tmp/|/private/tmp/|/var/folders/)"
    r"|(?:^|/)(?:node_modules|__pycache__|\.pytest_cache|\.mypy_cache|\.ruff_cache|\.next|\.turbo|\.cache"
    r"|dist|build|out|coverage|tmp|\.tmp)(?:/|$)"
)

SQL_DESTRUCTIVE_RE = re.compile(
    r"\bdrop\s+(?:table|database|schema|view|materialized\s+view|function|index|policy|trigger|type|extension|role|user)\b"
    r"|\btruncate\s+(?:table\s+)?\w"
    r"|\balter\s+table\s+[\w.\"]+\s+drop\b"
    r"|\bdelete\s+from\s+[\w.\"]+\s*(?:;|$|returning\b)"
    r"|\bupdate\s+[\w.\"]+\s+set\s+(?:(?!\bwhere\b)[^;])*(?:;|$)",
    re.IGNORECASE | re.DOTALL,
)

WRAPPERS = {"sudo", "env", "nohup", "time", "nice", "command", "exec", "caffeinate", "doas"}
WRAPPER_OPTS_WITH_ARG = {"-u", "-g", "-n", "-C", "-p", "-U"}
SHELLS = {"sh", "bash", "zsh", "dash", "ksh", "fish"}
HEREDOC_RE = re.compile(r"<<-?\s*(['\"]?)(\w+)\1[^\n]*\n(.*?)\n\s*\2(?=\s|$)", re.DOTALL)


def split_segments(line):
    """Split on ; && || | and newlines, but not inside quotes."""
    segs, cur, q, i = [], [], None, 0
    while i < len(line):
        c = line[i]
        if q:
            cur.append(c)
            if c == "\\" and q == '"' and i + 1 < len(line):
                cur.append(line[i + 1])
                i += 1
            elif c == q:
                q = None
        elif c in ("'", '"'):
            q = c
            cur.append(c)
        elif c == "\\" and i + 1 < len(line):
            cur.append(c + line[i + 1])
            i += 1
        elif line.startswith(("&&", "||"), i):
            segs.append("".join(cur)); cur = []; i += 1
        elif c in (";", "\n") or (c == "|" and not line.startswith("|&", i)):
            segs.append("".join(cur)); cur = []
        elif c == "&" and (i == 0 or line[i - 1] not in "<>") and not line.startswith("&>", i):
            segs.append("".join(cur)); cur = []  # background job: "a & b"
        else:
            cur.append(c)
        i += 1
    segs.append("".join(cur))
    return segs


def strip_heredocs(line):
    """Drop heredoc bodies (file content, not commands) unless a shell reads them."""
    out = []
    pos = 0
    for m in HEREDOC_RE.finditer(line):
        head = line[pos:m.start()]
        last_cmd = (split_segments(head) or [""])[-1].strip().split()
        feeds_shell = bool(last_cmd) and os.path.basename(last_cmd[0]) in SHELLS
        out.append(head)
        out.append("\n" + m.group(3) + "\n" if feeds_shell else " ")
        pos = m.end()
    out.append(line[pos:])
    return "".join(out)


def deny(reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": "[741 destructive-guard] " + reason +
        " This is blocked for every agent. If it is truly needed, the lead (not a teammate) "
        "shows Martin the exact command and asks for his go. Do not retry another way.",
    }}))
    return 0


def tokens(segment):
    try:
        toks = shlex.split(segment, comments=False, posix=True)
    except ValueError:
        toks = segment.split()
    # strip wrappers (sudo -u x, env A=b, nohup ...) and leading VAR=value assignments
    while toks:
        t = toks[0]
        if t in WRAPPERS or re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", t):
            toks = toks[1:]
            while toks and toks[0].startswith("-"):
                toks = toks[2:] if toks[0] in WRAPPER_OPTS_WITH_ARG else toks[1:]
            continue
        break
    return toks


def is_throwaway(path):
    p = path.strip().strip("'\"")
    if not p or p in (".", "..", "*", "/", "~", "$HOME", "${HOME}", "./", "../"):
        return False
    if p.startswith("~") or p.startswith("$HOME") or p.startswith("${HOME}"):
        return False
    if p.endswith("/*") and not THROWAWAY_RE.search(p[:-1]):
        return False
    return bool(THROWAWAY_RE.search(p))


def check_rm(toks):
    flags = "".join(t[1:] for t in toks[1:] if t.startswith("-") and not t.startswith("--"))
    long = [t for t in toks[1:] if t.startswith("--")]
    recursive = "r" in flags.lower() or "--recursive" in long
    if not recursive:
        return None
    targets = [t for t in toks[1:] if not t.startswith("-")]
    if not targets:
        return None
    risky = [t for t in targets if not is_throwaway(t)]
    if risky:
        return f"Recursive delete of {', '.join(risky[:3])}."
    return None


def check_git(toks):
    if len(toks) < 2:
        return None
    # skip "git -C path" style options
    i = 1
    while i < len(toks) and toks[i].startswith("-"):
        i += 2 if toks[i] in ("-C", "-c", "--git-dir", "--work-tree") else 1
    if i >= len(toks):
        return None
    sub, args = toks[i], toks[i + 1:]
    a = set(args)
    if sub == "reset" and "--hard" in a:
        return "git reset --hard discards uncommitted work."
    if sub == "clean" and any(re.match(r"^-[a-zA-Z]*f", x) for x in args):
        return "git clean -f deletes untracked files."
    if sub == "push" and (a & {"--force", "-f", "--force-with-lease", "--mirror", "--delete", "-d"}
                          or any(x.startswith("+") for x in args)
                          or any(x.startswith("--force-with-lease=") for x in args)
                          or any(x.startswith(":") for x in args)):
        return "Force push or remote branch delete rewrites shared history."
    if sub == "branch" and ("-D" in a or (a & {"-d", "--delete"} and a & {"--force", "-f"})):
        return "git branch -D deletes a branch with unmerged work."
    if sub == "restore" and "--staged" in a and "--worktree" not in a and "-W" not in a:
        return None  # only unstages, the files stay
    if sub in ("checkout", "restore") and ("." in args or ":/" in args or "*" in args) and "-b" not in a:
        return f"git {sub} . discards every uncommitted change in the tree."
    if sub == "checkout" and "--" in args and args[args.index("--") + 1:] in (["."], [":/"], ["*"]):
        return "git checkout -- . discards every uncommitted change in the tree."
    if sub == "stash" and args[:1] and args[0] in ("drop", "clear"):
        return "git stash drop/clear deletes saved work."
    if sub == "worktree" and args[:1] == ["remove"] and a & {"--force", "-f"}:
        return "git worktree remove --force deletes uncommitted work in that worktree."
    if sub in ("filter-branch", "filter-repo"):
        return f"git {sub} rewrites the whole history."
    if sub == "update-ref" and "-d" in a:
        return "git update-ref -d deletes a ref."
    if sub == "reflog" and args[:1] == ["expire"]:
        return "git reflog expire removes the safety net for lost commits."
    if sub == "gc" and any(x.startswith("--prune=now") for x in args):
        return "git gc --prune=now removes unreachable commits for good."
    return None


def check_find(toks):
    if "-delete" in toks:
        roots = [t for t in toks[1:] if not t.startswith("-") and t not in ("(", ")", "!")][:1]
        if roots and is_throwaway(roots[0]):
            return None
        return "find -delete removes files in bulk."
    if "-exec" in toks or "-execdir" in toks:
        j = toks.index("-exec") if "-exec" in toks else toks.index("-execdir")
        if j + 1 < len(toks) and os.path.basename(toks[j + 1]) in ("rm", "shred", "unlink"):
            roots = [t for t in toks[1:j] if not t.startswith("-")][:1]
            if roots and is_throwaway(roots[0]):
                return None
            return "find -exec rm removes files in bulk."
    return None


def check_segment(seg, depth=0):
    seg = seg.strip()
    if not seg:
        return None
    # command substitution and subshells: check their insides too
    for inner in re.findall(r"\$\(([^()]*)\)|`([^`]*)`", seg):
        r = check_line("".join(inner), depth + 1)
        if r:
            return r
    toks = tokens(seg)
    if not toks:
        return None
    cmd = os.path.basename(toks[0])
    low = seg.lower()

    if cmd in SHELLS and "-c" in toks:
        j = toks.index("-c")
        if j + 1 < len(toks):
            return check_line(toks[j + 1], depth + 1)
    if cmd == "eval":
        return check_line(" ".join(toks[1:]), depth + 1)
    if cmd == "xargs":
        rest = [t for t in toks[1:] if not t.startswith("-")]
        if rest and os.path.basename(rest[0]) in ("rm", "shred", "unlink", "git"):
            sub = [os.path.basename(rest[0])] + rest[1:]
            if sub[0] in ("rm", "shred", "unlink"):
                return "xargs rm deletes a computed list of files."
            return check_git(sub)
        return None

    if cmd == "rm":
        return check_rm(toks)
    if cmd in ("shred", "srm"):
        return f"{cmd} destroys files beyond recovery."
    if cmd == "git":
        return check_git(toks)
    if cmd == "find":
        return check_find(toks)
    if cmd in ("psql", "mysql", "mariadb", "sqlite3", "supabase", "pg_dump", "dropdb", "dropuser"):
        if cmd in ("dropdb", "dropuser"):
            return f"{cmd} deletes a database object."
        if any(SQL_DESTRUCTIVE_RE.search(t) for t in toks) or SQL_DESTRUCTIVE_RE.search(seg):
            return "Destructive SQL (DROP / TRUNCATE / DELETE or UPDATE without WHERE)."
        if cmd == "supabase" and re.search(r"\bdb\s+reset\b", low):
            return "supabase db reset wipes the database."
        return None
    if cmd.startswith("mkfs") or cmd in ("fdisk", "newfs_hfs", "newfs_apfs"):
        return f"{cmd} formats a disk."
    if cmd == "diskutil" and re.search(r"\b(erase\w*|zerodisk|secureerase|partitiondisk|reformat)\b", low):
        return "diskutil erase/partition wipes a disk."
    if cmd == "dd" and re.search(r"\bof=/dev/", seg):
        return "dd to a device overwrites a disk."
    if re.search(r">\s*/dev/(?:disk|sd|nvme|rdisk)", seg):
        return "Redirect into a raw disk device."
    if cmd in ("chmod", "chown") and any(t in ("-R", "-r") for t in toks):
        targets = [t for t in toks[1:] if not t.startswith("-")][1:]
        if any(t in ("/", "~", "$HOME", "/Users", "/System", "/usr", "/etc") or t.startswith("/System") for t in targets):
            return f"Recursive {cmd} on a system or home root."
    if cmd in ("shutdown", "reboot", "halt", "poweroff"):
        return f"{cmd} stops the machine."
    if cmd in ("killall", "pkill") and re.search(r"chrome", low):
        return "Killing Chrome is forbidden (memory rule never-kill-chrome-processes)."
    if cmd == "kill" and re.search(r"chrome", low):
        return "Killing Chrome is forbidden (memory rule never-kill-chrome-processes)."
    if cmd == "launchctl" and re.search(r"\b(remove|bootout|unload)\b", low):
        return "launchctl remove/bootout/unload stops system or user services."
    if cmd == "crontab" and "-r" in toks:
        return "crontab -r deletes every scheduled job."
    return None


def check_line(line, depth=0):
    if depth > 4 or not line:
        return None
    if re.search(r":\(\)\s*\{\s*:\s*\|\s*:\s*&\s*\}\s*;\s*:", line):
        return "Fork bomb."
    if re.search(r"\b(?:curl|wget)\b[^|;&]*\|\s*(?:sudo\s+)?(?:ba|z|da|k)?sh\b", line):
        return "Piping a download straight into a shell runs unreviewed code."
    line = strip_heredocs(line)
    for seg in split_segments(line):
        r = check_segment(seg, depth)
        if r:
            return r
    return None


def main():
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return 0
    tool = data.get("tool_name", "")
    inp = data.get("tool_input", {}) or {}
    session = data.get("session_id", "")

    reason = None
    if tool == "Bash":
        reason = check_line(inp.get("command", ""))
    elif re.search(r"__(?:execute_sql|apply_migration)$", tool):
        sql = inp.get("query", "") or inp.get("sql", "") or json.dumps(inp)
        if SQL_DESTRUCTIVE_RE.search(sql):
            reason = "Destructive SQL (DROP / TRUNCATE / DELETE or UPDATE without WHERE) on Supabase."
    if not reason:
        return 0
    if _go.active_go(session) is not None:
        return 0  # the lead holds Martin's go for this turn
    return deny(reason)


if __name__ == "__main__":
    sys.exit(main())
