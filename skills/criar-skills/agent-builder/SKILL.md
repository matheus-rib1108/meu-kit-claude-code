---
name: agent-builder
description: Creates the user's own personal AI agents (Claude Code subagents) for any recurring task — e.g. a study assistant, a social-media assistant, a client-site builder, an Obsidian librarian — and registers them so Claude picks them automatically. Use when the user asks to "criar um agente", "minha IA para…", "um assistente que…", or wants a repeatable specialist.
---

# Agent builder

An agent is a Markdown file in `.claude/agents/<name>.md` (this project) or
`~/.claude/agents/<name>.md` (all projects on the user's computer).

## 1. Interview (max 4 short questions, skip what's already clear)
- What should it do, with an example request?
- What must it never do? (e.g. never send messages or publish without confirmation)
- Which tools/places does it use? (web search, files, Obsidian, Notion, Vercel, browser)
- Style of the answer (short? Portuguese? table?).

## 2. Write the file
```markdown
---
name: kebab-case-name
description: "Use this agent when <concrete triggers, in the user's words too>. <What it delivers>."
tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch   # only what it needs
model: sonnet            # sonnet = fast/cheap; opus = hardest reasoning
---

You are <role> for <user>. <Goal in one sentence>.

## How you work
1. ...
## Rules
- Never <hard limits>.
- Answer in Portuguese, <style>.
## Output
<exact format>
```
Rules: the `description` decides when it's used — make it specific. Give the fewest tools
possible (security + fewer tokens). MCP tools are listed by name (e.g. `mcp__notion__*`) only
if that server is configured. Reuse existing skills by naming them in the body.

## 3. Register and test
- Add a row to the team table in `CLAUDE.md` ("Pedido do usuário → quem faz").
- Test it with one realistic request; fix the prompt if it went off-track.
- Tell the user how to call it: just ask normally, or "usa o agente <name>".

## Ideas to offer
`estudos` (resume vídeos/PDFs into Obsidian notes) · `social-media` (scripts for Reels/TikTok,
content calendar in Notion) · `site-cliente` (runs the full site pipeline + `site-fortress` +
`cost-estimator`) · `pesquisa-precos` · `organizador-obsidian`.
