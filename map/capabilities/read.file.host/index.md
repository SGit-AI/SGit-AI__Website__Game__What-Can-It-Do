# Read any file the account can reach

> read.file.host: which products grant it, what stands in the way, what narrows it, and who wants it.

*Source: <https://what-can-it-do.games.sgit.ai/map/capabilities/read.file.host/index.html> · site v0.7.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../index.md) / [The map](../../../map/index.md) / [The capabilities](../../../map/capabilities/index.md) / Read any file the account can reach

# Read any file the account can reach

`read.file.host` — **read** × **file** at **host** reach (the machine, container or account it runs as). Family: filesystem. Effect: **cannot be undone**.

## Granted by 7 of 9

| Profile | Control on the path | Evidence | Via |
|---|---|---|---|
| [Claude Code — web container](../../../map/grants/anthropic/claude-code-remote/ccr-container/index.md) | ● none | observed | shell (Bash) |
| [Claude Code — local · confirm off](../../../map/grants/anthropic/claude-code/local-confirmations-off/index.md) | ● none | derived | shell (Bash), files (Read, Edit, Write) |
| [Claude Code — local · confirm on](../../../map/grants/anthropic/claude-code/local-default/index.md) | ● none | derived | shell (Bash), files (Read, Edit, Write) |
| [Claude Desktop — local tools](../../../map/grants/anthropic/claude-desktop/default/index.md) | ◐ setting | derived | local files and commands (when enabled) |
| [Claude.ai — connectors on](../../../map/grants/anthropic/claude-web/connectors-on/index.md) | ○ boundary | derived | connectors |
| [Scheduled job — service account](../../../map/grants/generic/scheduled-job/service-account/index.md) | ● none | derived | the job |
| [GitHub Actions — hosted runner](../../../map/grants/github/actions-runner/ci/index.md) | ● none | observed | the job's shell |

## What narrows it

**The setting:** run the agent in a container with only the project mounted, or under a separate user account

**What it costs:** an afternoon, then ongoing friction (container) · days, and it fights you (account)

**Tier after:** boundary

## Questions that ask about it

- *Can it read files on your machine that are not the project?* — eliciting, reliability 0.35

## In the mandates

- **wanted** by [Chat, with connectors switched on](../../../map/mandates/chat-with-connectors/index.md)
- **wanted** by [A scheduled job under a service account](../../../map/mandates/scheduled-job-under-a-service-account/index.md)
- **not wanted** by [A coding assistant on my machine](../../../map/mandates/coding-assistant-on-my-machine/index.md)
- **not wanted** by [Chat in the browser, nothing connected](../../../map/mandates/chat-no-connectors/index.md)

[Edit the primitives](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/primitives.json) · [edit the reductions](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/reductions.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/capabilities/read.file.host/index.html)*
