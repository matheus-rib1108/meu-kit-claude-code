---
name: publicar-skills-github
description: Monta e publica no GitHub do usuário um repositório público de skills para Claude em português — página explicando cada skill, imagens e vídeo, download de todas ou de uma, instruções de instalação (claude.ai, app, Claude Code), avaliação com estrelas e sugestão de skills novas. Use quando o usuário pedir para colocar skills no GitHub, compartilhar skills, criar repositório/biblioteca/catálogo de skills ou atualizar esse repositório.
---

# Publicar biblioteca de skills no GitHub

## 0. Antes de começar
- Descubra a conta: `gh auth status`. Se não estiver logado, peça para o usuário rodar `gh auth login` (ou criar o repositório vazio pelo navegador).
- **Confirme com o usuário** o nome do repositório (sugestão `claude-skills-br`) e que ele será **público**. Não publique sem esse "sim".
- Junte as skills: as criadas pelo usuário (pastas com `SKILL.md`) e a lista das que ele usa de terceiros (só link, nunca copiar).

## 1. Estrutura do repositório
```
README.md                 # página principal
CATALOGO.md               # skills de terceiros: Skill | Repo (link) | O que faz | Instalar
COMO-INSTALAR.md          # passo a passo com imagens
DICAS.md                  # dicas de uso e como criar a própria skill
skills/<nome>/SKILL.md
skills/<nome>/README.md   # o que faz · o que muda no Claude · exemplos de pedido · antes/depois · dicas
dist/todas-as-skills.zip
dist/<nome>.zip           # pasta da skill na raiz do zip (formato do upload no claude.ai)
docs/images/              # diagramas (como skill funciona, instalação, mapa das skills)
docs/videos/              # demo .mp4 + .gif (gerar com Python/PIL + ffmpeg)
.claude-plugin/marketplace.json
.github/ISSUE_TEMPLATE/avaliar-skill.yml  # dropdown 1–5 estrelas + comentário
.github/ISSUE_TEMPLATE/sugerir-skill.yml
.github/ISSUE_TEMPLATE/problema.yml
.github/workflows/build-zips.yml          # regenera dist/ a cada push
CONTRIBUTING.md
LICENSE                                   # MIT
```

## 2. README principal (em pt-BR, bem explicado)
1. O que são skills (diagrama: descrição curta sempre carregada → instruções completas só quando o assunto aparece).
2. Tabela de todas as skills: nome com link para o README dela, para que serve, link de download individual.
3. Botão "⬇ Baixar todas" → `dist/todas-as-skills.zip` (e Release).
4. Como instalar:
   - **claude.ai / app**: Configurações → Capacidades → Skills → enviar o .zip.
   - **Claude Code**: copiar a pasta para `~/.claude/skills/`; ou `npx skills add <usuario>/<repo>`; ou `/plugin marketplace add <usuario>/<repo>`.
5. "Avalie e sugira": links diretos para os templates de issue e para as Discussions.
6. GIF de demonstração e links para CATALOGO e DICAS.

## 3. Publicação
1. `gh repo create <usuario>/<repo> --public --source . --push`
2. `gh repo edit --enable-discussions --add-topic claude,claude-skills,agent-skills,portugues,brasil`
3. Discussions fixadas: "Avalie as skills" (enquete) e "Ideias de skills".
4. Release `v1.0` com todos os zips anexados — **pergunte antes de publicar**.

## 4. Verificação
- Cada zip abre com uma pasta contendo `SKILL.md` com `name` (minúsculas e hífens) e `description`.
- README renderizado: todas as imagens aparecem e todos os links funcionam.
- Nada de e-mail, telefone ou dado pessoal do usuário no repo.

## Saída para o usuário
Link do repositório + 3 linhas do que foi feito + como ele pode divulgar.
