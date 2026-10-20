// Headless Chrome capture runner for Figma html-to-design.
// usage: node figcap.mjs '<json jobs>'  jobs: [{page, id, w, h, mobile}]
import { spawn } from 'node:child_process';
import { mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const jobs = JSON.parse(process.argv[2]);
const PORT = 9347;
const BASE = 'http://localhost:8970/';
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const sleep = ms => new Promise(r => setTimeout(r, ms));

const chrome = spawn(CHROME, [
  '--headless=new', `--remote-debugging-port=${PORT}`, '--window-size=1440,900',
  '--hide-scrollbars', '--no-first-run', '--disable-extensions',
  `--user-data-dir=${mkdtempSync(join(tmpdir(), 'figcap-'))}`, 'about:blank',
], { stdio: 'ignore' });

async function ready() {
  for (let i = 0; i < 50; i++) {
    try { return await (await fetch(`http://127.0.0.1:${PORT}/json/version`)).json(); } catch { await sleep(200); }
  }
  throw new Error('chrome did not start');
}

function cdp(wsUrl) {
  const ws = new WebSocket(wsUrl);
  let n = 0; const pend = new Map(); const subs = [];
  ws.onmessage = ev => {
    const m = JSON.parse(ev.data);
    if (m.id && pend.has(m.id)) { const p = pend.get(m.id); pend.delete(m.id); m.error ? p.rej(new Error(m.error.message)) : p.res(m.result); }
    else if (m.method) subs.forEach(f => f(m));
  };
  return new Promise(res => { ws.onopen = () => res({
    send: (method, params = {}) => new Promise((r, j) => { const id = ++n; pend.set(id, { res: r, rej: j }); ws.send(JSON.stringify({ id, method, params })); }),
    on: f => subs.push(f), close: () => ws.close(),
  }); });
}

async function run(job) {
  const t = await (await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: 'PUT' })).json();
  const c = await cdp(t.webSocketDebuggerUrl);
  await c.send('Page.enable'); await c.send('Network.enable');
  await c.send('Emulation.setDeviceMetricsOverride', { width: job.w, height: job.h, deviceScaleFactor: job.mobile ? 2 : 1, mobile: !!job.mobile });
  if (job.mobile) {
    await c.send('Emulation.setTouchEmulationEnabled', { enabled: true });
    await c.send('Emulation.setUserAgentOverride', { userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' });
  }
  let status = null, reqId = null;
  c.on(m => {
    if (m.method === 'Network.requestWillBeSent' && m.params.request.url.includes('/submit')) reqId = m.params.requestId;
    if (m.method === 'Network.responseReceived' && m.params.requestId === reqId) status = m.params.response.status;
    if (m.method === 'Network.loadingFailed' && m.params.requestId === reqId) status = 'failed:' + m.params.errorText;
  });
  const ep = encodeURIComponent(`https://mcp.figma.com/mcp/capture/${job.id}/submit?bindVariables=true`);
  const url = `${BASE}${job.page}?export=1#figmacapture=${job.id}&figmaendpoint=${ep}&figmadelay=3500`;
  await c.send('Page.navigate', { url });
  const t0 = Date.now();
  while (status === null && Date.now() - t0 < 120000) await sleep(500);
  const dim = await c.send('Runtime.evaluate', { expression: 'JSON.stringify({iw:innerWidth,sw:document.documentElement.scrollWidth,h:document.documentElement.scrollHeight})', returnByValue: true });
  console.log(JSON.stringify({ page: job.page, w: job.w, id: job.id.slice(0, 8), status, sec: Math.round((Date.now() - t0) / 1000), dim: dim.result.value }));
  await sleep(1500);
  c.close();
  await fetch(`http://127.0.0.1:${PORT}/json/close/${t.id}`);
}

try {
  await ready();
  for (const j of jobs) await run(j);
} finally { chrome.kill(); }
