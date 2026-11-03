"""Video B assembly: reaction clips then the two-shot reveal, one uniform phone grade, native TikTok text.
usage: assemble_b.py SPEC.json OUT [--root DIR]
Spec: {"clips": [{"file", "in", "out", "soft", "fx", "crop"}], "text": [[[lines], start, end]], "y", "gap", "size", "music"}
Paths in the spec are relative to --root (default: repo root)."""
import argparse, json, os, subprocess, tempfile
p = argparse.ArgumentParser(); p.add_argument('spec'); p.add_argument('out'); p.add_argument('--root', default=os.path.join(os.path.dirname(__file__), '../../..'))
a = p.parse_args(); S = json.load(open(a.spec))
FONT = os.path.join(os.path.dirname(__file__), '../../fonts/TikTokSans-600.ttf')
args, chains, vl, al = [], [], [], []
for i, c in enumerate(S['clips']):
    args += ['-i', os.path.join(a.root, c['file'])]
    d = c['out'] - c['in']
    crop = ',crop={}:{}:{}:{}'.format(*c['crop']) if c.get('crop') else ''  # static phone zoom: w,h,x,y
    blur = (f",gblur=sigma={c['soft']}" if c.get('soft') else '') + (f",{c['fx']}" if c.get('fx') else '')  # fx: per-shot colour match
    # one phone for every shot: same scale, frame rate, slight warmth, light grain
    chains.append(f"[{i}:v]trim={c['in']}:{c['out']},setpts=PTS-STARTPTS{crop},scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,"
                  f"crop=1080:1920,fps=30,setsar=1{blur},eq=saturation=0.96:contrast=1.02,noise=alls=7:allf=t[v{i}]")
    chains.append(f"[{i}:a]atrim={c['in']}:{c['out']},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,"
                  f"afade=t=in:d=0.03,afade=t=out:st={d - 0.04:.3f}:d=0.04[a{i}]")
    vl.append(f'[v{i}][a{i}]')
n = len(S['clips'])
tmp = tempfile.mkdtemp(); draw = []
for k, (lines, t0, t1) in enumerate(S.get('text', [])):
    for j, line in enumerate(lines):
        f = os.path.join(tmp, f't{k}_{j}.txt'); open(f, 'w').write(line)
        draw.append(f"drawtext=fontfile={FONT}:textfile={f}:fontsize={S.get('size', 52)}:fontcolor=white:borderw=4:bordercolor=black@0.85:"
                    f"shadowcolor=black@0.45:shadowx=0:shadowy=2:x=(w-text_w)/2:y={S.get('y', 230) + j * S.get('gap', 66)}:enable='between(t,{t0},{t1})'")
total = sum(c['out'] - c['in'] for c in S['clips'])
fc = ';'.join(chains) + f";{''.join(vl)}concat=n={n}:v=1:a=1[cv][ca];[cv]{','.join(draw) or 'null'}[v]"
M = S.get('music')  # {"file", "start" (s into the track), "amb": ambience gain under music}
if M:
    args += ['-ss', str(M['start']), '-i', os.path.join(a.root, M['file'])]
    fc += (f";[ca]volume={M.get('amb', 0.35)}[amb];[{n}:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,aresample=48000,"
           f"aformat=channel_layouts=stereo,afade=t=out:st={total - 0.35:.3f}:d=0.35[mus];"
           f"[mus][amb]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[a]")
else:
    fc += ";[ca]loudnorm=I=-16:TP=-1.5[a]"
subprocess.run(['ffmpeg', '-v', 'error', '-y', *args, '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '18',
                '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-movflags', '+faststart', a.out], check=True)
