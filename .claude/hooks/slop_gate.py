#!/usr/bin/env python3
"""Stop: run the AI-slop check on every ```text block of the last reply.

```text blocks are messages for sending (HARD RULE). Each block must score 5/5.
German -> 00_project/content-writing-skill/scripts/deslop_de.py
English -> .claude/skills/slopmonster/tools/deslop.py
Blocks the stop once with the findings. On the retry (stop_hook_active) it only
warns, so a regex false positive can never trap Claude in a loop.
"""
import json
import os
import re
import subprocess
import sys

BLOCK_RE = re.compile(r"```text[^\n]*\n(.*?)```", re.DOTALL)
DE_HINT = re.compile(r"\b(?:und|der|die|das|ich|du|nicht|ist|mit|für|auf|dein|deine|wir|eine?)\b|[äöüß]", re.IGNORECASE)
EN_HINT = re.compile(r"\b(?:the|and|you|your|is|with|for|this|that|we|our|are)\b", re.IGNORECASE)


def last_reply_text(transcript_path):
    """Text of all assistant entries after the last real user prompt."""
    texts = []
    try:
        with open(transcript_path, encoding="utf-8") as f:
            lines = f.readlines()
    except OSError:
        return ""
    for line in lines:
        try:
            e = json.loads(line)
        except ValueError:
            continue
        msg = e.get("message") or {}
        content = msg.get("content")
        if e.get("type") == "user":
            is_prompt = isinstance(content, str) or (
                isinstance(content, list) and any(c.get("type") == "text" for c in content if isinstance(c, dict)))
            if is_prompt:
                texts = []
        elif e.get("type") == "assistant" and isinstance(content, list):
            texts += [c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text"]
    return "\n".join(texts)


def check(block, root):
    de = len(DE_HINT.findall(block)) >= len(EN_HINT.findall(block))
    if de:
        cmd = ["python3", os.path.join(root, "00_project/content-writing-skill/scripts/deslop_de.py"), "--text", block]
    else:
        cmd = ["python3", os.path.join(root, ".claude/skills/slopmonster/tools/deslop.py"), "--text", block]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=4)
    except (subprocess.TimeoutExpired, OSError) as exc:
        return True, f"slop check not run ({exc})"  # never block on tool failure
    m = re.search(r"score\s+(\d)/5", r.stdout)
    score = int(m.group(1)) if m else None
    return score == 5, r.stdout.strip()[-1200:]


def main():
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return 0
    root = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
    text = data.get("last_assistant_message") or last_reply_text(data.get("transcript_path", ""))
    blocks = [b.strip() for b in BLOCK_RE.findall(text or "") if b.strip()]
    if not blocks:
        return 0
    fails = []
    for i, b in enumerate(blocks, 1):
        ok, report = check(b, root)
        if not ok:
            fails.append(f"--- text block {i} ---\n{report}")
    if not fails:
        return 0
    reason = ("[741 slop-gate] A ```text block is below 5/5. Rewrite it, cleanse it with "
              ".claude/skills/slopmonster/tools/cleanse.sh, lint again, then show the full message.\n"
              + "\n".join(fails))
    if data.get("stop_hook_active"):
        print(json.dumps({"systemMessage": "[741 slop-gate] Still below 5/5 after one retry:\n" + "\n".join(fails)}))
        return 0
    print(json.dumps({"decision": "block", "reason": reason}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
