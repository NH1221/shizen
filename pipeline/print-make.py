import json, numpy as np
from PIL import Image
D='/home/claude/assets/Shizen/designs/'
KEY={'fx-ryu-01':'shizen-01-dragon-spine.png','fx-hebi-01':'shizen-02-serpent-spine.png','fx-hebi-03':'shizen-03-serpent-mark.png','fx-koi-02':'shizen-04-twin-koi.png','fx-tora-01m':'shizen-05-twin-tigers.png','hd-tora-03':'shizen-06-tiger.jpg','final-tsuru-02':'shizen-07-crane-sun.jpg','fx-nami-01':'shizen-08-wave-column.png'}
N=json.load(open('/home/claude/comp/nests.json'))
PW,PH=2500,2961
Y0,LEN=401,2721; S=PH/LEN*0.98      # vertical scale blank->panel
cache={}
def art(key):
    if key not in cache: cache[key]=Image.open(D+KEY[key]).convert('RGB')
    return cache[key]
def layer(it,ground):
    sx,sy,sw,sh=it['src']; dx,dy,dw,dh=it['dst']
    a=np.asarray(art(it['key']).crop((sx,sy,sx+sw,sy+sh))).astype(np.float32)/255
    bg=np.array(it['bg'])/255; d=np.abs(a-bg).sum(2); al=np.clip((d-0.06)/0.16,0,1)
    return a,al
names={'dragon':'Ryu','serpent':'Hebi','serpentmark':'Hebi-Mark','koi':'Twin-Koi','tigerpair':'Twin-Tigers','tiger':'Tora','crane':'Tsuru','waves':'Nami'}
for e in N:
    n=e['name'].replace('nest-','').replace('-long','')
    if not e['name'].endswith('-long') or n not in names: continue
    g=np.array(e['ground'])/255
    for side in ['front','back']:
        cv=np.ones((PH,PW,3),np.float32)*g
        for it in e['items']:
            dx,dy,dw,dh=it['dst']; is_back=dx>2400
            if (side=='back')!=is_back: continue
            tcx=3580.5 if is_back else 1220.0
            if is_back: w=int(dw*S*1.35); h=int(dh*S*1.35); cx=PW/2+(dx+dw/2-tcx)*S
            else: w=int(dw*S*1.6); h=int(dh*S*1.6); cx=PW/2+(dx+dw/2-tcx)*2.6
            top=int((dy-Y0)*S*(0.85 if is_back else 1.0)) + (60 if is_back else 260)
            if h>PH*0.86: k=PH*0.86/h; w=int(w*k); h=int(h*k)
            if w>PW*0.86: k=PW*0.86/w; w=int(w*k); h=int(h*k)
            a,al=layer(it,e['ground'])
            ar=np.asarray(Image.fromarray((a*255).astype(np.uint8)).resize((w,h),Image.LANCZOS)).astype(np.float32)/255
            alr=np.asarray(Image.fromarray((al*255).astype(np.uint8)).resize((w,h),Image.LANCZOS)).astype(np.float32)/255
            x0=int(cx-w/2); y0=top
            reg=cv[y0:y0+h,x0:x0+w]; reg[:]=reg*(1-alr[...,None])+ar*alr[...,None]
        Image.fromarray((cv*255).astype(np.uint8)).save(f'/home/claude/print/{names[n]}_{side}.png',dpi=(300,300))
    Image.new('RGB',(2500,2961),tuple(int(v) for v in e['ground'])).save(f'/home/claude/print/{names[n]}_sleeves-neck.png',dpi=(300,300))
    print(n,'ok')
