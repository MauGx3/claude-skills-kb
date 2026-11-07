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
rows = []
for s in cat["skills"]:
    if not show_all and not s["enabled"]: continue
    name, desc = s["invoke_as"].lower(), (s["description"] or "").lower()
    score = sum(3 * (t in name) + desc.count(t) for t in q)
    if score: rows.append((score, s))
for a in cat["agents"]:
    name, desc = a["id"].lower(), (a["description"] or "").lower()
    score = sum(3 * (t in name) + desc.count(t) for t in q)
    if score: rows.append((score - 0.5, {"invoke_as": f"[agent] {a['id']}", "description": a["description"], "enabled": True}))
for score, s in sorted(rows, key=lambda r: -r[0])[:n]:
    print(f"{score:>5.1f}  {'✅' if s['enabled'] else '⬜'} {s['invoke_as']}\n       {(s['description'] or '')[:160]}")
