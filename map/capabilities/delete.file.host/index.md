# Delete files anywhere the account can reach

> delete.file.host: which products grant it, what stands in the way, what narrows it, and who wants it.

*Source: <https://what-can-it-do.games.sgit.ai/map/capabilities/delete.file.host/index.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../index.md) / [The map](../../../map/index.md) / [The capabilities](../../../map/capabilities/index.md) / Delete files anywhere the account can reach

# Delete files anywhere the account can reach

`delete.file.host` — **delete** × **file** at **host** reach (the machine, container or account it runs as). Family: filesystem. Effect: **cannot be undone**.

## Granted by 4 of 9

| Profile | Control on the path | Evidence | Via |
|---|---|---|---|
| [Claude Code — web container](../../../map/grants/anthropic/claude-code-remote/ccr-container/index.md) | ● none | observed | shell (Bash) |
| [Claude Code — local · confirm off](../../../map/grants/anthropic/claude-code/local-confirmations-off/index.md) | ● none | derived | shell (Bash), files (Read, Edit, Write) |
| [Claude Code — local · confirm on](../../../map/grants/anthropic/claude-code/local-default/index.md) | ● none | derived | shell (Bash), files (Read, Edit, Write) |
| [GitHub Actions — hosted runner](../../../map/grants/github/actions-runner/ci/index.md) | ● none | observed | the job's shell |

## What narrows it

**The setting:** the same container or account; and a backup that the agent cannot reach, because delete at host reach is irreversible

**What it costs:** as above, plus a backup outside the grant

**Tier after:** boundary

## In the mandates

- **not wanted** by [A coding assistant on my machine](../../../map/mandates/coding-assistant-on-my-machine/index.md)
- **not wanted** by [Chat in the browser, nothing connected](../../../map/mandates/chat-no-connectors/index.md)

[Edit the primitives](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/primitives.json) · [edit the reductions](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/reductions.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/capabilities/delete.file.host/index.html)*
