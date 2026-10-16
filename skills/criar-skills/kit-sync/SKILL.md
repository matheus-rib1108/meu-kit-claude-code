---
name: kit-sync
description: Atualiza o repositório público "meu-kit-claude-code" no GitHub com as skills, agentes, plugins, conectores MCP e CLAUDE.md atuais deste PC — copia tudo, refaz o README, roda o Gitleaks e a busca de dados pessoais, e só publica se estiver limpo. Use quando o usuário pedir "atualiza meu kit no GitHub", "sincroniza o kit", "publica minhas skills novas", ou perguntar se o kit está atualizado ou por que não publicou.
---

# kit-sync

O kit fica em `~/repos/meu-kit-claude-code` e é publicado em
https://github.com/matheus-rib1108/meu-kit-claude-code.

## Atualizar agora

1. Primeiro rode a skill `kit-sync-conta` (lista da conta claude.ai pelo Chrome, só leitura).
   Se o Chrome estiver fechado, siga sem ela e avise.
2. Depois:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "$HOME\repos\meu-kit-claude-code\sync-kit.ps1"
```

Depois leia as últimas linhas de `~/repos/meu-kit-claude-code/sync-kit.log` e diga ao usuário, em português:
- **Publicado:** o que mudou (a mensagem do commit) e o link do repositório.
- **Nada mudou:** só isso.
- **NÃO PUBLICADO:** o motivo e os arquivos citados. Nunca force a publicação.
  Se for falso positivo, mostre o trecho ao usuário e só com o "ok" dele:
  e-mail público de skill de terceiros → `scripts/personal-allowlist.txt`;
  segredo de exemplo → impressão digital no `.gitleaksignore`. Depois rode de novo.

## Como funciona

- `scripts/build_kit.py` copia `~/.claude/skills` (+ skills extras do dev-journey), `~/.claude/agents`,
  a lista `enabledPlugins` do `~/.claude/settings.json`, o `.mcp.json` sem `env`/`headers` e o `~/.claude/CLAUDE.md`.
- `kit-meta.json` guarda área, fonte, licença e descrição de cada skill. Skill nova entra na área `outras`
  com classificação automática: com fonte de terceiro e sem licença permissiva → só link; sem fonte → "própria".
  Para mudar a área ou a descrição, edite o `kit-meta.json` e rode o sync.
- Termos privados que nunca podem sair (nomes de clientes, e-mail, telefone) ficam em
  `~/.claude/kit-sync/private-terms.txt`, fora do repositório. Para bloquear um nome novo, acrescente uma linha lá.
- Também publica: comandos (`~/.claude/commands`), MCPs do `~/.claude.json` (só nome/tipo/url sem query),
  hooks (só o evento), a lista da conta claude.ai (`~/.claude/kit-sync/conta-claude-ai.json`), datas de entrada
  de cada item, badges e o `CHANGELOG.md` (+ entrou, ~ mudou, − saiu). O inventário anterior fica em `kit-meta.json` → `inventario`.
- **Vigia (na hora):** `kit-watch.ps1`, tarefa "MeuKitClaudeCode-Vigia" (inicia no logon, escondida). Quando algo
  muda em skills, agents, commands, settings.json, CLAUDE.md, installed_plugins.json, MCPs do ~/.claude.json,
  conta-claude-ai.json ou .mcp.json dos projetos, espera 2 min sem mudanças e roda o sync.
  - Pausar: criar `~/.claude/kit-sync/PAUSADO` (apagar para voltar), ou `Stop-ScheduledTask MeuKitClaudeCode-Vigia`
    + `Disable-ScheduledTask MeuKitClaudeCode-Vigia`.
- Reservas: hook `SessionEnd`, tarefa diária "MeuKitClaudeCode-Sync" (21h) e tarefa agendada do app
  "21h: conta claude.ai no kit". Só faz commit quando algo além do README mudou.
- Se não publicar, grava o motivo em `sync-kit.log` e mostra notificação do Windows.
