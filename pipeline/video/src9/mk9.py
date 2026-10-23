import json, re, wave, numpy as np, subprocess
SP=1.25; G=0.16
P=[(0.05,1.89,"I'm letting 1,000+"),(1.97,2.95,"BJJ players"),(3.01,4.47,"pick my first rash guard."),(4.86,5.05,"Eight"),(5.12,5.77,"designs."),(5.97,7.26,"Japanese ink art."),(7.56,9.20,"Only one gets made first."),(9.58,11.66,"Comment your number and the word waitlist,"),(11.77,13.30,"and get 15% off.")]
w=wave.open('e44.wav'); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),np.int16)
out=[]; t=0.0; newP=[]; prev_end=0.0
for i,(a,b,txt) in enumerate(P):
    gap = a-prev_end if i else a
    keep = min(gap, G) if i else a
    # take a slice that includes 'keep' seconds of the original lead-in silence
    s0=int((a-keep)*sr); s1=int((b+ (0.25 if i==len(P)-1 else 0))*sr)
    if i: s0=max(s0,int(prev_end*sr))
    seg=x[s0:s1]; start=t+(a-s0/sr); newP.append((start,start+(b-a),txt)); out.append(seg); t+=len(seg)/sr; prev_end=b
y=np.concatenate(out)
w2=wave.open('tight.wav','wb'); w2.setnchannels(1); w2.setsampwidth(2); w2.setframerate(sr); w2.writeframes(y.tobytes()); w2.close()
subprocess.run(['ffmpeg','-loglevel','error','-y','-i','tight.wav','-filter:a',f'atempo={SP}','vo-fast.wav'],check=True)
def syl(w):
    w=w.lower().strip('.,!?')
    if w=='15%': return 4
    if w=='1,000+': return 4
    if w=='bjj': return 3
    if w=='shizen': return 2
    n=len(re.findall(r'[aeiouy]+',w))
    if w.endswith('e') and n>1 and not w.endswith('le'): n-=1
    return max(1,n)
words=[]
for a,b,txt in newP:
    ws=txt.split(); wt=[syl(q)+0.6 for q in ws]; tot=sum(wt); tt=a
    for q,k in zip(ws,wt):
        d=(b-a)*k/tot; words.append([q,round(tt/SP,3),round((tt+d)/SP,3)]); tt+=d
json.dump(words,open('words.json','w'))
print(len(y)/sr/SP, words[-1])
print(' '.join(f'{q}@{s:.2f}' for q,s,e in words))
