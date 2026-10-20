// Small JSON diff. Prints one line per change: "~ path: old -> new", "+ path: value", "- path: value".
// Arrays of rows whose first cell is a text (map, ai, funnel ...) are matched by that text, other arrays by index.
const isObj = v => v && typeof v === 'object' && !Array.isArray(v);
const keyed = a => Array.isArray(a) && a.length > 0 && a.every(r => Array.isArray(r) && typeof r[0] === 'string');
const show = v => { const s = JSON.stringify(v); return s.length > 90 ? s.slice(0, 87) + '…' : s; };

export function diffLines(a, b, path = '', out = []) {
  if (JSON.stringify(a) === JSON.stringify(b)) return out;
  if (isObj(a) && isObj(b)) {
    for (const k of new Set([...Object.keys(a), ...Object.keys(b)])) {
      const p = path ? `${path}.${k}` : k;
      if (!(k in b)) out.push(`- ${p}: ${show(a[k])}`);
      else if (!(k in a)) out.push(`+ ${p}: ${show(b[k])}`);
      else diffLines(a[k], b[k], p, out);
    }
  } else if (keyed(a) && keyed(b)) {
    const am = new Map(a.map(r => [r[0], r])), bm = new Map(b.map(r => [r[0], r]));
    for (const [k, r] of am) if (!bm.has(k)) out.push(`- ${path}[${k}]: ${show(r.slice(1))}`);
    for (const [k, r] of bm) {
      if (!am.has(k)) out.push(`+ ${path}[${k}]: ${show(r.slice(1))}`);
      else if (JSON.stringify(am.get(k)) !== JSON.stringify(r)) out.push(`~ ${path}[${k}]: ${show(am.get(k).slice(1))} -> ${show(r.slice(1))}`);
    }
    const ao = a.map(r => r[0]).filter(k => bm.has(k)).join('|'), bo = b.map(r => r[0]).filter(k => am.has(k)).join('|');
    if (ao !== bo) out.push(`~ ${path}: row order changed`);
  } else if (Array.isArray(a) && Array.isArray(b)) {
    const n = Math.max(a.length, b.length);
    for (let i = 0; i < n; i++) {
      if (i >= b.length) out.push(`- ${path}[${i}]: ${show(a[i])}`);
      else if (i >= a.length) out.push(`+ ${path}[${i}]: ${show(b[i])}`);
      else diffLines(a[i], b[i], `${path}[${i}]`, out);
    }
  } else out.push(`~ ${path}: ${show(a)} -> ${show(b)}`);
  return out;
}
