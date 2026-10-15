import sys, json, soundfile as sf
from kokoro_onnx import Kokoro
d=sys.argv[1]; voice=sys.argv[2]
import os; T=os.environ['TTS']; k=Kokoro(T+'/kokoro-v1.0.onnx', T+'/voices-v1.0.bin')
lines=json.load(open(d+'/lines.json')); out=[]
for i,t in enumerate(lines):
    a,sr=k.create(t, voice=voice, speed=1.0, lang='en-us'); sf.write(f'{d}/l{i}.wav',a,sr); out.append(round(len(a)/sr,2))
print(out)
