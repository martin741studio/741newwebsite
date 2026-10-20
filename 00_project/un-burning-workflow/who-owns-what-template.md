# Who-owns-what — table template

> **Onboarding artefact, not part of Un-Burning** (Martin, 2026-10-11). Ownership and access are settled with the client at the start. Un-Burning only reads the result as a precondition (`preconditions.json`). Nothing in this file becomes a harm item, a light or a bedrock criterion.


Status: TEMPLATE. Rule: the client owns 100 percent of every asset. 741 is admin. Contract wording is for Martin or his lawyer.
Rule: an owner is never guessed. If the owner cannot be proven, the status is `unconfirmed` or `unknown`.
Machine form: `who-owns-what.json` per client (referenced from `preconditions.json`).

## Status values

| Status | Light | Meaning |
| --- | --- | --- |
| `owned` | green | The client is owner. Proof saved (screenshot, whois, role export) |
| `unconfirmed` | yellow | Probably the client, but no proof yet |
| `third_party` | red | Someone else owns it (former agency, freelancer, ex-employee) |
| `unknown` | grey | Not checked yet or needs a browser read |

## Table

| Asset | Where to check | Expected owner | Owner found | 741 role | Status | Evidence | Access request (client approves) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Domain (registrar) | Whois or RDAP, registrar login | Client | | contact or none | | whois text | Client confirms in the registrar. Transfer only with written approval |
| DNS | `dig`, registrar panel | Client | | none | | dig output | Client holds the registrar login |
| Hosting | Hosting panel, headers | Client | | admin user | | screenshot | Client creates a second user for 741 |
| CMS (WordPress) | User list | Client | | admin or editor | | user list | Client approves the 741 user. Old agency users are removed after a go |
| Google Business Profile | Profile settings, managers | Client (primary owner) | | manager | | screenshot | Client is primary owner. 741 is manager |
| Google Analytics 4 | Access management | Client | | administrator or viewer | | role export | Client is administrator |
| Search Console | Users and permissions | Client | | full user | | screenshot | Client is verified owner |
| Tag Manager | Account users | Client | | publisher | | screenshot | Client is account admin |
| Google Ads | Account access | Client | | standard | | screenshot | Client is admin |
| Social: Instagram | Page settings | Client | | none or editor | | screenshot | Client confirms the handle |
| Social: Facebook | Page roles | Client | | editor | | screenshot | Client is admin |
| Listing: `<directory>` | Listing page | Client | | none | | listing URL | Claim with the client's data, or correction request |

## Rules for the finding column

- Registrant data may be hidden for privacy. Then write `unconfirmed` and ask the client for a screenshot of the registrar panel.
- A role seen only through the service account (read access) is `verified` for that role only. It does not prove ownership.
- Old logins found in the client's vault go to `client_credentials`, never into this table.

## Example row (JSON)

```json
{
  "asset": "gbp",
  "owner_expected": "client",
  "owner_found": "unknown",
  "role_741": "manager",
  "status": "unknown",
  "evidence_ids": [],
  "access_request": "Client opens Profile settings, Managers, and sends a screenshot showing the primary owner.",
  "checked_at": null
}
```
