import * as ftp from "basic-ftp";
import fs from "fs";
import path from "path";
import crypto from "crypto";
import dotenv from "dotenv";

dotenv.config();

/**
 * Incremental FTP deploy for 741.Studio.
 *
 * Mirrors dist/ -> public_html/ but only uploads files whose content changed
 * since the last successful deploy. A local manifest (.deploy-manifest.json,
 * git-ignored) stores a SHA-1 per file. This avoids re-uploading the whole
 * (large) assets/ folder every time, which previously caused FTP timeouts.
 *
 *   npm run deploy          -> upload only changed/new files
 *   npm run deploy -- --full -> ignore manifest, upload everything
 *
 * Notes:
 * - Vite content-hashes asset filenames, so unchanged assets keep the same name
 *   and are skipped. Changed source produces new content -> re-uploaded.
 * - Remote files are never deleted (safe). Orphaned old hashed assets may
 *   linger; run with --full occasionally if you want to be thorough.
 */

const DIST = path.resolve("dist");
const MANIFEST = path.resolve(".deploy-manifest.json");
const FORCE_FULL = process.argv.includes("--full") || process.env.FORCE_FULL === "true";

function walk(dir, base = dir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, base, out);
    else if (entry.isFile()) out.push(path.relative(base, full));
  }
  return out;
}

function sha1(file) {
  return crypto.createHash("sha1").update(fs.readFileSync(file)).digest("hex");
}

async function connect() {
  const client = new ftp.Client(120000); // 120s per-operation timeout
  client.ftp.verbose = false;
  await client.access({
    host: process.env.FTP_HOST || "ftp.741.studio",
    user: process.env.FTP_USER || "agent_deploy@741.studio",
    password: process.env.FTP_PASSWORD,
    secure: false,
  });
  // The deploy user may or may not be chrooted to public_html.
  try { await client.cd("public_html"); } catch { /* already there / chrooted */ }
  const base = await client.pwd();
  return { client, base };
}

async function deploy() {
  console.log("🚀 741.Studio incremental FTP deploy");

  if (!fs.existsSync(DIST)) {
    throw new Error("dist/ not found. Run `npm run build` first.");
  }

  // 1. Hash every file in dist/
  const files = walk(DIST);
  const current = {};
  for (const rel of files) current[rel] = sha1(path.join(DIST, rel));

  // 2. Load previous manifest and diff
  const prev = !FORCE_FULL && fs.existsSync(MANIFEST)
    ? JSON.parse(fs.readFileSync(MANIFEST, "utf8"))
    : {};

  const changed = files.filter((rel) => current[rel] !== prev[rel]);

  console.log(`📦 ${files.length} files in dist, ${changed.length} changed/new${FORCE_FULL ? " (--full)" : ""}.`);

  if (changed.length === 0) {
    console.log("✅ Nothing to upload — live site already up to date.");
    return;
  }

  // 3. Upload changed files, reconnecting on transient failures
  const uploaded = new Set();
  const ensured = new Set();
  let { client, base } = await connect();
  console.log("🔑 Connected. Uploading...");

  try {
    for (const rel of changed) {
      const relPosix = rel.split(path.sep).join("/");
      const dir = path.posix.dirname(relPosix);
      const localAbs = path.join(DIST, rel);

      let ok = false;
      let lastErr;
      for (let attempt = 1; attempt <= 3 && !ok; attempt++) {
        try {
          await client.cd(base);
          if (dir !== "." && !ensured.has(dir)) {
            await client.ensureDir(dir); // creates nested dirs, cds into them
            ensured.add(dir);
            await client.cd(base);
          }
          await client.uploadFrom(localAbs, relPosix);
          ok = true;
        } catch (e) {
          lastErr = e;
          console.warn(`  ⚠︎ ${relPosix} — attempt ${attempt}/3 failed: ${e.message}`);
          try { client.close(); } catch { /* ignore */ }
          ({ client, base } = await connect()); // fresh connection
        }
      }
      if (!ok) throw new Error(`Upload failed permanently: ${relPosix} (${lastErr && lastErr.message})`);

      uploaded.add(rel);
      console.log(`  ↑ ${relPosix}`);
    }
    console.log(`🎉 Deployment complete — ${uploaded.size} file(s) uploaded.`);
  } finally {
    try { client.close(); } catch { /* ignore */ }

    // 4. Persist manifest: record hashes for unchanged + successfully uploaded files.
    //    Files that changed but failed keep their OLD hash so the next run retries them.
    const changedSet = new Set(changed);
    const finalManifest = {};
    for (const rel of files) {
      if (uploaded.has(rel)) finalManifest[rel] = current[rel];
      else if (!changedSet.has(rel)) finalManifest[rel] = current[rel]; // unchanged
      else if (prev[rel] !== undefined) finalManifest[rel] = prev[rel]; // failed -> retry next time
      // new file that failed to upload -> omit so it's treated as new next run
    }
    fs.writeFileSync(MANIFEST, JSON.stringify(finalManifest));
  }
}

deploy().catch((err) => {
  console.error("❌ Deployment failed:", err.message);
  process.exitCode = 1;
});
