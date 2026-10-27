---
name: musica-ia
description: Cria músicas com IA (Suno, Udio e parecidos) — escreve a letra em português ou inglês com métrica e rima, monta o prompt de estilo (gênero, BPM, instrumentos, voz) e a estrutura com tags [Verse] [Chorus], para jingle de negócio, trilha de Reels, música de aniversário, trabalho escolar ou projeto pessoal. Use quando o usuário pedir música, letra, jingle, paródia, trilha, beat, "faz uma música sobre…", ou mencionar Suno/Udio.
---

# Música com IA

Entregue o texto pronto para o usuário colar no site/app (no Suno, modo **Custom**: campo de letra + campo de estilo). Não gere a música por API de terceiros não oficial.

## Antes de escrever
Pergunte o que mudar o resultado: para quê (jingle, Reels, presente, escola), gênero, clima, duração, idioma, voz (masculina/feminina/dupla) e palavras obrigatórias (nome da loja, telefone, nome do aniversariante).

## Entrega (sempre neste formato)
**Estilo** (até ~200 caracteres, em inglês, que a IA entende melhor):
`brazilian funk, 130 bpm, punchy 808, catchy female vocals, upbeat, radio jingle`

**Letra** com tags de estrutura (música completa; para jingle curto use só `[Chorus]` + um `[Verse]`, veja abaixo):
```
[Intro]
[Verse 1]
…
[Chorus]
…
[Verse 2]
[Chorus]
[Bridge]
[Outro]
```

## Como escrever a letra
- Refrão curto (2–4 linhas), fácil de cantar, com o nome/mensagem principal. Repita o refrão.
- Versos com número de sílabas parecido entre linhas do mesmo bloco — a IA canta melhor.
- Rimas simples no fim das linhas; evite palavras difíceis de pronunciar.
- Jingle: nome da marca no refrão e no fim; até 30 s → só [Chorus] e um verso.
- Números, siglas e nomes estrangeiros: escreva como se fala ("vinte e quatro horas", "Dí-Jei") para a IA não errar.

## Regras
- **Não copie letra existente** nem use nome de artista real no estilo (o Suno bloqueia e é violação de direito autoral). Descreva o som: "anos 2000, pagode romântico, cavaquinho".
- Paródia de música famosa: só a ideia/ritmo, com letra 100% nova, e avise que publicar paródia comercialmente pode ter restrição.
- **Uso comercial** (jingle de cliente, propaganda): no Suno, só músicas geradas em plano pago têm direito de uso comercial — avise o usuário e mande conferir os termos atuais.
- Ofereça 2 versões de estilo diferentes para ele gerar e escolher.

Para pôr a música num vídeo: `video-maker` ou `ffmpeg-skill` (música de fundo com volume abaixando na fala).
