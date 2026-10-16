---
name: comparador-produtos-br
description: Compara produtos à venda em lojas brasileiras (Pichau, Kabum, Terabyte, Amazon BR, Mercado Livre, Magalu) — cadeiras, periféricos, peças de PC, celulares — com tabela por critério, ranking top 3/top 5 e link direto da melhor opção. Use quando o usuário pedir "qual é melhor", comparar modelos, achar o melhor custo-benefício, ou mandar print/lista de produtos de uma loja.
---

# Comparador de produtos (lojas BR)

## 1. Critérios antes de pesquisar
Defina os critérios que importam para a categoria e diga ao usuário quais são. Exemplos:
- **Cadeira**: apoio lombar (ajustável/automático), profundidade do assento, altura do encosto, apoio de braço (2D/3D/4D/6D), peso suportado, pistão classe 4, reclinação, material (mesh/couro sintético), garantia.
- **Headset/mouse/teclado**: conexão, latência, peso, switches/sensor, conforto, software, garantia.
- **Peças de PC**: desempenho em benchmarks reais, consumo, compatibilidade (soquete, fonte, gabinete), garantia.
- **Celular**: processador, câmera, bateria, atualizações garantidas, tela.

## 2. Coleta (dados verificados)
- Abra a **página do produto na loja** para preço à vista/PIX, parcelado, estoque, garantia e especificação. Snippet de busca não conta como preço confirmado.
- Complemente com ficha do fabricante e 1–2 reviews independentes.
- Anote o **link exato** de cada produto. Antes de entregar um link, confira que ele leva ao modelo certo (erro comum: link de variante/cor diferente).
- Ignore produtos indisponíveis, mas liste-os numa linha no fim.

## 3. Entrega
1. **Veredito em 1–2 frases** (qual comprar e por quê).
2. **Tabela**: produto × critérios, com ✔/✘ ou valor; marque o vencedor de cada critério.
3. **Top 3 (ou 5)** com: preço PIX, ponto forte, ponto fraco, link.
4. **Alertas**: preço subiu, poucas avaliações, link a confirmar.

## Regras
- Preço muda: escreva "preço consultado em <data>".
- Não invente especificação. Se a loja não informa, escreva "não informado".
- Considere o uso do usuário (horas sentado, jogos, estudo) acima de "mais caro = melhor".
