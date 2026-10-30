"""Assemble 'You have to earn the back'. usage: assemble.py VEO VO3 ENDCARD OUT
Veo 0-9.5 s, end card 9.5-13.0 s, VO at fixed cues, captions = VO word for word."""
import subprocess, sys, os, tempfile
D = 'incoming/2026-10-30/'
VEO, VO3, END, OUT = sys.argv[1:5]
FONT = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
CUT = 9.5
vo = [(D + 'VO1.mp3', 0.2, 0), (D + 'VO2.mp3', 3.0, 2.5), (VO3, 4.7, 0), (D + 'VO4.mp3', 9.8, 0), (D + 'VO5.mp3', 11.4, 2.5)]
caps = [("You've rolled with him for a year\nand never got his back.", 0.0, 2.9),
        ("Tonight, he finally turtles.", 3.0, 4.6),
        (open(sys.argv[5]).read().strip() if len(sys.argv) > 5 else "And he's had a tiger\non his back this whole time.", 4.7, 7.4),
        ("You have to earn the back.", 9.8, 11.2), ("Shizen. Drop 01.", 11.4, 13.0)]
tmp = tempfile.mkdtemp()
draw = []
for i, (t, a, b) in enumerate(caps):
    for j, line in enumerate(t.split('\n')):
        p = os.path.join(tmp, f'c{i}_{j}.txt'); open(p, 'w').write(line)
        draw.append(f"drawtext=fontfile={FONT}:textfile={p}:fontsize=54:fontcolor=white:box=1:boxcolor=black@0.55:"
                    f"boxborderw=14:x=(w-text_w)/2:y={200 + j * 84}:enable='between(t,{a},{b})'")
inputs = ['-i', VEO, '-i', END] + sum([['-i', f] for f, _, _ in vo], [])
fc = (f"[0:v]trim=0:{CUT},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,setsar=1[a];"
      f"[1:v]scale=1080:1920,fps=30,setsar=1[b];[a][b]concat=n=2:v=1:a=0,{','.join(draw)}[v];"
      f"[0:a]atrim=0:{CUT},asetpts=PTS-STARTPTS,volume=12dB,afade=t=out:st={CUT-0.3}:d=0.3,apad=whole_dur=13[bed];")
mix = ['[bed]']
for i, (_, t, g) in enumerate(vo):
    fc += f"[{i+2}:a]volume={g}dB,adelay={int(t*1000)}:all=1,apad=whole_dur=13[v{i}];"; mix.append(f'[v{i}]')
fc += f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0,atrim=0:13,loudnorm=I=-14:TP=-1.5[aout]"
subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', fc, '-map', '[v]', '-map', '[aout]',
                '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                '-ar', '48000', '-movflags', '+faststart', OUT], check=True)
