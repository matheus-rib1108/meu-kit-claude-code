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

| Site | Ramo | Tipografia | Paleta | O que pegar / por que não parece IA | Nota |
|---|---|---|---|---|---|
| **Pizza Amici** (pizza-amici.nl, Awwwards HM 2026) | Pizzaria | salo-variable em caixa alta com tracking −.015em; Awesome Serif; manuscrita La Belle Aurore; Azeret Mono 9.6px | dough #ECE6E1 · fundo #F2EDE9 · navy #0F2C56 (texto e botão) · red #C72531 · gold #E3AF04 · green #128643 · brown #4F3C2C | A paleta vem da massa e da caixa de pizza. Três vozes tipográficas com funções claras. O hero são 5 fotos reais que o botão "Shuffle" embaralha | 10 |
| **Sunbeam Bagels** (sunbeambagels.com, HM 2026) | Padaria/café | Belgard (serifa display) em `clamp(100px,21vw,350px)`; **corpo em mono** (forma-djr-mono) | creme #FCE9D5 · laranja #FFA344 · lilás #C3ABC6 · vermelho #F72F23 · preto | Corpo em mono é coisa que nenhum template faz. A paleta é estranha mas da marca. Os easter eggs são de brincadeira | 9 |
| **Flora Wellness Café** (florawellnesscafe.com, HM 2026) | Café | Adobe Caslon Pro em tamanho de corpo, sem título gigante | pergaminho #F2ECD9 · texto vinho #5F1E1B · botão #CE4C46 (raio 0) | O texto nunca é preto. Ilustração feita à mão e tom pessoal | 9 |
| **Caffè Gilli** (caffegilli.com, HM 2026) | Café/confeitaria | Cosen (serifa) com títulos revelados palavra por palavra; Greycliff | #FCFCFC · tinta #142342 · #C7D0E2 | A história real ("desde 1733") vira o título. Vídeo do próprio lugar | 8 |
| **Qissa** (qissa.co.uk, Nominee 2026) | Restaurante | **Cormorant Garamond peso 330**, 92px, −1.84px; Manrope no corpo (as duas são grátis) | --ink #05091A · --navy #0A1230 · --gold #C9A24B · --amber #E9A85C · --blossom #E7A6C4 · --cream #F6F1E7 | Os tokens têm nome. Peso variável "quebrado". O site conta a história do nome | 9 |
| **Restaurant GEM.** (restaurantgem.com, Nominee 2025) | Restaurante alto padrão | **Gilda Display + DM Sans** (grátis) | #151515 · superfície #1D1B19 · bronze #B58C67 · texto #FFF | Escuro quente e uma única cor de destaque. Os tokens são fáceis de copiar | 8 |
| **Burrito Madre** (burritomadre.rs, HM 2026) | Lanchonete | Deacon display + Figtree | marrom-pimenta #5F0E00 · laranja #F83E1C · pêssego #FAE8DF · verde #053626 | Paleta de comida, texto marrom. **Feito em Elementor**: dá para fazer premiado com ferramenta comum | 8 |
| **Deadstock Coffee** (deadstockcoffee.com, Nominee 2026) | Café jovem/hamburgueria | Display própria em 2 camadas (cheia + contorno) | amarelo #FFDB30 · quase-preto #09000E | Duas cores com atitude. Texto em gíria | 7 |
| **Rendezvous Barbers** (myrendezvous.ca, HM 2024) | Barbearia | Serifa de livro a 88px com **−4.5px** + máquina de escrever a 11px (grátis: Newsreader + IBM Plex Mono) | #000 · #FFF · laranja #FF622B · verde-claro #C7D9A7 | Barbearia sem bigode, couro e dourado; parece revista | 9 |
| **Il Colorista** (ilcolorista.salon, HM 2022) | Salão | **Karla peso 200** a 56px + Cormorant Garamond (tudo Google Fonts); corpo 24px | manteiga #FDEBBE · coral #F28A70 · rosa #D96772 · ardósia #2D4156 · texto #1F1F1F | O menu tipográfico é a peça principal. As cores saem do próprio cabelo colorido | 9 |
| **LAVA Dental** (lavadental.lv, HM 2026) | Dentista | Josefin Sans + Neue Montreal; escala inteira em `clamp()`; grid de 12 colunas com subgrid | verde #031C14 · creme #DDEFDE · bronze #DBC093 · #779E91 | Dentista **sem azul e sem dente de stock** | 10 |
| **MINEMAL Dental** (minemal.dental, HM 2024) | Estética dental | Uma fonte própria, títulos de 100 a 200px com −2 a −4px | #F6F4EF · #242424 · ocre #D9A42F · vinho #9A3E3E | Clínica com cara de estúdio | 8 |
| **Arbor Dental** (arbordentalnyc.com, Nominee 2025) | Dentista de bairro | proxima-nova, corpo 25px | #080808 · petróleo #3A8197 · #667D90 | Endereço e telefone no primeiro bloco. Fundo escuro em clínica | 8 |
| **Kindred Pet Care** (kindredpetcare.com, HM 2024) | Veterinária/pet | Display com caráter + Inter; tamanhos em vw | rosa #F745AB · ardósia #2C3547 · creme #F8F3EE | Foge do verde-menta + pata. Muita foto real de bicho | 9 |
| **Coutumes** (coutumes.com, HM 2026) | Loja/acessórios | Plaak a 122px contra corpo de 12px | #000 · #FFF · âmbar #F9AF26 · areia #EDE9DF | Shopify que não parece tema. Preço no botão | 9 |
| **Estudio Niksen** (estudioniksen.com, Nominee 2026) | Loja de roupa | Neue Montreal + Frama, −.035em | Monocromático; a cor vem das fotos | Foto de campanha de verdade, sem selo gritando | 7 |
| **Fenriz Gym** (fenriz-gym.com, Nominee 2024) | Academia/luta | Kenyan Coffee condensada em caixa alta | carvão #1C1C1C + **uma cor pastel por modalidade** | Academia sem neon e sem "no pain no gain". O bairro está no slogan | 8 |
| **Mocotó** (mocoto.com.br) | Restaurante (BR) | Display com maiúsculas e minúsculas misturadas, estilo letreiro/cordel | vermelho #D64F54 · amarelo #FDB913 · marrom #4D2F29 | Cultura nordestina na tipografia | 7 |
| **Bráz Pizzaria** (familiabraz.com.br, BR) | Pizzaria (BR) | Display inline de letreiro antigo | tijolo #A6302C · creme #F1E1CF | Cor de forno e fachada. Texto afetivo em português | 7 |

**Floricultura:** não há floricultura premiada no ar com qualidade. Use como base a paleta e tipografia do Flora Café e do Il Colorista, mais as paletas "Jardim", "Peônia" e "Estufa" da `paleta-por-negocio`.
