# Claude Code — local · confirm off

> Claude Code (the CLI, on your own machine): what it can reach, tool by tool, with the control on the path and the evidence behind each row.

*Source: <https://what-can-it-do.games.sgit.ai/map/grants/anthropic/claude-code/local-confirmations-off/index.html> · site v0.6.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../../../index.md) / [The map](../../../../../map/index.md) / [The products](../../../../../map/grants/index.md) / Claude Code — local · confirm off

# Claude Code (the CLI, on your own machine)

The same assistant with its confirmations turned off (an always-allow, or the flag that skips permissions). The rows are the sibling's; what changes is one control: the prompt on execution goes from a setting to nothing. The diff between this profile and local-default is the answer to 'what does turning that off actually give it'. DERIVED, not measured.

**Anthropic** · surface `cli` · variant `local-confirmations-off` · profile version `2026-09-05` · reaches **16** of 23 capabilities, **8** of which cannot be undone. [Edit this profile](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/profiles/anthropic/claude-code/local-confirmations-off.json) · [the file](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/blob/dev/data/profiles/anthropic/claude-code/local-confirmations-off.json).

| Capability | Undo | Claude Code (local · confirm off) |
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
| Commit to the repository it was pointed at `write.repository.project` | with-effort | ● |
| Push to a code host (any branch it can reach) `write.repository.tenant` | with-effort | ◉ |
| Sign commits with the key it holds `authenticate-as.credential.signing` | no | ● |
| Publish packages, images or pages under the name it holds `create.record.world` | no | ● |
| **money** — budgets and spend | |  |
| Spend money or tokens against an account it holds `write.budget.tenant` | no | · |
| **schedule** — things that outlive the turn | |  |
| Create something that outlives the turn where it runs (a cron, a service) `create.schedule.host` | yes | ● |
| Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) `create.schedule.tenant` | yes | · |
| **browser** — what a browser extension or automation can see and do in your browser | |  |
| Read every page you visit `read.record.browsing` | no | · |

## What host, tenant and world mean here

| Reach | Here, it means |
|---|---|
| host | your machine, as your user account |
| tenant | your accounts, with the credentials in your home directory |
| world | the internet |

## The grant, tool by tool

Two tools in one session reach different things, which is why the unit of mapping is the tool and not the product. Each row carries the control on the path and the tier of evidence behind it.

### shell (Bash)

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Run programs as the account](../../../../../map/capabilities/execute.process.host/index.md) `execute.process.host` | ● none | derived | none — confirmations disabled; the tool runs whatever it decides to run |
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) `read.file.host` | ● none | derived | — · *everything your account can read, because a shell as you reads as you* |
| [Change any file the account can reach](../../../../../map/capabilities/write.file.host/index.md) `write.file.host` | ● none | derived | — |
| [Delete files anywhere the account can reach](../../../../../map/capabilities/delete.file.host/index.md) `delete.file.host` | ● none | derived | — |
| [Reach any host on the internet](../../../../../map/capabilities/send.endpoint.world/index.md) `send.endpoint.world` | ● none | derived | — · *curl reaches the world unless something above the account stops it* |
| [Read credentials stored where it runs](../../../../../map/capabilities/read.credential.host/index.md) `read.credential.host` | ● none | documented | — · *a published read-only audit tool enumerates exactly this class in a home directory* |
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) `authenticate-as.credential.tenant` | ● none | derived | — · *inferred from the credentials the account holds* |
| [Push to a code host (any branch it can reach)](../../../../../map/capabilities/write.repository.tenant/index.md) `write.repository.tenant` | ◉ expectation | derived | branch discipline in prose, if any |
| [Sign commits with the key it holds](../../../../../map/capabilities/authenticate-as.credential.signing/index.md) `authenticate-as.credential.signing` | ● none | documented | — · *if commit signing is configured for the account, the agent signs as you* |
| [Publish packages, images or pages under the name it holds](../../../../../map/capabilities/create.record.world/index.md) `create.record.world` | ● none | documented | — · *if a registry token is in the home directory* |
| [Read a retained record: shell history, past sessions](../../../../../map/capabilities/read.record.history/index.md) `read.record.history` | ● none | documented | — · *shell history and the harness's own transcripts* |
| [Change its own permission settings](../../../../../map/capabilities/grant.credential.self/index.md) `grant.credential.self` | ◐ setting | derived | the settings file is owned by the same account · *anything running as you can rewrite the file that turns the prompt off* |
| [Create something that outlives the turn where it runs (a cron, a service)](../../../../../map/capabilities/create.schedule.host/index.md) `create.schedule.host` | ● none | derived | — · *a shell as you can write a crontab* |
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) `read.file.project` | ● none | derived | — |
| [Change the project it is working on](../../../../../map/capabilities/write.file.project/index.md) `write.file.project` | ● none | derived | — |
| [Commit to the repository it was pointed at](../../../../../map/capabilities/write.repository.project/index.md) `write.repository.project` | ● none | derived | — |

### files (Read, Edit, Write)

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) `read.file.project` | ● none | derived | — |
| [Change the project it is working on](../../../../../map/capabilities/write.file.project/index.md) `write.file.project` | ● none | derived | — |
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) `read.file.host` | ◐ setting | derived | the tool's own directory restriction and its confirmation prompt — enforced by the tool, which runs inside the grant; anything that can execute as you steps around it · *outside the working tree only with the prompt, which the shell does not need* |
| [Change any file the account can reach](../../../../../map/capabilities/write.file.host/index.md) `write.file.host` | ◐ setting | derived | the tool's own directory restriction and its confirmation prompt — enforced by the tool, which runs inside the grant; anything that can execute as you steps around it |
| [Delete files anywhere the account can reach](../../../../../map/capabilities/delete.file.host/index.md) `delete.file.host` | ◐ setting | derived | the tool's own directory restriction and its confirmation prompt — enforced by the tool, which runs inside the grant; anything that can execute as you steps around it |

### fetch (WebFetch)

| Capability | Control | Evidence | What is on the path |
|---|---|---|---|
| [Reach any host on the internet](../../../../../map/capabilities/send.endpoint.world/index.md) `send.endpoint.world` | ◐ setting | derived | the tool's own domain confirmation |

## What narrows it

For each capability in the grant: the specific setting or arrangement that narrows it, what it costs, and the tier the control reaches afterwards. Guidance is free and stays free.

| Capability | The setting | What it costs | Tier after |
|---|---|---|---|
| [Sign commits with the key it holds](../../../../../map/capabilities/authenticate-as.credential.signing/index.md) | a signing key of the agent's own, so its commits are signed as it and not as you (the registry's identity records exist for this) | an hour, and a second key to manage | boundary |
| [Act in accounts with the credentials it holds](../../../../../map/capabilities/authenticate-as.credential.tenant/index.md) | scoped, short-lived tokens issued to the agent rather than your own; read-only where read is all it needs | an hour per service, and rotation | boundary |
| [Publish packages, images or pages under the name it holds](../../../../../map/capabilities/create.record.world/index.md) | no publishing token in the agent's environment; publish from CI with a token the agent does not hold | an afternoon to move the publish step | boundary |
| [Create something that outlives the turn where it runs (a cron, a service)](../../../../../map/capabilities/create.schedule.host/index.md) | no scheduler in the agent's environment; anything that outlives the turn goes through a person | you create the routine | boundary |
| [Delete files anywhere the account can reach](../../../../../map/capabilities/delete.file.host/index.md) | the same container or account; and a backup that the agent cannot reach, because delete at host reach is irreversible | as above, plus a backup outside the grant | boundary |
| [Run programs as the account](../../../../../map/capabilities/execute.process.host/index.md) | keep the confirmation prompt on for commands, and run in a container: execution survives inside it and stops being execution on your machine | a click per command · an afternoon for the container | setting (prompt) · boundary (container) |
| [Change its own permission settings](../../../../../map/capabilities/grant.credential.self/index.md) | settings owned by a different user than the one the agent runs as, or set above the session by the platform | minutes, if the platform supports it; otherwise the separate account | boundary |
| [Read credentials stored where it runs](../../../../../map/capabilities/read.credential.host/index.md) | keep credentials out of the account the agent runs as: a credential helper, a separate account, or a container without your home mounted | an afternoon, and re-authenticating where the agent needs a credential of its own | boundary |
| [Read any file the account can reach](../../../../../map/capabilities/read.file.host/index.md) | run the agent in a container with only the project mounted, or under a separate user account | an afternoon, then ongoing friction (container) · days, and it fights you (account) | boundary |
| [Read the project it is working on](../../../../../map/capabilities/read.file.project/index.md) | none: this is what it is for | nothing | none |
| [Read a retained record: shell history, past sessions](../../../../../map/capabilities/read.record.history/index.md) | history off, or a fresh environment per task, so the grant is a tree over the present rather than a union over every prior turn | the agent forgets between tasks | boundary |
| [Reach any host on the internet](../../../../../map/capabilities/send.endpoint.world/index.md) | route outbound traffic through an allow-list — the one control the hosted container already has, demonstrated rather than claimed | an hour, if you already have somewhere to put it | boundary |
| [Change any file the account can reach](../../../../../map/capabilities/write.file.host/index.md) | the same container or account; the tool's own directory restriction is a setting anything running as you can step around | as above | boundary |
| [Change the project it is working on](../../../../../map/capabilities/write.file.project/index.md) | a review before merge | a reviewer's time | setting |
| [Commit to the repository it was pointed at](../../../../../map/capabilities/write.repository.project/index.md) | none needed for most work; a review before merge is the control | a reviewer's time | setting |
| [Push to a code host (any branch it can reach)](../../../../../map/capabilities/write.repository.tenant/index.md) | a branch protection rule at the host — the agent cannot edit it — and a pre-push hook in the clone for the earlier, cheaper refusal | minutes; and a review step before anything deploys | boundary (host rule) · setting (hook) |

## Against the mandates

What a reasonable person wanted from this setup, and the gap: ▲ excess is what it can do that they did not want; ▼ shortfall is what they wanted that it cannot do.

| Mandate | Excess | Shortfall |
|---|---|---|
| [A coding assistant on my machine](../../../../../map/mandates/coding-assistant-on-my-machine/index.md) | ▲ 10 | ▼ 1 |

## Sources

- `assess/library.json (surface cli)`
- `profiles/anthropic/claude-code/local-default.json`

> A **derived** row is an inference from what this kind of program architecturally is. It is a claim, and the most useful pull request on this page is one that replaces a claim with a probe run — [how](../../../../../map/contribute/index.md).

---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/grants/anthropic/claude-code/local-confirmations-off/index.html)*
