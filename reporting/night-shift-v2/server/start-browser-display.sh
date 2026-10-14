#!/bin/bash
# 741-agents-01 — persistent visible browser layer.
# Starts (idempotent): Xvfb virtual display :1 (1440x900) -> fluxbox window manager
# -> x11vnc sharing that display -> websockify/noVNC serving a browser-viewable
# page on 127.0.0.1:6080 (reachable only over Tailscale via an SSH/port setup,
# never bound to a public interface).
# Run as the nightshift user. Safe to re-run; skips what's already running.
set -u
DISPLAY_NUM=1
export DISPLAY=:${DISPLAY_NUM}
RUNDIR="$HOME/.browser-display"
mkdir -p "$RUNDIR"

pidfile() { echo "$RUNDIR/$1.pid"; }
running() { [ -f "$(pidfile "$1")" ] && kill -0 "$(cat "$(pidfile "$1")")" 2>/dev/null; }

if ! running xvfb; then
  Xvfb :${DISPLAY_NUM} -screen 0 1440x900x24 -nolisten tcp >"$RUNDIR/xvfb.log" 2>&1 &
  echo $! > "$(pidfile xvfb)"
  sleep 1
fi

if ! running fluxbox; then
  DISPLAY=:${DISPLAY_NUM} fluxbox >"$RUNDIR/fluxbox.log" 2>&1 &
  echo $! > "$(pidfile fluxbox)"
  sleep 1
fi

if ! running x11vnc; then
  x11vnc -display :${DISPLAY_NUM} -forever -shared -nopw -rfbport 5901 -localhost \
    >"$RUNDIR/x11vnc.log" 2>&1 &
  echo $! > "$(pidfile x11vnc)"
  sleep 1
fi

if ! running websockify; then
  websockify --web=/usr/share/novnc 6080 localhost:5901 >"$RUNDIR/novnc.log" 2>&1 &
  echo $! > "$(pidfile websockify)"
fi

sleep 1
echo "xvfb:$(running xvfb && echo up || echo down) fluxbox:$(running fluxbox && echo up || echo down) x11vnc:$(running x11vnc && echo up || echo down) novnc:$(running websockify && echo up || echo down)"
