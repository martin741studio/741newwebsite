#!/usr/bin/env python3
"""Stop hook (DRAFT, not installed): Martin's pre-send sweep.

Blocks the end of a turn when the final message hands Martin a prose list of open points or his own steps,
or ends with a prose question, instead of AskUserQuestion cards. Uses stop_hook_active so it never loops.
A crash never blocks.
"""
import json, re, sys

HEADING = re.compile(
    r'^\W*(offen(e)?\s+(bei\s+dir|punkte|fragen|go-?punkte|entscheidungen)|'
    r'was\s+(noch\s+)?offen\s+ist|noch\s+offen|'
    r'(deine|dein)\s+(schritte|nächste[rn]?\s+schritt\w*|klicks?)|'
    r'nächste\s+schritte(\s+(für|bei)\s+dir)?|'
    r'open\s+(items|questions|points)|your\s+(steps|next\s+steps))\s*[:\-–]?\s*\**\s*$',
    re.I | re.M)
CLOSING_Q = re.compile(
    r'(soll\s+ich|willst\s+du|möchtest\s+du|magst\s+du|sag\s+(mir|bescheid)|schreib\s+mir|'
    r'should\s+i|do\s+you\s+want|want\s+me\s+to|let\s+me\s+know|wenn\s+du\s+willst)[^\n]*', re.I)
YOU_STEP = re.compile(r'^\s*(\d+[.)]|[-•*])\s+.*\b(du|dein\w*|dir|you|your)\b.*\b(musst|sollst|kannst|klickst|löschst|sendest|'
                      r'schickst|loggst|legst|must|need to|should|click|delete|send|log in)\b', re.I | re.M)
FENCE = re.compile(r'```.*?```', re.S)   # message drafts in ```text blocks are deliverables, not asks


def check(msg):
    body = FENCE.sub(' ', msg or '')
    hits = []
    if HEADING.search(body):
        hits.append('a heading for open points or next steps')
    tail = [l for l in body.strip().splitlines() if l.strip()][-3:]
    if any(CLOSING_Q.search(l) and ('?' in l or re.search(r'sag|schreib|let me know|wenn du willst', l, re.I)) for l in tail):
        hits.append('a closing question or request to Martin in prose')
    if len(YOU_STEP.findall(body)) >= 2:
        hits.append('a list of steps Martin must do')
    return hits


def main():
    try:
        d = json.load(sys.stdin)
    except Exception:
        return
    if d.get('stop_hook_active'):
        return
    hits = check(d.get('last_assistant_message') or '')
    if not hits:
        return
    reason = ('Pre-send sweep (Martin, hard rule): the final message contains ' + '; '.join(hits) + '. '
              'Anything that waits on Martin must be an AskUserQuestion card, one per item (his own steps as '
              '"Your click" cards), and removed from the prose. Report only facts and results in the text. '
              'Call AskUserQuestion now, then finish.')
    print(json.dumps({'decision': 'block', 'reason': reason}))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        pass
