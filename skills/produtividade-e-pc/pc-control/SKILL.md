---
name: pc-control
description: Gets Claude controlling the user's own computer and browser — opening programs (Obsidian, Notepad, VS Code…), using Chrome while logged in, creating accounts on sites, signing up for apps — with the least effort from the user. Use when the user asks Claude to "mexer no meu PC", "abrir o programa", "instalar a extensão", "criar uma conta pra mim", "entrar no site com meu login", or when a task needs their logged-in browser or a desktop app.
---

# PC control

## Where Claude is running decides what's possible
- **Cloud session** (claude.ai/code, the phone app's Code tab): runs in a remote container.
  It **cannot** touch the user's computer. Say so in one line and give the setup below.
- **Claude desktop app with computer use on**: can see the screen, click, type, open any app.
- **Claude Code on the user's computer**: terminal + files; with Claude in Chrome
  (`claude --chrome`) or the `browser-use` / `chrome-devtools-mcp` plugins it drives their Chrome.

## One-time setup (the only thing the user must do)
1. Install the **Claude desktop app** and turn on **computer use** (Settings). From then on
   Claude opens programs and does tasks itself, asking permission per app.
2. Optional, for websites with their login: the **Claude in Chrome** extension from the
   Chrome Web Store (published by Anthropic). Chrome always asks the user to confirm an
   extension install — that confirmation is the user's one click; never try to skip it.

## Creating accounts for the user
1. Prefer **"Continuar com o Google"** (no new password). Otherwise ask which email to use.
2. **Passwords never go in the chat.** Generate a strong one in the browser's password
   manager (Google Password Manager or Bitwarden) during signup so it's saved there.
   If the user pastes a password anyway, tell them to change it afterwards.
3. Fill the form in the user's browser (computer use / Claude in Chrome). The user handles
   CAPTCHA, the email/SMS verification code and 2FA — those exist to prove a human is there.
4. Before accepting terms, tell the user what they agree to (paid plan, trial that
   auto-charges, data use). Never enter card details without an explicit OK for that charge.
5. Turn on 2FA for important accounts (GitHub, Vercel, Google, hosting, payments).

## No account needed at all (use these first)
- Vercel: skill `deploy-to-vercel` publishes without an account and gives a claim link.
- Neon database: Claimable Neon / `neon.new` (skill `neon`).
- GitHub: the GitHub tools in Claude Code, or `gh` CLI after one `gh auth login`.

## Opening programs (computer use)
Open via Start menu/Spotlight search, wait for the window, then act. For Obsidian prefer
the skill `obsidian-cli` (faster and more reliable than clicking). Close what you opened
when done. Never touch banking or password-manager apps unless the user explicitly asks.
