import numpy as np, wave, sys
def load(p):
    w=wave.open(p); x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)/32768; return x,w.getframerate()
def segs(x,sr,th=-40,gap=0.1):
    hop=int(sr*0.01); n=len(x)//hop; e=np.array([np.sqrt(np.mean(x[i*hop:(i+1)*hop]**2))+1e-9 for i in range(n)]); db=20*np.log10(e/e.max())
    on=db>th; out=[]; s=None
    for i,v in enumerate(on):
        if v and s is None: s=i
        if not v and s is not None: out.append([s/100,i/100]); s=None
    if s is not None: out.append([s/100,n/100])
    m=[]
    for a,b in out:
        if m and a-m[-1][1]<gap: m[-1][1]=b
        else: m.append([a,b])
    return [s for s in m if s[1]-s[0]>0.05], db
def f0(x,sr):
    fl=int(sr*0.04); hop=int(sr*0.01); res=[]
    for i in range(0,len(x)-fl,hop):
        f=x[i:i+fl]*np.hanning(fl)
        if np.sqrt(np.mean(f**2))<0.02: continue
        ac=np.correlate(f,f,'full')[fl-1:]; lo,hi=int(sr/300),int(sr/70)
        k=lo+np.argmax(ac[lo:hi])
        if ac[k]/ac[0]>0.45: res.append(sr/k)
    return np.array(res)
for p in sys.argv[1:]:
    x,sr=load(p); s,db=segs(x,sr); f=f0(x,sr); st=12*np.log2(f/np.median(f))
    print(p, 'dur %.2f'%(len(x)/sr), 'speech %.2f'%sum(b-a for a,b in s), 'F0 med %.0f'%np.median(f), 'semitone sd %.2f'%st.std(), 'p5-p95 %.1f'%(np.percentile(st,95)-np.percentile(st,5)), 'nseg',len(s))
    print('  ', ' '.join('%.2f-%.2f'%(a,b) for a,b in s))
