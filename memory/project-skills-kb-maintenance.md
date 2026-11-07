---
name: skills-kb-maintenance
description: How to regenerate the skills catalog and docs after plugins change
type: project
---

The knowledge base lives in the `claude-skills-kb/` folder. After adding or removing plugins:

1. Update `catalog/enabled-skills.txt` from the skill list the session shows the model.
2. Run `python3 scripts/build_catalog.py`. It scans the plugin, user and Anthropic skill folders and writes `catalog/skills-catalog.json`.
3. Run `python3 scripts/render_docs.py`. It writes `docs/CATALOG.md` and `docs/ROUTING.md`, and exits with an error if a routed ID is missing or disabled.
4. Edit routing in `config/skills-config.yaml`. Never edit the generated docs by hand.

**Why:** Plugins change often, so the catalog has to be regenerated rather than kept by hand.
