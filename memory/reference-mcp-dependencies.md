---
name: mcp-dependencies
description: Skills that depend on MCP servers, and which servers failed to connect in the cloud sandbox
type: reference
---

Connected in the cloud session of 2026-11-07: Firecrawl, Figma, Claude_Docs, Google Drive, playwright, browser-use, desktop-commander.

Failed in that session (most were proxy 403s): context7, exa, github, Notion, slack, asana, atlassian, clickup, linear, monday, amplitude, bigquery, definite, hex, lseg, spglobal, vanguard-advisors, cloudflare, animatedwebs, rankedin, resumenext-linkedin-resume, qt-docs, abracadabrax-image-video, agent-memory. cad-converter failed differently: its `cmd` executable is not on Linux.

These skills need their MCP server: `lseg:*`, `sp-global:*`, `vanguard-advisor-tools:*`, `Notion:*`, `animatedwebs:*`, `rankedin:*`, `exa:*`, `agent-memory:memory-search`, `contentasoft-cad-converter:*`. Warehouse parts of `data:*`, `productivity:*` and `finance:*` need their connectors too.

**How to apply:** If one of these skills fails, tell the user which server is disconnected. Fall back where possible: exa → firecrawl, context7 → `firecrawl:firecrawl-developer-index`. In a cloud environment, the user can allow the host under the environment's network settings.
