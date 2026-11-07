# Skills Catalog

_Generated 2026-11-07T17:48:33+00:00 by `scripts/render_docs.py` — do not edit by hand; edit `config/` and re-run._

**75 plugins · 387 skills (323 enabled in Claude Code) · 49 slash commands · 27 subagents**

Legend: ✅ invocable via `Skill` tool in Claude Code · ⏸ plugin turned off by `config/plugin-profile.yaml` (re-enable per project) · ⬜ present on disk but not exposed (disabled, in-progress, or claude.ai-only library skill).

Invoke: `Skill(skill="<id>")` — or type `/<id>` as the user.

## Contents

- [Meta / orchestration / skill system](#meta--orchestration--skill-system)
- [Software engineering lifecycle](#software-engineering-lifecycle)
- [Language / platform specific](#language--platform-specific)
- [Frontend, UI & design](#frontend-ui--design)
- [Web search, scraping & browsing](#web-search-scraping--browsing)
- [Academic research & writing](#academic-research--writing)
- [Writing, tone & humanizing](#writing-tone--humanizing)
- [Documents & office files](#documents--office-files)
- [Data & analytics](#data--analytics)
- [Finance & markets](#finance--markets)
- [Legal & governance](#legal--governance)
- [Productivity, notes & memory](#productivity-notes--memory)
- [Media (video/audio)](#media-videoaudio)
- [Career & personal](#career--personal)

## Meta / orchestration / skill system

### Built-in (Claude Code harness)

| Skill | Enabled | What it does |
|---|---|---|
| `fewer-permission-prompts` | ✅ | Scan transcripts for common read-only Bash/MCP calls and add a prioritized allowlist to project .claude/settings.json. |
| `init` | ✅ | Initialize a CLAUDE.md for the current repository by analysing the codebase. |
| `keybindings-help` | ✅ | Customize keyboard shortcuts / chord bindings in ~/.claude/keybindings.json. |
| `loop` | ✅ | Run a prompt or slash command on a recurring interval (/loop 5m /foo) or self-paced. Not for one-off tasks. |
| `plugin-authoring` | ✅ | Make or debug a 'mod': a change to Claude's own interface/behaviour — side panel, band, status line, toast, slash command, or tool-call hook. |
| `update-config` | ✅ | Configure the Claude Code harness via settings.json: hooks for automated behaviours ('whenever X', 'before/after X'), permissions, env vars, hook troubleshooting. |

### adaptive-agent

_Make your AI agent get stronger with use — skill self-improvement, memory-skill feedback loops, and user profiling. Inspired by Hermes Agent's four-layer memory architecture._

Source: https://github.com/truenorth-lj/adaptive-agent-skill

| Skill | | Description |
|---|---|---|
| `adaptive-agent:build-user-profile` | ✅ | Build or update the user profile memory by observing workspace context, git history, and conversation patterns. Run on first interaction or when profile feels outdated. Trigger words: "build profile", "update profile", … |
| `adaptive-agent:skill-review` | ✅ | Review all skills for staleness, missing gotchas, and improvement opportunities. Run periodically or after a series of tasks to keep procedural memory accurate. Trigger words: "review skills", "skill audit", "check skil… |

### agent-army `v1.0.0`

_Deploy a 2-layer parallel agent hierarchy for large, parallelizable work: big refactors, multi-file migrations, codebase-wide audits, and bulk generation. Pick an army size and power level; includes git checkpoints, a pre-deploy gate, phantom-completion checks, and multi-wave follow-up._

Source: https://github.com/OneWave-AI/claude-skills/tree/main/plugins/agent-army

| Skill | | Description |
|---|---|---|
| `agent-army:agent-army` | ✅ | Deploy a 2-layer parallel agent hierarchy for large, parallelizable work — big refactors, multi-file migrations, codebase-wide audits, bulk generation. A top-tier commander (Fable or Opus) orchestrates the swarms; the u… |

### agent-discussion `v0.1.0`

_Coordinate multi-agent debates across different AI platforms (Claude Code, Antigravity, Copilot, Gemini CLI, etc.) using a shared file protocol. Each agent reads one skill and handles everything autonomously — intros, turn-taking, and consensus._

Source: https://github.com/cyrusxyl/agent-discussion

| Skill | | Description |
|---|---|---|
| `agent-discussion:agent-discussion` | ✅ | Multi-agent discussion coordination skill. Use this immediately when the user invokes /agent-discussion, "start a debate", "join the discussion", "let's debate", or wants multiple AI agents (Claude Code, Antigravity, Co… |

### agent-estimate `v0.8.0`

_Effort estimation for AI coding agents — PERT three-point estimation with METR reliability thresholds and wave planning_

Source: https://github.com/kiloloop/agent-estimate

| Skill | | Description |
|---|---|---|
| `agent-estimate:claude` | ⬜ | Estimate effort for AI coding agent tasks using PERT three-point estimation, provenance-labeled reliability policies, and wave planning. |
| `agent-estimate:codex` | ⬜ | Codex skill for running agent-estimate CLI commands (estimate, validate, calibrate). |

### ai-mentor `v1.2.0`

_Learn the Claude Code capabilities you didn't know existed. A discovery mentor that reads your setup, remembers what you already use, and teaches your highest-leverage gap — one demonstrated move at a time, grounded in your repo, never repeating itself._

Source: https://github.com/gwenneg/ai-mentor

| Skill | | Description |
|---|---|---|
| `ai-mentor:mentor` | ✅ | Match a developer's question or problem to the best AI workflow, ranked and personalized from a persistent profile of what they already know. MUST BE USED — instead of answering from general knowledge — whenever the use… |

### claude-code-setup `v1.0.0`

_Analyze codebases and recommend tailored Claude Code automations such as hooks, skills, MCP servers, and subagents._

| Skill | | Description |
|---|---|---|
| `claude-code-setup:claude-automation-recommender` | ✅ | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving… |

### claude-md-management `v1.0.0`

_Tools to maintain and improve CLAUDE.md files - audit quality, capture session learnings, and keep project memory current._

| Skill | | Description |
|---|---|---|
| `claude-md-management:claude-md-improver` | ✅ | Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report,… |

**Slash commands:** `/claude-md-management:revise-claude-md` — Update CLAUDE.md with learnings from this session

### napkin-math `v0.1.0`

_Back-of-the-envelope estimates with stated assumptions and honest ranges, plus a sanity check for numbers other people quote at you._

Source: https://github.com/ajribeiro/napkin-math

| Skill | | Description |
|---|---|---|
| `napkin-math:estimate` | ✅ | Make a back-of-the-envelope estimate with stated assumptions and a range. Use when the user asks roughly how much, how many, how long or how big something is, asks for a Fermi estimate, a ballpark, or napkin math, or ru… |
| `napkin-math:sanity-check` | ✅ | Check whether a number someone quoted is plausible, using a quick independent estimate. Use when the user asks "does this number make sense", "is this plausible", "sanity check this figure", pastes a claim with a number… |

### receipts

_A personal Claude Code impact report for justifying your usage to a manager or a self-review: what you shipped, which projects it went to, and each project's share of your usage. Reads your ~/.claude/projects transcripts and runs read-only git locally; only counts and project names are sent to write it up, and the report stays on your machine._

Source: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/receipts

| Skill | | Description |
|---|---|---|
| `receipts:receipts` | ✅ | Generate a personal Claude Code usage & impact report ("receipts") from this machine's local session transcripts — for justifying Claude Code usage/spend to a manager, self-review, or "what have I been using this for" c… |

### session-report

_Generate an explorable HTML report of Claude Code session usage — tokens, cache efficiency, subagents, skills, and the most expensive prompts — from local ~/.claude/projects transcripts._

Source: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report

| Skill | | Description |
|---|---|---|
| `session-report:session-report` | ✅ | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts. |

### setup-audit `v0.10.0`

_Audit Claude Code configuration, usage, and common setup risks against current docs. Get evidence-backed security, cost, learning, and optional readiness findings, readable reports, and approved fixes with backups and verification._

Source: https://github.com/senzelden/claude-setup-audit

| Skill | | Description |
|---|---|---|
| `setup-audit:setup-audit` | ✅ | Audit the user's Claude Code configuration and usage (user and per-project settings, permissions, hooks, MCP servers, skills, plugins, CLAUDE.md files, memory, and usage and transcript data) against the current official… |

### skill-creator

_Create new skills, improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize an existing skill, run evals to test a skill, or benchmark skill performance with variance analysis._

| Skill | | Description |
|---|---|---|
| `skill-creator:skill-creator` | ✅ | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill p… |

### superpowers `v6.4.2`

_Core skills library for Claude Code: TDD, debugging, collaboration patterns, and proven techniques_

Source: https://github.com/obra/superpowers · Has hooks

| Skill | | Description |
|---|---|---|
| `superpowers:brainstorming` | ✅ | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation. |
| `superpowers:diagnosing-superpowers` | ✅ | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill that didn't fire, "it took too long", "why is it so expensive", "what is… |
| `superpowers:dispatching-parallel-agents` | ✅ | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `superpowers:executing-plans` | ✅ | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is available |
| `superpowers:finishing-a-development-branch` | ✅ | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work |
| `superpowers:receiving-code-review` | ✅ | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind… |
| `superpowers:requesting-code-review` | ✅ | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `superpowers:subagent-driven-development` | ✅ | Use when executing implementation plans with independent tasks in the current session |
| `superpowers:systematic-debugging` | ✅ | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `superpowers:test-driven-development` | ✅ | Use when implementing any feature or bugfix, before writing implementation code |
| `superpowers:using-git-worktrees` | ✅ | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback |
| `superpowers:using-superpowers` | ✅ | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions |
| `superpowers:verification-before-completion` | ✅ | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions … |
| `superpowers:writing-plans` | ✅ | Use when you have a spec or requirements for a multi-step task, before touching code |
| `superpowers:writing-skills` | ✅ | Use when creating new skills, editing existing skills, or verifying skills work before deployment |

### task-observer `v1.3.2`

_Turn your corrections into lasting rules in CLAUDE.md, so Claude Code remembers your package manager, style and conventions in every session._

Source: https://petrovicistefan.ro

| Skill | | Description |
|---|---|---|
| `task-observer:task-observer` | ✅ | Use when the user corrects how Claude works or states a lasting preference (style, tools, conventions), to record it so later sessions follow it. |

**Slash commands:** `/task-observer:learn` — Save a working preference to CLAUDE.md so future sessions follow it, `/task-observer:preferences` — Show and tidy the working preferences saved in CLAUDE.md

### user-level skills

| Skill | | Description |
|---|---|---|
| `session-start-hook` | ✅ | Creating and developing startup hooks for Claude Code cloud sessions. Use only when the user asks for a SessionStart hook committed to their repository. Not for setting up a cloud environment or a repository for cloud s… |

## Software engineering lifecycle

### Built-in (Claude Code harness)

| Skill | Enabled | What it does |
|---|---|---|
| `claude-api` | ✅ | Reference for the Claude API / Anthropic SDK: model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, migration. Trigger whenever Claude/Anthropic/LLM-shaped work is involved; never answer pricing/model questions from memory. |
| `code-review` | ✅ | Review the current diff or a PR/branch/path for correctness bugs at an effort level (low..max). --comment posts inline PR comments, --fix applies fixes, --max-findings N. |
| `run` | ✅ | Launch and drive this project's app to see a change working (CLI, server, TUI, Electron, browser, library); screenshot or confirm in the real app. |
| `security-review` | ✅ | Security review of the pending changes on the current branch. |
| `simplify` | ✅ | Review changed code for reuse, simplification, efficiency and altitude cleanups, then apply fixes. Quality only — not a bug hunt. |

### agent-protocols `v1.0.0`

_Structured engineering protocols for AI coding agents, covering the full software development lifecycle from spec to ship._

Source: https://github.com/arneesh/agent-protocols · Has hooks

| Skill | | Description |
|---|---|---|
| `agent-protocols:api-and-interface-design` | ✅ | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating REST or GraphQL endpoints, defining type contracts between modules, or establishing boundari… |
| `agent-protocols:browser-testing-with-devtools` | ✅ | Tests in real browsers. Use when building or debugging anything that runs in a browser. Use when you need to inspect the DOM, capture console errors, analyze network requests, profile performance, or verify visual outpu… |
| `agent-protocols:ci-cd-and-automation` | ✅ | Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality gates, configure test runners in CI, or establish deployment strategies. |
| `agent-protocols:code-review-and-quality` | ✅ | Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality across multiple dimensions before it enter… |
| `agent-protocols:code-simplification` | ✅ | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, maintain, or extend than it should be. Use when reviewing code that has accumulate… |
| `agent-protocols:context-engineering` | ✅ | Optimizes agent context setup. Use when starting a new session, when agent output quality degrades, when switching between tasks, or when you need to configure rules files and context for a project. |
| `agent-protocols:debugging-and-error-recovery` | ✅ | Guides systematic root-cause debugging. Use when tests fail, builds break, behavior doesn't match expectations, or you encounter any unexpected error. Use when you need a systematic approach to finding and fixing the ro… |
| `agent-protocols:deprecation-and-migration` | ✅ | Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to another. Use when deciding whether to maintain or sunset existing code. |
| `agent-protocols:documentation-and-adrs` | ✅ | Records decisions and documentation. Use when making architectural decisions, changing public APIs, shipping features, or when you need to record context that future engineers and agents will need to understand the code… |
| `agent-protocols:frontend-ui-engineering` | ✅ | Builds production-quality UIs. Use when building or modifying user-facing interfaces. Use when creating components, implementing layouts, managing state, or when the output needs to look and feel production-quality rath… |
| `agent-protocols:git-workflow-and-versioning` | ✅ | Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, or when you need to organize work across multiple parallel streams. |
| `agent-protocols:idea-refine` | ✅ | Refines ideas iteratively. Refine ideas through structured divergent and convergent thinking. Use "idea-refine" or "ideate" to trigger. |
| `agent-protocols:incident-response-and-postmortems` | ✅ | Guides live incident handling and blameless postmortems. Use when production is degraded or down, when alerts fire, when customers report outages, or when you need to capture learning after a serious incident. |
| `agent-protocols:incremental-implementation` | ✅ | Delivers changes incrementally. Use when implementing any feature or change that touches more than one file. Use when you're about to write a large amount of code at once, or when a task feels too big to land in one ste… |
| `agent-protocols:internationalization-and-localization` | ✅ | Structures i18n and l10n work for user-facing software. Use when adding multiple languages, regional formats, RTL layouts, or locale-aware content. Use when extracting strings, choosing i18n libraries, or verifying tran… |
| `agent-protocols:karpathy-guidelines` | ✅ | Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria. |
| `agent-protocols:performance-optimization` | ✅ | Optimizes application performance. Use when performance requirements exist, when you suspect performance regressions, or when Core Web Vitals or load times need improvement. Use when profiling reveals bottlenecks that n… |
| `agent-protocols:planning-and-task-breakdown` | ✅ | Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task feels too large to start, when you need to estimate scope, or when parallel… |
| `agent-protocols:research-spike-and-poc` | ✅ | Runs timeboxed technical exploration to reduce unknowns before commitment. Use when you must choose between technologies, prove feasibility, estimate effort for unfamiliar work, or answer "can we integrate X" before wri… |
| `agent-protocols:security-and-hardening` | ✅ | Hardens code against vulnerabilities. Use when handling user input, authentication, data storage, or external integrations. Use when building any feature that accepts untrusted data, manages user sessions, or interacts … |
| `agent-protocols:shipping-and-launch` | ✅ | Prepares production launches. Use when preparing to deploy to production. Use when you need a pre-launch checklist, when setting up monitoring, when planning a staged rollout, or when you need a rollback strategy. |
| `agent-protocols:source-driven-development` | ✅ | Grounds every implementation decision in official documentation. Use when you want authoritative, source-cited code free from outdated patterns. Use when building with any framework or library where correctness matters. |
| `agent-protocols:spec-driven-development` | ✅ | Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when requirements are unclear, ambiguous, or only exist as a vague idea. |
| `agent-protocols:test-driven-development` | ✅ | Drives development with tests. Use when implementing any logic, fixing any bug, or changing any behavior. Use when you need to prove that code works, when a bug report arrives, or when you're about to modify existing fu… |
| `agent-protocols:using-agent-skills` | ✅ | Discovers and invokes agent skills. Use when starting a session or when you need to discover which skill applies to the current task. This is the meta-skill that governs how all other skills are discovered and invoked. |

**Slash commands:** `/agent-protocols:build` — Implement the next task incrementally — build, test, verify, commit, `/agent-protocols:code-simplify` — Simplify code for clarity and maintainability — reduce complexity without changing behavi…, `/agent-protocols:plan` — Break work into small verifiable tasks with acceptance criteria and dependency ordering, `/agent-protocols:review` — Conduct a five-axis code review — correctness, readability, architecture, security, perfo…, `/agent-protocols:ship` — Run the pre-launch checklist and prepare for production deployment, `/agent-protocols:spec` — Start spec-driven development — write a structured specification before writing code, `/agent-protocols:test` — Run TDD workflow — write failing tests, implement, verify. For bugs, use the Prove-It pat…

**Subagents** (`Agent(subagent_type=…)`):

- `agent-protocols:accessibility-specialist` — Accessibility engineer focused on WCAG-oriented review, keyboard and screen reader flows, and inclusive UI. Use when auditing components, fixing a11y bugs, or defining acceptance criteria for accessi…
- `agent-protocols:code-reviewer` — Senior code reviewer that evaluates changes across five dimensions -- correctness, readability, architecture, security, and performance. Use for thorough code review before merge.
- `agent-protocols:documentation-specialist` — Technical writer focused on ADRs, API docs, and reader-first explanations. Use when drafting architecture decisions, public APIs, runbooks, or improving unclear technical documentation.
- `agent-protocols:performance-engineer` — Performance engineer focused on measurement-first analysis, profiling, and regressions. Use when optimizing hot paths, investigating slowness, or validating Core Web Vitals and backend latency target…
- `agent-protocols:release-engineer` — Release and platform engineer focused on CI/CD pipelines, deployment safety, and launch readiness. Use when designing pipelines, staging rollouts, rollbacks, or pre-launch checklists.
- `agent-protocols:security-auditor` — Security engineer focused on vulnerability detection, threat modeling, and secure coding practices. Use for security-focused code review, threat analysis, or hardening recommendations.
- `agent-protocols:spec-analyst` — Product-minded analyst focused on PRD quality, scope boundaries, and testable acceptance criteria. Use when refining a vague idea, reviewing a spec before build, or de-risking unclear requirements.
- `agent-protocols:test-engineer` — QA engineer specialized in test strategy, test writing, and coverage analysis. Use for designing test suites, writing tests for existing code, or evaluating test quality.

### claude-security `v0.11.0`

_Deep vulnerability scanning of your own code, run entirely inside your Claude Code session at a chosen effort tier, with every finding challenged before it is reported and the verification tally computed in code. Turns surviving findings into targeted patches, each verified by a panel of agents, that you apply when you choose. See the plugin README for the tiers, the report format, and the trust …_

Has hooks

| Skill | | Description |
|---|---|---|
| `claude-security:claude-security` | ⬜ | The Claude Security menu — pick a job: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's or a pull request's diff, or one commit), or suggest patches (findings turned into targ… |

**Subagents** (`Agent(subagent_type=…)`):

- `claude-security:claude-security` — The dedicated Claude Security orchestrator. Hand it an unattended job — "fully scan this repository and patch what you find; I understand it will use a lot of tokens" — and it runs the whole thing it…
- `claude-security:explore` — Read-only code explorer that the plugin's other agents dispatch to map a codebase — locate files, trace how a flow is wired, find every caller of a symbol, answer "where does X happen".
- `claude-security:patch-generator` — Implements the fix for one finding inside a scratch workspace clone, staged for review and delivery as a patch file; dispatched by the fix job, not for direct invocation.
- `claude-security:patch-verifier` — The single verifier per fix round — reviews the workspace's staged diff against the finding, runs the tests, and states the three confidence claims a patch file must earn; dispatched by the fix job, …
- `claude-security:scan-inventory` — Restricted read-only repository cartographer dispatched by the Claude Security scan workflow to partition the tree into components and account for every top-level directory; not for direct invocation…
- `claude-security:scan-loader` — Restricted read-only loader dispatched by the Claude Security scan workflow to return one candidates file from the run directory; not for direct invocation.
- `claude-security:scan-researcher` — Restricted read-only vulnerability researcher dispatched by the Claude Security scan workflow; not for direct invocation or general exploration.
- `claude-security:scan-verifier` — Restricted read-only verifier dispatched by the Claude Security scan workflow to vote on one candidate finding; not for direct invocation.

### code-review `v1.0.1`

_Automated code review for pull requests using multiple specialized agents with confidence-based scoring_

**Slash commands:** `/code-review:code-review` — Code review a pull request

### code-simplifier `v1.0.0`

_Agent that simplifies and refines code for clarity, consistency, and maintainability while preserving functionality_

**Subagents** (`Agent(subagent_type=…)`):

- `code-simplifier:code-simplifier` — Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. Focuses on recently modified code unless instructed otherwise.

### mattpocock-skills `v1.2.3` ⏸ off by plugin profile

_Matt Pocock's agent skills for real engineering: grilling, spec/ticket flows, TDD, code review, domain modelling and more. Plug-and-play, not vibe coding._

Source: https://www.aihero.dev/s/skills-newsletter

| Skill | | Description |
|---|---|---|
| `mattpocock-skills:code-review` | ⏸ | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating is… |
| `mattpocock-skills:codebase-design` | ⏸ | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when a… |
| `mattpocock-skills:diagnosing-bugs` | ⏸ | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. |
| `mattpocock-skills:domain-modeling` | ⏸ | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a CONTEXT.md, or recording or editing an ADR. |
| `mattpocock-skills:grilling` | ⏸ | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases. |
| `mattpocock-skills:prototype` | ⏸ | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like. |
| `mattpocock-skills:research` | ⏸ | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to … |
| `mattpocock-skills:resolving-merge-conflicts` | ⏸ | Use when you need to resolve an in-progress git merge/rebase conflict. |
| `mattpocock-skills:tdd` | ⏸ | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. |
| `mattpocock-skills:wizard` | ⏸ | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or run… |
| `mattpocock-skills:writing-for-agents` | ⏸ | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. |
| `mattpocock-skills:ask-matt` | ⬜ | Ask which skill or flow fits your situation. A router over the skills in this repo. |
| `mattpocock-skills:claude-handoff` | ⬜ | Hand the current conversation off to a fresh background agent that picks up the work immediately. |
| `mattpocock-skills:git-guardrails-claude-code` | ⬜ | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git pu… |
| `mattpocock-skills:grill-me` | ⬜ | A relentless interview to sharpen a plan or design. |
| `mattpocock-skills:grill-with-docs` | ⬜ | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| `mattpocock-skills:handoff` | ⬜ | Compact the current conversation into a handoff document for another agent to pick up. |
| `mattpocock-skills:implement` | ⬜ | Implement a piece of work based on a spec or set of tickets. |
| `mattpocock-skills:implement-spec` | ⬜ | Implement a specification in code. |
| `mattpocock-skills:improve-codebase-architecture` | ⬜ | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| `mattpocock-skills:loop-me` | ⬜ | Grill me about specs for the workflows I want to build, within this workspace. |
| `mattpocock-skills:migrate-to-shoehorn` | ⬜ | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data. |
| `mattpocock-skills:pr` | ⬜ | Use when writing a PR body. |
| `mattpocock-skills:retro` | ⬜ | Conduct a retrospective on a coding session. |
| `mattpocock-skills:scaffold-exercises` | ⬜ | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise stubs, or set up a new course section. |
| `mattpocock-skills:setup-matt-pocock-skills` | ⬜ | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills. |
| `mattpocock-skills:setup-pre-commit` | ⬜ | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/ty… |
| `mattpocock-skills:setup-ts-deep-modules` | ⬜ | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through its entry-point files. User-invoked. |
| `mattpocock-skills:teach` | ⬜ | Teach the user a new skill or concept, within this workspace. |
| `mattpocock-skills:to-questionnaire` | ⬜ | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |
| `mattpocock-skills:to-spec` | ⬜ | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. |
| `mattpocock-skills:to-tickets` | ⬜ | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in one file per ticket locally, or native blocki… |
| `mattpocock-skills:triage` | ⬜ | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. |
| `mattpocock-skills:wait-what` | ⬜ | Stop. That last message did not land: re-pitch it. |
| `mattpocock-skills:wayfinder` | ⬜ | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear. |
| `mattpocock-skills:writing-beats` | ⬜ | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. |
| `mattpocock-skills:writing-fragments` | ⬜ | Writing, explore: mine raw fragments, no structure yet. |
| `mattpocock-skills:writing-shape` | ⬜ | Writing, exploit: shape raw material into an article, paragraph by paragraph. |

### modern-web-guidance `v0.0.194`

_Keep your coding agent up to date with the latest web best practices_

| Skill | | Description |
|---|---|---|
| `modern-web-guidance:chrome-extensions` | ✅ | Build and publish Chrome Extensions using Manifest V3 best practices. Use this skill whenever the user asks to create, modify, debug, or understand Chrome browser extensions, add-ons, or anything involving the Chrome Ex… |
| `modern-web-guidance:modern-web-guidance` | ✅ | Search tool for modern web development best practices. MANDATORY: Execute FIRST for all HTML/CSS and clientside JS tasks. Do NOT skip — web APIs evolve rapidly and training weights contain obsolete patterns. Trigger imm… |

### zizi-skills `v0.5.0` ⏸ off by plugin profile

_A skill library for disciplined software work: planning, test-first implementation, code and security review, git hygiene, and session handoff. Invoked as zizi-skills:<skill> once installed._

Source: https://github.com/ziazon/zizi-skills

| Skill | | Description |
|---|---|---|
| `zizi-skills:adversarial-review` | ⏸ | Run several independent model seats against one problem or one plan, make them attack each other, fact-check every contested claim, then ask the human one gate of questions. Two modes: a design panel for an open problem… |
| `zizi-skills:app-store` | ⏸ | App Store and Google Play listings: title, subtitle, keywords, description, screenshots, previews, ratings prompts. Use when preparing or auditing a store listing or asking why installs are low. Copy wording is plain-la… |
| `zizi-skills:code-quality` | ⏸ | Standards for reviewing and cleaning up code. Use when reviewing any diff (your own before commit, a Codex or sub-agent diff, a colleague's PR) or when asked to clean up, de-duplicate or delete dead code. Holds the hard… |
| `zizi-skills:data-analytics` | ⏸ | Decide which metrics, KPIs and charts an app's data deserves. Use when exploring a schema or domain, planning a dashboard ("what should this show?", "add stats to X"), or choosing which data points matter. Keeps a per-p… |
| `zizi-skills:database-optimization` | ⏸ | Correct, fast queries, views, indexes and schema. Use before adding or changing any query (ORM or raw), entity, migration, index or view, and when an endpoint or list is slow. In a TypeORM project, load it before writin… |
| `zizi-skills:debugging-and-error-recovery` | ⏸ | Root-cause debugging. Use when a test fails, a build breaks, behavior doesn't match expectations, or any unexpected error appears. Builds a loop that goes red on the failure before theorising, ranks falsifiable hypothes… |
| `zizi-skills:deprecation-and-migration` | ⏸ | Remove or replace systems, APIs and features. Use when sunsetting code, migrating users to a new implementation, running a strangler migration off a legacy service, or making an expand/contract schema change while old a… |
| `zizi-skills:design-assets` | ⏸ | Visual assets: logos, icons, illustrations, hero and OG images, empty-state art, favicons, raster-to-vector conversion. Use whenever a task needs one. Recraft is called first and hand-authoring is the fallback; covers t… |
| `zizi-skills:design-guide` | ⏸ | Visual and UX judgment: color, typography, spacing, hierarchy, themes. Use when choosing colors or status/badge colors, theming (white-label included), making a screen "look better" or more polished, or reviewing a UI's… |
| `zizi-skills:done` | ⏸ | Session close-out with no resume prompt. Use on /done, or when wrapping up a session where nothing remains to resume or the continuation prompt already exists (a standup queue's next item). Runs the handoff close-out mi… |
| `zizi-skills:find-skills` | ⏸ | Discover and install agent skills. Use only when the user explicitly asks for a skill ("find or install a skill for X", "is there a skill that..."), never for an ordinary how-do-I question. |
| `zizi-skills:first-customers` | ⏸ | Find and reach a product's first customers honestly: demand signals, local-business prospect lists, outreach drafts a human sends. Use when asking "who would buy this" or "how do I get my first users or clients". Offer … |
| `zizi-skills:frontend` | ⏸ | Frontend structure and behavior: components, state, a typed service layer, lists, tables and filters, forms, modals, loading/empty/error states, routing, SSR, web performance. Use when building or refactoring UI or addi… |
| `zizi-skills:git-sync` | ⏸ | The standing git workflow. Use at the start of any branch work and before every commit, push, rebase or PR: your own branch (never main), rebased on current main, every branch pushed, PR bodies in the standard shape, PR… |
| `zizi-skills:grant-writing` | ⏸ | Research grant applications: research and mentoring plans, specific aims, budget justifications, abstracts. Use when writing or strengthening a proposal, checking a draft against a funder's guidelines or review criteria… |
| `zizi-skills:handoff` | ⏸ | Durable session handoff with a resume prompt. Use when pausing or ending work at a real boundary (a phase or PR done, a blocker, a pivot, a drained queue) or when the user says "hand off" or "we'll continue later". Save… |
| `zizi-skills:i18n` | ⏸ | Multi-language support (i18n/l10n). Use when a task touches a translation file or a user-facing string in a product that ships more than one language: adding a language or key, extracting strings, vue-i18n/nestjs-i18n/g… |
| `zizi-skills:idea-refine` | ⏸ | Turn a vague idea into a sharp, actionable concept by diverging, then converging. Use for pure ideation: "ideate", "refine this idea", "explore options for X". It sits upstream of a plan; to plan an idea already chosen,… |
| `zizi-skills:information-architecture` | ⏸ | How content and pages are organized for their audience: site maps, page inventories, each page's job, where a message or feature lives, navigation and funnels, heading structure, buried or orphaned messages. Applies to … |
| `zizi-skills:infrastructure` | ⏸ | Change infrastructure and dev-workflow tooling: Nomad, Consul, Vault, Terraform, Docker, GitHub Actions, task runners, env and direnv setup, setup scripts, a project's own ops CLI, launchd and hooks. Use when editing an… |
| `zizi-skills:integrations` | ⏸ | Connect to or automate third-party services: REST APIs, MCP servers, OAuth and tokens, webhooks, recurring syncs. Use when building or debugging an integration, scheduling a job against an external service, deciding whe… |
| `zizi-skills:marketing` | ⏸ | Why people choose, buy, sign up and stay, applied honestly: behavioral models, offers, pricing, trust, urgency, onboarding and growth loops for the apps and sites we build. Use when shaping a landing, pricing, signup or… |
| `zizi-skills:monitoring` | ⏸ | Observability into running code. Use when adding logging or instrumentation, diagnosing a running service ("watch the logs", "what is it actually doing"), standardizing log output, or when a change must be proven on the… |
| `zizi-skills:orchestration` | ⏸ | Run multi-step or long-running work as an orchestrator over disposable sub-agents. Use at the start of a program phase, migration, broad sweep, deep research or many-file job, or when your context fills with exploration… |
| `zizi-skills:plain-language` | ⏸ | Clear, friendly, jargon-free writing for non-technical readers: ticket text, QA steps, release notes, status updates, UI copy, business messages. Use when writing for QA, product, stakeholders or end users, or on a "mak… |
| `zizi-skills:planning` | ⏸ | Plan before building anything non-trivial: multi-file or multi-phase work, a feature, a migration, or whenever asked to plan. Research, write the plan, ask every decision up front (a second gate only for questions that … |
| `zizi-skills:project-config` | ⏸ | The recorded facts of how each project runs: node version, env and direnv, package manager, monorepo layout, and the exact install, run, build, test, lint and migrate commands. Consult before your first shell command in… |
| `zizi-skills:project-manager` | ⏸ | Keep the tracker (Jira, Trello, or GitHub Issues and Projects) in sync with the real work. Use on /project-manager or "file a ticket", "is this tracked", "write QA steps", "audit my tickets", "find duplicates", "clean u… |
| `zizi-skills:research-methods` | ⏸ | Social and health research design: conceptual and logic models, CBPR/YPAR, participatory and agent-based modeling, spatial indices, implementation frameworks (CFIR, RE-AIM), measures, IRB and human-subjects sections, li… |
| `zizi-skills:security-and-hardening` | ⏸ | Security standards a default pass gets wrong: credential reach, proving a control holds, leak-free secret scanning, SSRF/TOCTOU, deployment topology. Use when handling untrusted input, auth, sessions, stored data or thi… |
| `zizi-skills:service-architecture` | ⏸ | Backend architecture decisions: service boundaries, splitting vs consolidating, inter-service calls, auth guards and tiers, where logic lives, strangler migrations. Load before adding or versioning an endpoint or a serv… |
| `zizi-skills:source-driven-development` | ⏸ | Ground implementation decisions in official documentation, with citations. Use when building with a framework or library where correctness matters or common patterns may be outdated. |
| `zizi-skills:status-update` | ⏸ | Session status as a visual dashboard plus a 2-3 line TLDR, never prose alone. Use on /status-update, "where are we", "what's left", mid-way through a multi-item run, and at any wrap-up covering more than one unit of wor… |
| `zizi-skills:tabler-ui` | ⏸ | Tabler admin template (tabler.io) components and the workarounds that make them behave in Vue 3. Consult before any Tabler markup or interactive component: modals, dropdowns, badges, grids, forms, icons, wizards, empty … |
| `zizi-skills:tdd-skill` | ⏸ | Test-first (red-green-refactor) for any codebase. Use when adding or changing behavior, fixing a bug (it starts with a failing regression test), or asked to add or cover tests. Finds how this project runs tests, names t… |
| `zizi-skills:explain` | ⬜ | Re-explain the last message in plain words, using the project's own vocabulary. |

## Language / platform specific

### cloudflare `v1.0.0`

_Build, test, and deploy applications on Cloudflare with platform guidance Skills and the Cloudflare MCP server._

MCP: `cloudflare`

| Skill | | Description |
|---|---|---|
| `cloudflare:agents-sdk` | ✅ | Build, debug, or review Cloudflare Agents SDK applications using the agents package. |
| `cloudflare:cloudflare` | ✅ | Discover and choose Cloudflare products for apps, APIs, AI agents, storage, networking, and security. Use for architecture and product selection, including when the user describes a need without naming a Cloudflare prod… |
| `cloudflare:cloudflare-email-service` | ✅ | Implement or troubleshoot Cloudflare Email Sending and Email Routing integrations and their delivery configuration. |
| `cloudflare:cloudflare-one` | ✅ | Design, configure, troubleshoot, or review Cloudflare One Zero Trust and SASE deployments. Use cloudflare-one-migrations for migration planning from other vendors. |
| `cloudflare:cloudflare-one-migrations` | ✅ | Assess and plan migrations from existing VPN, SWG, or SASE platforms to Cloudflare One, including policy mapping, parity gaps, and rollout. |
| `cloudflare:durable-objects` | ✅ | Build, debug, or review Cloudflare Durable Objects code for persistent state and coordination. |
| `cloudflare:nextjs-on-cloudflare` | ✅ | Build, migrate, and deploy Next.js apps on Cloudflare Workers with vinext. Use when starting a Next.js project on Cloudflare, moving an existing app to Workers, choosing between vinext and OpenNext, or setting up vinext… |
| `cloudflare:sandbox-migrate-to-next` | ✅ | Migrate Cloudflare Sandbox apps from stable @cloudflare/sandbox to @cloudflare/sandbox@next (SDK 1.0 preview). Use sandbox-next for apps already on the preview. |
| `cloudflare:sandbox-next` | ✅ | Build or maintain Cloudflare Sandbox apps on @cloudflare/sandbox@next (SDK 1.0 preview). Use sandbox-migrate-to-next when porting a stable app. |
| `cloudflare:sandbox-stable` | ✅ | Build or maintain Cloudflare Sandbox apps on the stable @cloudflare/sandbox package. Use sandbox-next for preview apps and sandbox-migrate-to-next for stable-to-preview migrations. |
| `cloudflare:turnstile-spin` | ✅ | Set up, repair, or migrate to Cloudflare Turnstile bot verification in an existing frontend and backend, including server-side Siteverify. |
| `cloudflare:web-perf` | ✅ | Audit, diagnose, or optimize website loading and interaction performance, Core Web Vitals, and Lighthouse performance scores. |
| `cloudflare:workers-best-practices` | ✅ | Cloudflare Workers best practices for production applications. Use when writing, reviewing, or configuring Workers. |
| `cloudflare:wrangler` | ✅ | Run or troubleshoot Wrangler CLI commands and configure Worker projects for local development, deployment, and Cloudflare resource management. |

### contentasoft-cad-converter `v1.0.3` ⏸ off by plugin profile

_3D CAD Converter on your Windows PC from your AI agent: converting STEP, IGES, STL, OBJ, FBX, glTF, 3MF and other 3D/CAD files. Runs locally on your files._

Source: https://www.contenta-software.com/3dcadconverter/ · MCP: `cad-converter`

| Skill | | Description |
|---|---|---|
| `contentasoft-cad-converter:contenta-cad` | ⏸ | Convert 3D CAD and mesh files with the 3D CAD Converter CLI (cadconvert). Use when the user asks to convert STEP, IGES or BREP to STL, OBJ, 3MF, glTF/GLB, FBX, PLY or other formats, convert between mesh formats (includi… |

### github

_Official GitHub MCP server for repository management. Create issues, manage pull requests, review code, search repositories, and interact with GitHub's full API directly from Claude Code._

MCP: `github`

### qt-development-skills `v1.7.2`

_Agentic engineering skills for Qt software development, including Qt C++/QML code review, QML coding, and Qt C++/QML code documentation. Bundles the hosted Qt Documentation MCP server for live Qt API lookups. These skills use AI and can make mistakes. Always double-check the output carefully._

MCP: `qt-docs`

| Skill | | Description |
|---|---|---|
| `qt-development-skills:qt-canvas2d` | ✅ | Applies Qt Canvas2D (QtCanvas2D / Qt Canvas Painter, Qt 6.12+) best practices when producing or working with Canvas2D QML source code. Use whenever Canvas2D, Canvas2DContext, path2d, boxshadow2d, boxgradient2d, gridpatt… |
| `qt-development-skills:qt-cmake-project` | ✅ | Use to generate or update Qt 6 CMake projects or edit CMakeLists.txt, add sources/resources or define targets (executable, QML module, library). |
| `qt-development-skills:qt-cpp-docs` | ✅ | Generates standalone Markdown reference documentation for any Qt/C++ source files — Qt Widgets classes, Qt Quick backends, Qt/C++ modules, plain C++ utilities, structs, free-function headers, and entry points like main.… |
| `qt-development-skills:qt-cpp-review` | ✅ | Invoke when the user asks to review, check, audit, or look over Qt6 C++ code — or suggest before committing. Runs deterministic linting (60+ rules) then six parallel deep- analysis agents covering model contracts, owner… |
| `qt-development-skills:qt-figma-component-generation` | ✅ | Extract component metadata from a Figma design system and generate production-ready QML controls. Use this skill whenever someone wants to turn Figma components into QML files — whether they say "generate components fro… |
| `qt-development-skills:qt-figma-token-extraction` | ✅ | Extract design tokens, text styles, and variables from a Figma design system and produce a design-tokens.json plus ready-to-use QML singletons. Use this skill whenever someone wants to pull their design system out of Fi… |
| `qt-development-skills:qt-qml` | ✅ | Applies QML best practices when producing or working with QML source code. Use whenever QML code is the primary subject: writing, reviewing, fixing, refactoring, optimizing, or debugging QML files, components, or bindin… |
| `qt-development-skills:qt-qml-docs` | ✅ | Generates standalone Markdown reference documentation for QML components and applications. Use this skill whenever you want to document QML files, create API reference docs for a QML component or module, document a Qt Q… |
| `qt-development-skills:qt-qml-profiler` | ✅ | Use when the user is investigating QML / Qt Quick performance — both vague complaints ("the UI feels laggy", "this is slow", "frames are dropping", "the app stutters") and explicit asks to profile, find hotspots, or opt… |
| `qt-development-skills:qt-qml-review` | ✅ | Invoke when the user asks to review, check, audit, or look over Qt6 QML code -- or suggest before committing. Runs deterministic linting (47+ rules) then six parallel deep- analysis agents covering bindings, layout, loa… |
| `qt-development-skills:qt-qml-test` | ✅ | Generates Qt Quick Test cases (TestCase, SignalSpy, tryCompare) for QML components. Use for "write QML tests", "qml test", "qt quick test". |
| `qt-development-skills:qt-qml-test-run` | ✅ | Builds and runs Qt Quick Test (qmltestrunner / CTest) for a QML project, then writes a Markdown report. Use for "run qml tests", "run qmltestrunner". |
| `qt-development-skills:qt-ui-design` | ✅ | Design or audit UI for Qt/QML, Qt projects, web, or embedded MPU or MCU targets. Use when creating screens, layouts, navigation, or auditing UX. |

## Frontend, UI & design

### Built-in (Claude Code harness)

| Skill | Enabled | What it does |
|---|---|---|
| `artifact-capabilities` | ✅ | Runtime capabilities for published Artifacts: live/connected data, shared state/db, viewer identity, ask-Claude, file storage, downloads, camera/mic/location. Load before passing `capabilities` or writing window.claude.* code. |
| `artifact-design` | ✅ | Design guidance and page contract for Artifacts (title, libraries, theming tokens, dark mode, layout, size). Load before writing any artifact page. |
| `artifact-diagramming` | ✅ | When a diagram earns its place in an Artifact and how to draw legible inline-SVG diagrams that work in both themes. |
| `dataviz` | ✅ | Read BEFORE creating any chart, graph, plot, dashboard, stat tile or data visualization in any medium (HTML/React artifact, SVG, matplotlib/plotly/d3/Recharts, PNG). Form heuristic, color formula + validator, mark specs, interaction rules, validated default palette. |

### abracadabrax-image-video `v1.0.2`

_AI image generator and AI video generator: turn a text prompt into an image or a video, pick model, format and length with Claude, and render it with your Abracadabrax credits._

Source: https://abracadabrax.app/mcp#media · MCP: `abracadabrax-image-video`

### animatedwebs `v1.3.0`

_Build cinematic, animated websites from Claude Code: 1,400+ AnimatedWebs templates with live demos, cinematic video backgrounds, animated UI components, design systems and Design Studio, through a 15-tool MCP server._

Source: https://animatedwebs.com · MCP: `animatedwebs`

| Skill | | Description |
|---|---|---|
| `animatedwebs:animatedwebs-backgrounds` | ✅ | Add a cinematic video background (a seamless looping film) to a hero or section using AnimatedWebs Cinematic Backgrounds. Use when the user asks for a video background, a looping hero video, a film-like hero, or wants t… |
| `animatedwebs:animatedwebs-components` | ✅ | Add polished animated UI components (buttons, text effects, backgrounds, cards, loaders, sections) from the AnimatedWebs UI Library, or generate a new one. Use when the user asks for an animated button, heading effect, … |
| `animatedwebs:animatedwebs-design` | ✅ | Connect and use AnimatedWebs Design Studio, the private design workspace with built-in AI, from Claude Code. Use when the user wants to explore design directions, create design projects or artifacts, or asks to open or … |
| `animatedwebs:animatedwebs-hero` | ✅ | Give an existing website a cinematic hero section (looping video, WebGL or shader background, oversized type, refined navigation) using AnimatedWebs templates. Use when the user wants a more impressive first screen, an … |
| `animatedwebs:animatedwebs-site` | ✅ | Build a complete, premium animated website or landing page from an AnimatedWebs template (cinematic video heroes, WebGL scenes, scroll storytelling). Use when the user asks for a website, landing page, homepage or portf… |
| `animatedwebs:animatedwebs-style` | ✅ | Give a project a coherent, premium visual style from AnimatedWebs design systems, covering colour tokens, type scale, radius and buttons, exported as DESIGN.md, a Tailwind theme or CSS variables. Use when the user asks … |

**Slash commands:** `/animatedwebs:background` — Add a cinematic video background from AnimatedWebs to this site's hero, `/animatedwebs:browse` — Browse AnimatedWebs templates by style or industry, `/animatedwebs:component` — Add an animated UI component from the AnimatedWebs UI Library, `/animatedwebs:design` — Connect AnimatedWebs Design Studio to Claude Code, `/animatedwebs:hero` — Give this site a cinematic hero section with AnimatedWebs, `/animatedwebs:site` — Build a complete animated website for a business from the best-matching AnimatedWebs temp…, `/animatedwebs:style` — Apply an AnimatedWebs design system (colour, type, radius) to this project

### design-skills `v1.0.0`

_Ten UX and design skills that give coding agents deep knowledge of established design frameworks: research, critique, accessibility, journey mapping, design systems, strategy, interaction design, design ops, UX writing, and visual elevation._

Source: https://cuellarfr.github.io/design-skills/

| Skill | | Description |
|---|---|---|
| `design-skills:accessibility-audit` | ✅ | Conduct accessibility audits against WCAG 2.2 guidelines. Evaluate pages, components, and flows for conformance at A, AA, and AAA levels. Identify issues, assess severity, provide code fixes, and generate audit reports.… |
| `design-skills:design-critique` | ✅ | Evaluate UI designs against usability heuristics, UX laws, interaction patterns, interaction design principles, information architecture, and content quality. Conduct heuristic evaluations, structured design critiques, … |
| `design-skills:design-elevation` | ✅ | Comprehensive design elevation system that automatically transforms functional visual outputs into polished, professional designs. Use when creating ANY visual output including presentations (pptx), spreadsheets (xlsx),… |
| `design-skills:design-ops` | ✅ | Run design sprints, manage handoff, establish team rituals, documentation standards, and design QA processes. Covers the operational side of design — how teams organize work, collaborate with engineering, and ship quali… |
| `design-skills:design-systems` | ✅ | Build, document, and maintain design systems with design tokens, component specifications, pattern libraries, naming conventions, and governance processes. Conduct system audits, define component hierarchies, and establ… |
| `design-skills:interaction-design` | ✅ | Design meaningful interactions, microinteractions, animations, state machines, gesture patterns, error prevention, and product behavior. Specify how products respond to user input across all states and contexts using es… |
| `design-skills:journey-mapping` | ✅ | Create customer journey maps, service blueprints, experience maps, empathy maps, and other alignment diagrams. Guides diagram type selection, content structure, illustration syntax, and alignment workshops. |
| `design-skills:ux-research` | ✅ | Plan, conduct, and analyze UX research using proven methodologies. Use when planning user research, writing interview scripts, creating test plans, recruiting participants, analyzing qualitative data, or synthesizing fi… |
| `design-skills:ux-strategy` | ✅ | Connect design decisions to business outcomes through competitive analysis, opportunity mapping, Jobs to Be Done, outcome-driven discovery, value proposition design, and UX metrics. Shape product direction with strategi… |
| `design-skills:ux-writing` | ✅ | Create user-centered, accessible interface copy (microcopy) for digital products including buttons, labels, error messages, notifications, forms, onboarding, empty states, success messages, and help text. Use when writi… |

### design-superpowers `v1.0.0`

_Six Claude Code commands that make AI work like a design team: direction, design systems, product design, review, governance. Maturity-aware (L0 greenfield to L3 enterprise), Figma-optional via PluginOS, font-aware, behavior-validated._

Source: https://github.com/LSDimi/design-superpowers

| Skill | | Description |
|---|---|---|
| `design-superpowers:creative` | ✅ | Use when exploring visual direction, generating moodboards, proposing color palettes, typography systems, layout strategies, imagery/art direction, refreshing an existing design language, or setting brand-level directio… |
| `design-superpowers:design` | ✅ | Use when designing product features, flows, pages, or screens using an existing design system or design language. Activates for /design, "design a feature", "build a page", "select components", "compose a flow", "what c… |
| `design-superpowers:design-review` | ✅ | Use to evaluate existing designs against UX heuristics, accessibility standards, DS compliance, visual quality, or motion principles. Activates for /design-review, "review this design", "audit UI", "check accessibility"… |
| `design-superpowers:ds-consumer` | ✅ | Use when designing product features using an enterprise DS, evaluating existing UI, selecting DS components, reviewing information architecture, or requesting new components. Also use when fixing detached components in … |
| `design-superpowers:ds-make` | ✅ | Use when creating, updating, versioning, or deprecating design system tokens, components, or patterns. Activates for /ds-make, "new component", "add token", "create a variant", "update a component", "bump version", "dep… |
| `design-superpowers:ds-manage` | ✅ | Use for DS operations — publishing cascades, adoption analytics, documentation generation, health and drift monitoring. Activates for /ds-manage, "publish", "release cascade", "adoption report", "generate docs", "uspec"… |
| `design-superpowers:ds-producer` | ✅ | Use when creating, updating, auditing, documenting, versioning, or publishing DS components, foundations, icons, or patterns. Also use when managing Shortcut tickets for DS work or running governance checklists. |
| `design-superpowers:figma-setup` | ✅ | Install or verify PluginOS for Figma work in design-superpowers. Use when the user runs `/figma-setup`, asks how to set up Figma integration, or hits a Figma command without PluginOS installed. |
| `design-superpowers:map-design` | ✅ | Use to extract design language from an existing artifact (screenshot, URL, Figma file, or codebase) and generate a DESIGN.md. Activates for /map-design, "extract tokens", "generate DESIGN.md", "crawl this design", "docu… |

### frontend-design `v1.1.1`

_Frontend design skill for UI/UX implementation_

| Skill | | Description |
|---|---|---|
| `frontend-design:frontend-design` | ✅ | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't read as templated defaults. |

### image-generation `v1.0.0`

_Model-agnostic prompting guide for modern text-to-image models. Distilled from public guides for Imagen, Gemini Image, GPT Image, DALL-E, Stable Diffusion, Flux, Ideogram, Leonardo, and Midjourney._

Source: https://github.com/ahmedraza28/image-generation-skill

| Skill | | Description |
|---|---|---|
| `image-generation:image-generation` | ✅ | Best practices for prompting any text-to-image model (e.g. Imagen, Gemini Image, GPT Image, DALL·E, Stable Diffusion, Flux, Ideogram, Leonardo, Midjourney) to produce predictable, production-quality images. Use this ski… |

### superdesign `v0.6.0`

_Design or redesign frontend UI, presentations, and marketing graphics on the Superdesign infinite canvas. Uses approved slide outlines, project context, and branchable drafts you refine._

Source: https://superdesign.dev

| Skill | | Description |
|---|---|---|
| `superdesign:superdesign` | ✅ | Design or redesign frontend UI, presentations, and graphics on the Superdesign canvas with a choice of leading AI models. Use whenever the user wants to design a page, feature, flow, slide deck, or brand-new product; im… |

**Slash commands:** `/superdesign:commit` — Analyze git changes and create a commit without Claude Code attribution

## Web search, scraping & browsing

### auto-research `v1.0.0`

_Autonomous skill improvement through parallel research agents using the autoresearch methodology_

Source: https://github.com/gyoz-ai/auto-research

| Skill | | Description |
|---|---|---|
| `auto-research:auto-research` | ✅ | Autonomous skill improvement through parallel research agents. Applies the autoresearch methodology (Karpathy) to iteratively improve an existing Claude Code skill. Spawns 5 research agents, synthesizes findings, then e… |

### browser-use

_Give Claude a real browser — your Chrome or a Browser Use Cloud browser. Use it whenever a task involves a website or web app: browsing, scraping and data extraction, filling forms, testing sites, taking screenshots, automating web workflows._

Source: https://github.com/browser-use/browser-use · MCP: `browser-use`

### context7

_Upstash Context7 MCP server for up-to-date documentation lookup. Connects to Context7's hosted remote MCP server (https://mcp.context7.com/mcp) — no local Node.js or npx required — to pull version-specific documentation and code examples directly from source repositories into your LLM context. Authenticate with Context7 when prompted._

MCP: `context7`

### exa `v3.4.1`

_Exa web search, content fetching, and multi-step research via MCP tools and skills._

Source: https://github.com/exa-labs/exa-mcp-server · MCP: `exa`

| Skill | | Description |
|---|---|---|
| `exa:exa-agent` | ✅ | Use Exa Agent for multi-step web research, list-building, enrichment, structured output, run continuation, and coverage validation. Exa Agent can access additional data providers: fiber, financial_datasets, similarweb, … |
| `exa:search` | ✅ | Deep research powered by Exa. Use for lead generation, literature reviews, deep dives, competitive analysis, or any query where one search falls short, including phrases like 'research this', 'find everything about', 'f… |

### firecrawl `v1.0.9`

_Scrape, search, crawl, and map the web with a single command._

| Skill | | Description |
|---|---|---|
| `firecrawl:firecrawl` | ✅ | Any live-web task via the Firecrawl CLI — including ordinary web research: searching the web, reading or extracting pages, gathering sources, discovering site URLs, bulk extraction, downloading a site, change alerts, or… |
| `firecrawl:firecrawl-agent` | ✅ | Autonomous multi-page extraction into structured JSON. Use when the user wants website data matching a schema — pricing tiers, product listings — beyond a single-page scrape. |
| `firecrawl:firecrawl-crawl` | ✅ | Bulk-extract many pages from one site or section. Use for "crawl", "everything under /docs", or content spanning linked pages. |
| `firecrawl:firecrawl-developer-index` | ✅ | Search issues, merged pull requests, READMEs, and documentation. Use when the question is how a library or API behaves, what an error means, or whether a bug was fixed; prefer this over a general web page. |
| `firecrawl:firecrawl-download` | ✅ | Save a site or section as local files (markdown, screenshots). Use for "download the site", offline docs, or a local copy for reference. |
| `firecrawl:firecrawl-interact` | ✅ | Drive a live browser on a scraped page: click, fill forms, log in, paginate, infinite-scroll. Use when content requires interaction or a scrape failed or returned incomplete content. |
| `firecrawl:firecrawl-map` | ✅ | Discover and list a site's URLs, with search filtering. Use for "map the site" or "find the URL for" requests — when the user knows the site but not the exact page, or wants site structure. |
| `firecrawl:firecrawl-monitor` | ✅ | Alert by webhook/email on web changes — use for "monitor/watch/track/alert me when": recurring checks on known URLs (prefer over repeated one-off scrapes) or web-wide watches for new results (queries + goal). |
| `firecrawl:firecrawl-parse` | ✅ | Convert a local file (PDF, DOCX, XLSX, HTML, …) to markdown, or answer questions about its content. Use whenever the input is a file path, not a URL. |
| `firecrawl:firecrawl-research-index` | ✅ | Find the papers that answer a research query in Firecrawl's research paper index — a corpus of paper abstracts whose largest share is biomedical and life-science literature (PubMed, bioRxiv, medRxiv), alongside arXiv pr… |
| `firecrawl:firecrawl-scrape` | ✅ | Extract a URL's content as clean markdown, including JS-rendered pages. Use whenever the user provides a URL and wants its content; prefer over WebFetch. |
| `firecrawl:firecrawl-search` | ✅ | Web search with full page content. Use when no URL is known: finding sources, articles, or news. For papers use firecrawl-research-index; for library, API, error, or bug questions use firecrawl-developer-index. |

**Slash commands:** `/firecrawl:skill-gen` — Generate a complete Agent Skill from a documentation URL using Firecrawl

### playwright

_Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, click elements, and perform automated browser testing workflows._

MCP: `playwright`

### tavily `v2.0.0`

_Build AI applications with real-time web data using Tavily's search, extract, crawl, and research APIs._

Source: https://docs.tavily.com

| Skill | | Description |
|---|---|---|
| `tavily:tavily-best-practices` | ✅ | Build production-ready Tavily integrations with best practices baked in. Reference documentation for developers using coding assistants (Claude Code, Cursor, etc.) to implement web search, content extraction, crawling, … |
| `tavily:tavily-entity` | ✅ | Fill in a company, person, or organization for a CRM from the web, using Tavily, including a CSV of rows the user already has. Identifies the right entity when others share the name, then fills the fields from authorita… |
| `tavily:tavily-list` | ✅ | Build a deduplicated table of matches for a set, using Tavily. The table is what search returned, not every match that exists. Use when the user wants a list, all of something, or a table with duplicates removed. Confir… |
| `tavily:tavily-monitor` | ✅ | Build a Tavily search or extraction that runs on a cadence, with a saved baseline. Search monitors set max_age_hours to the interval so a cached copy from before it is not returned. Use when the user wants to monitor, t… |
| `tavily:tavily-research` | ✅ | Research a topic in depth with Tavily. Use this skill when a question needs many sources gathered and weighed together: analysing a market, policy, technology or trend, comparing options across several criteria, reviewi… |
| `tavily:tavily-search` | ✅ | Use this skill whenever a task needs the web: searching for information, checking current facts or news, finding sources, reading a URL, finding a page on a site, or collecting many pages from a site. Use it for anythin… |

## Academic research & writing

### research-superpowers `v0.41.1` ⏸ off by plugin profile

_Skill-driven research workflow for Claude Code and Cowork: idea → literature → ingest → analysis → draft → peer-review → publication. Methodology-aware (hermeneutic / quantitative / mixed). Focus-driven ingest: source pages capture project-specific extraction (claims relevant to a research focus), not generic summaries. MCP-aware: optional dao-paper-search-mcp + dao-searxng-mcp integration for ve…_

Source: https://github.com/leiverkus/research-superpowers · Has hooks

| Skill | | Description |
|---|---|---|
| `research-superpowers:acquire-sources` | ⏸ | Use AFTER literature-review and BEFORE ingest-source to obtain the actual PDFs for the A+B graded sources. Auto-downloads Open-Access PDFs into the shared library (<library>/pdf/<bibkey>.pdf — the bibkey IS the filename… |
| `research-superpowers:add-to-library` | ⏸ | Add ONE document (a PDF) directly to the shared master library — outside the project ingest flow. Auto-discovers the bibliographic metadata, VERIFIES it against Crossref/OpenAlex (never guessing), derives keywords cheap… |
| `research-superpowers:brainstorming-research` | ⏸ | Use BEFORE any research work — defining a question, planning a study, starting a chapter, proposing a grant. Explores intent, state of the field, methodology, feasibility, and ethics, then writes a design doc and gets u… |
| `research-superpowers:drafting-manuscript` | ⏸ | Use to draft a book chapter, article section, or grant exposé from synthesized wiki content. Settles the argument architecture with the user first, then drafts section by section — each section's argument agreed before … |
| `research-superpowers:drift-report` | ⏸ | Use to check the shared library, the current wiki, and all registered projects for accumulated drift — un-indexed PDFs, scans without a text layer, PDF bloat, project-bib keywords not yet merged into the master, cross-p… |
| `research-superpowers:executing-research-plan` | ⏸ | Use AFTER writing-research-plan has produced a ready plan (status=ready for hermeneutic projects, status=pre-registered for quantitative/mixed). Reads `input/ideas/<slug>-plan.md`, creates TodoWrite items, runs a pre-in… |
| `research-superpowers:finishing-a-research-project` | ⏸ | Use when a research project reaches completion — manuscript finalized, peer-review cleared, ready for publication / submission / archive. Runs the final checklist across rendering, BibTeX, wiki, data, reproducibility, a… |
| `research-superpowers:grant-finder` | ⏸ | Use for researching German and European funding programs (DFG, ERC, VolkswagenStiftung, Gerda Henkel, Fritz Thyssen, bilateral DE-IL) for projects in theology, biblical archaeology, digital humanities. Produces a DFG-st… |
| `research-superpowers:ingest-source` | ⏸ | Use when adding a scholarly source (PDF, book chapter, article) to the research project wiki under a specific focus. Produces a focus-driven Source page (claims relevant to the project, not a generic summary), extracts … |
| `research-superpowers:literature-review` | ⏸ | Systematic literature search for theology, biblical archaeology, ancient history, and digital humanities. Triggers on "literature review on X", "Stand der Forschung zu X", "Literaturrecherche zu X". NOT for single-paper… |
| `research-superpowers:requesting-peer-review` | ⏸ | Use when a manuscript (book chapter, article, grant) is drafted and ready for structured review. Runs a two-stage peer-review workflow — constructive then adversarial — with discipline-specific checklists (CONSORT/STROB… |
| `research-superpowers:scaffold-research-project` | ⏸ | Use to create a new research project from the template via conversation — no terminal, no `cp` commands. Asks for project name, parent directory, methodology, discipline, and languages; copies the template tree using th… |
| `research-superpowers:semantic-wiki-review` | ⏸ | Use when the user asks for a *content* review of the wiki — contradictions between pages, outdated claims overtaken by newer sources, weakly supported assertions, missing cross-references that the structural linter cann… |
| `research-superpowers:using-research-powers` | ⏸ | Use when starting any research conversation — establishes how to find and use research skills. Requires Skill tool invocation before ANY response, including clarifying questions. Governs the full research workflow from … |
| `research-superpowers:wiki-graph` | ⏸ | Use to build and analyse the knowledge wiki as a graph. Runs `scripts/wiki-to-graph.py` (from the research project template) to export an interactive self-contained graph.html (open in any browser, no install) plus grap… |
| `research-superpowers:wiki-lint` | ⏸ | Use to validate the knowledge wiki — frontmatter completeness, broken wikilinks, orphaned pages, status consistency. Wraps `scripts/lint-wiki.py` from the research project template. Required before drafting and before f… |
| `research-superpowers:writing-research-plan` | ⏸ | Use AFTER brainstorming-research has produced an approved design doc. Converts the design into a pre-registered research plan with falsifiable hypothesis, concrete task list, and verification criteria. No execution happ… |

**Subagents** (`Agent(subagent_type=…)`):

- `research-superpowers:analyst` — Dispatched by executing-research-plan for analysis tasks. Writes and runs Python/R scripts in output/data-analysis/, produces reproducible results with assumption checks. Fresh context per dispatch.
- `research-superpowers:drafter` — Dispatched by drafting-manuscript for one section whose argument sketch has been approved. Produces that section's prose from named synthesis + source pages, with inline citations, carrying out the a…
- `research-superpowers:literature-scout` — Dispatched by literature-review skill. Executes database queries across OpenAlex, IxTheo, Zenon-DAI, Propylaeum, Persée, OpenEdition, CORE, BASE, Crossref, DNB, arXiv. Returns graded candidate list w…
- `research-superpowers:peer-reviewer` — Dispatched by requesting-peer-review. Reviews a manuscript in one of two roles — constructive or adversarial — and produces a structured review report. Fresh context per dispatch.
- `research-superpowers:source-acquirer` — Dispatched by acquire-sources for large worklists (≥ ~8 sources). Runs the resolve→curl→validate download batch for the A+B graded sources and returns a compact status table. Isolates the noisy downl…
- `research-superpowers:source-ingester` — Dispatched by ingest-source or executing-research-plan. Reads ONE source PDF/text under a specific focus and produces a focus-driven Source page + entity pages + BibTeX entry + log line. Re-ingest of…
- `research-superpowers:wiki-linter` — Dispatched by wiki-lint for large wikis (>50 pages) or heavy cleanup. Runs lint, categorizes findings, applies safe fixes, reports decisions needed. Fresh context per dispatch.

## Writing, tone & humanizing

### caveman `v1.3.2`

_Make Claude answer short and to the point: answer or code first, no filler, no repeated questions. A concise mode that saves reading time and output tokens._

Source: https://petrovicistefan.ro

| Skill | | Description |
|---|---|---|
| `caveman:caveman` | ✅ | Use when the user wants short, direct answers without filler, for quick questions or when they only need the code. |

**Slash commands:** `/caveman:caveman` — Switch to short, direct answers until you ask for normal answers

### humanize-kit `v2.2.0`

_AI pattern interrupter for Claude. Three skills — humanize, humanize-ig, voice-profiler — that build a voice fingerprint from your real writing and rewrite AI output to match it. Free + MIT. The free gateway to the paid Branded Mayhem skill lineup (https://brandedmayhem.com)._

Source: https://brandedmayhem.com · Has hooks

| Skill | | Description |
|---|---|---|
| `humanize-kit:humanize` | ✅ | AI pattern interrupter — rewrites AI-generated text to break the statistical patterns detectors (Pangram, GPTZero, Copyleaks) key on, then re-renders in YOUR authentic voice from a saved profile. Requires a voice profil… |
| `humanize-kit:humanize-ig` | ✅ | Rewrites text for Instagram captions — compact, lowercase, imperfect grammar, no em dashes, abbreviated phrasing. Breaks AI detection patterns and reads like a real person typed it on their phone. Loads your voice profi… |
| `humanize-kit:voice-profiler` | ✅ | Interactive writing voice profiler — interviews you about your writing style and analyzes your real writing samples to generate a voice profile file for use with /humanize. Run this once, then every piece of humanized c… |

### humanizer `v3.0.0`

_Remove signs of AI-generated writing from text and rewrite in the author's actual voice. Based on Wikipedia's Signs of AI Writing guide plus a statistical voice fingerprint built from the author's own corpus._

Source: https://github.com/adelaidasofia/humanizer · Has hooks

| Skill | | Description |
|---|---|---|
| `humanizer:humanizer` | ✅ | Remove signs of AI-generated writing from text and rewrite in the author's actual voice. Based on Wikipedia's "Signs of AI writing" guide plus a statistical voice fingerprint built from the author's own corpus. Three mo… |

### writing-skills `v0.6.0`

_16 production writing-style skills for AI agents: 9 measurable frameworks (plain language, ASD-STE100, AP journalism, GOV.UK, Orwell's rules) and 7 character voices, as portable SKILL.md files._

Source: https://writing-skills.builditwithai.xyz

| Skill | | Description |
|---|---|---|
| `writing-skills:asd-ste100` | ✅ | Use when writing technical procedures, instructions, warnings, maintenance manuals, or any text where every reader including non-native English speakers must understand exactly one meaning. |
| `writing-skills:bob-ross` | ✅ | Write calm, soothing, gently instructional prose in the voice of Bob Ross. Use when the user wants encouraging guidance, mistakes reframed as opportunities, a serene step-by-step tone, or down-to-earth warmth for nervou… |
| `writing-skills:business-writing` | ✅ | Write executive-grade business communication with BLUF (bottom line up front), active verbs, and zero buzzwords. Use when the user writes memos, status updates, emails to leadership, decision briefs, meeting recaps, or … |
| `writing-skills:corporate-communication` | ✅ | Write internal corporate communications — announcements, org changes, policy updates, launch messages — with clarity, honesty, and calibrated warmth. Use when the user writes company-wide emails, leadership messages, ch… |
| `writing-skills:google-dev-docs` | ✅ | Use when writing API documentation, READMEs, tutorials, reference guides, error messages, or any technical content for developers using the Google developer documentation style guide. |
| `writing-skills:gov-uk-style` | ✅ | Use when writing public-facing content, government or civic communication, help pages, policy summaries, or content requiring maximum-scope readability according to GOV.UK standards. |
| `writing-skills:jack-sparrow` | ✅ | Write flamboyant, mischievously grand, baroque-pirate prose in the voice of Captain Jack Sparrow. Use when the user wants playful, swashbuckling, theatrical, or entertainingly evasive writing; humor with pageantry; or a… |
| `writing-skills:journalism-ap` | ✅ | Write news, press releases, and journalistic content to the Associated Press Stylebook essentials — attribution, numbers, dates, no editorializing. Use when the user writes press releases, news summaries, media announce… |
| `writing-skills:orwells-rules` | ✅ | Apply George Orwell's 6 rules for clear, honest, and unpretentious writing from "Politics and the English Language" (1946). Use when the user asks for Orwell's rules, George Orwell style, cutting dead metaphors and clic… |
| `writing-skills:paddington` | ✅ | Write exceedingly polite, earnestly kind prose in the voice of Paddington. Use when the user wants warmth expressed as careful courtesy, gentle formality, a kindness-protocol tone, or when recounting mishaps calmly and … |
| `writing-skills:plain-language` | ✅ | Write in plain language per the US Plain Writing Act of 2010 and the Plain Language Action Network. Use when the user wants clearer, simpler, shorter writing; wants to improve readability; writes public-facing or govern… |
| `writing-skills:scott-adams` | ✅ | Use when the user wants to simplify prose, prune extra words, craft high-curiosity opening hooks, write punchy short sentences, and structure ideas for maximum human brain comprehension based on Scott Adams' famous busi… |
| `writing-skills:shrek` | ✅ | Write deadpan, dry, grumpy-but-warm prose in the voice of Shrek. Use when the user wants blunt honesty with humor, layered dirt-and-fairy-tale analogies, sarcasm that lands kindly, or anything too mushy that needs groun… |
| `writing-skills:ted-lasso` | ✅ | Write warm, high-EQ, folksy-optimistic content in the voice of Ted Lasso. Use when the user asks for an encouraging, kind, or optimistic tone; a motivational pep talk; reframing a negative or difficult topic constructiv… |
| `writing-skills:winnie-the-pooh` | ✅ | Write gentle, unhurried, childlike-wisdom prose in the voice of Winnie the Pooh. Use when the user wants soft, simple, comforting writing; musings that circle a thought kindly; or kindness expressed in plain small words… |
| `writing-skills:yoda` | ✅ | Write in the concise, inverted, aphorism-driven voice of Yoda. Use when the user wants wisdom framed sparely, a mentoring tone, short punchy sentences, or playful subject-object-verb inversion instead of default prose. |
| `writing-skills:template` | ⬜ | One sentence stating what this skill produces and per which standard or character. Use when the user [concrete trigger situations, the actual phrases they'd type, and the contexts where this beats default prose]. |

## Documents & office files

### anthropic-skills

| Skill | | Description |
|---|---|---|
| `anthropic-skills:artifact-emulator` | ✅ | See a page, slide deck or design canvas artifact you made, close to how a person will see it: open its files in the real artifact viewer inside this cloud session, then screenshot it and read its console errors with a s… |
| `anthropic-skills:built-in-browser` | ✅ | Read this skill before the first step that uses the built-in browser, the browser pane inside the Claude desktop app (also called the in-app browser, the browser pane, Claude's browser, or "your own browser"), whose too… |
| `anthropic-skills:chrome-browser` | ✅ | Read this skill before the first step that uses Claude in Chrome, the browser extension whose tools are named mcp__claude-in-chrome__* (also called Chrome, the browser extension, or the external browser) and which acts … |
| `anthropic-skills:computer-use` | ✅ | Read this skill before the first step of any request to do something in an app on the person's own computer (Notes, Finder, System Settings, any desktop app), to look at their screen, or for "computer use". Computer use… |
| `anthropic-skills:deep-research` | ✅ | Use this skill when the user's prompt requires (1) researching a topic across multiple sources, comparing options or alternatives, analyzing trends or history, understanding markets or industries, or reviewing literatur… |
| `anthropic-skills:doc-coauthoring` | ✅ | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users e… |
| `anthropic-skills:docs` | ✅ | docs (editable docs people share and comment on; the default for any document, named as a doc or not: a document, report, proposal, resume, cover letter, letter, contract, policy, form, template, worksheet, essay, handb… |
| `anthropic-skills:docx` | ✅ | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word templates (.dotx). Triggers include: any mention of Microsoft Word Documents, such as 'Word doc', 'word document… |
| `anthropic-skills:google-workspace` | ✅ | Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or changes a Google file. Use this skill whenever the user wants to create or change a Google Doc, Sheet or Slides… |
| `anthropic-skills:import-memory` | ✅ | Import a memory export from another AI assistant into Claude's memory — conversationally, additively, and with the content treated as data. |
| `anthropic-skills:learn` | ✅ | Use this skill when the user wants intellectual understanding — learning how or why something works, not getting a task done or soliciting Claude's judgment. Trigger for: - Explicit learning requests: teach, explain, EL… |
| `anthropic-skills:morning` | ✅ | Render the user's morning brief as a styled HTML artifact, or set it up as a recurring weekday task. Use only when the user explicitly asks to run, see, or set up their morning brief, or if they invoke /morning by name.… |
| `anthropic-skills:pdf` | ✅ | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding … |
| `anthropic-skills:pptx` | ✅ | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations as PowerPoint (.pptx) files; reading, parsing, or extr… |
| `anthropic-skills:skill-creator` | ✅ | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill p… |
| `anthropic-skills:xlsx` | ✅ | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .xltx, .csv, or .tsv file (e.g., adding columns,… |
| `anthropic-skills:algorithmic-art` | ⬜ | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. … |
| `anthropic-skills:benepass-reimbursement` | ⬜ | Submit expense reimbursements through Benepass (app.getbenepass.com). For users whose employer uses Benepass as their benefits platform. Handles login, benefit selection, form filling, receipt upload, and submission. Re… |
| `anthropic-skills:brand-guidelines` | ⬜ | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design… |
| `anthropic-skills:call-to-book` | ⬜ | Make a phone call to book an appointment or reservation. Checks calendar first, gets explicit consent before dialing, discloses AI identity on the call, and adds the booking to calendar when done. |
| `anthropic-skills:cancel-unsubscribe` | ⬜ | Cancel a subscription or unsubscribe from a service. Works from a description, a pasted charge line, a URL, or a photo/screenshot. Can also audit a full statement for recurring charges and cancel several at once. Finds … |
| `anthropic-skills:canvas-design` | ⬜ | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual design… |
| `anthropic-skills:event-planning` | ⬜ | Help plan an event — from a birthday dinner to a wedding. Scales to the size of the occasion. Handles venue research, guest lists, timelines, vendors, and budgets. |
| `anthropic-skills:file-expenses` | ⬜ | Help submit an expense or reimbursement on any platform. Detects the right tool (Benepass, Brex, Concur, Expensify, etc.), finds receipts, checks for duplicates, and walks through submission. |
| `anthropic-skills:file-form` | ⬜ | Handle small bureaucratic tasks — jury duty responses, parking tickets, passport renewals, DMV forms, permit applications, and other government or administrative paperwork. |
| `anthropic-skills:file-reading` | ⬜ | Use this skill when a file has been uploaded but its content is NOT in your context — only its path at /mnt/user-data/uploads/ is listed in an uploaded_files block. This skill is a router: it tells you which tool to use… |
| `anthropic-skills:financial-calculator` | ⬜ | Run financial calculations and scenario comparisons — tax estimates, loan comparisons, retirement projections, rent vs. buy, investment scenarios, and more. Pure math, no accounts or logins needed. |
| `anthropic-skills:frontend-design` | ⬜ | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't read as templated defaults. |
| `anthropic-skills:grocery-shopping` | ⬜ | Help order groceries for delivery. Concierge-style flow — store selection, occasion-based list building, budget tracking, and cart assembly. |
| `anthropic-skills:hire-help` | ⬜ | Help find and book a service provider for a task — cleaning, handyman, moving, assembly, yard work, errands, etc. Searches TaskRabbit, Handy, Thumbtack, and similar platforms. |
| `anthropic-skills:internal-comms` | ⬜ | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status… |
| `anthropic-skills:mcp-builder` | ⬜ | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services,… |
| `anthropic-skills:meal-delivery` | ⬜ | Help order food timed to arrive at a specific time. Works backward from target arrival, suggests restaurants, builds cart, and monitors delivery. |
| `anthropic-skills:paint` | ⬜ | Paint an original image in a watercolor style by writing code, not by calling an image model. Use when the user asks you to draw, paint, sketch, or make a picture of something and there is no image-generation tool avail… |
| `anthropic-skills:pdf-reading` | ⬜ | Use this skill when you need to read, inspect, or extract content from PDF files — especially when file content is NOT in your context and you need to read it from disk. Covers content inventory, text extraction, page r… |
| `anthropic-skills:prescription-refill` | ⬜ | Refill a prescription at a pharmacy. Works from a medication name, an Rx number, a photo of the bottle, or just "I'm running low." Confirms exactly what's being requested, gathers everything the pharmacy will ask for up… |
| `anthropic-skills:product-self-knowledge` | ⬜ | Stop and consult this skill whenever your response would include specific facts about Anthropic's products. Covers: Claude Code (how to install, Node.js requirements, platform/OS support, MCP server integration, configu… |
| `anthropic-skills:return-refund` | ⬜ | Help return an item or request a refund from any retailer. Identifies the item, finds the return policy, navigates the process, and handles shipping labels or phone calls. |
| `anthropic-skills:setup-writing-style` | ⬜ | Learns how the user writes from their own sent messages and docs, and builds a voice profile so future drafts sound like them instead of generic AI. The profile is saved as the my-writing-style skill. Use when the user … |
| `anthropic-skills:slack-gif-creator` | ⬜ | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for… |
| `anthropic-skills:theme-factory` | ⬜ | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creati… |
| `anthropic-skills:video-making` | ⬜ | Use this skill before making a new video. Not for editing a video file the user supplied. |
| `anthropic-skills:web-artifacts-builder` | ⬜ | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or … |

## Data & analytics

### data `v1.1.0`

_Write SQL, explore datasets, and generate insights faster. Build visualizations and dashboards, and turn raw data into clear stories for stakeholders._

MCP: `amplitude`, `amplitude-eu`, `atlassian`, `bigquery`, `databricks`, `definite`, `hex`, `snowflake`

| Skill | | Description |
|---|---|---|
| `data:analyze` | ✅ | Answer data questions -- from quick lookups to full analyses. Use when looking up a single metric, investigating what's driving a trend or drop, comparing segments over time, or preparing a formal data report for stakeh… |
| `data:build-dashboard` | ✅ | Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a shareable self-contained report, building a team monitoring snap… |
| `data:create-viz` | ✅ | Create publication-quality visualizations with Python. Use when turning query results or a DataFrame into a chart, selecting the right chart type for a trend or comparison, generating a plot for a report or presentation… |
| `data:data-context-extractor` | ✅ | Generate or improve a company-specific data analysis skill by extracting tribal knowledge from analysts. BOOTSTRAP MODE - Triggers: "Create a data context skill", "Set up data analysis for our warehouse", "Help me creat… |
| `data:data-visualization` | ✅ | Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building charts, choosing the right chart type for a dataset, creating publication-quality figures, or applying design principles … |
| `data:explore-data` | ✅ | Profile and explore a dataset to understand its shape, quality, and patterns. Use when encountering a new table or file, checking null rates and column distributions, spotting data quality issues like duplicates or susp… |
| `data:sql-queries` | ✅ | Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.). Use when writing queries, optimizing slow SQL, translating between dialects, or building comple… |
| `data:statistical-analysis` | ✅ | Apply statistical methods including descriptive stats, trend analysis, outlier detection, and hypothesis testing. Use when analyzing distributions, testing for significance, detecting anomalies, computing correlations, … |
| `data:validate-data` | ✅ | QA an analysis before sharing -- methodology, accuracy, and bias checks. Use when reviewing an analysis before a stakeholder presentation, spot-checking calculations and aggregation logic, verifying a SQL query's result… |
| `data:write-query` | ✅ | Write optimized SQL for your dialect with best practices. Use when translating a natural-language data need into SQL, building a multi-CTE query with joins and aggregations, optimizing a query against a large partitione… |

## Finance & markets

### equity-research `v0.1.2`

_Equity research tools: earnings analysis, initiating coverage reports, and research workflows_

Has hooks

| Skill | | Description |
|---|---|---|
| `equity-research:catalyst-calendar` | ✅ | Build and maintain a calendar of upcoming catalysts across a coverage universe — earnings dates, conferences, product launches, regulatory decisions, and macro events. Helps prioritize attention and position ahead of ev… |
| `equity-research:earnings-analysis` | ✅ | Create professional equity research earnings update reports (8-12 pages, 3,000-5,000 words) analyzing quarterly results for companies already under coverage. Fast-turnaround format focusing on beat/miss analysis, key me… |
| `equity-research:earnings-preview` | ✅ | Build pre-earnings analysis with estimate models, scenario frameworks, and key metrics to watch. Use before a company reports quarterly earnings to prepare positioning notes, set up bull/bear scenarios, and identify wha… |
| `equity-research:idea-generation` | ✅ | Systematic stock screening and investment idea sourcing. Combines quantitative screens, thematic research, and pattern recognition to surface new long and short ideas. Use when looking for new ideas, running screens, or… |
| `equity-research:initiating-coverage` | ✅ | Create institutional-quality equity research initiation reports through a 5-task workflow. Tasks must be executed individually with verified prerequisites - (1) company research, (2) financial modeling, (3) valuation an… |
| `equity-research:model-update` | ✅ | Update financial models with new data — quarterly earnings, management guidance, macro changes, or revised assumptions. Adjusts estimates, recalculates valuation, and flags material changes. Use after earnings, guidance… |
| `equity-research:morning-note` | ✅ | Draft concise morning meeting notes summarizing overnight developments, trade ideas, and key events for coverage stocks. Designed for the 7am morning meeting format — tight, opinionated, actionable. Triggers on "morning… |
| `equity-research:sector-overview` | ✅ | Create comprehensive industry and sector landscape reports covering market dynamics, competitive positioning, key players, and thematic trends. Use for client requests, sector initiations, thematic research pieces, or i… |
| `equity-research:thesis-tracker` | ✅ | Maintain and update investment theses for portfolio positions and watchlist names. Track key data points, catalysts, and thesis milestones over time. Use when updating a thesis with new information, reviewing position r… |

**Slash commands:** `/equity-research:catalysts` — View or update the catalyst calendar, `/equity-research:earnings` — Analyze quarterly earnings and create an earnings update report, `/equity-research:earnings-preview` — Build a pre-earnings preview with scenarios, `/equity-research:initiate` — Create an initiating coverage report, `/equity-research:model-update` — Update a financial model with new data, `/equity-research:morning-note` — Draft a morning meeting note, `/equity-research:screen` — Run a stock screen or generate investment ideas, `/equity-research:sector` — Create a sector overview report, `/equity-research:thesis` — Create or update an investment thesis

### finance `v1.3.0`

_Streamline finance and accounting workflows, from journal entries and reconciliation to financial statements and variance analysis. Speed up audit prep, month-end close, and keeping your books clean._

MCP: `bigquery`, `databricks`, `gmail`, `google calendar`, `slack`, `snowflake`

| Skill | | Description |
|---|---|---|
| `finance:audit-support` | ✅ | Support SOX 404 compliance with control testing methodology, sample selection, and documentation standards. Use when generating testing workpapers, selecting audit samples, classifying control deficiencies, or preparing… |
| `finance:close-management` | ✅ | Manage the month-end close process with task sequencing, dependencies, and status tracking. Use when planning the close calendar, tracking close progress, identifying blockers, or sequencing close activities by day. |
| `finance:financial-statements` | ✅ | Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis. Use when preparing a monthly or quarterly P&L, closing the books and need to flag mate… |
| `finance:journal-entry` | ✅ | Prepare journal entries with proper debits, credits, and supporting detail. Use when booking month-end accruals (AP, payroll, prepaid), recording depreciation or amortization, posting revenue recognition or deferred rev… |
| `finance:journal-entry-prep` | ✅ | Prepare journal entries with proper debits, credits, and supporting documentation for month-end close. Use when booking accruals, prepaid amortization, fixed asset depreciation, payroll entries, revenue recognition, or … |
| `finance:reconciliation` | ✅ | Reconcile accounts by comparing GL balances to subledgers, bank statements, or third-party data. Use when performing bank reconciliations, GL-to-subledger recs, intercompany reconciliations, or identifying and categoriz… |
| `finance:sox-testing` | ✅ | Generate SOX sample selections, testing workpapers, and control assessments. Use when planning quarterly or annual SOX 404 testing, pulling a sample for a control (revenue, P2P, ITGC, close), building a testing workpape… |
| `finance:variance-analysis` | ✅ | Decompose financial variances into drivers with narrative explanations and waterfall analysis. Use when analyzing budget vs. actual, period-over-period changes, revenue or expense variances, or preparing variance commen… |

### finance-tutor `v0.1.10`

_Finance Q&A learning FOR EDUCATIONAL PURPOSES ONLY, not financial advice._

| Skill | | Description |
|---|---|---|
| `finance-tutor:finance-tutor` | ⬜ | FOR EDUCATIONAL PURPOSES ONLY — not financial advice. This skill sets up a finance Q&A learning workflow. The user asks finance questions, each one is answered educationally with references, and every exchange is append… |

### lseg `v1.0.0`

_Price bonds, analyze yield curves, evaluate FX carry trades, value options, and build macro dashboards using LSEG financial data and analytics._

MCP: `lseg`

| Skill | | Description |
|---|---|---|
| `lseg:bond-futures-basis` | ✅ | Analyze the bond futures basis by pricing futures, identifying the cheapest-to-deliver, and comparing with yield curves to assess delivery option value and basis trading opportunities. Use when analyzing bond futures, c… |
| `lseg:bond-relative-value` | ✅ | Perform relative value analysis on bonds by combining pricing, yield curve context, credit spreads, and scenario stress testing. Use when analyzing bond richness/cheapness, computing spread decomposition, comparing bond… |
| `lseg:equity-research` | ✅ | Generate comprehensive equity research snapshots combining analyst consensus estimates, company fundamentals, historical prices, and macroeconomic context. Use when researching stocks, comparing estimates to actuals, an… |
| `lseg:fixed-income-portfolio` | ✅ | Review fixed income portfolios by pricing multiple bonds, retrieving reference data, analyzing cashflows, and running scenario analysis. Use when reviewing bond portfolios, computing portfolio duration and DV01, analyzi… |
| `lseg:fx-carry-trade` | ✅ | Evaluate FX carry trade opportunities by combining spot rates, forward points, interest rate differentials, volatility surface analysis, and historical price trends. Use when analyzing carry trades, comparing FX forward… |
| `lseg:macro-rates-monitor` | ✅ | Build macroeconomic and rates dashboards combining macro indicators, yield curves, inflation breakevens, and swap rates. Use when monitoring macro conditions, analyzing yield curve shape, decomposing real vs nominal rat… |
| `lseg:option-vol-analysis` | ✅ | Analyze option volatility by combining vol surface data, option pricing with Greeks, and historical price data to assess implied vs realized volatility. Use when pricing options, analyzing volatility surfaces, computing… |
| `lseg:swap-curve-strategy` | ✅ | Analyze the interest rate swap curve by pricing swaps at multiple tenors, overlaying government and inflation curves, and identifying curve trade opportunities. Use when analyzing swap curves, computing swap spreads, de… |

**Slash commands:** `/lseg:analyze-bond-basis` — Analyze the bond futures basis with CTD identification, implied repo rate, and basis trad…, `/lseg:analyze-bond-rv` — Analyze a bond's relative value vs yield curves and credit spreads with scenario stress t…, `/lseg:analyze-fx-carry` — Evaluate FX carry trade opportunities with spot, forwards, vol surface, and historical co…, `/lseg:analyze-option-vol` — Analyze option volatility with vol surface, Greeks, and implied vs realized vol comparison, `/lseg:analyze-swap-curve` — Analyze the swap curve with government and inflation overlays to identify curve trade opp…, `/lseg:macro-rates` — Build a macro and rates dashboard with economic indicators, yield curves, inflation, and …, `/lseg:research-equity` — Generate a comprehensive equity research snapshot with consensus estimates, fundamentals,…, `/lseg:review-fi-portfolio` — Review a fixed income portfolio with pricing, reference data, cashflows, and scenario ana…

### market-researcher `v0.1.1`

_Sector or theme to industry overview, competitive landscape, peer comps, and ideas shortlist_

| Skill | | Description |
|---|---|---|
| `market-researcher:competitive-analysis` | ✅ | Framework for building competitive landscape decks — market positioning, competitor deep-dives, comparative analysis, strategic synthesis. Use when the user asks for a competitive landscape, competitor analysis, peer co… |
| `market-researcher:comps-analysis` | ✅ | Build institutional-grade comparable company analyses with operating metrics, valuation multiples, and statistical benchmarking in Excel/spreadsheet format. **Perfect for:** - Public company valuation (M&A, investment a… |
| `market-researcher:idea-generation` | ✅ | Systematic stock screening and investment idea sourcing. Combines quantitative screens, thematic research, and pattern recognition to surface new long and short ideas. Use when looking for new ideas, running screens, or… |
| `market-researcher:pptx-author` | ✅ | Produce a .pptx file on disk (headless) instead of driving a live PowerPoint document — for managed-agent sessions with no open Office app. |
| `market-researcher:sector-overview` | ✅ | Create comprehensive industry and sector landscape reports covering market dynamics, competitive positioning, key players, and thematic trends. Use for client requests, sector initiations, thematic research pieces, or i… |

**Subagents** (`Agent(subagent_type=…)`):

- `market-researcher:market-researcher` — Produces sector or thematic market research — industry overview, competitive landscape, trading-comps spread of the peer set, and a thematic ideas shortlist — packaged as a research note with optiona…

### sp-global `v1.0.0`

_S&P Global - Financial data and analytics skills including company tearsheets, earnings previews, and transaction summaries_

MCP: `spglobal`

| Skill | | Description |
|---|---|---|
| `sp-global:earnings-preview-beta` | ✅ | Generate a concise 4-5 page equity research earnings preview for a single company. Analyzes the most recent earnings transcript, competitor landscape, valuation, and recent news to produce a professional HTML report. |
| `sp-global:funding-digest` | ✅ | Generate a polished one-page PowerPoint slide summarizing key takeaways from recent funding rounds and notable capital markets activity across a user's watched sectors or companies. Use this skill when the user asks for… |
| `sp-global:tear-sheet` | ✅ | Generate professional company tear sheets using S&P Capital IQ data via the Kensho LLM-ready API MCP server. Use this skill whenever the user asks for a tear sheet, company one-pager, company profile, fact sheet, compan… |

### vanguard-advisor-tools `v1.3.0`

_Research and evaluate investment products across the industry using Vanguard advisor tools in Claude. Compare and evaluate investments and prepare for client conversations._

MCP: `vanguard-advisors`

| Skill | | Description |
|---|---|---|
| `vanguard-advisor-tools:model-prep` | ✅ | Help a financial advisor find Vanguard model portfolios that match a client need, understand how those models are built, and produce a meeting-ready advisor one-pager — as text and as a styled PDF — with optional client… |

## Legal & governance

### ai-governance-legal `v1.0.2`

_Triages proposed AI use cases against your registry, runs impact assessments across the regimes in scope, reviews vendor AI terms for training-on-data and liability gaps, and keeps your AI policy current with practice._

MCP: `Google Drive`, `Slack`

| Skill | | Description |
|---|---|---|
| `ai-governance-legal:ai-inventory` | ✅ | EU AI Act per-system inventory — track each AI system's role (provider, deployer, importer, distributor, authorized representative, product manufacturer) and risk tier (prohibited, high-risk, limited, minimal, GPAI, GPA… |
| `ai-governance-legal:aia-generation` | ✅ | Run an AI impact assessment — structured intake, risk analysis, regulatory classification per regime in scope, policy consistency diff, and recommendation with conditions. Uses the house-style structure learned from the… |
| `ai-governance-legal:cold-start-interview` | ✅ | Run the cold-start interview — learns your AI governance practice and writes `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` from your AI policy, a reference impact assessment, and key vendor A… |
| `ai-governance-legal:customize` | ✅ | Guided customization of your AI governance practice profile — change one thing without re-running the whole cold-start interview. Adjust risk posture, escalation contacts, use-case registry entries, vendor AI positions,… |
| `ai-governance-legal:matter-workspace` | ✅ | Manage matter workspaces — new, list, switch, close, or detach (practice-level). File-management logic for keeping one client or engagement's context separate from every other. Use when working across multiple clients o… |
| `ai-governance-legal:policy-monitor` | ✅ | Keep the AI policy current with practice — weekly sweep of saved AIAs, triage results, and vendor reviews to find policy drift, or direct query for a proposed new AI practice. Use when user says "policy sweep", "does ou… |
| `ai-governance-legal:policy-starter` | ✅ | Draft a firm AI usage policy from published model policies, adapted to your practice profile — a research-and-synthesis tool whose output is a draft for attorney review and adoption, not a finished policy. Use when user… |
| `ai-governance-legal:reg-gap-analysis` | ✅ | Diff a new AI regulation or guidance against your current governance posture — surfaces gaps, priorities, and a remediation plan with owners and deadlines. Use when an AI regulation moves (or you learn about one you mis… |
| `ai-governance-legal:use-case-triage` | ✅ | Classify a proposed AI use case against your registry — approved, conditional, or not approved — and produce required conditions and next steps. Flags cross-plugin handoffs to privacy or product counsel. Use when user s… |
| `ai-governance-legal:vendor-ai-review` | ✅ | Review vendor AI terms — agreement, addendum, or ToS AI provisions — against your governance positions; flag training-on-data, liability, model changes, and AI policy consistency. Use when user says "review this AI agre… |

## Productivity, notes & memory

### agent-memory `v0.1.0`

_Save 60-90% on LLM token costs with intelligent memory compression for multi-agent systems_

Source: https://github.com/Keshab0310/agent-memory · MCP: `agent-memory` · Has hooks

| Skill | | Description |
|---|---|---|
| `agent-memory:memory-search` | ✅ | Search past work and observations across sessions |

### claude-memory `v1.0.0`

_Structured memory system for Claude Code — categorized memories with recall/remember patterns, startup injection, and file templates_

Source: https://github.com/tars23364-bit/claude-memory · Has hooks

| Skill | | Description |
|---|---|---|
| `claude-memory:structured-memory` | ✅ | This skill should be used when the user asks to "set up memory", "configure memory", "add memory to my project", "remember things across sessions", or mentions wanting Claude to recall past decisions, preferences, or co… |

### desktop-commander `v0.2.0`

_MCP server for terminal commands, process management, and file operations across text files, code, PDF, DOCX, Excel, images, and structured data_

Source: https://desktopcommander.app · MCP: `desktop-commander`

| Skill | | Description |
|---|---|---|
| `desktop-commander:ai-tools-setup` | ✅ | Set up, connect, validate, and repair Claude Desktop and MCP servers using Desktop Commander — inspecting and fixing mcp.json / claude_desktop_config.json, getting MCP servers to connect, and diagnosing local AI tooling… |
| `desktop-commander:computer-health-check` | ✅ | Run a comprehensive, read-only health check on the user's computer and return a scored chat summary with prioritized, plain-English recommendations and safe cleanup suggestions. Use this whenever the user wants to check… |
| `desktop-commander:desktop-commander-overview` | ✅ | Use for Desktop Commander MCP capabilities — persistent shells and REPLs, long-running processes, filesystem beyond the workspace, structured files (.xlsx, .docx, .pdf, images) and large local data files such as CSVs, r… |
| `desktop-commander:knowledge-base` | ✅ | Create and maintain a Markdown knowledge base that any AI agent can read, search, and update. Use when the user wants to start a knowledge base, add or update notes, organize docs/notes for an agent or LLM to consume, b… |
| `desktop-commander:obsidian-vault` | ✅ | Organize Obsidian vaults with MOCs, wikilinks, frontmatter/properties, dashboards, orphan-note checks, and cleanup workflows. Use ONLY when the user explicitly refers to Obsidian — by naming "Obsidian", an Obsidian "vau… |
| `desktop-commander:terminal` | ✅ | Use Desktop Commander for terminal and command-line work, especially anything that needs a shell whose state persists across turns: Python/Node REPLs, database shells, dev servers and other long-running processes, SSH i… |

### Notion `v0.1.0`

_Notion Skills + Notion MCP server packaged as a Claude Code plugin._

Source: https://github.com/makenotion/claude-code-notion-plugin · MCP: `notion`

| Skill | | Description |
|---|---|---|
| `Notion:knowledge-capture` | ⬜ | Transforms conversations and discussions into structured documentation pages in Notion. Captures insights, decisions, and knowledge from chat context, formats appropriately, and saves to wikis or databases with proper o… |
| `Notion:meeting-intelligence` | ⬜ | Prepares meeting materials by gathering context from Notion, enriching with Claude research, and creating both an internal pre-read and external agenda saved to Notion. Helps you arrive prepared with comprehensive backg… |
| `Notion:research-documentation` | ⬜ | Searches across your Notion workspace, synthesizes findings from multiple pages, and creates comprehensive research documentation saved as new Notion pages. Turns scattered information into structured reports with prope… |
| `Notion:spec-to-implementation` | ⬜ | Turns product or tech specs into concrete Notion tasks that Claude code can implement. Breaks down spec pages into detailed implementation plans with clear tasks, acceptance criteria, and progress tracking to guide deve… |

**Slash commands:** `/Notion:create-database-row` — Insert a new row into a specified Notion database using natural-language property values., `/Notion:create-page` — Create a new Notion page, optionally under a specific parent, using the Notion Workspace …, `/Notion:create-task` — Create a new task in the user’s Notion tasks database with sensible defaults., `/Notion:database-query` — Query a Notion database by name or ID and return structured, readable results., `/Notion:find` — Quickly find pages or databases in Notion by title keywords., `/Notion:search` — Search the user’s Notion workspace using the Notion MCP server and Notion Workspace Skill., `/Notion:tasks:build` — Build a task from a Notion page URL, `/Notion:tasks:explain-diff` — Makes a Notion doc explaining a code change., `/Notion:tasks:plan` — Plan a task from a Notion page URL, `/Notion:tasks:setup` — Set up a Notion task board for tracking tasks

### obsidian-notes `v0.2.1`

_Reads, writes and maintains markdown so it works as an Obsidian vault and still renders on GitHub and in VS Code: a lint for broken and ambiguous links, orphans, duplicate basenames, missing index files and bad frontmatter; an index (map of content) writer; a wikilink-to-relative-markdown-link converter; one command to set a folder up as a vault; and the official Obsidian CLI when it is enabled. …_

Source: https://github.com/m4bwav/obsidian-notes

| Skill | | Description |
|---|---|---|
| `obsidian-notes:obsidian-notes` | ✅ | Makes a folder of markdown work as an Obsidian vault that still renders on GitHub and in VS Code: lints for broken, mis-cased or ambiguous links, orphans, duplicate basenames, missing indexes and bad frontmatter (script… |

### productivity `v1.3.1`

_Manage tasks, plan your day, and build up memory of important context about your work. Syncs with your calendar, email, and chat to keep everything organized and on track._

MCP: `asana`, `atlassian`, `clickup`, `gmail`, `google calendar`, `linear`, `monday`, `notion`, `slack`

| Skill | | Description |
|---|---|---|
| `productivity:memory-management` | ✅ | Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal language so Claude understands requests like a colleague would. CLAUDE.md for working memory, … |
| `productivity:start` | ✅ | Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your existing task list, or decoding the shorthand (nicknames, acronyms, pr… |
| `productivity:task-management` | ✅ | Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help tracking commitments. |
| `productivity:update` | ✅ | Sync tasks and refresh memory from your current activity. Use when pulling new assignments from your project tracker into TASKS.md, triaging stale or overdue tasks, filling memory gaps for unknown people or projects, or… |

## Media (video/audio)

### ffmpeg-llm `v0.1.0`

_Helps Claude Code generate accurate, efficient FFmpeg commands from natural-language descriptions._

Source: https://github.com/rendi-api/ffmpeg-llm · Has hooks

| Skill | | Description |
|---|---|---|
| `ffmpeg-llm:ffmpeg-command` | ✅ | Use when the user describes a video or audio operation in natural language and needs the corresponding FFmpeg command — transcoding, trimming, concatenating, extracting audio, changing resolution/bitrate/codec, applying… |

**Slash commands:** `/ffmpeg-llm:ffmpeg` — Generate an FFmpeg command from a natural-language description.

**Subagents** (`Agent(subagent_type=…)`):

- `ffmpeg-llm:ffmpeg-expert` — Use when an FFmpeg task needs deep analysis — diagnosing failed commands, optimizing encoder settings for size/quality tradeoffs, or designing complex filtergraphs with multiple inputs and outputs.

### video-cleanup `v1.0.1`

_Clean up speech audio (AI noise removal, loudness, stereo fixes) and picture quality in talking-head and demo videos, and add a logo watermark, name lower third and end card. Runs locally in Claude Code; needs Python and ffmpeg (Windows, macOS, Linux)._

Source: https://github.com/Mehdi-Ks/video-cleanup

| Skill | | Description |
|---|---|---|
| `video-cleanup:video-cleanup` | ✅ | Fix the audio and picture of talking-head / interview / product-demo videos and add simple branding, using ffmpeg plus an AI speech denoiser. Use this whenever someone wants a video's voice cleaned up (background noise,… |

### watch-video `v1.0.0`

_Make Claude watch any video. Local file, public URL (yt-dlp), or Jira attachment (fully automated). Extracts keyframes with ffmpeg, transcribes with local faster-whisper or hosted Groq/OpenAI Whisper, and produces a paste-ready evidence-bundle Markdown report._

Source: https://github.com/MarcinSufa/claude-watch-video

| Skill | | Description |
|---|---|---|
| `watch-video:watch-video` | ✅ | Make Claude "watch" a video — local file, public URL (yt-dlp), or Jira attachment (fully automated when an Atlassian API token is configured). Extracts keyframes with ffmpeg and transcribes audio with faster-whisper (mu… |

### youtube-transcriber `v1.1.0`

_Transcribe YouTube videos and playlists using browser-based caption extraction — free, no API key needed_

Source: https://msapps.mobi/plugins

| Skill | | Description |
|---|---|---|
| `youtube-transcriber:youtube-transcriber` | ✅ | Transcribe YouTube videos and playlists by extracting auto-generated captions directly from the browser — no API key, no external service, completely free. Trigger on: "transcribe this video", "transcribe this playlist"… |

## Career & personal

### adhd-study-coach `v0.1.1`

_A single study-companion agent for ADHD learners, any subject: automatic spaced-repetition warm-ups, small-chunk teaching, Feynman-style reflection, and periodic self-analysis — grounded in cited learning-science and ADHD research (see RESEARCH.md)._

Source: https://github.com/itsAalaa7/adhd-study-coach

**Subagents** (`Agent(subagent_type=…)`):

- `adhd-study-coach:adhd-study-coach` — Your ongoing ADHD-friendly study companion, for any subject. Use this to start a study session, review what's due, learn something new, wrap up and reflect, or check in on your learning patterns. Han…

### github-portfolio-builder `v1.1.0`

_Reviews a GitHub profile or repository as portfolio evidence. Returns up to five ranked improvements, each with a direct evidence link and a verified, reported, inferred, or unresolved label._

Source: https://github.com/RachaelQuisel/github-portfolio-builder

| Skill | | Description |
|---|---|---|
| `github-portfolio-builder:github-portfolio-builder` | ✅ | Review a GitHub profile or repository as professional portfolio evidence and suggest prioritized improvements. Use for GitHub presentation, case studies, reusable examples, attribution, licensing, and claim verification… |

### rankedin `v0.1.1`

_Understand where you stand professionally and decide what to do next. Get direction on your next career move, a job search that isn't working, changing careers, AI changing your job, or building your professional reputation — right away, with no upload. Add your own LinkedIn data export for personal profile scores, strengths and gaps, peer comparison, AI resilience and network insight._

Source: https://rankedin.app · MCP: `rankedin`

| Skill | | Description |
|---|---|---|
| `rankedin:next-career-move` | ✅ | Help the user decide what to do next in their career with rankedin. Use when they say they feel stuck, need a change, don't know what to do next, or aren't sure what their next move should be; when they ask what their n… |
| `rankedin:profile-review` | ✅ | Assess the user's own professional profile with rankedin. Use when they ask to analyze or review their LinkedIn profile, how strong their profile is, what their strengths or biggest gaps are, how they compare with peers… |

### resumenext-linkedin-resume `v1.0.0`

_Review the text of a LinkedIn profile section by section and turn it into a resume that opens in the ResumeNext editor._

Source: https://resumenext.io/mcp#linkedin · MCP: `resumenext-linkedin-resume`
