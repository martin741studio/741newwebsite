#!/usr/bin/env python3
"""PreToolUse: block live website writes and settings edits without a go.

Guards:
  1. FTP deploys of 741.studio (upload*.js/mjs, ftp-delete-old, npm run deploy,
     lftp, curl -T / --upload-file / ftp://, sftp).
  2. Novamira (WordPress) write abilities, incl. execute-php with write calls.
  3. Porkbun hosting writes (deploy_site, hosting files).
  4. Config protection: settings*.json, .claude/hooks/ (needs a go);
     .claude/go/ (always blocked: only go_marker.py writes it).
Unknown novamira abilities get "ask", not "deny" (regex can be wrong there).
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _go  # noqa: E402

FTP_RE = re.compile(
    r"\b(?:node|bun)\s+\S*(?:upload(?:_one|_only)?\.m?js|ftp-delete-old\.mjs)\b"
    r"|\bnpm\s+run\s+deploy\b"
    r"|\blftp\b|\bsftp\b|(?<![\w-])ftp\s+\S"
    r"|\bcurl\b[^|;&]*(?:\s-T\s|\s--upload-file\b|ftps?://)",
    re.IGNORECASE,
)

NOVA_TOOL_RE = re.compile(r"^mcp__novamira-[^_]+(?:_[^_]+)*__mcp-adapter-execute-ability$")
NOVA_READ_RE = re.compile(r"(?:^|[/-])(?:get|list|read|discover|search|find|info|status|check)(?:[/-]|$)")
PHP_WRITE_RE = re.compile(
    r"\b(?:wp_(?:update|insert|delete|trash)_\w+|update_(?:option|post_meta|user_meta|term_meta|field)"
    r"|add_(?:option|post_meta)|delete_(?:option|post_meta|transient)|set_theme_mod|remove_theme_mod"
    r"|file_put_contents|fwrite|unlink|rename|copy|mkdir|rmdir|wp_set_\w+|switch_theme|activate_plugin"
    r"|deactivate_plugins|update_post_cache|wp_cache_flush)\s*\("
    r"|\$wpdb\s*->\s*(?:update|insert|delete|replace|query)\s*\("
    r"|->\s*(?:save|update|delete)\s*\(",
    re.IGNORECASE,
)
PORKBUN_WRITE_RE = re.compile(r"^mcp__Porkbun__(?:deploy_site|delete_hosting(?:_file)?|create_hosting|make_hosting_dir)$")

PROTECTED_RE = re.compile(r"""(?:^|[/\s"'=])\.claude/(?:settings(?:\.local)?\.json|hooks/)""")
GO_DIR_RE = re.compile(r"""(?:^|[/\s"'=])\.claude/go(?:/|\s|$)""")
BASH_WRITE_RE = re.compile(r"(?:>>?|\btee\b|\bsed\s+-i|\bcp\b|\bmv\b|\brm\b|\btouch\b|\bln\b|\bchmod\b|python3?\s+-c|perl\s+-[pi])")


def out(decision, reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": reason,
    }}))
    return 0


def needs_go(session, what):
    go = _go.active_go(session)
    if go is not None:
        return 0  # allowed: the prompt of this turn holds a go
    return out("deny",
               f"[741 go-gate] {what} needs Martin's explicit go for exactly this change. "
               "Show the planned change and ask for the go. Do not retry another way.")


def main():
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return 0
    tool = data.get("tool_name", "")
    inp = data.get("tool_input", {}) or {}
    session = data.get("session_id", "")

    if tool == "Bash":
        cmd = inp.get("command", "")
        writes = BASH_WRITE_RE.search(cmd)
        if GO_DIR_RE.search(cmd) and writes:
            return out("deny", "[741 go-gate] .claude/go/ holds go markers. Only Martin's prompt sets them.")
        if PROTECTED_RE.search(cmd) and writes:
            return needs_go(session, "A write to Claude Code settings or hooks")
        if FTP_RE.search(cmd):
            return needs_go(session, "An FTP deploy to the live server")
        return 0

    if tool in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
        path = inp.get("file_path", "") or inp.get("notebook_path", "")
        if GO_DIR_RE.search(path):
            return out("deny", "[741 go-gate] .claude/go/ holds go markers. Only Martin's prompt sets them.")
        if PROTECTED_RE.search(path) or path.endswith("/.claude/settings.json"):
            return needs_go(session, f"An edit of {os.path.basename(path)} (settings/hooks)")
        return 0

    if NOVA_TOOL_RE.match(tool):
        ability = str(inp.get("ability_name", ""))
        if ability == "novamira/execute-php":
            code = json.dumps(inp.get("parameters", {}))
            if PHP_WRITE_RE.search(code):
                return needs_go(session, "PHP with write calls on a live WordPress site")
            return 0
        if NOVA_READ_RE.search(ability):
            return 0
        if _go.active_go(session) is not None:
            return 0
        if re.search(r"(?:write|edit|update|create|delete|insert|upload|set|save|publish|trash|activate|install)", ability):
            return needs_go(session, f"Novamira ability {ability}")
        return out("ask", f"[741 go-gate] Unknown Novamira ability {ability}. It can change the live site.")

    if PORKBUN_WRITE_RE.match(tool):
        return needs_go(session, f"Porkbun hosting write ({tool.split('__')[-1]})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
