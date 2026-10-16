"""Procura dados pessoais no kit antes de publicar.

Busca e-mails, telefones brasileiros, CPF, pastas proibidas e os termos da lista
privada (~/.claude/kit-sync/private-terms.txt, um por linha, que NUNCA vai para o repositório).
Sai com código 1 se achar algo. Mostra só arquivo, linha e tipo (sem repetir o dado).

Uso: python scripts/check_personal.py [pasta]
"""
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRIVATE = os.path.join(os.path.expanduser('~'), '.claude', 'kit-sync', 'private-terms.txt')

EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
# E-mails genéricos que podem aparecer (exemplos, licenças, bots)
EMAIL_OK = re.compile(r'(?i)(@(example|exemplo|email|domain|test|company|acme|yourdomain|domínio)\.|noreply|no-reply|'
                      r'@anthropic\.com|users\.noreply\.github\.com|@users\.github|you@|user@|seu@|nome@|name@|'
                      r'contato@|contact@|hello@|support@|security@|admin@|info@|privacy@|privacidade@|dpo@|'
                      r'git@github\.com|@localhost|\.(png|jpg|svg|webp)$|@[0-9]|@v?\d+\.\d)')
PHONE = re.compile(r'(?<![\d.])(?:\+?55[\s-]?)?\(?\b[1-9]{2}\)?[\s-]?9\d{4}[\s-]?\d{4}\b(?![\d.])'
                   r'|\(\d{2}\)\s?\d{4,5}-\d{4}')
PHONE_OK = re.compile(r'(?i)(9{4,}|99999|9xxxx|xxxx|0000-0000|1234-5678|91234-5678|98765-4321)')
CPF = re.compile(r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b')
CPF_OK = re.compile(r'(000\.000\.000|111\.111\.111|123\.456\.789|999\.999\.999)')
BAD_PATHS = ('chat-exports', 'instagram-export', '.remember', 'settings.local.json', '.env')
SKIP_DIRS = {'.git'}
TEXT_EXT = {'.md', '.txt', '.json', '.py', '.ps1', '.sh', '.js', '.ts', '.tsx', '.mjs', '.cjs', '.yml', '.yaml',
            '.toml', '.html', '.css', '.csv', '.xml', '.ini', '.cfg', '.svg', ''}


def load_private():
    try:
        return [t.strip() for t in open(PRIVATE, encoding='utf-8') if t.strip() and not t.startswith('#')]
    except OSError:
        return []


def load_allowlist():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'personal-allowlist.txt')
    try:
        return {t.strip().lower() for t in open(p, encoding='utf-8') if t.strip() and not t.startswith('#')}
    except OSError:
        return set()


def main():
    allow = load_allowlist()
    terms = [(t, re.compile(re.escape(t), re.I)) for t in load_private()]
    hits = []
    for dp, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel_dir = os.path.relpath(dp, ROOT)
        for f in files:
            rel = os.path.normpath(os.path.join(rel_dir, f))
            if any(b in rel.replace('\\', '/').split('/') or rel.endswith(b) for b in BAD_PATHS):
                hits.append(f'{rel}: arquivo/pasta proibido')
                continue
            if f in ('sync-kit.log', 'personal-allowlist.txt') or os.path.splitext(f)[1].lower() not in TEXT_EXT:
                continue
            try:
                lines = open(os.path.join(dp, f), encoding='utf-8', errors='replace').read().splitlines()
            except OSError:
                continue
            for i, line in enumerate(lines, 1):
                for m in EMAIL.finditer(line):
                    if not EMAIL_OK.search(m.group(0)) and m.group(0).lower() not in allow:
                        hits.append(f'{rel}:{i}: e-mail')
                for m in PHONE.finditer(line):
                    if not PHONE_OK.search(m.group(0)):
                        hits.append(f'{rel}:{i}: telefone')
                for m in CPF.finditer(line):
                    if not CPF_OK.search(m.group(0)):
                        hits.append(f'{rel}:{i}: CPF')
                for idx, (_, rx) in enumerate(terms, 1):
                    if rx.search(line):
                        hits.append(f'{rel}:{i}: termo privado #{idx}')
    if hits:
        print(f'DADOS PESSOAIS SUSPEITOS: {len(hits)}')
        for h in hits:
            print('  ' + h)
        return 1
    print(f'Busca de dados pessoais: limpo (e-mail, telefone, CPF, pastas proibidas, {len(terms)} termos privados).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
