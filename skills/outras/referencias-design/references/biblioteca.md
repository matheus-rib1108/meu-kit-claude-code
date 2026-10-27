# Biblioteca de referências: análise completa

Pesquisa de 26/10/2026. As fontes e os hex vêm do CSS/HTML de cada site e da extração com `skillui --url` (marcados como **SkillUI**). "Não lido" quer dizer que não foi possível confirmar.
Para cada site: **o que pegar** e **por que não parece IA**.

## Tokens extraídos com SkillUI (16 sites)

| Site | Tema | Fontes | Fundo · superfície · texto · suave · destaque |
|---|---|---|---|
| cosmos.so | escuro | cosmosOracle (Dinamo Oracle), SF Mono | #000000 · #383838 · #F7F5F3 · #8C8C8C · #FECDD3 |
| dennissnellenberg.com | escuro | Dennis Sans (própria) | #1C1D20 · #101010 · #FFFFFF · #646464 · #FFFF00 |
| linear.app | escuro | Inter Variable, Berkeley Mono | #080808 · #191D20 · #FFFFFF · #9C9DA1 · #7170FF |
| locomotive.ca | escuro | LocomotiveNew, Helvetica Now Display | #000000 · #292625 · #FFFFFF · #A7A4A4 · #DA382E/#312DFB |
| mercury.com | claro | Arcadia Display, Arcadia, IBM Plex Mono | #FFFFFF · #F5F5F5 · #272735 · #716B96 · #188554 |
| nothing.tech | escuro | NType82, Geist, Geist Mono | #000000 · #450A0A · #FFFFFF · #9CA3AF · #27D4E0 |
| ourworldindata.org | claro | Lato, Playfair Display (títulos) | #FFFFFF · #E7F2FF · #002147 · #577291 · #B40000 |
| plausible.io | claro | Roboto/sistema | #F8F8F8 · — · #1A202C · #6B7280 · #5F48FF |
| play.date | claro | Roobert | #FFFFFF · #F2EFE6 · #000000 · #948A78 · amarelo do produto |
| posthog.com | claro | IBM Plex Sans Variable, Source Code Pro | #EEEFE9 (creme) · — · #1E1F23 · — · #F54E00 |
| pudding.cool | claro | Tiempos Text, Atlas Grotesk | #FFFFFF · — · #000000 · #A8A8A8 · #F693FF |
| ramp.com | claro | Lausanne, IBM Plex Sans/Mono | #F4F2F0 (papel) · #FFFFFF · #1C1B17 · — · #0066FF |
| raycast.com | escuro | Instrument Serif, Inter, Geist Mono | #111214 · #000000 · #FFFFFF · #545F66 · #FF6363 |
| resend.com | claro/escuro | Domaine (serifa), ABC Favorit, Commit Mono | #000000 · — · #FFFFFF · #A0A0A0 · monocromático |
| teenage.engineering | claro | te-40, te-20 (próprias) | #FFFFFF · #F1F2F2 · #000000 · #73859F · — |
| wearecollins.com | claro/escuro | COLLINS Portrait (serifa), Graphik | #F8F8F7 · #140700 · — · #5E5855 · #FF7600 |

## Portfólio / estúdio

- **Dennis Snellenberg**, dennissnellenberg.com (Awwwards SOTD)
  - **Tipografia:** uma fonte própria; display `clamp(3.25em, 7vw, 8em)` com entrelinha 1.065; corpo `clamp(16px,1.2vw,19px)`.
  - **Movimento:** GSAP, Barba e Locomotive Scroll; botão magnético com overshoot `.34,1.5,.64,1`.
  - **Hero:** nome gigante e vídeo do rosto.
  - **Pegar:** escala fluida e um único azul #455CE9.
  - **Não parece IA porque:** é a pessoa no centro, não cards de serviço.
- **Lusion**, lusion.co (Awwwards SOTD, Developer Award)
  - **Tipografia:** Aeonik com IBM Plex Mono, tipo em vw, tracking -.02em e +.1em nos rótulos mono.
  - **Paleta:** #000, #F0F1FA, acentos #1A2FFB e #C1FF00.
  - **Hero:** cena WebGL.
  - **Pegar:** acento ácido sobre neutro e mono nos rótulos (o 3D é caro demais).
- **Locomotive**, locomotive.ca (SOTD)
  - **Tipografia:** fonte própria com Helvetica Now.
  - **Cor:** **o fundo muda por seção** (branco, preto, vermelho #DA382E, azul #312DFB).
  - **Pegar:** seções de cor chapada e humor de marca.
- **Obys**, obys.agency (SOTD)
  - **Sistema:** uma fonte, um peso, preto e branco puro; toda a expressão está na imagem e no movimento.
  - **Pegar:** restrição autoral.
- **COLLINS**, wearecollins.com
  - **Tipografia:** serifa Portrait com Graphik, tracking -.25px.
  - **Cor:** preto quente #140700, off-white #F8F8F7, laranja #FF7600 só como acento.
  - **Pegar:** neutros quentes e voz de manifesto ("Rewrite your worth.").
- **darkroom.engineering** (criadores do Lenis)
  - **Tipografia:** fontes próprias; display a 17–27vw com tracking -.05em; escala "px do Figma → vw".
  - **Paleta:** cinza com vermelho em 3 tons.

## SaaS / produto

- **Linear**, linear.app
  - **Tipografia:** Inter Variable em pesos 510/590/680, `tabular-nums slash-zero`.
  - **Cor:** fundo #08090A com cinzas em degraus e accent #7170FF dessaturado.
  - **Imagem:** screenshot real.
  - **Aviso:** de tão copiado, virou clichê. Use como aula de controle, não como visual.
- **Raycast**, raycast.com
  - **Tipografia:** Inter, Instrument Serif itálica, Geist Mono e VT323 (pixel).
  - **Cor:** escuro #101111 com vermelho #FF6363.
  - **Detalhes:** teclas desenhadas.
  - **Pegar:** a mistura sans + serifa + pixel, arriscada mas coerente.
- **Mercury**, mercury.com
  - **Tipografia:** Arcadia, **Tiempos** (serifa) e Plex Mono, com pesos 320/360; display `clamp(2.625rem, .979rem + 4.116vw, 6rem)`.
  - **Cor:** tinta #272735.
  - **Imagem:** foto conceitual.
  - **Pegar:** banco com cara de revista. Serifa passa confiança.
- **Resend**, resend.com
  - **Tipografia:** Domaine (serifa) com Favorit e Commit Mono; display `clamp(4rem,10.26vw,7.5rem)` com entrelinha .84.
  - **Cor:** monocromático, sem acento.
  - **Pegar:** serifa apertada em produto técnico e código como conteúdo.

## Landing de produto

- **Playdate**, play.date
  - **Tipografia:** Roobert.
  - **Cor:** **a paleta vem da tela LCD do aparelho**.
  - **Estrutura e texto:** capítulos ("The Crank."), texto engraçado e curto.
  - **Pegar:** a cor do produto como paleta.
- **teenage engineering**, teenage.engineering
  - **Tipografia:** fontes de laboratório, tudo em minúscula.
  - **Visual:** quase sem cor; hover = fundo #F1F2F2 sem sombra.
  - **Pegar:** premium sem animação nenhuma.
- **Nothing**, nothing.tech
  - **Tipografia:** fonte de pontos Ndot (o LED do aparelho), Geist e mono, com rótulos a .1em.
  - **Pegar:** a identidade do produto virando tipografia.
- **Cosmos**, cosmos.so (SOTD)
  - **Tipografia:** Oracle, display a 19vw, tracking graduado de -.01 a -.05em.
  - **Cor:** off-white quente #F7F5F3 e 6 degraus de cinza nomeados.
  - **Imagem:** masonry de imagens reais.
  - **Pegar:** título gigante sobre uma colagem real.

## Dashboard e dataviz

| Ref | O que pegar |
|---|---|
| Plausible (plausible.io/plausible.io) | 6 KPIs em linha com delta que escolhem a série; 1 gráfico de linha; listas com barra de fundo no lugar de donut |
| Linear | Densidade, cinzas escuros #08090A/#0F1011/#161718, números tabulares |
| Vercel Geist (vercel.com/geist/colors) | Escalas de 10 passos com função definida; Geist + Geist Mono |
| Stripe Sigma | Navy #0A2540 em vez de preto; roxo #635BFF só em ação; peso 425 |
| PostHog | Fundo creme #EEEFE9; trends em linha, funil em barra, retenção em tabela com intensidade |
| Mercury | Saldo em fonte display; transações em mono; cinza-violeta #272735 |
| Ramp | Papel #F4F2F0 com preto esverdeado; mono nos valores |
| Attio | Tabela tipo planilha, grade tracejada `4 6` |
| Tremor | Ordem de cores blue, emerald, violet, amber; `valueFormatter`; yAxis 56px |
| Our World in Data | Rótulo direto no fim da linha; abas Gráfico/Mapa/Tabela; título com conclusão |
| The Pudding | Anotação escrita no gráfico; direção de arte por matéria |
| Datawrapper (guia de cor) | 3 a 10 cores; cinza para "outros"; marca só no dado principal |
| FT Visual Vocabulary | Qual gráfico para cada pergunta (9 categorias) |

## Comércio local

(Abaixo, preenchido pela pesquisa de comércio local.)
