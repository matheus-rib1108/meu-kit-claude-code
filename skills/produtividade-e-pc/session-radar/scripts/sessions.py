#!/usr/bin/env python3
"""Read local Claude Code conversations (~/.claude/projects/**/*.jsonl).

  sessions.py list [N]            most recent N sessions (default 20)
  sessions.py search <words...>   sessions whose messages contain all the words
  sessions.py show <id> [chars]   user/assistant text of one session (id prefix ok)
"""
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path.home() / ".claude" / "projects"


def text_of(content):
    if isinstance(content, str):
        return content
    parts = []
    for block in content or []:
        if isinstance(block, dict) and block.get("type") == "text":
            parts.append(block.get("text", ""))
    return "\n".join(parts)


def load(path):
    title, msgs = None, []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                e = json.loads(line)
            except ValueError:
                continue
            kind = e.get("type")
            if kind == "ai-title":
                title = e.get("aiTitle") or e.get("title") or title
            elif kind in ("user", "assistant") and not e.get("isMeta"):
                t = text_of((e.get("message") or {}).get("content")).strip()
                if t and not t.startswith("<"):
                    msgs.append((kind, e.get("timestamp", ""), t))
    return title, msgs


def sessions():
    files = sorted(ROOT.glob("*/*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
    for p in files:
        yield p


def summary(p):
    title, msgs = load(p)
    first = next((m[2] for m in msgs if m[0] == "user"), "")
    when = datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
    project = p.parent.name
    return f"{p.stem[:8]}  {when}  {project}\n    {title or '(sem título)'} — {first[:120]!r}"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "list":
        n = int(args[0]) if args else 20
        for i, p in enumerate(sessions()):
            if i >= n:
                break
            print(summary(p))
    elif cmd == "search":
        words = [w.lower() for w in args]
        for p in sessions():
            _, msgs = load(p)
            hits = [m for m in msgs if all(w in m[2].lower() for w in words)]
            if hits:
                print(summary(p))
                for kind, ts, t in hits[:3]:
                    i = t.lower().find(words[0])
                    print(f"      [{kind} {ts[:16]}] …{t[max(0, i - 80):i + 160]!r}")
    elif cmd == "show":
        limit = int(args[1]) if len(args) > 1 else 40000
        match = [p for p in sessions() if p.stem.startswith(args[0])]
        if not match:
            sys.exit("session not found")
        title, msgs = load(match[0])
        out = [f"# {title or match[0].stem}"]
        out += [f"\n## {kind} {ts[:16]}\n{t}" for kind, ts, t in msgs]
        text = "\n".join(out)
        print(text[-limit:] if len(text) > limit else text)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
