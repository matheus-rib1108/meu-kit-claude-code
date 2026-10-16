---
name: github-helper
description: Does everything Git and GitHub for the user — creates repositories, first commit and push, branches, pull requests, releases, GitHub Pages, and turns on GitHub's free security features (Dependabot, secret scanning, CodeQL, branch protection). Use when the user asks "cria um Git/repositório", "sobe pro GitHub", "faz um PR", "salva no GitHub", "organiza meu GitHub", or starts a new project.
---

# GitHub helper

Use whatever is available, in this order: GitHub MCP tools (`mcp__github__*`) → `gh` CLI
(`gh auth status`; if not logged in, the user runs `gh auth login` once) → plain `git`.

## New project
1. `git init`, sensible `.gitignore` (include `.env*`, `node_modules`, build output), README
   in Portuguese with what it is and how to run it.
2. Create the repo (private by default unless the user wants it public), push `main`.
3. Turn on security for every new repo:
   - Dependabot alerts + security updates (`.github/dependabot.yml` for npm/pip, weekly).
   - Secret scanning + push protection (Settings → Code security; free on public repos).
   - CodeQL default setup (`gh api -X PATCH repos/{owner}/{repo}/code-scanning/default-setup -f state=configured`).
   - Branch protection on `main`: require PR + passing checks for client projects.
4. Never commit secrets. If one was committed: rotate the key first, then clean history.

## Daily work
- Work on a branch, small commits with clear messages, PR to `main`, merge when CI is green.
- Before pushing: run the project's lint/tests; for sites, `site-fortress` before a release.
- Releases: tag `vX.Y.Z` + short changelog.

## Deploys from GitHub
Vercel/Netlify/Cloudflare connect to the repo and deploy each push (preview per PR).
Static sites can also use GitHub Pages (`gh api -X POST repos/{owner}/{repo}/pages ...`).
