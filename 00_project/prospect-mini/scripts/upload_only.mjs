// Upload only selected dist/ paths (files or folders) via the same FTP account as upload.js.
// Usage (from repo root): node 00_project/prospect-mini/scripts/upload_only.mjs review/catja-grieshaber-v2 review-assets/martin-guide ...
// Updates .deploy-manifest.json only for the uploaded files.
import fs from "fs";
import path from "path";
import crypto from "crypto";
import { createRequire } from "module";
const require = createRequire(path.resolve("package.json"));
const ftp = require("basic-ftp");
require("dotenv").config({ path: path.resolve(".env") });

const DIST = path.resolve("dist");
const MANIFEST = path.resolve(".deploy-manifest.json");
const walk = (p) => fs.statSync(p).isDirectory() ? fs.readdirSync(p).flatMap((n) => walk(path.join(p, n))) : [p];
const files = process.argv.slice(2).flatMap((r) => walk(path.join(DIST, r))).map((f) => path.relative(DIST, f).split(path.sep).join("/"));

const client = new ftp.Client(120000);
await client.access({ host: process.env.FTP_HOST || "ftp.741.studio", user: process.env.FTP_USER || "agent_deploy@741.studio", password: process.env.FTP_PASSWORD, secure: false });
// web root = FTP root (a stray public_html folder exists inside it; do not cd into it)
const base = await client.pwd();
const man = fs.existsSync(MANIFEST) ? JSON.parse(fs.readFileSync(MANIFEST, "utf8")) : {};
for (const rel of files) {
  await client.cd(base);
  const dir = path.posix.dirname(rel);
  if (dir !== ".") { await client.ensureDir(dir); await client.cd(base); }
  await client.uploadFrom(path.join(DIST, rel), rel);
  const size = await client.size(rel).catch(() => -1);
  man[rel] = crypto.createHash("sha1").update(fs.readFileSync(path.join(DIST, rel))).digest("hex");
  console.log("↑", rel, "remote size", size);
}
client.close();
fs.writeFileSync(MANIFEST, JSON.stringify(man));
console.log("done", files.length, "files");
