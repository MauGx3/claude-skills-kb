#!/usr/bin/env python3
"""Scan installed Claude Code plugins + skill roots and emit catalog/skills-catalog.json.

Re-run any time plugins change:  python3 scripts/build_catalog.py
"""
import json, os, re, glob, sys, datetime
import yaml

HOME_CLAUDE = os.path.expanduser("~/.claude")
# Cloud sessions keep plugins in plugins/synced; local installs (macOS/Linux) in plugins/cache.
_plugin_dirs = [d for d in (f"{HOME_CLAUDE}/plugins/synced", f"{HOME_CLAUDE}/plugins/cache") if os.path.isdir(d)]
ROOTS = {
    "plugins": os.environ.get("CLAUDE_PLUGINS_DIR") or (_plugin_dirs[0] if _plugin_dirs else f"{HOME_CLAUDE}/plugins"),
    "user_skills": f"{HOME_CLAUDE}/skills",
    "anthropic_public": "/mnt/skills/public",
    "anthropic_examples": "/mnt/skills/examples",
}
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "catalog", "skills-catalog.json")

def frontmatter(path):
    try:
        txt = open(path, encoding="utf-8", errors="replace").read()
    except Exception:
        return {}, ""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)", txt, re.S)
    if not m:
        return {}, txt
    try:
        fm = yaml.safe_load(m.group(1)) or {}
        if not isinstance(fm, dict): fm = {}
    except Exception:
        fm = {}
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1); fm[k.strip()] = v.strip().strip('"')
    return fm, m.group(2)

def clean(s, n=600):
    if s is None: return ""
    s = re.sub(r"\s+", " ", str(s)).strip()
    return s if len(s) <= n else s[:n-1] + "…"

def plugin_root(path):
    """Walk up to the dir containing .claude-plugin/plugin.json."""
    d = os.path.dirname(path)
    while d.startswith(ROOTS["plugins"]) and d != ROOTS["plugins"]:
        pj = os.path.join(d, ".claude-plugin", "plugin.json")
        if os.path.exists(pj): return d, pj
        d = os.path.dirname(d)
    return None, None

plugins, skills, commands, agents = {}, [], [], []

def load_plugin(pj):
    root = os.path.dirname(os.path.dirname(pj))
    if root in plugins: return plugins[root]
    try: meta = json.load(open(pj))
    except Exception: meta = {}
    mcp = {}
    for f in [os.path.join(root, ".mcp.json")]:
        if os.path.exists(f):
            try: mcp.update(json.load(open(f)).get("mcpServers", json.load(open(f))))
            except Exception: pass
    if isinstance(meta.get("mcpServers"), dict): mcp.update(meta["mcpServers"])
    p = {
        "name": meta.get("name", os.path.basename(root)),
        "version": meta.get("version", ""),
        "description": clean(meta.get("description"), 400),
        "author": (meta.get("author") or {}).get("name", "") if isinstance(meta.get("author"), dict) else str(meta.get("author", "")),
        "homepage": meta.get("homepage") or meta.get("repository") or "",
        "mcp_servers": sorted(mcp.keys()),
        "has_hooks": os.path.isdir(os.path.join(root, "hooks")) or "hooks" in meta,
        "path": root,
        "skills": [], "commands": [], "agents": [],
    }
    plugins[root] = p
    return p

# Plugins
for pj in glob.glob(ROOTS["plugins"] + "/**/.claude-plugin/plugin.json", recursive=True):
    if "/node_modules/" in pj: continue
    load_plugin(pj)

for path in glob.glob(ROOTS["plugins"] + "/**/SKILL.md", recursive=True):
    if "/node_modules/" in path or "/tests/" in path or "/test/" in path: continue
    root, pj = plugin_root(path)
    p = load_plugin(pj) if pj else None
    fm, body = frontmatter(path)
    name = os.path.basename(os.path.dirname(path))  # Claude Code namespaces by directory name
    if root and os.path.dirname(path) == root:      # SKILL.md at plugin root ("skills": "./")
        name = fm.get("name") or (p["name"] if p else name)
    rec = {
        "id": f"{p['name']}:{name}" if p else name,
        "name": fm.get("name") or name, "plugin": p["name"] if p else None,
        "description": clean(fm.get("description")),
        "user_invocable": fm.get("user-invocable", True) is not False,
        "disable_model_invocation": bool(fm.get("disable-model-invocation", False)),
        "allowed_tools": fm.get("allowed-tools", ""),
        "argument_hint": fm.get("argument-hint", ""),
        "lines": body.count("\n"),
        "source": "plugin", "path": path,
    }
    skills.append(rec)
    if p: p["skills"].append(name)

for path in sorted(set(glob.glob(ROOTS["plugins"] + "/**/commands/**/*.md", recursive=True, include_hidden=True))):
    if "/node_modules/" in path: continue
    root, pj = plugin_root(path)
    if not pj: continue
    p = load_plugin(pj); fm, _ = frontmatter(path)
    cdir = path[:path.rindex("/commands/") + len("/commands")]
    name = os.path.splitext(os.path.relpath(path, cdir))[0].replace(os.sep, ":")
    commands.append({"id": f"{p['name']}:{name}", "plugin": p["name"], "name": name,
                     "description": clean(fm.get("description"), 300),
                     "argument_hint": fm.get("argument-hint", ""), "path": path})
    p["commands"].append(name)

for path in glob.glob(ROOTS["plugins"] + "/**/agents/*.md", recursive=True):
    if "/node_modules/" in path: continue
    root, pj = plugin_root(path)
    if not pj: continue
    p = load_plugin(pj); fm, _ = frontmatter(path)
    if not fm.get("name") and not fm.get("description"): continue
    name = fm.get("name") or os.path.splitext(os.path.basename(path))[0]
    agents.append({"id": f"{p['name']}:{name}", "plugin": p["name"], "name": name,
                   "description": clean(fm.get("description"), 400),
                   "tools": fm.get("tools", "*"), "model": fm.get("model", ""), "path": path})
    p["agents"].append(name)

# Non-plugin skill roots
# /root/.claude/skills/synced = Anthropic skills synced from claude.ai and loaded as "anthropic-skills:*"
# /root/.claude/skills/<name> = user-level skills;  /mnt/skills/* = Anthropic library copies (claude.ai)
for path in glob.glob(ROOTS["user_skills"] + "/**/SKILL.md", recursive=True):
    fm, body = frontmatter(path)
    d = os.path.basename(os.path.dirname(path))
    synced = "/synced/" in path
    sid = f"anthropic-skills:{fm.get('name') or d}" if synced else d
    skills.append({"id": sid, "name": fm.get("name") or d, "plugin": "anthropic-skills" if synced else None,
                   "description": clean(fm.get("description")), "user_invocable": True,
                   "disable_model_invocation": False, "allowed_tools": fm.get("allowed-tools", ""),
                   "argument_hint": "", "lines": body.count("\n"),
                   "source": "anthropic-skills(synced)" if synced else "user", "path": path})
for src, base in [("anthropic-library", ROOTS["anthropic_public"]), ("anthropic-library", ROOTS["anthropic_examples"])]:
    for path in glob.glob(base + "/**/SKILL.md", recursive=True):
        fm, body = frontmatter(path)
        name = fm.get("name") or os.path.basename(os.path.dirname(path))
        skills.append({"id": f"anthropic-skills:{name}", "name": name, "plugin": "anthropic-skills",
                       "description": clean(fm.get("description")), "user_invocable": True,
                       "disable_model_invocation": False, "allowed_tools": fm.get("allowed-tools", ""),
                       "argument_hint": "", "lines": body.count("\n"), "source": src, "path": path})

# Harness built-ins (bundled in the Claude Code binary; no SKILL.md on disk)
BUILTINS = json.load(open(os.path.join(os.path.dirname(OUT), "builtin-skills.json")))
for b in BUILTINS:
    skills.append({"id": b["id"], "name": b["id"], "plugin": None, "description": b["description"],
                   "user_invocable": True, "disable_model_invocation": False, "allowed_tools": "",
                   "argument_hint": b.get("argument_hint", ""), "lines": 0, "source": "builtin", "path": None})

# Prefer synced/plugin copy over library copy for the same id
PRI = {"builtin": 0, "plugin": 1, "user": 1, "anthropic-skills(synced)": 1, "anthropic-library": 3}
skills.sort(key=lambda r: (r["id"], PRI.get(r["source"], 5), r["path"] or ""))
seen, uniq = set(), []
for s_ in skills:
    if s_["id"] in seen: continue
    seen.add(s_["id"]); uniq.append(s_)

ENABLED_F = os.path.join(os.path.dirname(OUT), "enabled-skills.txt")
enabled = {l.strip() for l in open(ENABLED_F) if l.strip() and not l.startswith("#")} if os.path.exists(ENABLED_F) else set()
ALIASES = {"startup-hook-skill": "session-start-hook", "sp-global:earnings-preview-single": "sp-global:earnings-preview-beta"}
for s_ in uniq:
    if s_["id"] in ALIASES: s_["invoke_as"] = ALIASES[s_["id"]]
    else: s_["invoke_as"] = s_["id"]
    s_["enabled"] = s_["invoke_as"] in enabled
for c in commands:
    c["enabled"] = c["id"] in enabled
out = {
    "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    "counts": {"plugins": len(plugins), "skills": len(uniq), "skills_enabled": sum(x["enabled"] for x in uniq), "commands": len(commands), "agents": len(agents)},
    "plugins": sorted([{k: v for k, v in p.items()} for p in plugins.values()], key=lambda p: p["name"].lower()),
    "skills": uniq,
    "commands": sorted(commands, key=lambda r: r["id"]),
    "agents": sorted(agents, key=lambda r: r["id"]),
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(out, open(OUT, "w"), indent=1, ensure_ascii=False)
print(json.dumps(out["counts"]))
