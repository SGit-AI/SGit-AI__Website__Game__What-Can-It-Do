# Do you know what your AI agent can actually do?

> A five-minute game. Name the AI assistant you use, and answer forty questions about what it can do — and whether you wanted it to. You score for how well you know what you know. Free, no sign-up.

*Source: <https://what-can-it-do.games.sgit.ai/index.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

# Do you know what your AI agent can actually do?

You have given an AI assistant access to something — your laptop, a repository, a mailbox, a cloud account. This is a five-minute game about whether you can predict what it can do with that. Most people cannot, in both directions.

*[A live vault surface here in the HTML page — the game running out of vault `pg87npy3`. In this markdown twin, [open it in the vault UI](https://dev.vault.sgraph.ai/#cf04d8a9bac6185dcb71e9c6f19ae13238b6434780324b1873504f2d6f7b505f%3Apg87npy3).]*

## What actually happens

1. **You say what you use.** Claude, ChatGPT, Copilot, Cursor, GitHub Actions, something else — then where you run it and roughly how it is set up. Up to four taps, or press *Just play* and start immediately.
2. **The board asks about one capability at a time.** *Can it do this?* — yes, no, or don't know. Then: *do you want it to?*
3. **You get told straight away**, with the reason, and you can ask why.
4. **At the end**: your score, how well-calibrated you were, and — the interesting bit — the list of things it can do that you did not want it to.

## Three things worth knowing before you play

**“Don't know” is free** — It scores zero, always. A wrong answer costs more than a right one earns (−50 against +30), so guessing confidently is the losing strategy. Saying you are not sure costs you nothing at all.
[The scoring rule, in full](how-it-is-scored/index.md)

**Some questions are impossible** — Roughly two in five are things **no** AI agent can do, anywhere, however it is configured. They are in there on purpose. If they were not, the game could only catch you underestimating.
[Why](the-ceiling/index.md)

**It is not an audit of your setup** — The board answers from what the vendor publishes about the product, not from your machine. It never looks at your computer, your account or your files — it cannot, it is a web page.
[What it can and can't tell you](about/index.md)

Every question the game asks is one cell in [**the map**](map/index.md) — 23 capabilities against 9 products, with what stands in the way and how sure anyone is. It is generated from data you can change with a pull request.

## What you walk away with

A calibration figure — how often you were right when you said you were sure — and **a draft of what you actually wanted your agent to be allowed to do**, assembled from your answers to the second question. Most people have never written that down. You will not have set out to write it either.

Then the gap between the two: the things it can do that you did not want, split by whether you saw them coming. And one thing to change.

**That list is not the end of it.** You cannot un-decide those permissions — the agent already has them — so the only real question is how long you are prepared to live with each one, and who says so. [What to do next](what-next/index.md) is three things you can do this afternoon, and where this goes when it is somebody's job: [RiskMandate](https://riskmandate.ai), the business risk layer this game is part of.

## Free, no sign-up, nothing stored

No account. No email. Nothing is saved between visits — close the tab and the run is gone. The game runs entirely in your browser: the scoring is arithmetic, there is no model deciding whether you were right. The only thing that leaves your browser is the anonymous counting described above, and you can switch it off.

Send it to someone: **`what-can-it-do.games.sgit.ai`**

> This game counts usage anonymously — which screens people reach, which answers are common. No cookies, no analytics script, nothing that identifies you or your machine, and a pause switch on every screen. [What is sent](what-we-learn/index.md).

---

*[Site index for agents](llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/index.html)*
