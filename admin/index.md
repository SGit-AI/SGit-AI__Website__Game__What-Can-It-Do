# How this site is built

> One content file, generated HTML and markdown twins, and a release gate that fails a page mounting the game without its telemetry notice.

*Source: <https://what-can-it-do.games.sgit.ai/admin/index.html> · site v0.3.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../index.md) / [About](../about/index.md) / How this site is built

# How this site is built

Static files on GitHub Pages. No server, no database, no analytics. Every page exists once, as content, in `admin/build/build_pages.py`; nothing under the site root is hand-edited.

```
python3 admin/build/build_pages.py   # pages, .md twins, llms.txt, sitemap
node admin/build/validate.js          # the gate CI will run
```

## The game is embedded, not copied

`assets/vault-app-embed.js` opens the vault over the SG/Vault **embed protocol**: it loads the vault host in an iframe, waits for that frame to say it is ready, and then hands over the read key by `postMessage` with the target origin pinned. The key never appears in a URL, so it is never in browser history, a Referer header, or a server log.

It is the sgit.ai component with the vault-browser surface suppressed, so a player gets a game rather than a file manager. Using the real host rather than the smaller read-only one is what keeps the game's chat panel and its telemetry lane working — the smaller host serves file reads only.

## The gate

The house checks — version agreement, internal links, canonical host, and a key-leak tripwire — plus one that matters more here than anywhere: **a page that mounts the game must carry the telemetry disclosure.** Mechanical, and deliberately so. The vault this game lives in once shipped two pages saying *nothing sent* on the same screen as events being sent; the notice is not something to rely on remembering.

Full engineering notes are on the sibling site: [games.sgit.ai/admin](https://games.sgit.ai/admin/index.html).

---

*[Site index for agents](../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/admin/index.html)*
