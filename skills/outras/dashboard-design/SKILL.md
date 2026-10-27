---
name: dashboard-design
description: Desenha dashboards, painéis admin e telas de relatório com cara de produto de verdade (Linear, Stripe, Plausible, Mercury) e não de template — hierarquia de KPIs, gráfico certo para cada pergunta, cores de série, números tabulares em R$, tema claro e escuro, estados vazio e carregando, filtros de data. Use quando o usuário pedir "dashboard", "painel", "admin", "relatório com gráficos", "tela de métricas", "gráfico de vendas", "KPI", ou ao construir sistema interno, painel de loja ou SaaS.
---

# Dashboard design

Use junto com:
- `dataviz`: o método de cor e as marcas de gráfico. Leia antes do primeiro gráfico.
- `componentes-ui`: os gráficos prontos do shadcn (Recharts).
- `paleta-por-negocio`: a seção "Dashboard".
- `tipografia-pares`: a linha SaaS/dashboard.
- `anti-cara-de-ia`: a revisão final.

## 1. Comece pela pergunta, não pelo gráfico

Escreva as 3 a 5 perguntas que o dono faz toda manhã, por exemplo "vendi mais que ontem?", "qual produto sai mais?" e "quem está devendo?". **Cada pergunta vira um bloco.** O que não responde a nenhuma pergunta sai da tela.

## 2. Estrutura

- **Topo:** título da página, **um** filtro de data à direita (Hoje · 7 dias · 30 dias · Mês · Personalizado) e "comparar com o período anterior".
- **Linha de KPIs: 4 a 6, no máximo.** Cada um tem rótulo pequeno, valor grande e um delta com seta e cor (verde ou vermelho **só** no delta), além do período de comparação escrito. Sem ícone decorativo. KPI clicável escolhe a série do gráfico principal (padrão da Plausible).
- **Um gráfico grande** logo abaixo vale mais que seis pequenos.
- **Listas com barra de fundo** para os rankings ("produtos mais vendidos", "bairros"), não donut.
- **Tabela densa** no fim, com linhas de 36 a 40px, bordas de 1px e ações na linha.
- **Navegação:** sidebar fina à esquerda, ou abas no topo se houver até 5 seções. **Não ponha card dentro de card.**

## 3. Gráfico certo (FT Visual Vocabulary)

| Pergunta | Gráfico |
|---|---|
| Como mudou no tempo? | Linha (ou área com **uma** série) |
| Quanto de cada coisa? | Coluna/barra, eixo começando em 0 |
| Quem é maior? (ranking) | Barra horizontal ordenada |
| Parte de um todo | Coluna empilhada; donut **só** com 2 ou 3 partes |
| Distribuição | Histograma |
| Relação entre duas medidas | Dispersão |
| Onde? | Mapa coroplético |

- **Uma série = uma cor de destaque. O período anterior e "outros" ficam em cinza.**
- **Várias séries: 3 a 5 cores em ordem fixa**, com a cor da marca só no dado principal. Prefira rótulo direto no fim da linha a legenda (padrão da Our World in Data).
- **Só linhas de grade horizontais**, mais claras que os rótulos. Eixo Y com unidade curta ("R$ 12 mil", "1,2 mi").
- **O título do gráfico diz a conclusão**: "Vendas subiram 18% depois da promoção". Não "Vendas por mês".
- **Tooltip** com a data completa, o valor formatado e a comparação.

## 4. Números em pt-BR

```js
const brl = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' });
const curto = new Intl.NumberFormat('pt-BR', { notation: 'compact', maximumFractionDigits: 1 }); // 12,3 mil
const pct = new Intl.NumberFormat('pt-BR', { style: 'percent', maximumFractionDigits: 1, signDisplay: 'exceptZero' });
```

Valor, preço e ID com `font-variant-numeric: tabular-nums`. Mono (JetBrains/IBM Plex Mono) para ID e código.

## 5. Tema

- **Claro:** fundo off-white levemente tingido (#F7F7F5 ou #F6F9FC), texto navy ou quase-preto (#0A2540 ou #1C1B17).
- **Escuro:** fundo #08090A a #111214, com elevação pela **mudança de cinza** e não por sombra. Texto #E2E4E7, nunca #FFF em bloco.
- **Cinzas sempre tingidos** com a temperatura da paleta (Mercury #272735, Ramp #F4F2F0). Nunca o slate padrão do Tailwind.

## 6. Estados (o que separa produto de template)

- **Carregando:** skeleton no formato do gráfico ou da tabela. Nunca spinner no meio.
- **Vazio:** eixo e grade visíveis, com uma frase do que fazer ("Nenhuma venda hoje ainda. Os pedidos aparecem aqui em tempo real.").
- **Erro:** diga o que falhou e mostre um botão "tentar de novo".
- **Dado de exemplo** deve ser plausível para o negócio (valores em R$, nomes de produtos reais do cliente), nunca "Product A" ou "$12,345".

## Referências para abrir (sem login)

| Referência | Por que abrir |
|---|---|
| Plausible (plausible.io/plausible.io) | Painel ao vivo, hierarquia exemplar |
| Linear (linear.app) | Densidade e cinzas do tema escuro |
| Vercel Geist (vercel.com/geist/colors) | Escalas de cor em 10 passos |
| Tremor (tremor.so) | Props de gráfico |
| Our World in Data | Rótulo direto, abas Gráfico/Tabela |
| Stripe Sigma | Navy e cor só em ação |
