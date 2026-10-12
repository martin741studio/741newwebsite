"""Shared go-marker logic for the 741 hooks.

A "go" is valid only for the turn that answers the prompt that contained it.
go_marker.py (UserPromptSubmit) writes the marker when Martin's prompt has a go
and deletes it on every prompt without one. One go never carries into the next change.
"""
import json
import os
import re
import time

TTL_SECONDS = 30 * 60  # a go older than 30 min is stale even inside one turn

# Standalone "go" (not "go through", "go back" ...), or explicit live/deploy orders.
GO_RE = re.compile(
    r"(?<![\w-])go(?![\w-])(?!\s+(?:through|back|over|on|to|ahead\s+and\s+check|into)\b)"
    r"|\bmach(?:e|t)?\s+(?:es\s+)?live\b|\bdeploy\s+(?:jetzt|now)\b|\bjetzt\s+live\b",
    re.IGNORECASE,
)


def project_dir():
    return os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()


def marker_path(session_id):
    safe = re.sub(r"[^A-Za-z0-9_-]", "_", session_id or "nosession")
    return os.path.join(project_dir(), ".claude", "go", f"{safe}.json")


def has_go(prompt):
    return bool(GO_RE.search(prompt or ""))


def write_marker(session_id, prompt):
    path = marker_path(session_id)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"ts": time.time(), "prompt": (prompt or "")[:300]}, f, ensure_ascii=False)


def clear_marker(session_id):
    try:
        os.remove(marker_path(session_id))
    except FileNotFoundError:
        pass


def active_go(session_id):
    """Return the go prompt excerpt if a fresh marker exists, else None."""
    try:
        with open(marker_path(session_id), encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, ValueError):
        return None
    if time.time() - data.get("ts", 0) > TTL_SECONDS:
        return None
    return data.get("prompt", "")
