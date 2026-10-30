"""End card for 'You have to earn the back'.
Real Tora print on a seamless cream canvas, 12% start, 4% push-in anchored on the eyes (leaves a caption band above the logo),
then a 0.4 s push into a lower-body brushstroke so the loop cuts back to the
Veo opening macro. Output: 1080x1920, 30 fps, 3.5 s, no audio, no added text."""
import subprocess, sys, os
from PIL import Image, ImageFilter
SRC, OUT = sys.argv[1], sys.argv[2]
FPS, DUR, W, H, S = 30, 3.5, 1080, 1920, 2          # S = supersample
art = Image.open(SRC).convert('RGB')
bg = art.getpixel((5, 5))                            # print's own cream, so no seam
aw = W * S; ah = round(art.height * aw / art.width)
art = art.resize((aw, ah), Image.LANCZOS)
canvas = Image.new('RGB', (W * S, H * S), bg)
top = (H * S - ah) // 2
canvas.paste(art, (0, top))
k = aw / 1250                                        # print px -> canvas px
eyes = (625 * k, top + 560 * k)
stroke = (560 * k, top + 1180 * k)
def ease(u): return u * u * (3 - 2 * u)
tmp = os.path.join(os.path.dirname(OUT), '_ec_frames'); os.makedirs(tmp, exist_ok=True)
n = round(FPS * DUR); push_start = 3.1
for i in range(n):
    t = i / FPS
    if t < push_start:
        z = 1.12 + 0.045 * (t / push_start); cx, cy = eyes; blur = 0
    else:
        u = ease((t - push_start) / (DUR - push_start))
        z = 1.165 + (3.0 - 1.165) * u
        cx = eyes[0] + (stroke[0] - eyes[0]) * u; cy = eyes[1] + (stroke[1] - eyes[1]) * u
        blur = 1.5 * u
    cw, ch = W * S / z, H * S / z
    cx = min(max(cx, cw / 2), W * S - cw / 2); cy = min(max(cy, ch / 2), H * S - ch / 2)
    f = canvas.crop((round(cx - cw / 2), round(cy - ch / 2), round(cx + cw / 2), round(cy + ch / 2))).resize((W, H), Image.LANCZOS)
    if blur: f = f.filter(ImageFilter.GaussianBlur(blur))
    f.save(f'{tmp}/{i:04d}.png')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', f'{tmp}/%04d.png',
                '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '16', '-preset', 'veryfast', OUT], check=True)
for f in os.listdir(tmp): os.remove(os.path.join(tmp, f))
os.rmdir(tmp)
