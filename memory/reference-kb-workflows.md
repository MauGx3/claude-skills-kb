---
name: kb-workflows
description: How the skills knowledge base is maintained: regenerate, test, plugin profile, desktop setup, PR and CI handling. Read before changing anything in claude-skills-kb.
type: reference
---

Repo: `MauGx3/claude-skills-kb` (private). Work on a branch, never directly on `main`. Open PRs as drafts. Mark ready for review only when the user asks.

**Regenerate after any change to config, plugins or routing**
1. `python3 scripts/build_catalog.py`. Rescans plugin folders (`~/.claude/plugins/synced` or `cache`) and writes `catalog/skills-catalog.json`.
2. `python3 scripts/render_docs.py`. Writes `docs/CATALOG.md`, `docs/ROUTING.md`, `AGENTS.md` (from CLAUDE.md), and `desktop/skill-router/` plus `desktop/skill-router.zip`. It exits 1 if any routed ID is missing or unavailable, if CLAUDE.md is over 2,500 chars, or if `desktop/instructions.md` is over 2,500 chars or names a skill that chat doesn't have.
3. `python3 -m unittest discover -s tests`. Must pass.
4. Never hand-edit generated files: `docs/`, `AGENTS.md`, `desktop/skill-router*`, `catalog/skills-catalog.json`. Edit `config/skills-config.yaml`, `config/plugin-profile.yaml`, `CLAUDE.md`, or `desktop/instructions.md`.
5. Commit the generated files together with the change. CI runs `render_docs.py` and fails on any `git status` difference under `docs AGENTS.md desktop`. A merge can make these stale: if a PR shows that failure after a merge from main, rerun render_docs and commit the result.

**Plugin profile** (`config/plugin-profile.yaml`)
- Turns plugins off at user scope with `claude plugin disable <name>@synced`. Dry run by default: `./install.sh plugins`. Apply with `./install.sh plugins --apply`, then restart Claude Code.
- Off by default: zizi-skills, mattpocock-skills, research-superpowers, contentasoft-cad-converter. Re-enable per project with `{"enabledPlugins": {"<name>@synced": true}}` in that project's `.claude/settings.json`.
- Two synced plugins share names (humanizer, caveman). Those can't be turned off with the local setting. The user must remove the duplicate on claude.ai.
- A plugin turned off on claude.ai is off everywhere, including Claude Code, and per-project settings can't bring it back.

**Installing**
- `./install.sh user`: merges CLAUDE.md into `~/.claude/CLAUDE.md` inside a managed block, with absolute paths. It's idempotent, makes a backup only when content changes, and installs skill-router.
- `./install.sh project <dir>`: CLAUDE.md, skill-router, and memory files for one repo.

**Desktop app (Chat and Cowork; Claude Code is the Code tab)**
- Chat reads its setup from the claude.ai account, not from `~/.claude`.
- Instructions: paste `desktop/instructions.md` into Settings → Your Claude → Instructions.
- Skill: upload `desktop/skill-router.zip` in Customize → Skills. Requires code execution and file creation.
- Give the user fresh copies from `main` after any routing change. Files sent earlier go stale.
- Don't paste CLAUDE.md into chat. It names Claude Code-only tools.

**PRs, CI and reviews**
- Branch from current `origin/main`. Commit with the attribution lines the session requires. Push with `git push -u origin <branch>`.
- `gh pr create` fails in this environment (GraphQL is blocked). Use `gh api repos/MauGx3/claude-skills-kb/pulls -f title=... -f head=... -f base=main -F draft=true -F body=@file`.
- CI: `test (ubuntu-latest)`, `test (macos-latest)`, shellcheck, and the up-to-date check. Also GitGuardian, WIP (passes once the PR is ready for review) and pre-commit.ci (passes now that `.pre-commit-config.yaml` exists).
- The `pre-commit.ci - pr` status was "private repos require a paid plan" before the config existed. It is now a real check.
- Copilot sometimes posts a `copilot` review check on ready PRs.
- Post at most one comment per external failure. Explain why it isn't the PR's.
- Use `subscribe_pr_activity` for a PR you're working on. `unsubscribe` when it's merged or closed. Cancel the pending `send_later` check-in then.

**Environment limits seen so far**
- Cloud sessions can attach only repos added with `add_repo`. Creating repos from the session fails with 403.
- Long `sleep` is blocked. Poll with checks, or use a scheduled check-in.
- The auto-mode classifier blocks some Bash commands, such as running `pre-commit` (it downloads and runs hook code). Use a local equivalent and say so.
