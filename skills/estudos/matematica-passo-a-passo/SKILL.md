---
name: matematica-passo-a-passo
description: Resolve e explica exercícios de matemática do ensino médio/técnico (Pitágoras, trigonometria seno/cosseno/tangente, porcentagem, função, equação, geometria, estatística) passo a passo, com desenho da figura e checagem da conta. Use quando o usuário mandar foto ou texto de exercício de matemática, pedir "resolve", "explica", "por que eleva ao quadrado", ou tiver prova/lista de exercícios.
---

# Matemática passo a passo

## Para cada questão
1. **Desenhe primeiro** quando houver figura implícita (triângulo, escada na parede, avião subindo, sombra de prédio): SVG/diagrama com os valores dados e o "x" marcado.
2. **Identifique o que é o quê**: catetos × hipotenusa; cateto oposto × adjacente ao ângulo; dado × pedido. Escreva isso antes de calcular.
3. **Escolha a ferramenta e diga por quê**: dois lados → Pitágoras; ângulo + lado → seno/cos/tan (SOH-CAH-TOA, ou "SOH CAH TOA" em PT: seno = oposto/hipotenusa…).
4. **Conta linha a linha**, uma operação por linha. Use valores da tabela dos ângulos notáveis (30°, 45°, 60°) ou os que o enunciado der (ex.: sen 15° ≈ 0,26).
5. **Confira**: rode a conta em código quando possível (skill `sympy` para equação, fração e raiz exatas); teste se o resultado faz sentido (hipotenusa é o maior lado; altura não pode ser negativa).
6. **Resposta final em destaque** com unidade. Se for múltipla escolha, diga a letra e por que as outras não servem quando houver pegadinha.

## Quando o aluno pergunta "por quê"
Explique o conceito com imagem mental antes da fórmula (ex.: Pitágoras = áreas dos quadrados nos lados, 9 + 16 = 25). Depois mostre a fórmula como consequência.

## Regras
- Nunca pule passo "óbvio" para quem está aprendendo.
- Se a foto estiver ilegível, diga qual número não deu para ler em vez de chutar.
- Para listas grandes, numere igual à lista do aluno.
