# ClassKite media tools

Reusable scripts for making ClassKite social images and YouTube Shorts.

- `shots.js` — screenshot each artboard (`#img1`…) of an HTML file to PNG. `NODE_PATH=$(npm root -g) node shots.js page.html outdir`
- `render.js` — render an animated HTML page (exposes `window.render(t)` and `window.DUR`) to 30 fps PNG frames. `node render.js page.html frames full`
- `vo.py` — Kokoro TTS voiceover, one WAV per line in `lines.json`. Needs `pip install kokoro-onnx soundfile` and `kokoro-v1.0.onnx` + `voices-v1.0.bin` from github.com/thewh1teagle/kokoro-onnx releases (model-files-v1.0) in `$TTS`. Voice `af_heart`. `TTS=dir python3 vo.py workdir af_heart`
- `music.py` — original synth background bed. `python3 music.py out.wav SECONDS`
- `templates/` — the week 1 image sheet and teaching-cycle Short, in brand colours (#003463, #0067F8, #05A1D7, #15CDD2, #BAF0F2; Inter).

Mix: delay each VO line to its scene start (+0.3 s), duck music with `sidechaincompress`, `loudnorm=I=-14`, encode H.264 1080x1920 + AAC.
