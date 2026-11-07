#!/usr/bin/env python3
"""Inspect repository metadata and root structure without changing remote state.

Requires GitHub CLI authentication. Public repositories only unless explicitly opted in.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess


def gh(*args):
    result = subprocess.run(["gh", *args], capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def inspect(repo):
    name = repo["nameWithOwner"]
    try:
        root = gh("api", f"repos/{name}/contents")
        names = sorted(item["name"] for item in root)
        error = None
    except (subprocess.CalledProcessError, TypeError, KeyError):
        names, error = [], "Root unavailable; verify empty repository or access."
    return {**repo, "root": names, "inspection_error": error}


def recommendations(repo):
    names = repo["root"]
    actions = []
    if repo["isArchived"]:
        actions.append("Preserve as historical; identify a current successor.")
    elif repo["isFork"]:
        actions.append("Document upstream attribution, local changes and maintenance policy.")
    elif repo["inspection_error"]:
        actions.append(repo["inspection_error"])
    else:
        actions.append("Verify one exact-source quickstart and its limitations.")
    if not repo["inspection_error"] and not any(name.lower().startswith("readme") for name in names):
        actions.append("Add a project-specific README.")
    if not repo["licenseInfo"]:
        actions.append("Inspect rights; GitHub did not detect a license.")
    if "package.json" in names and not any(name in names for name in ["package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lock", "bun.lockb"]):
        actions.append("Check reproducible dependency installation; no root JS lockfile detected.")
    return " ".join(actions)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", default="sargonxg")
    parser.add_argument("--include-private", action="store_true", help="Include private metadata in local output. Do not publish that output.")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", action="store_true", help="Output evidence as JSON instead of Markdown.")
    args = parser.parse_args()
    try:
        repos = gh("repo", "list", args.owner, "--limit", "1000", "--json",
                   "nameWithOwner,isArchived,isFork,isPrivate,description,licenseInfo,defaultBranchRef,pushedAt")
        repos = [repo for repo in repos if args.include_private or not repo["isPrivate"]]
        with ThreadPoolExecutor(max_workers=4) as pool:
            evidence = sorted(pool.map(inspect, repos), key=lambda repo: repo["nameWithOwner"].casefold())
    except (subprocess.CalledProcessError, FileNotFoundError, json.JSONDecodeError) as error:
        parser.error(f"GitHub inspection failed ({type(error).__name__}). Check gh auth status; no remote changes were made.")
    stamp = datetime.now(timezone.utc).date().isoformat()
    if args.json:
        output = json.dumps({"inspected_on": stamp, "include_private": args.include_private, "repositories": evidence}, indent=2)
    else:
        lines = [f"# Repository evidence — {stamp}", "", "Metadata and root paths only. No code-quality, deployment or successful-test claim is implied.", "",
                 "| Repository | State | Root evidence / next check |", "| --- | --- | --- |"]
        for repo in evidence:
            name = repo["nameWithOwner"]
            state = "archived" if repo["isArchived"] else "active"
            state += " · fork" if repo["isFork"] else ""
            state += " · private" if repo["isPrivate"] else ""
            lines.append(f"| [{name}](https://github.com/{name}) | {state} | {recommendations(repo)} |")
        output = "\n".join(lines)
    if args.output:
        args.output.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()
