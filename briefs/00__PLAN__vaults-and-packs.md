# Plan — the vault split, question packs, and the Mavs PoC

**Status:** draft for review. Nothing below has been done.
**Written:** 9 September 2026, against vault `4evnlwrj` at **v0.23.2** (commit `353446b8d630`),
pulled this morning with the key you gave me — 39 releases, 11 past what the sites were built
from. The other agent is still landing fixes; §1 says how the plan absorbs that.
**Decisions this needs:** D1–D5, marked inline and collected at the end.

---

## 0. What I found in v0.23.2 that changes the plan

Three things, one of them urgent.

1. **The game now sends browser fingerprints.** v0.21.0: *"THREE FINGERPRINTS, not one"* —
   stable (GPU, canvas, audio, fonts, cores, memory, platform, screen), semi (time zone,
   languages, browser major), volatile (window) — plus **country, region and connection type**
   from an IP lookup the browser makes against a third party, on load. The author is honest
   about it (*"a speed bump and not a wall"*, since the salt ships in a vault with a public read
   key) and it sits behind a `signals` switch in `telemetry.config.json`, currently **`true`**.
   **`what-can-it-do.games.sgit.ai/what-we-learn/` says "No fingerprint. No browser
   fingerprinting of any kind."** That is false as of v0.21.0 and it is live. Whatever else
   happens, that page and the game have to agree by the end of this plan — see D2.
2. **A fourth app, `what-we-know/`** (v0.18.0) — the page that shows a visitor every signal a
   site can read before they type anything. It is the disclosure surface for §1 and it belongs
   wherever the telemetry goes.
3. **The loader is already one line from the pack.** `what-can-it-do/source/app.js:23`
   fetches from `https://pki.sgit.ai/` when `?live=1`, else from the vendored `./data/`.
   `engine.mjs` reads exactly `tree.json`, `profiles/index.json`, `primitives.json`,
   `reductions.json`, `mesh/graph.json`, `ceiling.json`, `picker.json` and `profiles/<id>.json`
   on demand — and with `live=false` it prefixes nothing, which is exactly the pack's layout at
   `https://what-can-it-do.games.sgit.ai/data/`. **No shim.** The pack is served with
   `access-control-allow-origin: *` (checked with a vault-host `Origin`), and the manifests
   already declare `permissions.network`, which is what lifts the frame's CSP for the fetch.

---

## 1. The lock, and what "the wider vault" means afterwards

The two asks — *lock the 9 Sep version* and *remove the tracking from the current vault* — cannot
both be true of one branch. They are true of one **vault** with two branches:

| | What it is | Moves? |
|---|---|---|
| **`release-2026-09-09`** | a named branch at the cut commit — the frozen 9 Sep version, every app, tracking and all, exactly as shipped | never |
| **`main`** | the wider games vault, going forward: home, *Which Agent Is It?*, the release history, and a **pointer** to the new game vault where *What Can It Do?* used to be | yes |

**The cut.** The other agent is still fixing bugs, so the lock is a *cut*, not a freeze:
agree a commit (their last fix, or v0.23.2 if that is it), and the branch is created there.
Everything they land after the cut goes to the **new** game vault (§2), not here.

```
sgit branch new release-2026-09-09          # at the agreed commit
sgit push --branch-only
```

**D1 — rotate the wider vault's key at the lock.** The vault key of `4evnlwrj` has been in this
chat, in one link, and briefly in a public git branch. A "locked" vault whose write key is
exposed is not locked. `sgit vault move` rotates the key with a sentinel commit; the cost is a
new vault id, which means updating the read key in **three constants** (`build_pages.py` in both
site repos, `PUBLISHED` in both `validate.js`) and the sgit.ai catalogue page. The lock is the
natural moment, the archive is the thing most worth protecting, and the constants are the whole
cost. Recommendation: rotate. Every vault created below gets a key that is never pasted
anywhere — see §7.

---

## 2. New vault: *What Can It Do?* alone, reading the pack

One game, its reply channel, its disclosure surface, and its telemetry — nothing else.

```
what-can-it-do/          the game (source + built page), as today
ideas/                   the reply channel — it is this game's, and answers.json is inlined into it
what-we-know/            the signals disclosure page — the telemetry's, so it goes with it
telemetry.js/.html/.config.json, telemetry-source/
app.json                 entry: what-can-it-do/index.html · permissions: network, append.write, llm.chat
version.json/.html       restarts at 1.0.0 — "reads the public pack" is the release
```

**Data: the pack, not a copy.**

- `app.js:23` → default source becomes `fetchSource(PACK_BASE, false)` with
  `PACK_BASE = 'https://what-can-it-do.games.sgit.ai/data/'`; `?live=1` goes away (there is
  no second live source now); `?pack=<url>` overrides the base (§5).
- `build.mjs` keeps inlining a snapshot **as the fallback only**, stamped with the pack's
  `content_hash`. On boot the game fetches `pack.json` first: if the fetch works, it uses the
  pack and shows *"pack v0.4.0 · d6d4ba40 · live"* in the footer; if the fetch fails (no
  network, a preview), it uses the snapshot and says so, and if the snapshot's hash differs
  from the last pack it saw, it says *"snapshot behind the pack"*. That is the `?live=1`
  idea done properly: the live copy is the default and the vendored one is the honesty
  fallback, rather than the reverse.
- The vault carries **no `data/` directory of its own**, so it cannot drift from the map.

**Telemetry lives here and only here.** Same lanes, same `kqngdecz` vault, same tokens.

**D2 — the signals switch on the new vault.** The site promises no fingerprinting; v0.21.0
sends three. Two honest options: (a) ship the new vault with `signals: false` and keep the
fingerprints as an opt-in experiment behind the existing switch, so the site's statement stays
true; (b) keep `signals: true` and rewrite `/what-we-learn/` to say exactly what v0.21.0 sends,
in its own uncomfortable words. Recommendation: **(a)** — this is a game about informed consent
on a public domain, the salt is public so the fingerprint is admitted to be a speed bump, and
the country lookup reaches a third party on load. The signals stay in the code and in the
disclosure page for the day there is a reason to turn them on. Either way the site and the
game must agree, and the release gate should check it (§5).

**What the other agent changes:** the one loader line, the build's fallback stamping, the
footer label, `?pack=`. Everything else in their tree is untouched, which is why their
in-flight fixes are not a conflict — they land in this vault after the cut.

---

## 3. The wider vault's `main`, with the tracking removed

After the cut, on `main` of `4evnlwrj` (or its rotated successor):

- **Remove:** `telemetry.js`, `telemetry.html`, `telemetry.config.json`, `telemetry-source/`,
  `what-we-know/`, the `SG_TELEMETRY` inlining in *Which Agent Is It?*'s `build.mjs`, and the
  telemetry notice from every page that remains.
- **Replace** `what-can-it-do/` with one page: the name, one paragraph, and the link to the
  new vault (read key) and to the player site. The floor plan's reveal, which hands the matched
  profile to the scoreboard, now hands it across vaults by URL — `?profile=<id>` on the new
  vault's entry, which the new game already accepts.
- **Manifests:** root and `which-agent-is-it/app.json` drop `append.write` and `network`. The
  floor plan reads its vendored data over the bridge and calls nothing, so its manifest becomes
  `"permissions": {}` — the line sgit.ai keeps pointing at, now true of this vault again.
- **`ideas/` leaves** with the game (§2). *Which Agent Is It?* has no reply channel of its own
  yet; when it does, it gets one the same way.
- **A gate.** `build.mjs` for the remaining apps refuses to build if `telemetry`, `append` or
  `fetch(` to a non-vault URL appears in the output — so the wider vault cannot quietly grow
  a lane back.

The sgit.ai vault page (`/demos/vaults/agent-permission-games/`) describes v0.8.1 and says
*"the first vault here that phones home"*. After this it does not, and that page needs a
paragraph: *phoned home from v0.7 to the 9 Sep cut; the game that does now lives at …*.

---

## 4. New vault: view, browse, and propose changes to the map

A vault app, not a copy of the site. It fetches the pack (same loader as the game), renders
the map, and lets a reader **propose** a change to any row without a GitHub account.

**View and browse.** The two matrices ported to JS (~150 lines: the renderers in
`map_pages.py` are already pure functions of the pack; the port is mechanical), plus a
profile page, a capability page and a mandate page. Same glyphs, same colours, same legend.

**Propose.** On any cell, row, reduction, ceiling entry or mandate line: *propose a change*.
The form knows the shape of the thing it is on, so it asks the right questions —

| On | The form asks |
|---|---|
| a profile row | new `control_tier` / `tier` / `control` / `note`, and *what is your evidence* (a probe run, a doc, a screenshot) |
| an absent cell | *does this product reach this? how do you know?* |
| a mandate line | want / do not want / unstated, and *why* |
| a reduction | a better setting, what it costs |
| a ceiling entry | a counter-example, which is *"a correction, not a quibble"* |

— and writes a **proposal record**: `{ target: "profiles/anthropic/claude-desktop/default.json",
path: "tools[1].grant[3].control_tier", from: "none", to: "setting", rationale, evidence,
pack_hash }`. It goes over `sg.append.write` to a **proposals lane** on a private vault — the
feedback-lane pattern, exactly, with the record anchored to a file and a JSON path instead of
to a question. Nothing is written to the pack from the app; the app holds a write-only token
and no `fs.write`.

**The loop closes on the site.** A drain script (the `drain.py` shape the feedback lane
already has) turns each proposal into a **pull request** against `data/` in the site repo —
the patch applied, the rationale as the PR body, the evidence attached, no author named — so
proposals arrive where the gate already checks them and a maintainer merges or argues. Merged
→ pack rebuilds → new `content_hash` → the map vault sees it on next open. The vault app also
shows *proposals on this row: 2 open, 1 merged* by reading the drain's public summary, so a
reader can see an argument is already happening.

**Manifest:** `network` (fetch the pack), `append.write` (proposals). No `fs.write`, no
`vault.*`, no `llm`. **Lane:** one new append token on `kqngdecz` (or a proposals vault of
its own), provisioned with `sgit` and published in the app's config — the third write-only
credential shape that survives a public read key.

---

## 5. The site: packs, and nothing else

No UX change except the one asked for. Three pieces, one of them a test that gates the other
two.

**5.1 — Test first: does the embed carry a query string?** The embed protocol's `deepLink` is
"a file path". `what-can-it-do/index.html?pack=https://…` may or may not survive the host. One
afternoon, one result, and it decides which of two mechanisms the site uses:

- *If it does:* the site sets `data-entry` with `?pack=<url>` and the game reads `pack` from
  its own URL. Clean.
- *If it does not:* the game reads the pack URL from a **registry inside the public pack**
  (`data/packs.json`), keyed by a short id, and the site passes `?pack=mavs` the same way —
  or, if even that fails, the game reads `document.referrer` for the id. The registry is worth
  having regardless (5.3).

**5.2 — `pack.json` grows a `registry`**, and `data/packs.json` lists known packs: id, name,
base URL, content hash, who maintains it, licence. The public pack lists itself first.

**5.3 — One control, in the place packs already live.** `/data/` gets *"Load a pack"*: the
registry as a list, or paste a manifest URL; it validates the manifest (fetches `pack.json`,
checks `type`, counts files) and reloads the game frame with that pack. The front page does
not change: it plays the public pack. **No new nav item** — the map menu already ends in
*The data pack*, and that is the page.

**5.4 — The gate keeps the site and the game honest.** Two new checks: `/what-we-learn/` must
state the same `signals` value the game's published config carries (fetched at build, cached
in the repo with its hash), and every registry entry's manifest must resolve. So the
fingerprint sentence can never silently go false again.

---

## 6. New vault: the Mavs PoC — the same game, a different pack

**What Mavs is, in this map's terms.** Mavs sits between a person, an app or an agent and any
model; sensitive values in a prompt are replaced with *"granularly similar synthetic
stand-ins"* before the model sees them, so the model keeps context and the real data never
leaves; injection and jailbreaks are detected at runtime; every interaction is logged. Four
surfaces: **Secure Chat**, a **Claude Desktop gateway**, a **browser extension**, and an
**API for apps and agents**. Its decisive category is *business-sensitive* data — codenames,
unannounced pricing, M&A terms — which PII tools do not see.

**The pitch is one matrix pair.** In the map's encoding, Mavs is a change of **control tier**
on the rows where data leaves toward a model: without Mavs a cell is ● *open*; with Mavs it is
○ *boundary — enforced above the grant, out of the agent's reach*. Show the same four surfaces
twice, side by side, and the argument makes itself. That is the whole MVP.

**The pack** (`packs/mavs/`, in the site repo or in Mavs' own — D4):

- **Profiles, ×2 per surface:** `mavs/secure-chat/with`, `…/without`; `mavs/claude-desktop-gateway/…`;
  `mavs/browser-extension/…`; `mavs/agent-api/…`. Eight profiles, all `derived` until Mavs
  says otherwise, and labelled so.
- **New primitives — the honest part.** The 23 primitives describe what an agent can *reach*;
  Mavs governs what *leaves in a prompt*. That is a new object class, and the rules say a new
  object class needs a probe. Proposed, in a new `data` family, for Mavs to confirm or
  correct: `disclose.pii.model`, `disclose.phi.model`, `disclose.business-sensitive.model`
  (each *reversible: no*), and `inject.instruction.model` (an injection reaching the model).
  Mavs' `send.endpoint.world` row stays as it is — a gateway does not stop the prompt leaving,
  it changes what is in it, and the game should say that plainly rather than overclaim.
- **Questions:** ~12, two per surface plus four cross-cutting — *"With Mavs in the path, does
  the model see the real deal codename?"*, *"Can a pasted document carry an instruction the
  model will follow?"*. Two-fifths above the ceiling, as the engine requires, chosen with Mavs
  so that the impossible ones are things Mavs would never claim.
- **Two mandates:** *an employee in Secure Chat* (I want help with this deal; I do not want the
  codename or the price to leave), and *an agent on the API* (read the record, draft the
  reply, never send the customer's data).
- **Scenarios:** a `scenarios.json` — one per surface — which is the only pack file the
  engine does not read; the wrapper page (below) does.

**The vault.** The game build pointed at the Mavs pack, plus one wrapper page: four
scenarios as four cards, each opening the game on that surface's profile, and a closing page
that renders the with/without matrix pair from the pack. No telemetry, unless Mavs wants it —
it is their prospects who will play. **Time to an exec-ready MVP: the pack is a day once Mavs
has answered the primitive question; the vault is a day; a week with their review.**

**D3 — the Mavs input session.** Before the pack is authored, one call with their engineer:
which of the four surfaces actually exists today, what each one does to a prompt (substitute /
block / log), and whether the four proposed primitives are the right cut. Everything after
that is mechanical.

**D4 — where the Mavs pack lives.** In the site repo under `packs/mavs/` (one gate, one
registry, one PR flow) or in a repo Mavs owns (they hold the claims about their product).
Recommendation: start in ours to get to the MVP, hand it over when they want it.

---

## 7. Credentials, so this does not happen again

- Every new vault: `sgit init` in this session, vault key **never printed to chat**. The key
  goes into a one-line file shared with `sgit share` — a Simple Token, one-shot, decrypted in
  your browser — and you put it in a password manager. Only the derived read key is ever
  published.
- Every published read key goes into `PUBLISHED` in both `validate.js` allow-lists as an exact
  string, which is how the tripwire already works.
- Write-only append tokens are the only credential any app holds, as today.

---

## 8. Sequence and dependencies

| # | Step | Depends on | Who |
|---|---|---|---|
| 1 | Agree the cut commit with the other agent | their last fix | you |
| 2 | Branch `release-2026-09-09`; rotate key (D1); update three constants + sgit.ai page | 1 | me |
| 3 | 5.1 — test whether `deepLink` carries a query | — | me, one afternoon |
| 4 | New game vault (§2): loader line, fallback stamping, `?pack=`, `signals` per D2 | 1, 3 | the other agent (their tree) + me |
| 5 | Wider vault `main` (§3): strip tracking, pointer page, `{}` manifests, the build gate | 2 | me |
| 6 | Site (§5): registry, *Load a pack*, the two gate checks; fix `/what-we-learn/` per D2 | 3, 4 | me |
| 7 | Map/propose vault (§4): port renderers, proposal form, lane, drain → PR | pack (live) | me |
| 8 | Mavs input session (D3) | — | you + Mavs |
| 9 | Mavs pack + vault (§6) | 6, 8 | me, with Mavs' review |

3, 7 and 8 start now. 4 and 5 start the moment the cut is agreed. **The Mavs MVP is gated by
one conversation, not by any engineering** — everything it needs from us (packs, the loader,
the site control) is on the path already.

---

## 9. The decisions

- **D1** — rotate `4evnlwrj`'s key at the lock. *Recommend yes.*
- **D2** — new vault ships `signals: false`; fingerprints stay as an opt-in behind the switch.
  *Recommend yes; the site's promise is the constraint.*
- **D3** — the Mavs input session, before their pack is authored.
- **D4** — the Mavs pack starts in our repo. *Recommend yes.*
- **D5** — the proposals lane: a new token on `kqngdecz`, or a proposals vault of its own?
  *Recommend its own: proposals are durable and reviewed, telemetry is purged; different
  retention is the reason the feedback lane was already split.*

---

*This plan is CC BY 4.0. Every claim about the vault names the file or the release note it
came from; every claim about Mavs comes from mavsai.ai's own `llms.txt` and should be checked
with them before it is built on.*

---

## Status — 9 September 2026, end of day

What was executed, against the sections above. Where the plan and what happened differ, what happened is stated.

| Section | Done | Where |
|---|---|---|
| §1 the lock | **Done.** Branch `release-2026-09-09` on `4evnlwrj` at v0.25.0 (commit `9fab669bf4cf`), pushed and verified from a fresh clone. | `sgit branch switch release-2026-09-09` |
| §1 D1 rotate | **Not done, by decision.** `4evnlwrj` keeps its key and id: it is the vault for the next games experiments. | — |
| §2 new vault | **Done.** `pg87npy3`, now v1.2.0: *What Can It Do?* alone, reading `data/` from this site on every load; verified snapshot as the fallback; `?pack=<url>`, `?pack=<id>` (through the registry) and `?pack=snapshot`; `ideas/` and `telemetry/` with it. Since v1.2.0 the top bar no longer links to the other game, and *what-we-know* is a screen of the game (`wwk.mjs`) rather than a page — nothing is looked up on load. Read key `cf04d8a9…7b505f`. | `admin/build/build_pages.py` (`VAULT`, `READKEY`) |
| §2 D2 signals | **(a) taken.** `signals: false` in the game's vault; `/what-we-learn/` states it and gate check 10 holds the two together. | `admin/build/vault-facts.json` |
| §3 wider vault `main` | **Done** as `current` v0.26.2: lane, events, notice, `ideas/`, `what-we-know/` removed; `what-can-it-do/` is a pointer; every manifest `permissions: {}`; root `build.mjs` with tripwires. Cost stated on games.sgit.ai: the floor plan's profile handover does not cross a vault boundary. | vault `4evnlwrj` |
| §4 propose/browse vault | **Done.** `mxhepww5` v1.0.0: the two matrices in JavaScript, held cell for cell to this site's Python by a gate that reads the markdown twins; browse profiles, capabilities, mandates, the ceiling; a proposal form on every row that writes one sealed record over a write-only lane, proved on both transports. **D5 deferred:** the lane is the games' feedback lane on `kqngdecz` with schema `map-proposal/v1`, because `sgit` v0.16.0 has no command that provisions a lane; `lane.config.json` says so and is the only thing that changes when one exists. The drain (`admin/proposals/drain.py`) opens records, patches `data/`, runs the gate, branches, opens the pull request, and publishes `data/proposals.json`; tested end to end on a copy of this checkout. Read key `3e1009cc…128816`. Embedded on [the contribute page](../map/contribute/index.html). | `admin/proposals/` |
| §5 packs on the site | **Done**, except 5.1. `data/packs.json` is the registry, resolved at build from each pack's manifest; `pack.json` names it. `/data/` has *Load a pack*. Gate checks 9 (registry resolves) and 10 (the site says what the vault does). **5.1 could not be run** from the build environment (no browser reaches the vault host from there): the control sets `data-entry` with `?pack=`, the game's footer names the pack it read, and whether the host carries the query through is answered by opening `/data/` and pressing *Load* — the plan's fallback (the registry, `?pack=<id>`) is built either way. | `admin/build/map_pages.py`, `assets/load-pack.js`, `admin/build/validate.js` |
| §6 Mavs PoC | **In progress.** D3 (the Mavs input session) has not happened; a draft pack is being authored from mavsai.ai's own `llms.txt` with every claim labelled *derived* and a list of questions for Mavs, under `packs/mavs/` (D4: our repo). | `packs/mavs/` |
| §7 credentials | Every vault created in-session had its key generated there and handed to the owner directly (the first, `k4nw8toe`, was abandoned after `sgit vault info` printed its passphrase; it holds an identical tree, nothing points at it, `sgit vault delete-on-remote` removes it). Every published read key is in `PUBLISHED` in both sites' `validate.js`. | — |

**New since the plan (9 Sep, from Dinis):** region and city are to be sent to the analytics log as well as the country. Recorded as **D6**, not yet done. What it implies: the geo lookup runs for the game again (the `signals` switch, or a narrower geo-only one), `EVENTS.md` and the vault's telemetry page change, `/what-we-learn/` must state it (gate 10 refuses a build where the page and the vault's config disagree, which is the point of that gate), and the *what this page knows* screen's *never sent* pills on region and city flip to *sent*.

Not yet updated: the catalogue page at `sgit.ai/demos/vaults/agent-permission-games/`, which describes the two-game vault at v0.16.1 and should name all three vaults.
