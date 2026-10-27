#!/usr/bin/env python3
"""Local photo editing — no account, no upload.

  photo.py enhance  <in> <out>            auto light/contrast/color, denoise, sharpen
  photo.py upscale  <in> <out> [2|3|4]    AI super-resolution (EDSR model, downloaded once)
  photo.py nobg     <in> <out.png>        remove background (rembg)
  photo.py resize   <in> <out> <WxH>      crop-to-fill for a format, e.g. 1080x1350, 1080x1920
  photo.py compare  <before> <after> <out> side-by-side image to check the result

Needs: pip install pillow opencv-contrib-python-headless numpy rembg onnxruntime
"""
import sys
import urllib.request
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageOps

MODELS = Path.home() / ".cache" / "photo-editor"
EDSR_URL = "https://raw.githubusercontent.com/Saafke/EDSR_Tensorflow/master/models/EDSR_x{n}.pb"


def read(path):
    img = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)


def write(path, bgr):
    Image.fromarray(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)).save(path, quality=95)


def enhance(bgr):
    # gray-world white balance, gentle
    avg = bgr.reshape(-1, 3).mean(axis=0)
    bgr = np.clip(bgr * (avg.mean() / avg) ** 0.5, 0, 255).astype(np.uint8)
    # local contrast on lightness only (keeps skin tones natural)
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.createCLAHE(clipLimit=1.6, tileGridSize=(8, 8)).apply(l)
    bgr = cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2BGR)
    bgr = cv2.fastNlMeansDenoisingColored(bgr, None, 3, 3, 7, 21)
    # mild saturation boost
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[..., 1] = np.clip(hsv[..., 1] * 1.08, 0, 255)
    bgr = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    # unsharp mask
    blur = cv2.GaussianBlur(bgr, (0, 0), 1.2)
    return cv2.addWeighted(bgr, 1.35, blur, -0.35, 0)


def upscale(bgr, n):
    MODELS.mkdir(parents=True, exist_ok=True)
    model = MODELS / f"EDSR_x{n}.pb"
    if not model.exists():
        urllib.request.urlretrieve(EDSR_URL.format(n=n), model)
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(str(model))
    sr.setModel("edsr", n)
    return sr.upsample(bgr)


def fill(bgr, size):
    w, h = map(int, size.lower().split("x"))
    img = Image.fromarray(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))
    img = ImageOps.fit(img, (w, h), Image.LANCZOS, centering=(0.5, 0.4))
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    cmd, src, dst, *rest = sys.argv[1:]
    if cmd == "enhance":
        write(dst, enhance(read(src)))
    elif cmd == "upscale":
        write(dst, upscale(read(src), int(rest[0]) if rest else 2))
    elif cmd == "nobg":
        from rembg import remove
        remove(Image.open(src)).save(dst)
    elif cmd == "resize":
        write(dst, fill(read(src), rest[0]))
    elif cmd == "compare":
        a, b = read(src), read(dst)
        b = cv2.resize(b, (int(b.shape[1] * a.shape[0] / b.shape[0]), a.shape[0]))
        write(rest[0], np.hstack([a, b]))
    else:
        sys.exit(__doc__)
    print("OK ->", rest[0] if cmd == "compare" else dst)


if __name__ == "__main__":
    main()
