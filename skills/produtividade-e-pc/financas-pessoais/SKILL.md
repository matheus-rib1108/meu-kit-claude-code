---
name: financas-pessoais
description: Organiza o dinheiro de um jovem brasileiro ou freelancer iniciante — controle de gastos e ganhos (planilha Excel/Google Sheets), orçamento do mês, metas de compra (PC, celular, curso), reserva de emergência, quanto cobrar e separar dos trabalhos, Pix e cartão sem cair em juros, e o básico de MEI. Explica investimentos de forma educativa, sem recomendar produto. Use quando o usuário falar em dinheiro, gastos, mesada, salário de Jovem Aprendiz, economizar, juntar para comprar algo, planilha de controle, dívida, cartão, Pix, MEI ou nota fiscal.
---

# Finanças pessoais

## Começo
Pergunte: quanto entra por mês (mesada, Jovem Aprendiz, freelas — valor médio se variar), gastos fixos, e qual a meta (ex.: PC de R$ 4.000). Trabalhe com os números dele, nunca com exemplo genérico.

## Planilha de controle
Gere com a skill `anthropic-skills:xlsx` uma planilha simples: aba **Lançamentos** (data | descrição | categoria | entrada | saída), aba **Resumo** com fórmulas (total por categoria, saldo do mês) e aba **Metas** (meta | valor | já guardado | falta | meses até chegar). Categorias curtas: Comida, Transporte, Lazer, Jogos/Assinaturas, Estudos, Trabalho, Guardar.

## Regras que valem mais que qualquer dica
- **Guarde primeiro, gaste depois**: separe a parte da meta no dia que o dinheiro entra.
- Divisão de partida (ajuste à realidade): 50% necessidades, 30% desejos, 20% guardar. Para quem mora com os pais e tem meta de compra, inverta: calcule **quanto precisa guardar por mês** (meta ÷ meses) e mostre 2 ou 3 cenários (ex.: R$ 300/mês = 10 meses; R$ 500/mês = 6 meses) com o que sobra para gastar em cada um.
- Enquanto junta para a meta, o dinheiro deve ficar separado da conta do dia a dia, em algo com **liquidez diária e sem risco de perder valor** (explique a ideia; não indique banco ou produto específico).
- **Reserva de emergência** antes de investir em risco: 3 a 6 meses dos gastos.
- **Rotativo do cartão e cheque especial** têm os juros mais altos do mercado — se não puder pagar a fatura inteira, avise e monte um plano para quitar.
- Parcelado "sem juros" ainda compromete os meses seguintes: some as parcelas abertas antes de fazer outra.
- Golpes de Pix: ninguém legítimo pede Pix para "liberar prêmio", "desbloquear conta" ou "taxa de entrega" por mensagem.

## Freelancer / MEI
- Separe o dinheiro do trabalho do pessoal (outra conta ou ao menos outra planilha).
- De cada trabalho, reserve uma parte para impostos e ferramentas antes de gastar.
- MEI exige **18 anos** (ou 16 emancipado). Valor do DAS mensal e limite de faturamento mudam todo ano: confira no Portal do Empreendedor (gov.br/mei) em vez de usar número de memória.
- Para orçar o serviço, use a skill `orcamento-servicos`.

## Investimentos (só educativo)
Explique como funcionam (Tesouro Selic, CDB com garantia do FGC, poupança, ações, cripto), riscos, liquidez e imposto, em linguagem simples. **Não recomende** produto, corretora ou quanto aplicar em cada um: diga que é educação financeira, não aconselhamento, e que menor de idade investe com o responsável.
