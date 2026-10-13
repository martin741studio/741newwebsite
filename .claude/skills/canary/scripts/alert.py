#!/usr/bin/env python3
"""Send a canary alert to Telegram with an acknowledge button, then wait and escalate.

Channel: Telegram bot "741 Canary" (@canary741_alerts_bot), token in
.secrets/canary-telegram.env (TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID_MARTIN).
Built and proven in the hand-run 2026-10-14 (workflow-builds/canary/hand-run.md).

Usage:
  python3 alert.py send --severity SEV1 --client "Marcel Rosenbach" \
      --what "Zap-Fehler" --since "2026-10-14 06:31" --impact "..." \
      --fix "..." [--check-id marcel-gewinnspiel-zaperror] \
      [--escalate-after-min 10] [--group-chat-id <id>]

Prints the sent timestamp and message_id. Logs to 00_project/canary/state/alerts.log.
Exits 0 once acknowledged, 3 if the escalate-after window passed with no ack (caller
decides what to do next — this script does not loop forever).
"""
import argparse, json, time, sys, datetime, urllib.request, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ENV = ROOT / ".secrets" / "canary-telegram.env"
LOG = ROOT / "00_project" / "canary" / "state" / "alerts.log"
WITA = datetime.timezone(datetime.timedelta(hours=8))


def env():
    if not ENV.exists():
        print(f"FAIL no {ENV} — Martin must create the 741 Canary bot token first "
              f"(see workflow-builds/canary/hand-run.md, round 4).")
        sys.exit(2)
    return dict(l.strip().split("=", 1) for l in ENV.read_text().splitlines() if "=" in l)


def call(token, method, **params):
    api = f"https://api.telegram.org/bot{token}/{method}"
    data = urllib.parse.urlencode(
        {k: (json.dumps(v) if isinstance(v, (dict, list)) else v) for k, v in params.items()}
    ).encode()
    with urllib.request.urlopen(api, data=data, timeout=40) as r:
        return json.load(r)


def log_line(line):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


def send(args):
    e = env()
    token = e["TELEGRAM_BOT_TOKEN"]
    chat = args.group_chat_id or e["TELEGRAM_CHAT_ID_MARTIN"]
    header = f"🔴 CANARY {args.severity} · {args.client} · {args.what}"
    text = (f"{header}\n"
            f"Seit: {args.since}\n"
            f"Wirkung: {args.impact}\n"
            f"Agent: {args.fix}\n\n"
            f"Nächster Schritt: Canary-Chat öffnen, Diagnose läuft. Nichts an den Kunden senden.")
    ack_data = f"ack:{args.check_id or 'unknown'}:{int(time.time())}"
    sent = call(token, "sendMessage", chat_id=chat, text=text,
                reply_markup={"inline_keyboard": [[{"text": "✅ Übernommen", "callback_data": ack_data}]]})
    if not sent.get("ok"):
        print("FAIL send:", sent)
        sys.exit(1)
    t0 = time.time()
    mid = sent["result"]["message_id"]
    sent_iso = datetime.datetime.now(WITA).isoformat(timespec="seconds")
    print(f"sent {sent_iso} message_id={mid} chat_id={chat}")
    log_line(f"{sent_iso} SENT check={args.check_id} severity={args.severity} chat={chat} mid={mid}")

    if args.no_wait:
        return 0

    deadline = t0 + 60 * args.escalate_after_min
    offset = None
    upd = call(token, "getUpdates", offset=-1, timeout=0)
    if upd.get("result"):
        offset = upd["result"][-1]["update_id"] + 1
    while time.time() < deadline:
        r = call(token, "getUpdates", offset=offset, timeout=25,
                  allowed_updates=["callback_query"]) if offset is not None else \
            call(token, "getUpdates", timeout=25, allowed_updates=["callback_query"])
        for u in r.get("result", []):
            offset = u["update_id"] + 1
            cq = u.get("callback_query")
            if cq and cq.get("data") == ack_data:
                dt = time.time() - t0
                call(token, "answerCallbackQuery", callback_query_id=cq["id"], text="Danke – übernommen.")
                call(token, "editMessageReplyMarkup", chat_id=chat, message_id=mid,
                      reply_markup={"inline_keyboard": []})
                ack_iso = datetime.datetime.now(WITA).isoformat(timespec="seconds")
                print(f"ACK {ack_iso} after_s={dt:.0f}")
                log_line(f"{ack_iso} ACK check={args.check_id} after_s={dt:.0f}")
                return 0
    esc_iso = datetime.datetime.now(WITA).isoformat(timespec="seconds")
    print(f"NO_ACK within {args.escalate_after_min} min (as of {esc_iso}) — caller should escalate")
    log_line(f"{esc_iso} NO_ACK check={args.check_id} window_min={args.escalate_after_min}")
    return 3


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("send")
    s.add_argument("--severity", required=True, choices=["SEV1", "SEV2", "SEV3"])
    s.add_argument("--client", required=True)
    s.add_argument("--what", required=True)
    s.add_argument("--since", required=True)
    s.add_argument("--impact", required=True)
    s.add_argument("--fix", required=True, help="what the agent tried or proposes")
    s.add_argument("--check-id")
    s.add_argument("--group-chat-id", help="escalation target (741 Canary group); default is Martin's private chat")
    s.add_argument("--escalate-after-min", type=int, default=10)
    s.add_argument("--no-wait", action="store_true", help="send and exit, do not wait for an ack")
    args = p.parse_args()
    sys.exit(send(args))


if __name__ == "__main__":
    main()
