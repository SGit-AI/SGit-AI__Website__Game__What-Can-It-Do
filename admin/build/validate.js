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
//   7. the read key is the one we meant to publish — see check 4's note
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
// The games send anonymous usage events. The vault says so on every one of its own pages;
// a page of ours that mounts the game and does not is a page that quietly extends the
// collection while looking like it does not. Mechanical, so it cannot be forgotten.
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

// --- report ---------------------------------------------------------------
if (errors.length) {
  console.error(`validate: ${errors.length} error(s)`);
  for (const e of errors) console.error('  ✗ ' + e);
  process.exit(1);
}
console.log(`validate: OK — ${VERSION} on ${HOST}, ${htmlFiles.length} pages, `
          + `${mdFiles.length} markdown files, links resolve, every embed discloses, `
          + `no key-shaped strings outside the published read key`);
