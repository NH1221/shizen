import subprocess, os, sys, shutil, json, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,30
IX='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'
V=sys.argv[1]; OUT=sys.argv[2]   # V = path prefix of VO (wav + words.json)
words=json.load(open(V+'.words.json')); WT=[w[1] for w in words]
END=words[-1][2]+1.2
TAG=words[-1][2]+0.35
GOLD={'ten.','from?'}
clips={}
def load(name):
    if name in clips: return clips[name]
    d=f'/tmp/v11_{name}'
    if not os.path.isdir(d) or not os.listdir(d):
        os.makedirs(d,exist_ok=True); subprocess.run(['ffmpeg','-loglevel','error','-i',name+'.mp4','-vf',f'fps={FPS},scale={W}:{H}:flags=lanczos',f'{d}/%05d.jpg'],check=True)
    clips[name]=[f'{d}/{x}' for x in sorted(os.listdir(d))]; return clips[name]
stills={}
def still(name):
    if name not in stills:
        im=Image.open(name).convert('RGB'); s=max(W/im.width,H/im.height); stills[name]=im.resize((int(im.width*s)+1,int(im.height*s)+1),Image.LANCZOS)
    return stills[name]
def crop(im,z,cx,cy):
    if z<=1.001: return im.resize((W,H)) if im.size!=(W,H) else im
    cw,ch=im.width/z,im.height/z; x0=min(max(0,im.width*cx-cw/2),im.width-cw); y0=min(max(0,im.height*cy-ch/2),im.height-ch)
    return im.crop((int(x0),int(y0),int(x0+cw),int(y0+ch))).resize((W,H),Image.BILINEAR)
def frame(src,t,z,push,u,cx,cy,shake):
    if src.endswith('.jpg'): im=still(src)
    else:
        fr=load(src); im=Image.open(fr[min(len(fr)-1,max(0,int(t*FPS)))]).convert('RGB')
    zz=z*(1+push*u)
    if shake:  # handheld jitter for stills
        cx+=0.004*math.sin(t*9.1)+0.003*math.sin(t*23.7); cy+=0.004*math.cos(t*7.3)+0.003*math.sin(t*19.1)
    return crop(im,zz,cx,cy)
def split(t):
    a=frame('boring',0.3+t,1.0,0,0,0.5,0.5,False); b=frame('loud',0.2+t,1.0,0,0,0.5,0.45,False)
    im=Image.new('RGB',(W,H)); hw=W//2
    im.paste(a.crop((W//4,0,W//4+hw,H)),(0,0)); im.paste(b.crop((W//4,0,W//4+hw,H)),(hw,0))
    ImageDraw.Draw(im).rectangle((hw-3,0,hw+3,H),fill=(255,255,255)); return im
# (word idx, source, src start, zoom, push, cx, cy, shake, text_y)
S=[(0,'boring',0.2,1.0,0.03,.5,.5,False,0.78),
   (6,'boring',2.6,1.4,0.04,.5,.45,False,0.78),
   (9,'loud',1.0,1.1,0.05,.5,.42,False,0.78),
   (14,'s2',1.4,1.25,0.05,.5,.42,False,0.78),
   (17,'s2',3.6,1.1,0.04,.5,.4,False,0.78),
   (20,'dragon-fixed',0.0,1.0,0.03,.5,.5,False,0.8),
   (23,'dragon-fixed',2.4,1.55,0.03,.5,.37,False,0.8)]
SCORES=[(8,'3/10',False),(11,'6/10',False),(16,'7/10',False),(23,'10/10',True)]
starts=[0.0 if i==0 else WT[i]-0.04 for i,*_ in S]
def word_at(t):
    cur=None
    for i,(w,b,e) in enumerate(words):
        if t>=b-0.03: cur=i
    if cur is None: return None,0
    return words[cur][0], t-words[cur][1]
def draw_word(im,w,age,ty):
    s=1.18-0.18*min(1,age/0.09); f=ImageFont.truetype(IX,int(128*s))
    txt=w.rstrip(',.').rstrip('.').upper(); col=(255,206,84) if w.lower().strip(',.') in GOLD or w.lower() in GOLD else (255,255,255)
    y=int(H*ty)
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).text((W//2,y+8),txt,font=f,fill=(0,0,0,170),anchor='mm')
    sh=sh.filter(ImageFilter.GaussianBlur(12)); im.paste(sh,(0,0),sh)
    ImageDraw.Draw(im).text((W//2,y),txt,font=f,fill=col,anchor='mm',stroke_width=8,stroke_fill=(0,0,0))
CM='/home/claude/fonts/Cormorant-600.ttf'
def score_at(t):
    cur=None
    for wi,txt,gold in SCORES:
        if t>=WT[wi]-0.02: cur=(txt,gold,t-WT[wi])
    # hide a score once the next subject's shot begins
    if cur:
        wi=[x for x in SCORES if x[1]==cur[0]][0][0]
        nxt=[starts[k] for k,(i,*_r) in enumerate(S) if i>wi]
        if nxt and t>=nxt[0]: return None
    return cur
def draw_score(im,txt,gold,age):
    s_=1.25-0.25*min(1,age/0.12)
    if gold: f=ImageFont.truetype(CM,int(250*s_)); col=(214,182,118)
    else: f=ImageFont.truetype(IX,int(170*s_)); col=(255,255,255)
    y=int(H*0.2)
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).text((W//2,y+10),txt,font=f,fill=(0,0,0,190),anchor='mm',features=['lnum'])
    sh=sh.filter(ImageFilter.GaussianBlur(14)); im.paste(sh,(0,0),sh)
    ImageDraw.Draw(im).text((W//2,y),txt,font=f,fill=col,anchor='mm',stroke_width=0 if gold else 8,stroke_fill=(0,0,0),features=['lnum'])
lk=Image.open('/home/claude/shizen/brand/shizen-neck-lockup-gold.png').convert('RGBA'); lk=lk.crop(lk.getbbox()); lk=lk.resize((260,int(lk.height*260/lk.width)),Image.LANCZOS)
def end_tag(im,age):
    a=min(1,age/0.25); dark=Image.new('RGB',(W,H),(10,11,14)); im=Image.blend(im,dark,0.72*a)
    l2=lk.copy(); l2.putalpha(l2.getchannel('A').point(lambda v:int(v*a))); im.paste(l2,((W-lk.width)//2,int(H*0.40)),l2)
    ImageDraw.Draw(im).text((W//2,int(H*0.40)+lk.height+60),'Founding Drop 01',font=ImageFont.truetype(CM,64),fill=(int(240*a),int(234*a),int(222*a)),anchor='mt')
    return im
tmp='/tmp/e4'; shutil.rmtree(tmp,ignore_errors=True); os.makedirs(tmp)
for n in range(int(END*FPS)):
    t=n/FPS; k=max(i for i in range(len(S)) if t>=starts[i]); _,src,s0,z,push,cx,cy,shake,ty=S[k]
    t0=starts[k]; t1=starts[k+1] if k+1<len(S) else END; u=(t-t0)/max(0.01,t1-t0)
    im=split(t-t0) if src=='SPLIT' else frame(src,s0+(t-t0),z,push,u,cx,cy,shake)
    sc=score_at(t)
    if sc and t<TAG: draw_score(im,*sc)
    w,age=word_at(t)
    if w and t<TAG: draw_word(im,w,age,ty)
    if t>=TAG: im=end_tag(im,t-TAG)
    im.save(f'{tmp}/{n:05d}.jpg',quality=92)
# ambience: quiet gym sound from the clips in order (stills use the dragon clip's room tone)
amb=[]
for k,(i,src,s0,*_r) in enumerate(S):
    t0=starts[k]; t1=starts[k+1] if k+1<len(S) else END; dur=t1-t0
    c={'SPLIT':'boring'}.get(src,src); c=c if not c.endswith('.jpg') else 'dragon-fixed'; o=f'{tmp}/a{k}.wav'
    subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',str(s0 if not src.endswith('.jpg') else 0),'-i',c+'.mp4','-af',f'apad,atrim=0:{dur:.3f}','-vn','-ac','2','-ar','48000',o],check=True); amb.append(o)
open(f'{tmp}/al.txt','w').write(''.join(f"file '{x}'\n" for x in amb))
subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i',f'{tmp}/al.txt','-c:a','pcm_s16le',f'{tmp}/amb.wav'],check=True)
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f'{tmp}/amb.wav','-i',V+'.wav','-filter_complex','[0:a]volume=0.2[a];[1:a]apad[v];[a][v]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[m]','-map','[m]','-t',f'{END:.3f}',f'{tmp}/mix.wav'],check=True)
subprocess.run(['ffmpeg','-loglevel','error','-y','-framerate',str(FPS),'-i',f'{tmp}/%05d.jpg','-i',f'{tmp}/mix.wav','-map','0:v','-map','1:a','-shortest','-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium','-c:a','aac','-b:a','192k','-movflags','+faststart',OUT],check=True)
print(OUT,round(END,2))
