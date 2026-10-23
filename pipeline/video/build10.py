"""Shizen v10 'What's your game?' identity quiz. usage: build10.py WORDS.json VO.wav OUT.mp4 tiktok|instagram"""
import os, glob, math, subprocess, sys, json, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter
WJ, VO, OUT, PLAT = sys.argv[1:5]
W, H, FPS = 1080, 1920, 30
F = '/home/claude/fonts/'
def font(sz, w='600'): return ImageFont.truetype(F + f'Cormorant-{w}.ttf', sz)
INK = (245, 240, 232); GOLD = (214, 182, 118); DARK = (12, 13, 16)
M = '/home/claude/assets/final/model3-{}-long.jpg'
words = json.load(open(WJ)); lw = [w[0].lower().strip('.,!?') for w in words]
ORDER = [('dragon','Ryū','Pressure passer','pressure'), ('serpent','Hebi','Guard player','guard'),
         ('serpentmark','Hebi Mark','Fundamentals','fundamentals'), ('koi','Twin Koi','Never taps','never'),
         ('tigerpair','Twin Tigers','Wrestler','wrestler'), ('tiger','Tora','Scrambler','scrambler'),
         ('crane','Tsuru','Leg locker','leg'), ('waves','Nami','Flow roller','flow')]
TS = [words[lw.index(k)][1] for *_, k in ORDER]
T_CTA = words[lw.index('comment' if PLAT == 'tiktok' else 'join')][1]
TOTAL = words[-1][2] + 1.1; NF = int(TOTAL * FPS)
cache = {}
def img(p):
    if p not in cache: cache[p] = Image.open(p).convert('RGB')
    return cache[p]
def ease(t): t = min(1, max(0, t)); return 0.5 - 0.5 * math.cos(math.pi * t)
CROP = {'koi': (0.47, 0.38)}
def torso(n, u, w0=0.62, w1=0.52, cy=0.40):
    im = img(M.format(n)); W0, H0 = im.size; cx, cy = CROP.get(n, (0.5, cy))
    cw = W0 * (w0 + (w1 - w0) * ease(u)); ch = cw * H / W
    if ch > H0: ch = H0; cw = ch * W / H
    x0 = min(max(0, W0 * cx - cw / 2), W0 - cw); y0 = min(max(0, H0 * cy - ch / 2), H0 - ch)
    return im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.BILINEAR)
def mtext(d, xy, txt, fnt, fill, anchor='mm'):
    plain = txt.replace('ū', 'u'); d.text(xy, plain, font=fnt, fill=fill, anchor=anchor, features=['lnum'])
    if 'ū' in txt:
        bb = d.textbbox(xy, plain, font=fnt, anchor=anchor); i = txt.index('ū')
        x0 = bb[0] + d.textlength(plain[:i], font=fnt); x1 = x0 + d.textlength('u', font=fnt)
        top = d.textbbox((0, xy[1]), 'u', font=fnt, anchor='lt')[1] - max(2, fnt.size // 16) + (bb[1] - d.textbbox((0, xy[1]), plain, font=fnt, anchor='lt')[1])
        d.line((x0 + fnt.size * 0.05, top, x1 - fnt.size * 0.05, top), fill=fill, width=max(2, fnt.size // 22))
def shadow_text(fr, xy, txt, fnt, fill, blur=10, a=200):
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); mtext(ImageDraw.Draw(sh), (xy[0], xy[1] + 4), txt, fnt, (0, 0, 0, a))
    sh = sh.filter(ImageFilter.GaussianBlur(blur)); fr.paste(sh, (0, 0), sh); mtext(ImageDraw.Draw(fr), xy, txt, fnt, fill)
def band(fr, y0, y1, a=150, top=True):
    m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m)
    for y in range(y0, y1):
        f = (y - y0) / (y1 - y0); d.line((0, y, W, y), fill=int(a * ((1 - f) if top else f)))
    fr.paste(Image.new('RGB', (W, H), (6, 7, 10)), (0, 0), m)
def card(t, k):
    n, name, style, _ = ORDER[k]; t0 = 0 if k == 0 else TS[k]; t1 = TS[k + 1] if k < 7 else T_CTA
    u = (t - t0) / max(0.3, t1 - t0); fr = torso(n, u)
    band(fr, 0, 520, 170, True); band(fr, 960, H, 200, False)
    if k == 0 and t < TS[0] - 0.02:  # hook frame: big question over the first shirt
        shadow_text(fr, (W // 2, 330), "What's your", font(132, '600'), INK)
        shadow_text(fr, (W // 2, 470), 'BJJ game?', font(150, '700' if os.path.exists(F + 'Cormorant-700.ttf') else '600'), GOLD)
        shadow_text(fr, (W // 2, 1340), "Your rash guard in 8 seconds", font(58, '500'), INK)
        return fr
    shadow_text(fr, (W // 2, 210), "What's your BJJ game?", font(66, '600'), INK)
    # progress dots
    d = ImageDraw.Draw(fr)
    for j in range(8):
        x = W // 2 + (j - 3.5) * 34; r = 8 if j == k else 6
        d.ellipse((x - r, 290 - r, x + r, 290 + r), fill=GOLD if j == k else (120, 116, 108))
    pop = ease((t - t0) / 0.12) if k else 1
    shadow_text(fr, (W // 2, 1240), style, font(int(112 * (0.92 + 0.08 * pop)), '600'), INK)
    cx, cy = W // 2, 1380; d = ImageDraw.Draw(fr)
    tw = d.textlength(name.replace('ū', 'u'), font=font(52, '600'))
    d.ellipse((cx - tw / 2 - 90, cy - 30, cx - tw / 2 - 30, cy + 30), fill=GOLD)
    d.text((cx - tw / 2 - 60, cy), str(k + 1), font=font(44, '700' if os.path.exists(F + 'Cormorant-700.ttf') else '600'), fill=DARK, anchor='mm', features=['lnum'])
    mtext(d, (cx + 10, cy), name, font(52, '600'), (226, 214, 190))
    return fr
TILE = {}
def cta(t):
    fr = Image.new('RGB', (W, H), DARK); d = ImageDraw.Draw(fr)
    cw, ch, gx_gap, gap = 236, 380, 18, 92; gx = (W - 4 * cw - 3 * gx_gap) // 2; gy = 300
    for k, (n, name, style, _) in enumerate(ORDER):
        if n not in TILE:
            im = img(M.format(n)); W0, H0 = im.size; cx, cy = CROP.get(n, (0.5, 0.40)); w = W0 * 0.5; h = w * ch / cw
            x0 = W0 * cx - w / 2; y0 = min(max(0, H0 * cy - h / 2), H0 - h)
            TILE[n] = im.crop((int(x0), int(y0), int(x0 + w), int(y0 + h))).resize((cw, ch), Image.LANCZOS)
        x = gx + (k % 4) * (cw + gx_gap); y = gy + (k // 4) * (ch + gap)
        a = ease((t - T_CTA - k * 0.03) / 0.15); fr.paste(Image.blend(Image.new('RGB', (cw, ch), DARK), TILE[n], a), (x, y))
        d.ellipse((x + 10, y + 10, x + 58, y + 58), fill=GOLD)
        d.text((x + 34, y + 34), str(k + 1), font=font(36, '600'), fill=DARK, anchor='mm', features=['lnum'])
        d.text((x + cw // 2, y + ch + 34), style, font=font(31, '600'), fill=(214, 206, 192), anchor='mm')
    yb = gy + 2 * ch + gap + 110
    if PLAT == 'tiktok':
        mtext(d, (W // 2, yb), 'Comment your number + waitlist', font(64, '600'), INK)
        pw = 400; d.rounded_rectangle((W // 2 - pw // 2, yb + 70, W // 2 + pw // 2, yb + 150), 40, outline=GOLD, width=3)
        mtext(d, (W // 2, yb + 110), 'e.g.  6 waitlist', font(46, '500'), GOLD)
        mtext(d, (W // 2, yb + 240), '15% off when we drop', font(72, '600'), GOLD)
    else:
        mtext(d, (W // 2, yb), 'Vote for the first drop', font(64, '600'), INK)
        mtext(d, (W // 2, yb + 100), 'Join the waitlist · link in bio', font(52, '500'), (214, 206, 192))
        mtext(d, (W // 2, yb + 220), '15% off when we drop', font(72, '600'), GOLD)
    mtext(d, (W // 2, 170), 'S H I Z E N', font(64, '500'), INK)
    return fr
def scene(t):
    if t >= T_CTA - 0.03: return cta(t)
    k = 0
    for j in range(8):
        if t >= TS[j] - 0.03: k = j
    return card(t, k)
fd = f'/tmp/vf10{PLAT}'; shutil.rmtree(fd, ignore_errors=True); os.makedirs(fd)
for i in range(NF): scene(i / FPS).save(f'{fd}/{i:05d}.jpg', quality=90)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{fd}/%05d.jpg', '-i', VO,
    '-filter_complex', '[1:a]apad,loudnorm=I=-14:TP=-1.5:LRA=11[a]', '-map', '0:v', '-map', '[a]', '-shortest',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'medium', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', OUT], check=True)
print(OUT, NF / FPS)
