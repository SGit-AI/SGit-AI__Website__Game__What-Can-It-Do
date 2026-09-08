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

ROOT = Path(__file__).resolve().parents[2]
VERSION = (ROOT / "admin/build/version.txt").read_text().strip()

# The games vault, read-only, published on purpose. See the note in the sibling site's
# build_pages.py and in validate.js: this is a READ key. It cannot write.
VAULT = "4evnlwrj"
READKEY = "f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118"
VAULT_UI = f"https://dev.vault.sgraph.ai/#{READKEY}%3A{VAULT}"
CONCEPT_SITE = "https://games.sgit.ai"

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
    "netline": (f'<a href="{CONCEPT_SITE}"><b>↗ games.sgit.ai</b></a> — why we build games, and '
                'the others · <a href="https://sgit.ai">↗ sgit.ai</a> — the encrypted vault the '
                'game is published in · <a href="https://pki.sgit.ai">↗ pki.sgit.ai</a> — where '
                'the capability data comes from'),
    "telemetry_note": '⚠ This game sends anonymous usage events while you play — no name, no '
                      'id, no fingerprint — and every screen has a pause switch. '
                      '<a href="{up}what-we-learn/index.html" style="display:inline;padding:0">'
                      'Exactly what is sent</a>.',
}

NAV = [
    ("Play", "index.html", [], ()),
    ("How it's scored", "how-it-is-scored/index.html", [], ("how-it-is-scored/",)),
    ("Some are impossible", "the-ceiling/index.html", [], ("the-ceiling/",)),
    ("What we learn", "what-we-learn/index.html", [], ("what-we-learn/",)),
    ("About", "about/index.html", [
        ("About the game", "about/index.html"),
        ("Release history", "admin/versions.html"),
        ("How this site is built", "admin/index.html"),
    ], ("about/", "admin/")),
]

FOOTER = [
    ("The game", [
        ("&#8594; Play", "index.html"),
        ("How it's scored", "how-it-is-scored/index.html"),
        ("Why some are impossible", "the-ceiling/index.html"),
    ]),
    ("Straight answers", [
        ("What we learn from you", "what-we-learn/index.html"),
        ("Who made it", "about/index.html"),
        ("Open the game's source", VAULT_UI),
    ]),
    ("More", [
        ("games.sgit.ai", CONCEPT_SITE),
        ("Release history", "admin/versions.html"),
        ("llms.txt", "llms.txt"),
    ]),
]

VERSION_LOG = [
    ("v0.1.0", "2026-09-08",
     "First publish. The game mounted and playable on arrival, over the SG/Vault embed "
     "protocol with the vault-browser surface suppressed, so a player sees a game and not a "
     "file manager. Four supporting pages — the scoring rule, the impossible questions, what "
     "is sent while you play, and who made it. The telemetry notice sits with the game rather "
     "than in the footer, and the release gate fails a page that mounts the game without one."),
]

# One sentence, above the game, where somebody who never scrolls still reads it. The longer
# statement is on /what-we-learn/ and the authoritative one is inside the vault.
DISCLOSE_SHORT = (
    "**Before you start:** this game sends **anonymous usage events** while you play — which "
    "screens you reach, your answers, your score. No name, no account, no id, no fingerprint, "
    "nothing that identifies you or your machine. There is a **pause switch** on every screen, "
    "and it works before the first question. "
    "[Exactly what is sent](/what-we-learn/index.html).")


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
    ("disclose", DISCLOSE_SHORT),
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
    ("h2", "What you walk away with"),
    ("p", "A calibration figure — how often you were right when you said you were sure — and "
          "**a draft of what you actually wanted your agent to be allowed to do**, assembled "
          "from your answers to the second question. Most people have never written that down. "
          "You will not have set out to write it either."),
    ("p", "Then the gap between the two: the things it can do that you did not want, split by "
          "whether you saw them coming. And one thing to change."),
    ("h2", "Free, no sign-up, nothing stored"),
    ("p", "No account. No email. Nothing is saved between visits — close the tab and the run "
          "is gone. The game runs entirely in your browser: the scoring is arithmetic, there "
          "is no model deciding whether you were right. The only thing that leaves your "
          "browser is the anonymous counting described above, and you can switch it off."),
    ("p", f"Send it to someone: **`{SITE['host']}`**"),
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
"what-we-learn/index.html": {
  "title": "What we learn from you",
  "description": "Exactly what the game sends while you play, what it deliberately does not "
                 "send, what it can and cannot prove, and how to switch it off.",
  "blocks": [
    ("crumb", "[Play](index.html) / What we learn"),
    ("h1", "What we learn from you"),
    ("lead", "The game sends anonymous usage events while you play. Here is exactly what is in "
             "them, what is deliberately left out, and how to stop it. Nothing on this page is "
             "a summary of something less flattering."),
    ("disclose", DISCLOSE_SHORT),
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
    ("p", f"The longer version of that argument — and the other games — is at "
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
    summary = shell.write_site(ROOT, SITE, NAV, FOOTER, PAGES, VERSION, VERSION_LOG)
    print(f"build_pages: {VERSION} — {summary}")


if __name__ == "__main__":
    main()
