import json, base64, sys, urllib.request
K=__import__("os").environ["ELEVENLABS_API_KEY"]
def go(text, out, vid='iP95p4xoKVk53GoZ742B'):
    req=urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{vid}/with-timestamps?output_format=mp3_44100_128',
        data=json.dumps({"text":text,"model_id":"eleven_v3","voice_settings":{"stability":1.0}}).encode(),
        headers={'xi-api-key':K,'Content-Type':'application/json'})
    d=json.load(urllib.request.urlopen(req))
    open(out+'.mp3','wb').write(base64.b64decode(d['audio_base64']))
    json.dump(d['alignment'],open(out+'.align.json','w'))
BODY="What's your game? Pressure passer. Guard player. Fundamentals. Never taps. Wrestler. Scrambler. Leg locker. Flow roller. "
go(BODY+"Comment your number, plus waitlist. Fifteen percent off when we drop.",'tt')
go(BODY+"Join the waitlist, link in bio. Fifteen percent off when we drop.",'ig')
