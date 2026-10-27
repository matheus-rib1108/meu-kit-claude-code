---
name: photo-editor
description: Improves and edits photos locally — fixes light, color and contrast, removes noise, sharpens, upscales with AI (2x-4x), removes the background, crops for Instagram/TikTok/site formats, and makes before/after comparisons. Use when the user sends a photo and asks to "melhorar a foto", "deixar mais bonita/nítida", "aumentar a qualidade", "tirar o fundo", "recortar pro Instagram", or needs images prepared for a site.
---

> **Neste PC:** use `C:/Users/user/.claude/venvs/midia/Scripts/python.exe` no lugar de `python3` (Python 3.13 com os pacotes já instalados; o Python 3.15 padrão não tem Pillow nem faster-whisper).

# Photo editor

```bash
python3 <this-skill-dir>/scripts/photo.py enhance  in.jpg out.jpg
python3 <this-skill-dir>/scripts/photo.py upscale  in.jpg out.jpg 4
python3 <this-skill-dir>/scripts/photo.py nobg     in.jpg out.png
python3 <this-skill-dir>/scripts/photo.py resize   in.jpg out.jpg 1080x1350
python3 <this-skill-dir>/scripts/photo.py compare  in.jpg out.jpg compare.jpg
```
Install once if missing: `pip install pillow opencv-contrib-python-headless numpy rembg onnxruntime`.
Models download on first use (needs internet).

## Steps
1. Look at the photo first and say what you'll fix (dark? blurry? noisy? bad crop?).
2. Usual order: `upscale` (only if small/blurry) → `enhance` → `resize` to the target format.
3. Make a `compare` image and look at it. Faces must stay natural: if skin looks plastic
   or colors are off, redo with fewer steps. Never change someone's face or body shape
   unless they ask for it.
4. Send the result file(s) to the user.

## Formats
Instagram feed 1080x1350 · Stories/Reels/TikTok 1080x1920 · square 1080x1080 ·
site hero 1920x1080 (then export WebP for the site: `cwebp -q 80`).

## Beyond this script
- Generative edits (add/remove objects, change background scene) need an image model:
  plugin `canva` (already enabled) or an API the user has (e.g. Gemini, OpenAI images).
- Old/damaged photo restoration of faces: GFPGAN / CodeFormer (heavier install; offer it).
