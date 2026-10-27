---
name: anti-cara-de-ia
description: Revisa e corrige sites e apps com "cara de feito por IA" (gradiente roxo, cards iguais em grade, hero centralizado genérico, emoji como ícone, fonte Inter em tudo, sombra e canto arredondado padrão, texto vazio, depoimento falso), com detector automático no código e uma tabela "isso → faça isto" baseada em sites premiados de verdade. Use antes de entregar qualquer site/página/dashboard, quando o usuário disser "tá com cara de IA", "parece template", "parece vibe code", "deixa mais profissional", "deixa com cara de caro", ou ao revisar um design.
---

# Anti-cara-de-IA

Funciona junto com `hallmark` (direção e slop test), `impeccable` (`/impeccable audit` e `polish`), `referencias-design` (de onde vêm as alternativas) e `paleta-por-negocio`.

## 1. Detector automático (30 s)

```bash
node ~/.claude/skills/anti-cara-de-ia/scripts/detectar.mjs <pasta-do-projeto>
```

Ele aponta arquivo:linha de cada sinal: gradiente roxo, Inter sozinha, emoji como ícone, texto de marketing vazio, lorem ipsum, sombra e arredondado de template, orbe borrado, grade de pontinhos, ícone de brilho, travessão em texto, número inventado e #FFF/#000 puros. Se não achar nada, isso **não** prova que está bom. Faça o passo 2.

## 2. Revisão visual (abra no navegador, celular e desktop)

Tire print e compare **lado a lado** com 2 referências do mesmo ramo (`referencias-design`). Passe a tabela:

| Sinal de IA | Faça no lugar | Quem faz assim |
|---|---|---|
| Gradiente roxo/índigo, orbes borrados, neon | 1 cor de destaque do ramo + neutros tingidos (`paleta-por-negocio`) | Mercury (#272735 + 1 acento), COLLINS (preto quente #140700 + laranja) |
| Inter/Geist/Space Grotesk em tudo | Par com contraste: serifa de título + sans de texto, ou uma fonte com personalidade (`tipografia-pares`) | Mercury (Tiempos + Arcadia), Resend (Domaine + Favorit), Raycast (Instrument Serif + Inter) |
| Hero centralizado: título + subtítulo + 2 botões + mockup flutuando | Hero com o **produto real** grande (foto da pizza, do salão, a tela do app) e texto alinhado à esquerda ou título gigante em `clamp()` | Cosmos (título 19vw + colagem real), Playdate (o aparelho), Dennis Snellenberg (rosto + nome) |
| 3 cards iguais "Rápido / Seguro / Fácil" com ícone | Uma lista editorial com números, uma foto por serviço, ou um único argumento forte por seção | Locomotive (seções de cor chapada), teenage engineering (catálogo seco) |
| Bento grid, janela de terminal decorativa, dot grid | Conteúdo real: cardápio com preço, fotos do lugar, print do produto, mapa | PostHog (telas do produto), Linear (screenshot real) |
| Emoji ou ícone Lucide genérico como ícone | Ícone próprio, ícones de uma família só e com traço consistente (Phosphor), ou nenhum ícone | Lusion (41 SVGs próprios), Linear |
| `rounded-2xl` + `shadow-xl` em tudo | Raio pequeno e coerente (0–8px), borda de 1px, elevação por mudança de cinza | Linear, Attio, Vercel |
| Branco #FFF e preto #000 puros | Off-white quente (#F7F5F3, #F8F8F7) e quase-preto (#140700, #1C1D20, #08090A) | Cosmos, COLLINS, Dennis, Linear |
| "Unlock the power", "Transforme seu negócio", "Solução completa" | Frase específica do negócio, com número verdadeiro ou detalhe concreto ("Forno a lenha desde 1998, entrega até 23h no Centro") | Playdate ("It's yellow. There's a crank."), COLLINS ("Rewrite your worth.") |
| Depoimento e número inventados, 5 estrelas sem fonte | Avaliações reais do Google (com link) ou nada | — |
| 3 planos de preço por padrão | Só se o negócio vende planos. Comércio local mostra cardápio, serviços e preço real | — |
| Animação em tudo (fade-up em cada bloco, seta pulando) | 1 ou 2 movimentos com propósito e curva própria (`motion-sutil`) e `prefers-reduced-motion` | Dennis (botão magnético), Raycast (`.16,1,.3,1`) |
| Foto de banco de imagem genérica | Fotos do próprio negócio (`photo-editor` para tratar). Na falta, ilustração ou tipografia, nunca stock genérico | Locomotive (cultura real), Nothing (produto) |
| Falta favicon, 404, meta description, política de privacidade | Básico de acabamento: favicon, `<title>` e descrição por página, 404 própria, termos e privacidade (`legal-compliance`), logo clicável, sem rolagem horizontal no celular | Lista de 12 itens de @tommello.edit (Instagram) |

## 3. Regra de ouro

**Referência antes de código.** IA sem referência devolve "a média da internet". Antes de construir, escolha 3 a 5 referências reais (`referencias-design`), extraia os tokens (`skillui --url`) e decida **uma** direção. A anti-cara-de-ia é a revisão final, não o ponto de partida.

Cuidado com a "nova cara de IA" (2026): título enorme em serifa itálica sobre fundo creme ou preto, para parecer caro. Isso também virou padrão. A saída é o conteúdo e a marca do cliente, não outro clichê.

Teste do detector: `node ~/.claude/skills/anti-cara-de-ia/scripts/detectar.mjs --teste`
