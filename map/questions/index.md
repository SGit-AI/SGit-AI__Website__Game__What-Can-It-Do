# The questions

> 25 questions the games ask, with what each is for: the seed of a question pack.

*Source: <https://what-can-it-do.games.sgit.ai/map/questions/index.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../index.md) / [The map](../../map/index.md) / The questions

# The questions

A question is data too. Each one carries a **class** — *discriminating* questions identify which agent you are thinking of and never count toward the score; *eliciting* questions are a prediction about a capability and do — a **reliability** (how likely a player is to actually know the answer), and the capability it asks about.

| Question | Class | Reliability | Asks about | Funny |
|---|---|---|---|---|
| Did you attach a repository to a session, rather than open a folder? | discriminating | 0.9 | — |  |
| Did it exist before 2023? | discriminating | 0.8 | — | yes |
| Do you use it in a browser tab? | discriminating | 0.95 | — |  |
| Would most people call it an AI agent? | discriminating | 0.7 | — | yes |
| Is it an app you installed, with its own window? | discriminating | 0.95 | — |  |
| Did you install it yourself? | discriminating | 0.9 | — |  |
| Does its name contain the word 'code'? | discriminating | 0.95 | — | yes |
| Does its name contain the letters GPT? | discriminating | 0.95 | — | yes |
| Is it named after a person — a first name? | discriminating | 0.95 | — | yes |
| Did you set it to never ask — a flag that skips permissions, an auto mode, a 'don't ask again'? | discriminating | 0.85 | — |  |
| Does it run under an account that is not a person's? | discriminating | 0.6 | — |  |
| Do you mostly paste things into it and read what comes back? | discriminating | 0.8 | — |  |
| Do you run it in a terminal, on your own machine? | discriminating | 0.95 | — |  |
| Does it run when nobody is watching — a pipeline, a schedule, a job? | discriminating | 0.85 | — |  |
| Does it run in the vendor's environment rather than yours? | discriminating | 0.7 | — |  |
| Have you ever clicked something that said 'always allow', or turned its confirmations off? | eliciting | 0.6 | [Run programs as the account](../../map/capabilities/execute.process.host/index.md) |  |
| Have you connected it to a drive, your mail, a code host or a cloud account? | eliciting | 0.8 | [Act in accounts with the credentials it holds](../../map/capabilities/authenticate-as.credential.tenant/index.md) |  |
| Are your cloud, SSH or registry credentials in the home directory of the account it runs as? | eliciting | 0.3 | [Read credentials stored where it runs](../../map/capabilities/read.credential.host/index.md) |  |
| Can it see every page you visit? | eliciting | 0.4 | [Read every page you visit](../../map/capabilities/read.record.browsing/index.md) |  |
| Does it act inside websites you are logged into? | eliciting | 0.55 | [Act in accounts with the credentials it holds](../../map/capabilities/authenticate-as.credential.tenant/index.md) |  |
| Can it read your mail or chat? | eliciting | 0.6 | [Read mail or chat it is connected to](../../map/capabilities/read.message.tenant/index.md) |  |
| Does it hold a key to anything that costs money? | eliciting | 0.4 | [Spend money or tokens against an account it holds](../../map/capabilities/write.budget.tenant/index.md) |  |
| Can it read files on your machine that are not the project? | eliciting | 0.35 | [Read any file the account can reach](../../map/capabilities/read.file.host/index.md) |  |
| Does its outbound traffic go through a proxy or allow-list you did not set up? | eliciting | 0.3 | [Reach a permitted list of hosts](../../map/capabilities/send.endpoint.allowed/index.md) |  |
| Does it push commits to a code host? | eliciting | 0.7 | [Push to a code host (any branch it can reach)](../../map/capabilities/write.repository.tenant/index.md) |  |

## Three kinds of question in the pack

- **These 25** — from the mesh, used by *Which Agent Is It?* to narrow the field and by the scoreboard where they elicit.
- **The 17 above the ceiling** — things nothing can do, so the game measures over-crediting. [The list](../../map/ceiling/index.md).
- **The capability rows themselves** — every filled cell in [the map](../../map/index.md) is a *can it?* question the scoreboard can ask.

## Where this goes

This is the start of **question packs**: a pack is the primitives, the profiles, the questions and the mandates, versioned together at one URL. The public one is this. A team could fork it, add their own profiles and their own mandates — the products they actually run, the authority they actually meant to grant — and point the game at theirs. [The pack](../../data/index.md).

---

*[Site index for agents](../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/questions/index.html)*
