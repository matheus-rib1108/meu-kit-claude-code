---
name: paleta-por-negocio
description: Escolhe a paleta de cores de um site ou app pelo tipo de negócio (pizzaria, hamburgueria, açaí, restaurante, salão, barbearia, clínica, dentista, floricultura, loja de roupa, academia, pet shop, imobiliária, advocacia, escola, SaaS, dashboard), com base em psicologia das cores com evidência (não mito), cultura brasileira e contraste WCAG conferido por script. Use quando o usuário pedir "que cores usar", "paleta para…", "cores de pizzaria/clínica/…", "psicologia das cores", "essa cor combina?", "o contraste está bom?", ou ao começar o design de qualquer site de negócio.
---

# Paleta por negócio

Base: `references/psicologia-e-paletas.md`, com 19 estudos citados, o capítulo "Brasil" e **45 paletas prontas** (3 por ramo), todas com contraste calculado.

## Processo

1. **Ramo e público.** Pergunte só o que faltar: o ramo, o público (família, jovem, alto padrão) e as cores que a marca já tem (logo, fachada, uniforme). **A cor da marca existente manda**: ajuste o resto em volta dela.
2. **3 opções.** Abra a seção do ramo em `references/psicologia-e-paletas.md` e mostre as 3 paletas com o "quando usar" de cada uma. Se a marca já tem cor, adapte a paleta mais próxima.
3. **Confira o contraste** de cada par que vai virar texto:
   ```bash
   node ~/.claude/skills/paleta-por-negocio/scripts/contraste.mjs '#TEXTO' '#FUNDO' '#TEXTO_BOTAO' '#BOTAO'
   ```
   O texto normal precisa de **AA (≥ 4.5:1)**. O texto grande (≥ 24px, ou 18,66px em negrito), os ícones e as bordas de campo precisam de **≥ 3:1**. Cor de "destaque" que reprova fica só **decorativa** (fundo de selo, ilustração), nunca em texto.
4. **Vire tokens** no CSS: `--fundo`, `--superficie`, `--texto`, `--texto-suave`, `--destaque`, `--cta`, `--cta-texto`. Nada de hex solto no meio do código.
5. **Siga com** `referencias-design` (para comparar com sites reais do ramo) e `anti-cara-de-ia`.

## O que a evidência diz (resumo; detalhes e fontes no reference)

- **Cor não vende sozinha.** O efeito vem do contexto e do *encaixe* com a marca (Labrecque & Milne 2012). Uma cor "certa" com foto ruim perde para uma cor neutra com foto boa.
- **"Vermelho dá fome" é mito.** Em estudo, prato ou copo vermelho levaram as pessoas a comer e beber **menos** (Genschow 2012). Em comida, o vermelho funciona como sinal de marca, urgência e destaque, não como apetite.
- **Azul** é associado a confiança e calma, e fundo azul faz a espera parecer mais curta (Gorn 2004). **Verde** puxa natureza e saúde. **Preto + dourado ou bege** passa luxo e sobriedade. **Rosa e nude** remetem a beleza e cuidado.
- **Brasil:** verde e amarelo juntos ganharam leitura política desde 2018, e vermelho chapado pode ser lido como partido. Evite os dois combinados em marca neutra. Cores de time dividem público. Preto e roxo lembram luto.
- **Cores que já têm dono:** roxo-Nubank, amarelo-Smart Fit, vermelho-Santander/Bradesco. Copiar essas faz o negócio parecer imitação.

## Regras rápidas

- **1 cor de destaque + neutros tingidos** (bege quente ou cinza azulado), nunca #000 e #FFF puros em tudo.
- **O CTA tem a cor mais forte da página e só ele usa essa cor.** Se tudo é vermelho, nada é botão.
- **A foto do produto é a maior fonte de cor.** Pizza, açaí e flores já são coloridos, então o fundo deve ser calmo.
- **Teste em tons de cinza** (filtro do DevTools). Se a hierarquia some, ela dependia só da cor.
- **Daltonismo:** nunca use só cor para dizer certo ou errado (WCAG 1.4.1). Junte ícone ou texto.
- **Tema escuro** é paleta própria, não inversão. Use o fundo #121212–#1B1714, e o texto nunca #FFF puro em blocos longos.

Teste do script: `node ~/.claude/skills/paleta-por-negocio/scripts/contraste.mjs --teste`
