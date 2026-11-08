---
name: skills-kb-maintenance
description: How to regenerate the skills catalog and docs after plugins change
type: project
---

The knowledge base lives in the `claude-skills-kb/` folder. After adding or removing plugins:

1. Update `catalog/enabled-skills.txt` from the skill list the session shows the model.
2. Run `python3 scripts/build_catalog.py` **only on a machine that has the full synced plugin set**. It rebuilds `catalog/skills-catalog.json` from disk, so on a laptop with only a few plugins in `~/.claude/plugins/cache` it drops most of the catalog. On 2026-11-08 the new plugins were merged in by hand instead (existing records were checked unchanged).
3. Run `python3 scripts/render_docs.py`. It writes `docs/CATALOG.md` and `docs/ROUTING.md`, and exits with an error if a routed ID is missing or disabled.
4. Edit routing in `config/skills-config.yaml` and plugin on/off choices in `config/plugin-profile.yaml`. Never edit the generated docs or AGENTS.md by hand.
5. Run `python3 -m unittest discover -s tests`. CI runs the same checks on Ubuntu and macOS and fails if the generated docs are stale. `install.sh` calls a bare `python3`, and the tests set `HOME` to a temp dir, so PyYAML must be visible from the system site-packages or the user base (set `PYTHONUSERBASE`).
6. Keep `CLAUDE.md` under 2,500 chars: it loads in every session. `render_docs.py` enforces the limit.

**Why:** Plugins change often, so the catalog has to be regenerated rather than kept by hand.
