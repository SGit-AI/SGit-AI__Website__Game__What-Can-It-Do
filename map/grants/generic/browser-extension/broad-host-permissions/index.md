# Browser extension — all sites

> A browser extension with broad host permissions: what it can reach, tool by tool, with the control on the path and the evidence behind each row.

*Source: <https://what-can-it-do.games.sgit.ai/map/grants/generic/browser-extension/broad-host-permissions/index.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../../../index.md) / [The map](../../../../../map/index.md) / [The products](../../../../../map/grants/index.md) / Browser extension — all sites

# A browser extension with broad host permissions

Not an agent by name, and it has a grant: an extension granted 'read and change all your data on all websites' reads every page you visit, reaches any host, and acts inside the sites you are logged into. Nobody wrote it a mandate. DERIVED from the permission model the browser documents; not measured on any instance.

**generic** · surface `extension` · variant `broad-host-permissions` · profile version `2026-09-05` · reaches **3** of 23 capabilities, **3** of which cannot be undone. [Edit this profile](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/profiles/generic/browser-extension/broad-host-permissions.json) · [the file](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/blob/dev/data/profiles/generic/browser-extension/broad-host-permissions.json).

| Capability | Undo | Browser extension (all sites) |
|---|---|---|
| **filesystem** — files and directories | |  |
| Read the project it is working on `read.file.project` | yes | · |
| Change the project it is working on `write.file.project` | with-effort | · |
| Read any file the account can reach `read.file.host` | no | · |
| Change any file the account can reach `write.file.host` | with-effort | · |
| Delete files anywhere the account can reach `delete.file.host` | no | · |
| Read a retained record: shell history, past sessions `read.record.history` | no | · |
| **process** — programs and their execution | |  |
| Run programs as the account `execute.process.host` | with-effort | · |
| Run programs inside its own sandbox only `execute.process.self` | yes | · |
| **network** — endpoints and hosts | |  |
| Reach a permitted list of hosts `send.endpoint.allowed` | no | · |
| Reach any host on the internet `send.endpoint.world` | no | ● |
| **identity** — credentials and who the agent can act as | |  |
| Read credentials stored where it runs `read.credential.host` | no | · |
| Act in accounts with the credentials it holds `authenticate-as.credential.tenant` | no | ◐ |
| Change its own permission settings `grant.credential.self` | yes | · |
| **communication** — messages to people | |  |
| Send a message to anyone `send.message.world` | no | · |
| Read mail or chat it is connected to `read.message.tenant` | no | · |
| **code** — repositories and what lands in them | |  |
| Commit to the repository it was pointed at `write.repository.project` | with-effort | · |
| Push to a code host (any branch it can reach) `write.repository.tenant` | with-effort | · |
| Sign commits with the key it holds `authenticate-as.credential.signing` | no | · |
| Publish packages, images or pages under the name it holds `create.record.world` | no | · |
| **money** — budgets and spend | |  |
| Spend money or tokens against an account it holds `write.budget.tenant` | no | · |
| **schedule** — things that outlive the turn | |  |
| Create something that outlives the turn where it runs (a cron, a service) `create.schedule.host` | yes | · |
| Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) `create.schedule.tenant` | yes | · |
| **browser** — what a browser extension or automation can see and do in your browser | |  |
| Read every page you visit `read.record.browsing` | no | ● |

## What host, tenant and world mean here

| Reach | Here, it means |
|---|---|
| host | your browser — every page, every logged-in site |
| tenant | the sites you are logged into, as you |
| world | the internet, from your browser |

## What it cannot reach, and why

| What | Why | Source |
|---|---|---|
| files on your disk | the browser sandbox; an extension reads pages, not the filesystem | the browser's extension permission model |

## The grant, tool by tool

Two tools in one session reach different things, which is why the unit of mapping is the tool and not the product. Each row carries the control on the path and the tier of evidence behind it.

### the extension

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Read every page you visit](../../../../../map/capabilities/read.record.browsing/index.md) `read.record.browsing` | ● none | documented | — · *'read and change all your data on all websites'* |
| [Reach any host on the internet](../../../../../map/capabilities/send.endpoint.world/index.md) `send.endpoint.world` | ● none | documented | — · *host permissions* |
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) `authenticate-as.credential.tenant` | ◐ setting | documented | the site's own session controls · *acts inside sites where you have a session, as you* |

## What narrows it

For each capability in the grant: the specific setting or arrangement that narrows it, what it costs, and the tier the control reaches afterwards. Guidance is free and stays free.

| Capability | The setting | What it costs | Tier after |
|---|---|---|---|
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) | scoped, short-lived tokens issued to the agent rather than your own; read-only where read is all it needs | an hour per service, and rotation | boundary |
| [Read every page you visit](../../../../../map/capabilities/read.record.browsing/index.md) | grant the extension access on click, or on a list of sites, instead of on all sites; remove the ones you do not use | a click the first time on each site | boundary |
| [Reach any host on the internet](../../../../../map/capabilities/send.endpoint.world/index.md) | route outbound traffic through an allow-list — the one control the hosted container already has, demonstrated rather than claimed | an hour, if you already have somewhere to put it | boundary |

## Against the mandates

What a reasonable person wanted from this setup, and the gap: ▲ excess is what it can do that they did not want; ▼ shortfall is what they wanted that it cannot do.

| Mandate | Excess | Shortfall |
|---|---|---|
| [A browser extension I installed](../../../../../map/mandates/browser-extension-i-installed/index.md) | ▲ 2 | ▼ 0 |

## Sources

- `the browser's documented extension permission model (brief v0.33.65: things nobody calls an agent)`

> A **derived** row is an inference from what this kind of program architecturally is. It is a claim, and the most useful pull request on this page is one that replaces a claim with a probe run — [how](../../../../../map/contribute/index.md).

---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/grants/generic/browser-extension/broad-host-permissions/index.html)*
