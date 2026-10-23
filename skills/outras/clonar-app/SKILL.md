---
name: clonar-app
description: Recria um site, app ou IA a partir de um link, print ou vídeo — estrutura, layout, funcionalidades e comportamento — em código próprio (Next.js/HTML), com textos, marca e imagens trocados pelos do usuário. Use quando o usuário disser "copia esse site", "clona esse app", "faz igual a esse", "quero um app tipo X", "faz uma IA igual ao ChatGPT/Character.ai", ou mandar link/print pedindo algo parecido.
---

# Clonar site, app ou IA

Objetivo: entregar uma versão **funcionando** que faz o mesmo que o original, mas com código, textos e marca próprios.

## Regra de ouro (não negociável)
- Copiar **estrutura, layout, fluxo e funcionalidades** — isso é livre.
- **Nunca** copiar logo, nome, marca, textos, fotos ou ícones proprietários. Trocar por conteúdo do usuário (ou placeholders reais do negócio dele, nunca lorem ipsum).
- Nunca fazer página que se passe pelo original (login falso, checkout falso, mesmo domínio parecido). Isso é golpe — recusar.
- Não burlar login, paywall ou captcha do site original; clonar só o que é público.
- Site do próprio usuário ou com permissão: pode copiar tudo.

## 1. Entender o original
| Entrada | Como estudar |
|---|---|
| Link de site | Navegador (`mcp__Claude_Browser__*` ou Playwright): `get_page_text`, `read_page`, screenshots em desktop **e** celular (`resize_window` mobile), rolar a página toda, abrir cada página do menu |
| Estilo visual | `javascript_tool` para ler cores, fontes, espaçamentos (`getComputedStyle`) — ou skill `hallmark` (modo study) |
| Print / foto | Ler a imagem e descrever cada seção |
| Vídeo / Reels do app | skill `video-link` (frames + transcrição) |
| Repositório GitHub público | MCP `deepwiki` para entender a arquitetura |
| App de celular | Prints das telas + descrição; recriar como web app (PWA) |
| IA (ChatGPT, Character.ai, assistente) | Anotar: personalidade, o que responde, ferramentas (busca, imagem, voz, memória), layout do chat |

Escrever em `clone-<nome>/PLANO.md`: lista de páginas/telas, componentes, funcionalidades, paleta, fontes. Mostrar ao usuário em 5–10 linhas e seguir (autonomia).

## 2. Construir
- Site simples → HTML/CSS único. Site com várias páginas, login ou banco → Next.js (ler `node_modules/next/dist/docs/` antes, a versão é nova).
- App → web app responsivo/PWA; banco com skill `neon`, login com `neon-auth`.
- **IA** → chat em Next.js chamando a API do Claude pelo servidor (skill `claude-api`, modelo mais recente). Personalidade no system prompt; streaming; histórico salvo no banco. Chave da API só no servidor (`.env`), nunca no front.
- Seguir a mesma ordem de seções e o mesmo comportamento (menus, animações, filtros, carrinho...). Fontes parecidas grátis do Google Fonts.

## 3. Conferir
- Abrir lado a lado com o original (screenshot dos dois, desktop e celular) e corrigir diferenças.
- Testar cada botão/fluxo (skill `webapp-testing`).
- Conferir que nenhum logo/texto/foto do original ficou.
- Antes de publicar: `site-fortress` + `legal-compliance` (regra do CLAUDE.md). Publicar com `deploy-to-vercel` e mandar o link.
