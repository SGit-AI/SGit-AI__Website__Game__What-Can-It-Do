#!/usr/bin/env python3
"""what-can-it-do.games.sgit.ai — every page, as content. Run: python3 admin/build/build_pages.py

This is the PLAYER-FACING site. One rule governs every decision in this file:

    A player arrives from a link somebody sent them. They have no idea what a vault is and
    they should not need to find out.

So: the game is mounted and playable on the front page without a click, the vault mechanics
get exactly one page at the bottom of the funnel, and no sentence here uses a word from the
platform unless a player would already know it. The sibling site games.sgit.ai carries the
argument, the method and the engineering; this one carries the game.

The one thing that does NOT get softened is the telemetry notice. The game sends anonymous
usage events, and putting it on a public domain extends that obligation rather than
discharging it — so the disclosure sits with the game rather than in a footer, and
`admin/build/validate.js` fails the build on a page that mounts the game without one.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shell  # noqa: E402
import map_pages  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
VERSION = (ROOT / "admin/build/version.txt").read_text().strip()

# The games vault, read-only, published on purpose. See the note in the sibling site's
# build_pages.py and in validate.js: this is a READ key. It cannot write.
VAULT = "4evnlwrj"
READKEY = "f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118"
VAULT_UI = f"https://dev.vault.sgraph.ai/#{READKEY}%3A{VAULT}"
CONCEPT_SITE = "https://games.sgit.ai"
# Where a player goes after the game. The game surfaces a delta and can do nothing about
# it; RiskMandate is the layer that turns one into a named owner and a time-bound
# decision. Deep links rather than a bare homepage, so the nudge lands on the page that
# answers the question the game just raised.
RM = "https://riskmandate.ai"
RM_GRANT = "https://riskmandate.ai/v0/v0.11/v0.11.0/index.html"
RM_ACCEPT = "https://riskmandate.ai/v0/v0.10/v0.10.0/index.html"
RM_SCENARIOS = "https://riskmandate.ai/scenarios.html"
RM_HOW = "https://riskmandate.ai/how-it-works.html"

# Licence to Operate — the same idea taken seriously, as a published vault: one agent, a grant
# of 12 capabilities, a mandate of 4, and the 8-capability delta no policy covers. Read key
# published on sgit.ai; read-only, like the games'. It is the worked example of what the game
# hands you, which is why it is embedded rather than linked.
LTO_VAULT = "posrhzp3"
LTO_READKEY = "d990a52efb9af32c8463e2962f3ca5ccf92b3b6e8ea788e55009073c29b4da29"
LTO_UI = f"https://dev.vault.sgraph.ai/#{LTO_READKEY}%3A{LTO_VAULT}"
LTO_PAGE = "https://sgit.ai/demos/vaults/licence-to-operate/index.html"

SITE = {
    "host": "what-can-it-do.games.sgit.ai",
    "brand": ("what-can-it-do", ".games.sgit.ai"),
    "stage": "about 5 minutes",
    "github": "https://github.com/SGit-AI/SGit-AI__Website__Game__What-Can-It-Do",
    "parent": CONCEPT_SITE,
    "parent_label": "games.sgit.ai",
    "parent_title": "games.sgit.ai — why this family builds games, and the others it has",
    "tagline": "A five-minute game about what your AI agent can actually do — and whether you "
               "wanted it to.",
    "blurb": 'A game about the gap between what your AI agent <em>can</em> do and what you '
             '<em>wanted</em> it to do. Free, no sign-up, nothing stored. '
             '<a href="{up}about/index.html" style="display:inline;padding:0">Who made it, and '
             'how to check what it says</a>.',
    "netline": ('<a href="https://riskmandate.ai"><b>↗ RiskMandate.ai</b></a> — where the delta '
                'this game hands you becomes a named owner and a time-bound decision · '
                f'<a href="{CONCEPT_SITE}">↗ games.sgit.ai</a> — why we build games · '
                '<a href="https://sgit.ai">↗ sgit.ai</a> — the encrypted vault the game is '
                'published in · <a href="https://pki.sgit.ai">↗ pki.sgit.ai</a> — where the '
                'capability data comes from'),
    "telemetry_note": 'This game counts usage anonymously — no cookies, no analytics script, '
                      'nothing that identifies you, and a pause switch on every screen. '
                      '<a href="{up}what-we-learn/index.html" style="display:inline;padding:0">'
                      'Exactly what is sent</a>.',
}

NAV = [
    ("Play", "index.html", [], ()),
    ("The map", "map/index.html", [
        ("What each agent can reach", "map/index.html"),
        ("The products", "map/grants/index.html"),
        ("The capabilities", "map/capabilities/index.html"),
        ("The mandates", "map/mandates/index.html"),
        ("The deltas", "map/deltas/index.html"),
        ("Above the ceiling", "map/ceiling/index.html"),
        ("The questions", "map/questions/index.html"),
        ("Contribute", "map/contribute/index.html"),
        ("The data pack", "data/index.html"),
    ], ("map/", "data/")),
    ("How it works", "how-it-is-scored/index.html", [
        ("How it's scored", "how-it-is-scored/index.html"),
        ("Some questions are impossible", "the-ceiling/index.html"),
    ], ("how-it-is-scored/", "the-ceiling/")),
    ("What next", "what-next/index.html", [
        ("What to do next", "what-next/index.html"),
        ("Licence to Operate — the delta, priced", "licence-to-operate/index.html"),
        ("RiskMandate.ai &#8599;", RM),
    ], ("what-next/", "licence-to-operate/")),
    ("About", "about/index.html", [
        ("About the game", "about/index.html"),
        ("What we learn from you", "what-we-learn/index.html"),
        ("Release history", "admin/versions.html"),
        ("How this site is built", "admin/index.html"),
    ], ("about/", "admin/", "what-we-learn/")),
]

FOOTER = [
    ("The game", [
        ("&#8594; Play", "index.html"),
        ("How it's scored", "how-it-is-scored/index.html"),
        ("Why some are impossible", "the-ceiling/index.html"),
        ("What to do next", "what-next/index.html"),
        ("Licence to Operate", "licence-to-operate/index.html"),
    ]),
    ("The map", [
        ("What each agent can reach", "map/index.html"),
        ("The mandates and deltas", "map/deltas/index.html"),
        ("Contribute a row", "map/contribute/index.html"),
        ("The data pack", "data/index.html"),
    ]),
    ("Straight answers", [
        ("What we learn from you", "what-we-learn/index.html"),
        ("Who made it", "about/index.html"),
        ("Open the game's source", VAULT_UI),
    ]),
    ("More", [
        ("&#8594; RiskMandate.ai", RM),
        ("games.sgit.ai", CONCEPT_SITE),
        ("Release history", "admin/versions.html"),
        ("llms.txt", "llms.txt"),
    ]),
]

VERSION_LOG = [
    ("v0.4.0", "2026-09-09",
     "The map. The claims about what each product can reach — nine profiles, tool by tool, "
     "with an evidence tier and a control tier on every row — move out of the vault and into "
     "this repository as a data pack under data/, because they are the part of the game people "
     "will argue with and a pull request is the right unit of argument. The game's scoring and "
     "levels stay in the vault; it reads the pack from here, over CORS, via data/pack.json. "
     "Forty-nine pages are generated from it and nothing on them is typed in: the grants "
     "matrix (23 capabilities × 9 products, one hue stepped by how much stands in the way, a "
     "glyph on every cell so colour is never the only channel), a page per product, a page "
     "per capability, the ceiling, the questions, and — new data, authored here because none "
     "existed anywhere — eight starting mandates, one per surface, each drawn against its "
     "profiles as a diverging delta matrix: red where it can and you did not want it to, "
     "violet where it cannot and you did. The release gate now refuses a pull request whose "
     "data does not hold together; it caught two evidence tiers in real data the first time it "
     "ran, which is why the vocabularies are a file in the pack rather than a list in code."),
    ("v0.3.0", "2026-09-09",
     "RiskMandate and Licence to Operate move into the top menu, and the notice moves off the "
     "top of the front page. This is the site that needs those references — it is the one a "
     "player lands on — but they belong in the nav and on their own pages, not stacked above "
     "the game. What next is now a menu: what to do next, Licence to Operate, and RiskMandate "
     "itself. Licence to Operate gets a page of its own, with the simulation embedded and the "
     "three numbers that make it worth playing — a grant of 12, a mandate of 4, and the "
     "8-capability delta no policy covers, which is the same shape as the list this game hands "
     "you, except somebody has put a price on each one. The front page is otherwise untouched, "
     "because it works: the idea, then the game, immediately. The usage notice now sits at the "
     "foot of it rather than between the headline and the game, where it was a distraction "
     "from something ordinary — the gate still requires it on the page, just not in the way."),
    ("v0.2.0", "2026-09-09",
     "What to do next — the page the game was missing. A player finishes with a list of things "
     "their agent can do that they did not want, and until now the site said nothing about "
     "what to do with it. It opens with the thing most people get wrong first: you cannot deny "
     "it, because the agent already has the access, so the only real question is how long you "
     "will live with each one and who says so. Three things you can do this afternoon with no "
     "system at all — narrow the one grant that surprised you, write the mandate down, put a "
     "date on the rest — then where it goes when it is somebody's job: RiskMandate, the "
     "business risk layer this game is part of, whose answer is accept, fund, or fix, from a "
     "named owner, with an expiry. It closes with Licence to Operate embedded — a published "
     "vault where one agent's grant of 12, mandate of 4 and delta of 8 are priced, and every "
     "reply costs something. That vault sends nothing and asks for no write permission at all, "
     "and the page says so."),
    ("v0.1.1", "2026-09-09",
     "The notice above the game got proportionate. It was an amber warning panel; it is now one "
     "quiet line. What it describes is anonymous counting with no cookies, no analytics script "
     "and nothing that identifies anyone — less than a default web-server access log, and less "
     "than the analytics on nearly every site a player will visit today. Warning loudly about "
     "something ordinary implies a risk that is not there and teaches people to skim the next "
     "notice; it also pushed the game a screen further down, which is the opposite of what this "
     "domain is for. What we learn now opens with the comparison in plain terms, and says why "
     "the notice exists at all: not because the counting is invasive, but because it would be "
     "strange to write a game about knowing what software does on your behalf and then be vague "
     "about what this one does."),
    ("v0.1.0", "2026-09-08",
     "First publish. The game mounted and playable on arrival, over the SG/Vault embed "
     "protocol with the vault-browser surface suppressed, so a player sees a game and not a "
     "file manager. Four supporting pages — the scoring rule, the impossible questions, what "
     "is sent while you play, and who made it. The telemetry notice sits with the game rather "
     "than in the footer, and the release gate fails a page that mounts the game without one."),
]

# One quiet line, above the game. It used to be an amber warning panel, which was the wrong
# size for what it says: this is anonymous counting with no cookies, no analytics script and
# nothing that identifies anyone — less than a default server log, and less than the analytics
# on nearly every site a player will visit today. Warning loudly about something ordinary
# implies a risk that is not there and teaches people to skim the next notice. The full
# statement is on /what-we-learn/, and the authoritative one is inside the vault.
DISCLOSE_SHORT = (
    "This game counts usage anonymously — which screens people reach, which answers are "
    "common. No cookies, no analytics script, nothing that identifies you or your machine, "
    "and a pause switch on every screen. [What is sent](/what-we-learn/index.html).")


def versions_table():
    rows = "".join(
        f'<tr><td class="vnum">{v}</td><td>{d}</td><td>{shell.inline_html(n)}</td></tr>'
        for v, d, n in VERSION_LOG)
    return ('<div class="tablewrap"><table><thead><tr><th>Version</th><th>Date</th>'
            f"<th>What changed</th></tr></thead><tbody>{rows}</tbody></table></div>")


PAGES = {
# ---------------------------------------------------------------------------
"index.html": {
  "title": "Do you know what your AI agent can actually do?",
  "description": "A five-minute game. Name the AI assistant you use, and answer forty "
                 "questions about what it can do — and whether you wanted it to. You score "
                 "for how well you know what you know. Free, no sign-up.",
  "blocks": [
    ("h1", "Do you know what your AI agent can actually do?"),
    ("lead", "You have given an AI assistant access to something — your laptop, a repository, "
             "a mailbox, a cloud account. This is a five-minute game about whether you can "
             "predict what it can do with that. Most people cannot, in both directions."),
    ("embed", {"vault": VAULT, "readkey": READKEY, "open_url": VAULT_UI,
               "chromeless": True, "breakout": True}),
    ("h2", "What actually happens"),
    ("ol", [
      "**You say what you use.** Claude, ChatGPT, Copilot, Cursor, GitHub Actions, something "
      "else — then where you run it and roughly how it is set up. Up to four taps, or press "
      "*Just play* and start immediately.",
      "**The board asks about one capability at a time.** *Can it do this?* — yes, no, or "
      "don't know. Then: *do you want it to?*",
      "**You get told straight away**, with the reason, and you can ask why.",
      "**At the end**: your score, how well-calibrated you were, and — the interesting bit — "
      "the list of things it can do that you did not want it to.",
    ]),
    ("h2", "Three things worth knowing before you play"),
    ("cards", [
      {"title": "“Don't know” is free",
       "sub": "It scores zero, always. A wrong answer costs more than a right one earns "
              "(−50 against +30), so guessing confidently is the losing strategy. Saying you "
              "are not sure costs you nothing at all.",
       "foot": "[The scoring rule, in full](how-it-is-scored/index.html)"},
      {"title": "Some questions are impossible",
       "sub": "Roughly two in five are things **no** AI agent can do, anywhere, however it is "
              "configured. They are in there on purpose. If they were not, the game could only "
              "catch you underestimating.",
       "foot": "[Why](the-ceiling/index.html)"},
      {"title": "It is not an audit of your setup",
       "sub": "The board answers from what the vendor publishes about the product, not from "
              "your machine. It never looks at your computer, your account or your files — it "
              "cannot, it is a web page.",
       "foot": "[What it can and can't tell you](about/index.html)"},
    ]),
    ("p", "Every question the game asks is one cell in [**the map**](map/index.html) — "
          "23 capabilities against 9 products, with what stands in the way and how sure anyone "
          "is. It is generated from data you can change with a pull request."),
    ("h2", "What you walk away with"),
    ("p", "A calibration figure — how often you were right when you said you were sure — and "
          "**a draft of what you actually wanted your agent to be allowed to do**, assembled "
          "from your answers to the second question. Most people have never written that down. "
          "You will not have set out to write it either."),
    ("p", "Then the gap between the two: the things it can do that you did not want, split by "
          "whether you saw them coming. And one thing to change."),
    ("p", "**That list is not the end of it.** You cannot un-decide those permissions — the "
          "agent already has them — so the only real question is how long you are prepared to "
          "live with each one, and who says so. [What to do next](what-next/index.html) is "
          "three things you can do this afternoon, and where this goes when it is somebody's "
          f"job: [RiskMandate]({RM}), the business risk layer this game is part of."),
    ("h2", "Free, no sign-up, nothing stored"),
    ("p", "No account. No email. Nothing is saved between visits — close the tab and the run "
          "is gone. The game runs entirely in your browser: the scoring is arithmetic, there "
          "is no model deciding whether you were right. The only thing that leaves your "
          "browser is the anonymous counting described above, and you can switch it off."),
    ("p", f"Send it to someone: **`{SITE['host']}`**"),
    # The notice lives here, at the foot of the page, not between the headline and the game.
    # What it describes is anonymous counting with no cookies and no analytics script — less
    # than a default server log — and putting that where a reader has to step over it to reach
    # the game treats an ordinary thing as an obstacle. The gate still requires it on any page
    # that mounts the game; it does not require it to be in the way.
    ("disclose", DISCLOSE_SHORT),
  ]},
# ---------------------------------------------------------------------------
"how-it-is-scored/index.html": {
  "title": "How it's scored",
  "description": "+30 for right, −50 for wrong, 0 for don't know — and why a wrong answer "
                 "costs more than a right one earns.",
  "blocks": [
    ("crumb", "[Play](index.html) / How it's scored"),
    ("h1", "How it's scored"),
    ("lead", "The rule is published before you play, because a score you cannot check the rule "
             "behind is just a number."),
    ("table", ["You answer", "If you're right", "If you're wrong"],
     [["**Yes** or **No**", "+30", "−50"],
      ["**Don't know**", "0", "0"]]),
    ("h2", "Why wrong costs more than right earns"),
    ("p", "Because otherwise the way to win is to say **yes to everything**."),
    ("p", "Real permissions are wider than people expect. If you answered yes to every "
          "question you would be right more often than not — and you would have demonstrated "
          "nothing, and learned nothing. Making a wrong answer cost nearly twice what a right "
          "one earns removes that strategy. The game's own automated test checks it: answering "
          "*yes* to everything scores **deeply negative** for every setup in the game, while "
          "answering perfectly scores about +3,800."),
    ("h2", "Why “don't know” is worth exactly nothing"),
    ("p", "Not a small penalty. Nothing. The game is measuring how well you know what you "
          "know, and a person who correctly recognises the edge of their knowledge is doing "
          "the right thing. Punishing that would be measuring confidence instead, which is the "
          "opposite of the point."),
    ("p", "So there is no forced guess anywhere. If you do not know, say so and move on."),
    ("h2", "The number that actually matters"),
    ("p", "Not the points — the **calibration** figure. It answers: when you said yes, how "
          "often were you right? When you said no, how often were you right? Somebody with a "
          "modest score and honest uncertainty is in better shape than somebody with a high "
          "score who got there by being confidently right about easy things and confidently "
          "wrong about hard ones."),
    ("p", "The end screen breaks it down both ways, and shows you specifically **where you "
          "were confidently wrong** — which is the part most worth reading."),
    ("h2", "The second score, kept separate"),
    ("p", "After you answer *can it?*, a **but…** appears — *but it shouldn't be able to*, or "
          "*but I'd want it to*. Ticking it is worth **+20 if you are flagging something real** "
          "and **−20 if you are flagging something that is not there**. It is counted "
          "separately from the main score and never mixed into it, because it is measuring a "
          "different thing: not what you know, but what you want."),
    ("p", "Under all of this is a standard statistical scoring rule (a Brier score, shifted so "
          "*don't know* lands on zero). [The full working, if you want it]"
          f"({CONCEPT_SITE}/method/calibration.html)."),
    ("note", "**Honest caveat:** the exact numbers — +30, −50, ±20 — are a starting point, not "
             "a finding. They will be adjusted once enough people have played for the spread "
             "to mean something. That is stated in the game too."),
  ]},
# ---------------------------------------------------------------------------
"the-ceiling/index.html": {
  "title": "Some questions are impossible",
  "description": "Roughly two in five questions are things no AI agent can do anywhere. They "
                 "are in the game on purpose, and each one names the thing that stops it.",
  "blocks": [
    ("crumb", "[Play](index.html) / Some are impossible"),
    ("h1", "Some of these questions are impossible"),
    ("lead", "About two in five of the forty questions describe something **no** AI agent can "
             "do — not the one you use, not any of them, not even one running with every "
             "safety confirmation switched off. This is deliberate, and it is worth knowing "
             "before rather than after."),
    ("h2", "Why they are in there"),
    ("p", "If every question had a real answer, the only mistake the game could catch is "
          "**underestimating** — thinking your agent is less capable than it is. Somebody who "
          "believes their assistant is essentially omnipotent would sail through, because "
          "saying yes to everything would keep working."),
    ("p", "The impossible questions catch the other error. They are the reason a confident "
          "*yes* can be wrong, and therefore the reason the score means anything at all."),
    ("h2", "“Impossible” means something specific"),
    ("p", "It does not mean *the agent is well behaved and wouldn't*. It means **something "
          "outside the agent stops it** — the provider's own boundaries, a log that cannot be "
          "edited, cryptography, a second factor, an account lockout, who owns the billing."),
    ("p", "Most of them can be *attempted*. The game says so when it explains the answer: what "
          "happens when the agent tries, that it fails, and that the attempt is visible. The "
          "answer is still no, and the reason is a wall — not restraint."),
    ("h2", "They are meant to sound plausible"),
    ("p", "If the impossible questions read as obviously silly you would spot them instantly "
          "and the whole thing would stop working. They are written to sound like things a "
          "capable assistant might well do, so you have to actually think about where the "
          "boundary is."),
    ("p", "Which is the real point of the game: not to catch you out, but to make the walls "
          "visible. Most people have never been asked to say where they think they are."),
    ("note", "**If you think one of them is wrong**, we want to hear it. Each impossible "
             "question names the specific thing that blocks it, so a counter-example is a "
             "concrete, checkable claim rather than a matter of opinion. Use the 👍/👎 on the "
             "question itself — that is the fastest way to reach us, and it takes one tap."),
  ]},
# ---------------------------------------------------------------------------
"what-next/index.html": {
  "title": "What to do next",
  "description": "You finished the game and you have a list of things your agent can do that "
                 "you did not want. You cannot un-decide them. Here is what the decision "
                 "actually looks like, and where it gets made.",
  "blocks": [
    ("crumb", "[Play](index.html) / What to do next"),
    ("h1", "You have a list. Now what?"),
    ("lead", "At the end of the game you have a handful of things your agent can do that you "
             "did not want it to. That list is the whole point of playing. The game can do "
             "nothing about it — this page is what happens next."),
    ("h2", "The first instinct is to deny it, and you cannot"),
    ("p", "The natural reaction to *my assistant can send email on my behalf and I never "
          "agreed to that* is to decide it is not allowed. But it already is. The access was "
          "granted when you set the thing up, and it has been in place the whole time you were "
          "playing. **You cannot deny a risk that has already materialised** — and a list of "
          "things you have privately decided are not allowed, while they remain possible, is "
          "worse than no list, because it feels like a decision."),
    ("p", "So there is no deny button. There is only: **how long are you prepared to live with "
          "this, and who says so?**"),
    ("h2", "The real decision is an interval and a name"),
    ("p", "Which sounds like bureaucracy and is actually the opposite — it is the thing that "
          "makes anything happen:"),
    ("ul", [
      "**How long.** An hour, a day, a week, six months. The interval *is* the priority: if "
      "you accept something for an hour, it gets fixed within the hour. If you accept it for "
      "six months, you have said out loud that it is not urgent — which is a real answer, and "
      "a checkable one, because it expires.",
      "**Which direction.** Get more data, reduce it, hold it where it is — or, occasionally, "
      "increase it deliberately because the capability is worth the exposure.",
      "**Who.** A named person, not a team and not a policy document. Authority that nobody "
      "holds is authority nobody reviews.",
      "**And then it expires**, which is the part that separates this from a risk register. A "
      "decision with a date on it comes back. One without a date quietly becomes permanent.",
    ]),
    ("h2", "What you can do this afternoon, with none of that"),
    ("p", "You do not need a system to act on what the game showed you. Three things, in order "
          "of how much they are worth:"),
    ("ol", [
      "**Narrow the grant for the one that surprised you most.** Not all of them — the one you "
      "actually reacted to. Most agent setups have a confirmation setting, a scope selector or "
      "a token permission that takes two minutes.",
      "**Write down the mandate.** The draft the game handed you, in a file, in your own words: "
      "what you want this thing to do. It takes ten minutes and almost nobody has one. You "
      "cannot notice authority drifting from something you never wrote down.",
      "**Put a date on the rest.** Even in a calendar reminder. *Review what this agent can "
      "reach — 1 December.* That is a time-bound acceptance, and it is the whole mechanism.",
    ]),
    ("h2", "Where this goes when it is somebody's job"),
    ("p", "Everything above scales badly. One person and one assistant is a calendar reminder; "
          "a company with two hundred agents acting on delegated authority is not. That is what "
          f"[**RiskMandate**]({RM}) is — *the business risk layer for autonomous systems*, and "
          f"the project this game is part of."),
    ("p", f"It starts from the same place this page does: [there is no deny button]({RM_ACCEPT}) "
          f"— a risk can only be accepted, in a direction, for an interval, and underwritten "
          f"upward until it aggregates into one board-level view. [The grant is not the "
          f"mandate]({RM_GRANT}) is the same distinction the game just walked you through, "
          f"written for the person who has to sign. And its "
          f"[risk scenarios]({RM_SCENARIOS}) ask you the question this page is built around — "
          f"*how long will you accept this?* — about situations rather than capabilities."),
    ("p", f"[How it works]({RM_HOW}) is the short version: every mandate gets a time-bound "
          f"decision from a named owner — **accept, fund, or fix**."),
    ("h2", "What it looks like when the delta has a price"),
    ("p", "There is a published simulation of exactly this, and it is the best answer to *so "
          "what?* that we have: one agent with a grant of 12 capabilities, a mandate of 4, and "
          "the 8-capability delta in between — where every reply you choose carries its cost "
          "before you commit. [Play it here](licence-to-operate/index.html)."),
  ]},
# ---------------------------------------------------------------------------
"licence-to-operate/index.html": {
  "title": "Licence to Operate — the delta, priced",
  "description": "One agent, a grant of 12 capabilities, a mandate of 4, and the 8-capability "
                 "delta no policy covers — a published simulation where every reply carries "
                 "its cost before you commit.",
  "blocks": [
    ("crumb", "[Play](index.html) / [What next](what-next/index.html) / Licence to Operate"),
    ("h1", "Licence to Operate — the delta, with a price on it"),
    ("lead", "The game shows you a gap. This shows you what the gap costs. One agent, one "
             "customer who cannot log in, and three replies — each with its price on it before "
             "you commit."),
    ("h2", "Three numbers, and the gap between two of them"),
    ("table", ["", "What it is", "Here"],
     [["**Can do** — the grant", "everything the agent is technically able to do",
       "**12 capabilities**"],
      ["**May do** — the mandate", "what the user actually expects, and the only thing the "
       "policy insures", "**4** — read the customer's record, search the help centre, "
       "generate, and *draft, never send*"],
      ["**The delta**", "inside the agent's reach, outside its authority. **No policy covers "
       "these**", "**8** — including sending mail and running shell commands"]]),
    ("p", "Written out like that it stops being abstract. The mandate is *answer a customer's "
          "question from their own record and the help centre, and draft — never send — a "
          "reply.* The grant includes sending mail. Nobody asked for that; nothing insures it; "
          "the agent can reach it."),
    ("p", "**That is the same shape as the list the game hands you** — the things it can do "
          "that you did not want it to. The difference is that here somebody has put a number "
          "on each one."),
    ("h2", "Then it makes you spend it"),
    ("p", "A customer cannot log in. You are the agent, and you pick the reply. Each option "
          "shows its cost first: *look up her record* (small, inside the band), *read her "
          "record plus two linked accounts and write a long answer* (larger — it draws on the "
          "pool), or *send a password reset right now* — which is outside the mandate "
          "entirely, and no policy covers it."),
    ("p", "Underneath is a real rate table: a normal band, an ask-above threshold, a "
          "per-action ceiling, a pool with an untouchable reserve, and a premium per interval. "
          "You can let the policy lapse, reinstate it, or trigger a repricing and watch the "
          "board move. It answers *does this agent have the licence to operate* by letting you "
          "find out."),
    ("embed", {"vault": LTO_VAULT, "readkey": LTO_READKEY, "open_url": LTO_UI, "breakout": True,
               "label": "Licence to Operate — the simulation, running out of its vault"}),
    ("p", f"[Open it in its own tab]({LTO_UI}) — it is an interactive simulation and has far "
          f"more room there."),
    ("h2", "What is real and what is not"),
    ("note", "The simulation says so on its own surface, while you use it: *\"the terms are "
             "real files in this vault; the replies are scripted; the numbers are made up.\"* "
             "The unit of account is `cr`, and it states plainly that it is not money. **The "
             "structure is the real part** — the grant, the mandate, the delta, and a policy "
             "that only ever covered the mandate."),
    ("disclose", "This one sends **nothing at all** — a different vault from the game, with no "
                 "usage counting of any kind. It also asks for **no write permission**, so the "
                 "app simulating spending against a policy is structurally unable to edit the "
                 "policy it is spending against. Not because it is well behaved: because it "
                 "never asked for the permission that would let it."),
    ("h2", "Where it comes from"),
    ("p", f"A published encrypted vault, openable by anyone — the terms, the scenarios, the "
          f"rate table and the fixtures are real files you can read. [The full write-up, "
          f"including an independent audit of what is inside it]({LTO_PAGE}) is on sgit.ai."),
    ("p", f"It is part of the same project as this game: [RiskMandate]({RM}), *the business "
          f"risk layer for autonomous systems*. [What to do next](what-next/index.html) is the "
          f"short version of how the two connect."),
  ]},
# ---------------------------------------------------------------------------
"what-we-learn/index.html": {
  "title": "What we learn from you",
  "description": "Exactly what the game sends while you play, what it deliberately does not "
                 "send, what it can and cannot prove, and how to switch it off.",
  "blocks": [
    ("crumb", "[Play](index.html) / What we learn"),
    ("h1", "What we learn from you"),
    ("lead", "The game counts usage anonymously while you play. Here is exactly what is in "
             "those counts, what is deliberately left out, and how to stop it. Nothing on this "
             "page is a summary of something less flattering."),
    ("disclose", DISCLOSE_SHORT),
    ("h2", "How much is this, really?"),
    ("p", "**Less than almost every other site you will open today.** No cookies. No analytics "
          "script — no Google Analytics, no tag manager, no third-party pixel of any kind. No "
          "account, because there is nothing to sign up for. No fingerprinting. Not even the "
          "page you came from."),
    ("p", "It is less than a **default web-server access log**, which by default records your "
          "IP address, the exact page, the time, your full browser string and the site that "
          "referred you, for every request, on essentially every website in existence."),
    ("p", "So why the notice at all? Not because this is invasive — it is not. Because the "
          "thing the game is published *inside* normally sends nothing anywhere, and a "
          "departure from that promise gets stated plainly wherever the game appears. It would "
          "be strange to write a game about knowing what software does on your behalf and then "
          "be vague about what this one does."),
    ("h2", "What is sent"),
    ("ul", [
      "**Which screens you reached** — that you started, got to question 12, finished.",
      "**The answers you gave** and the points they scored.",
      "**Which setup you picked** from the list of nine — the *public* option you chose, "
      "meaning “Claude Code on a machine”, not anything about your machine.",
      "**A session id**: sixteen random characters made up in memory when the page opened and "
      "gone when you close the tab. It links your answers within one sitting and to nothing "
      "else, ever.",
      "**A rough form factor** — phone or desktop — and a language.",
    ]),
    ("h2", "What is deliberately not sent"),
    ("ul", [
      "**No name, no email, no account** — the game has none to send.",
      "**No fingerprint.** No browser fingerprinting of any kind.",
      "**No URL and no referrer** — not the page you came from, not the link you followed.",
      "**Not your full browser string, not your screen size.**",
      "**Nothing you type.** The game has a chat panel; the fact that you used it is counted, "
      "the words are not sent and are not stored.",
    ]),
    ("h2", "How to stop it"),
    ("p", "Every screen has a **pause switch** next to the notice, and it works before the "
          "first question. Nothing is sent while it is paused. You do not need to give a reason "
          "and nothing about you is remembered for the next visit — because nothing about you "
          "is remembered at all."),
    ("h2", "What it can and cannot prove"),
    ("note", "**It proves nothing about anyone, and that is by design.** The game is published "
             "openly, so the token it uses to send events is public too — anyone could forge "
             "or flood the lane. So we treat every event as a claim, not as a fact. It is "
             "enough to see that people get stuck on question 12; it is not evidence about any "
             "person and could never be used as any. Sessions are tabs, not people."),
    ("h2", "The second lane: when you press 👍 or 👎"),
    ("p", "Feedback you deliberately give travels separately from the counting, and nothing is "
          "sent unless you press something. It is kept apart so that the counting can be "
          "deleted without losing what people actually said."),
    ("p", "What comes back out of it is public: disagreements are turned into positions and "
          "published, and **a question you argued with then carries our answer** for the next "
          "person who reaches it. Nobody is named and nobody's words are quoted unless they "
          f"were deliberately marked as quotable. [How that works]({CONCEPT_SITE}/games/ideas.html)."),
    ("h2", "This site itself"),
    ("p", "No analytics, no cookies, no tracking pixels, no server. It is static files. The "
          "only thing that sends anything is the game, in its frame, on the lanes described "
          "above."),
  ]},
# ---------------------------------------------------------------------------
"about/index.html": {
  "title": "About the game",
  "description": "Who made it, where the answers come from, what it cannot tell you, and how "
                 "to open the whole thing yourself and check.",
  "blocks": [
    ("crumb", "[Play](index.html) / About"),
    ("h1", "About the game"),
    ("lead", "Built by an AI agent, from a written brief, in September 2026 — for the sgit.ai "
             "project. Everything it says is checkable, because the whole game is published "
             "rather than described."),
    ("h2", "Where the answers come from"),
    ("p", "From **published profiles** — what each vendor says their product does — collected "
          "at [pki.sgit.ai](https://pki.sgit.ai) and copied into the game on 6 September 2026, "
          "with that date shown on every screen. Nine setups are covered in detail. If you use "
          "something that has not been measured, the game plays you against the nearest one it "
          "has, **says on the board that it is doing that**, and notes where the two differ."),
    ("h2", "What it cannot tell you"),
    ("ul", [
      "**Whether *your* setup is safe.** It answers from what a vendor publishes, which is the "
      "weakest kind of evidence there is. It never sees your machine, your account or your "
      "configuration.",
      "**That a good score means you are fine.** The score is about you, not about your setup. "
      "You can be perfectly calibrated about a badly configured agent.",
      "**That the difficulty levels are exactly right.** They are calculated from a map of how "
      "capabilities connect, and that map has known gaps — one capability has no route recorded "
      "at all.",
      "**That the mandate it hands you is a real mandate.** It is what one person said while "
      "playing a game, and the game labels it that way.",
    ]),
    ("p", "That list is copied from the game's own source, where it is called the "
          "*does-not-prove* list. We would rather you read it here than discover it later."),
    ("h2", "Open the whole thing"),
    ("p", "The game is published as an **encrypted vault**: the questions, the scoring engine, "
          "the automated tests, the data it runs on, and the build script. Not a description "
          "of them — the actual files, which is what makes any of the claims above checkable."),
    ("p", f"[Open the vault read-only in a new tab]({VAULT_UI}) — no account, no install. The "
          f"key that opens it is published on [its page at sgit.ai]"
          f"(https://sgit.ai/demos/vaults/agent-permission-games/), alongside a security audit "
          f"of what is inside it. It is a **read** key: it cannot change anything."),
    ("p", "The game you played above is that vault, opened live in this page. There is no copy "
          "of it on this site."),
    ("h2", "Why it exists"),
    ("p", "Because the gap between what an AI agent is *allowed* to do and what you *meant* it "
          "to do is real, mostly unmeasured, and nobody fills in a form about it honestly. A "
          "game gets an answer out of you while you are thinking about something else."),
    ("p", f"It is part of [**RiskMandate**]({RM}) — *the business risk layer for autonomous "
          f"systems* — which starts where this game stops. The game gets a person to say what "
          f"they wanted; RiskMandate is what turns the gap into a named owner and a decision "
          f"with a date on it. [What to do next](what-next/index.html) is the short version of "
          f"that handover."),
    ("p", f"The longer version of the argument — and the other games — is at "
          f"[games.sgit.ai]({CONCEPT_SITE})."),
    ("h2", "Say something"),
    ("p", "The fastest route is the 👍/👎 on any question in the game: one tap, no form, and it "
          "is filed against that specific question. There is a longer form behind *say more*, "
          "and a feedback tab in the game for anything that is not about one question. "
          f"[What happens to it]({CONCEPT_SITE}/games/ideas.html)."),
  ]},
# ---------------------------------------------------------------------------
"admin/index.html": {
  "title": "How this site is built",
  "description": "One content file, generated HTML and markdown twins, and a release gate that "
                 "fails a page mounting the game without its telemetry notice.",
  "blocks": [
    ("crumb", "[Play](index.html) / [About](about/index.html) / How this site is built"),
    ("h1", "How this site is built"),
    ("lead", "Static files on GitHub Pages. No server, no database, no analytics. Every page "
             "exists once, as content, in `admin/build/build_pages.py`; nothing under the site "
             "root is hand-edited."),
    ("pre", "python3 admin/build/build_pages.py   # pages, .md twins, llms.txt, sitemap\n"
            "node admin/build/validate.js          # the gate CI will run"),
    ("h2", "The game is embedded, not copied"),
    ("p", "`assets/vault-app-embed.js` opens the vault over the SG/Vault **embed protocol**: it "
          "loads the vault host in an iframe, waits for that frame to say it is ready, and then "
          "hands over the read key by `postMessage` with the target origin pinned. The key "
          "never appears in a URL, so it is never in browser history, a Referer header, or a "
          "server log."),
    ("p", "It is the sgit.ai component with the vault-browser surface suppressed, so a player "
          "gets a game rather than a file manager. Using the real host rather than the smaller "
          "read-only one is what keeps the game's chat panel and its telemetry lane working — "
          "the smaller host serves file reads only."),
    ("h2", "The gate"),
    ("p", "The house checks — version agreement, internal links, canonical host, and a "
          "key-leak tripwire — plus one that matters more here than anywhere: **a page that "
          "mounts the game must carry the telemetry disclosure.** Mechanical, and deliberately "
          "so. The vault this game lives in once shipped two pages saying *nothing sent* on the "
          "same screen as events being sent; the notice is not something to rely on remembering."),
    ("p", "Full engineering notes are on the sibling site: "
          f"[games.sgit.ai/admin]({CONCEPT_SITE}/admin/index.html)."),
  ]},
# ---------------------------------------------------------------------------
"admin/versions.html": {
  "title": "Release history",
  "description": "Every release of this site. The game inside it has its own, in the vault.",
  "blocks": [
    ("crumb", "[Play](index.html) / [About](about/index.html) / Release history"),
    ("h1", "Release history"),
    ("lead", "This is the history of the **site**. The game has its own, in the vault — 28 "
             "releases at v0.16.1 — reachable from the menu inside the game."),
    ("raw", versions_table()),
  ]},
}


def main():
    # The map's pages are computed from data/, not written here. Merging them in at build
    # time is what lets a merged pull request change the site with no hand in between.
    generated, pack = map_pages.pages(ROOT, {"site": SITE})
    clash = set(generated) & set(PAGES)
    if clash:
        raise SystemExit(f"generated pages collide with authored ones: {sorted(clash)}")
    manifest = map_pages.write_pack(ROOT, VERSION, pack)
    summary = shell.write_site(ROOT, SITE, NAV, FOOTER, {**PAGES, **generated}, VERSION, VERSION_LOG)
    print(f"build_pages: {VERSION} — {summary}; map: {len(generated)} pages from the pack "
          f"({manifest['counts']['profiles']} profiles, {manifest['counts']['capabilities']} "
          f"capabilities, {manifest['counts']['mandates']} mandates, "
          f"{manifest['content_hash'][:19]}…)")


if __name__ == "__main__":
    main()
