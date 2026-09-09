# The map — what each agent can reach

> 23 capabilities across 9 products and setups: what each one can reach, what stands in the way, and how sure anyone is. Generated from the data pack; change it with a pull request.

*Source: <https://what-can-it-do.games.sgit.ai/map/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../index.md) / The map

# What each agent can reach

Every question the game asks is a cell in this table. 23 capabilities — a verb, an object and how far it reaches — against 9 products in the setups people actually run them in. The fill says how open the door is; the glyph says the same thing without the colour.

**9** products × setups · **23** capabilities · **13** of them cannot be undone · **21/99** rows measured, not derived

Legend: ● none — nothing in the way · ◉ expectation — a rule in prose, enforced by nobody · ◐ setting — a switch the agent's own account can flip · ○ boundary — enforced above the grant, out of the agent's reach · · not in this grant

| Capability | Undo | Claude Code (web container) | Claude Code (local · confirm off) | Claude Code (local · confirm on) | Claude Desktop (local tools) | Claude.ai (connectors on) | Browser extension (all sites) | Scheduled job (service account) | GitHub Actions (hosted runner) | ChatGPT (no connectors) |
|---|---|---|---|---|---|---|---|---|---|---|
| **filesystem** — files and directories | |  |  |  |  |  |  |  |  |  |
| Read the project it is working on `read.file.project` | yes | ● | ● | ● | ● | ● | · | · | ● | ● |
| Change the project it is working on `write.file.project` | with-effort | ● | ● | ● | ● | · | · | · | ● | · |
| Read any file the account can reach `read.file.host` | no | ● | ● | ● | ◐ | ○ | · | ● | ● | · |
| Change any file the account can reach `write.file.host` | with-effort | ● | ● | ● | ◐ | · | · | ● | ● | · |
| Delete files anywhere the account can reach `delete.file.host` | no | ● | ● | ● | · | · | · | · | ● | · |
| Read a retained record: shell history, past sessions `read.record.history` | no | ● | ● | ● | ● | · | · | · | · | · |
| **process** — programs and their execution | |  |  |  |  |  |  |  |  |  |
| Run programs as the account `execute.process.host` | with-effort | ● | ● | ◐ | ◐ | · | · | ● | ● | · |
| Run programs inside its own sandbox only `execute.process.self` | yes | · | · | · | · | · | · | · | · | · |
| **network** — endpoints and hosts | |  |  |  |  |  |  |  |  |  |
| Reach a permitted list of hosts `send.endpoint.allowed` | no | ○ | · | · | · | · | · | · | · | · |
| Reach any host on the internet `send.endpoint.world` | no | · | ● | ● | ● | · | ● | ● | ● | · |
| **identity** — credentials and who the agent can act as | |  |  |  |  |  |  |  |  |  |
| Read credentials stored where it runs `read.credential.host` | no | ● | ● | ● | ● | · | · | · | · | · |
| Act in accounts with the credentials it holds `authenticate-as.credential.tenant` | no | ○ | ● | ● | ● | ○ | ◐ | ● | · | · |
| Change its own permission settings `grant.credential.self` | yes | · | ◐ | ◐ | ◐ | · | · | · | · | · |
| **communication** — messages to people | |  |  |  |  |  |  |  |  |  |
| Send a message to anyone `send.message.world` | no | · | · | · | · | · | · | · | · | · |
| Read mail or chat it is connected to `read.message.tenant` | no | · | · | · | · | ○ | · | · | · | · |
| **code** — repositories and what lands in them | |  |  |  |  |  |  |  |  |  |
| Commit to the repository it was pointed at `write.repository.project` | with-effort | ● | ● | ● | · | · | · | · | ○ | · |
| Push to a code host (any branch it can reach) `write.repository.tenant` | with-effort | ◐ | ◉ | ◉ | · | ○ | · | · | · | · |
| Sign commits with the key it holds `authenticate-as.credential.signing` | no | ● | ● | ● | · | · | · | · | · | · |
| Publish packages, images or pages under the name it holds `create.record.world` | no | · | ● | ● | · | · | · | · | · | · |
| **money** — budgets and spend | |  |  |  |  |  |  |  |  |  |
| Spend money or tokens against an account it holds `write.budget.tenant` | no | · | · | · | · | · | · | ● | · | · |
| **schedule** — things that outlive the turn | |  |  |  |  |  |  |  |  |  |
| Create something that outlives the turn where it runs (a cron, a service) `create.schedule.host` | yes | ○ | ● | ● | · | · | · | ● | · | · |
| Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) `create.schedule.tenant` | yes | ◐ | · | · | · | · | · | · | · | · |
| **browser** — what a browser extension or automation can see and do in your browser | |  |  |  |  |  |  |  |  |  |
| Read every page you visit `read.record.browsing` | no | · | · | · | · | · | ● | · | · | · |

## How to read it

- **A filled cell means the agent can.** What the fill *shade* adds is what stands between it and the capability: nothing (●), a rule somebody wrote down (◉), a setting the agent's own account could change (◐), or a boundary enforced above it that it cannot reach (○). Darker is more open.
- **Hover a cell** for the control, the evidence tier and the tool that reaches it. Click it for the row on that product's page.
- **The Undo column is the row's weight.** A capability that cannot be undone — read a credential, send a message, delete at host reach — is a different kind of thing from one that can, however many cells it fills. The game's levels are built on that.
- **Host, tenant and world mean what the profile says they mean.** For an agent in a vendor's container, *host* is the container and *tenant* is a scoped token — not your machine and not your accounts. Each product's page names its reaches.

## How sure is any of this

Not very, in most places, and every row says so. Of 99 tool-capability rows across the set, **21 were measured** — a probe run on an instance, dated — and the rest are *derived* from what a thing architecturally is, or *documented* by the vendor. A derived row is a claim until somebody runs the probes and contributes the file, and the honest reading of this table is **mostly claims, structured so that each one can be replaced by a measurement**.

That is what the pull request is for. [How to contribute](../map/contribute/index.md) — a row, a whole profile, a mandate, or a correction.

## The rest of the map

**Every product, one page each** — Tool by tool: what it reaches, the control on the path, the evidence, what the profile says is out of reach and why, and the reductions that narrow it.
[The products](../map/grants/index.md)

**The capabilities** — The 23 primitives the questions are built from — which products grant each, what narrows it, which questions ask about it, and which mandates want it.
[The capabilities](../map/capabilities/index.md)

**Mandates, and the deltas** — What a reasonable person wanted, per setup — and the gap against what was actually granted, as a matrix: excess in one colour, shortfall in the other.
[The mandates](../map/mandates/index.md) · [The deltas](../map/deltas/index.md)

**Above the ceiling** — The 17 things no agent in this set can do, each naming the control outside the agent that stops it.
[The ceiling](../map/ceiling/index.md)

**The questions** — 25 questions the games ask, with what each one is for — the seed of a question pack that could be customised.
[The questions](../map/questions/index.md)

**The data pack** — All of it as JSON, at a stable URL with CORS, which is how the game reads it. Fork it, change it, point the game at yours.
[The pack](../data/index.md) · [Contribute](../map/contribute/index.md)

---

*[Site index for agents](../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/index.html)*
