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
- `map/` — **generated**: the grants matrix, a page per product, per capability, per mandate,
  the deltas, the ceiling, the questions, how to contribute
- `data/` — the pack the map is generated from, and the manifest the game reads
- `briefs/` — plans, open for review: `00__PLAN__vaults-and-packs.md` is the vault split, question packs, and the Mavs PoC
- `admin/proposals/drain.py` — turns sealed proposals from the map vault (`mxhepww5`) into pull requests against `data/`, and writes `data/proposals.json`

## The map, and the data pack

`data/` is the **contribution surface**: the capability primitives, the nine profiles (what each
product can reach, tool by tool, with an evidence tier and a control tier on every row), the
reductions, the ceiling, the mesh, the questions and eight starting mandates — as JSON, under
CC BY 4.0. Everything under `/map/` is generated from it by `admin/build/map_pages.py`, and
nothing on those pages is typed in: **change the JSON, open a pull request, and the map
changes on the next build.**

The pack is served with CORS open at `https://what-can-it-do.games.sgit.ai/data/pack.json`,
which is how the game — whose scoring and levels stay in the vault — reads it. A team that runs
different products, or has decided what its agents may do, forks `data/`, edits it, hosts it
anywhere with CORS and points the game at its manifest: that is a *pack*, and this is the
public one.

The release gate refuses a pull request whose data does not hold together: every capability id
in every profile, reduction, mandate and ceiling row must exist; every indexed file must exist;
a profile's stated union must equal what its rows imply; a mandate cannot both want and refuse
the same capability; every tier must be in `data/vocabulary.json`. See
[`data/PROVENANCE.md`](data/PROVENANCE.md) for where it came from and
[/map/contribute/](https://what-can-it-do.games.sgit.ai/map/contribute/) for what is worth
contributing.

## The game is embedded, not copied

It lives in encrypted vault `pg87npy3` (v1.0.0, 9 September 2026 — its own vault since then; the version that shipped inside the two-game vault `4evnlwrj` is locked there on branch `release-2026-09-09`). The game reads `data/` from this site on every load. `assets/vault-app-embed.js` opens it over
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

The read key for vault `pg87npy3` is published on purpose — it is what lets a player open the
game's source and check it. It cannot write. The vault key is not published and never will be.

## Licence

Content CC BY 4.0. Code under the repository licence.
