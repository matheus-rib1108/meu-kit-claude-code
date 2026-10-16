"""Monta o kit a partir das pastas do Claude Code deste PC.

Copia skills, agentes, lista de plugins, .mcp.json (sem chaves) e CLAUDE.md
para o repositório e refaz o README. Não faz commit: isso é com o sync-kit.ps1.

Uso: python scripts/build_kit.py
"""
import datetime
import json
import os
import re
import shutil
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = os.path.expanduser('~')
CLAUDE = os.path.join(HOME, '.claude')
# Pastas extras de skills de projetos (só entram as que não existem em ~/.claude/skills)
EXTRA_SKILL_DIRS = [os.path.join(HOME, 'repos', 'dev-journey', '.claude', 'skills')]
MCP_SOURCES = [os.path.join(HOME, 'repos', 'dev-journey', '.mcp.json'), os.path.join(HOME, '.mcp.json')]
MCP_BIN = os.path.join(HOME, 'repos', 'dev-journey', '.claude', 'bin')
OWNER = 'matheus-rib1108'
REPO_NAME = 'meu-kit-claude-code'

# Nunca copiar (nomes de arquivo/pasta)
EXCLUDE_NAMES = {'.git', '.remember', 'node_modules', '__pycache__', 'settings.local.json',
                 'chat-exports', 'instagram-export', '.DS_Store', 'Thumbs.db'}
EXCLUDE_EXT = ('.zip', '.log', '.pyc', '.exe', '.dll', '.env')
PERMISSIVE = ('MIT', 'Apache', 'BSD', 'CC-BY-SA', 'ISC', 'MPL', 'Unlicense', 'CC0')
SECRET_KEYS = re.compile(r'(?i)(token|key|secret|password|passwd|auth|bearer|cookie)')


def ignore(_dir, names):
    return [n for n in names if n in EXCLUDE_NAMES or n.lower().endswith(EXCLUDE_EXT)
            or n.lower().startswith('.env')]


def frontmatter_description(path):
    try:
        txt = open(path, encoding='utf-8', errors='replace').read(4000)
    except OSError:
        return ''
    m = re.search(r'^description:\s*(.+)$', txt, re.M)
    if not m:
        return ''
    d = m.group(1).strip().strip('"\'')
    d = re.split(r'(?<=[.!?])\s', d)[0]
    return d[:160]


def detect_license(folder):
    for f in os.listdir(folder):
        if f.upper().startswith(('LICENSE', 'LICENCE', 'COPYING')):
            head = open(os.path.join(folder, f), encoding='utf-8', errors='replace').read(1500)
            for tag, name in (('MIT License', 'MIT'), ('Apache License', 'Apache-2.0'), ('BSD', 'BSD'),
                              ('Attribution-ShareAlike', 'CC-BY-SA-4.0'), ('ISC License', 'ISC')):
                if tag in head:
                    return name
            return 'desconhecida'
    return None


def skill_lock_sources():
    p = os.path.join(HOME, '.agents', '.skill-lock.json')
    try:
        d = json.load(open(p, encoding='utf-8'))
        s = d.get('skills', d)
        return {k: v.get('source') for k, v in s.items() if isinstance(v, dict)}
    except (OSError, ValueError):
        return {}


def license_file_for(source):
    p = os.path.join(REPO, 'licenses', source.replace('/', '_') + '.txt')
    return p if os.path.exists(p) else None


def collect_skills():
    found = {}
    base = os.path.join(CLAUDE, 'skills')
    for d in [base] + EXTRA_SKILL_DIRS:
        if not os.path.isdir(d):
            continue
        for n in sorted(os.listdir(d)):
            p = os.path.join(d, n)
            if n not in found and os.path.isfile(os.path.join(p, 'SKILL.md')):
                found[n] = p
    return found


def main():
    meta_path = os.path.join(REPO, 'kit-meta.json')
    meta = json.load(open(meta_path, encoding='utf-8'))
    lock = skill_lock_sources()
    notes = []

    # ---------- skills ----------
    skills = collect_skills()
    # Registros automáticos (área "outras") de skills que foram apagadas saem do meta
    for n in [n for n, m in meta['skills'].items() if n not in skills and m['area'] == 'outras']:
        del meta['skills'][n]
    for n, p in skills.items():
        if n in meta['skills']:
            continue
        lic = detect_license(p)
        src = lock.get(n)
        if src and not (lic and lic.startswith(PERMISSIVE)):
            entry = {'fonte': src, 'licenca': lic or 'sem licença', 'modo': 'link'}
        elif src:
            entry = {'fonte': src, 'licenca': lic, 'modo': 'copia'}
        elif lic and lic != 'MIT':
            entry = {'fonte': 'terceiro (origem desconhecida)', 'licenca': lic,
                     'modo': 'copia' if lic.startswith(PERMISSIVE) else 'link'}
        else:
            entry = {'fonte': 'própria', 'licenca': 'MIT', 'modo': 'copia'}
        entry.update({'area': 'outras', 'descricao': frontmatter_description(os.path.join(p, 'SKILL.md'))})
        meta['skills'][n] = entry
        notes.append(f'nova skill classificada automaticamente: {n} ({entry["fonte"]}, {entry["modo"]})')

    out_skills = os.path.join(REPO, 'skills')
    shutil.rmtree(out_skills, ignore_errors=True)
    for n, p in skills.items():
        m = meta['skills'][n]
        if m['modo'] != 'copia':
            continue
        dst = os.path.join(out_skills, m['area'], n)
        shutil.copytree(p, dst, ignore=ignore)
        if m['fonte'] != 'própria':
            if not detect_license(dst):
                lf = license_file_for(m['fonte'])
                if lf:
                    shutil.copy(lf, os.path.join(dst, 'LICENSE'))
                else:
                    notes.append(f'AVISO: {n} sem arquivo de licença')
            with open(os.path.join(dst, 'FONTE.md'), 'w', encoding='utf-8') as f:
                f.write(f'# Fonte\n\nSkill de terceiros, copiada sem alterações de '
                        f'<https://github.com/{m["fonte"]}>.\n\nAutor: {m["fonte"].split("/")[0]} · '
                        f'Licença: {m["licenca"]} (texto em `LICENSE` nesta pasta).\n')

    # ---------- agentes ----------
    out_agents = os.path.join(REPO, 'agents')
    shutil.rmtree(out_agents, ignore_errors=True)
    os.makedirs(out_agents)
    agents = {}
    adir = os.path.join(CLAUDE, 'agents')
    for f in sorted(os.listdir(adir)) if os.path.isdir(adir) else []:
        if f.endswith('.md'):
            n = f[:-3]
            agents[n] = os.path.join(adir, f)
            if n not in meta['agentes']:
                meta['agentes'][n] = {'area': 'outros', 'fonte': 'própria', 'licenca': 'MIT', 'modo': 'copia',
                                      'descricao': frontmatter_description(agents[n])}
                notes.append(f'novo agente: {n}')
            shutil.copy(agents[n], os.path.join(out_agents, f))
    shutil.copy(os.path.join(REPO, 'licenses', 'VoltAgent_awesome-claude-code-subagents.txt'),
                os.path.join(out_agents, 'LICENSE-VoltAgent'))

    # ---------- plugins ----------
    settings = json.load(open(os.path.join(CLAUDE, 'settings.json'), encoding='utf-8'))
    enabled = settings.get('enabledPlugins', {})
    os.makedirs(os.path.join(REPO, 'plugins'), exist_ok=True)
    json.dump({'enabledPlugins': enabled, 'extraKnownMarketplaces': settings.get('extraKnownMarketplaces', {})},
              open(os.path.join(REPO, 'plugins', 'plugins.json'), 'w', encoding='utf-8'), indent=2)

    # ---------- MCP (sem chaves) ----------
    os.makedirs(os.path.join(REPO, 'mcp'), exist_ok=True)
    servers = {}
    for src in MCP_SOURCES:
        if os.path.exists(src):
            for k, v in json.load(open(src, encoding='utf-8')).get('mcpServers', {}).items():
                v = {kk: vv for kk, vv in v.items() if kk not in ('env', 'headers')}
                v['args'] = [a for a in v.get('args', []) if not SECRET_KEYS.search(str(a))]
                if not v['args']:
                    v.pop('args')
                servers.setdefault(k, v)
    json.dump({'mcpServers': servers}, open(os.path.join(REPO, 'mcp', '.mcp.json'), 'w', encoding='utf-8'), indent=2)
    if os.path.isdir(MCP_BIN):
        shutil.copytree(MCP_BIN, os.path.join(REPO, 'mcp', 'bin'), dirs_exist_ok=True, ignore=ignore)

    # ---------- CLAUDE.md ----------
    shutil.copy(os.path.join(CLAUDE, 'CLAUDE.md'), os.path.join(REPO, 'CLAUDE.md'))

    json.dump(meta, open(meta_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    write_readme(meta, skills, agents, enabled, servers)
    for n in notes:
        print(n)


def write_readme(meta, skills, agents, enabled, servers):
    tmpl = open(os.path.join(REPO, 'scripts', 'README.template.md'), encoding='utf-8').read()
    today = datetime.date.today().strftime('%d/%m/%Y')

    def link(src):
        return src if '/' not in src or ' ' in src else f'[{src}](https://github.com/{src})'

    rows = []
    for area, title in meta['areas'].items():
        names = sorted(n for n in skills if meta['skills'][n]['area'] == area)
        if not names:
            continue
        rows.append(f'\n### {title} ({len(names)})\n\n| Skill | O que faz | Fonte | Licença |\n|---|---|---|---|')
        for n in names:
            m = meta['skills'][n]
            name = f'[`{n}`](skills/{area}/{n})' if m['modo'] == 'copia' else f'`{n}` (só link)'
            rows.append(f'| {name} | {m["descricao"]} | {link(m["fonte"])} | {m["licenca"]} |')
    skill_table = '\n'.join(rows)

    arows = ['| Agente | O que faz | Grupo |', '|---|---|---|']
    for n in sorted(agents, key=lambda x: (meta['agentes'][x]['area'], x)):
        m = meta['agentes'][n]
        arows.append(f'| [`{n}`](agents/{n}.md) | {m["descricao"]} | {m["area"]} |')

    prows = ['| Plugin | O que faz | Instalar |', '|---|---|---|']
    for full, on in sorted(enabled.items()):
        n = full.split('@')[0]
        desc = meta['plugins'].get(n, '')
        if not on:
            desc += ' (desligado por padrão)'
        prows.append(f'| `{n}` | {desc} | `/plugin install {full}` |')

    mrows = ['| Conector | Tipo |', '|---|---|']
    for k, v in servers.items():
        mrows.append(f'| `{k}` | {v.get("url") or "local (" + v.get("command", "") + ")"} |')

    links = [f'- `{n}` — {m["descricao"]}: <https://github.com/{m["fonte"]}> ({m["licenca"]})'
             for n, m in sorted(meta['skills'].items()) if m['modo'] == 'link' and n in skills]

    credits = {}
    for n in skills:
        m = meta['skills'][n]
        if m['fonte'] != 'própria':
            credits.setdefault((m['fonte'], m['licenca']), []).append(n)
    credits.setdefault(('VoltAgent/awesome-claude-code-subagents', 'MIT'), []).append(f'{len(agents)} agentes')
    crows = [f'- [{s}](https://github.com/{s}) · {l} — {", ".join(sorted(v))}' for (s, l), v in sorted(credits.items())]

    n_copy = sum(1 for n in skills if meta['skills'][n]['modo'] == 'copia')
    out = (tmpl.replace('{{DATA}}', today)
               .replace('{{N_SKILLS}}', str(len(skills))).replace('{{N_COPIA}}', str(n_copy))
               .replace('{{N_AGENTES}}', str(len(agents))).replace('{{N_PLUGINS}}', str(len(enabled)))
               .replace('{{TABELA_SKILLS}}', skill_table).replace('{{TABELA_AGENTES}}', '\n'.join(arows))
               .replace('{{TABELA_PLUGINS}}', '\n'.join(prows)).replace('{{TABELA_MCP}}', '\n'.join(mrows))
               .replace('{{SO_LINK}}', '\n'.join(links) or '_Nenhuma._')
               .replace('{{CREDITOS}}', '\n'.join(crows))
               .replace('{{OWNER}}', OWNER).replace('{{REPO}}', REPO_NAME))
    open(os.path.join(REPO, 'README.md'), 'w', encoding='utf-8', newline='\n').write(out)


if __name__ == '__main__':
    sys.exit(main())
