---
name: skill-first
description: Check for and load a matching skill before acting, and use one primary skill per discipline
type: feedback
---

Before acting on any task, check `docs/ROUTING.md` or CLAUDE.md for a matching skill. Load it with the `Skill` tool and follow it. Load process skills (brainstorming, debugging, planning) before implementation skills.

**Why:** The user built this skills knowledge base so agents use the installed skills consistently instead of improvising.

**How to apply:** Announce "Using <skill> to <purpose>". If skills overlap, use the primary listed in `config/skills-config.yaml` → `overlaps`. Explicit user instructions win over skills.
