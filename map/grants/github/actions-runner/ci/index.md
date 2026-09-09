# GitHub Actions — hosted runner

> Actions runner (a hosted CI job): what it can reach, tool by tool, with the control on the path and the evidence behind each row.

*Source: <https://what-can-it-do.games.sgit.ai/map/grants/github/actions-runner/ci/index.html> · site v0.4.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../../../index.md) / [The map](../../../../../map/index.md) / [The products](../../../../../map/grants/index.md) / GitHub Actions — hosted runner

# Actions runner (a hosted CI job)

An ephemeral CI job with no agent, no hooks, and one platform-enforced grant: the workflow's permissions block. MEASURED on 26 August by measure.py inside the runner (the library's second entry), translated into findings on 5 September. Unrestricted egress; the token cannot write.

**GitHub** · surface `ci` · variant `ci` · profile version `2026-08-26` · reaches **8** of 23 capabilities, **3** of which cannot be undone. [Edit this profile](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/profiles/github/actions-runner/ci.json) · [the file](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/blob/dev/data/profiles/github/actions-runner/ci.json).

| Capability | Undo | GitHub Actions (hosted runner) |
|---|---|---|
| **filesystem** — files and directories | |  |
| Read the project it is working on `read.file.project` | yes | ● |
| Change the project it is working on `write.file.project` | with-effort | ● |
| Read any file the account can reach `read.file.host` | no | ● |
| Change any file the account can reach `write.file.host` | with-effort | ● |
| Delete files anywhere the account can reach `delete.file.host` | no | ● |
| Read a retained record: shell history, past sessions `read.record.history` | no | · |
| **process** — programs and their execution | |  |
| Run programs as the account `execute.process.host` | with-effort | ● |
| Run programs inside its own sandbox only `execute.process.self` | yes | · |
| **network** — endpoints and hosts | |  |
| Reach a permitted list of hosts `send.endpoint.allowed` | no | · |
| Reach any host on the internet `send.endpoint.world` | no | ● |
| **identity** — credentials and who the agent can act as | |  |
| Read credentials stored where it runs `read.credential.host` | no | · |
| Act in accounts with the credentials it holds `authenticate-as.credential.tenant` | no | · |
| Change its own permission settings `grant.credential.self` | yes | · |
| **communication** — messages to people | |  |
| Send a message to anyone `send.message.world` | no | · |
| Read mail or chat it is connected to `read.message.tenant` | no | · |
| **code** — repositories and what lands in them | |  |
| Commit to the repository it was pointed at `write.repository.project` | with-effort | ○ |
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
| host | the runner — destroyed after the job; not your machine |
| tenant | the repository, with the workflow's token |
| world | the internet, unrestricted |

## What it cannot reach, and why

| What | Why | Source |
|---|---|---|
| your machine | a hosted runner | library entry 2 |
| the repository, for writing | the token is contents:read | evidence: ci.permissions-block |

## The grant, tool by tool

Two tools in one session reach different things, which is why the unit of mapping is the tool and not the product. Each row carries the control on the path and the tier of evidence behind it.

### the job's shell — measured, `evidence/github__actions-runner__ci__shell__2026-08-26.json`

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Run programs as the account](../../../../../map/capabilities/execute.process.host/index.md) `execute.process.host` | ● none | observed | — · *runs as uid 1001; passwordless escalation available (n1a) — programs run as this user and can escalate* |
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) `read.file.host` | ● none | observed | — · *the runner's user with passwordless escalation: every file on the ephemeral machine* |
| [Change any file the account can reach](../../../../../map/capabilities/write.file.host/index.md) `write.file.host` | ● none | observed | — · *the runner's user with passwordless escalation: every file on the ephemeral machine* |
| [Delete files anywhere the account can reach](../../../../../map/capabilities/delete.file.host/index.md) `delete.file.host` | ● none | observed | — · *the runner's user with passwordless escalation: every file on the ephemeral machine* |
| [Reach any host on the internet](../../../../../map/capabilities/send.endpoint.world/index.md) `send.endpoint.world` | ● none | observed | — · *github.com 200, pypi.org 200, example.com 200 — UNRESTRICTED egress, no proxy* |
| [Commit to the repository it was pointed at](../../../../../map/capabilities/write.repository.project/index.md) `write.repository.project` | ○ boundary | observed | the checkout is writable, but the token is contents:read, so nothing written can leave · *the checked-out tree at this ref is writable by the job* |
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) `read.file.project` | ● none | observed | — · *the checked-out tree at this ref is readable — including anything a contributor committed by mistake* |
| [Change the project it is working on](../../../../../map/capabilities/write.file.project/index.md) `write.file.project` | ● none | observed | — · *the checked-out tree at this ref is writable by the job* |

## What narrows it

For each capability in the grant: the specific setting or arrangement that narrows it, what it costs, and the tier the control reaches afterwards. Guidance is free and stays free.

| Capability | The setting | What it costs | Tier after |
|---|---|---|---|
| [Delete files anywhere the account can reach](../../../../../map/capabilities/delete.file.host/index.md) | the same container or account; and a backup that the agent cannot reach, because delete at host reach is irreversible | as above, plus a backup outside the grant | boundary |
| [Run programs as the account](../../../../../map/capabilities/execute.process.host/index.md) | keep the confirmation prompt on for commands, and run in a container: execution survives inside it and stops being execution on your machine | a click per command · an afternoon for the container | setting (prompt) · boundary (container) |
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) | run the agent in a container with only the project mounted, or under a separate user account | an afternoon, then ongoing friction (container) · days, and it fights you (account) | boundary |
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) | none: this is what it is for | nothing | none |
| [Reach any host on the internet](../../../../../map/capabilities/send.endpoint.world/index.md) | route outbound traffic through an allow-list — the one control the hosted container already has, demonstrated rather than claimed | an hour, if you already have somewhere to put it | boundary |
| [Change any file the account can reach](../../../../../map/capabilities/write.file.host/index.md) | the same container or account; the tool's own directory restriction is a setting anything running as you can step around | as above | boundary |
| [Change the project it is working on](../../../../../map/capabilities/write.file.project/index.md) | a review before merge | a reviewer's time | setting |
| [Commit to the repository it was pointed at](../../../../../map/capabilities/write.repository.project/index.md) | none needed for most work; a review before merge is the control | a reviewer's time | setting |

## Against the mandates

What a reasonable person wanted from this setup, and the gap: ▲ excess is what it can do that they did not want; ▼ shortfall is what they wanted that it cannot do.

| Mandate | Excess | Shortfall |
|---|---|---|
| [A CI job on a hosted runner](../../../../../map/mandates/ci-job/index.md) | ▲ 0 | ▼ 1 |

## Sources

- `packs/grant-and-mandate/library/github-actions-runner__ci__2026-08-26.json`
- `experiments/the-deploy/index.html`

> A **derived** row is an inference from what this kind of program architecturally is. It is a claim, and the most useful pull request on this page is one that replaces a claim with a probe run — [how](../../../../../map/contribute/index.md).

---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/grants/github/actions-runner/ci/index.html)*
