# Skills Memory — how to use the installed skills

Drop this file into a project root (or merge into `~/.claude/CLAUDE.md`) so every
Claude Code session knows which skill to load. Full detail: `docs/ROUTING.md`
(intent → skill), `docs/CATALOG.md` (all 387 skills), `catalog/skills-catalog.json`
(machine-readable).

## Operating rules

1. Before acting on any task, check the table below. If a skill could apply, load
   it with `Skill(skill="<id>")` and follow it. Say "Using <skill> to <purpose>".
2. Process skills come first (brainstorm, debug, plan), then implementation skills.
3. When skills overlap, use the **primary** listed here. Use an alternate only when
   the user names it.
4. User instructions override skills. Skills override defaults.
5. A subagent dispatched for one task skips orientation skills like `using-superpowers`.
6. A skill that needs a disconnected MCP server will fail. Tell the user and fall back.
7. Never answer Claude API, model or pricing questions from memory. Load `claude-api`.
8. Load `dataviz` before any chart. Load `artifact-design` before any Artifact page.

## Primary skill per task

| Task | Skill |
|---|---|
| New feature or idea, before code or plan mode | `superpowers:brainstorming` → `superpowers:writing-plans` |
| Spec or PRD | `agent-protocols:spec-driven-development` |
| Execute a written plan | `superpowers:subagent-driven-development` (or `superpowers:executing-plans`) |
| Write code or fix a bug, with tests | `superpowers:test-driven-development` |
| Bug, failure or unexpected behaviour | `superpowers:systematic-debugging` |
| Before saying "done" or "fixed" | `superpowers:verification-before-completion` |
| Run independent tasks in parallel | `superpowers:dispatching-parallel-agents` |
| Finish a branch, merge or PR | `superpowers:finishing-a-development-branch` |
| Review a diff or PR | `code-review` (built-in) |
| Act on review feedback | `superpowers:receiving-code-review` |
| Simplify changed code | `simplify` |
| Security review | `security-review`, or `agent-protocols:security-and-hardening` |
| Full-repo security scan | subagent `claude-security:claude-security` |
| API or interface design | `agent-protocols:api-and-interface-design` |
| Frontend UI | `frontend-design:frontend-design` |
| Run the app, see a change work | `run` |
| Build on Claude or Anthropic SDK | `claude-api` |
| Qt or QML | `qt-development-skills:qt-qml` (+ review and test skills) |
| Cloudflare Workers | `cloudflare:workers-best-practices` |
| Hooks, permissions, env vars ("whenever X") | `update-config` |
| Audit Claude Code setup | `setup-audit:setup-audit` |
| Create or improve CLAUDE.md | `init` / `claude-md-management:claude-md-improver` |
| Create or edit a skill | `skill-creator:skill-creator` |
| User states a lasting preference | `task-observer:task-observer` |
| Persistent project memory | `claude-memory:structured-memory` |
| Recurring or polling task | `loop` |
| Web search | `firecrawl:firecrawl-search` (alternates: tavily, exa) |
| Scrape, crawl or map a site | `firecrawl:firecrawl-scrape` / `-crawl` / `-map` |
| Deep research report | `anthropic-skills:deep-research` |
| Academic papers (biomed, arXiv) | `firecrawl:firecrawl-research-index` |
| Humanities research project | `research-superpowers:using-research-powers` (phased workflow) |
| .docx / .pdf / .pptx / .xlsx | `anthropic-skills:docx` / `pdf` / `pptx` / `xlsx` |
| Co-write a document | `anthropic-skills:doc-coauthoring` |
| Google Workspace | `anthropic-skills:google-workspace` |
| Browser automation | `anthropic-skills:built-in-browser` (or `chrome-browser`, `computer-use`) |
| Make AI text sound human | `humanizer:humanizer` |
| Plain or business writing | `writing-skills:plain-language` / `business-writing` |
| Charts or dashboards | `dataviz` (+ `data:create-viz`, `data:build-dashboard`) |
| UI/UX design | `design-superpowers:design`; design systems: `design-skills:design-systems` |
| Accessibility audit | `design-skills:accessibility-audit` |
| Animated marketing site | `animatedwebs:animatedwebs-site` |
| Images | `image-generation:image-generation` |
| SQL | `data:write-query` |
| Analyze a dataset | `data:analyze` |
| Accounting (close, JE, recon, SOX) | `finance:close-management` and siblings |
| Equity research | `equity-research:earnings-analysis` / `initiating-coverage` |
| Sector or competitor research | `market-researcher:sector-overview` |
| Rates, FX, options | `lseg:*` (needs the LSEG MCP) |
| AI governance and regulation | `ai-governance-legal:use-case-triage` |
| Tasks and daily planning | `productivity:task-management` |
| Notion | `Notion:search` (needs the Notion MCP) |
| Obsidian notes | `obsidian-notes:obsidian-notes` |
| Video or audio cleanup | `video-cleanup:video-cleanup` |
| Understand a video or YouTube link | `watch-video:watch-video` |
| Estimate effort or numbers | `napkin-math:estimate` |
| Hand off to another session | `zizi-skills:handoff` |
| Not sure which skill fits | `zizi-skills:find-skills`, or read `docs/ROUTING.md` |

## Useful subagents (`Agent(subagent_type=...)`)

- Engineering: `agent-protocols:code-reviewer`, `test-engineer`, `security-auditor`,
  `performance-engineer`, `spec-analyst`, `documentation-specialist`,
  `release-engineer`, `accessibility-specialist`, `code-simplifier:code-simplifier`.
- Research: `research-superpowers:literature-scout`, `source-ingester`, `analyst`,
  `drafter`, `peer-reviewer`. Markets: `market-researcher:market-researcher`.
- Built-in: `Explore` (read-only search), `Plan`, `general-purpose`, `claude-code-guide`.

## Keeping this current

Run these after adding or removing plugins:

    python3 scripts/build_catalog.py
    python3 scripts/render_docs.py

The second script fails if a routed skill ID no longer exists.
