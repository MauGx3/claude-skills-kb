#!/usr/bin/env python3
"""Apply config/plugin-profile.yaml with the official Claude Code CLI.

    python3 scripts/plugin_profile.py            # dry run: print what would change
    python3 scripts/plugin_profile.py --apply    # run `claude plugin disable <name>@synced`

Uses the CLI instead of editing settings.json, so Claude Code owns the file format.
"""
import json, os, shutil, subprocess, sys

import yaml

B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_profile(path=os.path.join(B, "config", "plugin-profile.yaml")):
    prof = yaml.safe_load(open(path))
    if prof.get("version") != 1:
        sys.exit(f"unsupported plugin-profile version: {prof.get('version')}")
    return prof


def current_state(settings=os.path.expanduser("~/.claude/settings.json")):
    try:
        return json.load(open(settings)).get("enabledPlugins", {})
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def plan(prof, state):
    """Return (todo, already) lists of plugin ids."""
    todo, already = [], []
    for item in prof.get("disable", []):
        pid = f"{item['name']}@synced"
        (already if state.get(pid) is False else todo).append(pid)
    return todo, already


def main(argv):
    apply = "--apply" in argv
    prof = load_profile()
    todo, already = plan(prof, current_state())
    for pid in already:
        print(f"ok       {pid} already disabled")
    for pid in todo:
        print(f"{'disable' if apply else 'would disable'} {pid}")
    for m in prof.get("manual", []):
        print(f"manual   {m['name']}: {m['action']}")
    if not apply or not todo:
        if todo:
            print("\nDry run. Re-run with --apply to disable.")
        return 0
    if not shutil.which("claude"):
        print("error: `claude` CLI not on PATH; run the printed commands in a terminal where it is.")
        return 1
    failed = 0
    for pid in todo:
        r = subprocess.run(["claude", "plugin", "disable", pid], capture_output=True, text=True)
        status = "done" if r.returncode == 0 else f"FAILED ({(r.stderr or r.stdout).strip()[:200]})"
        failed += r.returncode != 0
        print(f"  {pid}: {status}")
    print("Restart Claude Code for the change to take effect.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
