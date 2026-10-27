"""Raspa um site (várias páginas do mesmo domínio) para Markdown, sem chave de API.

Uso: python raspar.py <url-inicial> <pasta-saida> [--max 30] [--atraso 1.0]
Lê o sitemap.xml se existir; senão segue links do mesmo domínio (busca em largura).
Cada página vira um .md limpo pelo Defuddle (npx defuddle@0.19.6). Respeita robots.txt.
"""
import argparse, re, shutil, subprocess, sys, time, urllib.request, urllib.robotparser
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag

UA = "raspar-site/1.0 (+uso pessoal)"
DEFUDDLE = "defuddle@0.19.6"
PULAR = re.compile(r"\.(png|jpe?g|gif|webp|svg|ico|pdf|zip|mp4|mp3|css|js|woff2?|xml)$", re.I)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.hrefs.append(href)


def links_do_mesmo_site(html, base):
    p = Links()
    p.feed(html)
    host = urlparse(base).netloc
    out = []
    for h in p.hrefs:
        u = urldefrag(urljoin(base, h))[0]
        pu = urlparse(u)
        if pu.scheme in ("http", "https") and pu.netloc == host and not PULAR.search(pu.path) and u not in out:
            out.append(u)
    return out


def baixar(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        if "html" not in r.headers.get("Content-Type", "") and not url.endswith("sitemap.xml"):
            return ""
        return r.read(3_000_000).decode("utf-8", "replace")


def nome_arquivo(url):
    p = urlparse(url).path.strip("/") or "index"
    return re.sub(r"[^\w.-]+", "_", p)[:80] + ".md"


def para_markdown(html, arq):
    # HTML vai pelo stdin e os argumentos são fixos: nada da página vira comando.
    npx = shutil.which("npx") or shutil.which("npx.cmd")
    if not npx:
        sys.exit("Instale o Node.js (precisa do npx).")
    r =subprocess.run([npx, "-y", DEFUDDLE, "parse", "-", "--markdown", "--frontmatter", "-o", str(arq)],
                       input=html, capture_output=True, text=True, encoding="utf-8")
    return r.returncode == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("saida")
    ap.add_argument("--max", type=int, default=30)
    ap.add_argument("--atraso", type=float, default=1.0)
    a = ap.parse_args()

    inicio = urlparse(a.url)
    if inicio.scheme not in ("http", "https"):
        sys.exit("A URL precisa começar com http:// ou https://")
    raiz = f"{inicio.scheme}://{inicio.netloc}"
    robots = urllib.robotparser.RobotFileParser(raiz + "/robots.txt")
    try:
        robots.read()
    except Exception:
        robots = None
    pode = lambda u: robots is None or robots.can_fetch(UA, u)

    fila = [a.url]
    try:
        sm = baixar(raiz + "/sitemap.xml")
        fila += [u for u in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", sm) if urlparse(u).netloc == inicio.netloc]
    except Exception:
        pass

    out = Path(a.saida)
    out.mkdir(parents=True, exist_ok=True)
    vistos, feitas = set(), []
    while fila and len(feitas) < a.max:
        u = fila.pop(0)
        if u in vistos or not pode(u):
            continue
        vistos.add(u)
        try:
            html = baixar(u)
        except Exception as e:
            print(f"pulei {u}: {e}", file=sys.stderr)
            continue
        if not html:
            continue
        fila += [l for l in links_do_mesmo_site(html, u) if l not in vistos]
        arq = out / nome_arquivo(u)
        if para_markdown(html, arq):
            feitas.append((u, arq.name))
            print(f"ok {u} -> {arq.name}")
        time.sleep(a.atraso)

    (out / "_indice.md").write_text("# Páginas raspadas\n\n" + "\n".join(f"- [{u}]({f})" for u, f in feitas), encoding="utf-8")
    print(f"{len(feitas)} páginas em {out}")


def _teste():
    html = '<a href="/sobre">x</a><a href="https://outro.com/a">y</a><a href="/logo.png">z</a><a href="/sobre#time">w</a>'
    assert links_do_mesmo_site(html, "https://ex.com/") == ["https://ex.com/sobre"]
    assert nome_arquivo("https://ex.com/") == "index.md"
    assert nome_arquivo("https://ex.com/blog/post 1/") == "blog_post_1.md"


if __name__ == "__main__":
    if sys.argv[1:] == ["--teste"]:
        _teste()
        print("teste ok")
    else:
        main()
