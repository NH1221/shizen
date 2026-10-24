import cv2, numpy as np, glob, sys
from PIL import Image, ImageDraw, ImageFont
src_dir,out_mp4,clip=sys.argv[1],sys.argv[2],sys.argv[3]
cx0,cy0,D=int(sys.argv[4]),int(sys.argv[5]),float(sys.argv[6])  # circle centre and diameter in frame 0
fs=sorted(glob.glob(src_dir+'/*.png')); f0=cv2.imread(fs[0]); H,W=f0.shape[:2]
g0=cv2.cvtColor(f0,cv2.COLOR_BGR2GRAY); r=int(D*1.4)
tpl=g0[cy0-r:cy0+r, cx0-r:cx0+r]
# clean lockup at 8x then downscale
S=8; md=int(D*S); fnt=ImageFont.truetype('/home/claude/fonts/Cormorant-600.ttf',int(D*S*0.62))
tw=int(ImageDraw.Draw(Image.new('L',(1,1))).textlength('SHIZEN',font=fnt)); Wl=max(md,tw)+20; Hl=md+int(D*S*0.95)
L=Image.new('L',(Wl,Hl),0); d=ImageDraw.Draw(L); c=Wl/2; R=md/2; k=R/330
def disk(x,y,rr,f): d.ellipse((c+(x-rr)*k,R+(y-rr)*k,c+(x+rr)*k,R+(y+rr)*k),fill=f)
M=Image.new('L',(md,md),0); dm=ImageDraw.Draw(M); cc=md/2
def dk(x,y,rr,f): dm.ellipse((cc+(x-rr)*k,cc+(y-rr)*k,cc+(x+rr)*k,cc+(y+rr)*k),fill=f)
dm.pieslice((cc-300*k,cc-300*k,cc+300*k,cc+300*k),-90,90,fill=255); dk(0,150,150,255); dk(0,-150,150,0); dk(0,-150,40,255); dk(0,150,40,0)
dm.ellipse((cc-330*k,cc-330*k,cc+330*k,cc+330*k),outline=255,width=max(2,int(14*k)))
M=M.rotate(30,resample=Image.BICUBIC); L.paste(M,(int(c-md/2),0))
d.text((c,md+int(D*S*0.18)),'SHIZEN',font=fnt,fill=255,anchor='mt')
lw,lh=int(Wl/S),int(Hl/S); A=np.asarray(L.resize((lw,lh),Image.LANCZOS)).astype(np.float32)/255
# gold colour sampled from frame 0 circle
hsv=cv2.cvtColor(f0[cy0-r:cy0+r,cx0-r:cx0+r],cv2.COLOR_BGR2HSV)
gm=(hsv[...,0]>12)&(hsv[...,0]<35)&(hsv[...,1]>60)&(hsv[...,2]>110)
gold=np.median(f0[cy0-r:cy0+r,cx0-r:cx0+r][gm],axis=0)
pos=[]; px,py=cx0,cy0
for f in fs:
    im_=cv2.imread(f); s_=45
    win=im_[py-s_:py+s_, px-s_:px+s_]; hv=cv2.cvtColor(win,cv2.COLOR_BGR2HSV)
    gm_=((hv[...,0]>10)&(hv[...,0]<38)&(hv[...,1]>45)&(hv[...,2]>95)).astype(np.uint8)
    n_,l_,st_,c_=cv2.connectedComponentsWithStats(gm_)
    best=None
    for j in range(1,n_):
        if 120<st_[j,4]<900:
            dd=(c_[j][0]-s_)**2+(c_[j][1]-s_)**2
            if best is None or dd<best[0]: best=(dd,c_[j])
    if best is not None: px,py=int(round(px-s_+best[1][0])),int(round(py-s_+best[1][1]))
    pos.append((px,py))
P=np.array(pos,np.float32); P=cv2.GaussianBlur(P.reshape(-1,1,2),(1,5),0).reshape(-1,2) if len(P)>5 else P
for i,f in enumerate(fs):
    im=cv2.imread(f); x,y=P[i]; x,y=int(round(x)),int(round(y))
    # remove old logo: inpaint gold-ish pixels in the lockup box
    bx0,by0=x-lw//2-22,y-int(D/2)-14; bx1,by1=x+lw//2+22,y-int(D/2)+lh+14
    box=im[by0:by1,bx0:bx1]; hv=cv2.cvtColor(box,cv2.COLOR_BGR2HSV)
    fab=np.median(box.reshape(-1,3),axis=0)
    diff=np.linalg.norm(box.astype(np.float32)-fab,axis=2)>18
    mk=cv2.dilate(diff.astype(np.uint8),np.ones((5,5),np.uint8))
    im[by0:by1,bx0:bx1]=cv2.inpaint(box,mk,3,cv2.INPAINT_TELEA)
    # paste clean lockup with local shading
    ox,oy=x-lw//2,y-int(D/2)
    reg=im[oy:oy+lh,ox:ox+lw].astype(np.float32); Lm=reg.mean(2,keepdims=True); sh=np.clip(Lm/max(Lm.mean(),1),0.8,1.15)
    col=np.clip(gold[None,None,:]*sh,0,255); a=cv2.GaussianBlur(A,(0,0),0.6)[...,None]*0.95
    im[oy:oy+lh,ox:ox+lw]=(reg*(1-a)+col*a).astype(np.uint8)
    cv2.imwrite(f,im)
print('tracked',len(fs),'lockup',lw,lh)
import subprocess
subprocess.run(['ffmpeg','-loglevel','error','-y','-framerate','30','-i',src_dir+'/%04d.png','-i',clip,'-map','0:v','-map','1:a?','-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-c:a','copy','-shortest',out_mp4],check=True)
