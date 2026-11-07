#!/usr/bin/env python3
"""Render docs/CATALOG.md, docs/ROUTING.md and memory/ from catalog + config. Also validates IDs."""
import json, os, re, sys, yaml
from collections import defaultdict
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cat = json.load(open(f"{B}/catalog/skills-catalog.json"))
cfg = yaml.safe_load(open(f"{B}/config/skills-config.yaml"))
skills = {s["invoke_as"]: s for s in cat["skills"]}
cmds = {c["id"]: c for c in cat["commands"]}
valid = set(skills) | set(cmds)

def esc(s): return (s or "").replace("|", "\\|").replace("\n", " ")
def short(s, n=220):
    s = esc(s); return s if len(s) <= n else s[:n-1] + "…"

# ---- validate
bad = []
for r in cfg["routing"]:
    for k in ("use", "then", "alternates"):
        for i in r.get(k, []) or []:
            if i not in valid: bad.append((r["intent"], i))
for k, o in cfg["overlaps"].items():
    for i in [o["primary"], *o["others"]]:
        if i not in valid: bad.append((k, i))
for i in (x for r in cfg["routing"] for k in ("use","then","alternates") for x in r.get(k,[]) or []):
    if i in skills and not skills[i]["enabled"]: bad.append(("disabled", i))
if bad:
    print("INVALID IDS:"); [print("  ", b) for b in bad]; sys.exit(1)

# ---- categories
plugin_cat = {"user-level skills": "Meta / orchestration / skill system"}
for c, v in cfg["categories"].items():
    for p in v.get("plugins", []): plugin_cat[p] = c
    for b in v.get("builtins", []): plugin_cat["builtin:" + b] = c

by_plugin = defaultdict(list)
for s in cat["skills"]:
    key = s["plugin"] or ("builtin:" + s["id"] if s["source"] == "builtin" else "user-level skills")
    by_plugin[key].append(s)
pmeta = {}
for p in cat["plugins"]:
    pmeta.setdefault(p["name"], p)

os.makedirs(f"{B}/docs", exist_ok=True)
L = []
c = cat["counts"]
L += ["# Skills Catalog", "",
      f"_Generated {cat['generated_at']} by `scripts/render_docs.py` — do not edit by hand; edit `config/` and re-run._", "",
      f"**{c['plugins']} plugins · {c['skills']} skills ({c['skills_enabled']} enabled in Claude Code) · {c['commands']} slash commands · {c['agents']} subagents**", "",
      "Legend: ✅ invocable via `Skill` tool in Claude Code · ⬜ present on disk but not exposed (disabled, in-progress, or claude.ai-only library skill).", "",
      "Invoke: `Skill(skill=\"<id>\")` — or type `/<id>` as the user.", "", "## Contents", ""]
order = list(cfg["categories"].keys()) + ["Uncategorized"]
groups = defaultdict(list)
for key in by_plugin:
    groups[plugin_cat.get(key, "Uncategorized")].append(key)
for p in pmeta:
    if p not in by_plugin and (pmeta[p]["commands"] or pmeta[p]["agents"] or pmeta[p]["mcp_servers"]):
        groups[plugin_cat.get(p, "Uncategorized")].append(p)
for g in order:
    if groups.get(g): L.append(f"- [{g}](#{re.sub(r'[^a-z0-9 -]','',g.lower()).replace(' ','-')})")
L.append("")
for g in order:
    keys = groups.get(g)
    if not keys: continue
    L += [f"## {g}", ""]
    builtins = sorted(k for k in keys if k.startswith("builtin:"))
    if builtins:
        L += ["### Built-in (Claude Code harness)", "", "| Skill | Enabled | What it does |", "|---|---|---|"]
        for k in builtins:
            s = by_plugin[k][0]; L.append(f"| `{s['id']}` | ✅ | {short(s['description'],300)} |")
        L.append("")
    for k in sorted((k for k in keys if not k.startswith("builtin:")), key=str.lower):
        pm = pmeta.get(k, {})
        L += [f"### {k}" + (f" `v{pm['version']}`" if pm.get("version") else ""), ""]
        if pm.get("description"): L += [f"_{esc(pm['description'])}_", ""]
        extra = []
        if pm.get("homepage"): extra.append(f"Source: {pm['homepage']}")
        if pm.get("mcp_servers"): extra.append("MCP: " + ", ".join(f"`{m}`" for m in pm["mcp_servers"]))
        if pm.get("has_hooks"): extra.append("Has hooks")
        if extra: L += [" · ".join(extra), ""]
        ss = sorted(by_plugin.get(k, []), key=lambda s: (not s["enabled"], s["id"]))
        if ss:
            L += ["| Skill | | Description |", "|---|---|---|"]
            for s in ss:
                L.append(f"| `{s['invoke_as']}` | {'✅' if s['enabled'] else '⬜'} | {short(s['description'])} |")
            L.append("")
        pc = [x for x in cat["commands"] if x["plugin"] == k]
        if pc:
            L += ["**Slash commands:** " + ", ".join(f"`/{x['id']}`" + (f" — {short(x['description'],90)}" if x['description'] else "") for x in pc), ""]
        pa = [x for x in cat["agents"] if x["plugin"] == k]
        if pa:
            L += ["**Subagents** (`Agent(subagent_type=…)`):", ""]
            L += [f"- `{x['id']}` — {short(x['description'],200)}" for x in pa]
            L.append("")
open(f"{B}/docs/CATALOG.md", "w").write("\n".join(L))

# ---- ROUTING.md
R = ["# Skill Routing Guide", "",
     f"_Generated {cat['generated_at']} from `config/skills-config.yaml`._", "",
     "Use this to pick a skill fast. **Use** = load first. **Then** = follow-on skills. **Alternates** = only if named by the user or the primary doesn't fit.", "",
     "## Global rules", ""] + [f"{i+1}. {r}" for i, r in enumerate(cfg["rules"])] + ["", "## Intent → skill", "",
     "| When the task is… | Use | Then | Alternates |", "|---|---|---|---|"]
fmt = lambda xs: ", ".join(f"`{x}`" for x in (xs or [])) or "—"
for r in cfg["routing"]:
    R.append(f"| {esc(r['intent'])} | {fmt(r['use'])} | {fmt(r.get('then'))} | {fmt(r.get('alternates'))} |")
R += ["", "## Overlap resolution", "", "Several plugins teach the same discipline. Default to the primary.", "",
      "| Topic | Primary | Others (equivalent) |", "|---|---|---|"]
for k, o in cfg["overlaps"].items():
    R.append(f"| {k.replace('_',' ')} | `{o['primary']}` | {fmt(o['others'])} |")
m = cfg["mcp_dependencies"]
R += ["", "## MCP dependencies", "", f"Connected this session: {', '.join(m['connected'])}.", "",
      f"Failed this session: {', '.join(m['failed_this_session'])}.", "", "| Skills | Needs MCP server |", "|---|---|"]
R += [f"| `{k}` | {v} |" for k, v in m["skills_needing_mcp"].items()]
R += ["", f"> {m['note']}", "", "## Subagents", "", "| Agent type | Purpose |", "|---|---|"]
R += [f"| `{a['id']}` | {short(a['description'],180)} |" for a in cat["agents"]]
open(f"{B}/docs/ROUTING.md", "w").write("\n".join(R) + "\n")
print("ok", len(cfg["routing"]), "routes,", len(L), "catalog lines")
