---
name: video-link
description: Watches a video from a link or file — Instagram Reels/posts, TikTok, YouTube, Shorts, X, Facebook, Vimeo and 1000+ sites. Downloads it, transcribes the speech (local Whisper, no API key) and extracts keyframes so Claude can see and hear it. Use when the user sends a video link or file and asks what it says, to summarize it, take notes, copy the idea, or "olha esse vídeo / vê esse reels / esse tiktok".
---

> **Neste PC:** use `C:/Users/user/.claude/venvs/midia/Scripts/python.exe` no lugar de `python3` (Python 3.13 com os pacotes já instalados; o Python 3.15 padrão não tem Pillow nem faster-whisper).

# Video link

```bash
python3 <this-skill-dir>/scripts/watch.py "<url-or-file>" <out_dir>
```

Output in `<out_dir>`: `transcript.txt` (timestamped speech), `frames/` (one frame every
2 s, max 30), `summary.json` (title, author, caption, duration, views, likes, language).

## Steps

1. Check tools once: `yt-dlp --version && ffmpeg -version && python3 -c "import faster_whisper"`.
   Missing → `pip install -U yt-dlp faster-whisper` and install ffmpeg
   (Windows: `winget install ffmpeg`; macOS: `brew install ffmpeg`).
2. Run the script. Use a new folder per video in the scratchpad (or `videos/<name>` if the
   user wants to keep it).
3. Read `summary.json` and `transcript.txt`. Look at a handful of frames (start, middle, end,
   plus any moment the transcript points to) — don't open all 30 unless needed.
4. Answer what the user asked: summary, step-by-step, quotes with timestamps, ideas to copy.
   If they use Obsidian, offer to save the notes there (skill `obsidian-markdown`).

## When it fails

- **Instagram/TikTok asks for login or "rate-limit"** → retry with the user's browser
  session: add `--cookies-from-browser chrome` (or `firefox`, `edge`). This reads cookies
  locally; nothing is sent anywhere else. Only on the user's own computer.
- **Private video** → only works if the user's logged-in account can see it.
- **Cloud session with blocked network** (HTTP 403 from proxy) → tell the user to run it on
  their computer or send the video file itself; the script accepts a file path.
- `yt-dlp` breaks often when sites change → `pip install -U yt-dlp` first.

Respect copyright: summarizing and taking notes is fine; don't re-upload other people's videos.
