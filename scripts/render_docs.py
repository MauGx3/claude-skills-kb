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
profile = yaml.safe_load(open(f"{B}/config/plugin-profile.yaml"))
OFF = {d["name"] for d in profile.get("disable", [])}

def plugin_of(i):
    return (skills.get(i) or cmds.get(i) or {}).get("plugin")

def available(i):
    """Enabled in the catalog and its plugin not turned off by the plugin profile."""
    rec = skills.get(i) or cmds.get(i)
    return bool(rec) and rec.get("enabled", True) and rec.get("plugin") not in OFF

def effective(route):
    """First available skill in use, then alternates. Returns (id, is_fallback) or (None, False)."""
    for i in route.get("use", []):
        if available(i): return i, False
    for i in route.get("alternates", []) or []:
        if available(i): return i, True
    return None, False

def esc(s): return (s or "").replace("|", "\\|").replace("\n", " ")
def short(s, n=220):
    s = esc(s); return s if len(s) <= n else s[:n-1] + "…"

# ---- validate
bad = []
for r in cfg["routing"]:
    for k in ("use", "then", "alternates"):
        for i in r.get(k, []) or []:
            if i not in valid: bad.append((r["intent"], i))
for r in cfg["routing"]:
    if effective(r)[0] is None and not r.get("profile_off_ok"):
        bad.append((r["intent"], "no available skill after plugin profile"))
for k, o in cfg["overlaps"].items():
    for i in [o["primary"], *o["others"]]:
        if i not in valid: bad.append((k, i))
    if not available(o["primary"]): bad.append((k, f"primary {o['primary']} unavailable under plugin profile"))
for i in (x for r in cfg["routing"] for k in ("use","then","alternates") for x in r.get(k,[]) or []):
    if i in skills and not skills[i]["enabled"]: bad.append(("disabled", i))
# CLAUDE.md is loaded into every session: keep it small and its IDs live.
CLAUDE_MD_BUDGET = 2500  # chars (~625 tokens)
claude_md = open(f"{B}/CLAUDE.md").read()
if len(claude_md) > CLAUDE_MD_BUDGET:
    bad.append(("CLAUDE.md", f"{len(claude_md)} chars > budget {CLAUDE_MD_BUDGET}"))
for i in re.findall(r"`([\w-]+:[\w-]+)`", claude_md):
    if not available(i): bad.append(("CLAUDE.md", f"{i} not available"))
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
      "Legend: ✅ invocable via `Skill` tool in Claude Code · ⏸ plugin turned off by `config/plugin-profile.yaml` (re-enable per project) · ⬜ present on disk but not exposed (disabled, in-progress, or claude.ai-only library skill).", "",
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
        L += [f"### {k}" + (f" `v{pm['version']}`" if pm.get("version") else "") + (" ⏸ off by plugin profile" if k in OFF else ""), ""]
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
                mark = '⬜' if not s['enabled'] else ('⏸' if k in OFF else '✅')
                L.append(f"| `{s['invoke_as']}` | {mark} | {short(s['description'])} |")
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
     f"⏸ = plugin off by default (`config/plugin-profile.yaml`: {', '.join(sorted(OFF))}). When the primary is off, **Use** shows the first available fallback; re-enable the plugin per project to get the original.", "",
     "| When the task is… | Use | Then | Alternates |", "|---|---|---|---|"]
def fmt(xs):
    return ", ".join(f"`{x}`" + ("" if available(x) else " ⏸") for x in (xs or [])) or "—"
for r in cfg["routing"]:
    eff, fb = effective(r)
    if eff:
        use = f"`{eff}`" + (f" (fallback; primary {fmt(r['use'])})" if fb else "")
    else:
        use = fmt(r["use"]) + f" — enable `{plugin_of(r['use'][0])}@synced` in the project"
    R.append(f"| {esc(r['intent'])} | {use} | {fmt(r.get('then'))} | {fmt(r.get('alternates'))} |")
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
# AGENTS.md mirrors CLAUDE.md for other harnesses / claude.ai Project instructions.
open(f"{B}/AGENTS.md", "w").write(
    "<!-- Generated from CLAUDE.md by scripts/render_docs.py. Edit CLAUDE.md instead. -->\n"
    "# AGENTS.md\n\nSkills routing guide for any agent. In claude.ai, paste into Project instructions.\n\n"
    + claude_md.split("\n", 1)[1].lstrip())
# ---- Claude desktop app (Chat / Cowork tabs)
# Chat has no Claude Code built-ins and no local plugin profile (that lives in ~/.claude), so it
# gets its own availability rule and its own routing table, packaged as an uploadable skill.
import io, zipfile

def chat_available(i):
    rec = skills.get(i)
    return bool(rec) and rec.get("enabled") and rec.get("source") != "builtin"

DESKTOP_BUDGET = 2500  # chars; pasted into Settings → Your Claude → Instructions
desk = open(f"{B}/desktop/instructions.md").read()
dbad = []
if len(desk) > DESKTOP_BUDGET:
    dbad.append(f"desktop/instructions.md: {len(desk)} chars > budget {DESKTOP_BUDGET}")
for i in re.findall(r"`([\w-]+:[\w-]+)`", desk):
    if not chat_available(i): dbad.append(f"desktop/instructions.md: {i} not available in chat")
if dbad:
    print("INVALID DESKTOP:"); [print("  ", b) for b in dbad]; sys.exit(1)

rows, skipped = [], []
for r in cfg["routing"]:
    cands = [i for i in (r.get("use", []) + (r.get("alternates") or [])) if chat_available(i)]
    if not cands:
        skipped.append(r["intent"]); continue
    rest = [f"`{x}`" for x in cands[1:4]]
    rows.append(f"| {esc(r['intent'])} | `{cands[0]}` | {', '.join(rest) or '—'} |")
chat_routing = "\n".join([
    "# Skill routing for Claude chat and Cowork", "",
    f"_Generated {cat['generated_at']} by `scripts/render_docs.py` from `config/skills-config.yaml`._", "",
    "Use the **Use** skill first. Use an alternate only when the person names it or the first doesn't fit.",
    "Skills are listed only if they are available in chat; Claude Code-only tools are left out.", "",
    "| When the task is… | Use | Alternates |", "|---|---|---|", *rows, "",
    "## Overlaps", "", "When several skills teach the same thing, use the primary:", "",
    *[f"- {k.replace('_', ' ')}: `{o['primary']}`" for k, o in cfg["overlaps"].items() if chat_available(o["primary"])],
    "",
    f"_Left out (Claude Code only): {', '.join(skipped)}._" if skipped else "", ""])
chat_skill = """---
name: skill-router
description: Pick the right installed skill when unsure which one fits a task, when several skills overlap, or when asked which skills exist for a topic. Reads the bundled routing table.
---

# Skill Router

1. Open `ROUTING.md` in this skill and find the task under "When the task is…".
2. Use the skill in the **Use** column. If it isn't available or its connector isn't connected, say so and use the first alternate.
3. When skills overlap, use the primary listed under "Overlaps".
4. Say which skill you used and why, in one line.

If nothing matches, use your general judgment and say that no skill matched.
"""
os.makedirs(f"{B}/desktop/skill-router", exist_ok=True)
open(f"{B}/desktop/skill-router/SKILL.md", "w").write(chat_skill)
open(f"{B}/desktop/skill-router/ROUTING.md", "w").write(chat_routing)

# Deterministic zip so CI can check it is current: fixed timestamps and permissions, and
# ZIP_STORED, because deflate output can differ between zlib builds (macOS vs Linux).
buf = io.BytesIO()
with zipfile.ZipFile(buf, "w", zipfile.ZIP_STORED) as z:
    for name in ("SKILL.md", "ROUTING.md"):
        zi = zipfile.ZipInfo(f"skill-router/{name}", date_time=(2026, 1, 1, 0, 0, 0))
        zi.external_attr = 0o644 << 16
        zi.compress_type = zipfile.ZIP_STORED
        z.writestr(zi, open(f"{B}/desktop/skill-router/{name}").read())
data = buf.getvalue()
zpath = f"{B}/desktop/skill-router.zip"
if not os.path.exists(zpath) or open(zpath, "rb").read() != data:
    open(zpath, "wb").write(data)

print("ok", len(cfg["routing"]), "routes,", len(L), "catalog lines,", len(claude_md), "chars CLAUDE.md,",
      len(rows), "chat routes,", len(desk), "chars desktop instructions")
