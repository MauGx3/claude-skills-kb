---
name: skill-router
description: Use when unsure which installed skill fits a task, when several skills seem to overlap, or when asked "what skills do I have", "which skill should I use for X", or "list skills for <topic>". Looks up the task in the routing table and the full catalog, then names the skill to load.
---

# Skill Router

Find the right installed skill for a task and load it.

## Steps

1. Look up the task in `docs/ROUTING.md`, under "Intent → skill". The table sits in the knowledge-base folder next to this skill: `../../docs/ROUTING.md`.
2. If no intent matches, search the catalog by keyword:
   ```bash
   python3 ../../scripts/find_skill.py "<keywords>"
   ```
   This ranks enabled skills by how well their name and description match.
3. If several skills overlap, use the `primary` from `config/skills-config.yaml` → `overlaps`.
4. Load the chosen skill with `Skill(skill="<id>")`. Announce "Using <id> to <purpose>".
5. If the skill needs an MCP server (see ROUTING.md → MCP dependencies) and that server is down, tell the user and use the listed fallback.

## Rules

- Use only skills marked ✅ (enabled) in `docs/CATALOG.md`. ⬜ skills exist on disk but cannot be invoked.
- User instructions override routing.
- Do not load more than one skill from the same overlap group.
