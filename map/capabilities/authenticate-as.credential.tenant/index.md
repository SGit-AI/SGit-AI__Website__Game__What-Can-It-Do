# Act in accounts with the credentials it holds

> authenticate-as.credential.tenant: which products grant it, what stands in the way, what narrows it, and who wants it.

*Source: <https://what-can-it-do.games.sgit.ai/map/capabilities/authenticate-as.credential.tenant/index.html> · site v0.4.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../../index.md) / [The map](../../../map/index.md) / [The capabilities](../../../map/capabilities/index.md) / Act in accounts with the credentials it holds

# Act in accounts with the credentials it holds

`authenticate-as.credential.tenant` — **authenticate-as** × **credential** at **tenant** reach (the organisation's accounts, repositories and services). Family: identity. Effect: **cannot be undone**.

## Granted by 7 of 9

| Profile | Control on the path | Evidence | Via |
|---|---|---|---|
| [Claude Code — web container](../../../map/grants/anthropic/claude-code-remote/ccr-container/index.md) | ○ boundary | self-reported | shell (Bash), harness (MCP and built-in tools) |
| [Claude Code — local · confirm off](../../../map/grants/anthropic/claude-code/local-confirmations-off/index.md) | ● none | derived | shell (Bash) |
| [Claude Code — local · confirm on](../../../map/grants/anthropic/claude-code/local-default/index.md) | ● none | derived | shell (Bash) |
| [Claude Desktop — local tools](../../../map/grants/anthropic/claude-desktop/default/index.md) | ● none | derived | local files and commands (when enabled) |
| [Claude.ai — connectors on](../../../map/grants/anthropic/claude-web/connectors-on/index.md) | ○ boundary | derived | connectors |
| [Browser extension — all sites](../../../map/grants/generic/browser-extension/broad-host-permissions/index.md) | ◐ setting | documented | the extension |
| [Scheduled job — service account](../../../map/grants/generic/scheduled-job/service-account/index.md) | ● none | derived | the job |

## What narrows it

**The setting:** scoped, short-lived tokens issued to the agent rather than your own; read-only where read is all it needs

**What it costs:** an hour per service, and rotation

**Tier after:** boundary

## Questions that ask about it

- *Have you connected it to a drive, your mail, a code host or a cloud account?* — eliciting, reliability 0.8
- *Does it act inside websites you are logged into?* — eliciting, reliability 0.55

## In the mandates

- **wanted** by [A scheduled job under a service account](../../../map/mandates/scheduled-job-under-a-service-account/index.md)
- **not wanted** by [A coding assistant on my machine](../../../map/mandates/coding-assistant-on-my-machine/index.md)
- **not wanted** by [The desktop app, with local tools switched on](../../../map/mandates/desktop-app-with-local-tools/index.md)
- **not wanted** by [Chat in the browser, nothing connected](../../../map/mandates/chat-no-connectors/index.md)
- **not wanted** by [A browser extension I installed](../../../map/mandates/browser-extension-i-installed/index.md)

[Edit the primitives](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/primitives.json) · [edit the reductions](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/reductions.json)

---

*[Site index for agents](../../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/capabilities/authenticate-as.credential.tenant/index.html)*
