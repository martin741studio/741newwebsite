// Minimal single-file FTP upload — used when the full deploy's assets transfer
// times out the control socket. Uploads just the files passed as CLI args
// (paths relative to dist/), e.g.: node upload_one.js pages/home-v2.html
import * as ftp from "basic-ftp";
import path from "path";
import fs from "fs";
import dotenv from "dotenv";
dotenv.config();

const DIST = "/Users/martindrendel/741website/dist";
const files = process.argv.slice(2);
if (!files.length) { console.error("Usage: node upload_one.js <path-relative-to-dist> ..."); process.exit(1); }

async function run() {
  const client = new ftp.Client(30000);
  client.ftp.verbose = false;
  try {
    await client.access({
      host: process.env.FTP_HOST || "ftp.741.studio",
      user: process.env.FTP_USER || "agent_deploy@741.studio",
      password: process.env.FTP_PASSWORD,
      secure: false,
    });
    try { await client.cd("public_html"); } catch { /* already chrooted */ }
    const base = await client.pwd(); // remember root so each file starts from here
    for (const rel of files) {
      const local = path.join(DIST, rel);
      if (!fs.existsSync(local)) { console.warn("skip (missing):", rel); continue; }
      await client.cd(base); // reset to root before every file (ensureDir cd's into dirs)
      const dir = path.dirname(rel);
      if (dir && dir !== ".") await client.ensureDir(dir); // cd's into dir
      await client.uploadFrom(local, path.basename(rel));
      console.log("Uploaded:", rel);
    }
    console.log("Done.");
  } catch (err) {
    console.error("Failed:", err.message);
    process.exitCode = 1;
  } finally {
    client.close();
  }
}
run();
