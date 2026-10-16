#!/bin/sh
# Instala o kit no Claude Code (Mac/Linux).
# Uso:
#   sh install.sh                        # tudo em ~/.claude
#   sh install.sh --skill site-fortress  # só uma skill
#   sh install.sh --dest /tmp/teste      # outra pasta (para testar)
#   sh install.sh --force                # sobrescreve o que já existe
set -e
KIT=$(cd "$(dirname "$0")" && pwd)
DEST="$HOME/.claude"; SKILL=""; FORCE=0; NOAGENTS=0
while [ $# -gt 0 ]; do
  case "$1" in
    --dest) DEST="$2"; shift ;;
    --skill) SKILL="$2"; shift ;;
    --force) FORCE=1 ;;
    --no-agents) NOAGENTS=1 ;;
    *) echo "Opção desconhecida: $1"; exit 1 ;;
  esac
  shift
done
mkdir -p "$DEST/skills"
new=0; skip=0; found=0
for s in "$KIT"/skills/*/*/; do
  name=$(basename "$s")
  [ -n "$SKILL" ] && [ "$name" != "$SKILL" ] && continue
  found=1
  if [ -e "$DEST/skills/$name" ] && [ $FORCE -eq 0 ]; then skip=$((skip+1)); continue; fi
  rm -rf "$DEST/skills/$name"
  cp -R "$s" "$DEST/skills/$name"
  new=$((new+1))
done
if [ -n "$SKILL" ] && [ $found -eq 0 ]; then echo "Skill '$SKILL' não encontrada no kit."; exit 1; fi
echo "Skills: $new instaladas, $skip já existiam em $DEST/skills"

if [ -z "$SKILL" ] && [ $NOAGENTS -eq 0 ]; then
  mkdir -p "$DEST/agents"
  an=0; ap=0
  for a in "$KIT"/agents/*.md; do
    if [ -e "$DEST/agents/$(basename "$a")" ] && [ $FORCE -eq 0 ]; then ap=$((ap+1)); continue; fi
    cp "$a" "$DEST/agents/"; an=$((an+1))
  done
  echo "Agentes: $an instalados, $ap já existiam em $DEST/agents"
  echo
  echo "Plugins: cole no Claude Code:"
  echo "  /plugin marketplace add anthropics/claude-plugins-official"
  grep -oE '"[a-z0-9-]+@claude-plugins-official"' "$KIT/plugins/plugins.json" | tr -d '"' | sort -u | sed 's/^/  \/plugin install /'
  echo
  echo "CLAUDE.md e mcp/.mcp.json não foram copiados: veja o README e copie o que quiser."
fi
echo "Pronto. Abra uma conversa nova no Claude Code para carregar."
