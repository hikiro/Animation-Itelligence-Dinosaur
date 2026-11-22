#!/usr/bin/env python3
"""Original educational before/after storyboard animation demos, no source media or audio reused.
Creates three comparative 4-second MP4 clips and contact sheet. These are simple schematic tests,
not the DINO production film or proof that final rigs pass cinematic quality.
"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import math,subprocess,wave,numpy as np, json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'12_ACTION_INTELLIGENCE/EXPERIMENTS'
OUT.mkdir(parents=True,exist_ok=True)
FPS=30; W=960;H=540; PW=W//2;DUR=120
fontpath='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font=ImageFont.truetype(fontpath,17)
fontsm=ImageFont.truetype(fontpath,13)
fontlg=ImageFont.truetype(fontpath,21)
COLOR={'ground':'#E7DDBB','sky':'#DCEBF2','good':'#357F70','bad':'#AB5B57','ink':'#283849','portal':'#4BA6FF','edge':'#236BC0','egg':'#F8D78D'}
def smooth(x):x=max(0,min(1,x));return x*x*(3-2*x)
def mix(a,b,t):return a+(b-a)*t
def line(draw,pts,color='#253B51',width=10):draw.line(pts,fill=color,width=width,joint='curve')
def text(draw,xy,txt,color='#283849',font_=font):draw.text(xy,txt,fill=color,font=font_)

def ground(d,ox):
    d.rectangle((ox,0,ox+PW,H),fill=COLOR['sky']);
    d.rectangle((ox,457,ox+PW,H),fill=COLOR['ground']);d.line((ox,457,ox+PW,457),fill='#7EAE89',width=5)
    for i in [20,95,410,448]:
        if i<420:line(d,[(ox+i,456),(ox+i+5,444)],'#70A47F',3)

def head(d,x,y,r=22,eye_dir=1,alpha='#FFF5DF',reaction=False):
    d.ellipse((x-r,y-r,x+r,y+r),fill=alpha,outline='#253B51',width=4)
    if reaction:
        d.ellipse((x+6,y-4,x+11,y+3),fill='#283849'); d.ellipse((x-6,y-4,x-1,y+3),fill='#283849')
        d.ellipse((x-4,y+7,x+5,y+17),outline='#283849',width=2)
    else:
        d.ellipse((x+eye_dir*4-2,y-4,x+eye_dir*4+2,y+1),fill='#283849');d.arc((x-5,y+3,x+8,y+14),0,145,fill='#283849',width=2)

def person_layer(x,foot_y=456,pose=0,lean=0,step=0,gaze=1,arm_target=None,reaction=False,opacity=255,planted_foot_x=None):
    # x and coordinates local to a panel, opaque layer for portal compositing masks
    layer=Image.new('RGBA',(PW,H),(0,0,0,0));d=ImageDraw.Draw(layer)
    y=foot_y
    hipx=x+lean*0.4; hipy=y-75+pose
    shoulder=(int(hipx-lean*.4),int(hipy-65));hip=(int(hipx),int(hipy))
    hx=shoulder[0]+lean*.17; hy=shoulder[1]-28
    # Legs: articulated by computed knee positions; a planted foot can remain fixed in world space.
    planted=(round(hipx-18 if planted_foot_x is None else planted_foot_x),y)
    moving=(round(hipx+22+step*22),y-abs(step)*28)
    knee1=(int(mix(hipx,planted[0],.65)-8),int(mix(hipy,planted[1],.5)))
    knee2=(int(mix(hipx,moving[0],.65)+7),int(mix(hipy,moving[1],.5)))
    line(d,[hip,knee1,planted],width=9)
    line(d,[hip,knee2,moving],width=9)
    line(d,[hip,shoulder],width=13)
    if arm_target is None:
        a1=(int(shoulder[0]-24+step*7),int(shoulder[1]+47));a2=(int(shoulder[0]+27-step*7),int(shoulder[1]+42))
    else:
        a1=(int(arm_target[0]),int(arm_target[1]));a2=(int(arm_target[0]+14),int(arm_target[1]-1))
    line(d,[shoulder,(int(mix(shoulder[0],a1[0],.6)),int(mix(shoulder[1],a1[1],.6)+5)),a1],width=7)
    line(d,[shoulder,(int(mix(shoulder[0],a2[0],.6)+9),int(mix(shoulder[1],a2[1],.6))),a2],width=7)
    head(d,hx,hy,eye_dir=gaze,reaction=reaction)
    return layer

def overlay(d,ox,caption,phase,mark):
    d.rounded_rectangle((ox+16,14,ox+PW-16,92),radius=12,fill='#FFFFFF',outline='#BDCDD5',width=2)
    text(d,(ox+28,23),caption, '#A44D4D' if mark=='BAD' else '#276F61',fontlg)
    text(d,(ox+28,56),phase,font_=fontsm)

def status(d, ox, line1, line2):
    d.rounded_rectangle((ox+20,472,ox+PW-20,522),radius=9,fill='#FDFBF7',outline='#C4BBAF',width=2)
    text(d,(ox+32,481),line1,font_=fontsm)
    text(d,(ox+32,500),line2,font_=fontsm)

def portal_draw(d,ox,cx,top,bottom,stage,fill='#123E79',rim='#42ACF3',outline=True):
    hw=61*stage
    box=(ox+cx-hw,top,ox+cx+hw,bottom)
    if hw>6:
        d.ellipse(box,fill=fill,outline=rim,width=10)
        if outline:d.arc((box[0]+6,box[1]+6,box[2]-6,box[3]-6),30,240,fill='#C3F7FF',width=5)
    return box

def scene_portal(frame):
    I=Image.new('RGB',(W,H),'#F0F3F3');d=ImageDraw.Draw(I)
    for ox in (0,PW):ground(d,ox)
    # left faulty: a floating door and visible side entrance
    p=smooth((frame-7)/23)
    portal_draw(d,0,243,168,391,p)
    x=-35+min(1,frame/100)*370
    I.paste(person_layer(int(x),foot_y=455,step=math.sin(frame*.3)),(0,0),mask=person_layer(int(x),foot_y=455,step=math.sin(frame*.3)).getchannel('A'))
    # corrected: portal bottom anchored at foot plane; in-door matte until crossing
    portal_draw(d,PW,164,148,456,p)
    inside=Image.new('RGBA',(PW,H));outside=Image.new('RGBA',(PW,H))
    emergence=smooth((frame-24)/76)
    px=160+emergence*145
    # human only starts visible after opening, moving from portal interior, not the screen edge
    if frame>=24:
        step=math.sin(frame*.13)*(.6 if frame<95 else .12)
        local=person_layer(px,foot_y=455,lean=(1-emergence)*3,step=step,gaze=1)
        # viewport union: inside aperture + out-of-threshold right-side region
        mask=Image.new('L',(PW,H),0);md=ImageDraw.Draw(mask)
        md.ellipse((103,158,225,450),fill=255)
        md.rectangle((224,90,PW,456),fill=255)
        # Inside staged portal gets mild blue tint, exterior normal
        alpha=Image.fromarray(np.minimum(np.asarray(local.getchannel('A'),dtype=np.uint16),np.asarray(mask,dtype=np.uint16)).astype('uint8'))
        I.paste(local.convert('RGB'),(PW,0),alpha)
    # foreground rim re-overlay to establish occlusion at threshold
    if p>.05:
        d=ImageDraw.Draw(I); d.arc((PW+103,148,PW+225,456),280,80,fill='#E2FCFF',width=13)
        d.arc((PW+103,148,PW+225,456),280,80,fill='#236BC0',width=5)
    d=ImageDraw.Draw(I)
    badphase='slides in from screen edge' if frame>12 else 'floating decorative doorway'
    goodphase='partly inside aperture' if frame<52 else ('crossing threshold' if frame<86 else 'fully outside and balanced')
    overlay(d,0,'FAULTY — PORTAL',badphase,'BAD');overlay(d,PW,'CORRECTED — PORTAL',goodphase,'GOOD')
    status(d,0,'No real plane crossing','No inside/outside masking')
    status(d,PW,'Visible emergence + front rim','Ground-level threshold')
    return I

def dinosaur_foot(d,ox,x,foottop):
    # toy dinosaur leg / broad foot
    d.rounded_rectangle((ox+x-40,-35,ox+x+41,foottop+12),radius=18,fill='#6CA781',outline='#426F59',width=6)
    d.ellipse((ox+x-76,foottop-16,ox+x+79,foottop+28),fill='#588D6D',outline='#426F59',width=5)
    for toe in [-48,-8,36]:
        d.polygon([(ox+x+toe,foottop+18),(ox+x+toe+14,foottop+19),(ox+x+toe+7,foottop+31)],fill='#EDF0C7')

def scene_stomp(frame):
    I=Image.new('RGB',(W,H));d=ImageDraw.Draw(I)
    for ox in (0,PW):ground(d,ox)
    if frame<60:footTop=mix(100,421,smooth((frame-10)/50))
    else:footTop=428+8*math.exp(-(frame-60)/12)*math.sin((frame-60)*.35)
    # BAD: recoil and shake before foot contacts ground
    bad_trigger=frame>=28
    bx=185+(14*math.sin(frame*.9) if bad_trigger else 0)
    bad_layer=person_layer(bx,foot_y=455,pose=(-25 if bad_trigger else 0),reaction=bad_trigger)
    I.paste(bad_layer,(0,0),bad_layer)
    dinosaur_foot(d,0,353,footTop)
    # GOOD: no reaction until stomp contact at f60; eye+head at f63, torso after f72
    if frame<61: react=0
    else: react=smooth((frame-61)/15)
    headreact=smooth((frame-63)/8)
    bodyreact=smooth((frame-72)/14)
    torso_back=bodyreact*15
    x=185-torso_back
    good_layer=person_layer(x,foot_y=455,lean=-headreact*11,pose=bodyreact*10,step=0,gaze=-1 if frame>=63 else 1,reaction=frame>=65,planted_foot_x=167)
    I.paste(good_layer,(PW,0),good_layer)
    dinosaur_foot(d,PW,353,footTop)
    d=ImageDraw.Draw(I)
    if frame>=60:
        for ox in [0,PW]:
            k=max(0,1-(frame-60)/22)
            for i in range(6):
                a=(i-2.5)*.4
                xx=ox+350+int(math.sin(i*11)*40*k)
                yy=443-int(22*k*(i%3+1))
                d.ellipse((xx-4,yy-4,xx+4,yy+4),fill='#92A387')
    overlay(d,0,'FAULTY — STOMP','fear begins BEFORE contact' if frame>28 and frame<60 else 'unmotivated whole-body jitter','BAD')
    overlay(d,PW,'CORRECTED — STOMP','contact at f60 → gaze f63 → recoil f72','GOOD')
    status(d,0,'Cause/reaction out of order','Shake masks weak acting')
    status(d,PW,'Event-driven timing and recovery','Heavy step visibly contacts')
    return I

def egg(d,ox,x,y):
    d.ellipse((ox+x-18,y-24,ox+x+18,y+21),fill='#FFD98B',outline='#B18448',width=3)
    for dx,dy in [(0,-10),(-7,5),(11,7)]:d.ellipse((ox+x+dx-3,y+dy-4,ox+x+dx+4,y+dy+3),fill='#D7A45B')

def scene_catch(frame):
    I=Image.new('RGB',(W,H));d=ImageDraw.Draw(I)
    for ox in (0,PW):
        ground(d,ox)
        line(d,[(ox+290,205),(ox+400,205)],'#926F55',7)
        d.ellipse((ox+292,174,ox+364,201),outline='#AB8A6B',width=5)
    # FAULTY: instant teleport at f61; character hands remain wrong pose
    bpos=(337,159) if frame<61 else (184,327)
    egg(d,0,*bpos)
    badperson=person_layer(173,foot_y=455,arm_target=(202,355))
    I.paste(badperson,(0,0),badperson)
    # GOOD: egg leaves nest, follows one path, collides at f73; then hands carry it in
    if frame<30:
        ex,ey=337,159
    elif frame<73:
        u=(frame-30)/43
        ex=337+(220-337)*u
        ey=159+(346-159)*(u*u)
    else:
        u=smooth((frame-73)/36)
        ex=mix(220,190,u);ey=mix(346,340,u)
    handtarget=(221 if frame>45 else mix(188,221,smooth((frame-35)/20)),344)
    goodperson=person_layer(175,foot_y=455,lean=-7 if 35<frame<73 else 0,pose=6 if frame>72 and frame<95 else 0,arm_target=handtarget)
    I.paste(goodperson,(PW,0),goodperson)
    # egg drawn after hands at same point, but no switch in spatial world coordinate
    egg(d,PW,int(ex),int(ey))
    d=ImageDraw.Draw(I)
    if frame==73:d.ellipse((PW+205,332,PW+235,362),outline='#8ED4F2',width=4)
    overlay(d,0,'FAULTY — CATCH','egg teleports at F61' if frame>60 else 'static egg / hands','BAD')
    overlay(d,PW,'CORRECTED — CATCH','continuous fall; contact F73','GOOD')
    status(d,0,'No approach/contact path','Object appears already in hands')
    status(d,PW,'One continuous egg trajectory','Hands meet before secure carry')
    return I

def save_audio_stomp(path):
    rate=44100;dur=DUR/FPS;t=np.arange(int(rate*dur),dtype=np.float64)/rate
    rng=np.random.default_rng(2026)
    # A simple original synthetic low thump (not actual professional Foley)
    d=t-60/FPS
    tone=np.sin(2*np.pi*(58*d+18*d*d))*np.exp(-np.maximum(0,d)*9)*(d>=0)
    noise=rng.normal(size=len(t))*np.exp(-np.maximum(0,d)*34)*(d>=0)
    signal=np.clip((.33*tone+.08*noise),-1,1)
    with wave.open(str(path),'wb') as w:
        w.setnchannels(1);w.setsampwidth(2);w.setframerate(rate)
        w.writeframes((signal*32760).astype('<i2').tobytes())

def main():
    audit={}
    contact=Image.new('RGB',(W*2,H*3),'#FFFFFF')
    for i,(name,drawfn) in enumerate([('portal_crossing',scene_portal),('stomp_reaction',scene_stomp),('egg_catch',scene_catch)]):
        temp=OUT/f'{name}_frames';temp.mkdir(exist_ok=True)
        for frame in range(DUR):
            im=drawfn(frame)
            im.save(temp/f'{frame:04d}.png')
            if frame in [20,60,85]:
                pass
        strip=Image.new('RGB',(W*2,H))
        strip.paste(drawfn(30),(0,0));strip.paste(drawfn(88),(W,0));contact.paste(strip,(0,H*i))
        mp4=OUT/f'{name}_bad_vs_corrected.mp4'
        if name=='stomp_reaction':
            wav=OUT/'stomp_original_synthetic.wav';save_audio_stomp(wav)
            cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-framerate',str(FPS),'-i',str(temp/'%04d.png'),'-i',str(wav),'-c:v','libx264','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-shortest',str(mp4)]
        else:
            cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-framerate',str(FPS),'-i',str(temp/'%04d.png'),'-c:v','libx264','-crf','19','-pix_fmt','yuv420p',str(mp4)]
        subprocess.run(cmd,check=True)
        audit[name]={'file':str(mp4.relative_to(ROOT)),'frames':DUR,'seconds':DUR/FPS,'resolution':[W,H],'fps':FPS,'audio':'original synthetic stomp' if name=='stomp_reaction' else 'none', 'status':'RENDERED_DEMO_NOT_HUMAN_APPROVED'}
        # keep only representative snapshots; full encoded media is the reproducible sequence
        for f in temp.glob('*.png'):
            if f.stem not in {'0000','0030','0060','0073','0088','0119'}:f.unlink()
        print('Rendered',mp4.name)
    contact.save(OUT/'lesson05_bad_good_contact_sheet.jpg',quality=92)
    audit['test_sequence_notes']={
        'portal':'Good: aperture centered at x=164 local; ground at y=457; character originates at x=160 inside opening and crosses near-rim plane.',
        'stomp':'Good: contact f60; gaze/head after f63; body recoil f72; sound onset f60. Bad: shakes f28 before contact.',
        'egg':'Good: trajectory continuous from nest f30 to hand f73; after f73 egg retracts with hands. Bad: instant position jump at f61.',
        'limitation':'These are diagrammatic action tests; a rendered comparison does not prove character-art quality, inverse kinematics, or completed DINO benchmark.'}
    (ROOT/'12_ACTION_INTELLIGENCE/RESULTS/render_metrics.json').write_text(json.dumps(audit,indent=2)+'\n')
    print('Contact sheet and metadata complete')
if __name__=='__main__':main()
