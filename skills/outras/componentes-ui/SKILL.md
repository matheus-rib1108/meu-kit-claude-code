---
name: componentes-ui
description: Busca e instala componentes de interface prontos e grátis (botão, card de preço, hero, gráfico, formulário, bento, animações) dos catálogos shadcn/ui, Magic UI e Aceternity pelo CLI do shadcn, e logos de marcas pelo SVGL, sem conta nem chave de API — alternativa ao 21st.dev Magic. Use quando o usuário pedir "um componente de…", "card de preço", "seção hero bonita", "gráfico pronto", "botão animado", "logo da marca X", "acha um componente pronto", ou ao montar telas em React/Next.js com Tailwind.
---

# Componentes de UI grátis (alternativa ao 21st.dev Magic)

Sem conta, sem chave. Funciona em projeto React/Next.js com Tailwind. Versão fixa do CLI: `shadcn@4.22.1`.

## 1. Buscar (não instala nada)

```bash
npx -y shadcn@4.22.1 search @shadcn -q "<termo>" -l 10
npx -y shadcn@4.22.1 search @magicui -q "<termo>" -l 10
npx -y shadcn@4.22.1 search @aceternity -q "<termo>" -l 10
```

- Busque com termos em inglês: `pricing`, `hero`, `chart`, `card`, `navbar`, `testimonial`, `bento`, `marquee`, `form`, `footer`.
- `@shadcn`: base sóbria (button, dialog, form, chart, sidebar). `@magicui`: animações e efeitos. `@aceternity`: blocos de landing page (pricing, hero, features).
- Mostre ao usuário 3 a 5 opções com o nome e a descrição. Para ver o código antes: `npx -y shadcn@4.22.1 view @magicui/marquee`.
- **Confira se é grátis com `view` antes de oferecer.** O Aceternity mistura itens grátis e Pro: se aparecer "You are not authorized", o item é pago e você pula. Muitos blocos de pricing do Aceternity são Pro. Em geral os do tipo `ui` são grátis, e @shadcn e @magicui são grátis.

## 2. Instalar no projeto

1. Se o projeto não tem `components.json`: `npx -y shadcn@4.22.1 init` (pergunte antes, porque mexe no CSS global).
2. `npx -y shadcn@4.22.1 add @magicui/marquee` (troque pelo item escolhido).
3. O código vem para `components/` e é **seu**: adapte textos, cores e fontes ao design do projeto (skills `hallmark` e `frontend-design`). Não deixe o texto de exemplo em inglês nem números de mentira.
4. Rode o build e abra no navegador para conferir (skill `webapp-testing`).

## 3. Logos de marcas (SVGL, grátis)

```bash
curl -s "https://api.svgl.app?search=github"
```

Devolve JSON com o link do SVG (`route`, versão clara e escura). Use só para mostrar integrações ou "funciona com". Logo de marca não é seu: não altere nem use como se fosse da sua empresa.

## Regras

- Componente baixado é código de terceiro: leia o arquivo antes de rodar e veja as dependências novas que o `add` instalou no `package.json`.
- Não misture os três estilos na mesma página. Escolha um catálogo e adapte ao visual do projeto, para não ficar com "cara de template".
- Sem projeto React/Tailwind (HTML puro): use `view` para ler o código e reescreva em HTML/CSS.
