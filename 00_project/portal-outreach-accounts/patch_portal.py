#!/usr/bin/env python3
"""Patch the 741 portal file (index.html) for outreach numbers per LinkedIn account.

Usage: python3 patch_portal.py <in.html> <out.html>
Works on the live file and on staging (the team area is the same in both).
Every anchor must match exactly once, or the script stops without writing.
Needs migration outreach_numbers_per_account (applied 13.10.2026).
"""
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
if 'renderAccountsAdmin' in s:
    sys.exit('already patched')


def rep(old, new):
    global s
    n = s.count(old)
    if n != 1:
        sys.exit(f'anchor found {n}x: {old[:80]!r}')
    s = s.replace(old, new)


# 1) Strings + helpers, after seatsOf()
HELPERS = r'''
/* ---- Outreach numbers per LinkedIn account (13.10.2026) ---- */
const TA = {
  en: { rs:'Requests sent', ac:'Accepted', pi:'Pitched', fu:'Follow-ups', re:'Replies', in:'Interested',
        rsH:'Connection requests you sent today from this account', acH:'New accepts today (My Network → Connections, or notifications)',
        piH:'First message to a new connection', fuH:'Second or later message', reH:'New replies today', inH:'Replies that want to talk or want an offer',
        rt:'Requests target', mt:'Messages target', tHead:'Targets — per account',
        repHint:'Enter the numbers for each account you worked today. Leave an account empty if you did not work on it.',
        tot:'Totals for the board (filled in for you)', msgs:'messages', req:'requests', noAcc:'No numbers per account.',
        accT:'LinkedIn accounts', accHint:'One row per LinkedIn account. "Client" is a free label — it does not open any client data. People only see the accounts you give them.',
        who:'Who works it', edit:'Edit', deact:'Deactivate', act:'Activate', add:'Add account', addB:'Add', name:'Account name', client:'Client / campaign',
        kc:'Client account', k7:'741 seat', needName:'Enter an account name', perAcc:'Over the days — per account',
        status:'Status line', ready:'Ready for a client status', copy:'Copy', copied:'Copied', sum:'Sum', gC:'Client accounts', g7:'741 own seats',
        rates:'Accepted % = accepted ÷ requests. Reply % = replies ÷ (pitched + follow-ups).', none:'No numbers per account in this period yet.' },
  de: { rs:'Anfragen gesendet', ac:'Angenommen', pi:'Gepitcht', fu:'Follow-ups', re:'Antworten', in:'Interessiert',
        rsH:'Vernetzungsanfragen, die du heute von diesem Account gesendet hast', acH:'Neue Annahmen heute (Mein Netzwerk → Kontakte oder Benachrichtigungen)',
        piH:'Erste Nachricht an einen neuen Kontakt', fuH:'Zweite oder spätere Nachricht', reH:'Neue Antworten heute', inH:'Antworten, die reden oder ein Angebot wollen',
        rt:'Ziel Anfragen', mt:'Ziel Nachrichten', tHead:'Ziele — pro Account',
        repHint:'Trag die Zahlen für jeden Account ein, an dem du heute gearbeitet hast. Lass Accounts leer, an denen du nicht gearbeitet hast.',
        tot:'Summen fürs Board (automatisch)', msgs:'Nachrichten', req:'Anfragen', noAcc:'Keine Zahlen pro Account.',
        accT:'LinkedIn-Accounts', accHint:'Eine Zeile pro LinkedIn-Account. „Kunde“ ist ein freies Label und öffnet keine Kundendaten. Jede Person sieht nur die Accounts, die du ihr gibst.',
        who:'Wer arbeitet daran', edit:'Ändern', deact:'Deaktivieren', act:'Aktivieren', add:'Account hinzufügen', addB:'Hinzufügen', name:'Account-Name', client:'Kunde / Kampagne',
        kc:'Kunden-Account', k7:'741-Seat', needName:'Bitte Account-Namen eintragen', perAcc:'Über die Tage — pro Account',
        status:'Status-Zeile', ready:'Fertig für einen Kunden-Status', copy:'Kopieren', copied:'Kopiert', sum:'Summe', gC:'Kunden-Accounts', g7:'741-eigene Seats',
        rates:'Angenommen % = Angenommen ÷ Anfragen. Antwort % = Antworten ÷ (Gepitcht + Follow-ups).', none:'Noch keine Zahlen pro Account in diesem Zeitraum.' },
  id: { rs:'Permintaan terkirim', ac:'Diterima', pi:'Pitch', fu:'Follow up', re:'Balasan', in:'Tertarik',
        rsH:'Permintaan koneksi yang kamu kirim hari ini dari akun ini', acH:'Koneksi baru yang menerima hari ini (My Network → Connections, atau notifikasi)',
        piH:'Pesan pertama ke koneksi baru', fuH:'Pesan kedua atau berikutnya', reH:'Balasan baru hari ini', inH:'Balasan yang mau bicara atau minta penawaran',
        rt:'Target permintaan', mt:'Target pesan', tHead:'Target — per akun',
        repHint:'Isi angka untuk setiap akun yang kamu kerjakan hari ini. Kosongkan akun yang tidak kamu kerjakan.',
        tot:'Total untuk papan (otomatis)', msgs:'pesan', req:'permintaan', noAcc:'Tidak ada angka per akun.',
        accT:'Akun LinkedIn', accHint:'Satu baris per akun LinkedIn. "Klien" hanya label bebas — tidak membuka data klien. Orang hanya melihat akun yang kamu berikan.',
        who:'Siapa yang mengerjakan', edit:'Ubah', deact:'Nonaktifkan', act:'Aktifkan', add:'Tambah akun', addB:'Tambah', name:'Nama akun', client:'Klien / kampanye',
        kc:'Akun klien', k7:'Seat 741', needName:'Isi nama akun', perAcc:'Sepanjang waktu — per akun',
        status:'Baris status', ready:'Siap untuk status klien', copy:'Salin', copied:'Tersalin', sum:'Jumlah', gC:'Akun klien', g7:'Seat milik 741',
        rates:'Diterima % = diterima ÷ permintaan. Balasan % = balasan ÷ (pitch + follow up).', none:'Belum ada angka per akun di periode ini.' }
};
const ta = () => TA[(teamMe && teamMe.lang) || 'de'] || TA.de;
const ACC_F = ['requests_sent','accepted','pitched','follow_ups','replies','interested'];
const accLbl = (A,f) => ({requests_sent:A.rs, accepted:A.ac, pitched:A.pi, follow_ups:A.fu, replies:A.re, interested:A.in})[f];
const accHelp = (A,f) => ({requests_sent:A.rsH, accepted:A.acH, pitched:A.piH, follow_ups:A.fuH, replies:A.reH, interested:A.inH})[f];
const accTag = a => `<span style="font-size:11.5px;font-weight:700;background:${a.kind==='741'?'var(--grey-light)':'var(--yellow-soft)'};border-radius:6px;padding:2px 8px;">${esc(a.client_label||'—')}</span>`;
let teamAccts = [];
'''
rep("const seatsOf = () => (teamMe && Array.isArray(teamMe.seats) && teamMe.seats.length) ? teamMe.seats : ['Main LinkedIn'];\n",
    "const seatsOf = () => (teamMe && Array.isArray(teamMe.seats) && teamMe.seats.length) ? teamMe.seats : ['Main LinkedIn'];\n" + HELPERS)

# 2) renderMyDay: load account rows with today's plan and report, plus my accounts
rep("db.from('daily_plans').select('*').eq('member_id',teamMe.id).eq('day',day).maybeSingle(),",
    "db.from('daily_plans').select('*, daily_plan_accounts(*)').eq('member_id',teamMe.id).eq('day',day).maybeSingle(),")
rep("db.from('daily_reports').select('*').eq('member_id',teamMe.id).eq('day',day).maybeSingle(),",
    "db.from('daily_reports').select('*, daily_report_accounts(*)').eq('member_id',teamMe.id).eq('day',day).maybeSingle(),")
rep("    db.from('daily_reports').select('*').eq('member_id',teamMe.id).eq('day',yest).maybeSingle(),\n  ]);",
    "    db.from('daily_reports').select('*').eq('member_id',teamMe.id).eq('day',yest).maybeSingle(),\n"
    "    db.from('outreach_account_members').select('account_id, outreach_accounts(*)').eq('member_id',teamMe.id),\n  ]);")
rep("  const [{data:plan},{data:rep},{data:notes},{data:hist},{data:settings},{data:yrep}] = await Promise.all([",
    "  const [{data:plan},{data:rep},{data:notes},{data:hist},{data:settings},{data:yrep},{data:myAcc}] = await Promise.all([")

# 3) Per-account cards, built before histRows; used when the person has accounts
CARDS = r'''
  const A = ta();
  const accts = (myAcc||[]).map(x=>x.outreach_accounts).filter(a=>a&&a.active).sort((a,b)=>(a.sort-b.sort)||a.label.localeCompare(b.label));
  teamAccts = accts;
  const pa = {}; ((plan&&plan.daily_plan_accounts)||[]).forEach(x=>pa[x.account_id]=x);
  const ra = {}; ((rep&&rep.daily_report_accounts)||[]).forEach(x=>ra[x.account_id]=x);
  const accName = id => { const a = accts.find(x=>x.id===id); return a ? a.label : '—'; };
  const useAccPlan = accts.length && (!plan || (plan.daily_plan_accounts||[]).length);
  const useAccRep  = accts.length && (!rep  || (rep.daily_report_accounts||[]).length);
  const accBox = (a, inner) => `<div style="border:1.5px solid #eee7cf;border-radius:12px;padding:12px 14px;margin-top:10px;">
      <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;"><b style="font-size:14px;">${esc(a.label)}</b>${accTag(a)}</div>${inner}</div>`;
  const numIn = (id, lab, help) => `<div style="min-width:0;" title="${esc(help||'')}"><div class="muted" style="font-size:11.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${esc(lab)}</div>
      <input id="${id}" type="number" min="0" placeholder="0" style="width:100%;padding:8px 10px;" oninput="traSum()"></div>`;

  const accWorkBars = accts.map(a=>{ const t=pa[a.id]||{}, d=ra[a.id]||{};
      const b = prog(A.req, d.requests_sent||0, t.requests_target||0) + prog(L.msgs, (d.pitched||0)+(d.follow_ups||0), t.messages_target||0);
      return b ? `<div style="margin-top:10px;"><b style="font-size:13px;">${esc(a.label)}</b> ${accTag(a)}${b}</div>` : ''; }).join('');
  const accWork = accWorkBars ? workCard.replace(`<h2>🎯 ${L.work}</h2>`, `<h2>🎯 ${L.work}</h2>${accWorkBars}`) : workCard;

  const accPlan = plan
    ? `<div class="card"><h2>☀️ ${L.planT} <span class="pill pill-green">${L.submitted}</span></h2>
        ${bulletHtml(plan.intent)}
        ${(plan.daily_plan_accounts||[]).map(x=>`<div class="muted" style="font-size:12.5px;margin-top:4px;"><b>${esc(accName(x.account_id))}</b>: ${A.rt} <b>${x.requests_target}</b> · ${A.mt} <b>${x.messages_target}</b></div>`).join('')}
        <button class="btn btn-small btn-ghost" style="margin-top:10px;" onclick="editPlan()">${L.change}</button></div>`
    : `<div class="card"><h2>☀️ ${L.planT}</h2>
        <textarea id="tp-intent" rows="5" placeholder="${esc(L.planPh)}"></textarea>
        <div class="muted" style="font-size:11.5px;font-weight:700;margin-top:14px;">${A.tHead}</div>
        ${accts.map((a,i)=>accBox(a, `<div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:8px;">
            <div style="flex:1 1 140px;"><div class="muted" style="font-size:11.5px;">${A.rt}</div><input id="tpa-r${i}" type="number" min="0" placeholder="0" style="width:100%;padding:8px 10px;"></div>
            <div style="flex:1 1 140px;"><div class="muted" style="font-size:11.5px;">${A.mt}</div><input id="tpa-m${i}" type="number" min="0" placeholder="0" style="width:100%;padding:8px 10px;"></div></div>`)).join('')}
        <button class="btn btn-small btn-yellow" style="margin-top:12px;" onclick="saveDailyPlanAcc()">${L.save}</button></div>`;

  const accRep = rep
    ? `<div class="card"><h2>🌙 ${L.repT} <span class="pill pill-green">${L.submitted}</span></h2>
        ${(rep.daily_report_accounts||[]).map(x=>`<div style="font-size:12.5px;margin-top:6px;"><b>${esc(accName(x.account_id))}</b>
          <span class="muted">${ACC_F.map(f=>`${esc(accLbl(A,f))} <b>${x[f]}</b>`).join(' · ')}</span></div>`).join('')}
        <div class="muted" style="font-size:12.5px;margin-top:8px;">${L.msgs} <b>${rep.messages_sent}</b> · ${L.replies} <b>${rep.new_replies}</b> · ${L.interested} <b>${rep.interested}</b> · ${L.fups} <b>${rep.follow_ups}</b>${rep.hours_worked?` · ${rep.hours_worked}h`:''}</div>
        ${rep.progress?`<div style="margin-top:10px;"><b style="font-size:13px;">${L.progress}</b>${bulletHtml(rep.progress)}</div>`:''}
        ${rep.blockers?`<div style="margin-top:8px;font-size:13.5px;"><b>${L.blockers}:</b> ${esc(rep.blockers)}</div>`:''}
        ${rep.next_plan?`<div style="margin-top:10px;"><b style="font-size:13px;">${L.next}</b>${bulletHtml(rep.next_plan)}</div>`:''}
        <button class="btn btn-small btn-ghost" style="margin-top:10px;" onclick="editReport()">${L.change}</button></div>`
    : `<div class="card"><h2>🌙 ${L.repT}</h2>
        <div class="muted" style="font-size:12.5px;">${A.repHint}</div>
        ${accts.map((a,i)=>accBox(a, `<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:8px;">${ACC_F.map(f=>numIn(`tra-${i}-${f}`, accLbl(A,f), accHelp(A,f))).join('')}</div>`)).join('')}
        <div id="tra-sum" style="margin-top:12px;padding:10px 14px;background:var(--cream-2);border-radius:10px;font-size:13px;"></div>
        <div style="margin-top:10px;max-width:180px;"><div class="muted" style="font-size:11.5px;">${L.hours}</div><input id="tr-h" type="number" step="0.25" min="0" placeholder="0" style="width:100%;"></div>
        <div class="muted" style="font-size:12px;margin-top:12px;">${L.progress}</div>
        <textarea id="tr-prog" rows="3" placeholder="${esc(L.progressPh)}"></textarea>
        <div class="muted" style="font-size:12px;margin-top:8px;">${L.blockers}</div>
        <textarea id="tr-block" rows="2" placeholder="${esc(L.blockersPh)}"></textarea>
        <div class="muted" style="font-size:12px;margin-top:8px;">${L.next}</div>
        <textarea id="tr-next" rows="3" placeholder="${esc(L.nextPh)}"></textarea>
        <button class="btn btn-small btn-yellow" style="margin-top:10px;" onclick="saveDailyReportAcc()">${L.saveR}</button></div>`;

  const histRows = '''
rep("\n  const histRows = ", CARDS)

rep("<div class=\"grid grid-31\"><div class=\"grid\" style=\"align-content:start;\">${workCard}${planCard}${repCard}</div>",
    "<div class=\"grid grid-31\"><div class=\"grid\" style=\"align-content:start;\">${accts.length?accWork:workCard}${useAccPlan?accPlan:planCard}${useAccRep?accRep:repCard}</div>")

# 4) Save functions + manager cards, before the period section
FUNCS = r'''
function traVals(){ return teamAccts.map((a,i)=>{ const o={account_id:a.id}; ACC_F.forEach(f=>o[f]=parseInt(($(`tra-${i}-${f}`)||{}).value)||0); return o; }); }
function traSum(){
  const el=$('tra-sum'); if(!el) return; const A=ta(), L=tl(), t={}; ACC_F.forEach(f=>t[f]=0);
  traVals().forEach(o=>ACC_F.forEach(f=>t[f]+=o[f]));
  el.innerHTML = `<b>${A.tot}:</b> ${t.pitched+t.follow_ups} ${A.msgs} (= ${t.pitched} ${A.pi} + ${t.follow_ups} ${A.fu}) · ${t.requests_sent} ${A.req} · ${t.accepted} ${A.ac} · ${t.replies} ${A.re} · ${t.interested} ${A.in}`;
}
async function saveDailyPlanAcc(){
  const L=tl(), intent=$('tp-intent').value.trim();
  if(!intent){ toast(L.needPlan); return; }
  const targets = teamAccts.map((a,i)=>({ account_id:a.id, requests_target:parseInt(($('tpa-r'+i)||{}).value)||0, messages_target:parseInt(($('tpa-m'+i)||{}).value)||0 }))
    .filter(t=>t.requests_target||t.messages_target);
  const { error } = await db.rpc('submit_daily_plan', { p_day:tDay(), p_intent:intent, p_targets:targets });
  if(error){ toast('Error: '+error.message); return; }
  toast('✓'); loadTeamDash();
}
async function saveDailyReportAcc(){
  const L=tl(), prog=$('tr-prog').value.trim();
  const rows = traVals().filter(o=>ACC_F.some(f=>o[f]>0));
  if(!prog && !rows.length){ toast(L.needRep); return; }
  const { error } = await db.rpc('submit_daily_report', { p_day:tDay(), p_accounts:rows, p_fields:{
    hours_worked:$('tr-h').value||'', progress:prog, blockers:$('tr-block').value.trim(), next_plan:$('tr-next').value.trim() } });
  if(error){ toast('Error: '+error.message); return; }
  toast('✓'); loadTeamDash();
}

async function renderPeriodAccounts(){
  const A = ta();
  const to = pTo || new Date().toISOString().slice(0,10);
  const from = pFrom || new Date(Date.now()-6*864e5).toISOString().slice(0,10);
  const { data, error } = await db.rpc('team_period_accounts', { p_from: from, p_to: to });
  if(error) return `<div class="card" style="margin-top:14px;"><div class="muted">${esc(error.message)}</div></div>`;
  const rows = (data||[]).filter(x=>(+x.days||0)>0);
  const pct = (a,b) => b ? Math.round(a/b*100)+'%' : '–';
  const td = 'style="text-align:right;padding:8px;border-bottom:1px solid #f4f1e6;white-space:nowrap;"';
  const line = x => `<tr><td style="padding:8px;border-bottom:1px solid #f4f1e6;"><b>${esc(x.label)}</b><div class="muted" style="font-size:11.5px;">${esc(x.client_label||'—')} · ${esc((x.people||[]).join(', '))}</div></td>
      <td ${td}>${x.requests_sent}</td><td ${td}>${x.accepted} <span class="muted">(${pct(x.accepted,x.requests_sent)})</span></td><td ${td}>${x.pitched}</td>
      <td ${td}>${x.follow_ups}</td><td ${td}>${x.replies} <span class="muted">(${pct(x.replies,x.pitched+x.follow_ups)})</span></td><td ${td}>${x.interested}</td>
      <td ${td}><button class="btn btn-small btn-ghost" onclick="accStatusLine('${x.id}')">${A.status}</button></td></tr>`;
  const groups = [['client',A.gC],['741',A.g7]].map(([k,l])=>{ const g=rows.filter(x=>x.kind===k); if(!g.length) return '';
      const s={}; ACC_F.forEach(f=>s[f]=g.reduce((t,x)=>t+(+x[f]||0),0));
      return `<tr><td colspan="8" style="padding:6px 8px;background:var(--cream);font-weight:800;font-size:11.5px;text-transform:uppercase;color:var(--grey);">${l}</td></tr>${g.map(line).join('')}
        <tr><td class="muted" style="padding:8px;">${A.sum}</td>${ACC_F.map(f=>`<td ${td}><b>${s[f]}</b></td>`).join('')}<td></td></tr>`; }).join('');
  window._accPeriod = { rows, from, to };
  const th = l => `<th style="text-align:right;font-size:11px;text-transform:uppercase;color:var(--grey);padding:6px 8px;border-bottom:1.5px solid #eee7cf;white-space:nowrap;">${l}</th>`;
  return `<div style="margin-top:22px;"><div style="font-size:17px;font-weight:800;margin-bottom:10px;">${A.perAcc}</div>
    <div class="card">${rows.length ? `<div style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;font-size:13px;">
      <thead><tr><th style="text-align:left;font-size:11px;text-transform:uppercase;color:var(--grey);padding:6px 8px;border-bottom:1.5px solid #eee7cf;">Account</th>
      ${ACC_F.map(f=>th(accLbl(A,f))).join('')}<th style="border-bottom:1.5px solid #eee7cf;"></th></tr></thead><tbody>${groups}</tbody></table></div>
      <div id="acc-status"></div><div class="muted" style="font-size:12px;margin-top:10px;">${A.rates}</div>` : `<div class="muted">${A.none}</div>`}</div></div>`;
}
function accStatusLine(id){
  const A=ta(), p=window._accPeriod||{}, x=(p.rows||[]).find(r=>r.id===id); if(!x) return;
  const d = v => v.slice(8,10)+'.'+v.slice(5,7)+'.';
  const txt = `${x.client_label||x.label}, ${d(p.from)}–${d(p.to)} (${x.label}): ${x.requests_sent} connection requests sent, ${x.accepted} accepted, ${x.pitched} pitched, ${x.follow_ups} follow-ups, ${x.replies} replies, ${x.interested} interested.`;
  $('acc-status').innerHTML = `<div style="font-size:13px;background:var(--cream);border:1.5px dashed #e3d9b5;border-radius:10px;padding:10px 12px;margin-top:12px;">
    <b>${A.ready}:</b><br><span id="acc-status-txt">${esc(txt)}</span><br>
    <button class="btn btn-small btn-yellow" style="margin-top:8px;" onclick="navigator.clipboard.writeText($('acc-status-txt').textContent).then(()=>toast(ta().copied))">${A.copy}</button></div>`;
}

async function renderAccountsAdmin(){
  const A = ta();
  const [{data:accs,error},{data:mem},{data:asg}] = await Promise.all([
    db.from('outreach_accounts').select('*').order('active',{ascending:false}).order('sort').order('label'),
    db.from('team_members').select('id,display_name').eq('active',true).order('display_name'),
    db.from('outreach_account_members').select('*'),
  ]);
  if(error) return '';
  const on = (a,m) => (asg||[]).some(x=>x.account_id===a && x.member_id===m);
  const row = a => `<div style="border:1.5px solid #eee7cf;border-radius:12px;padding:12px 14px;margin-top:10px;${a.active?'':'opacity:.55;'}">
      <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;">
        <div><b style="font-size:14px;">${esc(a.label)}</b> ${accTag(a)}</div>
        <div style="display:flex;gap:6px;"><button class="btn btn-small btn-ghost" onclick="accEdit('${a.id}')">${A.edit}</button>
        <button class="btn btn-small btn-ghost" onclick="accActive('${a.id}',${!a.active})">${a.active?A.deact:A.act}</button></div></div>
      <div style="margin-top:8px;"><span class="muted" style="font-size:12px;margin-right:6px;">${A.who}:</span>
        ${(mem||[]).map(m=>{ const o=on(a.id,m.id); return `<span onclick="accAssign('${a.id}','${m.id}',${!o})" style="display:inline-block;font-size:12px;padding:3px 10px;border-radius:20px;margin:2px 4px 2px 0;cursor:pointer;user-select:none;border:1.5px solid ${o?'var(--black)':'#e3e0d5'};background:${o?'var(--black)':'transparent'};color:${o?'#fff':'inherit'};">${esc(m.display_name)}</span>`; }).join('')}</div></div>`;
  window._accList = accs||[];
  return `<div style="margin-top:22px;"><div class="card"><h2>🔗 ${A.accT}</h2>
    <div class="muted" style="font-size:12.5px;">${A.accHint}</div>
    ${(accs||[]).map(row).join('')}
    <div style="border:1.5px dashed #e3d9b5;border-radius:12px;padding:12px 14px;margin-top:12px;"><b style="font-size:14px;">${A.add}</b>
      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:8px;">
        <div style="flex:1 1 180px;"><div class="muted" style="font-size:11.5px;">${A.name}</div><input id="acc-n" placeholder="Peggy LinkedIn"></div>
        <div style="flex:1 1 160px;"><div class="muted" style="font-size:11.5px;">${A.client}</div><input id="acc-c" placeholder="Bali Healing"></div>
        <div style="flex:1 1 140px;"><div class="muted" style="font-size:11.5px;">&nbsp;</div><select id="acc-k"><option value="client">${A.kc}</option><option value="741">${A.k7}</option></select></div></div>
      <button class="btn btn-small btn-yellow" style="margin-top:10px;" onclick="accAdd()">${A.addB}</button></div></div></div>`;
}
async function accAdd(){
  const A=ta(), label=$('acc-n').value.trim(); if(!label){ toast(A.needName); return; }
  const sort = Math.max(0, ...(window._accList||[]).map(a=>a.sort||0)) + 10;
  const { error } = await db.from('outreach_accounts').insert({ label, client_label:$('acc-c').value.trim()||null, kind:$('acc-k').value, sort });
  if(error){ toast('Error: '+error.message); return; } toast('✓'); loadTeamDash();
}
async function accEdit(id){
  const A=ta(), a=(window._accList||[]).find(x=>x.id===id); if(!a) return;
  const label = prompt(A.name, a.label); if(label===null) return;
  const client = prompt(A.client, a.client_label||''); if(client===null) return;
  const { error } = await db.from('outreach_accounts').update({ label:label.trim()||a.label, client_label:client.trim()||null }).eq('id',id);
  if(error){ toast('Error: '+error.message); return; } loadTeamDash();
}
async function accActive(id, v){ const { error } = await db.from('outreach_accounts').update({ active:v }).eq('id',id); if(error) toast('Error: '+error.message); loadTeamDash(); }
async function accAssign(acc, mem, v){
  const { error } = v ? await db.from('outreach_account_members').insert({ account_id:acc, member_id:mem })
                      : await db.from('outreach_account_members').delete().eq('account_id',acc).eq('member_id',mem);
  if(error) toast('Error: '+error.message); loadTeamDash();
}

let pFrom = null, pTo = null;'''
rep("\nlet pFrom = null, pTo = null;", FUNCS)

rep("  el.innerHTML = back + (html || '<div class=\"card\"><h2>No access</h2></div>');",
    "  el.innerHTML = back + (html || '<div class=\"card\"><h2>No access</h2></div>');\n  if ($('tra-sum')) traSum();")

rep("  if (isMgr) { html += await renderTeamBoard(); html += await renderPeriod(); }",
    "  if (isMgr) { html += await renderTeamBoard(); html += await renderPeriod(); html += await renderPeriodAccounts(); html += await renderAccountsAdmin(); }")

open(dst, 'w', encoding='utf-8').write(s)
print('patched', src, '->', dst)
