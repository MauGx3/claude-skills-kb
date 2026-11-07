---
name: skill-routing
description: Which skill to load for a given task type, and the primary choice when several plugins overlap
type: reference
---

Primary skill per discipline (use the others only when the user names them):
- Ideation: `superpowers:brainstorming`. Planning: `superpowers:writing-plans`. Executing a plan: `superpowers:subagent-driven-development`.
- TDD: `superpowers:test-driven-development`. Debugging: `superpowers:systematic-debugging`. Before claiming done: `superpowers:verification-before-completion`.
- Code review: `code-review` (built-in). Simplify: `simplify`. Security: `agent-protocols:security-and-hardening` / `security-review`.
- Frontend: `frontend-design:frontend-design`. Charts: `dataviz`. Artifact pages: `artifact-design`.
- Web search: `firecrawl:firecrawl-search`. Deep research: `anthropic-skills:deep-research`.
- Office files: `anthropic-skills:{docx,pdf,pptx,xlsx}`.
- Humanize text: `humanizer:humanizer`. Plain language: `writing-skills:plain-language`.
- Skill authoring: `skill-creator:skill-creator`. Memory: `claude-memory:structured-memory`.
- Claude API work: `claude-api`, always. Settings and hooks: `update-config`.

Off by default (config/plugin-profile.yaml): zizi-skills, mattpocock-skills, research-superpowers, contentasoft-cad-converter. To use one in a project, add `{"enabledPlugins": {"<name>@synced": true}}` to that project's `.claude/settings.json`.

**Why:** Overlapping plugins (superpowers, agent-protocols, mattpocock-skills, zizi-skills) teach the same disciplines in different ways. Picking one primary keeps behaviour consistent.

**How to apply:** Look up the task in `docs/ROUTING.md` (88 intents), then load the "Use" skill.
