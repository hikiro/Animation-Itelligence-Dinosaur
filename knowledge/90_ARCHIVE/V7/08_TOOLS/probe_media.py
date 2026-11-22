#!/usr/bin/env python3
"""Future-chat tool: probe an ACTUAL video and optionally make a QC contact sheet.

This script reports technical media metadata ONLY; it cannot decide whether acting is believable.
Requires ffprobe; optional ffmpeg for frame sampling. Example:
    python 08_TOOLS/probe_media.py /absolute/path/scene.mp4 --sample-every 0.5 --output qa
"""
import argparse, subprocess, json, shutil, sys
from pathlib import Path

ap=argparse.ArgumentParser()
ap.add_argument('media', help='Existing file to probe')
ap.add_argument('--sample-every', type=float, default=0.0, help='Seconds between evidence frames (0 disables)')
ap.add_argument('--output', default=None, help='Optional directory for frame evidence')
a=ap.parse_args()
p=Path(a.media).expanduser().resolve()
if not p.is_file():
    sys.exit(f'BLOCKED: actual media not found: {p}')
if not shutil.which('ffprobe'):
    sys.exit('BLOCKED: ffprobe unavailable')
cmd=['ffprobe','-v','error','-show_entries','format=filename,duration,size,bit_rate:stream=index,codec_type,codec_name,width,height,avg_frame_rate,r_frame_rate,nb_frames,sample_rate,channels,color_space,color_transfer,color_primaries','-of','json',str(p)]
proc=subprocess.run(cmd,capture_output=True,text=True)
if proc.returncode:
    sys.exit(f'FAIL: ffprobe: {proc.stderr}')
data=json.loads(proc.stdout)
print(json.dumps(data,indent=2))
streams=data.get('streams',[])
videos=[s for s in streams if s.get('codec_type')=='video']
audios=[s for s in streams if s.get('codec_type')=='audio']
print('Video streams:',len(videos),'Audio streams:',len(audios))
print('NOTE: Media probe is NOT evidence of performance, narrative, camera or mixing quality.')
if a.sample_every:
    if a.sample_every<=0 or not shutil.which('ffmpeg'):
        sys.exit('BLOCKED: nonpositive sample period or ffmpeg unavailable')
    out=Path(a.output or (str(p.with_suffix(''))+'_qc')).expanduser().resolve()
    out.mkdir(parents=True,exist_ok=True)
    # Regular sampling helps find large changes; it is not enough for contact validation.
    frame_pattern=out/'overview_%04d.jpg'
    cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(p),'-vf',f'fps=1/{a.sample_every}',str(frame_pattern)]
    res=subprocess.run(cmd,capture_output=True,text=True)
    if res.returncode:
        sys.exit(f'FAIL: ffmpeg frame extraction: {res.stderr}')
    print('Overview frames extracted to',out)
    print('IMPORTANT: Extract consecutive frames at portal/contacts separately before any QC approval.')
