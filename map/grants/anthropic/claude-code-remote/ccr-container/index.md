# Claude Code — web container

> Claude Code on the web (a remote session container): what it can reach, tool by tool, with the control on the path and the evidence behind each row.

*Source: <https://what-can-it-do.games.sgit.ai/map/grants/anthropic/claude-code-remote/ccr-container/index.html> · site v0.4.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../../../index.md) / [The map](../../../../../map/index.md) / [The products](../../../../../map/grants/index.md) / Claude Code — web container

# Claude Code on the web (a remote session container)

A managed cloud container, ephemeral, one git repository attached, an egress proxy above it, and a set of harness tools scoped by the platform. MEASURED, by the thing being profiled: the shell probed on 5 September with probes/run.py, the fetch tool's reach and the harness tools reported by the operator. HOST MEANS THE CONTAINER, not your machine; TENANT means the platform's scoped tokens, not your accounts. The same environment measured on 26 August is the Grant & Mandate library's first entry, and the two agree on every row they share.

**Anthropic** · surface `agentbox` · variant `ccr-container` · profile version `2026-09-05.2` · reaches **15** of 23 capabilities, **7** of which cannot be undone. [Edit this profile](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/profiles/anthropic/claude-code-remote/ccr-container.json) · [the file](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/blob/dev/data/profiles/anthropic/claude-code-remote/ccr-container.json).

| Capability | Undo | Claude Code (web container) |
|---|---|---|
| **filesystem** — files and directories | |  |
| Read the project it is working on `read.file.project` | yes | ● |
| Change the project it is working on `write.file.project` | with-effort | ● |
| Read any file the account can reach `read.file.host` | no | ● |
| Change any file the account can reach `write.file.host` | with-effort | ● |
| Delete files anywhere the account can reach `delete.file.host` | no | ● |
| Read a retained record: shell history, past sessions `read.record.history` | no | ● |
| **process** — programs and their execution | |  |
| Run programs as the account `execute.process.host` | with-effort | ● |
| Run programs inside its own sandbox only `execute.process.self` | yes | · |
| **network** — endpoints and hosts | |  |
| Reach a permitted list of hosts `send.endpoint.allowed` | no | ○ |
| Reach any host on the internet `send.endpoint.world` | no | · |
| **identity** — credentials and who the agent can act as | |  |
| Read credentials stored where it runs `read.credential.host` | no | ● |
| Act in accounts with the credentials it holds `authenticate-as.credential.tenant` | no | ○ |
| Change its own permission settings `grant.credential.self` | yes | · |
| **communication** — messages to people | |  |
| Send a message to anyone `send.message.world` | no | · |
| Read mail or chat it is connected to `read.message.tenant` | no | · |
| **code** — repositories and what lands in them | |  |
| Commit to the repository it was pointed at `write.repository.project` | with-effort | ● |
| Push to a code host (any branch it can reach) `write.repository.tenant` | with-effort | ◐ |
| Sign commits with the key it holds `authenticate-as.credential.signing` | no | ● |
| Publish packages, images or pages under the name it holds `create.record.world` | no | · |
| **money** — budgets and spend | |  |
| Spend money or tokens against an account it holds `write.budget.tenant` | no | · |
| **schedule** — things that outlive the turn | |  |
| Create something that outlives the turn where it runs (a cron, a service) `create.schedule.host` | yes | ○ |
| Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) `create.schedule.tenant` | yes | ◐ |
| **browser** — what a browser extension or automation can see and do in your browser | |  |
| Read every page you visit `read.record.browsing` | no | · |

## What host, tenant and world mean here

| Reach | Here, it means |
|---|---|
| host | this container — ephemeral, the vendor's; not your machine |
| tenant | the attached repository and the platform's scoped tokens; not your accounts |
| world | the hosts the proxy allows |

## What it cannot reach, and why

| What | Why | Source |
|---|---|---|
| your machine's files | the container has no path to the operator's computer; the assess tree records home as a boundary | assess/library.json (agentbox: home) |
| your credentials | no user credential is in the image; the keys present are the session's own | evidence: filesystem.credential-presence, 5 Sep |
| hosts the proxy refuses | a 403 on the CONNECT, set above the process | evidence: network.egress-shell |
| repositories outside the platform's scope | the token is scoped by the platform; the API tool refuses out-of-scope calls | harness.platform-tools, self-reported |

## The grant, tool by tool

Two tools in one session reach different things, which is why the unit of mapping is the tool and not the product. Each row carries the control on the path and the tier of evidence behind it.

### shell (Bash) — measured, `evidence/anthropic__claude-code-remote__ccr-container__shell__2026-09-05.json`

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Run programs as the account](../../../../../map/capabilities/execute.process.host/index.md) `execute.process.host` | ● none | observed | — · *root inside the container: every process and file IN THE CONTAINER. The container is the host; your machine is not reachable* |
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) `read.file.host` | ● none | observed | — · *any file in the container — the attached clone, the harness's state, the system. Not your machine's files (the assess tree's 'home: boundary')* |
| [Change any file the account can reach](../../../../../map/capabilities/write.file.host/index.md) `write.file.host` | ● none | observed | — · *a zero-byte file was created and removed in /etc: system configuration of the container is writable* |
| [Delete files anywhere the account can reach](../../../../../map/capabilities/delete.file.host/index.md) `delete.file.host` | ● none | observed | — · *anything in the container, including the clone; irreversible for the container, and the container is disposable* |
| [Read credentials stored where it runs](../../../../../map/capabilities/read.credential.host/index.md) `read.credential.host` | ● none | observed | — · *the credential-shaped paths present are the SESSION'S OWN: its commit-signing key and its vault keystore. No user credential is in the container; presence cannot tell whose a key is, so this is the operator's account* |
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) `authenticate-as.credential.tenant` | ○ boundary | inferred | the token's scope, set by the platform (in-scope repositories only) · *five key-shaped variables and a code-host token — the platform's, scoped to in-scope repositories; it acts as the platform's app, never as you* |
| [Read a retained record: shell history, past sessions](../../../../../map/capabilities/read.record.history/index.md) `read.record.history` | ● none | observed | — · *the harness's project directory holds this session's own earlier tool outputs; no user shell history exists here* |
| [Reach a permitted list of hosts](../../../../../map/capabilities/send.endpoint.allowed/index.md) `send.endpoint.allowed` | ○ boundary | observed | a mandatory egress proxy configured above this process — hosts it refuses are refused with a 403 on the CONNECT; the six hosts probed on 5 September all answered · *six of six probed hosts answered through the proxy; a sibling container measured on 4 September had three refused: same product, two policies* |
| [Commit to the repository it was pointed at](../../../../../map/capabilities/write.repository.project/index.md) `write.repository.project` | ● none | observed | — · *a repository is attached and writable* |
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) `read.file.project` | ● none | observed | — · *the attached working tree is readable* |
| [Change the project it is working on](../../../../../map/capabilities/write.file.project/index.md) `write.file.project` | ● none | observed | — · *the attached working tree is writable* |
| [Push to a code host (any branch it can reach)](../../../../../map/capabilities/write.repository.tenant/index.md) `write.repository.tenant` | ◐ setting | observed | pre-commit and pre-push hooks in the clone (the mandate hook and the insurance policy) — refuse by exit code, --no-verify passes; no branch rule at the host · *the attached repository only (any branch it can reach); branch discipline is the clone's hooks, a setting; no rule at the host* |
| [Sign commits with the key it holds](../../../../../map/capabilities/authenticate-as.credential.signing/index.md) `authenticate-as.credential.signing` | ● none | observed | — · *commits are signed with the session's own key, registered as an agent identity in this site's registry (sha256-f9facb4c94da6c19) — not with yours* |
| [Create something that outlives the turn where it runs (a cron, a service)](../../../../../map/capabilities/create.schedule.host/index.md) `create.schedule.host` | ○ boundary | observed | the container is ephemeral: whatever is scheduled here dies with it · *systemctl and /etc/cron.d exist, so a cron can be written — and dies with the container; the real scheduler is the platform's routines, on the harness row* |

### fetch (WebFetch) — measured, `evidence/anthropic__claude-code-remote__ccr-container__fetch__2026-09-05.json`

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Reach a permitted list of hosts](../../../../../map/capabilities/send.endpoint.allowed/index.md) `send.endpoint.allowed` | ○ boundary | self-reported | the fetch tool's own allow-list — not observable from the shell, not the proxy's · *reached sgit.ai and riskmandate.ai during this session, by the operator's account; what it cannot reach is unknown* |

### harness (MCP and built-in tools) — measured, `evidence/anthropic__claude-code-remote__ccr-container__harness__2026-09-05.json`

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Push to a code host (any branch it can reach)](../../../../../map/capabilities/write.repository.tenant/index.md) `write.repository.tenant` | ○ boundary | self-reported | the platform's token scope — and NOT the clone's git hooks, which this path never runs · *a code-host API tool writes to in-scope repositories without passing pre-commit or pre-push: the mandate hook and the insurance policy bound the git tool, not this one* |
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) `authenticate-as.credential.tenant` | ○ boundary | self-reported | the platform's token scope · *acts on the code host as the platform's app, scoped; never as you* |
| [Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session)](../../../../../map/capabilities/create.schedule.tenant/index.md) `create.schedule.tenant` | ◐ setting | self-reported | the platform's routines are the operator's to list and delete · *a routine or a scheduled trigger resumes this session or spawns another later: it outlives the container* |
| [Reach a permitted list of hosts](../../../../../map/capabilities/send.endpoint.allowed/index.md) `send.endpoint.allowed` | ○ boundary | self-reported | the fetch tool's allow-list · *the fetch tool, again, as a harness tool* |
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) `read.file.project` | ● none | self-reported | — · *file tools over the attached working tree* |

## What narrows it

For each capability in the grant: the specific setting or arrangement that narrows it, what it costs, and the tier the control reaches afterwards. Guidance is free and stays free.

| Capability | The setting | What it costs | Tier after |
|---|---|---|---|
| [Sign commits with the key it holds](../../../../../map/capabilities/authenticate-as.credential.signing/index.md) | a signing key of the agent's own, so its commits are signed as it and not as you (the registry's identity records exist for this) | an hour, and a second key to manage | boundary |
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) | scoped, short-lived tokens issued to the agent rather than your own; read-only where read is all it needs | an hour per service, and rotation | boundary |
| [Create something that outlives the turn where it runs (a cron, a service)](../../../../../map/capabilities/create.schedule.host/index.md) | no scheduler in the agent's environment; anything that outlives the turn goes through a person | you create the routine | boundary |
| [Delete files anywhere the account can reach](../../../../../map/capabilities/delete.file.host/index.md) | the same container or account; and a backup that the agent cannot reach, because delete at host reach is irreversible | as above, plus a backup outside the grant | boundary |
| [Run programs as the account](../../../../../map/capabilities/execute.process.host/index.md) | keep the confirmation prompt on for commands, and run in a container: execution survives inside it and stops being execution on your machine | a click per command · an afternoon for the container | setting (prompt) · boundary (container) |
| [Read credentials stored where it runs](../../../../../map/capabilities/read.credential.host/index.md) | keep credentials out of the account the agent runs as: a credential helper, a separate account, or a container without your home mounted | an afternoon, and re-authenticating where the agent needs a credential of its own | boundary |
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) | run the agent in a container with only the project mounted, or under a separate user account | an afternoon, then ongoing friction (container) · days, and it fights you (account) | boundary |
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) | none: this is what it is for | nothing | none |
| [Read a retained record: shell history, past sessions](../../../../../map/capabilities/read.record.history/index.md) | history off, or a fresh environment per task, so the grant is a tree over the present rather than a union over every prior turn | the agent forgets between tasks | boundary |
| [Reach a permitted list of hosts](../../../../../map/capabilities/send.endpoint.allowed/index.md) | shorten the list; a host it does not need is a host it can reach | minutes per host, and a failure the first time it needs one you removed | boundary |
| [Change any file the account can reach](../../../../../map/capabilities/write.file.host/index.md) | the same container or account; the tool's own directory restriction is a setting anything running as you can step around | as above | boundary |
| [Change the project it is working on](../../../../../map/capabilities/write.file.project/index.md) | a review before merge | a reviewer's time | setting |
| [Commit to the repository it was pointed at](../../../../../map/capabilities/write.repository.project/index.md) | none needed for most work; a review before merge is the control | a reviewer's time | setting |
| [Push to a code host (any branch it can reach)](../../../../../map/capabilities/write.repository.tenant/index.md) | a branch protection rule at the host — the agent cannot edit it — and a pre-push hook in the clone for the earlier, cheaper refusal | minutes; and a review step before anything deploys | boundary (host rule) · setting (hook) |

## Against the mandates

What a reasonable person wanted from this setup, and the gap: ▲ excess is what it can do that they did not want; ▼ shortfall is what they wanted that it cannot do.

| Mandate | Excess | Shortfall |
|---|---|---|
| [A coding assistant in a container on the web](../../../../../map/mandates/coding-assistant-in-a-container/index.md) | ▲ 3 | ▼ 0 |

## Sources

- `evidence/anthropic__claude-code-remote__ccr-container__shell__2026-09-05.json`
- `evidence/anthropic__claude-code-remote__ccr-container__fetch__2026-09-05.json`
- `evidence/anthropic__claude-code-remote__ccr-container__harness__2026-09-05.json`
- `packs/grant-and-mandate/library/claude-code-remote__ccr-container__2026-08-26.json (the same environment, 26 August)`

> A **derived** row is an inference from what this kind of program architecturally is. It is a claim, and the most useful pull request on this page is one that replaces a claim with a probe run — [how](../../../../../map/contribute/index.md).

---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/grants/anthropic/claude-code-remote/ccr-container/index.html)*
