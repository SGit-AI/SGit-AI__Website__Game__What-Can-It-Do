#!/usr/bin/env python3
"""drain.py — turn proposals from the lane into pull requests against data/.

    python3 admin/proposals/drain.py --in <file-or-folder>... [--key private.pem] [--pr] [--summary]

A proposal arrives as a sealed record on the games' feedback lane (the map vault, source/lane.mjs):
`{"append_token": …, "payload": <v2 envelope>}`. This script

  1. opens each envelope with the lane's private key (--key; the same RSA-OAEP-SHA256 + AES-256-GCM
     envelope `sgit pki decrypt` reads), or reads an already-decrypted body,
  2. applies the record to data/ as a patch — a grant row, an absent cell, a mandate line, a
     reduction; an entry above the ceiling is never patched, only put to a maintainer,
  3. runs the same gate every pull request runs (build_pages.py, then validate.js) and refuses the
     proposal if the pack no longer holds together,
  4. commits the patch on a branch `proposal/<id>` with the rationale as the message, and with --pr
     pushes it and opens the pull request over the GitHub API (GITHUB_TOKEN), nobody named,
  5. with --summary, writes data/proposals.json — what is open and merged per row — which the map
     vault reads to say "proposals on this row: n open".

Nothing here trusts the record: the file and the path must exist in the pack, the values must be
in the vocabularies, and the gate decides. A record that does not apply is reported, not skipped.
"""
import argparse
import base64
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
GH_REPO = "SGit-AI/SGit-AI__Website__Game__What-Can-It-Do"
BASE_BRANCH = "dev"


# ---------------------------------------------------------------------------
# the envelope
# ---------------------------------------------------------------------------

def open_envelope(payload_b64, key_pem):
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    e = json.loads(base64.b64decode(payload_b64))
    if e.get("v") != 2:
        raise ValueError(f"envelope v{e.get('v')} is not v2")
    priv = serialization.load_pem_private_key(key_pem, password=None)
    aes = priv.decrypt(base64.b64decode(e["w"]),
                       padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    plain = AESGCM(aes).decrypt(base64.b64decode(e["i"]), base64.b64decode(e["c"]), None)
    return json.loads(plain)


def read_inputs(paths, key_pem):
    """Every proposal body found under the inputs: lane bodies (with a payload), bare envelopes,
    or decrypted bodies. Returns [(source, body)]."""
    out = []
    files = []
    for p in paths:
        p = Path(p)
        files += sorted(x for x in p.rglob("*") if x.is_file()) if p.is_dir() else [p]
    for f in files:
        text = f.read_text().strip()
        if not text:
            continue
        bodies = []
        try:
            j = json.loads(text)
            items = j if isinstance(j, list) else [j]
        except json.JSONDecodeError:
            items = [line for line in text.splitlines() if line.strip()]
        for it in items:
            if isinstance(it, str):
                it = json.loads(it) if it.lstrip().startswith("{") else {"payload": it}
            if "payload" in it:
                if not key_pem:
                    raise SystemExit(f"{f}: a sealed payload, and no --key to open it")
                bodies.append(open_envelope(it["payload"], key_pem))
            else:
                bodies.append(it)
        out += [(str(f), b) for b in bodies]
    return out


# ---------------------------------------------------------------------------
# applying a record
# ---------------------------------------------------------------------------

class NeedsHuman(Exception):
    """Not a failure: a proposal the drain will not patch, and puts to a maintainer as it is."""


def load(rel):
    p = DATA / rel
    if not p.is_file() or ".." in rel:
        raise ValueError(f"{rel}: not a file in the pack")
    return p, json.loads(p.read_text())


def save(p, obj):
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def vocab():
    v = json.loads((DATA / "vocabulary.json").read_text())
    keys = lambda o: [k for k in o if not k.startswith("_")]
    return keys(v["control_tiers"]), keys(v["evidence_tiers"])


def apply_record(rec):
    """Patch data/ for one record. Returns (files changed, one-line description)."""
    kind, t, to = rec["kind"], rec["target"], rec.get("to") or {}
    CONTROL, EVIDENCE = vocab()
    prim = json.loads((DATA / "primitives.json").read_text())
    caps = {c["id"]: c for c in prim["capabilities"]}

    if kind == "grant-row":
        m = re.fullmatch(r"tools\[(\d+)\]\.grant\[(\d+)\]", t.get("path") or "")
        if not m:
            raise ValueError(f"grant-row path {t.get('path')!r} is not tools[i].grant[j]")
        p, prof = load(t["file"])
        row = prof["tools"][int(m.group(1))]["grant"][int(m.group(2))]
        if row["capability"] != t.get("capability"):
            raise ValueError(f"the row at {t['path']} is {row['capability']}, the record says {t.get('capability')}")
        if to.get("control_tier") not in CONTROL:
            raise ValueError(f"control_tier {to.get('control_tier')!r} is not in the vocabulary")
        if to.get("tier") not in EVIDENCE:
            raise ValueError(f"tier {to.get('tier')!r} is not in the vocabulary")
        row["control_tier"] = to["control_tier"]
        row["tier"] = to["tier"]
        row["control"] = to.get("control") or None
        if to.get("note"):
            row["note"] = to["note"]
        elif "note" in row and not to.get("note"):
            row.pop("note")
        save(p, prof)
        return [t["file"]], f"{prof['id']}: {row['capability']} → control {row['control_tier']}, evidence {row['tier']}"

    if kind == "absent-cell":
        if to.get("reaches") != "yes":
            raise NeedsHuman(f"the proposer says the product {'does not reach' if to.get('reaches') == 'no' else 'may or may not reach'} it; nothing to patch")
        cap = t.get("capability")
        if cap not in caps:
            raise ValueError(f"{cap!r} is not a capability in the pack")
        if to.get("control_tier", "none") not in CONTROL:
            raise ValueError(f"control_tier {to.get('control_tier')!r} is not in the vocabulary")
        p, prof = load(t["file"])
        if cap in prof.get("union", []):
            raise ValueError(f"{prof['id']} already lists {cap}")
        tool_name = (to.get("tool") or "").strip() or "proposed"
        tool = next((x for x in prof["tools"] if x["tool"] == tool_name), None)
        if not tool:
            tool = {"tool": tool_name, "evidence": None, "grant": []}
            prof["tools"].append(tool)
        row = {"capability": cap, "tier": "self-reported", "control": to.get("control") or None,
               "control_tier": to.get("control_tier", "none"),
               "note": (to.get("note") or "proposed through the map vault") + (f" — evidence: {rec['evidence']}" if rec.get("evidence") else "")}
        tool["grant"].append(row)
        prof["union"] = sorted(set(prof.get("union", [])) | {cap})
        if caps[cap]["reversible"] == "no":
            prof["irreversible_in_union"] = sorted(set(prof.get("irreversible_in_union", [])) | {cap})
        save(p, prof)
        return [t["file"]], f"{prof['id']}: adds {cap} via {tool_name} (self-reported)"

    if kind == "mandate-line":
        cap, stance = t.get("capability"), to.get("stance")
        if cap not in caps:
            raise ValueError(f"{cap!r} is not a capability in the pack")
        if stance not in ("want", "do-not-want", "unstated"):
            raise ValueError(f"stance {stance!r}")
        p, mand = load(t["file"])
        mand["want"] = [c for c in mand["want"] if c != cap]
        mand["do_not_want"] = [c for c in mand["do_not_want"] if c != cap]
        if stance == "want":
            mand["want"].append(cap)
        elif stance == "do-not-want":
            mand["do_not_want"].append(cap)
        save(p, mand)
        return [t["file"]], f"{mand['id']}: {cap} → {stance}"

    if kind == "reduction":
        cap = t.get("capability")
        if cap not in caps:
            raise ValueError(f"{cap!r} is not a capability in the pack")
        p, red = load("reductions.json")
        r = red["reductions"].setdefault(cap, {})
        for k in ("setting", "costs", "tier_after"):
            if to.get(k):
                r[k] = to[k]
        save(p, red)
        return ["reductions.json"], f"reduction for {cap}: {r.get('setting', '')[:60]}"

    if kind == "ceiling":
        raise NeedsHuman("a counter-example to an entry above the ceiling is a correction a maintainer makes by hand: the row's control is what is in question")

    raise ValueError(f"unknown kind {kind!r}")


# ---------------------------------------------------------------------------
# git, the gate, the pull request
# ---------------------------------------------------------------------------

def sh(*args, check=True, capture=True):
    r = subprocess.run(args, cwd=ROOT, text=True, capture_output=capture)
    if check and r.returncode:
        raise RuntimeError(f"{' '.join(args)} → {r.returncode}\n{r.stdout}\n{r.stderr}")
    return r


def gate():
    r = subprocess.run([sys.executable, "admin/build/build_pages.py"], cwd=ROOT, text=True, capture_output=True)
    if r.returncode:
        return False, r.stderr.strip() or r.stdout.strip()
    r = subprocess.run(["node", "admin/build/validate.js"], cwd=ROOT, text=True, capture_output=True)
    return r.returncode == 0, (r.stderr.strip() or r.stdout.strip())


def pr_body(rec, desc, body):
    lines = [f"**Proposed through the map vault** — `{rec['kind']}` on `{rec['target']['file']}`"
             + (f" · `{rec['target']['path']}`" if rec['target'].get('path') else ""),
             "", f"**Change:** {desc}", "",
             f"**Why:** {rec['rationale']}", ""]
    if rec.get("evidence"):
        lines += [f"**Evidence:** {rec['evidence']}", ""]
    if rec.get("from"):
        lines += ["**Before:** `" + json.dumps(rec["from"], ensure_ascii=False) + "`"]
    lines += ["**After:** `" + json.dumps(rec.get("to"), ensure_ascii=False) + "`", "",
              f"Against pack {rec['pack'].get('version')} · `{str(rec['pack'].get('content_hash', ''))[:19]}…` "
              f"({rec['pack'].get('origin')}). Record `{body.get('id')}`, sent {dt.datetime.utcfromtimestamp(body.get('sent_at', 0)).isoformat()}Z "
              f"from the map vault v{body.get('version', '?')}. No author is named: proposals travel on a write-only lane and carry no identity.",
              "", "---", "_Opened by admin/proposals/drain.py_"]
    return "\n".join(lines)


def open_pr(branch, title, body):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        return None, "no GITHUB_TOKEN in the environment; the branch is pushed but no pull request was opened"
    req = urllib.request.Request(f"https://api.github.com/repos/{GH_REPO}/pulls",
                                 data=json.dumps({"title": title, "head": branch, "base": BASE_BRANCH, "body": body}).encode(),
                                 headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "Content-Type": "application/json"},
                                 method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        j = json.load(r)
    return j["html_url"], None


def write_summary(results):
    """data/proposals.json — per row: open and merged counts; the pull requests known. Merged with what is
    already there, keyed by record id, so a re-run updates rather than duplicates."""
    f = DATA / "proposals.json"
    cur = json.loads(f.read_text()) if f.exists() else {"pulls": []}
    known = {p["id"]: p for p in cur.get("pulls", [])}
    for r in results:
        if r.get("id"):
            known[r["id"]] = {"id": r["id"], "kind": r["kind"], "target": r["target"], "title": r["title"],
                              "url": r.get("url"), "branch": r.get("branch"), "state": r["state"], "drained_at": r["drained_at"]}
    by_target = {}
    for p in known.values():
        b = by_target.setdefault(p["target"], {"open": 0, "merged": 0, "other": 0})
        b["open" if p["state"] in ("open", "branch") else "merged" if p["state"] == "merged" else "other"] += 1
    out = {
        "type": "proposals-summary/v1",
        "_what_this_is": "What the drain has done with proposals from the map vault, per row: the pull requests opened (or branches made, when no token was at hand) and their state as of generated_at. The map vault reads this to say 'proposals on this row: n open'. Generated by admin/proposals/drain.py --summary; not hashed into the pack.",
        "generated_at": dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "total_open": sum(b["open"] for b in by_target.values()),
        "total_merged": sum(b["merged"] for b in by_target.values()),
        "by_target": by_target,
        "pulls": sorted(known.values(), key=lambda p: p["drained_at"], reverse=True),
    }
    f.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--in", dest="inputs", nargs="+", required=True, help="lane files, envelopes, or decrypted bodies")
    ap.add_argument("--key", help="the lane's private key, PEM, to open sealed payloads")
    ap.add_argument("--pr", action="store_true", help="push each branch and open a pull request (needs GITHUB_TOKEN)")
    ap.add_argument("--summary", action="store_true", help="write data/proposals.json afterwards")
    ap.add_argument("--dry-run", action="store_true", help="apply and gate, then throw the patch away; no branch")
    a = ap.parse_args()

    key_pem = Path(a.key).read_bytes() if a.key else None
    if sh("git", "status", "--porcelain").stdout.strip():
        raise SystemExit("the checkout has uncommitted changes; the drain needs a clean tree to branch from")
    start = sh("git", "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    results = []
    for source, body in read_inputs(a.inputs, key_pem):
        rec, rid = body.get("record"), body.get("id") or "no-id"
        tag = f"[{rid}] {source}"
        if body.get("schema") != "map-proposal/v1" or not rec:
            print(f"skip  {tag}: not a map-proposal/v1 body ({body.get('schema')})")
            continue
        branch = f"proposal/{rid}"
        target = f"{rec['target']['file']}#{rec['target'].get('path') or rec['target'].get('capability') or ''}"
        try:
            sh("git", "checkout", "-q", "-B", branch, start)
            try:
                changed, desc = apply_record(rec)
            except NeedsHuman as e:
                sh("git", "checkout", "-q", start)
                sh("git", "branch", "-q", "-D", branch, check=False)
                print(f"human {tag}: {e}\n      why: {rec.get('rationale')}")
                results.append({"id": rid, "kind": rec["kind"], "target": target, "title": f"{rec['kind']}: {target}", "state": "needs-a-maintainer", "drained_at": dt.date.today().isoformat()})
                continue
            ok, out = gate()
            if not ok:
                sh("git", "checkout", "-q", "--", ".")
                sh("git", "checkout", "-q", start)
                sh("git", "branch", "-q", "-D", branch, check=False)
                print(f"REFUSED {tag}: the gate failed after the patch —\n      {out.splitlines()[-1] if out else ''}")
                results.append({"id": rid, "kind": rec["kind"], "target": target, "title": f"{rec['kind']}: {target}", "state": "refused-by-the-gate", "drained_at": dt.date.today().isoformat()})
                continue
            if a.dry_run:
                sh("git", "checkout", "-q", "--", ".")
                sh("git", "checkout", "-q", start)
                sh("git", "branch", "-q", "-D", branch, check=False)
                print(f"ok    {tag}: {desc} — applies and passes the gate (dry run, nothing kept)")
                continue
            title = f"pack: {desc}"
            sh("git", "add", "-A")
            sh("git", "commit", "-q", "-m", f"{title}\n\n{pr_body(rec, desc, body)}")
            url, why = None, None
            if a.pr:
                sh("git", "push", "-u", "origin", branch)
                url, why = open_pr(branch, title, pr_body(rec, desc, body))
            sh("git", "checkout", "-q", start)
            print(f"ok    {tag}: {desc} → {url or 'branch ' + branch}" + (f" ({why})" if why else ""))
            results.append({"id": rid, "kind": rec["kind"], "target": target, "title": title, "url": url, "branch": branch,
                            "state": "open" if url else "branch", "drained_at": dt.date.today().isoformat()})
        except Exception as e:
            sh("git", "checkout", "-q", "--", ".", check=False)
            sh("git", "checkout", "-q", start, check=False)
            sh("git", "branch", "-q", "-D", branch, check=False)
            print(f"ERROR {tag}: {e}")
            results.append({"id": rid, "kind": rec.get("kind"), "target": target, "title": f"{rec.get('kind')}: {target}", "state": "error", "drained_at": dt.date.today().isoformat()})
    if a.summary and results:
        s = write_summary(results)
        print(f"summary: data/proposals.json — {s['total_open']} open, {s['total_merged']} merged, {len(s['pulls'])} known")


if __name__ == "__main__":
    main()
