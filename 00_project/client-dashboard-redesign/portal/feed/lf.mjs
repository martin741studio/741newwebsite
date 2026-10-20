// Read-only Local Falcon client over the MCP endpoint. Only tools named list*/get* are allowed.
// Scans (run*, save*, manage*, create*, update*, delete*) are refused here, so the job cannot spend credits.
import { readFileSync } from 'node:fs';

const ROOT = new URL('../../../../', import.meta.url);           // repo root
const envKey = () => {
  const m = readFileSync(new URL('.env', ROOT), 'utf8').match(/^LF_API_KEY=(.*)$/m);
  if (!m) throw new Error('LF_API_KEY not found in .env');
  return m[1].trim().replace(/^["']|["']$/g, '');
};
const K = envKey();
const URL_ = `https://mcp.localfalcon.com/mcp?local_falcon_api_key=${K}`;
const HDR = { Authorization: `Bearer ${K}`, 'Content-Type': 'application/json', Accept: 'application/json, text/event-stream' };
let sid = null, nid = 1;

async function rpc(payload) {
  const h = { ...HDR }; if (sid) h['Mcp-Session-Id'] = sid;
  const r = await fetch(URL_, { method: 'POST', headers: h, body: JSON.stringify(payload) });
  sid = r.headers.get('mcp-session-id') || sid;
  let t = await r.text();
  if (!r.ok) throw new Error(`LF HTTP ${r.status}: ${t.slice(0, 200).replace(K, '***')}`);
  if (/^(event:|data:)/.test(t.trimStart())) t = t.split('\n').filter(l => l.startsWith('data:')).map(l => l.slice(5).trim()).pop();
  return t ? JSON.parse(t) : null;
}
export async function lfInit() {
  await rpc({ jsonrpc: '2.0', id: nid++, method: 'initialize', params: { protocolVersion: '2025-03-26', capabilities: {}, clientInfo: { name: 'dashboard-feed', version: '1.0' } } });
  try { await rpc({ jsonrpc: '2.0', method: 'notifications/initialized' }); } catch {}
}
export async function lfCall(name, args) {
  if (!/^(list|get)[A-Z]/.test(name)) throw new Error(`refused: ${name} is not a read-only tool`);
  if (/^(runLocalFalcon|manage|create|update|delete|save|add|remove|pause|resume|reactivate)/.test(name)) throw new Error(`refused: ${name}`);
  if (!sid) await lfInit();
  const r = await rpc({ jsonrpc: '2.0', id: nid++, method: 'tools/call', params: { name, arguments: args } });
  if (r?.error) throw new Error(`LF ${name}: ${JSON.stringify(r.error).slice(0, 300)}`);
  const txt = r?.result?.content?.map(c => c.text).join('') ?? '';
  if (r?.result?.isError) throw new Error(`LF ${name} isError: ${txt.slice(0, 300)}`);
  try { return JSON.parse(txt); } catch { return txt; }
}
