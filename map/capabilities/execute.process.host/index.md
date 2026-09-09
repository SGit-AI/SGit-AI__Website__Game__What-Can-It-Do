# Run programs as the account

> execute.process.host: which products grant it, what stands in the way, what narrows it, and who wants it.

*Source: <https://what-can-it-do.games.sgit.ai/map/capabilities/execute.process.host/index.html> · site v0.4.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../index.md) / [The map](../../../map/index.md) / [The capabilities](../../../map/capabilities/index.md) / Run programs as the account

# Run programs as the account

`execute.process.host` — **execute** × **process** at **host** reach (the machine, container or account it runs as). Family: process. Effect: **recoverable from a backup, a history or a revert, at a cost**.

## Granted by 6 of 9

| Profile | Control on the path | Evidence | Via |
|---|---|---|---|
| [Claude Code — web container](../../../map/grants/anthropic/claude-code-remote/ccr-container/index.md) | ● none | observed | shell (Bash) |
| [Claude Code — local · confirm off](../../../map/grants/anthropic/claude-code/local-confirmations-off/index.md) | ● none | derived | shell (Bash) |
| [Claude Code — local · confirm on](../../../map/grants/anthropic/claude-code/local-default/index.md) | ◐ setting | derived | shell (Bash) |
| [Claude Desktop — local tools](../../../map/grants/anthropic/claude-desktop/default/index.md) | ◐ setting | derived | local files and commands (when enabled) |
| [Scheduled job — service account](../../../map/grants/generic/scheduled-job/service-account/index.md) | ● none | derived | the job |
| [GitHub Actions — hosted runner](../../../map/grants/github/actions-runner/ci/index.md) | ● none | observed | the job's shell |

## What narrows it

**The setting:** keep the confirmation prompt on for commands, and run in a container: execution survives inside it and stops being execution on your machine

**What it costs:** a click per command · an afternoon for the container

**Tier after:** setting (prompt) · boundary (container)

## Questions that ask about it

- *Have you ever clicked something that said 'always allow', or turned its confirmations off?* — eliciting, reliability 0.6

## In the mandates

- **wanted** by [A coding assistant on my machine](../../../map/mandates/coding-assistant-on-my-machine/index.md)
- **wanted** by [A coding assistant in a container on the web](../../../map/mandates/coding-assistant-in-a-container/index.md)
- **wanted** by [A CI job on a hosted runner](../../../map/mandates/ci-job/index.md)
- **wanted** by [A scheduled job under a service account](../../../map/mandates/scheduled-job-under-a-service-account/index.md)
- **not wanted** by [The desktop app, with local tools switched on](../../../map/mandates/desktop-app-with-local-tools/index.md)
- **not wanted** by [Chat in the browser, nothing connected](../../../map/mandates/chat-no-connectors/index.md)

[Edit the primitives](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/primitives.json) · [edit the reductions](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/reductions.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/capabilities/execute.process.host/index.html)*
