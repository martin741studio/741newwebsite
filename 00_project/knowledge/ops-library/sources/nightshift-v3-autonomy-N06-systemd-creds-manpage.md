# N06 — systemd-creds(1): encrypted credentials for systemd units, without a human typing a passphrase at boot

- Org/author: systemd project (official man page, mirrored on man7.org)
- Type: official docs, living reference
- Publish date: living/evergreen reference man page; counted as current on fetch date.
- URL: https://man7.org/linux/man-pages/man1/systemd-creds.1.html
- Fetch date: 2026-10-15

## Extract (own words)

- `systemd-creds` encrypts a single credential (API key, token, etc.) so a systemd unit can load it at start time via `LoadCredentialEncrypted=` (file) or `SetCredentialEncrypted=` (literal value in the unit file) — the secret is not stored in the repo or in a plain-text env file.
- Three key modes, which decide who/what can unlock the secret without a human present:
  - **TPM-bound key**: not stored on the host at all; decryption is only possible with access to the original TPM2 chip — i.e. the secret is bound to that one physical machine and survives an unattended reboot with no human input, but cannot be copied to another box.
  - **Host-file key**: stored on the host filesystem; decryption needs filesystem access and sufficient privilege — portable across reboots with no human input, but anyone with root on that host can decrypt it.
  - **Mixed (default)**: requires both the TPM2 chip and the host OS installation.
- This solves exactly the "unlock secrets with nobody there to type a passphrase" problem for a single host, at the cost of no audit trail, no rotation mechanism, and no central policy — those need a separate layer (e.g. a secrets server) if ever required.

## IF/THEN rules for 741

1. IF 741-agents-01's current secret handling (`.secrets/` + `.env` copied as 600-mode files, per decisions.md's "autonomous prep round") needs to survive an unattended reboot with zero human input and zero plaintext-on-disk exposure, THEN `systemd-creds` with a TPM-bound key (if the Hetzner CAX31's virtualised hardware exposes a vTPM) or a host-file key is the direct upgrade path — it keeps the "no login needed" property decisions.md already committed to, while removing the secrets from sitting as plain 600-mode files.
2. IF 741 ever needs audit logs or per-agent rotation policy for secrets (not just "keep them off disk in plaintext"), THEN `systemd-creds` alone will not provide that — it is a single-host credential loader, not a secrets management system; that would need a heavier tool (e.g. Vault) only if the number of agents/hosts grows past what one operator can track by hand.
3. IF Martin wants the simplest fix that doesn't change the current architecture, THEN leave `.secrets/` as 600-mode plaintext files for now (today's acceptable-risk choice per decisions.md) and treat `systemd-creds` as the specific next step only if a real incident (stolen disk image, unauthorized local user) makes that risk concrete — don't build it pre-emptively against a threat model 741 doesn't have yet (single operator, single trusted host, Tailscale-only access already closes the main remote attack surface).

## Caveats

- Whether the Hetzner CAX31 ARM instance exposes a usable vTPM for the TPM-bound mode was not checked in this research pass — that is a prerequisite to confirm before recommending it over the host-file key mode.
- This source is a man page, not a 2026-dated article; included because it is the primary technical reference for the mechanism and because living official references are treated as current per this library's existing convention.
