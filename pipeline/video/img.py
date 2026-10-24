import json, base64, sys, urllib.request, io
from PIL import Image
K=open('/home/claude/gen/.gk').read().strip()
def b64(p):
    im=Image.open(p).convert('RGB'); im.thumbnail((1600,1600)); bio=io.BytesIO(); im.save(bio,'JPEG',quality=92); return base64.b64encode(bio.getvalue()).decode()
out,aspect,prompt=sys.argv[1],sys.argv[2],sys.argv[3]; refs=sys.argv[4:]
parts=[{"inline_data":{"mime_type":"image/jpeg","data":b64(r)}} for r in refs]+[{"text":prompt}]
body={"contents":[{"parts":parts}],"generationConfig":{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":aspect,"imageSize":"2K"}}}
req=urllib.request.Request('https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image:generateContent',data=json.dumps(body).encode(),headers={'x-goog-api-key':K,'Content-Type':'application/json'})
d=json.load(urllib.request.urlopen(req,timeout=180))
for p in d['candidates'][0]['content']['parts']:
    if 'inlineData' in p: open(out,'wb').write(base64.b64decode(p['inlineData']['data'])); print('ok',out); break
else: print(json.dumps(d)[:400])
