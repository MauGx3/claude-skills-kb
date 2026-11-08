# Skill Routing Guide

_Generated 2026-11-08T16:49:14+00:00 from `config/skills-config.yaml`._

Use this to pick a skill fast. **Use** = load first. **Then** = follow-on skills. **Alternates** = only if named by the user or the primary doesn't fit.

## Global rules

1. Check this routing table BEFORE acting. If a skill plausibly applies (even ~1%), load it with the Skill tool and follow it.
2. Process skills first (brainstorming, debugging, planning), then domain/implementation skills.
3. When several skills overlap, use the `primary` in `overlaps` below; use alternates only if the user names them or the primary does not fit.
4. User instructions (CLAUDE.md / AGENTS.md / direct request) override skills; skills override defaults.
5. Subagents dispatched for a specific task skip the meta/orientation skills (using-superpowers etc.).
6. Skills that depend on an MCP server (see `mcp_dependencies`) fail if that server is disconnected — tell the user and fall back.
7. Never answer Claude/Anthropic API, model or pricing questions from memory: load `claude-api`.
8. Before any chart/dashboard: load `dataviz`. Before any Artifact page: load `artifact-design` (or run Artifact quickstart).

## Intent → skill

⏸ = plugin off by default (`config/plugin-profile.yaml`: contentasoft-cad-converter, mattpocock-skills, research-superpowers, zizi-skills). When the primary is off, **Use** shows the first available fallback; re-enable the plugin per project to get the original.

| When the task is… | Use | Then | Alternates |
|---|---|---|---|
| New feature, idea or "let's build X" (before any code or plan mode) | `superpowers:brainstorming` | `superpowers:writing-plans` | `agent-protocols:idea-refine`, `agent-protocols:spec-driven-development`, `mattpocock-skills:grilling` ⏸, `zizi-skills:idea-refine` ⏸ |
| Write a spec / PRD before coding | `agent-protocols:spec-driven-development` | — | `agent-protocols:spec`, `zizi-skills:planning` ⏸ |
| Break work into tasks / implementation plan | `superpowers:writing-plans` | — | `agent-protocols:planning-and-task-breakdown`, `agent-protocols:plan`, `zizi-skills:planning` ⏸ |
| Execute an existing written plan | `superpowers:subagent-driven-development` | — | `superpowers:executing-plans`, `agent-protocols:incremental-implementation`, `agent-protocols:build` |
| Estimate effort / back-of-envelope numbers | `napkin-math:estimate` | — | `napkin-math:sanity-check` |
| Throwaway prototype / spike / PoC | `agent-protocols:research-spike-and-poc` (fallback; primary `mattpocock-skills:prototype` ⏸) | — | `agent-protocols:research-spike-and-poc` |
| Implementing any feature or bugfix with tests | `superpowers:test-driven-development` | — | `agent-protocols:test-driven-development`, `mattpocock-skills:tdd` ⏸, `zizi-skills:tdd-skill` ⏸, `agent-protocols:test` |
| Bug, failing test, unexpected behaviour | `superpowers:systematic-debugging` | — | `mattpocock-skills:diagnosing-bugs` ⏸, `agent-protocols:debugging-and-error-recovery`, `zizi-skills:debugging-and-error-recovery` ⏸ |
| About to claim "done" / "fixed" / "tests pass" | `superpowers:verification-before-completion` | — | `zizi-skills:done` ⏸ |
| Independent sub-tasks that can run in parallel | `superpowers:dispatching-parallel-agents` | — | `agent-army:agent-army`, `zizi-skills:orchestration` ⏸ |
| Isolated workspace for feature work | `superpowers:using-git-worktrees` | — | — |
| Finish a branch (merge / PR / cleanup) | `superpowers:finishing-a-development-branch` | — | `agent-protocols:git-workflow-and-versioning`, `zizi-skills:git-sync` ⏸ |
| Merge conflicts | `agent-protocols:git-workflow-and-versioning` (fallback; primary `mattpocock-skills:resolving-merge-conflicts` ⏸) | — | `agent-protocols:git-workflow-and-versioning` |
| API / interface / module boundary design | `agent-protocols:api-and-interface-design` | — | `mattpocock-skills:codebase-design` ⏸, `mattpocock-skills:domain-modeling` ⏸, `zizi-skills:service-architecture` ⏸ |
| Use official docs as source of truth for a library | `agent-protocols:source-driven-development` | — | `zizi-skills:source-driven-development` ⏸, `firecrawl:firecrawl-developer-index` |
| Frontend UI implementation (production quality) | `frontend-design:frontend-design` | — | `agent-protocols:frontend-ui-engineering`, `zizi-skills:frontend` ⏸, `modern-web-guidance:modern-web-guidance`, `zizi-skills:tabler-ui` ⏸ |
| Performance problem | `agent-protocols:performance-optimization` | — | `cloudflare:web-perf`, `zizi-skills:database-optimization` ⏸ |
| Security hardening of code | `agent-protocols:security-and-hardening` | — | `zizi-skills:security-and-hardening` ⏸, `security-review` |
| Deprecations / migrations | `agent-protocols:deprecation-and-migration` | — | `zizi-skills:deprecation-and-migration` ⏸ |
| i18n / localization | `agent-protocols:internationalization-and-localization` | — | `zizi-skills:i18n` ⏸ |
| CI/CD pipelines, release, launch checklist | `agent-protocols:ci-cd-and-automation` | — | `agent-protocols:ship`, `zizi-skills:infrastructure` ⏸ |
| Production incident / postmortem | `agent-protocols:incident-response-and-postmortems` | — | `zizi-skills:monitoring` ⏸ |
| ADRs / technical documentation | `agent-protocols:documentation-and-adrs` | — | `writing-skills:google-dev-docs` |
| Run the app / check a change in the real UI | `run` | — | `agent-protocols:browser-testing-with-devtools` |
| Building on the Claude API / Anthropic SDK / any LLM feature | `claude-api` | — | — |
| Qt / QML / C++ Qt | `qt-development-skills:qt-qml` | — | `qt-development-skills:qt-cmake-project`, `qt-development-skills:qt-qml-review`, `qt-development-skills:qt-cpp-review`, `qt-development-skills:qt-qml-test` |
| Cloudflare Workers / Durable Objects / Wrangler | `cloudflare:workers-best-practices` | — | `cloudflare:wrangler`, `cloudflare:durable-objects`, `cloudflare:agents-sdk`, `cloudflare:nextjs-on-cloudflare`, `cloudflare:cloudflare` |
| Chrome extension | `modern-web-guidance:chrome-extensions` | — | — |
| Sharpen or rewrite a prompt before running it | `prompt-sharpener:prompt-sharpener` | — | — |
| Vet a third-party skill, plugin or package before installing it | `vet-before-install:vet-before-install` | — | — |
| Full change delivery (plan, implement, verify, review, publish) | `agent-engineering:deliver-change` | — | `agent-engineering:plan-change`, `agent-engineering:implement-change`, `agent-engineering:verify-change`, `agent-engineering:review-change`, `agent-engineering:publish-change` |
| Review a diff / PR for bugs | `code-review` | — | `code-review:code-review`, `agent-protocols:code-review-and-quality`, `mattpocock-skills:code-review` ⏸, `zizi-skills:adversarial-review` ⏸, `superpowers:requesting-code-review` |
| Received review feedback to act on | `superpowers:receiving-code-review` | — | — |
| Simplify / clean up changed code | `simplify` | — | `agent-protocols:code-simplification`, `agent-protocols:code-simplify`, `zizi-skills:code-quality` ⏸ |
| Security review of branch / full repo scan | `security-review` | — | `agent-protocols:security-and-hardening` |
| Automated behaviour ("whenever X", "before/after X"), permissions, env vars | `update-config` | — | — |
| Reduce permission prompts | `fewer-permission-prompts` | — | — |
| Audit/optimize Claude Code setup | `setup-audit:setup-audit` | — | `claude-code-setup:claude-automation-recommender` |
| Create or improve a CLAUDE.md | `init` | — | `claude-md-management:claude-md-improver`, `claude-md-management:revise-claude-md` |
| Create / edit / evaluate a skill | `skill-creator:skill-creator` | — | `superpowers:writing-skills`, `anthropic-skills:skill-creator`, `firecrawl:skill-gen` |
| User states a lasting preference or corrects how Claude works | `task-observer:task-observer` | — | `task-observer:learn`, `adaptive-agent:build-user-profile` |
| Set up persistent project memory | `claude-memory:structured-memory` | — | `productivity:memory-management`, `agent-memory:memory-search` |
| Recurring / polling task | `loop` | — | — |
| Hand off work to another session/agent | `zizi-skills:handoff` ⏸ — enable `zizi-skills@synced` in the project | — | — |
| Usage / cost / impact report of Claude Code | `session-report:session-report` | — | `receipts:receipts` |
| Customize Claude's UI (status line, panel, hook) | `plugin-authoring` | — | — |
| Find which skill fits | `agent-protocols:using-agent-skills` (fallback; primary `zizi-skills:find-skills` ⏸) | — | `agent-protocols:using-agent-skills` |
| Web search for current facts | `firecrawl:firecrawl-search` | — | `tavily:tavily-search`, `exa:search` |
| Scrape / crawl / map a site | `firecrawl:firecrawl-scrape` | — | `firecrawl:firecrawl-crawl`, `firecrawl:firecrawl-map`, `firecrawl:firecrawl-download`, `firecrawl:firecrawl-interact` |
| Deep multi-source research report | `anthropic-skills:deep-research` | — | `tavily:tavily-research`, `firecrawl:firecrawl-agent`, `exa:exa-agent`, `auto-research:auto-research`, `mattpocock-skills:research` ⏸ |
| Academic papers (biomed / arXiv) | `firecrawl:firecrawl-research-index` | — | — |
| Scholarly project (humanities) end-to-end | `research-superpowers:using-research-powers` ⏸ — enable `research-superpowers@synced` in the project | `research-superpowers:brainstorming-research` ⏸, `research-superpowers:writing-research-plan` ⏸, `research-superpowers:literature-review` ⏸, `research-superpowers:acquire-sources` ⏸, `research-superpowers:ingest-source` ⏸, `research-superpowers:drafting-manuscript` ⏸, `research-superpowers:requesting-peer-review` ⏸ | — |
| Grant / funding | `research-superpowers:grant-finder` ⏸ — enable `research-superpowers@synced` in the project | — | `zizi-skills:grant-writing` ⏸ |
| Monitor a page/topic over time | `firecrawl:firecrawl-monitor` | — | `tavily:tavily-monitor` |
| Browser automation with interaction / login | `anthropic-skills:built-in-browser` | — | `anthropic-skills:chrome-browser`, `anthropic-skills:computer-use`, `agent-protocols:browser-testing-with-devtools` |
| Word .docx | `anthropic-skills:docx` | — | — |
| PDF read/create/fill/merge | `anthropic-skills:pdf` | — | `firecrawl:firecrawl-parse` |
| PowerPoint .pptx | `anthropic-skills:pptx` | — | `market-researcher:pptx-author` |
| Excel .xlsx | `anthropic-skills:xlsx` | — | — |
| Co-write a structured document | `anthropic-skills:doc-coauthoring` | — | `anthropic-skills:docs` |
| Google Docs/Sheets/Gmail/Calendar | `anthropic-skills:google-workspace` | — | — |
| Make AI-sounding text sound human | `humanizer:humanizer` | — | `humanize-kit:humanize`, `humanize-kit:humanize-ig`, `humanize-kit:voice-profiler` |
| Plain / professional writing style | `writing-skills:plain-language` | — | `writing-skills:business-writing`, `writing-skills:corporate-communication`, `writing-skills:orwells-rules`, `writing-skills:gov-uk-style`, `writing-skills:journalism-ap`, `writing-skills:asd-ste100`, `zizi-skills:plain-language` ⏸ |
| Fun persona voice | `writing-skills:yoda` | — | `writing-skills:jack-sparrow`, `writing-skills:shrek`, `writing-skills:ted-lasso`, `writing-skills:paddington`, `writing-skills:winnie-the-pooh`, `writing-skills:bob-ross`, `writing-skills:scott-adams` |
| Draft, outline or edit a document or email | `writing-desk:write-draft` | — | `writing-desk:write-outline`, `writing-desk:write-edit`, `writing-desk:write-email`, `writing-desk:write-review`, `writing-desk:write-refs` |
| Final pass to remove AI-sounding phrasing from text | `slop-stopper:final-review` | — | `humanizer:humanizer` |
| Terse output to save tokens | `caveman:caveman` | — | — |
| Writing prompts/docs for other agents | `agent-protocols:context-engineering` (fallback; primary `mattpocock-skills:writing-for-agents` ⏸) | — | `agent-protocols:context-engineering` |
| Status update / standup | `writing-skills:business-writing` (fallback; primary `zizi-skills:status-update` ⏸) | — | `writing-skills:business-writing` |
| Any chart / plot / dashboard | `dataviz` | — | `data:create-viz`, `data:build-dashboard`, `data:data-visualization` |
| Artifact web page | `artifact-design` | — | `artifact-diagramming`, `artifact-capabilities` |
| UI/UX design work (non-code) | `design-superpowers:design` | — | `superdesign:superdesign`, `design-skills:design-critique`, `design-skills:design-elevation`, `design-superpowers:design-review` |
| Design system | `design-skills:design-systems` | — | `design-superpowers:ds-make`, `design-superpowers:ds-manage`, `design-superpowers:ds-consumer`, `design-superpowers:ds-producer` |
| Accessibility audit | `design-skills:accessibility-audit` | — | — |
| UX research / journeys / IA / copy | `design-skills:ux-research` | — | `design-skills:journey-mapping`, `zizi-skills:information-architecture` ⏸, `design-skills:ux-writing`, `design-skills:ux-strategy`, `design-skills:interaction-design` |
| Cinematic / animated marketing website | `animatedwebs:animatedwebs-site` | — | `animatedwebs:animatedwebs-hero`, `animatedwebs:animatedwebs-backgrounds`, `animatedwebs:animatedwebs-components`, `animatedwebs:animatedwebs-style` |
| Generate images | `image-generation:image-generation` | — | `zizi-skills:design-assets` ⏸ |
| Figma | `design-superpowers:figma-setup` | — | `qt-development-skills:qt-figma-component-generation`, `qt-development-skills:qt-figma-token-extraction` |
| SQL query writing | `data:write-query` | — | `data:sql-queries` |
| Explore / analyze / validate a dataset | `data:analyze` | — | `data:explore-data`, `data:statistical-analysis`, `data:validate-data`, `zizi-skills:data-analytics` ⏸ |
| Accounting close / JE / recon / SOX | `finance:close-management` | — | `finance:journal-entry`, `finance:journal-entry-prep`, `finance:reconciliation`, `finance:sox-testing`, `finance:variance-analysis`, `finance:financial-statements`, `finance:audit-support` |
| Equity research note / earnings / thesis | `equity-research:earnings-analysis` | — | `equity-research:initiating-coverage`, `equity-research:thesis-tracker`, `equity-research:sector-overview`, `equity-research:idea-generation`, `equity-research:catalyst-calendar`, `lseg:equity-research`, `sp-global:tear-sheet` |
| Sector / competitive / comps research | `market-researcher:sector-overview` | — | `market-researcher:competitive-analysis`, `market-researcher:comps-analysis`, `market-researcher:idea-generation` |
| Rates / bonds / FX / options (LSEG data) | `lseg:macro-rates-monitor` | — | `lseg:bond-relative-value`, `lseg:bond-futures-basis`, `lseg:fx-carry-trade`, `lseg:option-vol-analysis`, `lseg:swap-curve-strategy`, `lseg:fixed-income-portfolio` |
| AI governance / regulation / vendor AI review | `ai-governance-legal:use-case-triage` | — | `ai-governance-legal:reg-gap-analysis`, `ai-governance-legal:vendor-ai-review`, `ai-governance-legal:aia-generation`, `ai-governance-legal:ai-inventory`, `ai-governance-legal:policy-starter`, `ai-governance-legal:policy-monitor` |
| Task tracking / daily start | `productivity:task-management` | — | `productivity:start`, `productivity:update`, `zizi-skills:project-manager` ⏸, `anthropic-skills:morning` |
| Notion | `Notion:search` | — | `Notion:find`, `Notion:create-page`, `Notion:create-task`, `Notion:database-query` |
| Obsidian / personal knowledge base | `obsidian-notes:obsidian-notes` | — | `desktop-commander:obsidian-vault`, `desktop-commander:knowledge-base` |
| Clean up video/audio | `video-cleanup:video-cleanup` | — | `ffmpeg-llm:ffmpeg-command` |
| Understand a video / YouTube | `watch-video:watch-video` | — | `youtube-transcriber:youtube-transcriber` |
| Career move / LinkedIn profile | `rankedin:next-career-move` | — | `rankedin:profile-review`, `github-portfolio-builder:github-portfolio-builder` |
| Salary raise, job change, hiring or fundraising advice | `superme:ask-for-a-raise` | — | `superme:change-jobs`, `superme:hire-someone`, `superme:fundraise` |
| Resume from a LinkedIn profile or old CV | `infinite-resume:resume-builder` | — | — |
| Learning / tutoring | `ai-mentor:mentor` | — | `anthropic-skills:learn` |
| Startup go-to-market | `zizi-skills:first-customers` ⏸ — enable `zizi-skills@synced` in the project | — | `zizi-skills:marketing` ⏸, `zizi-skills:app-store` ⏸ |

## Overlap resolution

Several plugins teach the same discipline. Default to the primary.

| Topic | Primary | Others (equivalent) |
|---|---|---|
| tdd | `superpowers:test-driven-development` | `agent-protocols:test-driven-development`, `mattpocock-skills:tdd` ⏸, `zizi-skills:tdd-skill` ⏸ |
| debugging | `superpowers:systematic-debugging` | `mattpocock-skills:diagnosing-bugs` ⏸, `agent-protocols:debugging-and-error-recovery`, `zizi-skills:debugging-and-error-recovery` ⏸ |
| planning | `superpowers:writing-plans` | `agent-protocols:planning-and-task-breakdown`, `zizi-skills:planning` ⏸ |
| ideation | `superpowers:brainstorming` | `agent-protocols:idea-refine`, `zizi-skills:idea-refine` ⏸, `mattpocock-skills:grilling` ⏸ |
| code review | `code-review` | `code-review:code-review`, `agent-protocols:code-review-and-quality`, `mattpocock-skills:code-review` ⏸, `zizi-skills:adversarial-review` ⏸ |
| simplification | `simplify` | `agent-protocols:code-simplification`, `zizi-skills:code-quality` ⏸ |
| security | `agent-protocols:security-and-hardening` | `zizi-skills:security-and-hardening` ⏸, `security-review` |
| web search | `firecrawl:firecrawl-search` | `tavily:tavily-search`, `exa:search` |
| deep research | `anthropic-skills:deep-research` | `tavily:tavily-research`, `firecrawl:firecrawl-agent`, `exa:exa-agent`, `auto-research:auto-research` |
| humanize | `humanizer:humanizer` | `humanize-kit:humanize` |
| plain language | `writing-skills:plain-language` | `zizi-skills:plain-language` ⏸ |
| skill authoring | `skill-creator:skill-creator` | `superpowers:writing-skills`, `anthropic-skills:skill-creator` |
| frontend | `frontend-design:frontend-design` | `agent-protocols:frontend-ui-engineering`, `zizi-skills:frontend` ⏸ |
| memory | `claude-memory:structured-memory` | `productivity:memory-management`, `agent-memory:memory-search` |
| sector report | `market-researcher:sector-overview` | `equity-research:sector-overview` |

## MCP dependencies

Connected this session: Firecrawl, Figma, Claude_Docs, Google Drive (ai-governance-legal), playwright, browser-use, desktop-commander.

Failed this session: context7, exa, github, Notion, slack, asana, atlassian, clickup, linear, monday, amplitude, bigquery, definite, hex, lseg, spglobal, vanguard-advisors, cloudflare, animatedwebs, rankedin, resumenext-linkedin-resume, qt-docs, abracadabrax-image-video, agent-memory, cad-converter.

| Skills | Needs MCP server |
|---|---|
| `lseg:*` | lseg |
| `sp-global:*` | spglobal |
| `vanguard-advisor-tools:*` | vanguard-advisors |
| `Notion:*` | notion |
| `animatedwebs:*` | animatedwebs |
| `rankedin:*` | rankedin |
| `exa:*` | exa (fallback: firecrawl) |
| `agent-memory:memory-search` | agent-memory |
| `contentasoft-cad-converter:contenta-cad` | cad-converter |
| `data:* (warehouse queries)` | bigquery / snowflake / databricks / hex / amplitude |
| `productivity:*` | asana / linear / slack / notion / atlassian ... |
| `finance:*` | bigquery / snowflake / gmail / slack (optional) |

> Failures in the cloud sandbox are usually the network proxy (403) — allow the host in the environment or run locally.

## Subagents

| Agent type | Purpose |
|---|---|
| `adhd-study-coach:adhd-study-coach` | Your ongoing ADHD-friendly study companion, for any subject. Use this to start a study session, review what's due, learn something new, wrap up and reflect, or check in on your le… |
| `agent-protocols:accessibility-specialist` | Accessibility engineer focused on WCAG-oriented review, keyboard and screen reader flows, and inclusive UI. Use when auditing components, fixing a11y bugs, or defining acceptance … |
| `agent-protocols:code-reviewer` | Senior code reviewer that evaluates changes across five dimensions -- correctness, readability, architecture, security, and performance. Use for thorough code review before merge. |
| `agent-protocols:documentation-specialist` | Technical writer focused on ADRs, API docs, and reader-first explanations. Use when drafting architecture decisions, public APIs, runbooks, or improving unclear technical document… |
| `agent-protocols:performance-engineer` | Performance engineer focused on measurement-first analysis, profiling, and regressions. Use when optimizing hot paths, investigating slowness, or validating Core Web Vitals and ba… |
| `agent-protocols:release-engineer` | Release and platform engineer focused on CI/CD pipelines, deployment safety, and launch readiness. Use when designing pipelines, staging rollouts, rollbacks, or pre-launch checkli… |
| `agent-protocols:security-auditor` | Security engineer focused on vulnerability detection, threat modeling, and secure coding practices. Use for security-focused code review, threat analysis, or hardening recommendat… |
| `agent-protocols:spec-analyst` | Product-minded analyst focused on PRD quality, scope boundaries, and testable acceptance criteria. Use when refining a vague idea, reviewing a spec before build, or de-risking unc… |
| `agent-protocols:test-engineer` | QA engineer specialized in test strategy, test writing, and coverage analysis. Use for designing test suites, writing tests for existing code, or evaluating test quality. |
| `claude-security:claude-security` | The dedicated Claude Security orchestrator. Hand it an unattended job — "fully scan this repository and patch what you find; I understand it will use a lot of tokens" — and it run… |
| `claude-security:explore` | Read-only code explorer that the plugin's other agents dispatch to map a codebase — locate files, trace how a flow is wired, find every caller of a symbol, answer "where does X ha… |
| `claude-security:patch-generator` | Implements the fix for one finding inside a scratch workspace clone, staged for review and delivery as a patch file; dispatched by the fix job, not for direct invocation. |
| `claude-security:patch-verifier` | The single verifier per fix round — reviews the workspace's staged diff against the finding, runs the tests, and states the three confidence claims a patch file must earn; dispatc… |
| `claude-security:scan-inventory` | Restricted read-only repository cartographer dispatched by the Claude Security scan workflow to partition the tree into components and account for every top-level directory; not f… |
| `claude-security:scan-loader` | Restricted read-only loader dispatched by the Claude Security scan workflow to return one candidates file from the run directory; not for direct invocation. |
| `claude-security:scan-researcher` | Restricted read-only vulnerability researcher dispatched by the Claude Security scan workflow; not for direct invocation or general exploration. |
| `claude-security:scan-verifier` | Restricted read-only verifier dispatched by the Claude Security scan workflow to vote on one candidate finding; not for direct invocation. |
| `code-simplifier:code-simplifier` | Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. Focuses on recently modified code unless instructed otherwise. |
| `ffmpeg-llm:ffmpeg-expert` | Use when an FFmpeg task needs deep analysis — diagnosing failed commands, optimizing encoder settings for size/quality tradeoffs, or designing complex filtergraphs with multiple i… |
| `market-researcher:market-researcher` | Produces sector or thematic market research — industry overview, competitive landscape, trading-comps spread of the peer set, and a thematic ideas shortlist — packaged as a resear… |
| `research-superpowers:analyst` | Dispatched by executing-research-plan for analysis tasks. Writes and runs Python/R scripts in output/data-analysis/, produces reproducible results with assumption checks. Fresh co… |
| `research-superpowers:drafter` | Dispatched by drafting-manuscript for one section whose argument sketch has been approved. Produces that section's prose from named synthesis + source pages, with inline citations… |
| `research-superpowers:literature-scout` | Dispatched by literature-review skill. Executes database queries across OpenAlex, IxTheo, Zenon-DAI, Propylaeum, Persée, OpenEdition, CORE, BASE, Crossref, DNB, arXiv. Returns gra… |
| `research-superpowers:peer-reviewer` | Dispatched by requesting-peer-review. Reviews a manuscript in one of two roles — constructive or adversarial — and produces a structured review report. Fresh context per dispatch. |
| `research-superpowers:source-acquirer` | Dispatched by acquire-sources for large worklists (≥ ~8 sources). Runs the resolve→curl→validate download batch for the A+B graded sources and returns a compact status table. Isol… |
| `research-superpowers:source-ingester` | Dispatched by ingest-source or executing-research-plan. Reads ONE source PDF/text under a specific focus and produces a focus-driven Source page + entity pages + BibTeX entry + lo… |
| `research-superpowers:wiki-linter` | Dispatched by wiki-lint for large wikis (>50 pages) or heavy cleanup. Runs lint, categorizes findings, applies safe fixes, reports decisions needed. Fresh context per dispatch. |
