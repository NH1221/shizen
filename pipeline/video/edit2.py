import subprocess, os, sys, shutil, glob, json
from PIL import Image, ImageDraw, ImageFont
W,H,FPS=1080,1920,30
IB='/usr/share/fonts/opentype/inter/Inter-Bold.otf'; IX='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'; CM='/home/claude/fonts/Cormorant-600.ttf'
V='/home/claude/vid/vo/'
def wj(k): return json.load(open(V+k+'.words.json'))
# clip, in, out, vo segment, vo offset in scene, display words (label, punch)
CLIPS=[('s1.mp4',0.0,4.0,'seg1',0.05,['what your rash guard says about you','plain black','white belt for 4 years']),
       ('s2.mp4',0.2,4.2,'seg2',0.35,[None,'pink glitter','taps you. no sorry.']),
       ('s3.mp4',0.0,4.2,'seg3',0.35,[None,'ink art','black belt. says nothing.'])]
def pill(im,cx,y,s,f,bg,fg,pad=(30,16),r=22):
    d=ImageDraw.Draw(im,'RGBA'); w=d.textlength(s,font=f); asc,desc=f.getmetrics(); h=asc+desc
    d.rounded_rectangle((cx-w/2-pad[0],y,cx+w/2+pad[0],y+h+2*pad[1]),r,fill=bg)
    d.text((cx,y+pad[1]),s,font=f,fill=fg,anchor='mt'); return y+h+2*pad[1]
def shown(words,times,t):  # words revealed by time t
    return ' '.join(w for w,ts in zip(words,times) if t>=ts-0.04)
def build(plat):
    tmp=f'/tmp/ed2_{plat}'; shutil.rmtree(tmp,ignore_errors=True); os.makedirs(tmp); n=0
    ft=ImageFont.truetype(IX,46); fl=ImageFont.truetype(IX,64); fs=ImageFont.truetype(IX,56)
    title=CLIPS[0][5][0].split(); amb=[]; vo=[]; t_abs=0.0
    for ci,(f,a,b,seg,off,txts) in enumerate(CLIPS):
        ww=wj(seg); times=[x[1]+off for x in ww]
        if ci==0: tt_title=times[:7]; rest=times[7:]
        else: rest=times
        lab=txts[1].split(); pun=txts[2].split(); lt=rest[:len(lab)]; pt=rest[len(lab):len(lab)+len(pun)]
        cd=f'{tmp}/c{ci}'; os.makedirs(cd)
        subprocess.run(['ffmpeg','-loglevel','error','-ss',str(a),'-to',str(b),'-i',f,'-vf',f'fps={FPS},scale={W}:{H}:flags=lanczos',f'{cd}/%05d.png'],check=True)
        subprocess.run(['ffmpeg','-loglevel','error','-ss',str(a),'-to',str(b),'-i',f,'-vn','-ac','2','-ar','48000',f'{tmp}/a{ci}.wav'],check=True); amb.append(f'{tmp}/a{ci}.wav')
        vo.append((V+seg+'.wav',t_abs+off))
        frames=sorted(glob.glob(cd+'/*.png'))
        for i,p in enumerate(frames):
            t=i/FPS; im=Image.open(p).convert('RGB')
            tl=shown(title,tt_title,t+t_abs) if True else ''
            y=96
            if tl: y=pill(im,W//2,96,tl,ft,(255,255,255,240),(15,15,18),pad=(26,12),r=18)
            gold=ci==2
            if pt and t>=pt[0]-0.04: line=shown(pun,pt,t); bg=(15,15,18,220); fg=(214,182,118) if gold else (255,255,255); fnt=fs
            else: line=shown(lab,lt,t); bg=(214,182,118,245) if gold else (255,255,255,245); fg=(15,15,18); fnt=fl
            if line: pill(im,W//2,y+16,line,fnt,bg,fg)
            im.save(f'{tmp}/{n:05d}.jpg',quality=93); n+=1
        t_abs+=len(frames)/FPS
    # end card synced to VO
    ek='end_'+plat; ew=wj(ek); off=0.25; et=[x[1]+off for x in ew]; END=ew[-1][2]+off+0.7
    vo.append((V+ek+'.wav',t_abs+off))
    lk=Image.open('/home/claude/shizen/brand/shizen-neck-lockup-gold.png').convert('RGBA'); lk=lk.crop(lk.getbbox()); s=380/lk.width; lk=lk.resize((380,int(lk.height*s)),Image.LANCZOS)
    ctaw=["comment","'waitlist'","for","15%","off"] if plat=='tiktok' else ["waitlist","in","bio","for","15%","off"]
    cts=et[4:4+len(ctaw)] if plat=='tiktok' else et[4:4+len(ctaw)]
    if len(cts)<len(ctaw): cts=cts+[cts[-1]]*(len(ctaw)-len(cts))
    for i in range(int(END*FPS)):
        t=i/FPS; im=Image.new('RGB',(W,H),(12,13,16)); a=min(1,i/6)
        l2=lk.copy(); l2.putalpha(l2.getchannel('A').point(lambda v:int(v*a))); im.paste(l2,((W-lk.width)//2,560),l2); d=ImageDraw.Draw(im)
        fd=shown(['First','drop','soon.'],et[1:4],t)
        if fd: d.text((W//2,560+lk.height+90),fd,font=ImageFont.truetype(CM,80),fill=(240,234,222),anchor='mt')
        c=shown(ctaw,cts,t)
        if c: d.text((W//2,560+lk.height+220),c,font=ImageFont.truetype(IB,52),fill=(214,182,118),anchor='mt')
        im.save(f'{tmp}/{n:05d}.jpg',quality=93); n+=1
    total=n/FPS
    subprocess.run(['ffmpeg','-loglevel','error','-y','-f','lavfi','-t',str(END),'-i','anullsrc=r=48000:cl=stereo',f'{tmp}/aend.wav'],check=True); amb.append(f'{tmp}/aend.wav')
    open(f'{tmp}/al.txt','w').write(''.join(f"file '{x}'\n" for x in amb))
    subprocess.run(['ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i',f'{tmp}/al.txt','-c:a','pcm_s16le',f'{tmp}/amb.wav'],check=True)
    ins=['-i',f'{tmp}/amb.wav']; fc='[0:a]volume=0.22[am];'; labels=['[am]']
    for j,(pth,st) in enumerate(vo):
        ins+=['-i',pth]; ms=int(st*1000); fc+=f'[{j+1}:a]adelay={ms}|{ms},volume=1.0[v{j}];'; labels.append(f'[v{j}]')
    fc+=''.join(labels)+f'amix=inputs={len(labels)}:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[mix]'
    subprocess.run(['ffmpeg','-loglevel','error','-y',*ins,'-filter_complex',fc,'-map','[mix]','-t',str(total),f'{tmp}/mix.wav'],check=True)
    out=f'/home/claude/vid/Shizen-rashguard-says-{plat}.mp4'
    subprocess.run(['ffmpeg','-loglevel','error','-y','-framerate',str(FPS),'-i',f'{tmp}/%05d.jpg','-i',f'{tmp}/mix.wav','-map','0:v','-map','1:a','-shortest','-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','medium','-c:a','aac','-b:a','192k','-movflags','+faststart',out],check=True)
    print(out,round(total,2))
build(sys.argv[1])
