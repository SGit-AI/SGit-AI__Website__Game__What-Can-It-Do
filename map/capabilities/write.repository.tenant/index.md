# Push to a code host (any branch it can reach)

> write.repository.tenant: which products grant it, what stands in the way, what narrows it, and who wants it.

*Source: <https://what-can-it-do.games.sgit.ai/map/capabilities/write.repository.tenant/index.html> · site v0.4.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../index.md) / [The map](../../../map/index.md) / [The capabilities](../../../map/capabilities/index.md) / Push to a code host (any branch it can reach)

# Push to a code host (any branch it can reach)

`write.repository.tenant` — **write** × **repository** at **tenant** reach (the organisation's accounts, repositories and services). Family: code. Effect: **recoverable from a backup, a history or a revert, at a cost**.

## Granted by 4 of 9

| Profile | Control on the path | Evidence | Via |
|---|---|---|---|
| [Claude Code — web container](../../../map/grants/anthropic/claude-code-remote/ccr-container/index.md) | ◐ setting | observed | shell (Bash), harness (MCP and built-in tools) |
| [Claude Code — local · confirm off](../../../map/grants/anthropic/claude-code/local-confirmations-off/index.md) | ◉ expectation | derived | shell (Bash) |
| [Claude Code — local · confirm on](../../../map/grants/anthropic/claude-code/local-default/index.md) | ◉ expectation | derived | shell (Bash) |
| [Claude.ai — connectors on](../../../map/grants/anthropic/claude-web/connectors-on/index.md) | ○ boundary | derived | connectors |

## What narrows it

**The setting:** a branch protection rule at the host — the agent cannot edit it — and a pre-push hook in the clone for the earlier, cheaper refusal

**What it costs:** minutes; and a review step before anything deploys

**Tier after:** boundary (host rule) · setting (hook)

## Questions that ask about it

- *Does it push commits to a code host?* — eliciting, reliability 0.7

## In the mandates

- **wanted** by [A coding assistant in a container on the web](../../../map/mandates/coding-assistant-in-a-container/index.md)
- **wanted** by [A CI job on a hosted runner](../../../map/mandates/ci-job/index.md)
- **not wanted** by [Chat, with connectors switched on](../../../map/mandates/chat-with-connectors/index.md)
- **not wanted** by [Chat in the browser, nothing connected](../../../map/mandates/chat-no-connectors/index.md)

[Edit the primitives](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/primitives.json) · [edit the reductions](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/reductions.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/capabilities/write.repository.tenant/index.html)*
