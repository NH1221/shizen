import json, base64, urllib.request, subprocess, wave, numpy as np, sys
K=__import__('os').environ['ELEVENLABS_API_KEY']
k,T=sys.argv[1],sys.argv[2]; SP=float(sys.argv[3]) if len(sys.argv)>3 else 1.1
req=urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/TX3LPaxmHKxFdv7VOQHJ/with-timestamps?output_format=mp3_44100_128',
    data=json.dumps({"text":T,"model_id":"eleven_multilingual_v2","voice_settings":{"stability":0.4,"similarity_boost":0.75,"style":0.35,"speed":1.15}}).encode(),headers={'xi-api-key':K,'Content-Type':'application/json'})
d=json.load(urllib.request.urlopen(req,timeout=120)); open(k+'.mp3','wb').write(base64.b64decode(d['audio_base64']))
a=d['alignment']; ch,st,en=a['characters'],a['character_start_times_seconds'],a['character_end_times_seconds']
words=[];cur='';s=None
for c,b,e in zip(ch,st,en):
    if c==' ':
        if cur: words.append([cur,s,pe]);cur=''
        continue
    if not cur: s=b
    cur+=c;pe=e
if cur: words.append([cur,s,pe])
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',k+'.mp3','-ac','1','-ar','44100',k+'_raw.wav'],check=True)
w=wave.open(k+'_raw.wav'); sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),np.int16)
G=0.22; out=[]; t=0.0; prev=words[0][1]-0.02; nw=[]
for i,(q,b,e) in enumerate(words):
    gap=b-prev; keep=min(gap,G) if i else min(b,0.2)
    seg=x[int((b-keep)*sr):int(e*sr)]; nb=t+keep; nw.append([q,nb,nb+(e-b)]); out.append(seg); t+=len(seg)/sr; prev=e
y=np.concatenate(out+[np.zeros(int(0.2*sr),np.int16)])
w2=wave.open(k+'_tight.wav','wb'); w2.setnchannels(1); w2.setsampwidth(2); w2.setframerate(sr); w2.writeframes(y.tobytes()); w2.close()
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',k+'_tight.wav','-af',f'atempo={SP}','-ac','2','-ar','48000',k+'.wav'],check=True)
W=[[q,round(b/SP,3),round(e/SP,3)] for q,b,e in nw]
json.dump(W,open(k+'.words.json','w')); print(k,len(W),W[-1][2]); print(' '.join(f'{i}:{q}@{b}' for i,(q,b,e) in enumerate(W)))
