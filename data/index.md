# The data pack

> The map as JSON at a stable URL with CORS: primitives, profiles, reductions, ceiling, mesh, questions and mandates, versioned together. This is what the game reads.

*Source: <https://what-can-it-do.games.sgit.ai/data/index.html> · site v0.6.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../index.md) / [The map](../map/index.md) / The data pack

# The data pack

Everything the map is drawn from, as JSON, served from this site with CORS open — so the game inside the vault reads it from here, and so can you.

```
https://what-can-it-do.games.sgit.ai/data/pack.json
```

`pack.json` is the manifest: the version, a content hash, and the path of every file. The game fetches the manifest and follows it. Change a file, merge, and the next build stamps a new hash — a pack is versioned as a whole, never a file at a time.

## What is in it

| Path | Type | What |
|---|---|---|
| `primitives.json` | capability-primitives/v1 | the capability vocabulary — verbs, objects, reaches, families, reversibility |
| `profiles/index.json` → `profiles/…` | profiles-index/v1, profile/v1 | one product in one setup, tool by tool |
| `reductions.json` | reductions/v1 | what narrows each capability, what it costs, the tier after |
| `ceiling.json` | ceiling-capabilities/v1 | what nothing can do, and why |
| `mesh/ontology.json`, `mesh/graph.json` | ontology/v1, mesh/v1 | the typed graph the levels are derived from |
| `tree.json` | question tree | the questions *Which Agent Is It?* asks, with reliability |
| `picker.json` | picker | the what → where → which → how entry flow |
| `mandates/index.json` → `mandates/…` | mandates-index/v1, mandate/v1 | what a reasonable person wanted, per setup — starting drafts |

## Packs

This is the **public pack**. The idea it starts is that a pack is a unit: the products, the capabilities, the questions and the mandates, together, at one URL. A team that runs different products, or has decided what its agents may do, forks this folder, edits it, hosts it anywhere with CORS, and points the game at its manifest. The game's logic does not change; the world it asks about does.

What a customised pack changes: which profiles the picker offers, what each row claims, which questions are asked, and which mandate the delta is drawn against. What it cannot change: the scoring rule, the level derivation, the ceiling's share of the set — those are the engine's, and they are what make one pack's scores comparable with another's.

## For the game

Since its vault v1.0.0 (9 September 2026) the game reads this pack on every load: `pack.json` first, then the files, over CORS. Its footer names the pack version and hash it read. Its build fetches the same files, hashes them in the order `contents` lists, refuses a mismatch with `content_hash`, and inlines the verified copy as the fallback for a page that cannot reach this site — labelled as a snapshot, with the hash, so the two are never confused. `?pack=<url>` points the game at another pack; `?pack=<id>` looks the id up in [`packs.json`](../data/packs.json), the registry beside this manifest.

## Load a pack

Pick a pack from the registry, or paste the URL of a folder that holds a `pack.json`. The control reads the manifest and opens the game on it, here. The front page does not change: it plays the public pack. Whether the vault host carries the choice through to the game is the one thing this site cannot check from the outside — the game's own footer names the pack it actually read, and that is the answer.

> This game counts usage anonymously — which screens people reach, which answers are common. No cookies, no analytics script, nothing that identifies you or your machine, and a pause switch on every screen. [What is sent](../what-we-learn/index.md).

[The folder on GitHub](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/blob/dev/data/) · [how to contribute](../map/contribute/index.md)

---

*[Site index for agents](../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/data/index.html)*
