<!-- Generated from CLAUDE.md by scripts/render_docs.py. Edit CLAUDE.md instead. -->
# AGENTS.md

Skills routing guide for any agent. In claude.ai, paste into Project instructions.

Load the matching skill with `Skill(skill="<id>")` before acting. Process skills first
(brainstorm, debug, plan), then implementation skills. User instructions win. If unsure or
the task isn't listed, load `skill-router` (full table: `docs/ROUTING.md`). A skill whose MCP
server is down will fail: say so and fall back.

**Always:** Claude API, models or pricing → `claude-api` (never from memory) · chart → `dataviz`
· Artifact page → `artifact-design` · settings, hooks or "whenever X" → `update-config`.

**Engineering:** idea or new feature → `superpowers:brainstorming` → `superpowers:writing-plans`
· run a plan → `superpowers:subagent-driven-development` · code with tests → `superpowers:test-driven-development`
· bug → `superpowers:systematic-debugging` · before saying "done" → `superpowers:verification-before-completion`
· parallel tasks → `superpowers:dispatching-parallel-agents` · finish a branch → `superpowers:finishing-a-development-branch`
· review → `code-review` · review feedback → `superpowers:receiving-code-review` · cleanup → `simplify`
· security → `security-review` · spec → `agent-protocols:spec-driven-development`
· API design → `agent-protocols:api-and-interface-design` · frontend → `frontend-design:frontend-design` · run the app → `run`.

**Research and documents:** web search → `firecrawl:firecrawl-search` · scrape → `firecrawl:firecrawl-scrape`
· deep research → `anthropic-skills:deep-research` · docx/pdf/pptx/xlsx → `anthropic-skills:<type>`
· humanize text → `humanizer:humanizer` · plain writing → `writing-skills:plain-language`.

**Meta:** new or edited skill → `skill-creator:skill-creator` · lasting preference → `task-observer:task-observer`
· memory → `claude-memory:structured-memory` · setup audit → `setup-audit:setup-audit` · recurring task → `loop`.

Off by default, enable per project: `zizi-skills`, `mattpocock-skills`, `research-superpowers`
(see `config/plugin-profile.yaml`).
