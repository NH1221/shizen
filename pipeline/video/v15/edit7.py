import subprocess, os, sys, shutil, json, math, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
W,H,FPS=1080,1920,30
IX='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'; CM='/home/claude/fonts/Cormorant-600.ttf'
V=sys.argv[1]; OUT=sys.argv[2]
words=json.load(open(V+'.words.json'))
# --- insert breathing holds into the VO after given word indices
HOLDS={15:0.45,28:0.35}
w=wave.open(V+'.wav'); sr=w.getframerate(); ch=w.getnchannels(); a=np.frombuffer(w.readframes(w.getnframes()),np.int16).reshape(-1,ch)
parts=[]; prev=0; shift=0.0; newwords=[]
cuts=sorted(HOLDS.items())
for i,(q,b,e) in enumerate(words):
    newwords.append([q,b+shift,e+shift])
    if i in HOLDS:
        cut=int(min(len(a),(e+0.06)*sr)); parts.append(a[prev:cut]); parts.append(np.zeros((int(HOLDS[i]*sr),ch),np.int16)); prev=cut; shift+=HOLDS[i]
parts.append(a[prev:]); vo=np.concatenate(parts)
os.makedirs('/tmp/e7',exist_ok=True)
w2=wave.open('/tmp/e7/vo.wav','wb'); w2.setnchannels(ch); w2.setsampwidth(2); w2.setframerate(sr); w2.writeframes(vo.tobytes()); w2.close()
words=newwords; WT=[x[1] for x in words]
END=words[-1][2]+0.8
# --- shots: (word idx, clip, src, zoom0, zoom1, cx0, cy0, cx1, cy1, premium, sweep)
S=[(0,'P3',5.0,1.15,1.2,.5,.42,.5,.42,False,False),
   (6,'P4',5.6,1.55,1.6,.42,.62,.42,.62,False,False),
   (8,'P5',0.2,1.2,1.25,.6,.6,.6,.6,False,False),
   (11,'P1',0.6,2.0,2.25,.5,.26,.5,.27,True,15),
   (16,'P1',2.0,1.95,2.1,.34,.44,.40,.44,True,False),
   (20,'P1',3.0,1.95,2.1,.66,.46,.60,.46,True,False),
   (25,'P1',6.4,1.9,1.0,.5,.36,.5,.5,True,False),
   (29,'END',0,1,1,.5,.5,.5,.5,True,False)]
starts=[0.0 if i==0 else WT[i]-0.04 for i,*_ in S]
CHUNK={11:"THAT'S WHY",13:'WE MADE',15:'SHIZEN',16:'QUALITY',17:'JAPANESE INK ART',20:'RASH GUARDS',22:'THAT FEEL',24:'AS GOOD',26:'AS THEY LOOK',33:'WOULD YOU',35:'WEAR IT?'}
GOLDC={'SHIZEN','JAPANESE INK ART','WEAR IT?'}
HIDE=range(29,33)
clips={}
def load(name):
    if name in clips: return clips[name]
    d=f'/tmp/v15_{name}'
    if not os.path.isdir(d) or not os.listdir(d):
        os.makedirs(d,exist_ok=True); subprocess.run(['ffmpeg','-loglevel','error','-i',name+'.mp4','-vf',f'fps={FPS},scale={W}:{H}:flags=lanczos',f'{d}/%05d.png'],check=True)
    clips[name]=[f'{d}/{x}' for x in sorted(os.listdir(d))]; return clips[name]
def ease(u): return 0.5-0.5*math.cos(math.pi*min(1,max(0,u)))
def frame(src,t,z,cx,cy):
    fr=load(src); im=Image.open(fr[min(len(fr)-1,max(0,int(t*FPS)))]).convert('RGB')
    if z>1.001:
        cw,ch_=W/z,H/z; x0=min(max(0,W*cx-cw/2),W-cw); y0=min(max(0,H*cy-ch_/2),H-ch_)
        im=im.crop((int(x0),int(y0),int(x0+cw),int(y0+ch_))).resize((W,H),Image.LANCZOS)
        im=im.filter(ImageFilter.UnsharpMask(radius=2,percent=60,threshold=2))
    return im
rng=np.random.default_rng(7)
GRAIN=[(rng.standard_normal((H//2,W//2))*7).astype(np.float32) for _ in range(6)]
def premium(im,n,sweep_u=None):
    im=ImageEnhance.Contrast(im).enhance(1.06); im=ImageEnhance.Color(im).enhance(0.95)
    a=np.asarray(im).astype(np.float32)
    a[...,0]*=1.03; a[...,2]*=0.96   # warm
    g=np.kron(GRAIN[n%6],np.ones((2,2)))[:H,:W]; a+=g[...,None]
    if sweep_u is not None and 0<=sweep_u<=1:   # diagonal light sweep
        yy,xx=np.mgrid[0:H,0:W]; pos=(xx+yy*0.55)/(W+H*0.55); c=-0.2+1.4*sweep_u
        band=np.exp(-((pos-c)/0.05)**2)*0.28; a+=band[...,None]*np.array([255,235,190])
    # vignette
    yy,xx=np.mgrid[0:H,0:W]; v=1-0.28*(((xx-W/2)/(W/2))**2+((yy-H/2)/(H/2))**2)
    a*=np.clip(v,0.6,1)[...,None]
    im=Image.fromarray(np.clip(a,0,255).astype(np.uint8))
    d=ImageDraw.Draw(im); bh=int(H*0.045); d.rectangle((0,0,W,bh),fill=(0,0,0)); d.rectangle((0,H-bh,W,H),fill=(0,0,0))
    return im
lk=Image.open('/home/claude/shizen/brand/shizen-neck-lockup-gold.png').convert('RGBA'); lk=lk.crop(lk.getbbox()); lk=lk.resize((300,int(lk.height*300/lk.width)),Image.LANCZOS)
def endcard(t,n):
    base=frame('P1',7.6,1.0,.5,.5); base=Image.blend(base,Image.new('RGB',(W,H),(8,8,10)),0.7)
    a=min(1,t/0.3); im=base
    l2=lk.copy(); l2.putalpha(l2.getchannel('A').point(lambda v:int(v*a))); im.paste(l2,((W-lk.width)//2,int(H*0.33)),l2)
    d=ImageDraw.Draw(im); d.text((W//2,int(H*0.33)+lk.height+60),'Founding Drop 01',font=ImageFont.truetype(CM,72),fill=(int(240*a),int(234*a),int(222*a)),anchor='mt',features=['lnum'])
    return premium(im,n)
def caption_at(t):
    cur=None
    for i,(q,b,e) in enumerate(words):
        if t>=b-0.03: cur=i
    if cur is None or cur in HIDE: return None,0
    if cur>=11:
        j=cur
        while j not in CHUNK and j>11: j-=1
        if j in CHUNK: return CHUNK[j], t-words[j][1]
        return None,0
    return words[cur][0].rstrip(',.').upper(), t-words[cur][1]
def draw_caption(im,txt,age,ty):
    s=1.15-0.15*min(1,age/0.1); f=ImageFont.truetype(IX,int(118*s))
    while ImageDraw.Draw(im).textlength(txt,font=f)>W*0.86: f=ImageFont.truetype(IX,int(f.size*0.92))
    col=(255,206,84) if txt in GOLDC else (255,255,255); y=int(H*ty)
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).text((W//2,y+8),txt,font=f,fill=(0,0,0,170),anchor='mm')
    sh=sh.filter(ImageFilter.GaussianBlur(12)); im.paste(sh,(0,0),sh)
    ImageDraw.Draw(im).text((W//2,y),txt,font=f,fill=col,anchor='mm',stroke_width=8,stroke_fill=(0,0,0))
tmp='/tmp/e7/f'; shutil.rmtree(tmp,ignore_errors=True); os.makedirs(tmp)
for n in range(int(END*FPS)):
    t=n/FPS; k=max(i for i in range(len(S)) if t>=starts[i]); _,src,s0,z0,z1,cx0,cy0,cx1,cy1,prem,sweep=S[k]
    t0=starts[k]; t1=starts[k+1] if k+1<len(S) else END; u=ease((t-t0)/max(0.01,t1-t0))
    if src=='END': im=endcard(t-t0,n)
    else:
        im=frame(src,s0+(t-t0),z0+(z1-z0)*u,cx0+(cx1-cx0)*u,cy0+(cy1-cy0)*u)
        if prem: im=premium(im,n,((t-(WT[sweep]-0.05))/0.9) if sweep else None)
    # subtle film flash on every cut (CapCut-style warm bloom peaking on the cut)
    near=[t-c for c in starts[3:] if -0.07<=t-c<=0.13]
    if near:
        dt=near[0]; amt=0.62*(1-abs(dt)/0.07) if dt<0 else 0.62*max(0,1-dt/0.13)
        if amt>0:
            bloom=im.filter(ImageFilter.GaussianBlur(18))
            im=Image.blend(im,Image.blend(bloom,Image.new('RGB',(W,H),(255,246,228)),0.6),amt)
    txt,age=caption_at(t)
    if txt: draw_caption(im,txt,age,0.8 if prem else 0.5)
    im.save(f'{tmp}/{n:05d}.jpg',quality=93)
# --- SFX mix
def place(lst):
    total=int(END*48000); mix=np.zeros((total,2),np.float32)
    for f,at,g in lst:
        w_=wave.open(f); x=np.frombuffer(w_.readframes(w_.getnframes()),np.int16).reshape(-1,2).astype(np.float32)/32767
        i=int(max(0,at)*48000); j=min(total,i+len(x)); mix[i:j]+=x[:j-i]*g
    return mix
T11=starts[3]; sf=[('whoosh.wav',T11-0.4,0.04),('hit.wav',T11-0.02,0.3),('shimmer.wav',WT[15]-0.05,0.15)]
sf.append(('hit.wav',starts[-1]-0.02,0.22))
mix=place(sf); sw=wave.open('/tmp/e7/sfx.wav','wb'); sw.setnchannels(2); sw.setsampwidth(2); sw.setframerate(48000); sw.writeframes((np.clip(mix,-1,1)*32767).astype(np.int16).tobytes()); sw.close()
subprocess.run(['ffmpeg','-loglevel','error','-y','-i','/tmp/e7/vo.wav','-i','/tmp/e7/sfx.wav','-filter_complex','[0:a]aresample=48000,apad[v];[1:a]volume=1.0[s];[v][s]amix=inputs=2:duration=longest:normalize=0,loudnorm=I=-14:TP=-1.5[m]','-map','[m]','-t',f'{END:.3f}','/tmp/e7/mix.wav'],check=True)
subprocess.run(['ffmpeg','-loglevel','error','-y','-framerate',str(FPS),'-i',f'{tmp}/%05d.jpg','-i','/tmp/e7/mix.wav','-map','0:v','-map','1:a','-shortest','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','-c:a','aac','-b:a','192k','-movflags','+faststart',OUT],check=True)
print(OUT,round(END,2))
