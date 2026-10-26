import numpy as np, wave
SR=48000
def save(name,y):
    y=np.clip(y,-1,1); w=wave.open(name,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    s=(np.stack([y,y],1)*32767).astype(np.int16); w.writeframes(s.tobytes()); w.close()
rng=np.random.default_rng(1)
def lowpass(x,a): 
    y=np.zeros_like(x); acc=0.0
    for i in range(len(x)): acc+=a[i]*(x[i]-acc); y[i]=acc
    return y
# whoosh: noise with sweeping lowpass and swell
n=int(0.7*SR); t=np.linspace(0,1,n); env=np.sin(np.pi*t)**1.5
a=0.01+0.25*np.sin(np.pi*t)**2
save('whoosh.wav',0.9*env*lowpass(rng.standard_normal(n),a)*3)
# soft whoosh
n=int(0.45*SR); t=np.linspace(0,1,n); env=np.sin(np.pi*t)**2; a=0.01+0.12*np.sin(np.pi*t)**2
save('whoosh_soft.wav',0.5*env*lowpass(rng.standard_normal(n),a)*3)
# deep hit: sub sine pitch drop + soft click
n=int(1.6*SR); t=np.arange(n)/SR; f=42+30*np.exp(-t*8); ph=2*np.pi*np.cumsum(f)/SR
hit=np.sin(ph)*np.exp(-t*2.6)*0.95+0.25*rng.standard_normal(n)*np.exp(-t*60)
save('hit.wav',hit)
# shimmer: bell partials
n=int(1.8*SR); t=np.arange(n)/SR; y=np.zeros(n)
for fr,amp,d in [(1568,0.3,2.2),(2093,0.25,2.6),(2637,0.18,3.0),(3136,0.12,3.4),(4186,0.08,4.0)]:
    y+=amp*np.sin(2*np.pi*fr*t)*np.exp(-t*d)
y*=np.minimum(1,t/0.01); save('shimmer.wav',0.6*y)
print('ok')
