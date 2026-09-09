# A scheduled job under a service account

> A starting mandate for service: Run on schedule, read its own data, talk to the APIs it was built for with the account it was given, and stop. I did not want it spending mo…

*Source: <https://what-can-it-do.games.sgit.ai/map/mandates/scheduled-job-under-a-service-account/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../index.md) / [The map](../../../map/index.md) / [The mandates](../../../map/mandates/index.md) / A scheduled job under a service account

# A scheduled job under a service account

Run on schedule, read its own data, talk to the APIs it was built for with the account it was given, and stop. I did not want it spending money unattended or reaching arbitrary hosts.

Status: **starting-point** · authored 2026-09-09 · the site, as a starting point — not measured, not surveyed; the first thing to argue with · [edit this mandate](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/mandates/scheduled-job-under-a-service-account.json)

## The delta

Against every profile this mandate applies to. ▲ is authority you did not ask for; ▼ is something you were counting on that is not there. The tally is at the bottom.

Legend: ▲ excess — it can, and you did not want it to · ▼ shortfall — it cannot, and you wanted it to · ✓ aligned — it can, and you wanted it to · – aligned — it cannot, and you did not want it to · ? it can, and the mandate does not say · · it cannot, and the mandate does not say

| Capability | Scheduled job (service account) |
|---|---|
| **filesystem** |  |
| Read the project it is working on | · |
| Change the project it is working on | · |
| Read any file the account can reach | ✓ |
| Change any file the account can reach | ? |
| Delete files anywhere the account can reach | · |
| Read a retained record: shell history, past sessions | · |
| **process** |  |
| Run programs as the account | ✓ |
| Run programs inside its own sandbox only | · |
| **network** |  |
| Reach a permitted list of hosts | ▼ |
| Reach any host on the internet | ▲ |
| **identity** |  |
| Read credentials stored where it runs | · |
| Act in accounts with the credentials it holds | ✓ |
| Change its own permission settings | · |
| **communication** |  |
| Send a message to anyone | · |
| Read mail or chat it is connected to | · |
| **code** |  |
| Commit to the repository it was pointed at | · |
| Push to a code host (any branch it can reach) | · |
| Sign commits with the key it holds | · |
| Publish packages, images or pages under the name it holds | · |
| **money** |  |
| Spend money or tokens against an account it holds | ▲ |
| **schedule** |  |
| Create something that outlives the turn where it runs (a cron, a service) — *unstated: it is itself scheduled; whether it may schedule more of itself is a real question and the mandate does not pretend to answer it* | ? |
| Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) | · |
| **browser** |  |
| Read every page you visit | · |
| **The delta** | ▲ 2 · ▼ 1 |

## In words

- **Scheduled job — service account:** excess — Reach any host on the internet; Spend money or tokens against an account it holds. Shortfall — Reach a permitted list of hosts.

## The mandate, row by row

| Capability | Position | Note |
|---|---|---|
| [Run programs as the account](../../../map/capabilities/execute.process.host/index.md) | want |  |
| [Read any file the account can reach](../../../map/capabilities/read.file.host/index.md) | want |  |
| [Reach a permitted list of hosts](../../../map/capabilities/send.endpoint.allowed/index.md) | want |  |
| [Act in accounts with the credentials it holds](../../../map/capabilities/authenticate-as.credential.tenant/index.md) | want |  |
| [Spend money or tokens against an account it holds](../../../map/capabilities/write.budget.tenant/index.md) | do not want |  |
| [Reach any host on the internet](../../../map/capabilities/send.endpoint.world/index.md) | do not want |  |
| [Create something that outlives the turn where it runs (a cron, a service)](../../../map/capabilities/create.schedule.host/index.md) | unstated | unstated: it is itself scheduled; whether it may schedule more of itself is a real question and the mandate does not pretend to answer it |

> **You cannot deny the excess rows.** The agent already has the access. What is left is how long you are prepared to live with each one and who says so — [what to do next](../../../what-next/index.md).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/mandates/scheduled-job-under-a-service-account/index.html)*
