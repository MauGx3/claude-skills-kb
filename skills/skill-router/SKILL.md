---
name: skill-router
description: Pick the right installed skill when unsure which fits, when skills overlap, or when asked which skills exist for a topic. Looks up the routing table and catalog.
---

# Skill Router

1. Find the task in `../../docs/ROUTING.md` → "Intent → skill". Load the **Use** skill.
2. No match? Search by keyword:
   ```bash
   python3 ../../scripts/find_skill.py "<keywords>"
   ```
3. Overlapping skills: use the `primary` in `../../config/skills-config.yaml` → `overlaps`.
4. Load it with `Skill(skill="<id>")` and say "Using <id> to <purpose>".

Markers in the docs:
- ✅ available.
- ⏸ the plugin is off by default (`../../config/plugin-profile.yaml`). Use the listed fallback. If the user needs the original, tell them to add `{"enabledPlugins": {"<plugin>@synced": true}}` to the project's `.claude/settings.json` and restart Claude Code.
- ⬜ cannot be invoked.

If a skill's MCP server is down, tell the user and use the fallback listed under "MCP dependencies".
