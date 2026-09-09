#!/usr/bin/env node
// The pre-release gate. Run from anywhere: node admin/build/validate.js
//
// Four checks are the house gate, inherited from pki.sgit.ai, graphs.sgit.ai and
// wardley-maps.sgit.ai unchanged in intent:
//   1. version agreement — admin/build/version.txt vs every page's badge, the versions
//      table, llms.txt and every .md twin
//   2. internal links — every relative href/src resolves to a file in the tree
//   3. canonical host — every canonical and og:url is on the host in CNAME
//   4. key-leak tripwire — nothing in the tree may look like an sgit vault key
//
// Three are specific to these two sites, and each exists because of something this
// family has already got wrong once:
//   5. an embed page carries its disclosure — the games phone home, and a page that
//      mounts one without saying so is the exact defect sgit.ai published as finding 1
//      against the vault ("nothing sent" on the same screen as events being sent)
//   6. maturity labels come from the ladder — a card cannot invent a status
//   7. every page has its markdown twin
//   8. the data pack holds together — every capability id resolves, every indexed file
//      exists, unions agree with rows, mandates are consistent (the PR gate for data/)
//
// Any failure exits 1: no tag, no publish.
'use strict';
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const errors = [];

function walk(dir, out = []) {
  for (const name of fs.readdirSync(dir)) {
    if (['.git', '.github', 'node_modules', '.sg_vault'].includes(name)) continue;
    const p = path.join(dir, name);
    fs.statSync(p).isDirectory() ? walk(p, out) : out.push(p);
  }
  return out;
}
const rel = f => path.relative(ROOT, f);
const read = f => fs.readFileSync(f, 'utf8');

const files = walk(ROOT);
// briefs/ holds raw documents — a plan, a review draft — not site pages. They are standalone
// HTML and markdown that predate or sit outside the generated site, so the page-shaped checks
// (canonical host, version badge, .md twin) do not apply to them. Everything that is about
// SAFETY rather than about page shape — the key-leak tripwire, the link check — still scans
// them, because a leaked credential in a brief is a leaked credential.
const isPage = f => !rel(f).startsWith('briefs/');
const htmlFiles = files.filter(f => f.endsWith('.html') && isPage(f));
const mdFiles = files.filter(f => f.endsWith('.md'));

// --- 1. version agreement -------------------------------------------------
const VERSION = read(path.join(ROOT, 'admin/build/version.txt')).trim();
if (!/^v\d+\.\d+\.\d+$/.test(VERSION)) {
  errors.push(`version.txt does not carry a vX.Y.Z version: "${VERSION}"`);
}
for (const f of htmlFiles) {
  for (const m of read(f).matchAll(/class="ver"[^>]*>(v\d+\.\d+\.\d+)</g)) {
    if (m[1] !== VERSION) errors.push(`${rel(f)}: version badge ${m[1]} != ${VERSION}`);
  }
}
if (!read(path.join(ROOT, 'llms.txt')).includes(VERSION)) {
  errors.push(`llms.txt does not mention ${VERSION}`);
}
const versTable = read(path.join(ROOT, 'admin/versions.html'));
if (!versTable.includes(`class="vnum">${VERSION}<`)) {
  errors.push(`admin/versions.html has no row for ${VERSION}`);
}
// Each release appears exactly once — a blanket version-bump sed that touches the history
// table produces duplicates, which shipped once on the NHI site.
const rows = [...versTable.matchAll(/class="vnum">(v\d+\.\d+\.\d+)</g)].map(m => m[1]);
for (const v of rows) {
  if (rows.filter(x => x === v).length > 1) {
    errors.push(`admin/versions.html lists ${v} more than once`);
    break;
  }
}

// --- 2. internal links ----------------------------------------------------
// Every .html in the tree, briefs included: a broken link in a document is still broken.
for (const f of files.filter(f => f.endsWith('.html'))) {
  const dir = path.dirname(f);
  for (const m of read(f).matchAll(/(?:href|src)="([^"#]+)(?:#[^"]*)?"/g)) {
    const target = m[1];
    if (/^(https?:|mailto:|data:|\/\/)/.test(target) || target === '') continue;
    if (!fs.existsSync(path.resolve(dir, target))) {
      errors.push(`${rel(f)}: broken link -> ${target}`);
    }
  }
}

// --- 3. canonical host ----------------------------------------------------
const HOST = read(path.join(ROOT, 'CNAME')).trim();
if (!/^[a-z0-9.-]+$/.test(HOST)) errors.push(`CNAME does not carry a hostname: "${HOST}"`);
for (const f of htmlFiles) {
  const t = read(f);
  const claimed = [
    ...[...t.matchAll(/<link[^>]+rel="canonical"[^>]+href="([^"]+)"/g)].map(m => m[1]),
    ...[...t.matchAll(/<meta[^>]+property="og:url"[^>]+content="([^"]+)"/g)].map(m => m[1]),
  ];
  for (const url of claimed) {
    if (!url.startsWith(`https://${HOST}/`)) {
      errors.push(`${rel(f)}: canonical/og:url is not on ${HOST} -> ${url}`);
    }
  }
  if (!/rel="canonical"/.test(t)) errors.push(`${rel(f)}: no canonical link`);
}

// --- 4. key-leak tripwire -------------------------------------------------
// Two shapes, because this network uses two vault-id formats and the sibling sites'
// tripwire only ever knew the first:
//   · <secret>:<uuid>   — the long-form vault id
//   · <secret>:<8 lowercase alphanumerics> — the short form, which is what every vault
//     in the games family actually uses (4evnlwrj, kqngdecz, …)
// The second shape is the one that matters here and the one the inherited check missed.
// It is also the shape of a VAULT key, `<passphrase>:<vault-id>` — bearer read AND write,
// with no revocation list. A read key is 64 hex and is publishable on purpose; a vault key
// is not publishable ever, and the two are one character class apart to a careless eye.
//
// PUBLISHED is the allow-list, and it is deliberately a list of exact strings rather than a
// pattern: a pattern that admits our read key admits every credential of that shape, which
// is how the check would come to pass while meaning nothing.
const PUBLISHED = [
  // The games vault, read-only. Published on sgit.ai/demos/vaults/agent-permission-games/
  // and re-published here on purpose: it is what lets a reader open the vault themselves.
  'sgit_rk1_f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118:4evnlwrj',
  'f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118:4evnlwrj',
  // the game's own vault since 9 September 2026 (v1.0.0) — the read key, published on purpose
  'sgit_rk1_cf04d8a9bac6185dcb71e9c6f19ae13238b6434780324b1873504f2d6f7b505f:pg87npy3',
  'cf04d8a9bac6185dcb71e9c6f19ae13238b6434780324b1873504f2d6f7b505f:pg87npy3',
  // Licence to Operate (posrhzp3), read-only. Published on
  // sgit.ai/demos/vaults/licence-to-operate/ — the worked example of the delta the game
  // hands a player, embedded on /what-next/.
  'sgit_rk1_d990a52efb9af32c8463e2962f3ca5ccf92b3b6e8ea788e55009073c29b4da29:posrhzp3',
  'd990a52efb9af32c8463e2962f3ca5ccf92b3b6e8ea788e55009073c29b4da29:posrhzp3',
];
const KEY_SHAPES = [
  /[A-Za-z0-9_-]{20,}:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/g,
  /[A-Za-z0-9_-]{16,}:[a-z0-9]{8}\b/g,
];
for (const f of files) {
  if (/\.(png|jpg|jpeg|gif|webp|ico|svg|woff2?|zip|pdf)$/.test(f)) continue;
  const t = read(f);
  for (const shape of KEY_SHAPES) {
    for (const m of t.matchAll(shape)) {
      if (PUBLISHED.includes(m[0])) continue;
      errors.push(`${rel(f)}: vault-key-shaped string "${m[0].slice(0, 14)}…" — if this is a `
                + `read key we meant to publish, add it to PUBLISHED in validate.js; if it is `
                + `a vault key, rotate it`);
    }
  }
}

// --- 5. an embed page carries its disclosure ------------------------------
// The games count usage anonymously. A page of ours that mounts one and says nothing is a
// page that quietly extends the collection while looking like it does not — the exact defect
// sgit.ai published against this vault, where two pages read "nothing sent" on the same
// screen as events being sent. So the check is presence, not position: the notice belongs on
// the page, and it belongs at the FOOT of it. What it describes is less than a default
// server log, and a notice a reader has to step over to reach the game treats something
// ordinary as an obstacle — which is its own kind of dishonesty about the size of the thing.
for (const f of htmlFiles) {
  const t = read(f);
  if (t.includes('class="sgv-app') && !t.includes('class="disclose"')) {
    errors.push(`${rel(f)}: mounts a vault app but carries no telemetry disclosure`);
  }
}

// --- 6. maturity labels come from the ladder ------------------------------
const RUNGS = ['sketch', 'playable', 'scored', 'measured', 'answered'];
for (const f of htmlFiles) {
  for (const m of read(f).matchAll(/class="rung[^"]*">([^<]+)</g)) {
    if (!RUNGS.includes(m[1].trim())) {
      errors.push(`${rel(f)}: "${m[1].trim()}" is not a rung on the ladder (${RUNGS.join(', ')})`);
    }
  }
}

// --- 7. every page has its twin -------------------------------------------
for (const f of htmlFiles) {
  const twin = f.replace(/\.html$/, '.md');
  if (!fs.existsSync(twin)) errors.push(`${rel(f)}: no .md twin (run build_pages.py)`);
}

// --- 8. the data pack holds together ---------------------------------------
// data/ is the contribution surface: a pull request edits JSON and the map regenerates. So
// the gate has to refuse a pull request whose data does not hold together, or the first
// typo in a capability id ships as a silent hole in the matrix. Every id referenced anywhere
// must resolve; every file the indexes name must exist; a profile's stated union must equal
// what its rows imply; a mandate cannot both want and refuse the same thing.
(function () {
  const D = path.join(ROOT, 'data');
  const J = f => { try { return JSON.parse(read(path.join(D, f))); }
                   catch (e) { errors.push(`data/${f}: ${e.message}`); return null; } };
  const voc = J('vocabulary.json'); if (!voc) return;
  const TIERS = Object.keys(voc.evidence_tiers).filter(k => !k.startsWith('_'));
  const CTIERS = Object.keys(voc.control_tiers).filter(k => !k.startsWith('_'));
  const REV = Object.keys(voc.reversible);
  const prim = J('primitives.json'); if (!prim) return;
  const caps = new Set(prim.capabilities.map(c => c.id));
  const families = new Set(Object.keys(prim.families));
  for (const c of prim.capabilities) {
    if (!families.has(c.family)) errors.push(`data/primitives.json: ${c.id} has unknown family "${c.family}"`);
    if (!REV.includes(c.reversible)) errors.push(`data/primitives.json: ${c.id} has unknown reversible "${c.reversible}"`);
  }
  const idx = J('profiles/index.json'); if (!idx) return;
  const profiles = [];
  for (const e of idx.profiles) {
    const f = `profiles/${e.id}.json`;
    if (!fs.existsSync(path.join(D, f))) { errors.push(`data/profiles/index.json names ${f}, which does not exist`); continue; }
    const pr = J(f); if (!pr) continue;
    if (pr.id !== e.id) errors.push(`data/${f}: id "${pr.id}" does not match the index's "${e.id}"`);
    profiles.push(pr);
    const implied = new Set();
    for (const t of pr.tools || []) for (const r of t.grant || []) {
      if (!caps.has(r.capability)) errors.push(`data/${f}: ${t.tool} grants unknown capability "${r.capability}"`);
      implied.add(r.capability);
      if (r.control_tier && !CTIERS.includes(r.control_tier))
        errors.push(`data/${f}: ${t.tool}/${r.capability} has control_tier "${r.control_tier}", not in vocabulary.json`);
      if (r.tier && !TIERS.includes(r.tier))
        errors.push(`data/${f}: ${t.tool}/${r.capability} has tier "${r.tier}", not in vocabulary.json`);
    }
    const stated = new Set(pr.union || []);
    const diff = [...implied].filter(x => !stated.has(x)).concat([...stated].filter(x => !implied.has(x)));
    if (diff.length) errors.push(`data/${f}: union disagrees with its tool rows — ${diff.join(', ')}`);
    for (const c of pr.irreversible_in_union || []) if (!stated.has(c)) errors.push(`data/${f}: irreversible_in_union names ${c}, not in union`);
  }
  // every profile file on disk is in the index (an orphan file is a contribution nobody sees)
  const onDisk = walk(path.join(D, 'profiles')).filter(f => f.endsWith('.json') && path.basename(f) !== 'index.json')
    .map(f => path.relative(path.join(D, 'profiles'), f).replace(/\.json$/, ''));
  const indexed = new Set(idx.profiles.map(e => e.id));
  for (const id of onDisk) if (!indexed.has(id)) errors.push(`data/profiles/${id}.json exists but is not in profiles/index.json`);
  const red = J('reductions.json');
  if (red) for (const k of Object.keys(red.reductions)) if (!caps.has(k)) errors.push(`data/reductions.json: unknown capability "${k}"`);
  const ceil = J('ceiling.json');
  if (ceil) for (const c of ceil.capabilities) {
    if (!families.has(c.family)) errors.push(`data/ceiling.json: ${c.id} has unknown family "${c.family}"`);
    if (caps.has(c.id)) errors.push(`data/ceiling.json: ${c.id} is also a primitive — a thing above the ceiling cannot be in a grant`);
  }
  const midx = J('mandates/index.json');
  if (midx) for (const e of midx.mandates) {
    const f = `mandates/${e.file}`;
    if (!fs.existsSync(path.join(D, f))) { errors.push(`data/mandates/index.json names ${f}, which does not exist`); continue; }
    const m = J(f); if (!m) continue;
    for (const k of ['want', 'do_not_want']) for (const c of m[k] || []) if (!caps.has(c)) errors.push(`data/${f}: ${k} names unknown capability "${c}"`);
    for (const c of Object.keys(m.notes || {})) if (!caps.has(c)) errors.push(`data/${f}: note on unknown capability "${c}"`);
    for (const c of (m.want || []).filter(x => (m.do_not_want || []).includes(x))) errors.push(`data/${f}: both wants and does not want "${c}"`);
    for (const pid of m.applies_to || []) if (!indexed.has(pid)) errors.push(`data/${f}: applies_to unknown profile "${pid}"`);
    if (!m.applies_to || !m.applies_to.length) errors.push(`data/${f}: applies to no profile`);
  }
  const pack = J('pack.json');
  if (pack && pack.version !== VERSION) errors.push(`data/pack.json is ${pack.version}, site is ${VERSION} — run build_pages.py`);
}());

// --- report ---------------------------------------------------------------
if (errors.length) {
  console.error(`validate: ${errors.length} error(s)`);
  for (const e of errors) console.error('  ✗ ' + e);
  process.exit(1);
}
console.log(`validate: OK — ${VERSION} on ${HOST}, ${htmlFiles.length} pages, `
          + `${mdFiles.length} markdown files, links resolve, every embed discloses, `
          + `no key-shaped strings outside the published read key, the data pack holds together`);
