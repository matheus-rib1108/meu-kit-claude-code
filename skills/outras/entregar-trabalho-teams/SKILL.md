---
name: entregar-trabalho-teams
description: Entrega trabalhos e tarefas da escola/SENAI no Microsoft Teams (aba Tarefas) no nome do usuário, pelo Claude in Chrome — acha a tarefa, anexa o arquivo, mostra tudo e só clica em "Entregar" depois do ok. Use quando o usuário disser "entrega meu trabalho no Teams", "manda essa tarefa no Teams", "posta o trabalho na tarefa X", "não consigo entregar no Teams", ou mandar um arquivo dizendo que é para uma tarefa.
---

# Entregar trabalho no Microsoft Teams

O usuário já está logado no Teams no Chrome dele. Você só navega, anexa e, **depois do "pode entregar"**, clica em Entregar.

## Regras
- Nunca digite senha, código de verificação nem faça login. Se aparecer tela de login, pare e peça para ele logar.
- Nunca clique em **Entregar / Turn in** sem ele responder "pode entregar", "aprovo" ou "entrega" **depois** de ver o print com a tarefa e o arquivo anexado.
- Não escreva em chat, post de equipe nem mande mensagem para professor. Comentário na entrega só se ele ditar o texto.
- Só anexe arquivos que ele indicou. Não abra nem baixe trabalho de colega.

## Passo a passo
1. **Pergunte só o que faltar:** qual arquivo (caminho) e qual tarefa/matéria. Se ele mandou o arquivo no chat sem caminho, procure em Downloads/Documentos/Área de Trabalho pelo nome.
   Confira o arquivo antes: abre? é o certo? (nome, tamanho, 1ª página se for PDF/DOCX). Se for trabalho escolar sem formatar, ofereça `formatador-abnt` antes.
2. **Abra o Teams:** Claude in Chrome (carregue de uma vez `tabs_context_mcp, tabs_create_mcp, navigate, computer, find, read_page, file_upload, javascript_tool, tabs_close_mcp`), aba nova em `https://teams.microsoft.com/v2/`. Confira que está logado (aparece a barra lateral com "Tarefas"/"Assignments").
3. **Ache a tarefa:** barra lateral → **Tarefas** (ou: Equipes → turma → aba **Tarefas**). Use `find`/`read_page` para achar pelo nome da tarefa. Se houver várias parecidas, mostre a lista com prazo e pergunte qual.
4. **Anexe:** dentro da tarefa → **+ Adicionar trabalho** (Add work) → **Carregar deste dispositivo** (Upload from this device). Use `file_upload` no `input[type=file]`.
   - O app de Tarefas roda num iframe (`assignments.onenote.com`). Se o `find` não achar o input, use `read_page` focado no iframe ou `javascript_tool` só para localizar o elemento.
   - Se o upload direto falhar: opção **OneDrive** no mesmo menu (ele envia o arquivo para o OneDrive dele antes) — explique e peça para ele arrastar o arquivo, se nada funcionar.
5. **Mostre e espere:** tire print mostrando nome da tarefa, prazo, arquivo anexado e o botão Entregar. Diga: "Tarefa X, arquivo Y anexado. Posso clicar em Entregar?" e **pare**.
6. **Entregue:** só após o ok, clique **Entregar** (Turn in). Confirme que o status virou "Entregue"/"Turned in" (ou "Entregue com atraso") e mande o print final.
7. Feche a aba. Responda: tarefa, arquivo, horário da entrega.

## Problemas comuns
- **Botão Entregar cinza:** tarefa fechada ou sem arquivo anexado; veja a data limite e avise.
- **"Desfazer entrega" aparece:** já foi entregue antes. Para trocar o arquivo, ele precisa autorizar "Desfazer entrega", trocar e entregar de novo.
- **Arquivo grande demais / formato bloqueado:** converta para PDF (skill `pdf`) ou compacte, com o ok dele.
- **Pede para abrir no app do Teams:** clique em "Usar o aplicativo Web".
