#!/usr/bin/env python3
"""The page shell, the nav, the footer, and the block renderers — one definition, two outputs.

Every page on this site exists once, as content, in `build_pages.py`. This module turns that
content into the two surfaces the house pattern requires:

  · the `.html` page a person reads, and
  · the `.md` twin an agent reads,

from the SAME block list. That is the whole point of doing it this way rather than by hand:
sgit.ai says of every twin "this file is generated from the same content as the page, so the
two cannot drift", and a generator is the only way that sentence stays true. wardley-maps and
pki keep hand-written HTML and inject only the chrome; sgit.ai itself generates whole pages
from one template. This site takes the sgit.ai route, because a games catalogue is mostly the
same page shape repeated and hand-copying that shape is how a nav goes stale in three places.

The block vocabulary is deliberately small. If a page needs something outside it, that is a
signal the content wants rethinking — not a signal to reach for ("raw", ...), which exists for
the two or three places a table or a figure genuinely has no markdown equivalent.
"""
import html
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# inline markup: the same source string has to work in HTML and in markdown, so
# the content is written with markdown's inline syntax and converted for HTML.
# Deliberately three constructs and no more — bold, code, links.
# ---------------------------------------------------------------------------

_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD = re.compile(r"\*\*([^*]+)\*\*")
_EM   = re.compile(r"(?<![*\w])\*([^*]+)\*(?!\*)")
_CODE = re.compile(r"`([^`]+)`")
# A maturity rung is content, not decoration, so it gets its own inline construct rather than
# a raw-HTML escape hatch: `{{rung:scored}}`. Two reasons it has to be a construct. A raw span
# in the content would be escaped into visible tag soup (it was, before this existed), and
# unescaping it would put HTML in the markdown twin, which is the one thing the twin must not
# contain. This way the HTML gets a pill, the twin gets `scored`, and validate.js check 6 can
# still read the label back out of the rendered span.
_RUNG = re.compile(r"\{\{rung:([a-z]+)\}\}")


def inline_html(s, up=""):
    """Markdown inline -> HTML. Relative links get the page's `up` prefix, so content is
    written once with root-relative paths and works at any directory depth."""
    out = html.escape(s, quote=False)
    # Code first: nothing inside backticks should be re-read as markup.
    holds = []

    def stash(m):
        holds.append(f"<code>{m.group(1)}</code>")
        return f"\x00{len(holds) - 1}\x00"

    out = _CODE.sub(stash, out)
    out = _RUNG.sub(lambda m: f'<span class="rung rung-{m.group(1)}">{m.group(1)}</span>', out)
    out = _LINK.sub(lambda m: f'<a href="{_href(m.group(2), up)}">{m.group(1)}</a>', out)
    out = _BOLD.sub(r"<b>\1</b>", out)
    out = _EM.sub(r"<em>\1</em>", out)
    out = re.sub(r"\x00(\d+)\x00", lambda m: holds[int(m.group(1))], out)
    return out


def inline_md(s, up=""):
    """Markdown inline -> markdown. Almost the identity function; the work is rewriting
    internal links to point at the twin's neighbours (`.md`, not `.html`)."""
    def fix(m):
        href = m.group(2)
        if href.startswith(("http", "mailto:", "#")):
            return m.group(0)
        return f"[{m.group(1)}]({_href(href, up).replace('.html', '.md')})"
    return _LINK.sub(fix, _RUNG.sub(r"`\1`", s))


def _href(href, up):
    if href.startswith(("http", "mailto:", "#")):
        return href
    return up + href.lstrip("/")


def strip(s):
    """Inline markup -> plain text, for og:description and llms.txt."""
    s = _LINK.sub(r"\1", _RUNG.sub(r"\1", s))
    return s.replace("**", "").replace("`", "").replace("*", "")


# ---------------------------------------------------------------------------
# blocks
# ---------------------------------------------------------------------------

def render_html(blocks, up):
    out = []
    for kind, *args in blocks:
        if kind == "crumb":
            out.append(f'<p class="crumb">{inline_html(args[0], up)}</p>')
        elif kind == "h1":
            out.append(f"<h1>{inline_html(args[0], up)}</h1>")
        elif kind == "lead":
            out.append(f'<p class="lead">{inline_html(args[0], up)}</p>')
        elif kind in ("h2", "h3"):
            anchor = _slug(strip(args[0]))
            out.append(f'<{kind} id="{anchor}">{inline_html(args[0], up)}</{kind}>')
        elif kind == "p":
            out.append(f"<p>{inline_html(args[0], up)}</p>")
        elif kind in ("ul", "ol"):
            items = "".join(f"<li>{inline_html(i, up)}</li>" for i in args[0])
            out.append(f"<{kind}>{items}</{kind}>")
        elif kind == "note":
            out.append(f'<div class="note">{inline_html(args[0], up)}</div>')
        elif kind == "disclose":
            out.append(f'<div class="disclose">{inline_html(args[0], up)}</div>')
        elif kind == "pre":
            out.append(f'<pre class="shell">{html.escape(args[0])}</pre>')
        elif kind == "table":
            head = "".join(f"<th>{inline_html(h, up)}</th>" for h in args[0])
            rows = "".join(
                "<tr>" + "".join(f"<td>{inline_html(c, up)}</td>" for c in r) + "</tr>"
                for r in args[1])
            out.append(f'<div class="tablewrap"><table><thead><tr>{head}</tr></thead>'
                       f"<tbody>{rows}</tbody></table></div>")
        elif kind == "cards":
            cards = []
            for c in args[0]:
                foot = f'<div class="foot">{inline_html(c["foot"], up)}</div>' if c.get("foot") else ""
                cards.append(f'<div class="gamecard"><h3>{inline_html(c["title"], up)}</h3>'
                             f'<p class="sub">{inline_html(c["sub"], up)}</p>{foot}</div>')
            out.append(f'<div class="gamegrid">{"".join(cards)}</div>')
        elif kind == "embed":
            out.append(embed_html(args[0]))
        elif kind == "raw":
            out.append(args[0])
        else:
            raise SystemExit(f"unknown block kind: {kind}")
    return "\n  ".join(out)


def render_md(blocks, up):
    out = []
    for kind, *args in blocks:
        if kind in ("crumb", "lead", "p"):
            out.append(inline_md(args[0], up))
        elif kind == "h1":
            out.append(f"# {inline_md(args[0], up)}")
        elif kind == "h2":
            out.append(f"## {inline_md(args[0], up)}")
        elif kind == "h3":
            out.append(f"### {inline_md(args[0], up)}")
        elif kind == "ul":
            out.append("\n".join(f"- {inline_md(i, up)}" for i in args[0]))
        elif kind == "ol":
            out.append("\n".join(f"{n}. {inline_md(i, up)}" for n, i in enumerate(args[0], 1)))
        elif kind in ("note", "disclose"):
            out.append("> " + inline_md(args[0], up).replace("\n", "\n> "))
        elif kind == "pre":
            out.append("```\n" + args[0] + "\n```")
        elif kind == "table":
            head = "| " + " | ".join(args[0]) + " |"
            rule = "|" + "|".join("---" for _ in args[0]) + "|"
            rows = "\n".join("| " + " | ".join(inline_md(c, up) for c in r) + " |" for r in args[1])
            out.append(f"{head}\n{rule}\n{rows}")
        elif kind == "cards":
            out.append("\n\n".join(
                f'**{inline_md(c["title"], up)}** — {inline_md(c["sub"], up)}'
                + (f'\n{inline_md(c["foot"], up)}' if c.get("foot") else "")
                for c in args[0]))
        elif kind == "embed":
            cfg = args[0]
            out.append(f'*[A live vault surface here in the HTML page — the game running out of '
                       f'vault `{cfg["vault"]}`. In this markdown twin, '
                       f'[open it in the vault UI]({cfg.get("open_url", "")}).]*')
        elif kind == "raw":
            continue  # a raw HTML block has no markdown equivalent, by definition
    return "\n\n".join(out)


def embed_html(cfg):
    """The Option A embed: the official SG/Vault UI over the embed protocol, app-only.

    `chromeless` drops the surface label — for the player site, where the game should be the
    only thing on the screen. `breakout` lets a wide viewport give the board more width than
    the text measure allows, which the sgit.ai vault page says the games actually need."""
    attrs = [
        'class="sgv-app' + (" sgv-breakout" if cfg.get("breakout", True) else "") + '"',
        f'data-vault="{cfg["vault"]}"',
        f'data-readkey="{cfg["readkey"]}"',
    ]
    if cfg.get("entry"):
        attrs.append(f'data-entry="{cfg["entry"]}"')
    if cfg.get("chromeless"):
        attrs.append('data-chromeless="1"')
    if cfg.get("browser"):
        attrs.append('data-browser="1"')
    return f'<div {" ".join(attrs)}></div>'


def _slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]


# ---------------------------------------------------------------------------
# chrome
# ---------------------------------------------------------------------------

def nav_html(site, nav, rel, up, version):
    groups = []
    for label, own, subs, prefixes in nav:
        active = rel == own or any(rel.startswith(p) for p in prefixes)
        links = "\n".join(
            f'      <a class="sl{" here" if h == rel else ""}" href="{up}{h}">{t}</a>'
            for t, h in subs)
        if subs:
            groups.append(
                '    <div class="ni ni-has">\n'
                f'      <a class="nl{" here" if active else ""}" href="{up}{own}">{label}'
                '<span class="caret">&#9662;</span></a>\n'
                f'      <div class="sub">\n{links}\n      </div>\n'
                "    </div>")
        else:
            groups.append(f'    <div class="ni"><a class="nl{" here" if active else ""}" '
                          f'href="{up}{own}">{label}</a></div>')
    brand, dot = site["brand"]
    return (
        '<nav class="site"><div class="row">\n'
        f'  <a class="brand" href="{up}index.html">{brand}<span>{dot}</span></a>\n'
        f'  <a class="parent" href="{site["parent"]}" title="{site["parent_title"]}">'
        f'↗ part of <b>{site["parent_label"]}</b></a>\n'
        f'  <span class="stage-pill">{site["stage"]}</span>\n'
        f'  <a class="ver" href="{up}admin/versions.html" title="Site release history">{version}</a>\n'
        '  <button class="nav-toggle" type="button" aria-expanded="false" aria-label="Menu">Menu</button>\n'
        f'  <div class="nav-items">\n{chr(10).join(groups)}\n  </div>\n'
        f'  <a class="gh" href="{site["github"]}">&#9733; GitHub</a>\n'
        f'  <script src="{up}assets/nav.js" defer></script>\n'
        "</div></nav>")


def footer_html(site, footer, rel, up, version):
    cols = "\n".join(
        "  <div>\n"
        f"    <h4>{head}</h4>\n"
        + "\n".join(f'    <a href="{l if l.startswith("http") else up + l}">{t}</a>'
                    for t, l in links)
        + "\n  </div>"
        for head, links in footer)
    brand, dot = site["brand"]
    md_twin = (f' · <a href="{up}{rel.replace(".html", ".md")}">this page as markdown</a>')
    return (
        '<footer class="site"><div class="cols">\n'
        "  <div>\n"
        f'    <div class="brandline">{brand}<span>{dot}</span></div>\n'
        f'    <p>{site["blurb"].format(up=up)}</p>\n'
        f'    <p class="netline">{site["netline"]}</p>\n'
        f'    <p class="partnote">{site["telemetry_note"].format(up=up)}</p>\n'
        f'    <p class="verline">site <a href="{up}admin/versions.html">{version}</a> · '
        f'<a href="{up}admin/index.html">engineering</a> · '
        f'<a href="{up}llms.txt">llms.txt</a> · CC BY 4.0{md_twin}</p>\n'
        f"  </div>\n{cols}\n</div></footer>")


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://{host}/{rel}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{host}">
<meta property="og:url" content="https://{host}/{rel}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta name="twitter:card" content="summary">
<link rel="alternate" type="text/markdown" href="{mdname}" title="This page as markdown">
<link rel="icon" href="{up}assets/favicon.svg" type="image/svg+xml">
<link rel="mask-icon" href="{up}assets/favicon.svg" color="#0f766e">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body>

{nav}

<main class="doc">
  {body}
</main>

{footer}
{scripts}</body>
</html>
"""

MD = """# {plain_title}

> {description}

*Source: <https://{host}/{rel}> · site {version} · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

{body}

---

*[Site index for agents]({up}llms.txt) · [HTML version](https://{host}/{rel})*
"""


def write_site(root, site, nav, footer, pages, version, version_log):
    """Emit every page, its twin, llms.txt and sitemap.xml. Returns a summary line."""
    root = Path(root)
    written = []
    for rel, page in pages.items():
        up = "../" * (rel.count("/"))
        blocks = page["blocks"]
        needs_embed = any(b[0] == "embed" for b in blocks)
        scripts = (f'<script src="{up}assets/vault-app-embed.js" defer></script>\n'
                   if needs_embed else "")
        title = f'{page["title"]} — {site["host"]}' if rel != "index.html" else page["title"]
        out = PAGE.format(
            title=html.escape(title, quote=True),
            description=html.escape(strip(page["description"]), quote=True),
            host=site["host"], rel=rel, up=up,
            mdname=Path(rel).name.replace(".html", ".md"),
            nav=nav_html(site, nav, rel, up, version),
            footer=footer_html(site, footer, rel, up, version),
            body=render_html(blocks, up), scripts=scripts)
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(out)
        written.append(rel)

        md = MD.format(
            plain_title=strip(page["title"]), description=strip(page["description"]),
            host=site["host"], rel=rel, version=version, up=up,
            body=render_md(blocks, up))
        (root / rel.replace(".html", ".md")).write_text(md)

    _surfaces(root, site, pages, version, version_log)
    return f"{len(written)} pages + twins, llms.txt, sitemap.xml"


def _surfaces(root, site, pages, version, version_log):
    lines = [f"# {site['host']}", "", f"> {site['tagline']}", "",
             f"Site version: {version}", "",
             "Every page below has a markdown twin generated from the same content as the",
             "HTML page. Fetch the `.md` and you have the page, without the chrome.", "", "## Pages", ""]
    for rel, page in pages.items():
        lines.append(f"- [{strip(page['title'])}](https://{site['host']}/"
                     f"{rel.replace('.html', '.md')}): {strip(page['description'])}")
    lines += ["", "## Release history", ""]
    for v, date, note in version_log[:12]:
        lines.append(f"- {v} ({date}) — {note}")
    (root / "llms.txt").write_text("\n".join(lines) + "\n")

    urls = "".join(
        f"  <url><loc>https://{site['host']}/{rel}</loc>"
        f"<priority>{'1.0' if rel == 'index.html' else '0.7'}</priority></url>\n"
        for rel in pages)
    (root / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    (root / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: https://{site['host']}/sitemap.xml\n")
