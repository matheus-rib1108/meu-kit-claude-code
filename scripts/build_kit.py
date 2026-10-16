"""Monta o kit a partir das pastas do Claude Code deste PC.

Copia skills, agentes, comandos, lista de plugins, hooks (só o nome do evento), MCPs (sem chaves)
e CLAUDE.md para o repositório, registra no CHANGELOG.md o que entrou/mudou/saiu e refaz o README.
Não faz commit: isso é com o sync-kit.ps1.

Uso: python scripts/build_kit.py
"""
import datetime
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from urllib.parse import quote

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = os.path.expanduser('~')
CLAUDE = os.path.join(HOME, '.claude')
# Pastas extras de skills de projetos (só entram as que não existem em ~/.claude/skills)
EXTRA_SKILL_DIRS = [os.path.join(HOME, 'repos', 'dev-journey', '.claude', 'skills')]
# .mcp.json dos projetos + MCPs do usuário (~/.claude.json, só "mcpServers"; nunca env/headers)
MCP_SOURCES = ([os.path.join(HOME, 'repos', 'dev-journey', '.mcp.json'), os.path.join(HOME, '.mcp.json')]
               + sorted(glob.glob(os.path.join(HOME, 'repos', '*', '.mcp.json')))
               + sorted(glob.glob(os.path.join(HOME, 'OneDrive', '*', '*', '.mcp.json'))))
USER_CLAUDE_JSON = os.path.join(HOME, '.claude.json')
MCP_BIN = os.path.join(HOME, 'repos', 'dev-journey', '.claude', 'bin')
COMMANDS = os.path.join(CLAUDE, 'commands')
# Lista da conta claude.ai (gerada pela skill kit-sync-conta; só nomes e para que servem)
CONTA_JSON = os.path.join(CLAUDE, 'kit-sync', 'conta-claude-ai.json')
OWNER = 'matheus-rib1108'
REPO_NAME = 'meu-kit-claude-code'

# Nunca copiar (nomes de arquivo/pasta)
EXCLUDE_NAMES = {'.git', '.remember', 'node_modules', '__pycache__', 'settings.local.json',
                 'chat-exports', 'instagram-export', '.DS_Store', 'Thumbs.db', 'graphify-out'}
EXCLUDE_EXT = ('.zip', '.log', '.pyc', '.exe', '.dll', '.env')
PERMISSIVE = ('MIT', 'Apache', 'BSD', 'CC-BY-SA', 'ISC', 'MPL', 'Unlicense', 'CC0')
SECRET_KEYS = re.compile(r'(?i)(token|key|secret|password|passwd|auth|bearer|cookie)')
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
TIPOS = {'skills': 'skill', 'agentes': 'agente', 'comandos': 'comando', 'plugins': 'plugin',
         'mcp': 'MCP', 'hooks': 'hook', 'conta': 'claude.ai'}


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


def tree_hash(path):
    """Impressão digital do conteúdo (arquivo ou pasta), para saber se algo mudou."""
    h = hashlib.sha1()
    if os.path.isfile(path):
        h.update(open(path, 'rb').read())
        return h.hexdigest()[:12]
    for dp, dirs, files in os.walk(path):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDE_NAMES)
        for f in sorted(files):
            if f in EXCLUDE_NAMES or f.lower().endswith(EXCLUDE_EXT):
                continue
            fp = os.path.join(dp, f)
            h.update(os.path.relpath(fp, path).replace('\\', '/').encode())
            try:
                h.update(open(fp, 'rb').read())
            except OSError:
                pass
    return h.hexdigest()[:12]


def load_json(path, default):
    try:
        return json.load(open(path, encoding='utf-8'))
    except (OSError, ValueError):
        return default


def clean_mcp(v):
    """Só o que é seguro publicar: tipo, url sem query, comando e argumentos sem segredo."""
    out = {}
    for k in ('type', 'command', 'url'):
        if k in v:
            out[k] = str(v[k])
    if 'url' in out:
        out['url'] = out['url'].split('?')[0]
    args = [str(a) for a in v.get('args', []) if not SECRET_KEYS.search(str(a)) and not EMAIL.search(str(a))]
    if args:
        out['args'] = args
    for k in list(out):
        if isinstance(out[k], str):
            out[k] = out[k].replace(HOME, '~').replace(HOME.replace('\\', '/'), '~')
    out['args'] = [a.replace(HOME, '~').replace(HOME.replace('\\', '/'), '~') for a in out.get('args', [])]
    if not out['args']:
        out.pop('args')
    return out


def collect_mcp():
    servers = {}
    for src in MCP_SOURCES:
        for k, v in load_json(src, {}).get('mcpServers', {}).items():
            servers.setdefault(k, clean_mcp(v))
    for k, v in load_json(USER_CLAUDE_JSON, {}).get('mcpServers', {}).items():
        servers.setdefault(k, clean_mcp(v))
    return servers


def hook_summary(cmd):
    c = cmd.lower()
    if 'sync-kit' in c:
        return 'atualiza este kit no GitHub'
    if 'claude-hud' in c:
        return 'barra de status claude-hud'
    m = re.search(r'([\w.-]+\.(ps1|py|sh|js|cmd|mjs))', cmd)
    return f'roda `{m.group(1)}`' if m else 'comando local'


def collect_hooks(settings):
    hooks = {}
    for event, groups in (settings.get('hooks') or {}).items():
        descs = []
        for g in groups or []:
            for hk in g.get('hooks', []):
                descs.append(hook_summary(hk.get('command', '')))
        if descs:
            hooks[event] = ', '.join(sorted(set(descs)))
    if settings.get('statusLine'):
        hooks['statusLine'] = hook_summary(settings['statusLine'].get('command', ''))
    return hooks


def collect_conta():
    """Lê a lista da conta claude.ai e devolve só nome + descrição (sem e-mail nem dados)."""
    d = load_json(CONTA_JSON, None)
    if not d:
        return None
    out = {'atualizado': str(d.get('atualizado', ''))[:10]}
    for tipo in ('skills', 'conectores', 'plugins'):
        itens = []
        for it in d.get(tipo, []):
            nome = str(it.get('nome', '')).strip()[:80]
            desc = str(it.get('descricao', '')).strip()[:160]
            if nome and not EMAIL.search(nome + desc):
                itens.append({'nome': nome, 'descricao': desc})
        out[tipo] = sorted(itens, key=lambda x: x['nome'].lower())
    return out


def published_paths():
    """Arquivos que já estão no commit atual (para datar o que já existia)."""
    try:
        r = subprocess.run(['git', 'ls-tree', '-r', '--name-only', 'HEAD'], cwd=REPO,
                           capture_output=True, text=True, encoding='utf-8')
        return set(r.stdout.splitlines())
    except OSError:
        return set()


def head_file(path):
    """Conteúdo do arquivo no último commit publicado ('' se não existir)."""
    try:
        r = subprocess.run(['git', 'show', f'HEAD:{path}'], cwd=REPO, capture_output=True, text=True, encoding='utf-8')
        return r.stdout if r.returncode == 0 else ''
    except OSError:
        return ''


def first_added(path_glob):
    try:
        r = subprocess.run(['git', 'log', '--diff-filter=A', '--format=%as', '--', path_glob], cwd=REPO,
                           capture_output=True, text=True, encoding='utf-8')
        dates = r.stdout.split()
        return dates[-1] if dates else None
    except OSError:
        return None


def main():
    meta_path = os.path.join(REPO, 'kit-meta.json')
    meta = json.load(open(meta_path, encoding='utf-8'))
    meta.setdefault('mcp', {})
    meta.setdefault('plugins_info', {})
    lock = skill_lock_sources()
    notes = []
    today = datetime.date.today().isoformat()

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

    # ---------- comandos (~/.claude/commands) ----------
    out_cmds = os.path.join(REPO, 'commands')
    shutil.rmtree(out_cmds, ignore_errors=True)
    commands = {}
    if os.path.isdir(COMMANDS):
        for dp, _dirs, files in os.walk(COMMANDS):
            for f in files:
                if f.endswith('.md'):
                    rel = os.path.relpath(os.path.join(dp, f), COMMANDS)
                    n = rel[:-3].replace('\\', '/')
                    commands[n] = os.path.join(dp, f)
                    os.makedirs(os.path.dirname(os.path.join(out_cmds, rel)), exist_ok=True)
                    shutil.copy(commands[n], os.path.join(out_cmds, rel))

    # ---------- plugins ----------
    settings = json.load(open(os.path.join(CLAUDE, 'settings.json'), encoding='utf-8'))
    enabled = settings.get('enabledPlugins', {})
    markets = settings.get('extraKnownMarketplaces', {})
    os.makedirs(os.path.join(REPO, 'plugins'), exist_ok=True)
    json.dump({'enabledPlugins': enabled, 'extraKnownMarketplaces': markets},
              open(os.path.join(REPO, 'plugins', 'plugins.json'), 'w', encoding='utf-8'), indent=2)

    # ---------- MCP (sem chaves) ----------
    os.makedirs(os.path.join(REPO, 'mcp'), exist_ok=True)
    servers = collect_mcp()
    json.dump({'mcpServers': servers}, open(os.path.join(REPO, 'mcp', '.mcp.json'), 'w', encoding='utf-8'), indent=2)
    if os.path.isdir(MCP_BIN):
        shutil.copytree(MCP_BIN, os.path.join(REPO, 'mcp', 'bin'), dirs_exist_ok=True, ignore=ignore)

    # ---------- hooks e conta claude.ai ----------
    hooks = collect_hooks(settings)
    conta = collect_conta()
    if conta:
        write_conta_md(conta)

    # ---------- CLAUDE.md ----------
    shutil.copy(os.path.join(CLAUDE, 'CLAUDE.md'), os.path.join(REPO, 'CLAUDE.md'))

    # ---------- inventário, datas de entrada e CHANGELOG ----------
    inv = {
        'skills': {n: tree_hash(p) for n, p in skills.items()},
        'agentes': {n: tree_hash(p) for n, p in agents.items()},
        'comandos': {n: tree_hash(p) for n, p in commands.items()},
        'plugins': {k: 'ligado' if v else 'desligado' for k, v in enabled.items()},
        'mcp': {k: json.dumps(v, sort_keys=True) for k, v in servers.items()},
        'hooks': dict(hooks),
        'conta': ({f'{t}: {i["nome"]}': i['descricao'] for t in ('skills', 'conectores', 'plugins')
                   for i in conta.get(t, [])} if conta else {}),
    }
    fill_dates(meta, inv, skills, today)
    prev = meta.get('inventario')
    if prev is not None:
        lines = diff_inventory(prev, inv)
        if lines:
            write_changelog(lines)
    else:
        write_changelog(['= inventário inicial registrado (as próximas mudanças aparecem aqui)'])
    meta['inventario'] = inv

    json.dump(meta, open(meta_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    write_readme(meta, skills, agents, commands, enabled, markets, servers, hooks, conta)
    for n in notes:
        print(n)


def fill_dates(meta, inv, _skills, today):
    """Data em que cada item entrou no kit (YYYY-MM-DD). Itens antigos são datados pelo git."""
    ent = meta.setdefault('entrou', {})
    pub = None
    first_kit = first_added('README.md') or today
    for tipo, items in inv.items():
        d = ent.setdefault(tipo, {})
        for n in list(d):
            if n not in items:
                del d[n]
        for n in items:
            if n in d:
                continue
            if 'inventario' not in meta:
                # primeira vez: descobre pelo histórico do git
                if pub is None:
                    pub = published_paths()
                if tipo == 'skills':
                    m = meta['skills'].get(n, {})
                    path = f'skills/{m.get("area", "outras")}/{n}/SKILL.md'
                    if path in pub:
                        d[n] = first_added(path) or first_kit
                    else:
                        d[n] = first_kit if f'`{n}`' in head_file('README.md') else today
                elif tipo == 'agentes':
                    path = f'agents/{n}.md'
                    d[n] = (first_added(path) or first_kit) if path in pub else today
                else:
                    published = {'plugins': head_file('plugins/plugins.json'), 'mcp': head_file('mcp/.mcp.json')}
                    d[n] = first_kit if f'"{n}"' in published.get(tipo, '') else today
            else:
                d[n] = today


def diff_inventory(prev, cur):
    lines = []
    for tipo, label in TIPOS.items():
        a, b = prev.get(tipo, {}), cur.get(tipo, {})
        for n in sorted(set(b) - set(a)):
            lines.append(f'+ {label} `{n}`')
        for n in sorted(set(a) & set(b)):
            if a[n] != b[n]:
                extra = f' ({a[n]} → {b[n]})' if tipo == 'plugins' else ''
                lines.append(f'~ {label} `{n}`{extra}')
        for n in sorted(set(a) - set(b)):
            lines.append(f'− {label} `{n}`')
    return lines


def write_changelog(lines):
    path = os.path.join(REPO, 'CHANGELOG.md')
    head = ('# Changelog\n\nTudo o que entrou (**+**), mudou (**~**) ou saiu (**−**) do kit, '
            'em cada atualização. Gerado sozinho pelo `sync-kit.ps1`.\n')
    old = ''
    if os.path.exists(path):
        txt = open(path, encoding='utf-8').read()
        i = txt.find('\n## ')
        old = txt[i:] if i >= 0 else ''
    stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    entry = f'\n## {stamp}\n\n' + '\n'.join(f'- {l}' for l in lines) + '\n'
    open(path, 'w', encoding='utf-8', newline='\n').write(head + entry + old)


def write_conta_md(conta):
    out = ['# Minha conta claude.ai', '',
           'O que está ativado na minha conta do claude.ai (Personalização → Skills, Conectores e Plugins). '
           'Só nomes e para que servem: nenhuma conta conectada, e-mail ou dado dos conectores.', '',
           f'Lista conferida em: {conta.get("atualizado") or "?"}', '']
    out += conta_tables(conta)
    open(os.path.join(REPO, 'conta-claude-ai.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')


def conta_tables(conta):
    out = []
    for tipo, titulo in (('skills', 'Skills'), ('conectores', 'Conectores'), ('plugins', 'Plugins')):
        itens = conta.get(tipo, [])
        out.append(f'### {titulo} ({len(itens)})\n')
        if not itens:
            out.append('_Nenhum._\n')
            continue
        out.append('| Nome | Para que serve |\n|---|---|')
        out += [f'| {i["nome"]} | {i["descricao"]} |' for i in itens]
        out.append('')
    return out


def badge(label, value, color):
    esc = lambda s: quote(str(s).replace('-', '--').replace('_', '__'), safe='')
    return f'![{label}](https://img.shields.io/badge/{esc(label)}-{esc(value)}-{color})'


def write_readme(meta, skills, agents, commands, enabled, markets, servers, hooks, conta):
    tmpl = open(os.path.join(REPO, 'scripts', 'README.template.md'), encoding='utf-8').read()
    today = datetime.date.today().strftime('%d/%m/%Y')
    ent = meta.get('entrou', {})

    def link(src):
        return src if '/' not in src or ' ' in src else f'[{src}](https://github.com/{src})'

    def dt(tipo, n):
        d = ent.get(tipo, {}).get(n, '')
        return '/'.join(reversed(d.split('-'))) if d else ''

    rows = []
    for area, title in meta['areas'].items():
        names = sorted(n for n in skills if meta['skills'][n]['area'] == area)
        if not names:
            continue
        rows.append(f'\n### {title} ({len(names)})\n\n| Skill | O que faz | Fonte | Licença | Entrou |\n|---|---|---|---|---|')
        for n in names:
            m = meta['skills'][n]
            name = f'[`{n}`](skills/{area}/{n})' if m['modo'] == 'copia' else f'`{n}` (só link)'
            rows.append(f'| {name} | {m["descricao"]} | {link(m["fonte"])} | {m["licenca"]} | {dt("skills", n)} |')
    skill_table = '\n'.join(rows)

    arows = ['| Agente | O que faz | Área | Fonte | Licença | Entrou |', '|---|---|---|---|---|---|']
    for n in sorted(agents, key=lambda x: (meta['agentes'][x]['area'], x)):
        m = meta['agentes'][n]
        arows.append(f'| [`{n}`](agents/{n}.md) | {m["descricao"]} | {m["area"]} | {link(m["fonte"])} | '
                     f'{m["licenca"]} | {dt("agentes", n)} |')
    if commands:
        arows += ['', '**Comandos** (`~/.claude/commands`):', '', '| Comando | O que faz | Entrou |', '|---|---|---|']
        arows += [f'| [`/{n}`](commands/{n}.md) | {frontmatter_description(p)} | {dt("comandos", n)} |'
                  for n, p in sorted(commands.items())]

    def market_repo(mk):
        if mk == 'claude-plugins-official':
            return 'anthropics/claude-plugins-official'
        src = (markets.get(mk) or {}).get('source', {})
        return src.get('repo') or mk

    prows = ['| Plugin | O que faz | Área | Fonte | Licença | Entrou | Instalar |', '|---|---|---|---|---|---|---|']
    for full, on in sorted(enabled.items()):
        n, mk = (full.split('@') + [''])[:2]
        info = meta['plugins_info'].get(n, {})
        desc = meta['plugins'].get(n, '')
        if not on:
            desc += ' (desligado)'
        prows.append(f'| `{n}` | {desc} | {info.get("area", "")} | {link(market_repo(mk))} | '
                     f'{info.get("licenca", "ver fonte")} | {dt("plugins", full)} | `/plugin install {full}` |')

    mrows = ['| Conector | O que faz | Tipo | Entrou |', '|---|---|---|---|']
    for k, v in sorted(servers.items()):
        tipo = v.get('url') or 'local (' + v.get('command', '') + ')'
        mrows.append(f'| `{k}` | {meta["mcp"].get(k, "")} | {tipo} | {dt("mcp", k)} |')

    hrows = ['| Evento | O que faz |', '|---|---|'] + [f'| `{e}` | {d} |' for e, d in sorted(hooks.items())]

    if conta:
        conta_txt = (f'Conferido em {conta.get("atualizado") or "?"} pela skill `kit-sync-conta` '
                     f'(só nomes; detalhes em [`conta-claude-ai.md`](conta-claude-ai.md)).\n\n'
                     + '\n'.join(conta_tables(conta)))
    else:
        conta_txt = '_Ainda não conferida (rode a skill `kit-sync-conta`)._'

    links = [f'- `{n}` — {m["descricao"]}: <https://github.com/{m["fonte"]}> ({m["licenca"]})'
             for n, m in sorted(meta['skills'].items()) if m['modo'] == 'link' and n in skills]

    credits = {}
    for n in skills:
        m = meta['skills'][n]
        if m['fonte'] != 'própria':
            credits.setdefault((m['fonte'], m['licenca']), []).append(n)
    credits.setdefault(('VoltAgent/awesome-claude-code-subagents', 'MIT'), []).append(f'{len(agents)} agentes')
    crows = [f'- [{s}](https://github.com/{s}) · {l} — {", ".join(sorted(v))}' for (s, l), v in sorted(credits.items())]

    n_conta = sum(len(conta.get(t, [])) for t in ('skills', 'conectores', 'plugins')) if conta else 0
    badges = ' '.join([badge('última atualização', today, '2ea44f'), badge('skills', len(skills), 'blue'),
                       badge('agentes', len(agents), 'blue'), badge('plugins', len(enabled), 'blue'),
                       badge('MCP', len(servers), 'blue'), badge('claude.ai', n_conta, 'orange')])

    n_copy = sum(1 for n in skills if meta['skills'][n]['modo'] == 'copia')
    out = (tmpl.replace('{{BADGES}}', badges).replace('{{DATA}}', today)
               .replace('{{N_SKILLS}}', str(len(skills))).replace('{{N_COPIA}}', str(n_copy))
               .replace('{{N_AGENTES}}', str(len(agents))).replace('{{N_PLUGINS}}', str(len(enabled)))
               .replace('{{N_MCP}}', str(len(servers)))
               .replace('{{TABELA_SKILLS}}', skill_table).replace('{{TABELA_AGENTES}}', '\n'.join(arows))
               .replace('{{TABELA_PLUGINS}}', '\n'.join(prows)).replace('{{TABELA_MCP}}', '\n'.join(mrows))
               .replace('{{TABELA_HOOKS}}', '\n'.join(hrows)).replace('{{CONTA}}', conta_txt)
               .replace('{{SO_LINK}}', '\n'.join(links) or '_Nenhuma._')
               .replace('{{CREDITOS}}', '\n'.join(crows))
               .replace('{{OWNER}}', OWNER).replace('{{REPO}}', REPO_NAME))
    open(os.path.join(REPO, 'README.md'), 'w', encoding='utf-8', newline='\n').write(out)


if __name__ == '__main__':
    sys.exit(main())
