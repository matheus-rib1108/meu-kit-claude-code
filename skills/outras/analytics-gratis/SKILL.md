---
name: analytics-gratis
description: Coloca medição de visitas e desempenho num site de graça e sem cookie, como alternativa ao PostHog pago — Vercel Web Analytics + Speed Insights para sites na Vercel, ou Umami (código aberto, hospedado por você) para outros, com um checklist de onde as pessoas desistem. Use quando o usuário pedir "quero saber quantas visitas", "analytics", "onde as pessoas saem do site", "por que ninguém compra", "medir o site", "métricas", "Google Analytics sem cookie", ou ao publicar um site.
---

# Analytics grátis (alternativa ao PostHog)

Escolha pelo lugar onde o site está:

| Site em | Use | Cookie? | Conta nova? |
|---|---|---|---|
| Vercel (o padrão do usuário) | Vercel Web Analytics + Speed Insights | Não | Não, usa a conta Vercel que ele já tem |
| Outro lugar, ou ele quer os dados no próprio banco | Umami hospedado por você (Vercel + banco Neon grátis) | Não | Não, se já tiver Vercel e Neon |

## Vercel (Next.js)

1. Peça ao usuário para ligar a função no painel: projeto → **Analytics** → Enable, e **Speed Insights** → Enable. É um clique dele; você não mexe na conta.
2. No projeto:
   ```bash
   npm i @vercel/analytics@2.0.1 @vercel/speed-insights@2.0.0
   ```
   No `app/layout.tsx`, dentro do `<body>`:
   ```tsx
   import { Analytics } from "@vercel/analytics/next";
   import { SpeedInsights } from "@vercel/speed-insights/next";
   // ...
   <Analytics />
   <SpeedInsights />
   ```
   React puro: importe de `/react`. HTML estático: siga as instruções do painel.
3. Publique e confira depois de algumas visitas no painel (aba Analytics).
4. Eventos (clicou em "Comprar", enviou formulário): `import { track } from "@vercel/analytics"` e `track("clicou_comprar")`. O plano Hobby limita os eventos personalizados: confira no painel e na skill `cost-estimator` antes de prometer.

## Umami hospedado por você

Código aberto (MIT). Siga a documentação oficial (umami.is/docs) para publicar na Vercel com o banco Postgres da skill `neon`. Depois cole o `<script defer src=".../script.js" data-website-id="...">` no site. Para criar o banco e a hospedagem, use as skills `neon` e `golive` e peça o ok do usuário antes de criar algo.

## "Onde as pessoas desistem" sem ferramenta paga

O PostHog grava sessões; aqui você faz o mesmo raciocínio com os dados grátis:
1. Páginas com mais saída (Analytics → Pages) e o caminho até o botão principal.
2. Um `track()` em cada passo do funil (viu o produto → clicou → abriu o WhatsApp/checkout) para ver onde a contagem cai.
3. Speed Insights: página lenta no celular (LCP alto) perde gente. Corrija com a skill `vercel-optimize`.
4. Teste você mesmo no celular (skill `webapp-testing`): botão que não funciona, layout quebrado.

## Regras (LGPD)

- Esses dois não usam cookie nem guardam IP. Mesmo assim, cite a medição de visitas na política de privacidade (skill `legal-compliance`).
- Nunca mande nome, e-mail, telefone ou CPF em `track()`.
- Não instale gravação de tela (Hotjar, Clarity, PostHog replay) sem aviso e consentimento no banner de cookies.
