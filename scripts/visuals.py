"""Gera as imagens do README (claro e escuro) com os números reais do kit.

- assets/banner-{dark,light}.svg  — topo "manual técnico" (direção A)
- assets/painel-{dark,light}.svg  — painel ao vivo: totais, skills por área, última mudança (direção C)

Chamado pelo build_kit.py a cada montagem; os números nunca ficam desatualizados.
"""
import os
from xml.sax.saxutils import escape

TEMAS = {
    'dark': {'paper': '#14161a', 'paper2': '#1c1f24', 'ink': '#e8e6e1', 'muted': '#8a8f98', 'rule': '#2c3038',
             'accent': '#e8a33d', 'bar': '#e8a33d', 'bar2': '#8a6a3a'},
    'light': {'paper': '#f6f5f2', 'paper2': '#ebe9e4', 'ink': '#14161a', 'muted': '#5b6070', 'rule': '#d6d3cc',
              'accent': '#b45309', 'bar': '#b45309', 'bar2': '#d9a876'},
}
MONO = "'JetBrains Mono','Cascadia Code',Consolas,'DejaVu Sans Mono',monospace"
SANS = "'Inter Tight','Segoe UI','Helvetica Neue',Arial,sans-serif"


def banner(t, n):
    c = TEMAS[t]
    linhas = [('skills', n['skills'], c['accent']), ('agentes', n['agentes'], c['ink']),
              ('plugins', n['plugins'], c['ink']), ('conectores MCP', n['mcp'], c['ink'])]
    inv = []
    for i, (nome, val, cor) in enumerate(linhas):
        y = 178 + 54 * i
        inv.append(f'<text x="840" y="{y}" font-family="{MONO}" font-size="15" fill="{c["ink"]}">{nome}</text>'
                   f'<text x="1200" y="{y}" text-anchor="end" font-family="{MONO}" font-size="28" font-weight="700" fill="{cor}">{val}</text>')
        if i < 3:
            inv.append(f'<line x1="840" y1="{y + 16}" x2="1200" y2="{y + 16}" stroke="{c["rule"]}"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 440" width="1280" height="440" role="img" aria-label="Meu kit do Claude Code: {n["skills"]} skills, {n["agentes"]} agentes, {n["plugins"]} plugins, {n["mcp"]} conectores MCP">
<rect width="1280" height="440" fill="{c["paper"]}"/>
<text x="64" y="76" font-family="{MONO}" font-size="15" fill="{c["muted"]}">matheus-rib1108 / meu-kit-claude-code</text>
<text x="64" y="150" font-family="{SANS}" font-size="46" font-weight="700" fill="{c["ink"]}">O Claude Code que eu uso,</text>
<text x="64" y="204" font-family="{SANS}" font-size="46" font-weight="700" fill="{c["ink"]}">inteiro. <tspan fill="{c["accent"]}">Instale em 1 comando.</tspan></text>
<text x="64" y="262" font-family="{SANS}" font-size="19" fill="{c["muted"]}">Skills, agentes, plugins e conectores em português, com a tabela "pedido → quem faz".</text>
<rect x="64" y="300" width="640" height="52" fill="{c["paper2"]}" stroke="{c["rule"]}"/>
<text x="84" y="333" font-family="{MONO}" font-size="16" fill="{c["accent"]}">&gt;</text>
<text x="104" y="333" font-family="{MONO}" font-size="16" fill="{c["ink"]}">git clone …/meu-kit-claude-code; .\\install.ps1</text>
<text x="64" y="396" font-family="{MONO}" font-size="13" fill="{c["muted"]}">atualiza sozinho ~2 min depois de cada mudança · gitleaks + checagem de dados pessoais</text>
<line x1="800" y1="96" x2="800" y2="376" stroke="{c["rule"]}"/>
<text x="840" y="128" font-family="{MONO}" font-size="15" fill="{c["muted"]}">INVENTÁRIO</text>
{"".join(inv)}
</svg>
'''


def painel(t, n, areas, data, ultima):
    c = TEMAS[t]
    maxv = max([v for _, v in areas] or [1])
    barras = []
    for i, (nome, v) in enumerate(areas[:9]):
        y = 118 + 32 * i
        w = round(230 * v / maxv)
        cor = c['bar'] if i < 7 else c['bar2']
        barras.append(f'<text x="740" y="{y}" font-family="{SANS}" font-size="15" fill="{c["ink"]}">{escape(nome)}</text>'
                      f'<rect x="950" y="{y - 14}" width="{w}" height="18" fill="{cor}"/>'
                      f'<text x="{950 + w + 8}" y="{y}" font-family="{MONO}" font-size="14" fill="{c["ink"]}">{v}</text>')
    tot = [('SKILLS', n['skills']), ('AGENTES', n['agentes']), ('PLUGINS', n['plugins']), ('MCP', n['mcp'])]
    tops = ''.join(f'<text x="{64 + 170 * i}" y="70" font-family="{MONO}" font-size="13" fill="{c["muted"]}">{k}</text>'
                   f'<text x="{64 + 170 * i}" y="126" font-family="{SANS}" font-size="52" font-weight="700" fill="{c["ink"]}">{v}</text>'
                   for i, (k, v) in enumerate(tot))
    ult = escape(ultima[:46] + ('…' if len(ultima) > 46 else ''))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 440" width="1280" height="440" role="img" aria-label="Painel do kit: skills por área e última atualização {escape(data)}">
<rect width="1280" height="440" fill="{c["paper"]}"/>
{tops}
<text x="64" y="206" font-family="{MONO}" font-size="13" fill="{c["muted"]}">ÚLTIMA ATUALIZAÇÃO</text>
<text x="64" y="240" font-family="{SANS}" font-size="24" font-weight="700" fill="{c["ink"]}">{escape(data)}</text>
<text x="64" y="272" font-family="{SANS}" font-size="18" fill="{c["muted"]}">{ult}</text>
<text x="64" y="330" font-family="{MONO}" font-size="13" fill="{c["muted"]}">PAINEL GERADO SOZINHO A CADA PUBLICAÇÃO</text>
<text x="64" y="356" font-family="{MONO}" font-size="13" fill="{c["accent"]}">CHANGELOG.md → o que entrou, mudou e saiu</text>
<line x1="700" y1="50" x2="700" y2="390" stroke="{c["rule"]}"/>
<text x="740" y="76" font-family="{MONO}" font-size="13" fill="{c["muted"]}">SKILLS POR ÁREA</text>
{"".join(barras)}
</svg>
'''


# (chave da área, rótulo, pedido de exemplo, skill que atende)
EXEMPLOS = [
    ('sites-e-design', 'Sites e design', 'Faz um site para uma barbearia que não pareça feito por IA', 'hallmark'),
    ('marketing-e-vendas', 'Marketing e vendas', 'Escreve a primeira mensagem de WhatsApp para oferecer um cardápio digital', 'abordagem-whatsapp-vendas'),
    ('seguranca-e-lei', 'Segurança e lei', 'Deixa meu site seguro antes de publicar', 'site-fortress'),
    ('publicar-e-banco', 'Publicar e banco', 'Quanto custa colocar esse site no ar?', 'cost-estimator'),
    ('video-foto-e-musica', 'Vídeo, foto e música', 'Faz um Reels de 15 segundos com essas fotos', 'video-maker'),
    ('estudos', 'Estudos', 'Corrige minha redação do ENEM', 'redacao-enem'),
    ('produtividade-e-pc', 'Produtividade e PC', 'Salva essa página no meu Obsidian', 'defuddle'),
    ('metodo-de-trabalho', 'Método de trabalho', 'Acha a causa desse bug antes de mexer', 'systematic-debugging'),
]


def quebra(txt, maxc=46):
    linhas, atual = [], ''
    for p in txt.split():
        if len(atual) + len(p) + 1 > maxc and atual:
            linhas.append(atual)
            atual = p
        else:
            atual = f'{atual} {p}'.strip()
    return linhas + [atual]


def areas_svg(t, por_area):
    c = TEMAS[t]
    partes = []
    for i, (chave, rotulo, pedido, skill) in enumerate(EXEMPLOS):
        col, lin = i % 2, i // 2
        x, y = 64 + 608 * col, 140 + 150 * lin
        qtd = por_area.get(chave, 0)
        partes.append(f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="22" font-weight="700" fill="{c["ink"]}">{escape(rotulo)}</text>'
                      f'<text x="{x + 544}" y="{y}" text-anchor="end" font-family="{MONO}" font-size="14" fill="{c["muted"]}">{qtd} skills</text>')
        for j, l in enumerate(quebra(f'“{pedido}”')):
            partes.append(f'<text x="{x}" y="{y + 32 + 24 * j}" font-family="{SANS}" font-size="17" fill="{c["ink"]}">{escape(l)}</text>')
        partes.append(f'<text x="{x}" y="{y + 98}" font-family="{MONO}" font-size="15" fill="{c["accent"]}">→ {escape(skill)}</text>')
        if lin < 3:
            partes.append(f'<line x1="{x}" y1="{y + 120}" x2="{x + 544}" y2="{y + 120}" stroke="{c["rule"]}"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 760" width="1280" height="760" role="img" aria-label="O que dá para pedir: um exemplo de pedido e a skill que atende, em 8 áreas">
<rect width="1280" height="760" fill="{c["paper"]}"/>
<text x="64" y="72" font-family="{MONO}" font-size="14" fill="{c["muted"]}">O QUE DÁ PARA PEDIR · um exemplo por área e a skill que entra em ação</text>
<line x1="640" y1="110" x2="640" y2="720" stroke="{c["rule"]}"/>
{"".join(partes)}
</svg>
'''


def write_visuals(repo, n, areas, data, ultima, por_area=None):
    out = os.path.join(repo, 'assets')
    os.makedirs(out, exist_ok=True)
    for t in TEMAS:
        arquivos = [(f'banner-{t}.svg', banner(t, n)), (f'painel-{t}.svg', painel(t, n, areas, data, ultima))]
        if por_area is not None:
            arquivos.append((f'areas-{t}.svg', areas_svg(t, por_area)))
        for nome, svg in arquivos:
            path = os.path.join(out, nome)
            old = open(path, encoding='utf-8').read() if os.path.exists(path) else None
            if old != svg:
                open(path, 'w', encoding='utf-8', newline='\n').write(svg)
