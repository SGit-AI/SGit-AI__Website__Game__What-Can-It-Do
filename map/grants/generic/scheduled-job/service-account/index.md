# Scheduled job — service account

> A scheduled job running as a service account: what it can reach, tool by tool, with the control on the path and the evidence behind each row.

*Source: <https://what-can-it-do.games.sgit.ai/map/grants/generic/scheduled-job/service-account/index.html> · site v0.4.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../../../index.md) / [The map](../../../../../map/index.md) / [The products](../../../../../map/grants/index.md) / Scheduled job — service account

# A scheduled job running as a service account

A cron job or scheduled task on a server, under an account that is not a person's, with a credential nobody rotates. It runs when nobody is watching and no person's judgement stands in front of it. DERIVED; not measured on any instance.

**generic** · surface `service` · variant `service-account` · profile version `2026-09-05` · reaches **7** of 23 capabilities, **4** of which cannot be undone. [Edit this profile](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/profiles/generic/scheduled-job/service-account.json) · [the file](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/blob/dev/data/profiles/generic/scheduled-job/service-account.json).

| Capability | Undo | Scheduled job (service account) |
|---|---|---|
| **filesystem** — files and directories | |  |
| Read the project it is working on `read.file.project` | yes | · |
| Change the project it is working on `write.file.project` | with-effort | · |
| Read any file the account can reach `read.file.host` | no | ● |
| Change any file the account can reach `write.file.host` | with-effort | ● |
| Delete files anywhere the account can reach `delete.file.host` | no | · |
| Read a retained record: shell history, past sessions `read.record.history` | no | · |
| **process** — programs and their execution | |  |
| Run programs as the account `execute.process.host` | with-effort | ● |
| Run programs inside its own sandbox only `execute.process.self` | yes | · |
| **network** — endpoints and hosts | |  |
| Reach a permitted list of hosts `send.endpoint.allowed` | no | · |
| Reach any host on the internet `send.endpoint.world` | no | ● |
| **identity** — credentials and who the agent can act as | |  |
| Read credentials stored where it runs `read.credential.host` | no | · |
| Act in accounts with the credentials it holds `authenticate-as.credential.tenant` | no | ● |
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
| Spend money or tokens against an account it holds `write.budget.tenant` | no | ● |
| **schedule** — things that outlive the turn | |  |
| Create something that outlives the turn where it runs (a cron, a service) `create.schedule.host` | yes | ● |
| Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) `create.schedule.tenant` | yes | · |
| **browser** — what a browser extension or automation can see and do in your browser | |  |
| Read every page you visit `read.record.browsing` | no | · |

## What host, tenant and world mean here

| Reach | Here, it means |
|---|---|
| host | the server it runs on, as the service account |
| tenant | whatever the service account's credential opens |
| world | the internet, from the server |

## What it cannot reach, and why

| What | Why | Source |
|---|---|---|
| your machine | it runs on a server | by construction |

## The grant, tool by tool

Two tools in one session reach different things, which is why the unit of mapping is the tool and not the product. Each row carries the control on the path and the tier of evidence behind it.

### the job

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Run programs as the account](../../../../../map/capabilities/execute.process.host/index.md) `execute.process.host` | ● none | derived | — · *as the service account, on a schedule* |
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) `read.file.host` | ● none | derived | — |
| [Change any file the account can reach](../../../../../map/capabilities/write.file.host/index.md) `write.file.host` | ● none | derived | — |
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) `authenticate-as.credential.tenant` | ● none | derived | — · *a service-account credential, rarely rotated* |
| [Reach any host on the internet](../../../../../map/capabilities/send.endpoint.world/index.md) `send.endpoint.world` | ● none | derived | — |
| [Create something that outlives the turn where it runs (a cron, a service)](../../../../../map/capabilities/create.schedule.host/index.md) `create.schedule.host` | ● none | derived | — · *it is one* |
| [Spend money or tokens against an account it holds](../../../../../map/capabilities/write.budget.tenant/index.md) `write.budget.tenant` | ● none | derived | — · *if the credential is billed* |

## What narrows it

For each capability in the grant: the specific setting or arrangement that narrows it, what it costs, and the tier the control reaches afterwards. Guidance is free and stays free.

| Capability | The setting | What it costs | Tier after |
|---|---|---|---|
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) | scoped, short-lived tokens issued to the agent rather than your own; read-only where read is all it needs | an hour per service, and rotation | boundary |
| [Create something that outlives the turn where it runs (a cron, a service)](../../../../../map/capabilities/create.schedule.host/index.md) | no scheduler in the agent's environment; anything that outlives the turn goes through a person | you create the routine | boundary |
| [Run programs as the account](../../../../../map/capabilities/execute.process.host/index.md) | keep the confirmation prompt on for commands, and run in a container: execution survives inside it and stops being execution on your machine | a click per command · an afternoon for the container | setting (prompt) · boundary (container) |
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) | run the agent in a container with only the project mounted, or under a separate user account | an afternoon, then ongoing friction (container) · days, and it fights you (account) | boundary |
| [Reach any host on the internet](../../../../../map/capabilities/send.endpoint.world/index.md) | route outbound traffic through an allow-list — the one control the hosted container already has, demonstrated rather than claimed | an hour, if you already have somewhere to put it | boundary |
| [Spend money or tokens against an account it holds](../../../../../map/capabilities/write.budget.tenant/index.md) | a spend cap at the supplier, set by somebody other than the agent — the supplier has a reason to refuse: it is paying | the work stops when the cap is reached, which is the point | boundary |
| [Change any file the account can reach](../../../../../map/capabilities/write.file.host/index.md) | the same container or account; the tool's own directory restriction is a setting anything running as you can step around | as above | boundary |

## Against the mandates

What a reasonable person wanted from this setup, and the gap: ▲ excess is what it can do that they did not want; ▼ shortfall is what they wanted that it cannot do.

| Mandate | Excess | Shortfall |
|---|---|---|
| [A scheduled job under a service account](../../../../../map/mandates/scheduled-job-under-a-service-account/index.md) | ▲ 2 | ▼ 1 |

## Sources

- `brief v0.33.65: things nobody calls an agent — a scheduled job with a service account`

> A **derived** row is an inference from what this kind of program architecturally is. It is a claim, and the most useful pull request on this page is one that replaces a claim with a probe run — [how](../../../../../map/contribute/index.md).

---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/grants/generic/scheduled-job/service-account/index.html)*
