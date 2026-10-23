# Shizen weekly video pipeline

Used by the weekly Claude scheduled task. Fresh session setup:

```
git clone https://github.com/NH1221/shizen /home/claude/shizen
mkdir -p /home/claude/assets/vid7 /home/claude/fonts
ln -sfn /home/claude/shizen/pipeline/assets/designs /home/claude/assets/vid7/designs
ln -sfn /home/claude/shizen/pipeline/assets/mocks   /home/claude/assets/vid7/mocks
ln -sfn /home/claude/shizen/pipeline/assets/models  /home/claude/assets/vid7/models
cp /home/claude/shizen/pipeline/fonts/*.ttf /home/claude/fonts/
```

- video/build9.py: latest builder (hook strobe, 8-design grid, spotlight, comment CTA). build8 = TikTok comment CTA, build6 = Instagram link-in-bio.
- video/src9/mk9.py: phrase timings -> words.json, pause compression G=0.16, atempo 1.25. Needs e44.wav (44.1k mono voiceover).
- Voice: ElevenLabs voice "Asher", model eleven_v3/v4, stability 1.0, no emotive tags.
- Output: 1080x1920, 30 fps, 11 to 13 s. Always show all 8 designs, label as AI mock-ups, never claim hand-drawn art, no UPF/compression claims.
- Design numbering (grid order): 1 Ryu (dragon), 2 Hebi (serpent), 3 Hebi Mark, 4 Twin Koi, 5 Twin Tigers, 6 Tora (tiger), 7 Tsuru (crane), 8 Nami (wave).
- Models: assets/models/model3-<name>-long.jpg (3 rotating models). Crop overrides in video/crops.json.
