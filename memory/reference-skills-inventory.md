---
name: skills-inventory
description: Inventory of installed Claude Code skills, plugins, commands and subagents, with on-disk locations
type: reference
---

As of 2026-11-08 the account has **89 plugins**, **494 skills** catalogued, and **430 skills enabled** for the
`Skill` tool. There are also **49 slash commands** and **27 subagents**.

Where the files live in a Claude Code cloud session:
- Plugin skills: `/root/.claude/plugins/synced/<account>/<plugin-uuid>/skills/<name>/SKILL.md`. The ID is `<plugin>:<dir-name>`.
- Anthropic skills synced from claude.ai: `/root/.claude/skills/synced/...`. The ID is `anthropic-skills:<name>` (docx, pdf, pptx, xlsx, deep-research, doc-coauthoring, google-workspace, built-in-browser, chrome-browser, computer-use, learn, morning, import-memory, artifact-emulator, docs, skill-creator).
- Anthropic library copies: `/mnt/skills/public` and `/mnt/skills/examples`. Most are claude.ai-only and not enabled in Claude Code.
- Built-in harness skills (no SKILL.md on disk): dataviz, artifact-design, artifact-diagramming, artifact-capabilities, update-config, keybindings-help, code-review, simplify, fewer-permission-prompts, loop, claude-api, run, plugin-authoring, init, security-review.

Largest plugins by skill count: mattpocock-skills (38 on disk, 11 enabled), zizi-skills (36), agent-protocols (25 + 7 commands + 8 agents), writing-skills (17), research-superpowers (17 + 7 agents), superpowers (15), cloudflare (14), qt-development-skills (13), firecrawl (12).

Full list: `docs/CATALOG.md`. Machine-readable list: `catalog/skills-catalog.json`.
