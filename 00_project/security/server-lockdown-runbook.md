# Server lockdown runbook — 2026-10-15

Do the steps in this order. Tell Claude "server locked" after block A.

## A. 741 server (WHM) — do this first, ~15 min

1. Open `https://741.studio:2087` and log in as root.
2. If the login fails: the attacker may have changed it. Then use the hoster's rescue console and reset root there.
3. Change the root password: Home → Server Configuration → **Change Root Password**. Use a new, long password from your password manager.
4. End all sessions: Home → Security Center → **Terminate all active sessions** (or log out all users under "Manage Current Sessions").
5. List accounts: Home → Account Information → **List Accounts**. Write down any account you do not know. Do not delete yet — tell Claude.
6. Change EVERY cPanel account password there (List Accounts → + → Change Password). Also covers FTP main users.
7. FTP extra users: cPanel of 741.studio account → FTP Accounts → change password of **agent_deploy**.
8. Check for foreign access:
   - Home → Security Center → **Manage root's SSH Keys**: remove keys you do not know.
   - Home → Server Contacts + **API Tokens (Manage API Tokens)**: delete tokens you do not know.
   - Home → Account Functions → look for new reseller/admin accounts.
9. Turn on 2FA: Home → Security Center → **Two-Factor Authentication** for root.

## B. Hoster portals — today, ~20 min

| Hoster | Login URL | Covers | Steps |
|---|---|---|---|
| Strato | https://www.strato.de/apps/CustomerService | Tacheles site + Strato webmail | New password, end sessions, 2FA on |
| IONOS account 1 (user kam…/phy…) | https://login.ionos.de | Kamil / Kraft domains | New password, 2FA on |
| IONOS account 2 (user 964…/inf…/616…) | https://login.ionos.de | second account | New password, 2FA on |
| Hetzner | https://accounts.hetzner.com | future night-shift server | New password, 2FA on |
| Hostinger | https://hpanel.hostinger.com | old VPS account | New password, 2FA on |

Also soon (same reason, stolen logins): GoDaddy or your registrar (nameservers of 741.studio, katharinakisser.at, physiotherapieoberhausen.com run over domaincontrol.com), SharePoint/Microsoft (physiotherapiekraft-my.sharepoint.com), janeapp (balihealing.janeapp.com).

## C. After "server locked" — Claude does, with your go per step

1. Scan the Kisser cPanel account, take the site to 403, clean with the Kraft runbook, verify, reopen.
2. Re-scan Kraft and Oberhausen for new backdoors.
3. Rotate WP admin passwords of all client sites, force logouts.
4. Search Console: remove the spam sitemaps for katharinakisser.at.
