# SGit-AI__Website__Game__What-Can-It-Do

Repo for **[what-can-it-do.games.sgit.ai](https://what-can-it-do.games.sgit.ai)** — the
player-facing home of *What Can It Do?*, a five-minute game about whether you can predict what
your AI agent is actually able to do, and whether you wanted it to.

One rule governs every decision in this repo:

> A player arrives from a link somebody sent them. They have no idea what a vault is and they
> should not need to find out.

So the game is mounted and playable on the front page without a click, the vault mechanics get
exactly one page at the bottom of the funnel, and the sibling site
[games.sgit.ai](https://games.sgit.ai) carries the argument, the method and the engineering.

The one thing that is **not** softened is the telemetry notice. The game sends anonymous usage
events; putting it on a public domain extends that obligation rather than discharging it. The
notice sits with the game rather than in a footer, and the release gate fails a page that
mounts the game without one.

## Structure

- `index.html` — the game, playable on arrival
- `how-it-is-scored/` — +30 / −50 / 0, and why wrong costs more than right earns
- `the-ceiling/` — why roughly two in five questions are impossible on purpose
- `what-we-learn/` — exactly what is sent, what is not, and how to switch it off
- `about/` — who made it, what it cannot tell you, and how to open the whole thing

## The game is embedded, not copied

It lives in encrypted vault `4evnlwrj` (v0.16.1). `assets/vault-app-embed.js` opens it over
the SG/Vault **embed protocol**: load the vault host in an iframe, wait for it to report
ready, then hand over the read key by `postMessage` with the target origin pinned — so the
credential never appears in a URL, and therefore never in browser history, a Referer header,
or a server log.

It is the sgit.ai component with the vault-browser surface suppressed, so a player gets a game
rather than a file manager. It uses the real host rather than the smaller read-only one
because the game declares `llm.chat` (its chat panel) and `append.write` (its telemetry lane);
under the minimal host the chat panel is dead and both grants are inert.

## Build

```bash
python3 admin/build/build_pages.py   # pages, .md twins, llms.txt, sitemap, robots
node admin/build/validate.js          # the gate CI will run
```

Every page exists once, as content, in `admin/build/build_pages.py`; nothing under the site
root is hand-edited. Every push to `dev` runs **validate → tag → deploy**.

## Credentials

The read key for vault `4evnlwrj` is published on purpose — it is what lets a player open the
game's source and check it. It cannot write. The vault key is not published and never will be.

## Licence

Content CC BY 4.0. Code under the repository licence.
