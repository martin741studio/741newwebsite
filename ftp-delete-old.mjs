import { Client } from "basic-ftp";
import "dotenv/config";

const TARGET = process.argv[2] || "de/pages/stipendium.html";
const client = new Client();
try {
  await client.access({
    host: process.env.FTP_HOST || "ftp.741.studio",
    user: process.env.FTP_USER || "agent_deploy@741.studio",
    password: process.env.FTP_PASSWORD,
    secure: false,
  });
  try { await client.cd("public_html"); } catch { /* chrooted */ }
  const base = await client.pwd();
  console.log("base:", base, "→ removing:", TARGET);
  try {
    await client.remove(TARGET);
    console.log("✅ deleted", TARGET);
  } catch (e) {
    console.log("⚠︎ remove failed:", e.message);
  }
} finally {
  client.close();
}
