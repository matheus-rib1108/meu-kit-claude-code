# Como trabalhar neste repositório

O usuário fala português. Responda em português, direto e curto.

## Equipe de agentes (use como uma empresa)

Os agentes ficam em `.claude/agents/`, as skills em `.claude/skills/`.
Escolha pela tarefa e rode agentes independentes em paralelo.

| Pedido do usuário | Quem faz |
|---|---|
| Pesquisa / "pesquisa pra mim" | `search-specialist` coleta fontes → `research-analyst` resume. Mercado/concorrência: `market-researcher`, `competitive-analyst` |
| Site ou app novo | 1. `product-manager` define páginas e objetivo · 2. `ux-researcher` + `ui-designer` definem estilo (skills `hallmark` + `frontend-design`) · 3. `landing-page-copywriter` escreve os textos (skill `copywriting`) · 4. `frontend-developer` / `nextjs-developer` / `backend-developer` constroem · 5. `security-auditor`, `accessibility-tester`, `performance-engineer`, `seo-specialist` revisam em paralelo · 6. `qa-expert` testa (skill `webapp-testing`) · 7. `code-reviewer` dá o ok final |
| Bug | skill `systematic-debugging` + agente `debugger` |
| Revisar código | `code-reviewer` + `security-auditor` |
| Marketing / redes sociais / SEO | `content-marketer`, `seo-specialist`; skills `social`, `seo-audit`, `ai-seo`, `cro`, `schema` |
| Tarefa grande com várias etapas | `multi-agent-coordinator` / `workflow-orchestrator`; skills `planning-with-files`, `writing-plans`, `dispatching-parallel-agents` |
| Segurança / "deixa seguro" / antes de publicar | skill `site-fortress` (fase por fase) + agentes `security-auditor`, `code-reviewer`; skills `semgrep`, `sharp-edges`, `supply-chain-risk-auditor`, `fp-check` |
| Publicar site | skills `golive` (hospedagem, banco, domínio, pagamentos) ou `deploy-to-vercel`; MCP `vercel` |
| Banco de dados | skills `neon`, `neon-postgres`, `neon-auth`; MCP `neon` |
| "Quanto custa?" / custo-benefício | skill `cost-estimator` (preços de hoje, com fonte) |
| Link de vídeo (Instagram, TikTok, YouTube) | skill `video-link` |
| Obsidian | skills `obsidian-cli`, `obsidian-markdown`, `obsidian-bases`, `json-canvas`; `defuddle` para salvar páginas da web limpas |
| Notion | MCP `notion` |
| Criar um agente pessoal | skill `agent-builder` |
| Política de privacidade, termos, cookies, LGPD, "não ser processado" | skill `legal-compliance` |
| Melhorar foto / tirar fundo / recortar | skill `photo-editor` |
| Git, GitHub, criar repositório | skill `github-helper` |
| Mexer no PC, abrir programas, criar contas | skill `pc-control` |
| Trabalhos, relatórios, documentos | skill `doc-coauthoring` (+ `research-analyst` para pesquisa) |
| Entregar trabalho/tarefa no Microsoft Teams | skill `entregar-trabalho-teams` (só clica em Entregar depois do ok) |
| Fazer vídeo (Reels, TikTok, propaganda, explicativo) | skill `video-maker` (HyperFrames / Remotion) |
| Design de site (paleta, fontes, estilo por tipo de negócio) | skill `ui-ux-pro-max` + `hallmark` |
| "O que tá acontecendo na outra conversa?" (Claude Code) | skill `session-radar` |
| Conversas do Claude normal (claude.ai / app) | skill `claude-chats` (lê o "Exportar dados") |
| Documentação atualizada de biblioteca | plugin `context7` |
| Pagamentos | plugins `mercadopago`, `stripe` + fase 6 da `site-fortress` |
| Achar/instalar novas skills | skill `skill-hunter` (sempre verificar com `skill-inspector` antes) |
| Pôster, flyer, arte estática (PNG/PDF) | skill `canvas-design` |
| Componente pronto (card de preço, hero, gráfico, logo de marca) | skill `componentes-ui` (shadcn/Magic UI/Aceternity grátis) |
| Raspar várias páginas de um site | skill `raspar-site` (uma página: `defuddle`) |
| Visitas / analytics / "onde as pessoas desistem" | skill `analytics-gratis` |
| "Como funciona esse repositório do GitHub?" | MCP `deepwiki` (só repositórios públicos) |
| "Quanto do meu limite eu usei?" | `npx -y ccusage@20.0.34 daily --offline` ou a barra do `claude-hud` |
| Pesquisa grande e profunda | skill `deep-research` (vários agentes em paralelo); relatório do ecossistema em `Obsidian Vault/Claude/Pesquisa ecossistema Claude.md` |

## Sites que não parecem "vibe code"

- Sempre carregue `hallmark` e `frontend-design` antes de escrever UI.
- Nada de gradiente roxo genérico, emojis como ícones, cards iguais em grade, "Unlock the power of…".
  Escolha uma direção visual concreta (tipografia, paleta, grid) e mantenha.
- Textos reais e específicos do negócio — nunca lorem ipsum nem frases de marketing vazias.
- Segurança: validar toda entrada no servidor, nunca expor chaves no front-end,
  usar HTTPS, cabeçalhos de segurança (CSP, HSTS), dependências com versão fixa.
  **Todo site, sem exceção**, passa pela skill `site-fortress` inteira (inclui `legal-compliance`:
  política de privacidade, termos e cookies) antes de ser publicado. Não publicar com achado crítico/alto aberto.
- Pagamento com cartão: o site nunca vê nem guarda número de cartão — usar checkout
  hospedado (Stripe Checkout, Mercado Pago Checkout Pro) e confirmar pagamento só por webhook assinado.
- Antes de dizer "pronto": skill `verify-and-stop` / `verification-before-completion` — rodar, testar, conferir.

## Economia de tokens

- Investigar antes de agir (`investigate-first`), mudanças pequenas e cirúrgicas (`surgical-patch`).
- Ler só o trecho necessário de arquivos grandes; usar busca em vez de abrir tudo.
- Pesquisas amplas vão para subagentes, que devolvem só a conclusão.
- O usuário pode pedir respostas ultra-curtas com a skill `caveman`.

## Navegador

`.mcp.json` traz o Playwright MCP: abrir sites, pesquisar no Google, clicar, preencher,
tirar print. Para contas pessoais (Instagram, TikTok, WhatsApp) veja `SKILLS-CATALOG.md`,
seção "Precisa de você". Nunca enviar mensagem ou publicar sem o usuário confirmar texto e destinatário.

## Repositório público de skills

Tudo que for skill, agente ou kit para publicar vai para **um repositório só**: `matheus-rib1108/meu-kit-claude-code`
(local `~/repos/meu-kit-claude-code`). Sempre atualizar esse; nunca criar repositório novo. Usar a skill `kit-sync`.
