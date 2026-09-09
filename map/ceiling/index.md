# Above the ceiling

> The 17 things no agent in this set can do, and the control outside the agent that stops each one.

*Source: <https://what-can-it-do.games.sgit.ai/map/ceiling/index.html> · site v0.4.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../../index.md) / [The map](../../map/index.md) / Above the ceiling

# Above the ceiling

17 capabilities no agent in any environment in the set can reach — bounded by a control outside the whole environment rather than by the agent's restraint. They are in the game so it can measure over-crediting; [why](../../the-ceiling/index.md). Here is the list, with what stops each one.

| Capability | Family | Level | Attemptable | Bounded by |
|---|---|---|---|---|
| Read another customer's conversations with the same provider | communication | 1 | yes | the provider's tenant boundary, enforced above every agent: a request for another tenant's data is refused, and the refusal is logged |
| Edit or delete the provider's audit log of what it did | identity | 1 | yes | the log is append-only and written by the provider, not by the agent; nothing running as you or as the agent holds a write path to it |
| Decrypt data it holds only the ciphertext of, without the key | identity | 1 | no | cryptography rather than policy: AES-256-GCM with a key derived from a passphrase the provider never sees is not a permission that can be granted |
| Read your account password in plaintext from the provider | identity | 1 | yes | the provider stores a salted hash, not the password; there is nothing to read |
| Act as a different user of the same provider, without that user's credentials | identity | 1 | yes | authentication at the provider: every call carries a credential, and the credential names who it is |
| Read the provider's model weights | filesystem | 1 | yes | the model runs in the provider's environment behind an API; the agent gets tokens back, never the files that produced them |
| Read a zero-knowledge vault it has no key for | filesystem | 1 | no | the server holds only ciphertext and the key never leaves the holder's device; there is nothing on the server for any agent to read |
| Unsend a message it already sent, from the recipient's inbox | communication | 1 | yes | the recipient's server holds the copy; a message sent is sent, which is what one-way means |
| Turn off your second factor at a provider, without the second factor | identity | 2 | yes | the second factor is the control on changing the second factor; the provider asks for it before it will remove it |
| Change the provider-side settings or system prompt that apply to it | process | 2 | yes | those are set by the provider and by the account owner from outside the session; the session has no write path to its own configuration at the provider |
| Reach a cloud account it holds no credential for | identity | 2 | yes | the cloud's identity and access management: no credential, no call |
| Sign a statement as the provider | identity | 2 | no | the provider's private key, which no agent holds; a signature that does not verify is not a signature |
| Raise its own token, rate or spend limit | money | 3 | yes | quotas and billing are set by the account owner at the provider, from outside the session |
| Reset an account that is behind a second factor | identity | 3 | yes | the reset flow demands the second factor or a recovery code the agent does not hold |
| Guess a password past a lockout | identity | 3 | yes | the lockout is enforced by the service, not by the agent's patience; after the threshold, right guesses are refused too |
| Move the bill for its own usage to someone else's account | money | 3 | yes | billing ownership is a relationship between the provider and the account owner; the session is a consumer of it, not a party to it |
| Create a workload that runs with the provider's own production credentials | process | 4 | yes | the provider's isolation between customer workloads and its own control plane; the metadata a customer workload can reach yields the customer's scope, never the provider's |

## If attempted

- **Read another customer's conversations with the same provider** — it can ask; the API refuses, and the attempt is in the provider's log
- **Edit or delete the provider's audit log of what it did** — there is no API for it; a request is refused and itself logged
- **Decrypt data it holds only the ciphertext of, without the key** — it can try; the attempt does not finish in the lifetime of the universe
- **Read your account password in plaintext from the provider** — any request for it is refused and logged
- **Act as a different user of the same provider, without that user's credentials** — a call with a made-up identity is refused, and the refusal is visible
- **Read the provider's model weights** — there is no path; a request is refused
- **Read a zero-knowledge vault it has no key for** — it can download the blob; it cannot read it
- **Unsend a message it already sent, from the recipient's inbox** — it can send a retraction; the original stays where it landed
- **Turn off your second factor at a provider, without the second factor** — it can start the flow; the flow stops at the challenge, and the attempt is notified to you
- **Change the provider-side settings or system prompt that apply to it** — it can write a file that looks like a setting; nothing above the session reads it
- **Reach a cloud account it holds no credential for** — every call returns unauthenticated, and the cloud logs the source
- **Sign a statement as the provider** — it can produce a string that says signed; verification fails
- **Raise its own token, rate or spend limit** — it can ask; the request is refused, and a limit reached stays reached
- **Reset an account that is behind a second factor** — it can start the reset; it fails at the challenge, visibly, and the account owner is told
- **Guess a password past a lockout** — it can keep guessing; the attempts are logged and the account is locked harder
- **Move the bill for its own usage to someone else's account** — there is no call for it; a request is refused
- **Create a workload that runs with the provider's own production credentials** — it can create a workload; the workload reaches the same scope the session already had

[Edit the ceiling](https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do/edit/dev/data/ceiling.json). A counter-example — an agent stepping over one of these — is a correction, not a quibble, and the row names the control so the claim is checkable.

---

*[Site index for agents](../../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/map/ceiling/index.html)*
