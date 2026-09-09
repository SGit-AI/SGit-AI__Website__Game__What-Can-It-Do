# The capabilities

> The 23 capability primitives every question is built from: a verb, an object class and a reach, each carrying whether its effect can be undone.

*Source: <https://what-can-it-do.games.sgit.ai/map/capabilities/index.html> · site v0.4.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../index.md) / [The map](../../map/index.md) / The capabilities

# The capabilities

A capability is a **verb** crossed with an **object class** crossed with a **reach**, carrying whether its effect can be undone. *Read a file in the project* and *read a file anywhere the account can* are two capabilities; `/etc/passwd` is not a third — a specific path is an instance, never a new primitive.

| Capability | Id | Family | Undo | Granted by | Reduction |
|---|---|---|---|---|---|
| [Read the project it is working on](../../map/capabilities/read.file.project/index.md) | `read.file.project` | filesystem | yes | 7 | yes |
| [Change the project it is working on](../../map/capabilities/write.file.project/index.md) | `write.file.project` | filesystem | with-effort | 5 | yes |
| [Read any file the account can reach](../../map/capabilities/read.file.host/index.md) | `read.file.host` | filesystem | no | 7 | yes |
| [Change any file the account can reach](../../map/capabilities/write.file.host/index.md) | `write.file.host` | filesystem | with-effort | 6 | yes |
| [Delete files anywhere the account can reach](../../map/capabilities/delete.file.host/index.md) | `delete.file.host` | filesystem | no | 4 | yes |
| [Read a retained record: shell history, past sessions](../../map/capabilities/read.record.history/index.md) | `read.record.history` | filesystem | no | 4 | yes |
| [Run programs as the account](../../map/capabilities/execute.process.host/index.md) | `execute.process.host` | process | with-effort | 6 | yes |
| [Run programs inside its own sandbox only](../../map/capabilities/execute.process.self/index.md) | `execute.process.self` | process | yes | 0 | yes |
| [Reach a permitted list of hosts](../../map/capabilities/send.endpoint.allowed/index.md) | `send.endpoint.allowed` | network | no | 1 | yes |
| [Reach any host on the internet](../../map/capabilities/send.endpoint.world/index.md) | `send.endpoint.world` | network | no | 6 | yes |
| [Read credentials stored where it runs](../../map/capabilities/read.credential.host/index.md) | `read.credential.host` | identity | no | 4 | yes |
| [Act in accounts with the credentials it holds](../../map/capabilities/authenticate-as.credential.tenant/index.md) | `authenticate-as.credential.tenant` | identity | no | 7 | yes |
| [Change its own permission settings](../../map/capabilities/grant.credential.self/index.md) | `grant.credential.self` | identity | yes | 3 | yes |
| [Send a message to anyone](../../map/capabilities/send.message.world/index.md) | `send.message.world` | communication | no | 0 | yes |
| [Read mail or chat it is connected to](../../map/capabilities/read.message.tenant/index.md) | `read.message.tenant` | communication | no | 1 | yes |
| [Commit to the repository it was pointed at](../../map/capabilities/write.repository.project/index.md) | `write.repository.project` | code | with-effort | 4 | yes |
| [Push to a code host (any branch it can reach)](../../map/capabilities/write.repository.tenant/index.md) | `write.repository.tenant` | code | with-effort | 4 | yes |
| [Sign commits with the key it holds](../../map/capabilities/authenticate-as.credential.signing/index.md) | `authenticate-as.credential.signing` | code | no | 3 | yes |
| [Publish packages, images or pages under the name it holds](../../map/capabilities/create.record.world/index.md) | `create.record.world` | code | no | 2 | yes |
| [Spend money or tokens against an account it holds](../../map/capabilities/write.budget.tenant/index.md) | `write.budget.tenant` | money | no | 1 | yes |
| [Create something that outlives the turn where it runs (a cron, a service)](../../map/capabilities/create.schedule.host/index.md) | `create.schedule.host` | schedule | yes | 4 | yes |
| [Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session)](../../map/capabilities/create.schedule.tenant/index.md) | `create.schedule.tenant` | schedule | yes | 1 | — |
| [Read every page you visit](../../map/capabilities/read.record.browsing/index.md) | `read.record.browsing` | browser | no | 1 | yes |

## The rules the set is written under

- A specific path, host or mailbox is an instance of a primitive, never a new one.
- Reversibility sits on the primitive, not the instance, because it decides whether a gap is a nuisance or a loss — and this estate has settled that recoverability decides insurability.
- A grant containing irreversible primitives is a different object from one that does not, however many rows each has.
- The set is a starting set and will be wrong at the edges from the first week. A proposed primitive that is a specific thing is an instance; one that is a new verb, object class or reach needs a probe.
- A label never says 'your' or 'as you': what host, tenant and world mean is the profile's to say (reach_names), because for an agent in a vendor's container 'host' is the container and 'tenant' is a scoped token, not your machine and not your accounts.

## Reach

| Reach | Means |
|---|---|
| self | the agent's own process, sandbox or turn |
| project | the working tree or workspace it was pointed at |
| host | the machine, container or account it runs as |
| tenant | the organisation's accounts, repositories and services |
| world | anything on the internet |

Reach is the axis people get wrong. *Host* for an agent in a vendor's container is the container, and *tenant* is a scoped token; each product's page says what the words mean there.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/capabilities/index.html)*
