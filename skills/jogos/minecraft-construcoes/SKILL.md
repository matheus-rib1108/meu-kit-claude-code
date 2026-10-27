---
name: minecraft-construcoes
description: Ajuda com Minecraft Java modado (CurseForge, Fabric, modpacks como Cobbleverse) — Litematica e schematics, conversão de .mcstructure/.mcpack Bedrock para .litematic, comandos /fill /clone /kill sem estourar limite, conflito de teclas entre mods e onde baixar schematics grátis com segurança. Use quando o usuário falar de Minecraft, schematic, Litematica, mod, modpack, CurseForge, construção ou comando.
---

# Minecraft: construções, schematics e mods

## Diagnóstico de mods
- Peça o zip de logs do CurseForge ou a lista da pasta mods. Procure por `litematica|malilib|minihud|tweakeroo|fabric-api` em `mod-file-list.txt` e `logs/latest.log`.
- Conflitos de tecla comuns: Litematica (M) × Xaero's World Map (M). Solução: Opções → Mods → Litematica → Hotkeys.
- Jars duplicados (ex.: dois fabric-api) → remover o mais antigo.

## Converter Bedrock → Java (.mcstructure/.mcpack → .litematic)
1. `.mcpack` é zip: extrair e achar o `.mcstructure`.
2. Ler com `nbtlib.load(path, byteorder='little')`.
3. Camada `block_indices[0]` = blocos; `[1]` = água (waterlogged).
4. Renomear blocos que mudam de nome (`grass_path→dirt_path`, `stone_stairs→cobblestone_stairs`, `normal_stone_stairs→stone_stairs`) e traduzir estados (escadas: `weirdo_direction`→`facing` + `shape`; portas/alçapões: `direction`/bits; muros: conexões; folhas: `distance` por BFS a partir dos troncos).
5. Montar com `litemapy` (Schematic/Region/BlockState), salvar e **conferir a contagem de blocos** contra o original antes de entregar.

## Comandos seguros
- `/fill` tem limite de 32.768 blocos por comando: divida a área (ex.: duas metades na altura). Mostre as coordenadas de cada parte.
- Limpar itens soltos: `/kill @e[type=item,distance=..50]`.
- **Sempre** recomendar backup do mundo antes de colar estrutura grande (Editar → Fazer backup) e sair do modo "Paste Schematic in World" depois de colar.

## Onde baixar schematics
Planet Minecraft (seção de projetos, botão "Download Schematic", não "Download World"). Fugir de `.exe` e de instaladores (TeraBox etc.). Arquivos `.mcpack/.mcstructure` são Bedrock — oferecer conversão.
