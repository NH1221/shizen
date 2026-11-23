"""Track the small neck mark (yin-yang circle) frame by frame and blur ONLY the letter row under it.
usage: python3 soften_mark.py RAW.mp4 OUT.mp4 --tmpl x,y,w,h --letters dx,dy,w,h [--sigma 1.8] [--log track.csv]
tmpl: circle box in frame 0; letters: ellipse box relative to the circle's top-left, scaled with the match."""
import argparse, csv, subprocess, cv2, numpy as np
p = argparse.ArgumentParser(); p.add_argument('raw'); p.add_argument('out')
p.add_argument('--tmpl', required=True); p.add_argument('--letters', required=True)
p.add_argument('--sigma', type=float, default=1.8); p.add_argument('--log', default=None)
a = p.parse_args()
tx, ty, tw, th = map(int, a.tmpl.split(',')); lx, ly, lw, lh = map(int, a.letters.split(','))
cap = cv2.VideoCapture(a.raw); fps = cap.get(cv2.CAP_PROP_FPS); W = int(cap.get(3)); H = int(cap.get(4))
ok, f0 = cap.read(); g0 = cv2.cvtColor(f0, cv2.COLOR_BGR2GRAY); T = g0[ty:ty + th, tx:tx + tw].copy()
vw = cv2.VideoWriter('/tmp/_soft.mp4' if False else a.out + '.noaudio.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (W, H))
px, py, rows, fr = tx, ty, [], f0
while True:
    g = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY); best = (-1, px, py, 1.0)
    for s in np.linspace(0.85, 1.25, 9):
        t = cv2.resize(T, None, fx=s, fy=s); r = 50
        x0, y0 = max(0, px - r), max(0, py - r); x1, y1 = min(W, px + r + t.shape[1]), min(H, py + r + t.shape[0])
        win = g[y0:y1, x0:x1]
        if win.shape[0] < t.shape[0] or win.shape[1] < t.shape[1]: continue
        m = cv2.matchTemplate(win, t, cv2.TM_CCOEFF_NORMED); _, v, _, loc = cv2.minMaxLoc(m)
        if v > best[0]: best = (v, x0 + loc[0], y0 + loc[1], s)
    v, px, py, s = best
    cx, cy = int(px + (lx + lw / 2) * s), int(py + (ly + lh / 2) * s); ax, ay = int(lw * s / 2), int(lh * s / 2)
    mask = np.zeros((H, W), np.float32); cv2.ellipse(mask, (cx, cy), (ax, ay), 0, 0, 360, 1.0, -1)
    mask = cv2.GaussianBlur(mask, (0, 0), 3)[..., None]
    blur = cv2.GaussianBlur(fr, (0, 0), a.sigma * s)
    out = (fr * (1 - mask) + blur * mask).astype(np.uint8); vw.write(out)
    rows.append((len(rows), round(v, 3), px, py, round(s, 3), cx, cy))
    ok, fr = cap.read()
    if not ok: break
vw.release()
if a.log:
    with open(a.log, 'w', newline='') as f: csv.writer(f).writerows([('frame', 'score', 'x', 'y', 'scale', 'cx', 'cy'), *rows])
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', a.out + '.noaudio.mp4', '-i', a.raw, '-map', '0:v', '-map', '1:a?', '-c:v', 'libx264',
                '-crf', '12', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-c:a', 'copy', a.out], check=True)
print('min score', min(r[1] for r in rows), 'frames', len(rows))
