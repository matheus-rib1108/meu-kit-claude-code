---
name: assistente-voz-jarvis
description: Guia para construir um assistente pessoal de IA estilo JARVIS em Python — palavra de ativação (hotword), gravação, transcrição (Whisper), resposta com a API do Claude, voz (TTS), comandos no PC e extensão de navegador — em etapas testáveis. Use quando o usuário falar do projeto JARVIS, assistente de voz, hotword, Porcupine, Whisper, TTS, ou quiser que o assistente faça ações no computador.
---

# Assistente de voz pessoal (projeto JARVIS)

## Arquitetura (montar nesta ordem, testando cada etapa)
1. **Ambiente**: Python 3.10+, `venv`, `.env` com chaves (`ANTHROPIC_API_KEY` etc.). Nunca commitar `.env` (pôr no `.gitignore`).
2. **Texto primeiro**: loop de chat no terminal chamando a API do Claude com histórico. Só avance quando funcionar.
3. **Voz → texto**: gravar com `sounddevice`, transcrever (Whisper local `faster-whisper` ou API). Testar com frase fixa.
4. **Texto → voz**: TTS (`pyttsx3` offline, ou Edge-TTS/ElevenLabs online). Voz em pt-BR.
5. **Hotword**: Porcupine (chave Picovoice) ou openWakeWord (grátis, sem chave). Palavra personalizada.
6. **Ferramentas (tool use)**: dar ao modelo funções controladas — abrir programa, pesquisar na web, lembrete, clima. Cada ação perigosa (apagar, enviar mensagem, comprar) pede confirmação falada.
7. **Memória**: arquivo JSON/SQLite com fatos do usuário, lido no início de cada conversa.
8. **Extensão de navegador** (opcional): Manifest V3, conversa com o backend local via `localhost`.

## Regras do projeto
- Explicar cada etapa para iniciante e dizer qual SO (Windows/Linux) muda o comando.
- Código em arquivos separados por módulo (`audio.py`, `cerebro.py`, `voz.py`, `ferramentas.py`).
- Custos: avisar quais serviços são pagos e oferecer alternativa grátis/local.
- Nome: "JARVIS" é marca da Marvel/Disney — para publicar, sugerir nome próprio; para uso pessoal tudo bem.
