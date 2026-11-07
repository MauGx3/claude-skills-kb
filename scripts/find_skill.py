#!/usr/bin/env python3
"""Keyword search over the skills catalog.  Usage: find_skill.py "pdf merge" [--all] [-n 10]"""
import json, os, re, sys
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = [a for a in sys.argv[1:] if not a.startswith("-")]
n = int(sys.argv[sys.argv.index("-n") + 1]) if "-n" in sys.argv else 10
if "-n" in sys.argv: args.remove(str(n))
show_all = "--all" in sys.argv
q = [t for t in re.findall(r"\w+", " ".join(args).lower()) if len(t) > 1]
if not q: sys.exit(__doc__)
cat = json.load(open(f"{B}/catalog/skills-catalog.json"))
try:
    import yaml
    OFF = {d["name"] for d in yaml.safe_load(open(f"{B}/config/plugin-profile.yaml")).get("disable", [])}
    PRIMARY = {o["primary"] for o in yaml.safe_load(open(f"{B}/config/skills-config.yaml"))["overlaps"].values()}
except Exception:
    OFF, PRIMARY = set(), set()
rows = []
for s in cat["skills"]:
    if not show_all and (not s["enabled"] or s["plugin"] in OFF): continue
    name, desc = s["invoke_as"].lower(), (s["description"] or "").lower()
    score = sum(3 * (t in name) + desc.count(t) for t in q)
    if score and s["invoke_as"] in PRIMARY: score += 5  # agree with the routing config
    if score: rows.append((score, s))
for a in cat["agents"]:
    name, desc = a["id"].lower(), (a["description"] or "").lower()
    score = sum(3 * (t in name) + desc.count(t) for t in q)
    if a["plugin"] in OFF and not show_all: continue
    if score: rows.append((score - 0.5, {"invoke_as": f"[agent] {a['id']}", "description": a["description"], "enabled": True}))
for score, s in sorted(rows, key=lambda r: -r[0])[:n]:
    print(f"{score:>5.1f}  {'✅' if s['enabled'] else '⬜'} {s['invoke_as']}\n       {(s['description'] or '')[:160]}")
