import wave, numpy as np, json, re, subprocess, sys
src,out,SP=sys.argv[1],sys.argv[2],float(sys.argv[3]); segs=json.loads(sys.argv[4]); PH=json.loads(sys.argv[5]); G=float(sys.argv[6])
w=wave.open(src); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)
def syl(w):
    w=w.lower().strip('.,?!'); n=len(re.findall(r'[aeiouy]+',w))
    if w.endswith('e') and n>1 and not w.endswith('le'): n-=1
    return max(1,n)
o=[];t=0.0;words=[];pad=0.03
for i,((a,b),ph) in enumerate(zip(segs,PH)):
    if i: o.append(np.zeros(int(G*sr),np.float32)); t+=G
    seg=x[int(max(0,a-pad)*sr):int((b+pad)*sr)]; d=len(seg)/sr
    ws=ph.split(); wt=[syl(q)+0.5 for q in ws]; tot=sum(wt); tt=t+pad; span=d-2*pad
    for q,k in zip(ws,wt): dd=span*k/tot; words.append([q,tt,tt+dd]); tt+=dd
    o.append(seg); t+=d
y=np.concatenate(o+[np.zeros(int(0.15*sr),np.float32)])
w2=wave.open(out+'_tight.wav','wb'); w2.setnchannels(1); w2.setsampwidth(2); w2.setframerate(sr); w2.writeframes(np.clip(y,-32768,32767).astype(np.int16).tobytes()); w2.close()
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',out+'_tight.wav','-af',f'atempo={SP}','-ac','2','-ar','48000',out+'.wav'],check=True)
W=[[q,round(b/SP,3),round(e/SP,3)] for q,b,e in words]
json.dump(W,open(out+'.words.json','w')); print(out,len(W),round(len(y)/sr/SP,2))
