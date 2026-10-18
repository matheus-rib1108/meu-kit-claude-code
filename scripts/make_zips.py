"""Gera dist/<skill>.zip (pasta da skill na raiz, formato do upload no claude.ai) e dist/todas-as-skills.zip."""
import os
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DIST = REPO / 'dist'


def zip_dir(target, folders):
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as z:
        for folder in folders:
            for p in sorted(folder.rglob('*')):
                if p.is_file():
                    # data fixa: o mesmo conteúdo gera o mesmo zip em qualquer PC
                    info = zipfile.ZipInfo(p.relative_to(folder.parent).as_posix(), (2026, 1, 1, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    z.writestr(info, p.read_bytes())


def main():
    folders = sorted((p.parent for p in REPO.glob('skills/*/*/SKILL.md')), key=lambda p: p.name)
    names = [p.name for p in folders]
    dup = {n for n in names if names.count(n) > 1}
    assert not dup, f'skills com nome repetido: {dup}'
    DIST.mkdir(exist_ok=True)
    for old in DIST.glob('*.zip'):
        old.unlink()
    for f in folders:
        zip_dir(DIST / f'{f.name}.zip', [f])
    zip_dir(DIST / 'todas-as-skills.zip', folders)
    with zipfile.ZipFile(DIST / f'{names[0]}.zip') as z:  # autoteste: SKILL.md dentro da pasta da skill
        assert f'{names[0]}/SKILL.md' in z.namelist()
    print(f'{len(folders)} skills, {len(folders) + 1} zips em {DIST}')


if __name__ == '__main__':
    sys.exit(main())
