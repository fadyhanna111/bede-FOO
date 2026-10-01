import json, pathlib, time
import mlx_whisper
root=pathlib.Path(__file__).resolve().parent.parent
start=time.time()
print('Loading Whisper large v3 turbo and transcribing locally',flush=True)
r=mlx_whisper.transcribe(str(root/'meetings/2026-10-01/recordings/Bede.m4a'),path_or_hf_repo=str(root/'working/whisper-model'),verbose=True,condition_on_previous_text=False)
output=root/'meetings/2026-10-01/transcripts'
output.mkdir(parents=True,exist_ok=True)
(output/'Bede.raw.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
lines=[]
for s in r['segments']:
 t=int(s['start']); lines.append(f"[{t//60:02d}:{t%60:02d}] {s['text'].strip()}")
(output/'Bede.timestamped.txt').write_text('\n'.join(lines))
print(f'COMPLETE {len(lines)} segments in {time.time()-start:.1f}s',flush=True)
