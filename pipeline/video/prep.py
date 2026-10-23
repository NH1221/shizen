import json, subprocess, numpy as np, sys
SP=1.2; G=0.14
for n in ['tt','ig']:
    a=json.load(open(n+'.align.json')); ch=a['characters']; st=a['character_start_times_seconds']; en=a['character_end_times_seconds']
    words=[]; cur=''; s=None
    for c,b,e in zip(ch,st,en):
        if c==' ':
            if cur: words.append([cur,s,pe]); cur=''
            continue
        if not cur: s=b
        cur+=c; pe=e
    if cur: words.append([cur,s,pe])
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',n+'.mp3','-ac','1','-ar','44100',n+'.wav'],check=True)
    import wave; w=wave.open(n+'.wav'); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),np.int16)
    # cut long gaps between words
    segs=[]; t=0.0; out=[]; prev=0.0
    for i,(q,b,e) in enumerate(words):
        gap=b-prev; lead=min(gap,G) if i else min(b,0.05)
        s0=int((b-lead)*sr); s1=int(e*sr)
        seg=x[s0:s1]; nb=t+lead; out.append((q,nb,nb+(e-b))); segs.append(seg); t+=len(seg)/sr; prev=e
    segs.append(np.zeros(int(0.3*sr),np.int16))
    y=np.concatenate(segs); w2=wave.open(n+'-tight.wav','wb'); w2.setnchannels(1); w2.setsampwidth(2); w2.setframerate(sr); w2.writeframes(y.tobytes()); w2.close()
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',n+'-tight.wav','-filter:a',f'atempo={SP}',n+'-fast.wav'],check=True)
    W=[[q,round(b/SP,3),round(e/SP,3)] for q,b,e in out]
    json.dump(W,open(n+'-words.json','w')); print(n, W[-1][2], ' '.join(f'{q}@{b:.2f}' for q,b,e in W))
