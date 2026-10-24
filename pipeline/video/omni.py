import json, base64, sys, urllib.request, io
from PIL import Image
K=open('/home/claude/gen/.gk').read().strip()
out,prompt=sys.argv[1],sys.argv[2]; img=sys.argv[3] if len(sys.argv)>3 else None
if img:
    im=Image.open(img).convert('RGB'); im.thumbnail((1080,1920)); bio=io.BytesIO(); im.save(bio,'JPEG',quality=92)
    inp=[{"type":"image","data":base64.b64encode(bio.getvalue()).decode(),"mime_type":"image/jpeg"},{"type":"text","text":prompt}]
else: inp=prompt
body={"model":"gemini-omni-1.1-flash","input":inp,"response_format":{"type":"video","aspect_ratio":"9:16","resolution":__import__("os").environ.get("RES","720p")}}
req=urllib.request.Request('https://generativelanguage.googleapis.com/v1beta/interactions',data=json.dumps(body).encode(),headers={'x-goog-api-key':K,'Content-Type':'application/json'})
try: d=json.load(urllib.request.urlopen(req,timeout=600))
except urllib.error.HTTPError as e: print('HTTP',e.code,e.read()[:800].decode()); sys.exit(1)
json.dump({k:v for k,v in d.items() if k!='steps'},open(out+'.meta.json','w'))
for st in d.get('steps',[]):
    if st.get('type')=='model_output':
        for c in st.get('content',[]):
            if c.get('type')=='video':
                open(out,'wb').write(base64.b64decode(c['data'])); print('saved',out,d.get('usage')); sys.exit(0)
print('no video',json.dumps(d)[:800])
