#!/bin/bash
# 741-agents-01 — runbook phase 2 (base setup). Run as root over SSH:
#   ssh 741-agents-01 'bash -s' < reporting/night-shift-v2/server/setup-phase2.sh
# Idempotent. No secrets, no repo clone, nothing scheduled. Public SSH stays open
# (key only) until Tailscale is joined; then setup-tailscale step closes port 22.
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive
log(){ echo "== $*"; }

log "1 packages"
apt-get update -qq
apt-get -y -qq upgrade
apt-get -y -qq install ufw unattended-upgrades fail2ban git python3 python3-venv python3-pip curl jq unzip ca-certificates gnupg

log "2 time zone"
timedatectl set-timezone Asia/Makassar

log "3 automatic security updates"
dpkg-reconfigure -f noninteractive unattended-upgrades
systemctl enable --now unattended-upgrades

log "4 SSH: keys only"
cat > /etc/ssh/sshd_config.d/10-741.conf <<'EOF'
PasswordAuthentication no
KbdInteractiveAuthentication no
PermitRootLogin prohibit-password
EOF
systemctl try-reload-or-restart ssh.service 2>/dev/null || systemctl try-reload-or-restart ssh 2>/dev/null || true

log "5 firewall: deny inbound except SSH"
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
ufw --force enable
systemctl enable --now fail2ban

log "6 swap 4G"
if ! swapon --show | grep -q /swapfile; then
  fallocate -l 4G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
  grep -q /swapfile /etc/fstab || echo '/swapfile none swap sw 0 0' >> /etc/fstab
fi

log "7 user nightshift (no sudo)"
id nightshift >/dev/null 2>&1 || useradd -m -s /bin/bash nightshift
deluser nightshift sudo >/dev/null 2>&1 || true

log "8 Node 22 LTS"
if ! command -v node >/dev/null || ! node -v | grep -q '^v22'; then
  curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
  apt-get -y -qq install nodejs
fi

log "9 Playwright system deps for Chromium"
npx -y playwright@1.63.0 install-deps chromium

log "10 Claude Code + Chromium for user nightshift"
sudo -iu nightshift bash -lc 'curl -fsSL https://claude.ai/install.sh | bash'
sudo -iu nightshift bash -lc 'npx -y playwright@1.63.0 install chromium'

log "11 verify"
echo "os:      $(grep PRETTY /etc/os-release | cut -d= -f2)"
echo "arch:    $(uname -m)  tz: $(timedatectl show -p Timezone --value)"
echo "node:    $(node -v)  python: $(python3 --version)"
echo "claude:  $(sudo -iu nightshift bash -lc '~/.local/bin/claude --version' 2>&1 | tail -1)"
echo "chromium:$(sudo -iu nightshift bash -lc 'ls ~/.cache/ms-playwright 2>/dev/null | tr "\n" " "')"
ufw status | head -5
echo "sshd:    $(sshd -T 2>/dev/null | grep -E '^(passwordauthentication|permitrootlogin)' | tr '\n' ' ')"
echo "unattended-upgrades: $(systemctl is-active unattended-upgrades)  fail2ban: $(systemctl is-active fail2ban)"
log "done"
