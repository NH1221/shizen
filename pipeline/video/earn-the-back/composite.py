"""Put the real Tora print on the back of the turtled partner in the base still.

Ink is applied as a multiply normalised to the print's own cream, so the print
background vanishes and the shirt's shading and grain show through. The art is
bent around the rounded back (cylinder across, foreshortened at the top) and
nudged along the shirt's creases.

usage: composite.py BASE ART OUT [--cx 390 --logo-top 385 --scale 0.406]
"""
import argparse
import numpy as np
import cv2

p = argparse.ArgumentParser()
p.add_argument('base'); p.add_argument('art'); p.add_argument('out')
p.add_argument('--cx', type=float, default=390)        # spine x in the base still
p.add_argument('--logo-top', type=float, default=385)  # where the logo's top lands
p.add_argument('--scale', type=float, default=0.406)   # art px -> base px
p.add_argument('--strength', type=float, default=0.9)  # ink opacity
a = p.parse_args()

base = cv2.cvtColor(cv2.imread(a.base, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB).astype(np.float32)
art = cv2.cvtColor(cv2.imread(a.art, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB).astype(np.float32)
H, W = base.shape[:2]; ah, aw = art.shape[:2]
bg = art[:10, :10].reshape(-1, 3).mean(0)
ratio = np.clip(art / bg, 0, 1.0)
ratio = cv2.GaussianBlur(ratio, (0, 0), 1.2)           # match the photo's softness

s = a.scale
box_h, half_w = ah * s, aw * s / 2
y0 = a.logo_top - 25 * s
k, theta = -0.2, 0.9                                    # top foreshortening, back curvature

# crease displacement from the shirt itself
lum = cv2.cvtColor(base.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
sm = cv2.GaussianBlur(lum, (0, 0), 3)
gx = cv2.Sobel(sm, cv2.CV_32F, 1, 0, ksize=3); gy = cv2.Sobel(sm, cv2.CV_32F, 0, 1, ksize=3)
mag = np.sqrt(gx ** 2 + gy ** 2) + 1e-6
disp = 4.5 * np.tanh(mag / 40.0)
dx, dy = gx / mag * disp, gy / mag * disp

Y, X = np.mgrid[0:H, 0:W].astype(np.float32)
t = (Y + dy - y0) / box_h
v = (-(1 + k) + np.sqrt((1 + k) ** 2 + 4 * (-k) * np.clip(t, 0, 1))) / (2 * (-k))
wscale = 0.9 + 0.15 * v
u_scr = (X + dx - a.cx) / (half_w * wscale)
u = np.arcsin(np.clip(u_scr * np.sin(theta), -1, 1)) / theta
map_x = (aw / 2 + u * aw / 2).astype(np.float32)
map_y = (v * ah).astype(np.float32)
inside = (t >= 0) & (t <= 1) & (np.abs(u_scr) <= 1)
ink = cv2.remap(ratio, map_x, map_y, cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=(1, 1, 1))
ink[~inside] = 1.0

# only on the shirt: cream pixels, cleaned up
r, g, b = base[..., 0], base[..., 1], base[..., 2]
shirt = ((r > 150) & (r - b > 10) & (r - b < 70) & (g > 130)).astype(np.uint8)
shirt = cv2.morphologyEx(shirt, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
shirt = cv2.GaussianBlur(shirt.astype(np.float32), (0, 0), 1.5)[..., None]

ink = 1 - a.strength * (1 - ink)
out = base * (1 - shirt + shirt * ink)
noise = np.random.default_rng(7).normal(0, 1.6, out.shape).astype(np.float32)
out = np.clip(out + noise * (1 - ink) * 2.5, 0, 255).astype(np.uint8)
cv2.imwrite(a.out, cv2.cvtColor(out, cv2.COLOR_RGB2BGR))
