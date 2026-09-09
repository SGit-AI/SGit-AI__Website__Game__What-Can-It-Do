# Change any file the account can reach

> write.file.host: which products grant it, what stands in the way, what narrows it, and who wants it.

*Source: <https://what-can-it-do.games.sgit.ai/map/capabilities/write.file.host/index.html> · site v0.4.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../index.md) / [The map](../../../map/index.md) / [The capabilities](../../../map/capabilities/index.md) / Change any file the account can reach

# Change any file the account can reach

`write.file.host` — **write** × **file** at **host** reach (the machine, container or account it runs as). Family: filesystem. Effect: **recoverable from a backup, a history or a revert, at a cost**.

## Granted by 6 of 9

| Profile | Control on the path | Evidence | Via |
|---|---|---|---|
| [Claude Code — web container](../../../map/grants/anthropic/claude-code-remote/ccr-container/index.md) | ● none | observed | shell (Bash) |
| [Claude Code — local · confirm off](../../../map/grants/anthropic/claude-code/local-confirmations-off/index.md) | ● none | derived | shell (Bash), files (Read, Edit, Write) |
| [Claude Code — local · confirm on](../../../map/grants/anthropic/claude-code/local-default/index.md) | ● none | derived | shell (Bash), files (Read, Edit, Write) |
| [Claude Desktop — local tools](../../../map/grants/anthropic/claude-desktop/default/index.md) | ◐ setting | derived | local files and commands (when enabled) |
| [Scheduled job — service account](../../../map/grants/generic/scheduled-job/service-account/index.md) | ● none | derived | the job |
| [GitHub Actions — hosted runner](../../../map/grants/github/actions-runner/ci/index.md) | ● none | observed | the job's shell |

## What narrows it

**The setting:** the same container or account; the tool's own directory restriction is a setting anything running as you can step around

**What it costs:** as above

**Tier after:** boundary

## In the mandates

- **not wanted** by [A coding assistant on my machine](../../../map/mandates/coding-assistant-on-my-machine/index.md)
- **not wanted** by [The desktop app, with local tools switched on](../../../map/mandates/desktop-app-with-local-tools/index.md)
- **not wanted** by [Chat in the browser, nothing connected](../../../map/mandates/chat-no-connectors/index.md)

[Edit the primitives](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/primitives.json) · [edit the reductions](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/reductions.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/capabilities/write.file.host/index.html)*
