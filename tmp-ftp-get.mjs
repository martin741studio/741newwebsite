import * as ftp from "basic-ftp";
import dotenv from "dotenv";
dotenv.config({ path: "/Users/martindrendel/741website/.env" });
const [remote, local] = process.argv.slice(2);
const client = new ftp.Client(30000);
try {
  await client.access({ host: process.env.CLIENTS_FTP_HOST, user: process.env.CLIENTS_FTP_USER, password: process.env.CLIENTS_FTP_PASSWORD, secure: false });
  try { await client.cd("public_html"); } catch {}
  await client.downloadTo(local, remote);
  console.log("Downloaded:", remote);
} catch (e) { console.error("FAIL:", e.message); process.exitCode = 1; } finally { client.close(); }
