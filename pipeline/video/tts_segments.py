import json, base64, urllib.request, sys
K=__import__('os').environ['ELEVENLABS_API_KEY']
def go(text,out,vid='iP95p4xoKVk53GoZ742B'):
    req=urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{vid}/with-timestamps?output_format=mp3_44100_128',
        data=json.dumps({"text":text,"model_id":"eleven_v3","voice_settings":{"stability":1.0}}).encode(),headers={'xi-api-key':K,'Content-Type':'application/json'})
    d=json.load(urllib.request.urlopen(req,timeout=120))
    open(out+'.mp3','wb').write(base64.b64decode(d['audio_base64'])); json.dump(d['alignment'],open(out+'.json','w')); print('ok',out)
S={'seg1':"What your rash guard says about you. Plain black. White belt for four years.",
   'seg2':"Pink glitter. Taps you. No sorry.",
   'seg3':"Ink art. Black belt. Says nothing.",
   'end_tiktok':"Shizen. First drop soon. Comment waitlist for fifteen percent off.",
   'end_instagram':"Shizen. First drop soon. Waitlist in bio for fifteen percent off."}
for k,v in S.items(): go(v,k)
