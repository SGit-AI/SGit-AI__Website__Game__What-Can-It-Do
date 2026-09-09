# A coding assistant in a container on the web

> A starting mandate for agentbox: I attached a repository and I want it worked on: read it, change it, run things, commit, and push to that repository — that is why I attache…

*Source: <https://what-can-it-do.games.sgit.ai/map/mandates/coding-assistant-in-a-container/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../index.md) / [The map](../../../map/index.md) / [The mandates](../../../map/mandates/index.md) / A coding assistant in a container on the web

# A coding assistant in a container on the web

I attached a repository and I want it worked on: read it, change it, run things, commit, and push to that repository — that is why I attached it. The container is disposable, so what it does to the container's own files is its business. I do not want it signing as me, and I do not want it creating sessions or routines that keep going after this one ends.

Status: **starting-point** · authored 2026-09-09 · the site, as a starting point — not measured, not surveyed; the first thing to argue with · [edit this mandate](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/mandates/coding-assistant-in-a-container.json)

## The delta

Against every profile this mandate applies to. ▲ is authority you did not ask for; ▼ is something you were counting on that is not there. The tally is at the bottom.

Legend: ▲ excess — it can, and you did not want it to · ▼ shortfall — it cannot, and you wanted it to · ✓ aligned — it can, and you wanted it to · – aligned — it cannot, and you did not want it to · ? it can, and the mandate does not say · · it cannot, and the mandate does not say

| Capability | Claude Code (web container) |
|---|---|
| **filesystem** |  |
| Read the project it is working on | ✓ |
| Change the project it is working on | ✓ |
| Read any file the account can reach — *unstated: host is the container, and the container is thrown away* | ? |
| Change any file the account can reach | ? |
| Delete files anywhere the account can reach | ? |
| Read a retained record: shell history, past sessions | ▲ |
| **process** |  |
| Run programs as the account | ✓ |
| Run programs inside its own sandbox only | · |
| **network** |  |
| Reach a permitted list of hosts | ✓ |
| Reach any host on the internet | · |
| **identity** |  |
| Read credentials stored where it runs — *unstated: the only keys in the image are the session's own* | ? |
| Act in accounts with the credentials it holds — *unstated: the scoped platform token is how it pushes at all — not a want, not a refusal, a mechanism* | ? |
| Change its own permission settings | · |
| **communication** |  |
| Send a message to anyone | · |
| Read mail or chat it is connected to | · |
| **code** |  |
| Commit to the repository it was pointed at | ✓ |
| Push to a code host (any branch it can reach) | ✓ |
| Sign commits with the key it holds | ▲ |
| Publish packages, images or pages under the name it holds | · |
| **money** |  |
| Spend money or tokens against an account it holds | · |
| **schedule** |  |
| Create something that outlives the turn where it runs (a cron, a service) | ? |
| Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) | ▲ |
| **browser** |  |
| Read every page you visit | · |
| **The delta** | ▲ 3 · ▼ 0 |

## In words

- **Claude Code — web container:** excess — Sign commits with the key it holds; Read a retained record: shell history, past sessions; Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session). No shortfall.

## The mandate, row by row

| Capability | Position | Note |
|---|---|---|
| [Read the project it is working on](../../../map/capabilities/read.file.project/index.md) | want |  |
| [Change the project it is working on](../../../map/capabilities/write.file.project/index.md) | want |  |
| [Run programs as the account](../../../map/capabilities/execute.process.host/index.md) | want |  |
| [Commit to the repository it was pointed at](../../../map/capabilities/write.repository.project/index.md) | want |  |
| [Push to a code host (any branch it can reach)](../../../map/capabilities/write.repository.tenant/index.md) | want |  |
| [Reach a permitted list of hosts](../../../map/capabilities/send.endpoint.allowed/index.md) | want |  |
| [Sign commits with the key it holds](../../../map/capabilities/authenticate-as.credential.signing/index.md) | do not want |  |
| [Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session)](../../../map/capabilities/create.schedule.tenant/index.md) | do not want |  |
| [Read a retained record: shell history, past sessions](../../../map/capabilities/read.record.history/index.md) | do not want |  |
| [Read any file the account can reach](../../../map/capabilities/read.file.host/index.md) | unstated | unstated: host is the container, and the container is thrown away |
| [Read credentials stored where it runs](../../../map/capabilities/read.credential.host/index.md) | unstated | unstated: the only keys in the image are the session's own |
| [Act in accounts with the credentials it holds](../../../map/capabilities/authenticate-as.credential.tenant/index.md) | unstated | unstated: the scoped platform token is how it pushes at all — not a want, not a refusal, a mechanism |

> **You cannot deny the excess rows.** The agent already has the access. What is left is how long you are prepared to live with each one and who says so — [what to do next](../../../what-next/index.md).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/mandates/coding-assistant-in-a-container/index.html)*
