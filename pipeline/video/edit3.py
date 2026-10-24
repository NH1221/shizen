import subprocess, os, sys, shutil, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,30
IX='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'; CM='/home/claude/fonts/Cormorant-600.ttf'
plat=sys.argv[1]; V='/home/claude/vid/vo/'
words=json.load(open(V+f'full_{plat}.words.json')); WT=[w[1] for w in words]
ENDCARD=words[-1][2]+0.45
END=ENDCARD+1.1
GOLD={'says','you?','asian','dragon','nothing','prove','waitlist','15%'}
DISP={'fifteen':'15%','percent':None}
clips={}
def load(name):
    if name in clips: return clips[name]
    d=f'/tmp/f_{name}'
    if not os.path.isdir(d) or not os.listdir(d):
        os.makedirs(d,exist_ok=True); subprocess.run(['ffmpeg','-loglevel','error','-i',name+'.mp4','-vf',f'fps={FPS},scale={W}:{H}:flags=lanczos',f'{d}/%05d.jpg'],check=True)
    clips[name]=[f'{d}/{x}' for x in sorted(os.listdir(d))]; return clips[name]
def frame(name,t,zoom=1.0,push=0.0,u=0.0,cy=0.5):
    fr=load(name); i=min(len(fr)-1,max(0,int(t*FPS))); im=Image.open(fr[i]).convert('RGB'); z=zoom*(1+push*u)
    if z>1.001:
        cw,ch=W/z,H/z; x0=(W-cw)/2; y0=max(0,min(H-ch,H*cy-ch/2)); im=im.crop((int(x0),int(y0),int(x0+cw),int(y0+ch))).resize((W,H),Image.BILINEAR)
    return im
S=[(0,'s2',1.7,1.30,0.08,0.45),(2,'s1',2.7,1.25,0.08,0.4),(4,'s4',2.0,1.15,0.05,0.4),
   (7,'s1',0.2,1.05,0.06,0.45),(9,'s1',2.4,1.25,0.06,0.4),
   (13,'s2',0.3,1.05,0.06,0.45),(15,'s2',1.6,1.30,0.08,0.45),(17,'s2',3.6,1.1,0.06,0.4),
   (20,'s3',0.4,1.0,0.05,0.5),(22,'s4',0.3,1.05,0.10,0.4),
   (27,'TRI',0,1,0,0.5),(-1,'END',0,1,0,0.5)]
starts=[(ENDCARD if i==-1 else WT[i]-0.05 if i else 0.0) for i,*_ in S]
def tri(t):
    im=Image.new('RGB',(W,H)); sw=W//3
    for k,(n,src) in enumerate([('s1',2.6),('s2',3.8),('s3',1.0)]):
        f=frame(n,src+t*0.6); im.paste(f.crop(((W-sw)//2,0,(W-sw)//2+sw,H)),(k*sw,0))
    d=ImageDraw.Draw(im)
    for k in (1,2): d.rectangle((k*sw-3,0,k*sw+3,H),fill=(12,13,16))
    return im
lk=Image.open('/home/claude/shizen/brand/shizen-neck-lockup-gold.png').convert('RGBA'); lk=lk.crop(lk.getbbox()); lk=lk.resize((300,int(lk.height*300/lk.width)),Image.LANCZOS)
def endcard(t):
    im=Image.new('RGB',(W,H),(12,13,16)); a=min(1,t/0.2)
    l2=lk.copy(); l2.putalpha(l2.getchannel('A').point(lambda v:int(v*a))); im.paste(l2,((W-lk.width)//2,330),l2)
    ImageDraw.Draw(im).text((W//2,330+lk.height+50),'first drop soon',font=ImageFont.truetype(CM,64),fill=(240,234,222),anchor='mt')
    return im
def word_at(t):
    cur=None
    for i,(w,b,e) in enumerate(words):
        if t>=b-0.03: cur=i
    if cur is None: return None,0
    if t>ENDCARD: return None,0
    j=cur
    while j>0 and DISP.get(words[j][0].lower().strip('.,?'),'x') is None: j-=1
    w=words[j][0]; w=DISP.get(w.lower().strip('.,?'),w) or w
    return w, t-words[j][1]
def draw_word(im,w,age):
    s=1.18-0.18*min(1,age/0.09); f=ImageFont.truetype(IX,int(132*s))
    txt=w.rstrip(',.').upper(); col=(255,206,84) if w.lower().strip(',.?') in GOLD else (255,255,255)
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).text((W//2,H//2+8),txt,font=f,fill=(0,0,0,170),anchor='mm')
    sh=sh.filter(ImageFilter.GaussianBlur(12)); im.paste(sh,(0,0),sh)
    ImageDraw.Draw(im).text((W//2,H//2),txt,font=f,fill=col,anchor='mm',stroke_width=8,stroke_fill=(0,0,0))
tmp=f'/tmp/e3_{plat}'; shutil.rmtree(tmp,ignore_errors=True); os.makedirs(tmp)
for n in range(int(END*FPS)):
    t=n/FPS; k=max(i for i in range(len(S)) if t>=starts[i]); _,clip,src,z,push,cy=S[k]
    t0=starts[k]; t1=starts[k+1] if k+1<len(S) else END; u=(t-t0)/max(0.01,t1-t0)
    im=tri(t-t0) if clip=='TRI' else endcard(t-t0) if clip=='END' else frame(clip,src+(t-t0),z,push,u,cy)
    w,age=word_at(t)
    if w: draw_word(im,w,age)
    im.save(f'{tmp}/{n:05d}.jpg',quality=92)
amb=[]
for k,(i,clip,src,*_r) in enumerate(S):
    t0=starts[k]; t1=starts[k+1] if k+1<len(S) else END; dur=t1-t0
    c=clip if clip not in ('TRI','END') else 's3'; o=f'{tmp}/amb{k}.wav'
    subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',str(src if clip not in('TRI','END') else 0),'-i',c+'.mp4','-af',f'apad,atrim=0:{dur:.3f}','-vn','-ac','2','-ar','48000',o],check=True); amb.append(o)
open(f'{tmp}/al.txt','w').write(''.join(f"file '{x}'\n" for x in amb))
subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i',f'{tmp}/al.txt','-c:a','pcm_s16le',f'{tmp}/amb.wav'],check=True)
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f'{tmp}/amb.wav','-i',V+f'full_{plat}.wav','-filter_complex','[0:a]volume=0.18[a];[1:a]apad[v];[a][v]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[m]','-map','[m]','-t',f'{END:.3f}',f'{tmp}/mix.wav'],check=True)
out=f'/home/claude/vid/Shizen-rashguard-says-{plat}.mp4'
subprocess.run(['ffmpeg','-loglevel','error','-y','-framerate',str(FPS),'-i',f'{tmp}/%05d.jpg','-i',f'{tmp}/mix.wav','-map','0:v','-map','1:a','-shortest','-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium','-c:a','aac','-b:a','192k','-movflags','+faststart',out],check=True)
print(out,round(END,2))
