"""Shizen TikTok v3. usage: python3 build3.py ASSET_DIR HOOK.mp4 VO.wav WORDS.json OUT.mp4 [mockprefix] [modelprefix]
ASSET_DIR has designs/, mocks/ (<prefix>-<n>-<sl>.jpg), models/ (<prefix>-<n>-<sl>.jpg)."""
import os, glob, math, subprocess, sys, json, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter
A, HOOK, VO, WJ, OUT = sys.argv[1:6]
MP = sys.argv[6] if len(sys.argv) > 6 else 'mock3'
OP = sys.argv[7] if len(sys.argv) > 7 else 'model3'
W, H, FPS = 1080, 1920, 30
F = '/home/claude/fonts/'
def font(sz, w='600'): return ImageFont.truetype(F + f'Cormorant-{w}.ttf', sz)
JP = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc', 60, index=0)
INK = (245, 240, 232); GOLD = (200, 170, 110); DARK = (12, 13, 16)
words = json.load(open(WJ))
TOTAL = words[-1][2] + 0.9
NF = int(TOTAL * FPS)
cache = {}
def img(p):
    if p not in cache:
        im = Image.open(p).convert('RGB'); im.thumbnail((2600, 2600), Image.LANCZOS); cache[p] = im
    return cache[p]
def cover(im, scale=1.0, cx=0.5, cy=0.5):
    iw, ih = im.size; s = max(W / iw, H / ih) * scale; nw, nh = int(iw * s), int(ih * s)
    r = im.resize((nw, nh), Image.BILINEAR); x = int((nw - W) * cx); y = int((nh - H) * cy)
    return r.crop((x, y, x + W, y + H))
def ease(t): t = min(1, max(0, t)); return 0.5 - 0.5 * math.cos(math.pi * t)
def fade(fr, a, col=DARK):
    return fr if a >= 1 else Image.blend(Image.new('RGB', (W, H), col), fr, max(0, a))
def vignette(fr, y0, y1, a=120):
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).rectangle((0, y0, W, y1), fill=a)
    m = m.filter(ImageFilter.GaussianBlur(70)); fr.paste(Image.new('RGB', (W, H), (6, 8, 12)), (0, 0), m)
def wordmark(fr, y, sz=92, ink=INK):
    d = ImageDraw.Draw(fr); fnt = font(sz, '500')
    d.text((W // 2, y), 'S H I Z E N', font=fnt, fill=ink, anchor='mt')
    d.text((W // 2, y + sz + 26), '自然', font=JP, fill=GOLD, anchor='mt')

D = sorted(glob.glob(os.path.join(A, 'designs/*')))
def dz(key): return next(p for p in D if key in p)
def mk(n, sl='long'): return os.path.join(A, 'mocks', f'{MP}-{n}-{sl}.jpg')
def md(n, sl='long'): return os.path.join(A, 'models', f'{OP}-{n}-{sl}.jpg')
def half(p, side):  # front (left) or back (right) of a mockup, on studio grey
    im = img(p); w = im.width // 2
    return im.crop((0, 0, w, im.height)) if side == 'front' else im.crop((im.width - w, 0, im.width, im.height))
def closeup(p, side, u, cy):  # tight crop of a studio mockup half
    h = half(p, side); cw = h.width * (0.80 - 0.08 * ease(u)); ch = cw * H / W
    x0 = (h.width - cw) / 2; y0 = max(0, min(h.height - ch, h.height * cy - ch / 2))
    return h.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.BILINEAR)
def studio(p, side, u):
    base = Image.new('RGB', (W, H), (226, 222, 216)); h = half(p, side)
    s = (W * (1.02 + 0.06 * u)) / h.width; r = h.resize((int(h.width * s), int(h.height * s)), Image.BILINEAR)
    base.paste(r, ((W - r.width) // 2, (H - r.height) // 2 - 60)); return base

# hook: three hard cuts, the moment each top lands
hk = '/tmp/hook3'; shutil.rmtree(hk, ignore_errors=True); os.makedirs(hk)
subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', HOOK, '-vf', f'fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}', f'{hk}/%05d.jpg'], check=True)
HF = sorted(glob.glob(hk + '/*.jpg'))
HOOK_CUTS = [(0.35, 0.8), (2.45, 0.8), (4.35, 0.8)]  # (source start, length)

lw = [w[0].lower().strip('.,!?') for w in words]
def t_word(w, after=0):
    i = next(k for k in range(after, len(lw)) if lw[k] == w); return words[i][1], i
T_THERE, _ = t_word('eight')
T_JAP, _ = t_word('japanese'); T_ONLY, _ = t_word('only'); T_FIRST = T_THERE
T_PICK, _ = t_word('comment')

GRID = ['dragon', 'serpent', 'serpentmark', 'koi', 'tigerpair', 'tiger', 'crane', 'waves']
NAMES = {'dragon': 'Ryū', 'serpent': 'Hebi', 'serpentmark': 'Hebi Mark', 'koi': 'Twin Koi', 'tigerpair': 'Twin Tigers', 'tiger': 'Tora', 'crane': 'Tsuru', 'waves': 'Nami'}
SLEEVE = ['long'] * 8
CROP = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'crops.json'))) if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'crops.json')) else {}
def torso(p, u, w0=0.47, w1=0.41, cy=0.36, cx=0.5):  # worn close-up with a slow push
    im = img(p); W0, H0 = im.size; c = CROP.get(os.path.basename(p), {})
    cx = c.get('cx', cx); cy = c.get('cy', cy); s = c.get('w', 1.0)
    cw = W0 * (w0 + (w1 - w0) * ease(u)) * s; ch = cw * H / W
    x0 = min(max(0, W0 * cx - cw / 2), W0 - cw); y0 = min(max(0, H0 * cy - ch / 2), H0 - ch)
    return im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.BILINEAR)
def mtext(d, xy, txt, fnt, fill, anchor='mt'):  # draws ū as u plus a macron (font subset lacks it)
    plain = txt.replace('ū', 'u'); d.text(xy, plain, font=fnt, fill=fill, anchor=anchor, features=['lnum'])
    if 'ū' in txt:
        bb = d.textbbox(xy, plain, font=fnt, anchor=anchor); i = txt.index('ū')
        x0 = bb[0] + d.textlength(plain[:i], font=fnt); x1 = x0 + d.textlength('u', font=fnt)
        top = d.textbbox((0, xy[1]), 'u', font=fnt, anchor='lt')[1] - max(2, fnt.size // 16)
        d.line((x0 + fnt.size * 0.05, top, x1 - fnt.size * 0.05, top), fill=fill, width=max(2, fnt.size // 22))
def label(fr, k, n):
    d = ImageDraw.Draw(fr); sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    txt = f'No. {k + 1:02d}   {NAMES[n]}'
    mtext(sd, (W // 2, 1514), txt, font(44, '600'), (0, 0, 0, 170)); sh = sh.filter(ImageFilter.GaussianBlur(8)); fr.paste(sh, (0, 0), sh)
    mtext(d, (W // 2, 1510), txt, font(44, '600'), (226, 214, 190))
LAB = [None]
def scene(t):
    if t < T_THERE - 0.03:  # hook: rapid strobe through all 8, worn
        k = int(t / 0.22); n = GRID[k % 8]; u = (t - k * 0.22) / 0.22
        fr = torso(md(n, 'long'), 0.3 + 0.7 * u, 0.44, 0.40)
        g = Image.new('L', (1, 560)); [g.putpixel((0, y), int(215 * (1 - y / 560) ** 1.3)) for y in range(560)]
        fr.paste(Image.new('RGB', (W, 560), (6, 8, 12)), (0, 0), g.resize((W, 560)))
        d = ImageDraw.Draw(fr); sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
        for dd, col in ((sd, (0, 0, 0, 190)), (d, None)):
            dd.text((W // 2, 190 + (6 if col else 0)), '1,000+ of you', font=font(118, '600'), fill=col or GOLD, anchor='mm', features=['lnum'])
            dd.text((W // 2, 310 + (6 if col else 0)), 'pick my first drop', font=font(84, '600'), fill=col or INK, anchor='mm')
            if col: sh = sh.filter(ImageFilter.GaussianBlur(10)); fr.paste(sh, (0, 0), sh)
        return fr
    if T_JAP - 0.05 <= t < T_ONLY - 0.05:  # Japanese ink art: two slow worn close-ups
        mid = (T_JAP + T_ONLY) / 2; n = 'dragon' if t < mid else 'tiger'
        u = (t - (T_JAP if t < mid else mid)) / (mid - T_JAP)
        return torso(md(n, 'long'), u, 0.40, 0.34, 0.33)
    if True:  # the range, then the comment CTA under it
        fr = Image.new('RGB', (W, H), DARK); d = ImageDraw.Draw(fr)
        cw, ch, gx_gap, gap = 230, 409, 22, 60; gx = (W - 4 * cw - 3 * gx_gap) // 2; gy = 480
        for k, n in enumerate(GRID):
            key = ('g', n)
            if key not in TILE: TILE[key] = torso(md(n, 'long'), 0, 0.5, 0.5, 0.37).resize((cw, ch), Image.LANCZOS)
            th = TILE[key]
            if T_ONLY - 0.05 <= t < T_PICK - 0.05 and k != int((t - T_ONLY) / 0.18) % 8: th = Image.blend(th, Image.new('RGB', th.size, DARK), 0.7)
            x = gx + (k % 4) * (cw + gx_gap); y = gy + (k // 4) * (ch + gap); fr.paste(th, (x, y))
            cx, cy = x + 28, y + 28; d.ellipse((cx - 19, cy - 19, cx + 19, cy + 19), fill=INK)
            d.text((cx, cy), str(k + 1), font=font(30, '600'), fill=(20, 20, 22), anchor='mm', features=['lnum'])
            mtext(d, (x + cw // 2, y + ch + 10), NAMES[n], font(30, '600'), (200, 194, 184))
        wordmark(fr, 260, 72)
        yb = gy + 2 * ch + gap + 70
        if t < T_PICK - 0.05:
            d.text((W // 2, yb), 'Eight designs' if t < T_JAP else 'Only one gets made', font=font(62, '500'), fill=INK, anchor='mt')
        else:
            a = min(1, (t - T_PICK + 0.05) / 0.15); c1 = tuple(int(DARK[k] + (INK[k] - DARK[k]) * a) for k in range(3)); c2 = tuple(int(DARK[k] + (GOLD[k] - DARK[k]) * a) for k in range(3))
            d.text((W // 2, yb), 'Comment your number + waitlist', font=font(54, '600'), fill=c1, anchor='mt')
            bx0, by0 = W // 2 - 150, yb + 84; d.rounded_rectangle((bx0, by0, bx0 + 300, by0 + 64), radius=32, outline=c2, width=2)
            d.text((W // 2, by0 + 32), 'e.g.  3 waitlist', font=font(36, '500'), fill=c2, anchor='mm', features=['lnum'])
            d.text((W // 2, by0 + 96), '15% off when we drop', font=font(58, '600'), fill=c2, anchor='mt', features=['lnum'])
        return fr
    fr = Image.new('RGB', (W, H), DARK); d = ImageDraw.Draw(fr)
    wordmark(fr, 430, 92)
    d.text((W // 2, 760), '15% off', font=font(190, '500'), fill=GOLD, anchor='mt', features=['lnum'])
    d.text((W // 2, 990), 'your first order', font=font(64, '500'), fill=INK, anchor='mt')
    d.line((W // 2 - 90, 1120, W // 2 + 90, 1120), fill=(90, 84, 74), width=2)
    d.text((W // 2, 1170), 'JOIN THE WAITLIST', font=font(46, '600'), fill=INK, anchor='mt')
    d.text((W // 2, 1240), 'vote for your favourite  ·  link in bio', font=font(44, '500'), fill=(170, 164, 154), anchor='mt')
    return fade(fr, (t - T_PICK + 0.1) / 0.12)
TILE = {}
def cover_tile(im, w, h):
    key = (id(im), w, h)
    if key not in TILE:
        s = max(w / im.width, h / im.height); r = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
        x = (r.width - w) // 2; y = int((r.height - h) * 0.25); TILE[key] = r.crop((x, y, x + w, y + h))
    return TILE[key]

HL = {'shizen': GOLD, '15%': GOLD, 'boring': GOLD, 'waitlist': GOLD}
def caption(fr, t):
    cur = None
    for wd, s, e in words:
        if s - 0.03 <= t < max(e, s + 0.2) + 0.04: cur = (wd, s)
    if not cur: return
    wd, s = cur; u = min(1, (t - s) / 0.1); sz = int(118 * (0.9 + 0.1 * ease(u)))
    late = t >= T_FIRST - 0.1; y = 1790 if late else 1420
    if late: sz = int(sz * 0.6)
    fnt = font(sz, '600'); col = HL.get(wd.lower().strip('.,!?'), INK)
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((W // 2, y + 4), wd, font=fnt, fill=(0, 0, 0, 210), anchor='mm', features=['lnum'])
    sh = sh.filter(ImageFilter.GaussianBlur(10)); fr.paste(sh, (0, 0), sh)
    ImageDraw.Draw(fr).text((W // 2, y), wd, font=fnt, fill=col, anchor='mm', features=['lnum'])

os.makedirs('/tmp/vf9', exist_ok=True)
for f in glob.glob('/tmp/vf9/*.jpg'): os.remove(f)
for i in range(NF):
    t = i / FPS; LAB[0] = None; fr = scene(t)
    if t < T_FIRST - 0.1: vignette(fr, 1260, 1580, 110)
    pass  # per-cut name labels removed (18 Oct)
    caption(fr, t); fr.save(f'/tmp/vf9/{i:05d}.jpg', quality=90)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', '/tmp/vf9/%05d.jpg', '-i', VO,
                '-filter_complex', '[1:a]apad,loudnorm=I=-14:TP=-1.5:LRA=11[a]', '-map', '0:v', '-map', '[a]', '-shortest',
                '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', OUT], check=True)
print('frames', NF, 'secs', NF / FPS)
