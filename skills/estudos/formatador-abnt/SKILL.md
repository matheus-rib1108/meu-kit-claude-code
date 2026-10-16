---
name: formatador-abnt
description: Formata trabalhos escolares e acadêmicos nas normas ABNT (NBR 14724, 6023, 10520, 6024, 6027, 6028) — capa, folha de rosto, sumário, margens, fonte, espaçamento, citações, numeração de páginas e lista de referências — e gera o arquivo Word (.docx) pronto. Também transforma link, livro ou DOI em referência ABNT. Use quando o usuário falar em ABNT, normas, formatar trabalho, TCC, relatório técnico, referência bibliográfica, citação, "como cito esse site", ou pedir um trabalho em Word para entregar.
---

# Formatador ABNT

Gere o .docx com a skill `docx` (ou `anthropic-skills:docx`). Antes, pergunte só o que mudar o resultado: nome da escola/curso, aluno(s), professor, cidade, ano — e se a escola tem **manual próprio** (SENAI, SESI e faculdades costumam ter; o manual da escola vence a ABNT).

## Formatação (NBR 14724)
- Papel A4. Margens: **superior e esquerda 3 cm; inferior e direita 2 cm**.
- Fonte 12 no texto (a norma não fixa a família; Arial ou Times New Roman é o costume); **tamanho menor e uniforme** (10 ou 11) em citações longas, notas de rodapé, legendas e fontes de figuras/tabelas.
- Espaçamento 1,5 no texto. Espaço simples em citações longas, notas, referências, legendas e natureza do trabalho na folha de rosto.
- Recuo de 1,25 cm na primeira linha do parágrafo (uso comum).
- Páginas contadas a partir da folha de rosto, **número só a partir da Introdução**, canto superior direito.
- Títulos de seção numerados (1 INTRODUÇÃO, 1.1 Objetivo…) conforme NBR 6024; elementos sem número (SUMÁRIO, REFERÊNCIAS) centralizados.
- Ordem: capa → folha de rosto → (resumo) → sumário → introdução → desenvolvimento → conclusão → referências → (apêndices/anexos).

## Citações (NBR 10520:2023)
- Na versão de 2023, o autor entre parênteses fica **só com a inicial maiúscula**: (Silva, 2020, p. 15).
- Citação direta de até 3 linhas: no parágrafo, entre aspas, com página.
- Mais de 3 linhas: parágrafo separado, **recuo de 4 cm**, fonte menor, espaço simples, sem aspas.
- Citação indireta (paráfrase): sem aspas, página opcional.

## Referências (NBR 6023:2018)
Alinhadas à esquerda, espaço simples, separadas por uma linha em branco, em ordem alfabética. Título em **negrito**.
- Livro: SOBRENOME, Nome. **Título**: subtítulo. Edição. Cidade: Editora, ano.
- Site: AUTOR (ou NOME DA INSTITUIÇÃO). **Título da página**. Cidade, data. Disponível em: URL. Acesso em: 15 out. 2026.
- Artigo: SOBRENOME, Nome. Título do artigo. **Nome da Revista**, cidade, v. X, n. Y, p. inicial-final, ano. DOI.
- Lei: BRASIL. Lei nº 13.709, de 14 de agosto de 2018. …

Para um **DOI**, busque os dados em `https://api.crossref.org/works/<DOI>` e monte a referência; para um **site**, abra a página e pegue autor, título e data reais. Se faltar autor, a entrada é pelo título. Se faltar data, a NBR 6023:2018 pede **data aproximada entre colchetes** — [2026?], [ca. 2020], [202-] — e não "[s. d.]". Nunca invente dado.

## Antes de entregar
Confira no .docx gerado: margens, numeração começando na introdução, sumário com as páginas certas, toda citação no texto com a referência correspondente no fim (e vice-versa).
