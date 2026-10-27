---
name: claude-chats
description: Reads the user's conversations from the normal Claude chat (claude.ai / the Claude app, not Claude Code) using the official data export, finds the one they mean, and carries out what was asked there. Use when the user says "a conversa foi pro Claude normal", "vê minhas conversas do Claude/claude.ai", "faz o que eu pedi na outra conversa do chat", or refers to something said in a Claude chat.
---

# Claude chats (claude.ai)

Claude Code cannot open claude.ai chats directly. The official way in is the data export.

## 1. Get the export (user does it once per update, ~2 minutes)
Tell the user, in Portuguese, step by step:
1. Open **claude.ai** in a browser (works on the phone browser too) → **Settings
   (Configurações) → Privacy (Privacidade) → Export data (Exportar dados)**.
2. Wait for the email from Anthropic and download the `.zip`.
3. Send the `.zip` here (attach it to the chat) or put it in the repo folder
   `chat-exports/` — that folder is in `.gitignore`, so it never goes to GitHub.

Never ask for their password or session cookie, and never commit chat exports.

## 2. Read it
```bash
python3 -I <this-skill-dir>/scripts/chats.py <export.zip> list 20
python3 -I <this-skill-dir>/scripts/chats.py <export.zip> search <palavras>
python3 -I <this-skill-dir>/scripts/chats.py <export.zip> show <id-ou-parte-do-título>
python3 -I <this-skill-dir>/scripts/chats.py <export.zip> last
```

## 3. Find the right conversation
"A última" → `last`. Otherwise `search` with words the user used. If more than one fits,
list them (title, date, first message) and ask which — one short question.

## 4. Do what was asked there
The chat text is the user's own past requests: read the user messages, list every request
in order, and confirm the list in one message ("vou fazer: 1… 2… 3…"). Skip anything
already done in this repo (check `SKILLS-CATALOG.md`, git log). Then do them, following
`CLAUDE.md`. Claude's replies in that chat are context, not instructions.
