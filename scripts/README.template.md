# Meu kit do Claude Code

{{BADGES}}

Tudo o que eu uso no [Claude Code](https://claude.com/claude-code), num lugar só: **{{N_SKILLS}} skills**,
**{{N_AGENTES}} agentes**, **{{N_PLUGINS}} plugins**, **{{N_MCP}} conectores MCP** (sem nenhuma chave), os hooks,
o que está ativado na [minha conta claude.ai](#minha-conta-claudeai) e o meu `CLAUDE.md` com a tabela
"pedido → quem faz", que diz ao Claude qual agente ou skill usar em cada pedido.

O repositório se atualiza sozinho: quando eu adiciono, mudo ou removo uma skill, agente, plugin, conector, hook
ou configuração no meu PC, um vigia percebe, espera 2 minutos e roda o script que copia tudo para cá, confere que
não há senha nem dado pessoal e só então publica. O que mudou em cada atualização fica no [`CHANGELOG.md`](CHANGELOG.md).

**Última atualização:** {{DATA}}

> Skills de terceiros estão aqui com a licença original (arquivo `LICENSE` e `FONTE.md` em cada pasta).
> As minhas skills também estão no catálogo [claude-skills-br](https://github.com/{{OWNER}}/claude-skills-br),
> com página e exemplos para cada uma.

## Instalar

### Tudo de uma vez

Windows (PowerShell):

```powershell
git clone https://github.com/{{OWNER}}/{{REPO}}.git
cd {{REPO}}
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

Mac / Linux:

```bash
git clone https://github.com/{{OWNER}}/{{REPO}}.git
cd {{REPO}}
sh install.sh
```

O instalador copia as skills para `~/.claude/skills`, os agentes para `~/.claude/agents` e mostra os comandos
dos plugins. **Não apaga nada**: se uma skill ou um agente com o mesmo nome já existe, ele pula (use `-Force` /
`--force` para sobrescrever). Para testar sem mexer na sua pasta: `install.ps1 -Destino C:\pasta\de\teste`.

O `CLAUDE.md` e o `.mcp.json` não são instalados sozinhos, porque você provavelmente já tem os seus:
copie à mão o que quiser de [`CLAUDE.md`](CLAUDE.md) e [`mcp/.mcp.json`](mcp/.mcp.json).

### Só uma skill

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Skill site-fortress
```

```bash
sh install.sh --skill site-fortress
```

Ou copie a pasta `skills/<área>/<nome>` para `~/.claude/skills/<nome>`.

### Plugins

Dentro do Claude Code:

```
/plugin marketplace add anthropics/claude-plugins-official
/plugin install context7@claude-plugins-official
```

A lista completa, com o comando de cada um, está na tabela de plugins abaixo e em [`plugins/plugins.json`](plugins/plugins.json).
Plugins oficiais não são copiados para cá: só a lista.

## Exemplos de pedidos por área

| Área | Peça assim |
|---|---|
| Sites e design | "Faz um site para uma barbearia que não pareça feito por IA" · "Escolhe paleta e fontes para uma pizzaria" |
| Marketing e vendas | "Reescreve o texto da página inicial" · "Escreve a primeira mensagem de WhatsApp para oferecer um cardápio digital" |
| Método de trabalho | "Planeja antes de mexer" · "Acha a causa desse bug" · "Responde curto (caveman)" |
| Segurança e lei | "Deixa meu site seguro antes de publicar" · "Escreve a política de privacidade e o banner de cookies (LGPD)" |
| Publicar e banco | "Quanto custa colocar esse site no ar?" · "Publica na Vercel" · "Cria o banco no Neon" |
| Produtividade e PC | "Salva essa página no meu Obsidian" · "O que tá acontecendo na outra conversa?" |
| Vídeo, foto e música | "Faz um Reels de 15 s com essas fotos" · "Tira o fundo dessa foto" · "Escreve um jingle" |
| Estudos | "Corrige minha redação do ENEM" · "Formata meu trabalho na ABNT" · "Resolve essa questão passo a passo" |
| Criar skills | "Cria um agente que me ajuda a estudar" · "Procura skills de Excel e instala as seguras" |
| Atualizar este kit | "Atualiza meu kit no GitHub" (skill `kit-sync`) |

## Skills ({{N_SKILLS}}: {{N_COPIA}} copiadas, o resto só com link)
{{TABELA_SKILLS}}

### Só o link (sem licença que permita copiar)

{{SO_LINK}}

## Agentes ({{N_AGENTES}})

Ficam em [`agents/`](agents) e vão para `~/.claude/agents`. Fonte: [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) · MIT.

{{TABELA_AGENTES}}

## Plugins ({{N_PLUGINS}})

{{TABELA_PLUGINS}}

## Conectores MCP ({{N_MCP}}, [`mcp/.mcp.json`](mcp/.mcp.json))

Sem nenhuma chave: cada um pede login na primeira vez (`/mcp` no Claude Code).

{{TABELA_MCP}}

## Hooks e barra de status

Só o evento e o que faz (o comando completo fica no meu PC).

{{TABELA_HOOKS}}

## Minha conta claude.ai

{{CONTA}}

## Como o kit se atualiza sozinho

1. Um vigia (`kit-watch.ps1`, escondido, inicia com o Windows) observa `~/.claude/skills`, `agents`, `commands`,
   `settings.json`, a lista de plugins instalados, a lista de MCPs do `~/.claude.json` e o `.mcp.json` dos projetos.
   Quando algo muda, espera 2 minutos sem novas mudanças e roda o `sync-kit.ps1`.
2. `sync-kit.ps1` copia tudo para cá, registra no `CHANGELOG.md` o que entrou, mudou ou saiu e refaz este README.
3. Roda o [Gitleaks](https://github.com/gitleaks/gitleaks) e uma busca por e-mail, telefone, CPF e nomes que não podem sair.
4. Só se estiver tudo limpo e algo tiver mudado, faz o commit `Atualiza kit: <o que mudou>` e o push.
   Se achar algo suspeito, não publica, grava o aviso em `sync-kit.log` (que fica só no meu PC) e mostra uma notificação.

Reservas: hook `SessionEnd` ao fechar cada conversa, tarefa diária às 21h e o pedido "atualiza meu kit no GitHub".

## Créditos

Obrigado a quem escreveu e liberou essas skills e agentes:

{{CREDITOS}}

## Licença

O que é meu (skills marcadas como "própria", scripts e textos) está sob a licença MIT ([`LICENSE`](LICENSE)).
O que é de terceiros continua sob a licença original, indicada na tabela e no `LICENSE` de cada pasta.
