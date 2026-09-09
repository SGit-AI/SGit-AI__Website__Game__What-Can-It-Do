# ChatGPT — no connectors

> ChatGPT (in the browser, no connectors): what it can reach, tool by tool, with the control on the path and the evidence behind each row.

*Source: <https://what-can-it-do.games.sgit.ai/map/grants/openai/chatgpt-web/default/index.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../../../index.md) / [The map](../../../../../map/index.md) / [The products](../../../../../map/grants/index.md) / ChatGPT — no connectors

# ChatGPT (in the browser, no connectors)

An assistant in the vendor's environment. It reaches what you paste or upload and nothing on your machine: the vendor's environment is a boundary you did not build. DERIVED from the assess library's web tree. Browsing, if on, is the vendor's egress, not yours.

**OpenAI** · surface `web` · variant `default` · profile version `2026-09-05` · reaches **1** of 23 capabilities, **0** of which cannot be undone. [Edit this profile](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/profiles/openai/chatgpt-web/default.json) · [the file](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/blob/dev/data/profiles/openai/chatgpt-web/default.json).

| Capability | Undo | ChatGPT (no connectors) |
|---|---|---|
| **filesystem** — files and directories | |  |
| Read the project it is working on `read.file.project` | yes | ● |
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
| Reach any host on the internet `send.endpoint.world` | no | · |
| **identity** — credentials and who the agent can act as | |  |
| Read credentials stored where it runs `read.credential.host` | no | · |
| Act in accounts with the credentials it holds `authenticate-as.credential.tenant` | no | · |
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
| Read every page you visit `read.record.browsing` | no | · |

## What host, tenant and world mean here

| Reach | Here, it means |
|---|---|
| host | the vendor's environment; not your machine |
| tenant | nothing of yours |
| world | the vendor's egress, if browsing is on |

## What it cannot reach, and why

| What | Why | Source |
|---|---|---|
| your machine's files | the vendor's environment is a boundary you did not build | assess/library.json (web: home) |
| your accounts | no connectors are on | assess/library.json (web: connect) |

## The grant, tool by tool

Two tools in one session reach different things, which is why the unit of mapping is the tool and not the product. Each row carries the control on the path and the tier of evidence behind it.

### conversation and uploads

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) `read.file.project` | ● none | derived | — · *what you paste or upload — and a record once read is exposure that cannot be unread, on the vendor's side* |

## What narrows it

For each capability in the grant: the specific setting or arrangement that narrows it, what it costs, and the tier the control reaches afterwards. Guidance is free and stays free.

| Capability | The setting | What it costs | Tier after |
|---|---|---|---|
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) | none: this is what it is for | nothing | none |

## Against the mandates

What a reasonable person wanted from this setup, and the gap: ▲ excess is what it can do that they did not want; ▼ shortfall is what they wanted that it cannot do.

| Mandate | Excess | Shortfall |
|---|---|---|
| [Chat in the browser, nothing connected](../../../../../map/mandates/chat-no-connectors/index.md) | ▲ 0 | ▼ 0 |

## Sources

- `assess/library.json (surface web)`

> A **derived** row is an inference from what this kind of program architecturally is. It is a claim, and the most useful pull request on this page is one that replaces a claim with a probe run — [how](../../../../../map/contribute/index.md).

---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/grants/openai/chatgpt-web/default/index.html)*
