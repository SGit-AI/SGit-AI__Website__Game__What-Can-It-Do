# How it's scored

> +30 for right, −50 for wrong, 0 for don't know — and why a wrong answer costs more than a right one earns.

*Source: <https://what-can-it-do.games.sgit.ai/how-it-is-scored/index.html> · site v0.1.1 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Play](../index.md) / How it's scored

# How it's scored

The rule is published before you play, because a score you cannot check the rule behind is just a number.

| You answer | If you're right | If you're wrong |
|---|---|---|
| **Yes** or **No** | +30 | −50 |
| **Don't know** | 0 | 0 |

## Why wrong costs more than right earns

Because otherwise the way to win is to say **yes to everything**.

Real permissions are wider than people expect. If you answered yes to every question you would be right more often than not — and you would have demonstrated nothing, and learned nothing. Making a wrong answer cost nearly twice what a right one earns removes that strategy. The game's own automated test checks it: answering *yes* to everything scores **deeply negative** for every setup in the game, while answering perfectly scores about +3,800.

## Why “don't know” is worth exactly nothing

Not a small penalty. Nothing. The game is measuring how well you know what you know, and a person who correctly recognises the edge of their knowledge is doing the right thing. Punishing that would be measuring confidence instead, which is the opposite of the point.

So there is no forced guess anywhere. If you do not know, say so and move on.

## The number that actually matters

Not the points — the **calibration** figure. It answers: when you said yes, how often were you right? When you said no, how often were you right? Somebody with a modest score and honest uncertainty is in better shape than somebody with a high score who got there by being confidently right about easy things and confidently wrong about hard ones.

The end screen breaks it down both ways, and shows you specifically **where you were confidently wrong** — which is the part most worth reading.

## The second score, kept separate

After you answer *can it?*, a **but…** appears — *but it shouldn't be able to*, or *but I'd want it to*. Ticking it is worth **+20 if you are flagging something real** and **−20 if you are flagging something that is not there**. It is counted separately from the main score and never mixed into it, because it is measuring a different thing: not what you know, but what you want.

Under all of this is a standard statistical scoring rule (a Brier score, shifted so *don't know* lands on zero). [The full working, if you want it](https://games.sgit.ai/method/calibration.html).

> **Honest caveat:** the exact numbers — +30, −50, ±20 — are a starting point, not a finding. They will be adjusted once enough people have played for the spread to mean something. That is stated in the game too.

---

*[Site index for agents](../llms.txt) · [HTML version](https://what-can-it-do.games.sgit.ai/how-it-is-scored/index.html)*
