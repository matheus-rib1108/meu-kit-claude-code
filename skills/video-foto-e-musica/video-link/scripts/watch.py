#!/usr/bin/env python3
"""Download a video from a link (Instagram, TikTok, YouTube, X...), transcribe it
and extract keyframes so Claude can "watch" it.

Usage: python3 watch.py <url-or-file> [out_dir] [--cookies-from-browser chrome]
Needs: yt-dlp, ffmpeg, faster-whisper  (pip install yt-dlp faster-whisper)
"""
import json
import subprocess
import sys
from pathlib import Path


def run(cmd):
    subprocess.run(cmd, check=True)


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    url = args.pop(0)
    extra = []
    if "--cookies-from-browser" in args:
        i = args.index("--cookies-from-browser")
        extra = ["--cookies-from-browser", args[i + 1]]
        del args[i:i + 2]
    out = Path(args[0] if args else "video-out").resolve()
    out.mkdir(parents=True, exist_ok=True)

    if Path(url).is_file():  # a video file the user sent
        video = Path(url).resolve()
    else:
        # yt-dlp from the same Python, so it works even when its .exe is not on PATH.
        run([sys.executable, "-m", "yt_dlp", *extra, "--no-playlist", "-f", "mp4/best", "-o", str(out / "video.%(ext)s"),
             "--write-info-json", "--write-thumbnail", url])
        video = next(p for p in out.iterdir()
                     if p.stem == "video" and p.suffix not in (".json", ".jpg", ".webp", ".png"))

    # One frame every 2 seconds, max 30 frames, small enough to read cheaply.
    frames = out / "frames"
    frames.mkdir(exist_ok=True)
    run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(video), "-vf", "fps=1/2,scale=640:-2",
         "-frames:v", "30", str(frames / "frame_%03d.jpg")])

    from faster_whisper import WhisperModel
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segments, info = model.transcribe(str(video), vad_filter=True)
    lines = [f"[{s.start:6.1f}s] {s.text.strip()}" for s in segments]
    (out / "transcript.txt").write_text("\n".join(lines), encoding="utf-8")

    meta = {}
    info_json = next(out.glob("*.info.json"), None)
    if info_json:
        raw = json.loads(info_json.read_text(encoding="utf-8"))
        meta = {k: raw.get(k) for k in ("title", "uploader", "description", "duration",
                                         "view_count", "like_count", "upload_date", "webpage_url")}
    (out / "summary.json").write_text(json.dumps(
        {"language": info.language, "meta": meta, "frames": len(list(frames.glob("*.jpg")))},
        ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK -> {out}  (transcript.txt, frames/, summary.json)")


if __name__ == "__main__":
    main()
