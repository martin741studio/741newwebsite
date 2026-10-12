#!/usr/bin/env python3
"""UserPromptSubmit: set the go marker when the prompt has a go, clear it otherwise."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _go  # noqa: E402


def main():
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return 0
    session = data.get("session_id", "")
    prompt = data.get("prompt", "")
    if _go.has_go(prompt):
        _go.write_marker(session, prompt)
        # stdout of UserPromptSubmit becomes context for Claude.
        print("[741 go-gate] Go marker set for this turn only. "
              "It covers the change named in this prompt, nothing else.")
    else:
        _go.clear_marker(session)
    return 0


if __name__ == "__main__":
    sys.exit(main())
