# A coding assistant on my machine

> A starting mandate for cli: I want it to read and change the project I pointed it at, run the build and the tests, commit to that repository, and fetch the packages and…

*Source: <https://what-can-it-do.games.sgit.ai/map/mandates/coding-assistant-on-my-machine/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../index.md) / [The map](../../../map/index.md) / [The mandates](../../../map/mandates/index.md) / A coding assistant on my machine

# A coding assistant on my machine

I want it to read and change the project I pointed it at, run the build and the tests, commit to that repository, and fetch the packages and docs it needs. I did not sign up for it reading the rest of my disk, my credentials or my shell history, sending anything to anyone, publishing under my name, changing its own permission settings, or leaving anything behind that runs after it stops.

Status: **starting-point** · authored 2026-09-09 · the site, as a starting point — not measured, not surveyed; the first thing to argue with · [edit this mandate](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/mandates/coding-assistant-on-my-machine.json)

## The delta

Against every profile this mandate applies to. ▲ is authority you did not ask for; ▼ is something you were counting on that is not there. The tally is at the bottom.

Legend: ▲ excess — it can, and you did not want it to · ▼ shortfall — it cannot, and you wanted it to · ✓ aligned — it can, and you wanted it to · – aligned — it cannot, and you did not want it to · ? it can, and the mandate does not say · · it cannot, and the mandate does not say

| Capability | Claude Code (local · confirm on) | Claude Code (local · confirm off) |
|---|---|---|
| **filesystem** |  |  |
| Read the project it is working on | ✓ | ✓ |
| Change the project it is working on | ✓ | ✓ |
| Read any file the account can reach | ▲ | ▲ |
| Change any file the account can reach | ▲ | ▲ |
| Delete files anywhere the account can reach | ▲ | ▲ |
| Read a retained record: shell history, past sessions | ▲ | ▲ |
| **process** |  |  |
| Run programs as the account — *‘run my tests’ is, on a machine with no sandbox, ‘run programs as me’ — the want is honest and the consequence is the whole point of the delta* | ✓ | ✓ |
| Run programs inside its own sandbox only | · | · |
| **network** |  |  |
| Reach a permitted list of hosts | ▼ | ▼ |
| Reach any host on the internet — *unstated: the want is ‘the hosts it needs’, which is the allowed-list capability; whether the whole internet is acceptable is a real decision* | ? | ? |
| **identity** |  |  |
| Read credentials stored where it runs | ▲ | ▲ |
| Act in accounts with the credentials it holds | ▲ | ▲ |
| Change its own permission settings | ▲ | ▲ |
| **communication** |  |  |
| Send a message to anyone | – | – |
| Read mail or chat it is connected to | · | · |
| **code** |  |  |
| Commit to the repository it was pointed at | ✓ | ✓ |
| Push to a code host (any branch it can reach) — *left unstated on purpose: some people want it to push, some do not, and the mandate should not pretend to know* | ? | ? |
| Sign commits with the key it holds | ▲ | ▲ |
| Publish packages, images or pages under the name it holds | ▲ | ▲ |
| **money** |  |  |
| Spend money or tokens against an account it holds | · | · |
| **schedule** |  |  |
| Create something that outlives the turn where it runs (a cron, a service) | ▲ | ▲ |
| Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) | · | · |
| **browser** |  |  |
| Read every page you visit | · | · |
| **The delta** | ▲ 10 · ▼ 1 | ▲ 10 · ▼ 1 |

## In words

- **Claude Code — local · confirm on:** excess — Read any file the account can reach; Change any file the account can reach; Delete files anywhere the account can reach; Read credentials stored where it runs; Act in accounts with the credentials it holds; Change its own permission settings; Sign commits with the key it holds; Publish packages, images or pages under the name it holds; Create something that outlives the turn where it runs (a cron, a service); Read a retained record: shell history, past sessions. Shortfall — Reach a permitted list of hosts.
- **Claude Code — local · confirm off:** excess — Read any file the account can reach; Change any file the account can reach; Delete files anywhere the account can reach; Read credentials stored where it runs; Act in accounts with the credentials it holds; Change its own permission settings; Sign commits with the key it holds; Publish packages, images or pages under the name it holds; Create something that outlives the turn where it runs (a cron, a service); Read a retained record: shell history, past sessions. Shortfall — Reach a permitted list of hosts.

## The mandate, row by row

| Capability | Position | Note |
|---|---|---|
| [Read the project it is working on](../../../map/capabilities/read.file.project/index.md) | want |  |
| [Change the project it is working on](../../../map/capabilities/write.file.project/index.md) | want |  |
| [Run programs as the account](../../../map/capabilities/execute.process.host/index.md) | want | ‘run my tests’ is, on a machine with no sandbox, ‘run programs as me’ — the want is honest and the consequence is the whole point of the delta |
| [Commit to the repository it was pointed at](../../../map/capabilities/write.repository.project/index.md) | want |  |
| [Reach a permitted list of hosts](../../../map/capabilities/send.endpoint.allowed/index.md) | want |  |
| [Read any file the account can reach](../../../map/capabilities/read.file.host/index.md) | do not want |  |
| [Change any file the account can reach](../../../map/capabilities/write.file.host/index.md) | do not want |  |
| [Delete files anywhere the account can reach](../../../map/capabilities/delete.file.host/index.md) | do not want |  |
| [Read credentials stored where it runs](../../../map/capabilities/read.credential.host/index.md) | do not want |  |
| [Act in accounts with the credentials it holds](../../../map/capabilities/authenticate-as.credential.tenant/index.md) | do not want |  |
| [Sign commits with the key it holds](../../../map/capabilities/authenticate-as.credential.signing/index.md) | do not want |  |
| [Change its own permission settings](../../../map/capabilities/grant.credential.self/index.md) | do not want |  |
| [Send a message to anyone](../../../map/capabilities/send.message.world/index.md) | do not want |  |
| [Publish packages, images or pages under the name it holds](../../../map/capabilities/create.record.world/index.md) | do not want |  |
| [Create something that outlives the turn where it runs (a cron, a service)](../../../map/capabilities/create.schedule.host/index.md) | do not want |  |
| [Read a retained record: shell history, past sessions](../../../map/capabilities/read.record.history/index.md) | do not want |  |
| [Reach any host on the internet](../../../map/capabilities/send.endpoint.world/index.md) | unstated | unstated: the want is ‘the hosts it needs’, which is the allowed-list capability; whether the whole internet is acceptable is a real decision |
| [Push to a code host (any branch it can reach)](../../../map/capabilities/write.repository.tenant/index.md) | unstated | left unstated on purpose: some people want it to push, some do not, and the mandate should not pretend to know |

> **You cannot deny the excess rows.** The agent already has the access. What is left is how long you are prepared to live with each one and who says so — [what to do next](../../../what-next/index.md).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/mandates/coding-assistant-on-my-machine/index.html)*
