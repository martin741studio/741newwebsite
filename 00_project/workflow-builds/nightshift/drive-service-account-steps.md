> **RETIRED 14.10. — do not do this.** The Drive connector from the full Claude Code login already works, verified with a real file create + read. See decisions.md "Drive verified working". Kept only for reference.
# Drive service account — your steps (reuses the existing GCP project)

There's already a 741 GCP project with a reporting service account (`reporting-bot@studio-apis-503306.iam.gserviceaccount.com`, used for GA4/GSC reads). We add a second, separate service account in the SAME project, scoped to Drive only — keeps read-only reporting and write-capable Drive access cleanly separated.

1. console.cloud.google.com — make sure you're on **741studio18@gmail.com** (the project owner), not your personal account.
2. Top bar → select project **"741 Studio APIs"** (`studio-apis-503306`).
3. "APIs & Services" → "Library" → search **Google Drive API** → Enable.
4. "IAM & Admin" → "Service Accounts" → "Create Service Account" → name `drive-agent` → Create and Continue → skip roles (none needed at project level) → Done.
5. Click the new `drive-agent@studio-apis-503306.iam.gserviceaccount.com` → "Keys" tab → "Add Key" → "Create new key" → JSON → downloads to your Mac.
6. In Google Drive: open each client/deliverable folder this should reach (e.g. `Local SEO/<Client>/`) → Share → paste `drive-agent@studio-apis-503306.iam.gserviceaccount.com` → role **Editor** → Send (no notification needed).
7. **Don't paste the key file content to me.** Put the JSON file onto the server yourself:
```bash
scp ~/Downloads/studio-apis-503306-*.json 741-agents-01:/home/nightshift/.secrets-drive-key.json
```
   Tell me when it's there — I'll set permissions and wire it in.

Step 6 can be repeated any time for a new client folder, no re-setup needed.
