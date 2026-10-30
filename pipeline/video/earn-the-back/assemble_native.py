"""Native-style cut: Veo footage only, original audio, TikTok-style text, no VO, no end card.
usage: assemble_native.py VEO SPEC.json OUT  (spec: {"end": s, "text": [[[lines], start, end], ...]})"""
import json
import subprocess, sys, os, tempfile
VEO, SPEC, OUT = sys.argv[1:4]
spec = json.load(open(SPEC)); END = spec['end']
FONT = os.path.join(os.path.dirname(__file__), '../../fonts/TikTokSans-600.ttf')
# (lines, start, end)
TEXT = spec['text']
tmp = tempfile.mkdtemp(); draw = []
for i, (lines, a, b) in enumerate(TEXT):
    for j, line in enumerate(lines):
        p = os.path.join(tmp, f't{i}_{j}.txt'); open(p, 'w').write(line)
        draw.append(f"drawtext=fontfile={FONT}:textfile={p}:fontsize={spec.get('size', 52)}:fontcolor=white:borderw=4:bordercolor=black@0.85:"
                    f"shadowcolor=black@0.45:shadowx=0:shadowy=2:x=(w-text_w)/2:y={spec.get('y', 190) + j * spec.get('gap', 68)}:enable='between(t,{a},{b})'")
fc = (f"[0:v]scale=1080:1920:flags=lanczos,fps=30,setsar=1,trim=0:{END},setpts=PTS-STARTPTS,{','.join(draw)}[v];"
      f"[0:a]atrim=0:{END},asetpts=PTS-STARTPTS,volume=18dB,afade=t=out:st={END-0.2}:d=0.2,loudnorm=I=-16:TP=-1.5[a]")
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', VEO, '-filter_complex', fc, '-map', '[v]', '-map', '[a]',
                '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                '-ar', '48000', '-movflags', '+faststart', OUT], check=True)
