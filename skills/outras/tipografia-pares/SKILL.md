---
name: tipografia-pares
description: Escolhe fontes e pares de fontes grátis (Google Fonts, Fontshare, OFL) com escala, pesos, entrelinha e espaçamento entre letras prontos em CSS, por tipo de negócio e estilo, tirados de sites premiados — para fugir de "Inter em tudo". Use quando o usuário pedir "que fonte usar", "par de fontes", "tipografia", "deixa o título mais bonito", "fonte para pizzaria/clínica/…", ou ao definir o design de um site, app ou dashboard.
---

# Tipografia e pares de fontes

Os sites premiados quase nunca usam uma fonte só, e nunca a fonte padrão. Usam **contraste** (serifa + sans, ou sans + mono para rótulos) e ajustam tamanho, peso e espaçamento à mão.

## 1. Escolha o par (todas grátis para uso comercial)

| Estilo | Título | Texto | Rótulo / número | Parecido com (pago) |
|---|---|---|---|---|
| Editorial e confiável | Newsreader ou Source Serif 4 | Hanken Grotesk | IBM Plex Mono | Mercury (Tiempos + Arcadia) |
| Elegante e premium | Instrument Serif | Schibsted Grotesk | JetBrains Mono | Raycast, Resend (Domaine) |
| Quente e artesanal | Fraunces (eixo "soft") | Work Sans | — | COLLINS (Portrait + Graphik) |
| Moderno com personalidade | Bricolage Grotesque | Bricolage Grotesque (peso menor) | Commit Mono | Cosmos (Oracle) |
| Técnico e limpo | Familjen Grotesk ou Onest | Onest | Geist Mono | Linear, Vercel |
| Display marcante (Fontshare) | Clash Display ou Cabinet Grotesk | Satoshi ou General Sans | — | Estúdios Awwwards |
| Industrial / produto | Space Grotesk só no display + mono | Manrope | Space Mono | Nothing, teenage engineering |

**Por ramo (ponto de partida):**
- Pizzaria e cantina: Fraunces + Work Sans.
- Hamburgueria: Bricolage Grotesque condensada em peso 800 + Manrope.
- Açaí e doceria: Fraunces soft + Onest.
- Restaurante e bistrô: Newsreader + Hanken Grotesk.
- Barbearia: Clash Display + Satoshi.
- Salão e estética: Instrument Serif + Schibsted Grotesk.
- Clínica e dentista: Source Serif 4 + Onest. Dá confiança sem ficar frio.
- Advocacia: Newsreader + Hanken Grotesk.
- Academia: Cabinet Grotesk peso 800 + General Sans.
- Pet shop e escola: Bricolage Grotesque + Onest.
- SaaS e dashboard: Onest ou Hanken Grotesk + JetBrains Mono para os números.

Fuja de usar **sozinhas**: Inter, Roboto, Poppins, Montserrat, Open Sans e Playfair Display. Hoje elas denunciam "template".

## 2. Escala e ajustes (copie e adapte)

```css
:root {
  --f-titulo: "Fraunces", Georgia, serif;
  --f-texto: "Work Sans", system-ui, sans-serif;
  --f-mono: "JetBrains Mono", ui-monospace, monospace;

  --t-display: clamp(2.75rem, 1.2rem + 6.5vw, 7rem);  /* hero */
  --t-h2: clamp(1.9rem, 1.2rem + 2.6vw, 3.25rem);
  --t-h3: clamp(1.25rem, 1.05rem + .8vw, 1.6rem);
  --t-corpo: clamp(1rem, .96rem + .2vw, 1.125rem);
  --t-pequeno: .8125rem;
}
h1 { font: 600 var(--t-display)/0.95 var(--f-titulo); letter-spacing: -0.035em; text-wrap: balance; }
h2 { font: 600 var(--t-h2)/1.05 var(--f-titulo); letter-spacing: -0.02em; text-wrap: balance; }
body { font: 400 var(--t-corpo)/1.6 var(--f-texto); }
p { max-width: 65ch; text-wrap: pretty; }
.rotulo { font: 500 var(--t-pequeno)/1.2 var(--f-mono); letter-spacing: .08em; text-transform: uppercase; }
.numero { font-variant-numeric: tabular-nums; }
```

Regras que saíram das referências:
- **Título grande pede entrelinha < 1.1 e tracking negativo** (de -0.02 a -0.05em). **Texto pequeno em caixa alta pede tracking positivo** (+0.05 a +0.12em).
- **Pesos fora do padrão** dão acabamento: 450, 550 e 650 em fontes variáveis (Linear usa 510/590, Mercury 320/360).
- **Números em tabela, preço e KPI:** `tabular-nums`, para os dígitos não "dançarem".
- **Corpo com 60 a 75 caracteres por linha**, no máximo 2 famílias e mais uma mono.
- **Carregue só os pesos usados**, com `font-display: swap`. Fontes do Google: `<link>` com `&display=swap` ou `next/font`. Teste também o fallback.

## 3. Confira

Faça um print do hero e de um bloco de texto no celular. Pergunte: dá para saber o ramo do negócio **só pela tipografia**? Se não dá, troque o título.
