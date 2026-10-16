# Meu kit do Claude Code

Tudo o que eu uso no [Claude Code](https://claude.com/claude-code), num lugar só: **110 skills**,
**29 agentes**, **19 plugins** oficiais, os conectores MCP (sem nenhuma chave) e o meu
`CLAUDE.md` com a tabela "pedido → quem faz", que diz ao Claude qual agente ou skill usar em cada pedido.

O repositório se atualiza sozinho: quando eu adiciono ou mudo uma skill, um agente ou um plugin no meu PC,
um script copia tudo para cá, confere que não há senha nem dado pessoal e só então publica.

**Última atualização:** 16/10/2026

> Skills de terceiros estão aqui com a licença original (arquivo `LICENSE` e `FONTE.md` em cada pasta).
> As minhas skills também estão no catálogo [claude-skills-br](https://github.com/matheus-rib1108/claude-skills-br),
> com página e exemplos para cada uma.

## Instalar

### Tudo de uma vez

Windows (PowerShell):

```powershell
git clone https://github.com/matheus-rib1108/meu-kit-claude-code.git
cd meu-kit-claude-code
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

Mac / Linux:

```bash
git clone https://github.com/matheus-rib1108/meu-kit-claude-code.git
cd meu-kit-claude-code
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

## Skills (110: 109 copiadas, o resto só com link)

### Sites e design (9)

| Skill | O que faz | Fonte | Licença |
|---|---|---|---|
| [`frontend-design`](skills/sites-e-design/frontend-design) | Design visual intencional e marcante para interfaces | [anthropics/skills](https://github.com/anthropics/skills) | Apache-2.0 |
| [`hallmark`](skills/sites-e-design/hallmark) | Anti "cara de IA": direção visual, auditoria e redesign de páginas | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | MIT |
| [`site-architecture`](skills/sites-e-design/site-architecture) | Estrutura de páginas, menus e navegação do site | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT |
| [`theme-factory`](skills/sites-e-design/theme-factory) | Temas prontos (cores + fontes) para páginas e documentos | [anthropics/skills](https://github.com/anthropics/skills) | Apache-2.0 |
| [`ui-ux-pro-max`](skills/sites-e-design/ui-ux-pro-max) | Estilo, paleta, fontes e estrutura certos para cada tipo de negócio | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT |
| [`vercel-react-best-practices`](skills/sites-e-design/vercel-react-best-practices) | Boas práticas de desempenho em React e Next.js | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | MIT |
| [`web-artifacts-builder`](skills/sites-e-design/web-artifacts-builder) | Páginas HTML complexas com React, Tailwind e shadcn | [anthropics/skills](https://github.com/anthropics/skills) | Apache-2.0 |
| [`web-design-guidelines`](skills/sites-e-design/web-design-guidelines) | Regras de design de interface da equipe da Vercel | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | MIT |
| [`webapp-testing`](skills/sites-e-design/webapp-testing) | Testa o site num navegador de verdade (Playwright) | [anthropics/skills](https://github.com/anthropics/skills) | Apache-2.0 |

### Marketing, textos e vendas (15)

| Skill | O que faz | Fonte | Licença |
|---|---|---|---|
| [`abordagem-whatsapp-vendas`](skills/marketing-e-vendas/abordagem-whatsapp-vendas) | Escreve a primeira mensagem de venda, o acompanhamento e as respostas para objeções, sem cara de spam. | própria | MIT |
| [`ai-seo`](skills/marketing-e-vendas/ai-seo) | Aparecer e ser citado em buscas de IA (ChatGPT, Perplexity, AI Overviews) | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT |
| [`cardapio-digital`](skills/marketing-e-vendas/cardapio-digital) | Cria cardápio digital leve com pedido pelo WhatsApp, horário aberto/fechado e QR code de mesa, para publicar de graça. | própria | MIT |
| [`copywriting`](skills/marketing-e-vendas/copywriting) | Textos de site que vendem, sem frases genéricas | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT |
| [`cro`](skills/marketing-e-vendas/cro) | Aumenta a conversão de páginas e formulários | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT |
| [`humanizar-texto-pt`](skills/marketing-e-vendas/humanizar-texto-pt) | Tira a "cara de IA" de textos em português, mantendo o sentido e a sua voz. | própria | MIT |
| [`humanizer`](skills/marketing-e-vendas/humanizer) | Tira a "cara de IA" de textos em inglês | [blader/humanizer](https://github.com/blader/humanizer) | MIT |
| [`legenda-instagram-negocio`](skills/marketing-e-vendas/legenda-instagram-negocio) | Legendas, ideias de post, roteiro de Reels e calendário do mês para o Instagram de um negócio local, com a voz do dono. | própria | MIT |
| [`marketing-psychology`](skills/marketing-e-vendas/marketing-psychology) | Psicologia aplicada ao marketing | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT |
| [`offers`](skills/marketing-e-vendas/offers) | Monta a oferta: pacote, bônus, garantia, urgência | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT |
| [`orcamento-servicos`](skills/marketing-e-vendas/orcamento-servicos) | Calcula quanto cobrar por site, cardápio, Instagram ou vídeo e monta proposta com 3 pacotes e contrato simples. | própria | MIT |
| [`prospeccao-local-br`](skills/marketing-e-vendas/prospeccao-local-br) | Acha negócios da sua cidade que precisam do seu serviço (site, cardápio, Instagram), dá nota de oportunidade e escreve a mensagem de abordagem. | própria | MIT |
| [`schema`](skills/marketing-e-vendas/schema) | Dados estruturados (schema.org) para o Google | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT |
| [`seo-audit`](skills/marketing-e-vendas/seo-audit) | Auditoria de SEO técnico e de conteúdo | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT |
| [`social`](skills/marketing-e-vendas/social) | Conteúdo e estratégia para redes sociais | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT |

### Método de trabalho e economia de tokens (20)

| Skill | O que faz | Fonte | Licença |
|---|---|---|---|
| [`brainstorming`](skills/metodo-de-trabalho/brainstorming) | Pensa e desenha a ideia antes de construir | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`caveman`](skills/metodo-de-trabalho/caveman) | Respostas ultra-curtas (gasta bem menos tokens) | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Apache-2.0 |
| [`caveman-compress`](skills/metodo-de-trabalho/caveman-compress) | Comprime CLAUDE.md e memórias para economizar tokens | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Apache-2.0 |
| [`diagnosing-superpowers`](skills/metodo-de-trabalho/diagnosing-superpowers) | Diagnostica por que uma skill não foi usada | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`dispatching-parallel-agents`](skills/metodo-de-trabalho/dispatching-parallel-agents) | Divide tarefas independentes entre agentes em paralelo | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`executing-plans`](skills/metodo-de-trabalho/executing-plans) | Executa um plano por etapas com pontos de revisão | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`finishing-a-development-branch`](skills/metodo-de-trabalho/finishing-a-development-branch) | Fecha uma branch: merge, PR ou limpeza | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`investigate-first`](skills/metodo-de-trabalho/investigate-first) | Investiga antes de mexer | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Apache-2.0 |
| [`planning-with-files`](skills/metodo-de-trabalho/planning-with-files) | Plano em arquivos que sobrevive a conversas longas | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | MIT |
| [`receiving-code-review`](skills/metodo-de-trabalho/receiving-code-review) | Avalia e aplica revisões com rigor | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`requesting-code-review`](skills/metodo-de-trabalho/requesting-code-review) | Pede revisão de código do jeito certo | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`subagent-driven-development`](skills/metodo-de-trabalho/subagent-driven-development) | Executa um plano com um subagente por tarefa | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`surgical-patch`](skills/metodo-de-trabalho/surgical-patch) | Muda só o necessário | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Apache-2.0 |
| [`systematic-debugging`](skills/metodo-de-trabalho/systematic-debugging) | Corrige bugs pela causa raiz | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`test-driven-development`](skills/metodo-de-trabalho/test-driven-development) | Escreve o teste antes do código | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`using-git-worktrees`](skills/metodo-de-trabalho/using-git-worktrees) | Trabalho isolado com git worktrees | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`using-superpowers`](skills/metodo-de-trabalho/using-superpowers) | Ensina o Claude a achar e usar as skills | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`verification-before-completion`](skills/metodo-de-trabalho/verification-before-completion) | Confere de verdade antes de dizer "pronto" | [obra/superpowers](https://github.com/obra/superpowers) | MIT |
| [`verify-and-stop`](skills/metodo-de-trabalho/verify-and-stop) | Verifica e para, sem se estender | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Apache-2.0 |
| [`writing-plans`](skills/metodo-de-trabalho/writing-plans) | Escreve um plano de implementação detalhado | [obra/superpowers](https://github.com/obra/superpowers) | MIT |

### Criar skills e agentes (8)

| Skill | O que faz | Fonte | Licença |
|---|---|---|---|
| [`agent-builder`](skills/criar-skills/agent-builder) | Cria seus próprios agentes de IA para tarefas que se repetem, como assistente de estudos, de redes sociais ou de sites. | própria | MIT |
| [`kit-sync`](skills/criar-skills/kit-sync) | Atualiza este kit no GitHub: copia tudo, confere segredos e dados pessoais e publica | própria | MIT |
| [`mcp-builder`](skills/criar-skills/mcp-builder) | Cria servidores MCP para ligar o Claude a qualquer API | [anthropics/skills](https://github.com/anthropics/skills) | Apache-2.0 |
| [`publicar-skills-github`](skills/criar-skills/publicar-skills-github) | Monta e publica um repositório público de skills, como este: página de cada skill, downloads, instalação, notas e sugestões. | própria | MIT |
| [`skill-creator`](skills/criar-skills/skill-creator) | Cria, testa e melhora skills | [anthropics/skills](https://github.com/anthropics/skills) | Apache-2.0 |
| [`skill-hunter`](skills/criar-skills/skill-hunter) | Procura skills, agentes e servidores MCP no GitHub, verifica a segurança e instala os bons. | própria | MIT |
| [`skill-inspector`](skills/criar-skills/skill-inspector) | Checklist de segurança antes de instalar uma skill | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Apache-2.0 |
| [`writing-skills`](skills/criar-skills/writing-skills) | Como escrever e testar skills novas | [obra/superpowers](https://github.com/obra/superpowers) | MIT |

### Segurança e lei (19)

| Skill | O que faz | Fonte | Licença |
|---|---|---|---|
| [`audit-context-building`](skills/seguranca-e-lei/audit-context-building) | Entende o código a fundo antes de auditar | [trailofbits/skills](https://github.com/trailofbits/skills) | CC-BY-SA-4.0 |
| [`cybersecurity`](skills/seguranca-e-lei/cybersecurity) | Revisão com 8 especialistas: OWASP, CWE Top 25, MITRE ATT&CK | [AgriciDaniel/claude-cybersecurity](https://github.com/AgriciDaniel/claude-cybersecurity) | MIT |
| [`dast-nuclei`](skills/seguranca-e-lei/dast-nuclei) | Varredura de vulnerabilidades conhecidas com Nuclei | [AgentSecOps/SecOpsAgentKit](https://github.com/AgentSecOps/SecOpsAgentKit) | CC-BY-SA-4.0 / MPL-2.0 |
| [`dast-zap`](skills/seguranca-e-lei/dast-zap) | Ataques reais contra a versão de teste do seu site (OWASP ZAP) | [AgentSecOps/SecOpsAgentKit](https://github.com/AgentSecOps/SecOpsAgentKit) | CC-BY-SA-4.0 / MPL-2.0 |
| [`differential-review`](skills/seguranca-e-lei/differential-review) | Revisa mudanças recentes procurando falhas | [trailofbits/skills](https://github.com/trailofbits/skills) | CC-BY-SA-4.0 |
| [`fp-check`](skills/seguranca-e-lei/fp-check) | Confirma se um alerta é real ou falso positivo | [trailofbits/skills](https://github.com/trailofbits/skills) | CC-BY-SA-4.0 |
| [`ghost-repo-context`](skills/seguranca-e-lei/ghost-repo-context) | Mapeia o repositório antes da varredura | [ghostsecurity/skills](https://github.com/ghostsecurity/skills) | Apache-2.0 |
| [`ghost-report`](skills/seguranca-e-lei/ghost-report) | Gera o relatório de segurança | [ghostsecurity/skills](https://github.com/ghostsecurity/skills) | Apache-2.0 |
| [`ghost-scan-code`](skills/seguranca-e-lei/ghost-scan-code) | Scanner de vulnerabilidades no código | [ghostsecurity/skills](https://github.com/ghostsecurity/skills) | Apache-2.0 |
| [`ghost-validate`](skills/seguranca-e-lei/ghost-validate) | Valida cada achado do scanner | [ghostsecurity/skills](https://github.com/ghostsecurity/skills) | Apache-2.0 |
| [`legal-compliance`](skills/seguranca-e-lei/legal-compliance) | Deixa o site pronto para publicar no Brasil: política de privacidade, termos de uso, banner de cookies com consentimento real e exclusão de dados (LGPD). | própria | MIT |
| [`owasp-security`](skills/seguranca-e-lei/owasp-security) | Regras OWASP Top 10 e ASVS ao escrever e revisar código | [agamm/claude-code-owasp](https://github.com/agamm/claude-code-owasp) | MIT |
| [`sca-trivy`](skills/seguranca-e-lei/sca-trivy) | Acha bibliotecas com falha conhecida (Trivy) | [AgentSecOps/SecOpsAgentKit](https://github.com/AgentSecOps/SecOpsAgentKit) | CC-BY-SA-4.0 / MPL-2.0 |
| [`secrets-gitleaks`](skills/seguranca-e-lei/secrets-gitleaks) | Acha senhas e chaves vazadas no código (Gitleaks) | [AgentSecOps/SecOpsAgentKit](https://github.com/AgentSecOps/SecOpsAgentKit) | CC-BY-SA-4.0 / MPL-2.0 |
| [`semgrep`](skills/seguranca-e-lei/semgrep) | Roda o Semgrep (scanner de vulnerabilidades) | [trailofbits/skills](https://github.com/trailofbits/skills) | CC-BY-SA-4.0 |
| [`sharp-edges`](skills/seguranca-e-lei/sharp-edges) | Acha funções e configurações perigosas | [trailofbits/skills](https://github.com/trailofbits/skills) | CC-BY-SA-4.0 |
| [`site-fortress`](skills/seguranca-e-lei/site-fortress) | Auditoria de segurança completa do seu próprio site em 12 fases: segredos, dependências, login, pagamentos, cabeçalhos, LGPD. Corrige e prova cada correção. | própria | MIT |
| [`supply-chain-risk-auditor`](skills/seguranca-e-lei/supply-chain-risk-auditor) | Verifica se as bibliotecas instaladas são confiáveis | [trailofbits/skills](https://github.com/trailofbits/skills) | CC-BY-SA-4.0 |
| [`variant-analysis`](skills/seguranca-e-lei/variant-analysis) | Achou um bug? Procura todos os parecidos | [trailofbits/skills](https://github.com/trailofbits/skills) | CC-BY-SA-4.0 |

### Publicar, GitHub e banco de dados (9)

| Skill | O que faz | Fonte | Licença |
|---|---|---|---|
| [`cost-estimator`](skills/publicar-e-banco/cost-estimator) | Pesquisa o preço de hoje para colocar um site ou app no ar (hospedagem, banco, domínio, taxas de Pix e cartão) e recomenda o melhor custo-benefício. | própria | MIT |
| [`deploy-to-vercel`](skills/publicar-e-banco/deploy-to-vercel) | Publica na Vercel | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | MIT |
| [`github-helper`](skills/publicar-e-banco/github-helper) | Faz tudo de Git e GitHub: cria repositório, primeiro commit, branches, PRs, releases, GitHub Pages e segurança grátis. | própria | MIT |
| [`golive`](skills/publicar-e-banco/golive) | Coloca o site no ar nas suas contas: hospedagem, banco, domínio, pagamentos | [mikehasa/golive-skill](https://github.com/mikehasa/golive-skill) | MIT |
| [`neon`](skills/publicar-e-banco/neon) | Visão geral do Neon (Postgres na nuvem com plano grátis) | [neondatabase/agent-skills](https://github.com/neondatabase/agent-skills) | Apache-2.0 |
| [`neon-auth`](skills/publicar-e-banco/neon-auth) | Login de usuários com Neon Auth | [neondatabase/agent-skills](https://github.com/neondatabase/agent-skills) | Apache-2.0 |
| [`neon-postgres`](skills/publicar-e-banco/neon-postgres) | Banco Postgres no Neon: SQL, schema, conexão | [neondatabase/agent-skills](https://github.com/neondatabase/agent-skills) | Apache-2.0 |
| [`vercel-cli-with-tokens`](skills/publicar-e-banco/vercel-cli-with-tokens) | Usa a Vercel pelo terminal com token | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | MIT |
| [`vercel-optimize`](skills/publicar-e-banco/vercel-optimize) | Deixa o site na Vercel mais rápido e barato | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | MIT |

### Produtividade, PC e Obsidian (12)

| Skill | O que faz | Fonte | Licença |
|---|---|---|---|
| [`assistente-voz-jarvis`](skills/produtividade-e-pc/assistente-voz-jarvis) | Guia para construir seu assistente pessoal de voz em Python: palavra de ativação, transcrição, resposta da IA, voz e comandos no PC. | própria | MIT |
| [`claude-chats`](skills/produtividade-e-pc/claude-chats) | Lê suas conversas do claude.ai pela exportação oficial, acha a que você quer e faz no Claude Code o que foi pedido lá. | própria | MIT |
| [`comparador-produtos-br`](skills/produtividade-e-pc/comparador-produtos-br) | Compara produtos de lojas brasileiras (Pichau, Kabum, Terabyte, Amazon, Mercado Livre) com tabela, ranking e link certo. | própria | MIT |
| [`defuddle`](skills/produtividade-e-pc/defuddle) | Extrai só o texto útil de uma página da web | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | MIT |
| `doc-coauthoring` (só link) | Escreve documentos junto com você, por etapas | [anthropics/skills](https://github.com/anthropics/skills) | sem licença no original |
| [`financas-pessoais`](skills/produtividade-e-pc/financas-pessoais) | Controle de gastos, metas, cartão/Pix sem juros, básico de MEI | própria | MIT |
| [`json-canvas`](skills/produtividade-e-pc/json-canvas) | Mapas mentais (Canvas) do Obsidian | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | MIT |
| [`obsidian-bases`](skills/produtividade-e-pc/obsidian-bases) | Tabelas (Bases) do Obsidian | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | MIT |
| [`obsidian-cli`](skills/produtividade-e-pc/obsidian-cli) | Abre, pesquisa e cria notas no Obsidian pelo terminal | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | MIT |
| [`obsidian-markdown`](skills/produtividade-e-pc/obsidian-markdown) | Notas no formato certo do Obsidian | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | MIT |
| [`pc-control`](skills/produtividade-e-pc/pc-control) | Faz o Claude mexer no seu computador e no Chrome logado: abrir programas, usar sites, criar contas com o mínimo de esforço seu. | própria | MIT |
| [`session-radar`](skills/produtividade-e-pc/session-radar) | Mostra o que está acontecendo nas suas outras conversas do Claude Code (nuvem ou computador), resume e diz o que falta. | própria | MIT |

### Vídeo, foto, redes e música (6)

| Skill | O que faz | Fonte | Licença |
|---|---|---|---|
| [`ffmpeg-skill`](skills/video-foto-e-musica/ffmpeg-skill) | Edita vídeo e áudio no PC: corta, legenda, 9:16, exporta | [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | MIT |
| [`musica-ia`](skills/video-foto-e-musica/musica-ia) | Letra e prompt de estilo para Suno/Udio | própria | MIT |
| [`photo-editor`](skills/video-foto-e-musica/photo-editor) | Melhora fotos no seu computador: luz, cor, nitidez, ampliação com IA, remoção de fundo e recorte para Instagram ou site. | própria | MIT |
| [`roteiro-reels-br`](skills/video-foto-e-musica/roteiro-reels-br) | Roteiro de Reels/TikTok/Shorts para negócio local | própria | MIT |
| [`video-link`](skills/video-foto-e-musica/video-link) | Você manda o link (Instagram, TikTok, YouTube) e o Claude "assiste": baixa, transcreve a fala e tira quadros da imagem. | própria | MIT |
| [`video-maker`](skills/video-foto-e-musica/video-maker) | Faz vídeos .mp4 de verdade: Reels, TikTok, propaganda, explicativo com narração e legenda, slideshow de fotos. | própria | MIT |

### Estudos (11)

| Skill | O que faz | Fonte | Licença |
|---|---|---|---|
| [`curriculo-jovem-aprendiz`](skills/estudos/curriculo-jovem-aprendiz) | Currículo de uma página para primeiro emprego, Jovem Aprendiz ou estágio, usando cursos e projetos como experiência, mais carta e treino de entrevista. | própria | MIT |
| [`formatador-abnt`](skills/estudos/formatador-abnt) | Formata trabalho na ABNT e gera o Word | própria | MIT |
| [`matematica-passo-a-passo`](skills/estudos/matematica-passo-a-passo) | Resolve exercícios de matemática do ensino médio e técnico explicando cada passo, com desenho da figura e conferência da conta. | própria | MIT |
| [`organizador-de-estudos`](skills/estudos/organizador-de-estudos) | Monta um cronograma de estudos que cabe na sua semana real, com provas, Pomodoro, revisão espaçada e checagem semanal. | própria | MIT |
| [`projeto-senai-desafio`](skills/estudos/projeto-senai-desafio) | Estrutura projetos de desafio técnico (Grand Prix SENAI, desafios de empresa): problema, causa raiz, solução, Canvas, custos, KPIs e pitch. | própria | MIT |
| [`redacao-enem`](skills/estudos/redacao-enem) | Corrige redação nas 5 competências do ENEM com nota estimada | própria | MIT |
| [`revisao-flashcards`](skills/estudos/revisao-flashcards) | Transforma a matéria em resumo de uma página, flashcards, quiz com gabarito comentado e plano de revisão até a prova. | própria | MIT |
| [`sympy`](skills/estudos/sympy) | Matemática exata por código para conferir contas | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | MIT |
| [`trabalho-escolar`](skills/estudos/trabalho-escolar) | Ajuda em trabalhos de escola, SESI e SENAI: pesquisa, resumo, cartaz, slides, roteiro de fala cronometrado e perguntas do professor. | própria | MIT |
| [`tutor-ingles`](skills/estudos/tutor-ingles) | Professor de inglês para brasileiros, do A1 ao C1 | própria | MIT |
| [`tutor-sql`](skills/estudos/tutor-sql) | Professor de SQL/MySQL em português: corrige scripts, explica comandos e cria missões no seu próprio banco de exemplo. | própria | MIT |

### Jogos (1)

| Skill | O que faz | Fonte | Licença |
|---|---|---|---|
| [`minecraft-construcoes`](skills/jogos/minecraft-construcoes) | Ajuda com Minecraft Java modado: Litematica, schematics, conversão de Bedrock para Java, comandos seguros e conflitos entre mods. | própria | MIT |

### Só o link (sem licença que permita copiar)

- `doc-coauthoring` — Escreve documentos junto com você, por etapas: <https://github.com/anthropics/skills> (sem licença no original)

## Agentes (29)

Ficam em [`agents/`](agents) e vão para `~/.claude/agents`. Fonte: [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) · MIT.

| Agente | O que faz | Grupo |
|---|---|---|
| [`agent-organizer`](agents/agent-organizer.md) | Divide a tarefa e escolhe os agentes | coordenacao |
| [`multi-agent-coordinator`](agents/multi-agent-coordinator.md) | Coordena vários agentes ao mesmo tempo | coordenacao |
| [`workflow-orchestrator`](agents/workflow-orchestrator.md) | Desenha fluxos e máquinas de estado | coordenacao |
| [`api-designer`](agents/api-designer.md) | Desenho de APIs REST/GraphQL | desenvolvimento |
| [`backend-developer`](agents/backend-developer.md) | APIs e servidores | desenvolvimento |
| [`frontend-developer`](agents/frontend-developer.md) | Front-end React/Vue/Angular | desenvolvimento |
| [`fullstack-developer`](agents/fullstack-developer.md) | Banco, API e tela juntos | desenvolvimento |
| [`nextjs-developer`](agents/nextjs-developer.md) | Apps Next.js completos | desenvolvimento |
| [`python-pro`](agents/python-pro.md) | Python tipado e moderno | desenvolvimento |
| [`react-specialist`](agents/react-specialist.md) | React avançado e desempenho | desenvolvimento |
| [`typescript-pro`](agents/typescript-pro.md) | TypeScript com tipos avançados | desenvolvimento |
| [`webhook-engineer`](agents/webhook-engineer.md) | Webhooks seguros: assinatura, retry, idempotência | desenvolvimento |
| [`competitive-analyst`](agents/competitive-analyst.md) | Análise de concorrentes | pesquisa |
| [`market-researcher`](agents/market-researcher.md) | Pesquisa de mercado e público | pesquisa |
| [`research-analyst`](agents/research-analyst.md) | Junta as fontes e resume em conclusões | pesquisa |
| [`search-specialist`](agents/search-specialist.md) | Acha fontes e informações precisas | pesquisa |
| [`content-marketer`](agents/content-marketer.md) | Estratégia e criação de conteúdo | produto-e-design |
| [`landing-page-copywriter`](agents/landing-page-copywriter.md) | Textos de landing page que convertem | produto-e-design |
| [`product-manager`](agents/product-manager.md) | Define objetivo, páginas e prioridades | produto-e-design |
| [`seo-specialist`](agents/seo-specialist.md) | SEO técnico e de conteúdo | produto-e-design |
| [`ui-designer`](agents/ui-designer.md) | Design visual e sistema de design | produto-e-design |
| [`ux-researcher`](agents/ux-researcher.md) | Pesquisa com usuário e usabilidade | produto-e-design |
| [`accessibility-tester`](agents/accessibility-tester.md) | Acessibilidade (WCAG) | qualidade-e-seguranca |
| [`ai-writing-auditor`](agents/ai-writing-auditor.md) | Acha e reescreve textos com cara de IA | qualidade-e-seguranca |
| [`code-reviewer`](agents/code-reviewer.md) | Revisão de código | qualidade-e-seguranca |
| [`debugger`](agents/debugger.md) | Acha a causa de bugs | qualidade-e-seguranca |
| [`performance-engineer`](agents/performance-engineer.md) | Desempenho e gargalos | qualidade-e-seguranca |
| [`qa-expert`](agents/qa-expert.md) | Estratégia e plano de testes | qualidade-e-seguranca |
| [`security-auditor`](agents/security-auditor.md) | Auditoria de segurança | qualidade-e-seguranca |

## Plugins (19, do marketplace oficial `anthropics/claude-plugins-official`)

| Plugin | O que faz | Instalar |
|---|---|---|
| `browser-use` | Usa o seu Chrome logado para tarefas em sites | `/plugin install browser-use@claude-plugins-official` |
| `canva` | Cria e edita designs no Canva | `/plugin install canva@claude-plugins-official` |
| `cc-safety-net` |  | `/plugin install cc-safety-net@cc-marketplace` |
| `chrome-devtools-mcp` | Controla e inspeciona o Chrome (Google) | `/plugin install chrome-devtools-mcp@claude-plugins-official` |
| `claude-md-management` | Mantém o CLAUDE.md atualizado | `/plugin install claude-md-management@claude-plugins-official` |
| `claude-security` | Varredura profunda de vulnerabilidades | `/plugin install claude-security@claude-plugins-official` |
| `code-simplifier` | Deixa o código mais limpo | `/plugin install code-simplifier@claude-plugins-official` |
| `context7` | Documentação atualizada das bibliotecas | `/plugin install context7@claude-plugins-official` |
| `expo` | Apps de celular com Expo/React Native (instalado desligado) (desligado por padrão) | `/plugin install expo@claude-plugins-official` |
| `hyperframes` | Vídeos em HTML renderizados em MP4 (HeyGen) | `/plugin install hyperframes@claude-plugins-official` |
| `mercadopago` | Integração oficial do Mercado Pago (Pix, cartão) | `/plugin install mercadopago@claude-plugins-official` |
| `modern-web-guidance` | Boas práticas web atuais (Chrome) | `/plugin install modern-web-guidance@claude-plugins-official` |
| `pyright-lsp` | Entende Python de verdade (tipos) | `/plugin install pyright-lsp@claude-plugins-official` |
| `remember` | Memória contínua entre conversas | `/plugin install remember@claude-plugins-official` |
| `security-guidance` | Avisa na hora quando um código inseguro é escrito | `/plugin install security-guidance@claude-plugins-official` |
| `session-report` | Relatório de onde os tokens foram gastos | `/plugin install session-report@claude-plugins-official` |
| `stripe` | Integração oficial do Stripe | `/plugin install stripe@claude-plugins-official` |
| `telegram` | Conversa com o Claude Code pelo Telegram | `/plugin install telegram@claude-plugins-official` |
| `typescript-lsp` | Entende TypeScript de verdade | `/plugin install typescript-lsp@claude-plugins-official` |

## Conectores MCP ([`mcp/.mcp.json`](mcp/.mcp.json))

Sem nenhuma chave: cada um pede login na primeira vez (`/mcp` no Claude Code).

| Conector | Tipo |
|---|---|
| `playwright` | local (sh) |
| `vercel` | https://mcp.vercel.com |
| `notion` | https://mcp.notion.com/mcp |
| `neon` | https://mcp.neon.tech/mcp |

## Como o kit se atualiza sozinho

1. `sync-kit.ps1` copia skills, agentes, plugins, `.mcp.json` e `CLAUDE.md` do meu PC para cá e refaz este README.
2. Roda o [Gitleaks](https://github.com/gitleaks/gitleaks) e uma busca por e-mail, telefone, CPF e nomes que não podem sair.
3. Só se estiver tudo limpo e algo tiver mudado, faz o commit `Atualiza kit: <o que mudou>` e o push.
   Se achar algo suspeito, não publica e grava o aviso em `sync-kit.log` (que fica só no meu PC).

Roda ao fechar cada conversa do Claude Code (hook `SessionEnd`), uma vez por dia pelo Agendador de Tarefas do
Windows e quando eu peço "atualiza meu kit no GitHub".

## Créditos

Obrigado a quem escreveu e liberou essas skills e agentes:

- [AgentSecOps/SecOpsAgentKit](https://github.com/AgentSecOps/SecOpsAgentKit) · CC-BY-SA-4.0 / MPL-2.0 — dast-nuclei, dast-zap, sca-trivy, secrets-gitleaks
- [AgriciDaniel/claude-cybersecurity](https://github.com/AgriciDaniel/claude-cybersecurity) · MIT — cybersecurity
- [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) · Apache-2.0 — caveman, caveman-compress, investigate-first, surgical-patch, verify-and-stop
- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · MIT — sympy
- [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) · Apache-2.0 — skill-inspector
- [Nutlope/hallmark](https://github.com/Nutlope/hallmark) · MIT — hallmark
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) · MIT — planning-with-files
- [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) · MIT — 29 agentes
- [agamm/claude-code-owasp](https://github.com/agamm/claude-code-owasp) · MIT — owasp-security
- [anthropics/skills](https://github.com/anthropics/skills) · Apache-2.0 — frontend-design, mcp-builder, skill-creator, theme-factory, web-artifacts-builder, webapp-testing
- [anthropics/skills](https://github.com/anthropics/skills) · sem licença no original — doc-coauthoring
- [blader/humanizer](https://github.com/blader/humanizer) · MIT — humanizer
- [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · MIT — ai-seo, copywriting, cro, marketing-psychology, offers, schema, seo-audit, site-architecture, social
- [ghostsecurity/skills](https://github.com/ghostsecurity/skills) · Apache-2.0 — ghost-repo-context, ghost-report, ghost-scan-code, ghost-validate
- [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) · MIT — ffmpeg-skill
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) · MIT — defuddle, json-canvas, obsidian-bases, obsidian-cli, obsidian-markdown
- [mikehasa/golive-skill](https://github.com/mikehasa/golive-skill) · MIT — golive
- [neondatabase/agent-skills](https://github.com/neondatabase/agent-skills) · Apache-2.0 — neon, neon-auth, neon-postgres
- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · MIT — ui-ux-pro-max
- [obra/superpowers](https://github.com/obra/superpowers) · MIT — brainstorming, diagnosing-superpowers, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills
- [trailofbits/skills](https://github.com/trailofbits/skills) · CC-BY-SA-4.0 — audit-context-building, differential-review, fp-check, semgrep, sharp-edges, supply-chain-risk-auditor, variant-analysis
- [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) · MIT — deploy-to-vercel, vercel-cli-with-tokens, vercel-optimize, vercel-react-best-practices, web-design-guidelines

## Licença

O que é meu (skills marcadas como "própria", scripts e textos) está sob a licença MIT ([`LICENSE`](LICENSE)).
O que é de terceiros continua sob a licença original, indicada na tabela e no `LICENSE` de cada pasta.
