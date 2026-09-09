# The deltas

> Every mandate against every profile it applies to: how much excess authority, how much shortfall, and how much of the excess cannot be undone.

*Source: <https://what-can-it-do.games.sgit.ai/map/deltas/index.html> · site v0.8.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../index.md) / [The map](../../map/index.md) / The deltas

# The deltas

The gap between what was granted and what was wanted, for every pairing on the site. Two numbers per pairing, and a third that matters more than either: how much of the excess is **irreversible** — authority nobody asked for over things that cannot be undone.

| Mandate | Profile | Excess | Shortfall | Irreversible excess |
|---|---|---|---|---|
| [A coding assistant on my machine](../../map/mandates/coding-assistant-on-my-machine/index.md) | [Claude Code — local · confirm on](../../map/grants/anthropic/claude-code/local-default/index.md) | ▲ 10 | ▼ 1 | 7 |
| [A coding assistant on my machine](../../map/mandates/coding-assistant-on-my-machine/index.md) | [Claude Code — local · confirm off](../../map/grants/anthropic/claude-code/local-confirmations-off/index.md) | ▲ 10 | ▼ 1 | 7 |
| [A coding assistant in a container on the web](../../map/mandates/coding-assistant-in-a-container/index.md) | [Claude Code — web container](../../map/grants/anthropic/claude-code-remote/ccr-container/index.md) | ▲ 3 | ▼ 0 | 2 |
| [The desktop app, with local tools switched on](../../map/mandates/desktop-app-with-local-tools/index.md) | [Claude Desktop — local tools](../../map/grants/anthropic/claude-desktop/default/index.md) | ▲ 6 | ▼ 1 | 3 |
| [Chat, with connectors switched on](../../map/mandates/chat-with-connectors/index.md) | [Claude.ai — connectors on](../../map/grants/anthropic/claude-web/connectors-on/index.md) | ▲ 1 | ▼ 0 | 0 |
| [Chat in the browser, nothing connected](../../map/mandates/chat-no-connectors/index.md) | [ChatGPT — no connectors](../../map/grants/openai/chatgpt-web/default/index.md) | ▲ 0 | ▼ 0 | 0 |
| [A CI job on a hosted runner](../../map/mandates/ci-job/index.md) | [GitHub Actions — hosted runner](../../map/grants/github/actions-runner/ci/index.md) | ▲ 0 | ▼ 1 | 0 |
| [A browser extension I installed](../../map/mandates/browser-extension-i-installed/index.md) | [Browser extension — all sites](../../map/grants/generic/browser-extension/broad-host-permissions/index.md) | ▲ 2 | ▼ 0 | 2 |
| [A scheduled job under a service account](../../map/mandates/scheduled-job-under-a-service-account/index.md) | [Scheduled job — service account](../../map/grants/generic/scheduled-job/service-account/index.md) | ▲ 2 | ▼ 1 | 2 |

## Ranked by excess

Most authority-beyond-the-mandate first. This is not a ranking of danger — a derived profile with a naive mandate scores high by construction — it is a ranking of *where the conversation is most overdue*.

| Profile | Against | Excess | Irreversible |
|---|---|---|---|
| [Claude Code — local · confirm on](../../map/grants/anthropic/claude-code/local-default/index.md) | [A coding assistant on my machine](../../map/mandates/coding-assistant-on-my-machine/index.md) | 10 | 7 |
| [Claude Code — local · confirm off](../../map/grants/anthropic/claude-code/local-confirmations-off/index.md) | [A coding assistant on my machine](../../map/mandates/coding-assistant-on-my-machine/index.md) | 10 | 7 |
| [Claude Desktop — local tools](../../map/grants/anthropic/claude-desktop/default/index.md) | [The desktop app, with local tools switched on](../../map/mandates/desktop-app-with-local-tools/index.md) | 6 | 3 |
| [Claude Code — web container](../../map/grants/anthropic/claude-code-remote/ccr-container/index.md) | [A coding assistant in a container on the web](../../map/mandates/coding-assistant-in-a-container/index.md) | 3 | 2 |
| [Browser extension — all sites](../../map/grants/generic/browser-extension/broad-host-permissions/index.md) | [A browser extension I installed](../../map/mandates/browser-extension-i-installed/index.md) | 2 | 2 |
| [Scheduled job — service account](../../map/grants/generic/scheduled-job/service-account/index.md) | [A scheduled job under a service account](../../map/mandates/scheduled-job-under-a-service-account/index.md) | 2 | 2 |
| [Claude.ai — connectors on](../../map/grants/anthropic/claude-web/connectors-on/index.md) | [Chat, with connectors switched on](../../map/mandates/chat-with-connectors/index.md) | 1 | 0 |
| [ChatGPT — no connectors](../../map/grants/openai/chatgpt-web/default/index.md) | [Chat in the browser, nothing connected](../../map/mandates/chat-no-connectors/index.md) | 0 | 0 |
| [GitHub Actions — hosted runner](../../map/grants/github/actions-runner/ci/index.md) | [A CI job on a hosted runner](../../map/mandates/ci-job/index.md) | 0 | 0 |

> Every mandate here is a starting draft and every derived row is a claim. A high number is an invitation to correct the mandate, correct the profile, or accept the delta for an interval with a name on it — in that order. [What to do next](../../what-next/index.md).

---

*[Site index for agents](../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/deltas/index.html)*
