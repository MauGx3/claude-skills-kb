# Skill routing for Claude chat and Cowork

_Generated 2026-11-07T17:48:33+00:00 by `scripts/render_docs.py` from `config/skills-config.yaml`._

Use the **Use** skill first. Use an alternate only when the person names it or the first doesn't fit.
Skills are listed only if they are available in chat; Claude Code-only tools are left out.

| When the task is… | Use | Alternates |
|---|---|---|
| New feature, idea or "let's build X" (before any code or plan mode) | `superpowers:brainstorming` | `agent-protocols:idea-refine`, `agent-protocols:spec-driven-development`, `mattpocock-skills:grilling` |
| Write a spec / PRD before coding | `agent-protocols:spec-driven-development` | `zizi-skills:planning` |
| Break work into tasks / implementation plan | `superpowers:writing-plans` | `agent-protocols:planning-and-task-breakdown`, `zizi-skills:planning` |
| Execute an existing written plan | `superpowers:subagent-driven-development` | `superpowers:executing-plans`, `agent-protocols:incremental-implementation` |
| Estimate effort / back-of-envelope numbers | `napkin-math:estimate` | `napkin-math:sanity-check` |
| Throwaway prototype / spike / PoC | `mattpocock-skills:prototype` | `agent-protocols:research-spike-and-poc` |
| Implementing any feature or bugfix with tests | `superpowers:test-driven-development` | `agent-protocols:test-driven-development`, `mattpocock-skills:tdd`, `zizi-skills:tdd-skill` |
| Bug, failing test, unexpected behaviour | `superpowers:systematic-debugging` | `mattpocock-skills:diagnosing-bugs`, `agent-protocols:debugging-and-error-recovery`, `zizi-skills:debugging-and-error-recovery` |
| About to claim "done" / "fixed" / "tests pass" | `superpowers:verification-before-completion` | `zizi-skills:done` |
| Independent sub-tasks that can run in parallel | `superpowers:dispatching-parallel-agents` | `agent-army:agent-army`, `zizi-skills:orchestration` |
| Isolated workspace for feature work | `superpowers:using-git-worktrees` | — |
| Finish a branch (merge / PR / cleanup) | `superpowers:finishing-a-development-branch` | `agent-protocols:git-workflow-and-versioning`, `zizi-skills:git-sync` |
| Merge conflicts | `mattpocock-skills:resolving-merge-conflicts` | `agent-protocols:git-workflow-and-versioning` |
| API / interface / module boundary design | `agent-protocols:api-and-interface-design` | `mattpocock-skills:codebase-design`, `mattpocock-skills:domain-modeling`, `zizi-skills:service-architecture` |
| Use official docs as source of truth for a library | `agent-protocols:source-driven-development` | `zizi-skills:source-driven-development`, `firecrawl:firecrawl-developer-index` |
| Frontend UI implementation (production quality) | `frontend-design:frontend-design` | `agent-protocols:frontend-ui-engineering`, `zizi-skills:frontend`, `modern-web-guidance:modern-web-guidance` |
| Performance problem | `agent-protocols:performance-optimization` | `cloudflare:web-perf`, `zizi-skills:database-optimization` |
| Security hardening of code | `agent-protocols:security-and-hardening` | `zizi-skills:security-and-hardening` |
| Deprecations / migrations | `agent-protocols:deprecation-and-migration` | `zizi-skills:deprecation-and-migration` |
| i18n / localization | `agent-protocols:internationalization-and-localization` | `zizi-skills:i18n` |
| CI/CD pipelines, release, launch checklist | `agent-protocols:ci-cd-and-automation` | `agent-protocols:shipping-and-launch`, `zizi-skills:infrastructure` |
| Production incident / postmortem | `agent-protocols:incident-response-and-postmortems` | `zizi-skills:monitoring` |
| ADRs / technical documentation | `agent-protocols:documentation-and-adrs` | `writing-skills:google-dev-docs` |
| Run the app / check a change in the real UI | `agent-protocols:browser-testing-with-devtools` | — |
| Qt / QML / C++ Qt | `qt-development-skills:qt-qml` | `qt-development-skills:qt-cmake-project`, `qt-development-skills:qt-qml-review`, `qt-development-skills:qt-cpp-review` |
| Cloudflare Workers / Durable Objects / Wrangler | `cloudflare:workers-best-practices` | `cloudflare:wrangler`, `cloudflare:durable-objects`, `cloudflare:agents-sdk` |
| Chrome extension | `modern-web-guidance:chrome-extensions` | — |
| Review a diff / PR for bugs | `agent-protocols:code-review-and-quality` | `mattpocock-skills:code-review`, `zizi-skills:adversarial-review`, `superpowers:requesting-code-review` |
| Received review feedback to act on | `superpowers:receiving-code-review` | — |
| Simplify / clean up changed code | `agent-protocols:code-simplification` | `zizi-skills:code-quality` |
| Security review of branch / full repo scan | `agent-protocols:security-and-hardening` | — |
| Audit/optimize Claude Code setup | `setup-audit:setup-audit` | `claude-code-setup:claude-automation-recommender` |
| Create or improve a CLAUDE.md | `claude-md-management:claude-md-improver` | — |
| Create / edit / evaluate a skill | `skill-creator:skill-creator` | `superpowers:writing-skills`, `anthropic-skills:skill-creator` |
| User states a lasting preference or corrects how Claude works | `task-observer:task-observer` | `adaptive-agent:build-user-profile` |
| Set up persistent project memory | `claude-memory:structured-memory` | `productivity:memory-management`, `agent-memory:memory-search` |
| Hand off work to another session/agent | `zizi-skills:handoff` | — |
| Usage / cost / impact report of Claude Code | `session-report:session-report` | `receipts:receipts` |
| Find which skill fits | `zizi-skills:find-skills` | `agent-protocols:using-agent-skills` |
| Web search for current facts | `firecrawl:firecrawl-search` | `tavily:tavily-search`, `exa:search` |
| Scrape / crawl / map a site | `firecrawl:firecrawl-scrape` | `firecrawl:firecrawl-crawl`, `firecrawl:firecrawl-map`, `firecrawl:firecrawl-download` |
| Deep multi-source research report | `anthropic-skills:deep-research` | `tavily:tavily-research`, `firecrawl:firecrawl-agent`, `exa:exa-agent` |
| Academic papers (biomed / arXiv) | `firecrawl:firecrawl-research-index` | — |
| Scholarly project (humanities) end-to-end | `research-superpowers:using-research-powers` | — |
| Grant / funding | `research-superpowers:grant-finder` | `zizi-skills:grant-writing` |
| Monitor a page/topic over time | `firecrawl:firecrawl-monitor` | `tavily:tavily-monitor` |
| Browser automation with interaction / login | `anthropic-skills:built-in-browser` | `anthropic-skills:chrome-browser`, `anthropic-skills:computer-use`, `agent-protocols:browser-testing-with-devtools` |
| Word .docx | `anthropic-skills:docx` | — |
| PDF read/create/fill/merge | `anthropic-skills:pdf` | `firecrawl:firecrawl-parse` |
| PowerPoint .pptx | `anthropic-skills:pptx` | `market-researcher:pptx-author` |
| Excel .xlsx | `anthropic-skills:xlsx` | — |
| Co-write a structured document | `anthropic-skills:doc-coauthoring` | `anthropic-skills:docs` |
| Google Docs/Sheets/Gmail/Calendar | `anthropic-skills:google-workspace` | — |
| Make AI-sounding text sound human | `humanizer:humanizer` | `humanize-kit:humanize`, `humanize-kit:humanize-ig`, `humanize-kit:voice-profiler` |
| Plain / professional writing style | `writing-skills:plain-language` | `writing-skills:business-writing`, `writing-skills:corporate-communication`, `writing-skills:orwells-rules` |
| Fun persona voice | `writing-skills:yoda` | `writing-skills:jack-sparrow`, `writing-skills:shrek`, `writing-skills:ted-lasso` |
| Terse output to save tokens | `caveman:caveman` | — |
| Writing prompts/docs for other agents | `mattpocock-skills:writing-for-agents` | `agent-protocols:context-engineering` |
| Status update / standup | `zizi-skills:status-update` | `writing-skills:business-writing` |
| Any chart / plot / dashboard | `data:create-viz` | `data:build-dashboard`, `data:data-visualization` |
| UI/UX design work (non-code) | `design-superpowers:design` | `superdesign:superdesign`, `design-skills:design-critique`, `design-skills:design-elevation` |
| Design system | `design-skills:design-systems` | `design-superpowers:ds-make`, `design-superpowers:ds-manage`, `design-superpowers:ds-consumer` |
| Accessibility audit | `design-skills:accessibility-audit` | — |
| UX research / journeys / IA / copy | `design-skills:ux-research` | `design-skills:journey-mapping`, `zizi-skills:information-architecture`, `design-skills:ux-writing` |
| Cinematic / animated marketing website | `animatedwebs:animatedwebs-site` | `animatedwebs:animatedwebs-hero`, `animatedwebs:animatedwebs-backgrounds`, `animatedwebs:animatedwebs-components` |
| Generate images | `image-generation:image-generation` | `zizi-skills:design-assets` |
| Figma | `design-superpowers:figma-setup` | `qt-development-skills:qt-figma-component-generation`, `qt-development-skills:qt-figma-token-extraction` |
| SQL query writing | `data:write-query` | `data:sql-queries` |
| Explore / analyze / validate a dataset | `data:analyze` | `data:explore-data`, `data:statistical-analysis`, `data:validate-data` |
| Accounting close / JE / recon / SOX | `finance:close-management` | `finance:journal-entry`, `finance:journal-entry-prep`, `finance:reconciliation` |
| Equity research note / earnings / thesis | `equity-research:earnings-analysis` | `equity-research:initiating-coverage`, `equity-research:thesis-tracker`, `equity-research:sector-overview` |
| Sector / competitive / comps research | `market-researcher:sector-overview` | `market-researcher:competitive-analysis`, `market-researcher:comps-analysis`, `market-researcher:idea-generation` |
| Rates / bonds / FX / options (LSEG data) | `lseg:macro-rates-monitor` | `lseg:bond-relative-value`, `lseg:bond-futures-basis`, `lseg:fx-carry-trade` |
| AI governance / regulation / vendor AI review | `ai-governance-legal:use-case-triage` | `ai-governance-legal:reg-gap-analysis`, `ai-governance-legal:vendor-ai-review`, `ai-governance-legal:aia-generation` |
| Task tracking / daily start | `productivity:task-management` | `productivity:start`, `productivity:update`, `zizi-skills:project-manager` |
| Obsidian / personal knowledge base | `obsidian-notes:obsidian-notes` | `desktop-commander:obsidian-vault`, `desktop-commander:knowledge-base` |
| Clean up video/audio | `video-cleanup:video-cleanup` | `ffmpeg-llm:ffmpeg-command` |
| Understand a video / YouTube | `watch-video:watch-video` | `youtube-transcriber:youtube-transcriber` |
| Career move / LinkedIn profile | `rankedin:next-career-move` | `rankedin:profile-review`, `github-portfolio-builder:github-portfolio-builder` |
| Learning / tutoring | `ai-mentor:mentor` | `anthropic-skills:learn` |
| Startup go-to-market | `zizi-skills:first-customers` | `zizi-skills:marketing`, `zizi-skills:app-store` |

## Overlaps

When several skills teach the same thing, use the primary:

- tdd: `superpowers:test-driven-development`
- debugging: `superpowers:systematic-debugging`
- planning: `superpowers:writing-plans`
- ideation: `superpowers:brainstorming`
- security: `agent-protocols:security-and-hardening`
- web search: `firecrawl:firecrawl-search`
- deep research: `anthropic-skills:deep-research`
- humanize: `humanizer:humanizer`
- plain language: `writing-skills:plain-language`
- skill authoring: `skill-creator:skill-creator`
- frontend: `frontend-design:frontend-design`
- memory: `claude-memory:structured-memory`
- sector report: `market-researcher:sector-overview`

_Left out (Claude Code only): Building on the Claude API / Anthropic SDK / any LLM feature, Automated behaviour ("whenever X", "before/after X"), permissions, env vars, Reduce permission prompts, Recurring / polling task, Customize Claude's UI (status line, panel, hook), Artifact web page, Notion._
