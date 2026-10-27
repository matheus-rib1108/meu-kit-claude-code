---
name: motion-sutil
description: Coloca animação e movimento com cara de site premiado (curvas próprias, duração certa, rolagem suave, hover magnético, revelação de texto) sem exagero e sem pesar o site, com prefers-reduced-motion — usando CSS puro, Motion (motion.dev), GSAP ou Lenis, todos grátis. Use quando o usuário pedir "animação", "efeito ao rolar", "deixa mais vivo", "transição suave", "hover bonito", "parallax", ou quando o site parecer parado ou animado demais.
---

# Movimento sutil

Junto com `apple-design` (física de mola e gestos) e `impeccable` (`/impeccable animate`).

## Regra principal

**Um movimento por intenção.** Mostrar que algo é clicável, guiar o olho para o próximo bloco ou dar retorno de ação. Se a animação não tem um desses trabalhos, tire. Site de IA anima **tudo** com o mesmo fade-up. Site premiado anima pouco e com curva própria.

## Curvas e durações (das referências)

```css
:root {
  --ease-saida: cubic-bezier(.16, 1, .3, 1);     /* expo-out: Lusion, Raycast, Cosmos */
  --ease-suave: cubic-bezier(.23, 1, .32, 1);    /* Locomotive, Raycast */
  --ease-mola: cubic-bezier(.34, 1.5, .64, 1);   /* overshoot: botão magnético do Dennis Snellenberg */
  --d-rapida: 160ms;  /* hover, foco, botão */
  --d-media: 320ms;   /* menu, abrir card */
  --d-lenta: 700ms;   /* entrada de seção, troca de página */
}
```

- **Entra com `ease-saida`** (começa rápido e para devagar). **Sai mais rápido do que entrou.**
- **Anime só `transform` e `opacity`**, e nunca `width`, `top` ou `box-shadow` em loop.
- **Atraso em cascata** de 40 a 80ms entre itens, no máximo 6 itens. Nada de 300ms por item.

## Receitas

1. **Revelar ao rolar (CSS puro, sem biblioteca):**
   ```css
   @supports (animation-timeline: view()) {
     .revela { animation: revela linear both; animation-timeline: view(); animation-range: entry 10% cover 30%; }
     @keyframes revela { from { opacity: 0; transform: translateY(24px); } }
   }
   ```
2. **Hover que "responde":** botão sobe 1 a 2px, a seta anda 4px e a cor muda em `--d-rapida`. Para o magnético, siga o mouse em até 8px com `--ease-mola` (Motion: `useSpring`).
3. **Título que se monta:** separe as palavras (não as letras) e dê `translateY(100%)` dentro de `overflow:hidden`, em cascata. Use só no hero.
4. **Rolagem suave:** Lenis (`lenis@1.3.x`) só em site de vitrine e portfólio. **Não use** em loja, dashboard ou formulário, porque atrapalha.
5. **Troca de página:** View Transitions API (`document.startViewTransition`, ou `@view-transition` no CSS). É grátis e nativo.
6. **Número que conta** (KPI, "+20 anos"): conte só uma vez ao entrar na tela, em menos de 1s, com `tabular-nums`.

**Bibliotecas** (fixe a versão exata no `package.json`):
- Motion (motion.dev): React e JS, com mola.
- GSAP + ScrollTrigger: sequências e scroll complexo; hoje é grátis.
- anime.js: microinterações leves.
- Animista e Coconut UI: copiar animações CSS prontas.

## Obrigatório

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; scroll-behavior: auto !important; }
}
```

Teste no celular médio (Chrome DevTools → CPU 4x mais lenta). Se travar, corte.
