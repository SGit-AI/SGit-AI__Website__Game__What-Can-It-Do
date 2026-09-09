#!/usr/bin/env python3
"""admin/build/vault-facts.json — what the game's published vault says about itself, cached here
with the day it was read.

    python3 admin/build/vault_facts.py --clone <dir> --vault <id> [--commit <id>]

<dir> is a clone of the game's vault (sgit clone <read-key>:<id> <dir>). The facts are read from
files in that clone — version.json and telemetry/telemetry.config.json — never typed. The release
gate (validate.js, check 10) then holds the site to them: the vault the pages mount must be the
vault these facts describe, and /what-we-learn/ must state the same `signals` value the vault's
config carries. That is how the sentence "no fingerprinting" can never silently go false again:
v0.21.0 of the game turned fingerprinting on while the site went on promising there was none,
and nothing in either build could see the other.

The site's CI does not run sgit, so the read happens here, by hand, and the file carries its
date. A stale file is visible as a stale date; a wrong one fails the gate.
"""
import argparse
import datetime as dt
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clone", required=True, help="a clone of the game's vault")
    ap.add_argument("--vault", required=True, help="the vault id the clone was made from")
    ap.add_argument("--commit", default=None, help="the vault commit the clone is at, if known")
    a = ap.parse_args()
    clone = Path(a.clone)
    version = json.loads((clone / "version.json").read_text())
    tel = json.loads((clone / "telemetry" / "telemetry.config.json").read_text())
    facts = {
        "type": "vault-facts/v1",
        "_what_this_is": ("What the game's vault says about itself, read from a clone of it by "
                          "admin/build/vault_facts.py and dated. validate.js check 10 holds the "
                          "site to this file; the file holds itself to the vault by its date and "
                          "commit."),
        "vault": a.vault,
        "version": version["version"],
        "released": version["date"],
        "releases": len(version["releases"]),
        "signals": bool(tel.get("signals", False)),
        "telemetry_vault": tel.get("telemetry_vault_id"),
        "taken": dt.date.today().isoformat(),
        "commit": a.commit,
        "read_from": ["version.json", "telemetry/telemetry.config.json"],
    }
    out = HERE / "vault-facts.json"
    out.write_text(json.dumps(facts, indent=2) + "\n")
    print(f"vault-facts.json: {facts['vault']} v{facts['version']} · signals {facts['signals']} · "
          f"{facts['releases']} releases · taken {facts['taken']}")


if __name__ == "__main__":
    main()
