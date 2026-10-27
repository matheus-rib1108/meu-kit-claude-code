---
name: referencias-design
description: Biblioteca de referências de design reais (sites premiados no Awwwards, Godly, Siteinspire, Land-book, Lapa Ninja e outros, mais de 500 sites) organizada por categoria (comércio local, landing, portfólio, e-commerce, SaaS, dashboard, dataviz, app), com análise de tipografia, paleta, grid, hero e movimento, tokens extraídos com SkillUI e um processo obrigatório "referência antes de código". Use SEMPRE que for criar ou refazer um site, landing page, loja, portfólio, app ou dashboard, quando o usuário pedir "faz um site bonito", "com cara de site caro", "sem cara de IA", "me dá referências", "sites parecidos com…", ou mandar um link de site que ele gostou.
---

# Referências de design

IA sem referência entrega a média da internet. Esta skill obriga a começar por sites reais e bons.

## Processo obrigatório (5 passos)

1. **Escolha 3 a 5 referências** do mesmo tipo de negócio ou do estilo que o cliente quer:
   - `references/biblioteca.md`: cerca de 50 sites com análise completa e tokens.
   - `references/lista-ampla.md`: mais de 500 sites, uma linha cada.

   Misture pelo menos 1 do ramo do cliente com 1 de fora do ramo (é daí que vem a ideia que ninguém do ramo usou). Mostre as escolhidas ao usuário com 1 frase do porquê de cada uma.
2. **Extraia os tokens** das que estão no ar:
   ```bash
   skillui --url https://site-de-referencia.com --out ./.referencias --format design-md
   ```
   O resultado é um `DESIGN.md` com cores, fontes, espaçamento, raio, sombra, movimento e print. Se o site bloquear, use a análise da biblioteca. Para empresas conhecidas, também há DESIGN.md prontos em github.com/VoltAgent/awesome-design-md (Mercury, Linear, Resend, PostHog, Raycast, Notion, Airbnb…).
3. **Defina UMA direção** num bloco curto e mostre ao usuário antes de construir:
   - **Tipografia:** o par, de `tipografia-pares`.
   - **Paleta:** de `paleta-por-negocio`, com o contraste conferido.
   - **Grid e densidade.**
   - **Hero:** o que é o protagonista. O produto real, nunca um mockup genérico.
   - **Movimento:** 1 ou 2 movimentos, de `motion-sutil`.
   - **"O que vamos pegar de cada referência" e "o que NÃO vamos copiar".**

   **Não copie** logo, texto, fotos nem layout inteiro: pegue princípios e tokens. Fontes pagas (Tiempos, Söhne, Domaine…) viram a alternativa grátis da `tipografia-pares`.
4. **Construa** com `hallmark` e `frontend-design`; componentes de `componentes-ui`; dashboards com `dashboard-design`.
5. **Compare lado a lado antes de entregar.** Tire print do seu site e das referências na mesma largura (1440 e 390px). Responda:
   - O nível de acabamento está igual?
   - O que denuncia que o meu é feito por IA? (Rode `anti-cara-de-ia` e o detector.)
   - Dá para saber o ramo do negócio sem ler o texto?

   Corrija até as respostas serem "sim, nada, sim". Depois faça `impeccable` → `polish`.

## O que os melhores têm em comum (resumo da pesquisa)

- **Fonte própria ou incomum**, quase sempre em **par contrastante**: serifa + sans, ou sans + mono para rótulos.
- **Título gigante em `clamp()`/vw**, com entrelinha < 1.1 e tracking negativo.
- **Neutros escolhidos à mão:** off-white quente (#F7F5F3, #F8F8F7) e quase-preto (#140700, #1C1D20, #08090A). Nunca #FFF/#000 em tudo.
- **1 ou 2 cores de destaque, no máximo**, às vezes tiradas do produto físico (o amarelo do Playdate, o LED da Nothing).
- **Conteúdo real como imagem:** produto, comida, lugar, tela do app, vídeo do trabalho. Nada de ilustração de banco.
- **Texto com voz** ("It's yellow. There's a crank."), específico, curto e às vezes com humor.
- **Movimento com curva própria** (`cubic-bezier(.16,1,.3,1)`), pouco e com propósito.

## Comércio local brasileiro

O que diferencia na prática:
- Foto boa do produto e do lugar.
- Cardápio, serviços e preço claros.
- Botão de WhatsApp e de agendamento visível.
- Horário e mapa.
- Avaliações reais do Google.

O visual "premiado" entra na tipografia, na cor e no acabamento, **sem esconder essas informações**. Veja a seção "Comércio local" da biblioteca.
