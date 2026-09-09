# Claude Desktop — local tools

> Claude Desktop (a desktop app with local tools): what it can reach, tool by tool, with the control on the path and the evidence behind each row.

*Source: <https://what-can-it-do.games.sgit.ai/map/grants/anthropic/claude-desktop/default/index.html> · site v0.8.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../../../index.md) / [The map](../../../../../map/index.md) / [The products](../../../../../map/grants/index.md) / Claude Desktop — local tools

# Claude Desktop (a desktop app with local tools)

A desktop application running as your user account, with connectors and local tools that can read files and run commands with a prompt. DERIVED from the assess library's desktop tree; not measured on any instance.

**Anthropic** · surface `desktop` · variant `default` · profile version `2026-09-05` · reaches **10** of 23 capabilities, **5** of which cannot be undone. [Edit this profile](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/profiles/anthropic/claude-desktop/default.json) · [the file](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/blob/dev/data/profiles/anthropic/claude-desktop/default.json).

| Capability | Undo | Claude Desktop (local tools) |
|---|---|---|
| **filesystem** — files and directories | |  |
| Read the project it is working on `read.file.project` | yes | ● |
| Change the project it is working on `write.file.project` | with-effort | ● |
| Read any file the account can reach `read.file.host` | no | ◐ |
| Change any file the account can reach `write.file.host` | with-effort | ◐ |
| Delete files anywhere the account can reach `delete.file.host` | no | · |
| Read a retained record: shell history, past sessions `read.record.history` | no | ● |
| **process** — programs and their execution | |  |
| Run programs as the account `execute.process.host` | with-effort | ◐ |
| Run programs inside its own sandbox only `execute.process.self` | yes | · |
| **network** — endpoints and hosts | |  |
| Reach a permitted list of hosts `send.endpoint.allowed` | no | · |
| Reach any host on the internet `send.endpoint.world` | no | ● |
| **identity** — credentials and who the agent can act as | |  |
| Read credentials stored where it runs `read.credential.host` | no | ● |
| Act in accounts with the credentials it holds `authenticate-as.credential.tenant` | no | ● |
| Change its own permission settings `grant.credential.self` | yes | ◐ |
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
| host | your machine, as your user account |
| tenant | your accounts |
| world | the internet |

## The grant, tool by tool

Two tools in one session reach different things, which is why the unit of mapping is the tool and not the product. Each row carries the control on the path and the tier of evidence behind it.

### conversation

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) `read.file.project` | ● none | derived | — · *what you paste or attach* |

### local files and commands (when enabled)

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) `read.file.project` | ● none | derived | — |
| [Change the project it is working on](../../../../../map/capabilities/write.file.project/index.md) `write.file.project` | ● none | derived | — |
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) `read.file.host` | ◐ setting | derived | the app's folder permission |
| [Change any file the account can reach](../../../../../map/capabilities/write.file.host/index.md) `write.file.host` | ◐ setting | derived | the app's folder permission |
| [Run programs as the account](../../../../../map/capabilities/execute.process.host/index.md) `execute.process.host` | ◐ setting | derived | a confirmation prompt · *run terminal commands as you* |
| [Read credentials stored where it runs](../../../../../map/capabilities/read.credential.host/index.md) `read.credential.host` | ● none | documented | — |
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) `authenticate-as.credential.tenant` | ● none | derived | — |
| [Read a retained record: shell history, past sessions](../../../../../map/capabilities/read.record.history/index.md) `read.record.history` | ● none | documented | — |
| [Change its own permission settings](../../../../../map/capabilities/grant.credential.self/index.md) `grant.credential.self` | ◐ setting | derived | the app's own settings file |
| [Reach any host on the internet](../../../../../map/capabilities/send.endpoint.world/index.md) `send.endpoint.world` | ● none | derived | — |

## What narrows it

For each capability in the grant: the specific setting or arrangement that narrows it, what it costs, and the tier the control reaches afterwards. Guidance is free and stays free.

| Capability | The setting | What it costs | Tier after |
|---|---|---|---|
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) | scoped, short-lived tokens issued to the agent rather than your own; read-only where read is all it needs | an hour per service, and rotation | boundary |
| [Run programs as the account](../../../../../map/capabilities/execute.process.host/index.md) | keep the confirmation prompt on for commands, and run in a container: execution survives inside it and stops being execution on your machine | a click per command · an afternoon for the container | setting (prompt) · boundary (container) |
| [Change its own permission settings](../../../../../map/capabilities/grant.credential.self/index.md) | settings owned by a different user than the one the agent runs as, or set above the session by the platform | minutes, if the platform supports it; otherwise the separate account | boundary |
| [Read credentials stored where it runs](../../../../../map/capabilities/read.credential.host/index.md) | keep credentials out of the account the agent runs as: a credential helper, a separate account, or a container without your home mounted | an afternoon, and re-authenticating where the agent needs a credential of its own | boundary |
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) | run the agent in a container with only the project mounted, or under a separate user account | an afternoon, then ongoing friction (container) · days, and it fights you (account) | boundary |
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) | none: this is what it is for | nothing | none |
| [Read a retained record: shell history, past sessions](../../../../../map/capabilities/read.record.history/index.md) | history off, or a fresh environment per task, so the grant is a tree over the present rather than a union over every prior turn | the agent forgets between tasks | boundary |
| [Reach any host on the internet](../../../../../map/capabilities/send.endpoint.world/index.md) | route outbound traffic through an allow-list — the one control the hosted container already has, demonstrated rather than claimed | an hour, if you already have somewhere to put it | boundary |
| [Change any file the account can reach](../../../../../map/capabilities/write.file.host/index.md) | the same container or account; the tool's own directory restriction is a setting anything running as you can step around | as above | boundary |
| [Change the project it is working on](../../../../../map/capabilities/write.file.project/index.md) | a review before merge | a reviewer's time | setting |

## Against the mandates

What a reasonable person wanted from this setup, and the gap: ▲ excess is what it can do that they did not want; ▼ shortfall is what they wanted that it cannot do.

| Mandate | Excess | Shortfall |
|---|---|---|
| [The desktop app, with local tools switched on](../../../../../map/mandates/desktop-app-with-local-tools/index.md) | ▲ 6 | ▼ 1 |

## Sources

- `assess/library.json (surface desktop)`

> A **derived** row is an inference from what this kind of program architecturally is. It is a claim, and the most useful pull request on this page is one that replaces a claim with a probe run — [how](../../../../../map/contribute/index.md).

---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/grants/anthropic/claude-desktop/default/index.html)*
