# Claude Skills Knowledge Base

Configuration, documentation and memory for every skill on this Claude account. It is
written so agents in **Claude Code** and **claude.ai** pick the right skill on the first try.

**Snapshot (2026-11-07):** 75 plugins · 387 skill files · **323 skills enabled** in Claude Code · 49 slash commands · 27 subagents.

## What's here

| Path | Purpose | Audience |
|---|---|---|
| `CLAUDE.md` | Compact routing rules (~490 tokens, capped at 2,500 chars because it loads in every session) | Claude Code agents |
| `AGENTS.md` | Generated from CLAUDE.md for other harnesses and claude.ai Project instructions | Any agent |
| `docs/ROUTING.md` | 88 intent → skill routes, overlap resolution, MCP dependencies, subagents | Agents and humans |
| `docs/CATALOG.md` | Every plugin, skill, command and subagent, grouped into 14 categories, with ✅/⬜ enabled flags | Reference |
| `catalog/skills-catalog.json` | Machine-readable catalog: id, plugin, description, enabled flag, allowed tools, path | Scripts and agents |
| `catalog/enabled-skills.txt` | The skill list the session exposed to the model; the source of the enabled flags | Maintenance |
| `catalog/builtin-skills.json` | Built-in harness skills that have no SKILL.md on disk | Maintenance |
| `config/skills-config.yaml` | **Main configuration file:** rules, categories, routes, overlap primaries, MCP dependencies | Edit this |
| `memory/` | Structured memory files (`claude-memory:structured-memory` format) | Claude Code memory |
| `skills/skill-router/` | An installable skill that routes a task to the right skill | Claude Code |
| `scripts/build_catalog.py` | Rescans the plugin folders and rebuilds the JSON catalog | Maintenance |
| `scripts/render_docs.py` | Renders CATALOG.md and ROUTING.md, and checks every routed ID exists and is enabled | Maintenance |
| `scripts/find_skill.py` | Keyword search: `python3 scripts/find_skill.py "merge pdf"` | Agents |
| `config/plugin-profile.yaml` | Plugins to turn off for a smaller context baseline, with reasons | Edit this |
| `scripts/plugin_profile.py` | Applies the profile with `claude plugin disable` (dry run by default) | Setup |
| `tests/` | Installer, renderer, profile and search tests (`python3 -m unittest discover -s tests`) | Maintenance |
| `install.sh` | Installs into `~/.claude` or a project; `plugins` mode applies the profile | Setup |

## Install

All projects (adds the guide to `~/.claude/CLAUDE.md` and installs the skill-router skill):

```bash
./install.sh user
```

One project (adds CLAUDE.md, `.claude/skills/skill-router` and the memory files):

```bash
./install.sh project /path/to/repo
```

Turn off the plugins in `config/plugin-profile.yaml` (dry run first, then apply, then restart Claude Code):

```bash
./install.sh plugins
```

```bash
./install.sh plugins --apply
```

**claude.ai:** paste `AGENTS.md` into a Project's custom instructions, or upload `docs/ROUTING.md` as Project knowledge.

## Update after plugin changes

```bash
python3 scripts/build_catalog.py
```

```bash
python3 scripts/render_docs.py
```

To refresh enabled flags, replace `catalog/enabled-skills.txt` with the current session's skill list first.
Change routing only in `config/skills-config.yaml`; the files under `docs/` are generated.

## Notes and limits

- The enabled flags come from one Claude Code cloud session. Other surfaces (desktop, claude.ai) may enable a different set.
- Built-in harness skills (`dataviz`, `claude-api`, `code-review`, …) have no files on disk. Their descriptions in `catalog/builtin-skills.json` are summaries.
- MCP connection status in `docs/ROUTING.md` was recorded in a cloud sandbox where many hosts were blocked by the proxy. It is not a statement about your accounts.
- Overlap primaries are judgment calls. Change them in `config/skills-config.yaml → overlaps`.
