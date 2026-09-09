# Claude.ai — connectors on

> Claude (in the browser, with connectors switched on): what it can reach, tool by tool, with the control on the path and the evidence behind each row.

*Source: <https://what-can-it-do.games.sgit.ai/map/grants/anthropic/claude-web/connectors-on/index.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../../../index.md) / [The map](../../../../../map/index.md) / [The products](../../../../../map/grants/index.md) / Claude.ai — connectors on

# Claude (in the browser, with connectors switched on)

The same web assistant with connectors you switched on — a drive, a code host, a cloud account. Each connector is a boundary (the vendor holds the token, scoped as you scoped it) and each one is a row you granted by clicking. DERIVED from the assess library's web tree; which connectors is yours to name.

**Anthropic** · surface `web` · variant `connectors-on` · profile version `2026-09-05` · reaches **5** of 23 capabilities, **3** of which cannot be undone. [Edit this profile](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/profiles/anthropic/claude-web/connectors-on.json) · [the file](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/blob/dev/data/profiles/anthropic/claude-web/connectors-on.json).

| Capability | Undo | Claude.ai (connectors on) |
|---|---|---|
| **filesystem** — files and directories | |  |
| Read the project it is working on `read.file.project` | yes | ● |
| Change the project it is working on `write.file.project` | with-effort | · |
| Read any file the account can reach `read.file.host` | no | ○ |
| Change any file the account can reach `write.file.host` | with-effort | · |
| Delete files anywhere the account can reach `delete.file.host` | no | · |
| Read a retained record: shell history, past sessions `read.record.history` | no | · |
| **process** — programs and their execution | |  |
| Run programs as the account `execute.process.host` | with-effort | · |
| Run programs inside its own sandbox only `execute.process.self` | yes | · |
| **network** — endpoints and hosts | |  |
| Reach a permitted list of hosts `send.endpoint.allowed` | no | · |
| Reach any host on the internet `send.endpoint.world` | no | · |
| **identity** — credentials and who the agent can act as | |  |
| Read credentials stored where it runs `read.credential.host` | no | · |
| Act in accounts with the credentials it holds `authenticate-as.credential.tenant` | no | ○ |
| Change its own permission settings `grant.credential.self` | yes | · |
| **communication** — messages to people | |  |
| Send a message to anyone `send.message.world` | no | · |
| Read mail or chat it is connected to `read.message.tenant` | no | ○ |
| **code** — repositories and what lands in them | |  |
| Commit to the repository it was pointed at `write.repository.project` | with-effort | · |
| Push to a code host (any branch it can reach) `write.repository.tenant` | with-effort | ○ |
| Sign commits with the key it holds `authenticate-as.credential.signing` | no | · |
| Publish packages, images or pages under the name it holds `create.record.world` | no | · |
| **money** — budgets and spend | |  |
| Spend money or tokens against an account it holds `write.budget.tenant` | no | · |
| **schedule** — things that outlive the turn | |  |
| Create something that outlives the turn where it runs (a cron, a service) `create.schedule.host` | yes | · |
| Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) `create.schedule.tenant` | yes | · |
| **browser** — what a browser extension or automation can see and do in your browser | |  |
| Read every page you visit `read.record.browsing` | no | · |

## What host, tenant and world mean here

| Reach | Here, it means |
|---|---|
| host | what the drive connector is scoped to; not your machine |
| tenant | the accounts you connected, as you scoped them |
| world | the vendor's egress |

## What it cannot reach, and why

| What | Why | Source |
|---|---|---|
| your machine's files | a browser tab; the connector reaches a drive, not a disk | assess/library.json (web: home) |

## The grant, tool by tool

Two tools in one session reach different things, which is why the unit of mapping is the tool and not the product. Each row carries the control on the path and the tier of evidence behind it.

### conversation and uploads

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) `read.file.project` | ● none | derived | — |

### connectors

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) `read.file.host` | ○ boundary | derived | the connector's scope, held by the vendor · *a drive connector: your other files, as scoped* |
| [Push to a code host (any branch it can reach)](../../../../../map/capabilities/write.repository.tenant/index.md) `write.repository.tenant` | ○ boundary | derived | the connector's scope · *a code-host connector* |
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) `authenticate-as.credential.tenant` | ○ boundary | derived | the connector's scope · *a cloud connector acts as you* |
| [Read mail or chat it is connected to](../../../../../map/capabilities/read.message.tenant/index.md) `read.message.tenant` | ○ boundary | derived | the connector's scope · *a mail or chat connector reads your mail* |

## What narrows it

For each capability in the grant: the specific setting or arrangement that narrows it, what it costs, and the tier the control reaches afterwards. Guidance is free and stays free.

| Capability | The setting | What it costs | Tier after |
|---|---|---|---|
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) | scoped, short-lived tokens issued to the agent rather than your own; read-only where read is all it needs | an hour per service, and rotation | boundary |
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) | run the agent in a container with only the project mounted, or under a separate user account | an afternoon, then ongoing friction (container) · days, and it fights you (account) | boundary |
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) | none: this is what it is for | nothing | none |
| [Read mail or chat it is connected to](../../../../../map/capabilities/read.message.tenant/index.md) | a connector scoped to one folder or label, or none | the agent answers about less | boundary |
| [Push to a code host (any branch it can reach)](../../../../../map/capabilities/write.repository.tenant/index.md) | a branch protection rule at the host — the agent cannot edit it — and a pre-push hook in the clone for the earlier, cheaper refusal | minutes; and a review step before anything deploys | boundary (host rule) · setting (hook) |

## Against the mandates

What a reasonable person wanted from this setup, and the gap: ▲ excess is what it can do that they did not want; ▼ shortfall is what they wanted that it cannot do.

| Mandate | Excess | Shortfall |
|---|---|---|
| [Chat, with connectors switched on](../../../../../map/mandates/chat-with-connectors/index.md) | ▲ 1 | ▼ 0 |

## Sources

- `assess/library.json (surface web)`

> A **derived** row is an inference from what this kind of program architecturally is. It is a claim, and the most useful pull request on this page is one that replaces a claim with a probe run — [how](../../../../../map/contribute/index.md).

---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/grants/anthropic/claude-web/connectors-on/index.html)*
