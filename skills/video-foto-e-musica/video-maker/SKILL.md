---
name: video-maker
description: Makes real videos exactly as the user describes — Reels/TikTok/Shorts, promo/ad videos, product videos of a website, explainer videos with narration and subtitles, animated text, slideshows from photos — and renders an actual .mp4 file. Use when the user asks "faz um vídeo", "cria um reels", "vídeo pro Instagram/TikTok", "vídeo de divulgação", "vídeo explicando…", "anima isso", or wants to edit/cut an existing video.
---

# Video maker

Deliver a real `.mp4` the user can post, not a script. Videos are built in code (HTML or
React), so every frame is controlled and editable.

## 1. Brief (ask only what's missing, max 3 questions)
Format (9:16 Reels/TikTok · 1:1 feed · 16:9 YouTube) · length · purpose and audience ·
style references (a link → skill `video-link` to study it) · text/narration language ·
brand colors, logo, photos/clips the user has · music yes/no.
Then write a short shot list (scene, seconds, what's on screen, text, audio) and show it
before rendering anything longer than 30 s.

## 2. Pick the engine
| Need | Use |
|---|---|
| Most videos: animated text, cuts, photos, captions, ads | **HyperFrames** (official plugin `hyperframes`, by HeyGen) — write HTML + GSAP, render to MP4 |
| React-based, data-driven, many variants, product demos | **Remotion** — `npx create-video@latest`, then `npx skills add remotion-dev/skills` for the official Remotion skills |
| Cinematic product/website promo with camera moves | `git clone --depth 1 https://github.com/Vincentwei1021/video-shotcraft` into a work folder and follow its `SKILL.md` (Apache-2.0) |
| Narrated explainer (topic → video with voice + subtitles) | `git clone --depth 1 https://github.com/Vincentwei1021/anything2explainer` and follow its `SKILL.md` |
| Simple cut/trim/merge/subtitles/resize of an existing video | `ffmpeg` directly |
| AI-generated footage (realistic scenes) | official plugin `runway-api` — paid, needs the user's Runway key; say the cost first |

Remotion is free for individuals and companies up to 3 people; bigger companies need a
license — mention it if the video is for a business client.

## 3. Quality bar (so it doesn't look "AI-made")
- Hook in the first 1–2 s; one idea per scene; scene changes every 1.5–3 s for Reels.
- Big readable text inside the safe area (top/bottom 15% free on 9:16 for app UI).
- One type family + one accent color from the brand; consistent motion easing.
- Captions burned in (most people watch muted). Music under voice at ~-18 dB.
- Narration: real voice from the user if possible; otherwise TTS in natural Portuguese.

## 4. Render, check, deliver
- Render MP4 (H.264, 30 fps, 1080×1920 for 9:16). Extract 4–6 frames with ffmpeg and look
  at them before saying it's done; fix anything off (text cut, overlap, wrong colors).
- Save to `videos/<nome>.mp4` (or scratchpad) and send the file to the user.
- Offer variations (other hook, other length, other format) — cheap once the code exists.
