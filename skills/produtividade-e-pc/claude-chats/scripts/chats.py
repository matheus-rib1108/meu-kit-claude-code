#!/usr/bin/env python3
"""Read the user's claude.ai chat history from the official data export.

Export: claude.ai -> Settings -> Privacy -> Export data -> download the .zip from the email.

  chats.py <export> list [N]               newest N conversations (default 30)
  chats.py <export> search <words...>      conversations containing all the words
  chats.py <export> show <id|title> [chars] full text of one conversation
  chats.py <export> last [chars]           the most recent conversation

<export> = the .zip, the extracted folder, or conversations.json.
"""
import json
import sys
import zipfile
from pathlib import Path


def load(src):
    p = Path(src)
    if p.is_dir():
        p = next(p.rglob("conversations.json"))
    if p.suffix == ".zip":
        with zipfile.ZipFile(p) as z:
            name = next(n for n in z.namelist() if n.endswith("conversations.json"))
            data = json.loads(z.read(name))
    else:
        data = json.loads(p.read_text(encoding="utf-8"))
    return sorted(data, key=lambda c: c.get("updated_at") or c.get("created_at") or "", reverse=True)


def message_text(m):
    parts = [b.get("text", "") for b in m.get("content") or [] if b.get("type") == "text"]
    text = "\n".join(t for t in parts if t) or m.get("text", "")
    for a in m.get("attachments") or []:
        if a.get("extracted_content"):
            text += f"\n[anexo {a.get('file_name', '')}]\n{a['extracted_content'][:2000]}"
    return text.strip()


def messages(c):
    return [(m.get("sender"), m.get("created_at", ""), message_text(m)) for m in c.get("chat_messages") or []]


def head(c):
    msgs = messages(c)
    first = next((t for s, _, t in msgs if s == "human"), "")
    when = (c.get("updated_at") or c.get("created_at") or "")[:16].replace("T", " ")
    return f"{c['uuid'][:8]}  {when}  {len(msgs):3d} msgs  {c.get('name') or '(sem título)'}\n    {first[:140]!r}"


def render(c, limit):
    out = [f"# {c.get('name') or c['uuid']}  ({c.get('created_at', '')[:10]})"]
    for sender, ts, text in messages(c):
        who = "VOCÊ" if sender == "human" else "CLAUDE"
        out.append(f"\n## {who} {ts[:16].replace('T', ' ')}\n{text}")
    text = "\n".join(out)
    return text if len(text) <= limit else "[…início cortado…]\n" + text[-limit:]


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    convs = load(sys.argv[1])
    cmd, args = sys.argv[2], sys.argv[3:]
    if cmd == "list":
        for c in convs[: int(args[0]) if args else 30]:
            print(head(c))
    elif cmd == "search":
        words = [w.lower() for w in args]
        for c in convs:
            blob = (c.get("name") or "").lower() + " " + " ".join(t.lower() for _, _, t in messages(c))
            if all(w in blob for w in words):
                print(head(c))
    elif cmd in ("show", "last"):
        if cmd == "last":
            c, limit = convs[0], int(args[0]) if args else 60000
        else:
            key = args[0].lower()
            c = next((c for c in convs if c["uuid"].startswith(key) or key in (c.get("name") or "").lower()), None)
            if not c:
                sys.exit("conversa não encontrada")
            limit = int(args[1]) if len(args) > 1 else 60000
        print(render(c, limit))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
