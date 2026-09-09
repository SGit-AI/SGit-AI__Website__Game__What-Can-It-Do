#!/usr/bin/env python3
"""The map — every page under /map/ and the /data/ page, generated from data/.

data/ is the pack: the capability primitives, the nine profiles (what each product can reach,
tool by tool, with an evidence tier and a control tier on every row), the reductions, the
ceiling, the mesh, and the starting mandates. It is the part of the game that people will
argue with, so it lives here in git where a pull request is the unit of argument — the game's
scoring and levels stay in the vault, and the game reads this pack over the network.

Nothing on these pages is typed in. Every number, glyph and row is computed from the JSON, so
a merged pull request changes the pages on the next build with no hand in between. That is
the whole reason the map is generated rather than written: a map that has to be re-drawn by
a person after each contribution is a map that will fall behind its own data inside a month.

Two matrices carry most of the weight, and they are deliberately different encodings:

  · THE GRANTS MATRIX (capability × profile) is ORDINAL — how much stands between the agent
    and the capability: nothing, an expectation in prose, a setting the agent's own account
    can flip, or a boundary enforced above it. One hue, stepped by that order, plus a glyph
    on every cell so the reading never depends on colour alone.
  · THE DELTA MATRIX (capability × profile, for one mandate) is DIVERGING — two poles that
    read as opposite (excess: it can and you did not want it to; shortfall: it cannot and
    you did) with a neutral middle, plus a glyph on every cell for the same reason.

The palette was checked with the data-viz validator rather than judged by eye: the diverging
pair passes every gate on the light surface; the teal steps are a sequential ramp (monotone
in lightness), and the two lightest carry a dark glyph because they sit under 3:1 on white.
"""
import hashlib
import html
import json
from pathlib import Path

import shell

# The pack is served from here, with CORS `*` (GitHub Pages), which is what lets the game
# fetch it from inside the vault host. Confirmed against the live site, not assumed.
PACK_BASE = "https://what-can-it-do.games.sgit.ai/data/"
GH = "https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do"
GH_EDIT = f"{GH}/edit/dev/data/"
GH_BLOB = f"{GH}/blob/dev/data/"
PKI_PROBES = "https://github.com/SGit-AI/SGit-AI__Website__PKI/tree/dev/probes"

# ---------------------------------------------------------------------------
# vocabularies
# ---------------------------------------------------------------------------

# The vocabularies come from data/vocabulary.json — ordered, weakest first — so that a new
# tier is a pull request to the pack rather than an edit here AND in validate.js. Filled in
# by load(); referenced by name below.
CONTROL, CONTROL_LABEL = [], {}
EVIDENCE, EVIDENCE_LABEL = [], {}
# Every cell carries one of these as well as a fill, so the reading never depends on colour.
GLYPH = {"none": "●", "expectation": "◉", "setting": "◐", "boundary": "○", "absent": "·"}

REV_LABEL = {}  # from the vocabulary

# The delta classes are the game's own, in the game's own words.
DELTA = {
    "excess":          ("▲", "excess — it can, and you did not want it to"),
    "shortfall":       ("▼", "shortfall — it cannot, and you wanted it to"),
    "aligned-can":     ("✓", "aligned — it can, and you wanted it to"),
    "aligned-cannot":  ("–", "aligned — it cannot, and you did not want it to"),
    "unstated-can":    ("?", "it can, and the mandate does not say"),
    "unstated-cannot": ("·", "it cannot, and the mandate does not say"),
}

# Column headers for a 9-column matrix. The picker's labels are a sentence each; a column
# needs two short lines. Hand-set, keyed by profile id, so adding a profile that has no entry
# here falls back to its variant name rather than breaking the build.
SHORT = {
    "anthropic/claude-code/local-default": ("Claude Code", "local · confirm on"),
    "anthropic/claude-code/local-confirmations-off": ("Claude Code", "local · confirm off"),
    "anthropic/claude-code-remote/ccr-container": ("Claude Code", "web container"),
    "anthropic/claude-desktop/default": ("Claude Desktop", "local tools"),
    "anthropic/claude-web/connectors-on": ("Claude.ai", "connectors on"),
    "openai/chatgpt-web/default": ("ChatGPT", "no connectors"),
    "github/actions-runner/ci": ("GitHub Actions", "hosted runner"),
    "generic/browser-extension/broad-host-permissions": ("Browser extension", "all sites"),
    "generic/scheduled-job/service-account": ("Scheduled job", "service account"),
}


# ---------------------------------------------------------------------------
# loading and derivation
# ---------------------------------------------------------------------------

def load(root):
    d = Path(root) / "data"
    J = lambda p: json.loads((d / p).read_text())
    voc = J("vocabulary.json")
    CONTROL[:] = [k for k in voc["control_tiers"] if not k.startswith("_")]
    CONTROL_LABEL.update({k: f"{k} — {v}" for k, v in voc["control_tiers"].items() if not k.startswith("_")})
    EVIDENCE[:] = [k for k in voc["evidence_tiers"] if not k.startswith("_")]
    EVIDENCE_LABEL.update({k: f"{k} — {v}" for k, v in voc["evidence_tiers"].items() if not k.startswith("_")})
    REV_LABEL.update(voc["reversible"])
    prim = J("primitives.json")
    idx = J("profiles/index.json")
    profiles = [J(f"profiles/{p['id']}.json") for p in idx["profiles"]]
    mesh = J("mesh/graph.json")
    mand_idx = J("mandates/index.json")
    mandates = [J(f"mandates/{m['file']}") for m in mand_idx["mandates"]]
    pack = {
        "primitives": prim,
        "caps": prim["capabilities"],
        "cap_by_id": {c["id"]: c for c in prim["capabilities"]},
        "families": prim["families"],
        "reaches": prim["reaches"],
        "profiles": profiles,
        "prof_by_id": {p["id"]: p for p in profiles},
        "reductions": J("reductions.json")["reductions"],
        "ceiling": J("ceiling.json")["capabilities"],
        "picker": J("picker.json"),
        "mesh": mesh,
        "mandates": mandates,
        "mand_by_id": {m["id"]: m for m in mandates},
        "reach_label": {n["id"].split(":", 1)[1]: n.get("label", n["id"])
                        for n in mesh["nodes"] if n["type"] == "reach"},
        "questions": [n for n in mesh["nodes"] if n["type"] == "question"],
    }
    for p in profiles:
        p["_cells"] = grant_cells(p)
        # The union the file carries and the union the rows imply must agree, or one of them
        # is stale. A contributor edits rows; the build refuses to publish a file whose summary
        # disagrees with its own rows.
        implied = set(p["_cells"])
        stated = set(p["union"])
        if implied != stated:
            raise SystemExit(f"{p['id']}: union disagrees with its tool rows — "
                             f"rows imply {sorted(implied ^ stated)} differ")
    return pack


def grant_cells(profile):
    """capability id -> the weakest control across the tools that reach it, the strongest
    evidence, and the tools and notes behind it."""
    cells = {}
    for tool in profile.get("tools", []):
        for row in tool.get("grant", []):
            cid = row["capability"]
            c = cells.setdefault(cid, {"control": "boundary", "evidence": "derived",
                                       "tools": [], "notes": [], "controls": []})
            ct = row.get("control_tier") or "none"
            if ct not in CONTROL:
                raise SystemExit(f"{profile['id']}: {tool['tool']}/{cid} control_tier "
                                 f"'{ct}' is not in data/vocabulary.json")
            if CONTROL.index(ct) < CONTROL.index(c["control"]):
                c["control"] = ct
            et = row.get("tier") or "derived"
            if et not in EVIDENCE:
                raise SystemExit(f"{profile['id']}: {tool['tool']}/{cid} tier '{et}' is not "
                                 f"in data/vocabulary.json")
            if EVIDENCE.index(et) > EVIDENCE.index(c["evidence"]):
                c["evidence"] = et
            c["tools"].append(tool["tool"])
            if row.get("note"):
                c["notes"].append(f'{tool["tool"]}: {row["note"]}')
            if row.get("control"):
                c["controls"].append(f'{tool["tool"]}: {row["control"]} ({ct})')
    return cells


def delta(mandate, profile):
    """capability id -> delta class, for one mandate against one profile."""
    want, no = set(mandate["want"]), set(mandate["do_not_want"])
    out = {}
    for cid in (c["id"] for c in _caps_cache):
        can = cid in profile["_cells"]
        if cid in want:
            out[cid] = "aligned-can" if can else "shortfall"
        elif cid in no:
            out[cid] = "excess" if can else "aligned-cannot"
        else:
            out[cid] = "unstated-can" if can else "unstated-cannot"
    return out


_caps_cache = []


# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------

def esc(s):
    return html.escape(str(s), quote=True)


def prof_href(pid):
    return f"map/grants/{pid}/index.html"


def cap_href(cid):
    return f"map/capabilities/{cid}/index.html"


def mand_href(mid):
    return f"map/mandates/{mid}/index.html"


def short(pid, pack):
    if pid in SHORT:
        return SHORT[pid]
    p = pack["prof_by_id"][pid]
    return (p["vendor"], p["variant"])


def by_family(pack):
    fams = list(pack["families"].keys())
    groups = {f: [] for f in fams}
    for c in pack["caps"]:
        groups.setdefault(c["family"], []).append(c)
    return [(f, pack["families"].get(f, ""), groups[f]) for f in groups if groups[f]]


# ---------------------------------------------------------------------------
# the two matrices — each rendered twice, HTML and markdown
# ---------------------------------------------------------------------------

def grants_matrix(pack, up, profiles=None):
    profiles = profiles or pack["profiles"]
    ncol = 2 + len(profiles)
    # Nine columns need more than the text measure; one column should not be stretched to it.
    shape = "wide" if len(profiles) > 3 else "narrow"
    h = [f'<div class="matrixwrap {shape}"><table class="matrix grants">', "<thead><tr>",
         '<th class="cap">Capability</th><th class="rev" title="Whether the effect can be undone">Undo</th>']
    for p in profiles:
        a, b = short(p["id"], pack)
        h.append(f'<th class="p"><a href="{up}{prof_href(p["id"])}" title="{esc(p["product"])} — {esc(p["variant"])}">'
                 f'{esc(a)}<span>{esc(b)}</span></a></th>')
    h.append("</tr></thead><tbody>")
    m = ["| Capability | Undo | " + " | ".join(f"{a} ({b})" for a, b in (short(p["id"], pack) for p in profiles)) + " |",
         "|---|---|" + "|".join("---" for _ in profiles) + "|"]
    for fam, fam_desc, caps in by_family(pack):
        h.append(f'<tr class="fam"><th colspan="{ncol}">{esc(fam)} <span>— {esc(fam_desc)}</span></th></tr>')
        m.append(f"| **{fam}** — {fam_desc} | | " + " | ".join("" for _ in profiles) + " |")
        for c in caps:
            rev = c["reversible"]
            h.append(f'<tr><th class="cap"><a href="{up}{cap_href(c["id"])}">{esc(c["label"])}</a>'
                     f'<span class="id">{esc(c["id"])}</span></th>'
                     f'<td class="rev rev-{rev}" title="{esc(REV_LABEL[rev])}">{esc(rev)}</td>')
            cells_md = []
            for p in profiles:
                cell = p["_cells"].get(c["id"])
                if not cell:
                    h.append(f'<td class="m m-absent" title="{esc(short(p["id"], pack)[0])}: not in this grant">'
                             f'{GLYPH["absent"]}</td>')
                    cells_md.append(GLYPH["absent"])
                    continue
                ct, ev = cell["control"], cell["evidence"]
                tip = (f'{short(p["id"], pack)[0]} · {CONTROL_LABEL[ct]} · evidence: {ev} · '
                       f'via {", ".join(dict.fromkeys(cell["tools"]))}')
                h.append(f'<td class="m m-{ct}" title="{esc(tip)}">'
                         f'<a href="{up}{prof_href(p["id"])}#{esc(c["id"])}">{GLYPH[ct]}</a></td>')
                cells_md.append(GLYPH[ct])
            h.append("</tr>")
            m.append(f"| {c['label']} `{c['id']}` | {rev} | " + " | ".join(cells_md) + " |")
    h.append("</tbody></table></div>")
    return "\n".join(h), "\n".join(m)


def grants_legend(up):
    items = "".join(
        f'<span class="lg"><b class="m m-{k}">{GLYPH[k]}</b> {esc(CONTROL_LABEL[k])}</span>'
        for k in CONTROL)
    items += f'<span class="lg"><b class="m m-absent">{GLYPH["absent"]}</b> not in this grant</span>'
    h = f'<div class="legend">{items}</div>'
    m = ("Legend: " + " · ".join(f"{GLYPH[k]} {CONTROL_LABEL[k]}" for k in CONTROL)
         + f" · {GLYPH['absent']} not in this grant")
    return h, m


def delta_matrix(pack, up, mandate, profiles):
    ncol = 1 + len(profiles)
    shape = "wide" if len(profiles) > 3 else "narrow"
    h = [f'<div class="matrixwrap {shape}"><table class="matrix deltas">', "<thead><tr>",
         '<th class="cap">Capability</th>']
    for p in profiles:
        a, b = short(p["id"], pack)
        h.append(f'<th class="p"><a href="{up}{prof_href(p["id"])}">{esc(a)}<span>{esc(b)}</span></a></th>')
    h.append("</tr></thead><tbody>")
    m = ["| Capability | " + " | ".join(f"{a} ({b})" for a, b in (short(p["id"], pack) for p in profiles)) + " |",
         "|---|" + "|".join("---" for _ in profiles) + "|"]
    deltas = {p["id"]: delta(mandate, p) for p in profiles}
    counts = {p["id"]: {"excess": 0, "shortfall": 0} for p in profiles}
    for fam, fam_desc, caps in by_family(pack):
        h.append(f'<tr class="fam"><th colspan="{ncol}">{esc(fam)}</th></tr>')
        m.append(f"| **{fam}** | " + " | ".join("" for _ in profiles) + " |")
        for c in caps:
            note = mandate.get("notes", {}).get(c["id"])
            h.append(f'<tr><th class="cap"><a href="{up}{cap_href(c["id"])}">{esc(c["label"])}</a>'
                     + (f'<span class="mnote">{esc(note)}</span>' if note else "") + "</th>")
            row_md = []
            for p in profiles:
                k = deltas[p["id"]][c["id"]]
                if k in counts[p["id"]]:
                    counts[p["id"]][k] += 1
                g, lab = DELTA[k]
                h.append(f'<td class="d d-{k}" title="{esc(lab)}">{g}</td>')
                row_md.append(g)
            h.append("</tr>")
            m.append(f"| {c['label']}" + (f" — *{note}*" if note else "") + " | " + " | ".join(row_md) + " |")
    # the tally row: what the whole matrix comes to
    h.append('<tr class="tally"><th class="cap">The delta</th>')
    tally_md = []
    for p in profiles:
        e, s = counts[p["id"]]["excess"], counts[p["id"]]["shortfall"]
        h.append(f'<td><b class="d d-excess">▲ {e}</b> <b class="d d-shortfall">▼ {s}</b></td>')
        tally_md.append(f"▲ {e} · ▼ {s}")
    h.append("</tr></tbody></table></div>")
    m.append("| **The delta** | " + " | ".join(tally_md) + " |")
    return "\n".join(h), "\n".join(m), counts


def delta_legend():
    items = "".join(f'<span class="lg"><b class="d d-{k}">{g}</b> {esc(lab)}</span>' for k, (g, lab) in DELTA.items())
    return (f'<div class="legend">{items}</div>',
            "Legend: " + " · ".join(f"{g} {lab}" for g, lab in DELTA.values()))


def tiles(items):
    """Hero numbers — used once, on the map's front page, where the figures are the point."""
    h = '<div class="tiles">' + "".join(
        f'<div class="tile"><b>{esc(n)}</b><span>{esc(l)}</span></div>' for n, l in items) + "</div>"
    m = " · ".join(f"**{n}** {l}" for n, l in items)
    return h, m


# ---------------------------------------------------------------------------
# pages
# ---------------------------------------------------------------------------

def pages(root, ctx):
    """Every /map/ page and /data/index.html. `ctx` carries the site's constants."""
    pack = load(root)
    global _caps_cache
    _caps_cache = pack["caps"]
    P = {}
    n_prof, n_cap = len(pack["profiles"]), len(pack["caps"])
    rows = [r for p in pack["profiles"] for t in p["tools"] for r in t["grant"]]
    n_rows = len(rows)
    n_measured = sum(1 for r in rows if r.get("tier") in EVIDENCE[-2:])
    n_irrev = sum(1 for c in pack["caps"] if c["reversible"] == "no")

    # ---- /map/ — the grants matrix --------------------------------------
    mh, mm = grants_matrix(pack, "../")
    lh, lm = grants_legend("../")
    th, tm = tiles([(n_prof, "products × setups"), (n_cap, "capabilities"),
                    (n_irrev, "of them cannot be undone"),
                    (f"{n_measured}/{n_rows}", "rows measured, not derived")])
    P["map/index.html"] = {
      "title": "The map — what each agent can reach",
      "description": f"{n_cap} capabilities across {n_prof} products and setups: what each one "
                     "can reach, what stands in the way, and how sure anyone is. Generated from "
                     "the data pack; change it with a pull request.",
      "blocks": [
        ("crumb", "[Play](index.html) / The map"),
        ("h1", "What each agent can reach"),
        ("lead", f"Every question the game asks is a cell in this table. {n_cap} capabilities — "
                 f"a verb, an object and how far it reaches — against {n_prof} products in the "
                 f"setups people actually run them in. The fill says how open the door is; the "
                 f"glyph says the same thing without the colour."),
        ("both", th, tm),
        ("both", lh, lm),
        ("both", mh, mm),
        ("h2", "How to read it"),
        ("ul", [
          "**A filled cell means the agent can.** What the fill *shade* adds is what stands "
          "between it and the capability: nothing (●), a rule somebody wrote down (◉), a "
          "setting the agent's own account could change (◐), or a boundary enforced above it "
          "that it cannot reach (○). Darker is more open.",
          "**Hover a cell** for the control, the evidence tier and the tool that reaches it. "
          "Click it for the row on that product's page.",
          "**The Undo column is the row's weight.** A capability that cannot be undone — read a "
          "credential, send a message, delete at host reach — is a different kind of thing from "
          "one that can, however many cells it fills. The game's levels are built on that.",
          "**Host, tenant and world mean what the profile says they mean.** For an agent in a "
          "vendor's container, *host* is the container and *tenant* is a scoped token — not "
          "your machine and not your accounts. Each product's page names its reaches.",
        ]),
        ("h2", "How sure is any of this"),
        ("p", f"Not very, in most places, and every row says so. Of {n_rows} tool-capability rows "
              f"across the set, **{n_measured} were measured** — a probe run on an instance, "
              f"dated — and the rest are *derived* from what a thing architecturally is, or "
              f"*documented* by the vendor. A derived row is a claim until somebody runs the "
              f"probes and contributes the file, and the honest reading of this table is "
              f"**mostly claims, structured so that each one can be replaced by a measurement**."),
        ("p", "That is what the pull request is for. [How to contribute](map/contribute/index.html) "
              "— a row, a whole profile, a mandate, or a correction."),
        ("h2", "The rest of the map"),
        ("cards", [
          {"title": "Every product, one page each",
           "sub": "Tool by tool: what it reaches, the control on the path, the evidence, what the "
                  "profile says is out of reach and why, and the reductions that narrow it.",
           "foot": "[The products](map/grants/index.html)"},
          {"title": "The capabilities",
           "sub": f"The {n_cap} primitives the questions are built from — which products grant "
                  "each, what narrows it, which questions ask about it, and which mandates want it.",
           "foot": "[The capabilities](map/capabilities/index.html)"},
          {"title": "Mandates, and the deltas",
           "sub": "What a reasonable person wanted, per setup — and the gap against what was "
                  "actually granted, as a matrix: excess in one colour, shortfall in the other.",
           "foot": "[The mandates](map/mandates/index.html) · [The deltas](map/deltas/index.html)"},
          {"title": "Above the ceiling",
           "sub": f"The {len(pack['ceiling'])} things no agent in this set can do, each naming the "
                  "control outside the agent that stops it.",
           "foot": "[The ceiling](map/ceiling/index.html)"},
          {"title": "The questions",
           "sub": f"{len(pack['questions'])} questions the games ask, with what each one is for — "
                  "the seed of a question pack that could be customised.",
           "foot": "[The questions](map/questions/index.html)"},
          {"title": "The data pack",
           "sub": "All of it as JSON, at a stable URL with CORS, which is how the game reads it. "
                  "Fork it, change it, point the game at yours.",
           "foot": "[The pack](data/index.html) · [Contribute](map/contribute/index.html)"},
        ]),
      ]}

    # ---- /map/grants/ — the products -------------------------------------
    rows_tbl = []
    for p in pack["profiles"]:
        a, b = short(p["id"], pack)
        cells = p["_cells"]
        open_n = sum(1 for c in cells.values() if c["control"] == "none")
        meas = sum(1 for c in cells.values() if c["evidence"] in EVIDENCE[-2:])
        rows_tbl.append([f"[{a} — {b}]({prof_href(p['id'])})", p["surface"], str(len(cells)),
                         str(open_n), str(len(p["irreversible_in_union"])), f"{meas}/{len(cells)}"])
    P["map/grants/index.html"] = {
      "title": "The products",
      "description": f"One page per product and setup — {n_prof} of them — with every tool, "
                     "what it reaches, the control on the path and the evidence behind the row.",
      "blocks": [
        ("crumb", "[Play](index.html) / [The map](map/index.html) / The products"),
        ("h1", "The products, in the setups people run them in"),
        ("lead", "A *profile* is one product in one configuration — Claude Code with "
                 "confirmations on is a different animal from Claude Code with them off, and "
                 "the same product in a vendor's container is different again. Nine so far. "
                 "The one you use is probably close to one of them, and the game says so when "
                 "it is playing you against a stand-in."),
        ("table", ["Profile", "Surface", "Can reach", "With nothing in the way",
                   "Cannot be undone", "Measured"], rows_tbl),
        ("p", "*Can reach* counts capabilities in the grant. *With nothing in the way* is the "
              "subset with no control at all on the path. *Cannot be undone* is the subset "
              "whose effect is irreversible. *Measured* is how many of the grant's rows rest on a "
              "probe run rather than an inference."),
        ("h2", "Something missing?"),
        ("p", "A product you use that is not here, or a setup of one that is — a profile is one "
              "JSON file, and [contributing one](map/contribute/index.html) is a pull request. "
              "A derived profile, honestly labelled, is worth having; a measured one is worth "
              "more."),
      ]}

    # ---- one page per profile ------------------------------------------
    for p in pack["profiles"]:
        pid = p["id"]
        a, b = short(pid, pack)
        cells = p["_cells"]
        # must equal shell.write_site's: the slashes in "map/grants/<pid>/index.html"
        up = "../" * (pid.count("/") + 3)
        # the grant, tool by tool
        tool_blocks = []
        for t in p["tools"]:
            trows = []
            for r in t["grant"]:
                c = pack["cap_by_id"].get(r["capability"])
                if not c:
                    continue
                ct = r.get("control_tier") or "none"
                trows.append([f"[{c['label']}]({cap_href(c['id'])}) `{c['id']}`",
                              f"{GLYPH[ct]} {ct}", r.get("tier") or "derived",
                              (r.get("control") or "—") + (f" · *{r['note']}*" if r.get("note") else "")])
            ev = t.get("evidence")
            tool_blocks.append(("h3", f"{t['tool']}" + (f" — measured, `{ev}`" if ev else "")))
            tool_blocks.append(("table", ["Capability", "Control", "Evidence", "What is on the path"], trows))
        # this profile's single-column matrix, for orientation
        mh1, mm1 = grants_matrix(pack, up, [p])
        # reaches: what host / tenant / world mean here
        rn = p.get("reach_names", {})
        reach_rows = [[k, v] for k, v in rn.items()]
        # not reachable, with why
        nr_rows = [[x["what"], x["why"], x.get("source", "")] for x in p.get("not_reachable", [])]
        # reductions that apply
        red_rows = []
        for cid in sorted(cells):
            r = pack["reductions"].get(cid)
            if r:
                red_rows.append([f"[{pack['cap_by_id'][cid]['label']}]({cap_href(cid)})",
                                 r["setting"], r["costs"], r["tier_after"]])
        # mandates that apply, with their delta tallies
        mand_rows = []
        for m in pack["mandates"]:
            if pid in m["applies_to"]:
                d = delta(m, p)
                e = sum(1 for v in d.values() if v == "excess")
                s = sum(1 for v in d.values() if v == "shortfall")
                mand_rows.append([f"[{m['label']}]({mand_href(m['id'])})", f"▲ {e}", f"▼ {s}"])
        blocks = [
          ("crumb", f"[Play](index.html) / [The map](map/index.html) / [The products](map/grants/index.html) / {a} — {b}"),
          ("h1", f"{p['product']}"),
          ("lead", p["description"]),
          ("p", f"**{p['vendor']}** · surface `{p['surface']}` · variant `{p['variant']}` · profile "
                f"version `{p['version']}` · reaches **{len(cells)}** of {n_cap} capabilities, "
                f"**{len(p['irreversible_in_union'])}** of which cannot be undone. "
                f"[Edit this profile]({GH_EDIT}profiles/{pid}.json) · [the file]({GH_BLOB}profiles/{pid}.json)."),
          ("both", mh1, mm1),
          ("h2", "What host, tenant and world mean here"),
          ("table", ["Reach", "Here, it means"], reach_rows) if reach_rows else
          ("p", "The profile uses the primitives' default reach names."),
        ]
        if nr_rows:
            blocks += [("h2", "What it cannot reach, and why"),
                       ("table", ["What", "Why", "Source"], nr_rows)]
        blocks += [("h2", "The grant, tool by tool"),
                   ("p", "Two tools in one session reach different things, which is why the unit of "
                         "mapping is the tool and not the product. Each row carries the control on "
                         "the path and the tier of evidence behind it.")]
        blocks += tool_blocks
        if red_rows:
            blocks += [("h2", "What narrows it"),
                       ("p", "For each capability in the grant: the specific setting or arrangement "
                             "that narrows it, what it costs, and the tier the control reaches "
                             "afterwards. Guidance is free and stays free."),
                       ("table", ["Capability", "The setting", "What it costs", "Tier after"], red_rows)]
        if mand_rows:
            blocks += [("h2", "Against the mandates"),
                       ("p", "What a reasonable person wanted from this setup, and the gap: "
                             "▲ excess is what it can do that they did not want; ▼ shortfall is what "
                             "they wanted that it cannot do."),
                       ("table", ["Mandate", "Excess", "Shortfall"], mand_rows)]
        blocks += [("h2", "Sources"),
                   ("ul", [f"`{s}`" for s in p.get("sources", [])] or ["none recorded"]),
                   ("note", "A **derived** row is an inference from what this kind of program "
                            "architecturally is. It is a claim, and the most useful pull request "
                            "on this page is one that replaces a claim with a probe run — "
                            "[how](map/contribute/index.html).")]
        P[prof_href(pid)] = {"title": f"{a} — {b}",
                             "description": f"{p['product']}: what it can reach, tool by tool, "
                                            f"with the control on the path and the evidence "
                                            f"behind each row.",
                             "blocks": blocks}

    # ---- /map/capabilities/ ------------------------------------------------
    cap_rows = []
    for fam, fam_desc, caps in by_family(pack):
        for c in caps:
            granters = [p for p in pack["profiles"] if c["id"] in p["_cells"]]
            cap_rows.append([f"[{c['label']}]({cap_href(c['id'])})", f"`{c['id']}`", fam,
                             c["reversible"], str(len(granters)),
                             "yes" if c["id"] in pack["reductions"] else "—"])
    P["map/capabilities/index.html"] = {
      "title": "The capabilities",
      "description": f"The {n_cap} capability primitives every question is built from: a verb, "
                     "an object class and a reach, each carrying whether its effect can be undone.",
      "blocks": [
        ("crumb", "[Play](index.html) / [The map](map/index.html) / The capabilities"),
        ("h1", "The capabilities"),
        ("lead", "A capability is a **verb** crossed with an **object class** crossed with a "
                 "**reach**, carrying whether its effect can be undone. *Read a file in the "
                 "project* and *read a file anywhere the account can* are two capabilities; "
                 "`/etc/passwd` is not a third — a specific path is an instance, never a new "
                 "primitive."),
        ("table", ["Capability", "Id", "Family", "Undo", "Granted by", "Reduction"], cap_rows),
        ("h2", "The rules the set is written under"),
        ("ul", [r if isinstance(r, str) else json.dumps(r) for r in pack["primitives"]["rules"]]),
        ("h2", "Reach"),
        ("table", ["Reach", "Means"], [[k, v] for k, v in pack["reaches"].items()]),
        ("p", "Reach is the axis people get wrong. *Host* for an agent in a vendor's container "
              "is the container, and *tenant* is a scoped token; each product's page says what "
              "the words mean there."),
      ]}
    for c in pack["caps"]:
        cid = c["id"]
        granters = []
        for p in pack["profiles"]:
            cell = p["_cells"].get(cid)
            if cell:
                a, b = short(p["id"], pack)
                granters.append([f"[{a} — {b}]({prof_href(p['id'])})",
                                 f"{GLYPH[cell['control']]} {cell['control']}", cell["evidence"],
                                 ", ".join(dict.fromkeys(cell["tools"]))])
        red = pack["reductions"].get(cid)
        qs = [q for q in pack["questions"] if q.get("asks_about") == cid]
        wants = [m for m in pack["mandates"] if cid in m["want"]]
        nos = [m for m in pack["mandates"] if cid in m["do_not_want"]]
        blocks = [
          ("crumb", f"[Play](index.html) / [The map](map/index.html) / [The capabilities](map/capabilities/index.html) / {c['label']}"),
          ("h1", c["label"]),
          ("lead", f"`{cid}` — **{c['verb']}** × **{c['object']}** at **{c['reach']}** reach "
                   f"({pack['reaches'].get(c['reach'], '')}). Family: {c['family']}. "
                   f"Effect: **{REV_LABEL[c['reversible']]}**."),
          ("h2", f"Granted by {len(granters)} of {n_prof}"),
          ("table", ["Profile", "Control on the path", "Evidence", "Via"], granters) if granters else
          ("p", "No profile in the set grants this capability."),
        ]
        if red:
            blocks += [("h2", "What narrows it"),
                       ("p", f"**The setting:** {red['setting']}"),
                       ("p", f"**What it costs:** {red['costs']}"),
                       ("p", f"**Tier after:** {red['tier_after']}")]
        if qs:
            blocks += [("h2", "Questions that ask about it"),
                       ("ul", [f"*{q['label']}* — {q.get('cls','')}, reliability {q.get('reliability','')}" for q in qs])]
        if wants or nos:
            blocks += [("h2", "In the mandates"),
                       ("ul", ([f"**wanted** by [{m['label']}]({mand_href(m['id'])})" for m in wants]
                               + [f"**not wanted** by [{m['label']}]({mand_href(m['id'])})" for m in nos]))]
        blocks += [("p", f"[Edit the primitives]({GH_EDIT}primitives.json) · "
                         f"[edit the reductions]({GH_EDIT}reductions.json)")]
        P[cap_href(cid)] = {"title": c["label"], "description": f"{cid}: which products grant "
                            "it, what stands in the way, what narrows it, and who wants it.",
                            "blocks": blocks}

    # ---- /map/mandates/ ----------------------------------------------------
    mand_tbl = []
    for m in pack["mandates"]:
        profs = [pack["prof_by_id"][pid] for pid in m["applies_to"]]
        tot_e = tot_s = 0
        for p in profs:
            d = delta(m, p)
            tot_e += sum(1 for v in d.values() if v == "excess")
            tot_s += sum(1 for v in d.values() if v == "shortfall")
        mand_tbl.append([f"[{m['label']}]({mand_href(m['id'])})", ", ".join(m["surface"]),
                         str(len(m["want"])), str(len(m["do_not_want"])),
                         str(len(profs)), f"▲ {tot_e}", f"▼ {tot_s}"])
    P["map/mandates/index.html"] = {
      "title": "The mandates",
      "description": "What a reasonable person wanted from each kind of setup, stated per "
                     "capability — a starting set, written to be argued with.",
      "blocks": [
        ("crumb", "[Play](index.html) / [The map](map/index.html) / The mandates"),
        ("h1", "What people wanted — the mandates"),
        ("lead", "A **grant** is what the system allows. A **mandate** is what you meant to "
                 "authorise. Nobody writes the second one down, so here are starting drafts: "
                 "for each kind of setup, what a reasonable person wanted the agent to do, what "
                 "they did not, and what they never thought about."),
        ("note", "**These were not measured or surveyed.** Each is a first draft written by the "
                 "site to have something to show a delta against. They are meant to be wrong in "
                 "places, and a pull request that changes one is the intended way to say so. The "
                 "game hands every player a mandate of their own at the end of a run; what we "
                 "learn from those, anonymously, will change these."),
        ("table", ["Mandate", "Surface", "Wants", "Does not want", "Profiles", "Excess", "Shortfall"], mand_tbl),
        ("p", "Excess and shortfall are totals across the profiles a mandate applies to. "
              "[The deltas, as matrices](map/deltas/index.html)."),
      ]}
    dl_h, dl_m = delta_legend()
    for m in pack["mandates"]:
        profs = [pack["prof_by_id"][pid] for pid in m["applies_to"]]
        dh, dm, counts = delta_matrix(pack, "../../../", m, profs)
        want_rows = [[f"[{pack['cap_by_id'][c]['label']}]({cap_href(c)})", "want",
                      m.get("notes", {}).get(c, "")] for c in m["want"]]
        no_rows = [[f"[{pack['cap_by_id'][c]['label']}]({cap_href(c)})", "do not want",
                    m.get("notes", {}).get(c, "")] for c in m["do_not_want"]]
        unstated = [c["id"] for c in pack["caps"] if c["id"] not in m["want"] and c["id"] not in m["do_not_want"]]
        un_rows = [[f"[{pack['cap_by_id'][c]['label']}]({cap_href(c)})", "unstated",
                    m.get("notes", {}).get(c, "")] for c in unstated if m.get("notes", {}).get(c)]
        excess_lines = []
        for p in profs:
            d = delta(m, p)
            ex = [pack["cap_by_id"][c]["label"] for c, v in d.items() if v == "excess"]
            sh = [pack["cap_by_id"][c]["label"] for c, v in d.items() if v == "shortfall"]
            a, b = short(p["id"], pack)
            excess_lines.append(f"**{a} — {b}:** " + (f"excess — {'; '.join(ex)}. " if ex else "no excess. ")
                                + (f"Shortfall — {'; '.join(sh)}." if sh else "No shortfall."))
        P[mand_href(m["id"])] = {
          "title": m["label"],
          "description": f"A starting mandate for {', '.join(m['surface'])}: {m['description'][:140]}…",
          "blocks": [
            ("crumb", f"[Play](index.html) / [The map](map/index.html) / [The mandates](map/mandates/index.html) / {m['label']}"),
            ("h1", m["label"]),
            ("lead", m["description"]),
            ("p", f"Status: **{m['status']}** · authored {m['authored']} · {m['authored_by']} · "
                  f"[edit this mandate]({GH_EDIT}mandates/{m['id']}.json)"),
            ("h2", "The delta"),
            ("p", "Against every profile this mandate applies to. ▲ is authority you did not ask "
                  "for; ▼ is something you were counting on that is not there. The tally is at the "
                  "bottom."),
            ("both", dl_h, dl_m),
            ("both", dh, dm),
            ("h2", "In words"),
            ("ul", excess_lines),
            ("h2", "The mandate, row by row"),
            ("table", ["Capability", "Position", "Note"], want_rows + no_rows + un_rows),
            ("note", "**You cannot deny the excess rows.** The agent already has the access. What "
                     "is left is how long you are prepared to live with each one and who says so "
                     "— [what to do next](what-next/index.html)."),
          ]}

    # ---- /map/deltas/ — the overview ---------------------------------------
    ov_rows = []
    league = []
    for m in pack["mandates"]:
        for pid in m["applies_to"]:
            p = pack["prof_by_id"][pid]
            d = delta(m, p)
            e = sum(1 for v in d.values() if v == "excess")
            s = sum(1 for v in d.values() if v == "shortfall")
            hid = sum(1 for c, v in d.items() if v == "excess" and pack["cap_by_id"][c]["reversible"] == "no")
            a, b = short(pid, pack)
            ov_rows.append([f"[{m['label']}]({mand_href(m['id'])})", f"[{a} — {b}]({prof_href(pid)})",
                            f"▲ {e}", f"▼ {s}", str(hid)])
            league.append((e, hid, f"{a} — {b}", m["label"], pid, m["id"]))
    league.sort(key=lambda x: (-x[0], -x[1]))
    lg_rows = [[f"[{n}]({prof_href(pid)})", f"[{ml}]({mand_href(mid)})", str(e), str(hid)]
               for e, hid, n, ml, pid, mid in league]
    P["map/deltas/index.html"] = {
      "title": "The deltas",
      "description": "Every mandate against every profile it applies to: how much excess "
                     "authority, how much shortfall, and how much of the excess cannot be undone.",
      "blocks": [
        ("crumb", "[Play](index.html) / [The map](map/index.html) / The deltas"),
        ("h1", "The deltas"),
        ("lead", "The gap between what was granted and what was wanted, for every pairing on "
                 "the site. Two numbers per pairing, and a third that matters more than either: "
                 "how much of the excess is **irreversible** — authority nobody asked for over "
                 "things that cannot be undone."),
        ("table", ["Mandate", "Profile", "Excess", "Shortfall", "Irreversible excess"], ov_rows),
        ("h2", "Ranked by excess"),
        ("p", "Most authority-beyond-the-mandate first. This is not a ranking of danger — a "
              "derived profile with a naive mandate scores high by construction — it is a ranking "
              "of *where the conversation is most overdue*."),
        ("table", ["Profile", "Against", "Excess", "Irreversible"], lg_rows),
        ("note", "Every mandate here is a starting draft and every derived row is a claim. A high "
                 "number is an invitation to correct the mandate, correct the profile, or accept "
                 "the delta for an interval with a name on it — in that order. "
                 "[What to do next](what-next/index.html)."),
      ]}

    # ---- /map/ceiling/ -----------------------------------------------------
    ce_rows = [[c["label"], c["family"], str(c.get("level", "")), "yes" if c.get("attemptable") else "no",
                c["bounded_by"]] for c in pack["ceiling"]]
    P["map/ceiling/index.html"] = {
      "title": "Above the ceiling",
      "description": f"The {len(pack['ceiling'])} things no agent in this set can do, and the "
                     "control outside the agent that stops each one.",
      "blocks": [
        ("crumb", "[Play](index.html) / [The map](map/index.html) / Above the ceiling"),
        ("h1", "Above the ceiling"),
        ("lead", f"{len(pack['ceiling'])} capabilities no agent in any environment in the set "
                 "can reach — bounded by a control outside the whole environment rather than by "
                 "the agent's restraint. They are in the game so it can measure over-crediting; "
                 "[why](the-ceiling/index.html). Here is the list, with what stops each one."),
        ("table", ["Capability", "Family", "Level", "Attemptable", "Bounded by"], ce_rows),
        ("h2", "If attempted"),
        ("ul", [f"**{c['label']}** — {c['if_attempted']}" for c in pack["ceiling"] if c.get("if_attempted")]),
        ("p", f"[Edit the ceiling]({GH_EDIT}ceiling.json). A counter-example — an agent stepping "
              "over one of these — is a correction, not a quibble, and the row names the control "
              "so the claim is checkable."),
      ]}

    # ---- /map/questions/ ---------------------------------------------------
    q_rows = []
    for q in sorted(pack["questions"], key=lambda x: (x.get("cls", ""), x["id"])):
        ab = q.get("asks_about")
        q_rows.append([q["label"], q.get("cls", ""), str(q.get("reliability", "")),
                       f"[{pack['cap_by_id'][ab]['label']}]({cap_href(ab)})" if ab in pack["cap_by_id"] else "—",
                       "yes" if q.get("funny") else ""])
    P["map/questions/index.html"] = {
      "title": "The questions",
      "description": f"{len(pack['questions'])} questions the games ask, with what each is for: "
                     "the seed of a question pack.",
      "blocks": [
        ("crumb", "[Play](index.html) / [The map](map/index.html) / The questions"),
        ("h1", "The questions"),
        ("lead", "A question is data too. Each one carries a **class** — *discriminating* "
                 "questions identify which agent you are thinking of and never count toward the "
                 "score; *eliciting* questions are a prediction about a capability and do — a "
                 "**reliability** (how likely a player is to actually know the answer), and the "
                 "capability it asks about."),
        ("table", ["Question", "Class", "Reliability", "Asks about", "Funny"], q_rows),
        ("h2", "Three kinds of question in the pack"),
        ("ul", [
          f"**These {len(pack['questions'])}** — from the mesh, used by *Which Agent Is It?* to "
          "narrow the field and by the scoreboard where they elicit.",
          f"**The {len(pack['ceiling'])} above the ceiling** — things nothing can do, so the game "
          "measures over-crediting. [The list](map/ceiling/index.html).",
          "**The capability rows themselves** — every filled cell in "
          "[the map](map/index.html) is a *can it?* question the scoreboard can ask.",
        ]),
        ("h2", "Where this goes"),
        ("p", "This is the start of **question packs**: a pack is the primitives, the profiles, "
              "the questions and the mandates, versioned together at one URL. The public one is "
              "this. A team could fork it, add their own profiles and their own mandates — the "
              "products they actually run, the authority they actually meant to grant — and "
              "point the game at theirs. [The pack](data/index.html)."),
      ]}

    # ---- /map/contribute/ ---------------------------------------------------
    P["map/contribute/index.html"] = {
      "title": "Contribute",
      "description": "How to change the map: a row, a profile, a mandate or a correction, as a "
                     "pull request against the data pack.",
      "blocks": [
        ("crumb", "[Play](index.html) / [The map](map/index.html) / Contribute"),
        ("h1", "Change the map"),
        ("lead", "Everything on the map is generated from JSON in one folder of one repository. "
                 "Change the JSON, open a pull request, and the pages change on the next build. "
                 "There is no other way to edit them, on purpose."),
        ("h2", "What is worth contributing, most valuable first"),
        ("ol", [
          "**A measurement that replaces a claim.** Most rows are *derived*. Run the probes on a "
          "real instance, attach the evidence file, change the row's tier. This is the single "
          "most useful thing anyone can do to this map.",
          "**A profile that is missing.** A product you use, or a setup of one — a container, a "
          "corporate-managed desktop, confirmations off. One file under `data/profiles/`, named "
          "`<vendor>/<product>/<variant>.json`, listed in `index.json`. Label every row's tier "
          "honestly; a derived profile is welcome and says it is derived.",
          "**A mandate you disagree with.** Every one under `data/mandates/` is a first draft. "
          "Change a row from *want* to *do not want*, add a note saying why, and that is an "
          "argument the site can show.",
          "**A capability the set is missing.** Only if it is a new verb, object class or reach — "
          "a specific path or host is an instance of an existing one. New primitives need a probe.",
        ]),
        ("h2", "The files"),
        ("table", ["File", "What it is", "Who edits it"],
         [["`data/primitives.json`", "the capability vocabulary", "rarely — a new verb, object or reach"],
          ["`data/profiles/<vendor>/<product>/<variant>.json`", "one product in one setup, tool by tool", "anyone who runs that product"],
          ["`data/profiles/index.json`", "the manifest of profiles", "add a line when you add a file"],
          ["`data/reductions.json`", "what narrows each capability, and what it costs", "anyone with a better setting"],
          ["`data/ceiling.json`", "what nothing can do, and the control that stops it", "anyone with a counter-example"],
          ["`data/mandates/<id>.json`", "what a reasonable person wanted, per setup", "anyone who disagrees"],
          ["`data/mesh/`", "the graph the levels are derived from", "compiled — edit the sources"],
          ["`data/pack.json`", "the manifest the game reads", "generated by the build; do not edit"]]),
        ("h2", "The shape of a profile row"),
        ("pre", '{ "capability": "read.file.host",\n'
                '  "tier": "derived",          // derived · documented · measured · observed\n'
                '  "control": "the tool\'s own directory restriction and its confirmation prompt",\n'
                '  "control_tier": "setting",  // none · expectation · setting · boundary\n'
                '  "note": "outside the working tree only with the prompt, which the shell does not need" }'),
        ("p", "`tier` is how the row is known. `control_tier` is what stands on the path: *none*; "
              "an *expectation* somebody wrote down; a *setting* the agent's own account could "
              "change; a *boundary* enforced above it. The matrix is coloured by the second and "
              "the tooltip names the first."),
        ("h2", "What the build checks"),
        ("p", "The release gate refuses a pull request whose data does not hold together: every "
              "capability id in every profile, reduction, mandate and ceiling row must exist in "
              "the primitives; every profile in the index must exist on disk; a profile's stated "
              "union must equal what its rows imply; a mandate cannot both want and not want the "
              "same capability. If it merges, the map is consistent."),
        ("h2", "Where the data came from"),
        ("p", f"The primitives, profiles, reductions, ceiling and mesh were built at "
              f"[pki.sgit.ai]({PKI_PROBES}) under CC BY 4.0 and vendored here on 6 September "
              f"2026 so that this site could be their home for contribution. The mandates were "
              f"authored here. [Provenance]({GH_BLOB}PROVENANCE.md)."),
        ("p", f"[Open a pull request]({GH}/pulls) · [the data folder]({GH_BLOB})"),
      ]}

    # ---- /data/ — the pack -------------------------------------------------
    P["data/index.html"] = {
      "title": "The data pack",
      "description": "The map as JSON at a stable URL with CORS: primitives, profiles, "
                     "reductions, ceiling, mesh, questions and mandates, versioned together. This "
                     "is what the game reads.",
      "blocks": [
        ("crumb", "[Play](index.html) / [The map](map/index.html) / The data pack"),
        ("h1", "The data pack"),
        ("lead", "Everything the map is drawn from, as JSON, served from this site with CORS "
                 "open — so the game inside the vault reads it from here, and so can you."),
        ("pre", f"{PACK_BASE}pack.json"),
        ("p", "`pack.json` is the manifest: the version, a content hash, and the path of every "
              "file. The game fetches the manifest and follows it. Change a file, merge, and the "
              "next build stamps a new hash — a pack is versioned as a whole, never a file at a "
              "time."),
        ("h2", "What is in it"),
        ("table", ["Path", "Type", "What"],
         [["`primitives.json`", "capability-primitives/v1", "the capability vocabulary — verbs, objects, reaches, families, reversibility"],
          ["`profiles/index.json` → `profiles/…`", "profiles-index/v1, profile/v1", "one product in one setup, tool by tool"],
          ["`reductions.json`", "reductions/v1", "what narrows each capability, what it costs, the tier after"],
          ["`ceiling.json`", "ceiling-capabilities/v1", "what nothing can do, and why"],
          ["`mesh/ontology.json`, `mesh/graph.json`", "ontology/v1, mesh/v1", "the typed graph the levels are derived from"],
          ["`tree.json`", "question tree", "the questions *Which Agent Is It?* asks, with reliability"],
          ["`picker.json`", "picker", "the what → where → which → how entry flow"],
          ["`mandates/index.json` → `mandates/…`", "mandates-index/v1, mandate/v1", "what a reasonable person wanted, per setup — starting drafts"]]),
        ("h2", "Packs"),
        ("p", "This is the **public pack**. The idea it starts is that a pack is a unit: the "
              "products, the capabilities, the questions and the mandates, together, at one "
              "URL. A team that runs different products, or has decided what its agents may do, "
              "forks this folder, edits it, hosts it anywhere with CORS, and points the game at "
              "its manifest. The game's logic does not change; the world it asks about does."),
        ("p", "What a customised pack changes: which profiles the picker offers, what each row "
              "claims, which questions are asked, and which mandate the delta is drawn against. "
              "What it cannot change: the scoring rule, the level derivation, the ceiling's "
              "share of the set — those are the engine's, and they are what make one pack's "
              "scores comparable with another's."),
        ("h2", "For the game"),
        ("p", "The game currently vendors this data at build time with a dated snapshot, and takes "
              "`?live=1` to fetch instead. Pointing the live path at this pack's base URL is the "
              "handover — and the manifest's hash is what tells a running game whether its "
              "snapshot is behind."),
        ("p", f"[The folder on GitHub]({GH_BLOB}) · [how to contribute](map/contribute/index.html)"),
      ]}
    return P, pack


def write_pack(root, version, pack):
    """data/pack.json — the manifest the game fetches. Generated: counts and a content hash over
    every file in the pack, so a change anywhere is a new pack version."""
    d = Path(root) / "data"
    files = sorted(p for p in d.rglob("*.json") if p.name != "pack.json")
    h = hashlib.sha256()
    for p in files:
        h.update(p.relative_to(d).as_posix().encode())
        h.update(p.read_bytes())
    manifest = {
        "type": "pack/v1",
        "id": "what-can-it-do-public",
        "name": "What Can It Do? — the public pack",
        "_what_this_is": "The manifest of the data pack the game reads: the capability "
                         "vocabulary, the profiles, the reductions, the ceiling, the mesh, the "
                         "questions and the starting mandates, versioned together. Generated by "
                         "the site build; do not edit — edit the files it names.",
        "version": version,
        "content_hash": "sha256:" + h.hexdigest(),
        "base": PACK_BASE,
        "licence": "CC BY 4.0",
        "provenance": "PROVENANCE.md",
        "files": {
            "vocabulary": "vocabulary.json",
            "primitives": "primitives.json",
            "profiles": "profiles/index.json",
            "reductions": "reductions.json",
            "ceiling": "ceiling.json",
            "picker": "picker.json",
            "mesh": {"ontology": "mesh/ontology.json", "graph": "mesh/graph.json"},
            "questions": {"tree": "tree.json", "mesh": "mesh/graph.json#type=question",
                          "ceiling": "ceiling.json"},
            "mandates": "mandates/index.json",
        },
        "counts": {
            "profiles": len(pack["profiles"]),
            "capabilities": len(pack["caps"]),
            "reductions": len(pack["reductions"]),
            "ceiling": len(pack["ceiling"]),
            "questions": len(pack["questions"]),
            "mandates": len(pack["mandates"]),
            "files": len(files),
        },
    }
    (d / "pack.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest
