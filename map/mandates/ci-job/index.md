# A CI job on a hosted runner

> A starting mandate for ci: Check out the code, build it, run the tests, fetch what it needs, and — when a release is cut — push the tag. I did not want it reading cred…

*Source: <https://what-can-it-do.games.sgit.ai/map/mandates/ci-job/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../index.md) / [The map](../../../map/index.md) / [The mandates](../../../map/mandates/index.md) / A CI job on a hosted runner

# A CI job on a hosted runner

Check out the code, build it, run the tests, fetch what it needs, and — when a release is cut — push the tag. I did not want it reading credentials beyond its own token.

Status: **starting-point** · authored 2026-09-09 · the site, as a starting point — not measured, not surveyed; the first thing to argue with · [edit this mandate](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/mandates/ci-job.json)

## The delta

Against every profile this mandate applies to. ▲ is authority you did not ask for; ▼ is something you were counting on that is not there. The tally is at the bottom.

Legend: ▲ excess — it can, and you did not want it to · ▼ shortfall — it cannot, and you wanted it to · ✓ aligned — it can, and you wanted it to · – aligned — it cannot, and you did not want it to · ? it can, and the mandate does not say · · it cannot, and the mandate does not say

| Capability | GitHub Actions (hosted runner) |
|---|---|
| **filesystem** |  |
| Read the project it is working on | ✓ |
| Change the project it is working on | ✓ |
| Read any file the account can reach | ? |
| Change any file the account can reach | ? |
| Delete files anywhere the account can reach — *unstated: the runner is destroyed after the job* | ? |
| Read a retained record: shell history, past sessions | · |
| **process** |  |
| Run programs as the account | ✓ |
| Run programs inside its own sandbox only | · |
| **network** |  |
| Reach a permitted list of hosts | · |
| Reach any host on the internet | ✓ |
| **identity** |  |
| Read credentials stored where it runs | – |
| Act in accounts with the credentials it holds | · |
| Change its own permission settings | · |
| **communication** |  |
| Send a message to anyone | · |
| Read mail or chat it is connected to | · |
| **code** |  |
| Commit to the repository it was pointed at | ? |
| Push to a code host (any branch it can reach) — *deliberately in the mandate: most release workflows push a tag, and this profile's token is contents:read — so this row is a shortfall, and the kind the game calls ‘a gap you were counting on’* | ▼ |
| Sign commits with the key it holds | · |
| Publish packages, images or pages under the name it holds | · |
| **money** |  |
| Spend money or tokens against an account it holds | · |
| **schedule** |  |
| Create something that outlives the turn where it runs (a cron, a service) | · |
| Create something that outlives the session, on the platform (a routine, a scheduled trigger, a new session) | · |
| **browser** |  |
| Read every page you visit | · |
| **The delta** | ▲ 0 · ▼ 1 |

## In words

- **GitHub Actions — hosted runner:** no excess. Shortfall — Push to a code host (any branch it can reach).

## The mandate, row by row

| Capability | Position | Note |
|---|---|---|
| [Read the project it is working on](../../../map/capabilities/read.file.project/index.md) | want |  |
| [Change the project it is working on](../../../map/capabilities/write.file.project/index.md) | want |  |
| [Run programs as the account](../../../map/capabilities/execute.process.host/index.md) | want |  |
| [Reach any host on the internet](../../../map/capabilities/send.endpoint.world/index.md) | want |  |
| [Push to a code host (any branch it can reach)](../../../map/capabilities/write.repository.tenant/index.md) | want | deliberately in the mandate: most release workflows push a tag, and this profile's token is contents:read — so this row is a shortfall, and the kind the game calls ‘a gap you were counting on’ |
| [Read credentials stored where it runs](../../../map/capabilities/read.credential.host/index.md) | do not want |  |
| [Delete files anywhere the account can reach](../../../map/capabilities/delete.file.host/index.md) | unstated | unstated: the runner is destroyed after the job |

> **You cannot deny the excess rows.** The agent already has the access. What is left is how long you are prepared to live with each one and who says so — [what to do next](../../../what-next/index.md).

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/mandates/ci-job/index.html)*
