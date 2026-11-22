#!/usr/bin/env python3
"""Rebuild Lesson 05 action recipe cards and machine-readable registry. Source entries below are
human-authored, original production proposals, not claims of studio-prescribed shot timings."""
from pathlib import Path
import json, re, textwrap, csv
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'12_ACTION_INTELLIGENCE'
# Fields: category~slug~everyday phrase~stimulus~perception~decision~anticipation~action~consequence~camera~audio~failure~fix~primary_channel~rig
DATA=r'''
Perception~notice-egg~Make the human notice the egg~The speckled egg moves in the edge of the frame~Eyes turn toward its motion before the head~Decide whether it is in danger~Blink stops and the neck leads into a lean~Eyes lock on egg; head follows; torso rotates slightly~Body changes travel direction toward nest~Hold medium framing with both egg and eyes visible~Small rustle then egg roll; no dramatic score yet~Head rotates before the egg moves~Start eye direction only after observable egg movement~headTurnDeg~eyes/head/neck/torso
Perception~turn-toward-sound~Make him hear something behind him~An offscreen thump reaches him~Ear/head attention shifts toward sonic source~Identify where sound came from~Foot freezes and shoulder lifts~Eyes move left; head rotates; torso follows later~Now faces the unseen source~Begin on his profile, retain screen geography of sound~Offscreen low thump can correctly lead reveal~Character reacts before thump without an intended premonition~Key perception after sound onset; let head follow ears~headTurnDeg~head/shoulder/torso/eyes
Perception~scan-danger~Have the character search the forest~Ambience suddenly becomes quieter~Notices gaps in known animal sounds~Search for a hidden threat~Pause gait and adjust balance~Eye scan left-right; head catches up; step to clear obstruction~Threat location becomes a plausible next reveal~Do not cut away during essential glance changes~Fade bird ambience then focused leaf rustle~Random head wiggle with no visual target~Assign three look targets tied to sound and scene geometry~gazeX~eyes/head/neck/pelvis
Perception~recognize-mother~She realizes the egg belongs to her~Mother finds nest empty then sees egg in human arms~Her gaze alternates between nest and egg~Conclude human has the baby~Body stiffens; nostrils widen~Head lowers and body points toward egg~Aggression becomes understandable~Over-shoulder or shared axis includes nest, egg, mother~One low breath rising toward roar~Instant anger before seeing empty nest or egg~Stage empty nest and egg eyeline before posture change~headLowerPx~eyes/head/neck/hips/tail
Perception~spot-hazard~He sees the branch before ducking~Low branch approaches on chase path~Eyes track branch and available clearance~Decide to lower his body~Quick head tuck and knee flex~Torso folds; hips lower; feet maintain forward contact sequence~Passes safely beneath branch~Keep branch edge and head in same shot~Wind rush ahead of nearest foliage brush~Character ducks before any branch is visible~Show obstacle well before avoidance beat~torsoLowerPx~eyes/head/spine/hips/knees
Perception~change-mind~He hesitates before deciding to rescue~Egg balances near ledge edge~Looks from egg to safe exit route~Chooses risky rescue~Weight rocks backward then forward~Hand retracts briefly then reaches firmly~Commitment has clear visible turning point~Hold stable composition during decision~Ambient detail drops; tiny egg scraping gains prominence~Linear reach with no hesitation despite scripted indecision~Insert separate opposing anticipation and commitment poses~reachPx~hand/shoulder/hips/eyes
Locomotion~first-step~Make the first step look grounded~Human has fully emerged from portal~Sees clear forest floor~Choose where to plant leading foot~Hips shift over current support~Leading foot swings then plants; hips transfer onto it~Trailing foot is released and body advances~Full figure and ground horizon in frame~Soft heel/sole contact on plant frame~Root slides at uniform speed while foot planted~Lock planted foot in world coordinates and solve knee~rootX~hips/knee/ankle/foot IK
Locomotion~steady-walk~Make the character walk naturally~Character sees desired destination~Eyes lead travel direction~Maintain controlled pace~Body leans by small angle~Alternate stance and swing with independent support foot~Head and arms overlap the stride~Side-on readable feet and floor~Footfalls at support transitions; footsteps vary slightly~Sinusoidal legs with no support lock~Use stride phase and world-space support anchors~rootX~hips/leg IK/arms/head
Locomotion~panic-run~Make the escape urgent~Dinosaur finishes roar and leans toward human~Human sees the threat approach~Run away while protecting egg~Sharp pivot, compress and push off~Root accelerates; feet alternate airborne and grounded phases~Distance from threat briefly grows~Track both subjects long enough to read pursuit~Breath, faster footfalls, mother footsteps on separate stem~Root begins at full speed with still-facing character~Anticipation pose then accelerating trajectory and foot phase~rootX~head/torso/hips/arms/feet
Locomotion~turn-around~Make him turn before running~He notices danger behind him~Eyes swing toward escape route~Decide to reverse direction~Hips load supporting foot~Eyes/head/shoulders/hips turn in sequence, feet pivot~Exit direction becomes unambiguous~Keep screen direction constant and hold turn in shot~Shoe friction sound on pivot contact~Translate left while torso still faces right~Use staggered yaw/key poses followed by push off~bodyAngleDeg~eyes/head/torso/hips/foot anchors
Locomotion~brake-heavy~Make the dinosaur stop convincingly~Baby chirp reaches mother mid-run~Eyes focus on newborn~Avoid stepping on it~Lower body, shorten stride, forelegs react~Hips decelerate; planted foot skids briefly; tail keeps moving~Dinosaur stops with visible mass and tail settle~Wider view retains feet and moving tail~Two heavy decelerating footfalls, tail whoosh then quiet~Instant zero velocity with frozen tail~Apply finite braking distance and delayed tail follow-through~rootX~hips/feet/head/tail
Locomotion~stumble-recovery~Make him nearly fall but recover~One shoe catches exposed root~Sees falling ground and egg at risk~Keep egg safe and restore balance~Arms clamp egg; torso pitches~Recovery step lands ahead of tipping center of mass~Body regains balance without dropping egg~Hold continuous medium-wide to show foot and hands~Scuff, gasp, heavy recovery step~Sudden spin or squash with no visible trip cause~Root contact first; move COM toward failure then plant recovery foot~torsoTiltDeg~root/hips/feet/egg hands
Object~reach-and-grasp~Make the egg pickup readable~Human notices egg resting on ground~Gaze locks onto target position~Pick up without crushing it~Bend knees, open hands, align approach~Hands reach egg and close after contact~Egg becomes attached to two-hand prop anchor~Close enough to see contact, wide enough for posture~Cloth movement then light finger/shell contact~Egg jumps to hands before touch~Switch parent or hand constraint only at contact event~handReachPx~shoulders/elbows/hands/prop anchor
Object~catch-falling~Make him catch the falling egg~Egg leaves nest under gravity~Eyes track its predicted fall~Intercept before ground contact~Knees load and arms extend~Hands intercept moving egg, absorb momentum, retract~Egg remains stable after capture~Hold egg trajectory and hands in same frame~Egg scrape, brief whoosh, contact muffled by hands~Egg disappears from air and reappears held~Intersect continuous paths and attach at shared contact frame~propY~hands/elbows/root/egg
Object~carry-prop~Keep egg attached during chase~Human has just caught egg~Checks that it is stable~Protect egg while running~Bring elbows close to ribs~Arms counteract gait; egg stays in torso-relative cup~Egg never clips torso or floats outside hands~Use frame including chest, hands, and escape path~Subtle shell/rubbing noise, no separate random thumps~Egg independently interpolates with its own X movement~Drive egg from established hand attachment transform~eggAnchorX~torso/arm/hand/prop constraint
Object~put-down~Make him gently put the baby down~Mother waits and baby wriggles~Human identifies safe landing spot~Set baby down safely~Crouch and align baby over ground~Lower baby until feet contact; open hands after support~Hands withdraw; baby stands independently~Avoid cut at release; feet must remain visible~Soft toe contact precedes cloth release sound~Baby teleports from hands to ground~Release ownership only after ground contact constraint is valid~handHeightPx~root/hips/knees/hands/baby
Object~hand-over~Pass an object from one character to another~Receiver reaches toward offered object~Both characters follow object with gaze~Perform coordinated transfer~Receiver opens hand; giver slows~Receiver grips at overlap then giver releases~Object remains continuously supported~Two-shot with hands sharing spatial region~Fabric and soft grip sounds at hand overlap~Object briefly floats between characters~Dual-grip interval then explicit ownership change~propX~givers hand/receiver hand/prop anchors
Object~push-door~Make a door open when pushed~Closed door blocks character route~Eyes settle on handle and hinge~Open it with appropriate force~Feet brace and shoulder leans~Hand contacts door; shoulder and arm push, door rotates at hinge~Character steps through clear opening~Three-quarter shot demonstrates hinge axis~Latch click then hinge creak and footstep~Door swings before hand reaches it~Hinge angle driven only after visible hand force begins~doorAngleDeg~feet/shoulder/hand/door hinge
Force~giant-stomp~Make the dinosaur foot feel heavy~Mother lifts a foot over ground~Human sees moving shadow~Mother plants weight while progressing~Knee bends and body mass lowers~Foot contacts ground and ground elements compress~Torso and tail settle; leaves react a few frames later~Low angle framing reveals full contact and scale~Low-frequency impact plus leaf/rattle transients~Camera shakes before footfall without intentional J-cut~Tie peak impulse to contact frame and weight transfer~footY~leg/foot/hips/tail/ground
Force~recoil-shot~Make the firing action physically legible~Character voluntarily performs a stylized fictional firing action~Eyes align with prop and target~Commit to firing~Body braces; shoulder and arms stabilize~Prop emits flash then arms, shoulders and torso recoil~Balance adjusts and muzzle settles~Show source and recoil without obscuring action~Sharp fictional sound follows source event, then tail decay~Flash-only with static shooter~Trigger flash and whole-body recoil keyed from common event time~torsoBackPx~hand/arm/shoulder/torso/hips
Force~impact-body~Make the hit clearly understandable~Moving object visibly reaches target~Target registers force at contact~Balance must respond~Body has braced or remains unaware as intended~Contact compression; torso moves, limbs and head lag~Body recoils or falls with follow-through~Show target contact clearly before close emphasis~Contact transient then clothes/grunt and lingering room tone~Random wiggle and flash without actual collision~Drive recoil by contact time, force direction and coordinated poses~torsoDisplacePx~torso/hips/neck/limbs/ground
Force~land-from-jump~Make the jump landing have weight~Character falls toward chosen landing spot~Feet orient toward contact plane~Absorb downward momentum~Knees begin extending toward floor~Feet touch then knees/hips compress~Torso settles; arms counterbalance and recover~Wide view with feet and landing plane~Foot impact at measured contact frame, small fabric tail~Instantly frozen pose at ground y~Vertical path intersects floor then compressed body pose~hipDropPx~feet/knees/hips/arms
Force~shove-object~Make him push a heavy boulder~Boulder blocks travel~Hands test surface and resistance~Commit more effort~Feet spread; torso leans; hands press~Shoulders drive force and boulder begins moving after resistance~Character follows moving mass slowly~Wide framing includes feet, contact and boulder~Stone scraping begins after applied force~Boulder glides away before character touches it~Constraint requires hand contact and push threshold~objectX~feet/hips/arms/hands/object
Force~crash-branch~Make the dinosaur break the branch~Branch lies across mother's pursuit path~She sees branch too late~Continue chase through the obstacle without stopping~Neck ducks imperfectly; shoulders drive forward~Head/shoulder impacts branch; bending precedes snapping~Pieces move outward with gravity and drag~Preserve recognizable branch and dinosaur contact point~Wood strain then sharp crack at fracture, leaves after~Branch explodes before dinosaur reaches it~Fracture only on predicted geometry contact and threshold~branchDeflectionPx~head/neck/branch joints/fragments
Spatial~cross-portal~Make the man genuinely emerge from a portal~Portal opens anchored at ground~Human looks out from inside the aperture~Step from interior into forest~Hand grips near rim, leading foot tests ground~Head/torso/legs cross plane with masks and weight transfer~Trailing foot exits; entire body outside and stable~Camera maintains aperture, threshold and planted foot~Portal hum swells as near/far sound perspective changes~Character slides in from offscreen in front of portal~Use portal interior mask + exterior character layers and crossing states~crossingPct~portal aperture/front rim/rig/foot
Spatial~duck-under~Make ducking under a branch credible~Branch appears in path ahead~Eyes measure branch clearance~Choose to lower center of mass~Head tucks and knees flex~Torso, hips and head move under obstacle while feet continue~Character rises only once head clears~Hold enough profile for top of head and branch~Near-ear branch swish only at closest pass~Torso drops after head already intersects branch~Lower before collision and track clearance frame-by-frame~headHeightPx~neck/hips/knees/branch
Spatial~squeeze-gap~Make the mother squeeze through a narrow opening~Portal aperture is narrower than her snout~Mother tests rim with nose~Push through while portal yields~Neck draws back slightly~Snout contacts rim; rim stretches; head advances~Portal recoil trails departure of contact~Oblique framing shows rim shape around snout~Elastic hum and rim strain synchronized to deformation~Dinosaur materializes inside room with no threshold crossing~Drive rim deformation from signed penetration/contact~portalScaleX~snout/head/portal mesh
Spatial~break-through~Make the crash through foliage readable~Dense fern screens the chase route~Dinosaur sees travel corridor through leaves~Keep advancing into the obstructing foliage~Head pushes foliage ahead of torso~Leaves bend before tearing, then separate and fall~Branch and leaves retain momentum after passage~Do not hide every contact with particles~Layered leaf rustle, tearing, delayed falling leaves~Decorative green particles appear before foliage touched~Simulate progressive contact response then fragment release~foliageDeflectionPx~foliage joints/body collider
Spatial~enter-room~Make arrival in apartment geographically coherent~Portal connects prehistoric forest to apartment~Human sees a floor immediately beyond rim~Move into new environment~Leading foot tests carpet~Body crosses plane; contact surface/material changes~Footstep texture changes and apartment reverb appears~Match screen direction through plane or clearly re-establish~Cross-portal ambience and carpet foot sound with perspective~New room starts with character already fully in it~Match portal world transform and mask over cut~crossingPct~portal/human/camera/floor
Spatial~leap-gap~Make a gap jump visually plausible~Character sees missing ground ahead~Eyes estimate landing zone~Choose jump instead of stopping~Knees compress and arms swing back~Takeoff occurs at edge, airborne arc crosses gap~Landing contacts far side and absorbs momentum~Wide shot shows both edges and full trajectory~Takeoff scrape, airborne quiet, landing thump~Character teleports over gap with linear root X and constant Y~Define takeoff/contact frames and continuous ballistic-like arc~rootY~legs/hips/arms/root
Emotion~hesitation~Make the character hesitate before acting~An uncertain obstacle threatens success~Looks at obstacle then possible exit~Weigh competing actions~Small backward weight shift and incomplete reach~First movement aborts, brief hold, second committed gesture~Decision becomes visible through contrast~Keep medium composition stable to read micro-actions~Small breath and pause; avoid excessive stinger~Uniform slow movement called hesitation~Distinct blocked attempt, pause and committed pose~handReachPx~eyes/shoulders/hand/feet
Emotion~fear~Show fear without cartoon jitter~A huge dinosaur lowers head toward human~Human notices threatening gaze and jaw~Protect egg and seek exit~Breath catch; neck retracts; shoulders rise~Recoil and protective posture, then pivot~Fear visibly changes goal and locomotion~Maintain threat and human in eyeline sequence~Low breath, reduced ambience, sharp inhale~Whole-body random wiggle before threat becomes known~Trigger reaction from recognition then coordinated protective posing~torsoBackPx~eyes/neck/shoulders/hips/prop
Emotion~curiosity~Make him curious about the new world~Human emerges into unfamiliar forest~Looks at enormous leaves above~Investigate cautiously~Lean forward while keeping planted foot~Eyes rise, head tilts, hand reaches toward leaf~Discovering motivates next movement~Hold revealing foreground plant in shared frame~Gentle leaves and quiet interested breath~Random tilt without visible subject~Anchor every glance and reach to a plant or sound~headTiltDeg~eyes/head/neck/arm
Emotion~relief~Make the relief after the chase feel earned~Mother nuzzles newborn instead of threatening~Human verifies she is calm~Release protective tension~Chest holds breath then softens~Shoulders lower, grip relaxes, knees unlock~Human smiles and regains normal posture~Move to less compressed medium framing only after recognition~Music opens after safe nuzzle; exhale prominent~Instant smile at first appearance of baby despite danger~Make mother-behavior verification precede relaxation~shoulderDropPx~eyes/shoulders/arms/hips
Emotion~affection~Make mother and baby contact tender~Baby reaches mother's lowered muzzle~Both make eye contact and orient toward each other~Reunite and soothe~Mother slows head approach; baby leans up~Gentle nose-to-head contact; subtle compression~Mother raises head slightly; baby follows with gaze~Sustain readable two-shot and silence~Quiet chirp, warm breath, restrained chord after contact~Faces touch only because both sprites overlap with no anticipation~Establish attention, approach speed, contact deformation and recovery~headLowerPx~mother head/baby head/neck/ground
Emotion~comic-surprise~Make a funny delayed reaction~Unexpected giant snout begins stretching portal~Human perceives odd shadow and hears creak~Slowly realize what is happening~Character stays still for one beat, eyes shift~Head turns slowly, then body springs in exaggerated shock~Pause after reveal lets joke land~Keep snout offscreen long enough to earn reveal~Creak then intentionally awkward silence and short accent~Random instant scream before audience sees the snout~Set up sightline, delayed recognition, decisive reaction and hold~headTurnDeg~eyes/head/shoulders/hips
Cinema~track-chase~Make the chase easy to follow~Human runs left and dinosaur follows from right~Audience must track decreasing gap~Maintain both subjects spatially legible~Start tracking after running speed is established~Camera moves to retain positions while foreground parallax passes~Dinosaur closing distance is measurable~Side tracking, ground horizon and direction locked~Independent footfalls and whoosh anchored to camera perspective~Camera crosses axis and swaps predator/prey sides accidentally~Define chase axis and camera path preserving screen direction~cameraX~camera root/environment layers
Cinema~reveal-threat~Reveal the dinosaur's size dramatically~Ground begins vibrating before creature appears~Audience hears offscreen footsteps and sees human reaction~Build anticipation before identification~Hold lower portion of frame with shadow and foot~Tilt or reframe from foot to massive head~Character scale is established in shared geography~Begin low, let human remain a size reference~Low footfalls can intentionally precede visual reveal~Immediate face close-up removes size information~Reveal scale by connected view foot→body→head~cameraTiltDeg~camera/ground/shadow/dinosaur
Cinema~emphasize-detail~Give the cracking egg cinematic importance~Egg produces first quiet crack amid noisy chase~Human hears a small unexpected sound~Direct viewer to source without losing geography~Brief hold and human glance~Camera gently pushes to shell crack after hand/egg visibility~Crack becomes new center of attention~Push-in motivated by recognition, return to wider shot~Duck music so shell transient is audible~Random dramatic zoom unrelated to what characters see~Begin after eye contact establishes source, preserve orientation~cameraScale~camera/human hands/egg
Cinema~match-action~Cut between views without teleporting~Human begins lifting baby in wide shot~Audience recognizes start of lift~Show hand contact close, then return wide~Hand approaches, cut on continuous movement~New shot continues same hand/egg positions and phase~Object geography remains consistent over cut~Match hand vector/axis, not just any position~Maintain one continuous Foley trajectory across cut~Hands reset to old position after cut~Record world state at edit and reconstruct new camera pose~handY~camera/hand/baby
Cinema~sound-bridge~Use sound to lead the next revelation~Mother footfall happens outside camera frame~Human hears source while camera stays with him~Allow audience to anticipate danger~Hold reaction shot longer before cut~Offscreen effect begins as spatial cue; camera reveal follows~Sound is justified when mother becomes visible~Hold first shot, reveal source in next~J-cut is intentional; label offscreen origin in cue sheet~All audio early labelled error or disconnected thump~Define emitter position and audible event before picture reveal~soundGain~audio emitter/camera/gaze
Cinema~silence-payoff~Make the baby reveal emotionally powerful~First hatch chirp cuts through chase chaos~Human and dinosaur both notice~Direct attention to newborn~Music and effects reduce before baby appears~Hold baby emergence with minimal score then gentle return~Emotional reversal becomes audible and visible~Stable two-shot then close detail only if needed~Short audible void/duck, intimate chirp, softer ambience~Constant loud music masks the tiny hatch~Sidechain/automation of score around baby chirp event~musicGain~audio mixer/camera/egg/baby
'''.strip()

configs={
'Perception':dict(rig='eye target then head turn; torso and foot turn only if intention changes', lens='medium staging with target readable', source=['S45','S46'], kind='acting'),
'Locomotion':dict(rig='hips COM, stance foot world-lock, knee IK and overlapping arms', lens='full-body including ground', source=['S45','S48'], kind='locomotion'),
'Object':dict(rig='two-hand target constraints, object world pose, ownership transfer', lens='keep interacting hands and object readable', source=['S45','S47'], kind='interaction'),
'Force':dict(rig='contact-driven force envelope plus hips/head/tail/limb overlap', lens='include source and recipient of force', source=['S45','S46'], kind='impact'),
'Spatial':dict(rig='rig/world coordinates, apertures, collision and camera continuity', lens='show entry path and obstacles', source=['S46','S47'], kind='spatial'),
'Emotion':dict(rig='gaze, intention, pose contrasts, breath and whole-body reactions', lens='favor visible face and body silhouette', source=['S45','S46'], kind='emotion'),
'Cinema':dict(rig='camera or mixer controls referenced to actor world events', lens='camera motion meaningful not arbitrary', source=['S46','S49'], kind='cinema')}
phases=('stimulus','perception','decision','anticipation','action','consequence')
# Edit-friendly distinct beat schedules (times at 30 fps, last end-exclusive). Source-specific proposal, not universal durations.
framesets={
'Perception':[0,9,18,27,39,66,90], 'Locomotion':[0,8,16,25,37,73,96],
'Object':[0,12,19,28,40,76,108], 'Force':[0,10,17,25,38,69,90],
'Spatial':[0,12,20,30,42,85,120], 'Emotion':[0,14,24,34,46,78,108],
'Cinema':[0,12,23,31,45,83,120]
}
recipes=[]
for line in DATA.splitlines():
    values=[x.strip() for x in line.split('~')]
    assert len(values)==15,(len(values),line)
    category,slug,utterance,*vals=values
    stim,perceive,decide,anticipate,act,cons,camera,audio,fail,fix,channel,rig=vals
    count=len(recipes)+1
    boundaries=framesets[category]
    event_times={phase:boundaries[i] for i,phase in enumerate(phases)}
    event_times['end']=boundaries[-1]
    # primary normalized channel rises over anticipation+action. Secondary lags to represent overlap.
    curves={channel:[[0,0],[boundaries[3],0],[boundaries[4],0.12],[boundaries[5],1.0],[boundaries[-1],1.0]],
            'secondaryOverlap':[[0,0],[boundaries[4],0],[boundaries[5],0.5],[boundaries[-1],1.0]]}
    if slug in ('cross-portal','enter-room'):
        event_times['crossing_start']=boundaries[4];event_times['crossing_complete']=boundaries[5]
    if slug in ('catch-falling','reach-and-grasp','put-down','hand-over','push-door','giant-stomp','impact-body','land-from-jump','crash-branch'):
        event_times['contact']=boundaries[4]+max(2,(boundaries[5]-boundaries[4])//2)
    r={'id':f'ACT-{count:03d}','category':category,'slug':slug,'utterance':utterance,'intent':f'Make the viewer understand: {utterance.lower().replace("make ","")}.',
       'stimulus':stim,'perception':perceive,'decision':decide,'anticipation':anticipate,'action':act,'consequence':cons,
       'camera':camera,'audio':audio,'failed_pattern':fail,'repair_strategy':fix,'primary_channel':channel,
       'rig':rig,'phase_frames':event_times,'curves':curves,'duration_frames':boundaries[-1],
       'source_ids':configs[category]['source'],'status':'PROPOSED_RECIPE_NOT_RENDER_VERIFIED',
       'qa_expected':[f'Stimulus visible or intentionally audible: {stim}',f'Perception and decision visibly motivate action: {perceive}; {decide}',f'Main event actually completed: {act}',f'Aftermath visible: {cons}'],
       'ambiguity':'Decide realism versus style and audience viewpoint before adding graphics, blur, or speed ramps.'}
    recipes.append(r)
assert len(recipes)==42,len(recipes)
(OUT/'DATA/action_recipes.json').write_text(json.dumps(recipes,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
# Actual source snippet and bad comparison shown with every card. The engine reads the exact channels defined in JSON.
for r in recipes:
    frames=r['phase_frames'];ch=r['primary_channel'];slug=r['slug'];name=r['id'];cat=r['category'];src=','.join(r['source_ids'])
    phase_table='\n'.join(f'| {ph.title()} | F{frames[ph]:03d}–F{frames[phases[i+1]]-1:03d} | {r[ph if ph!="perception" else "perception"]} |' if i<5 else f'| {ph.title()} | F{frames[ph]:03d}–F{frames["end"]-1:03d} | {r[ph]} |' for i,ph in enumerate(phases))
    # show a deliberately wrong model *specific to the named channel*
    wrong=f'const {ch} = frame < {frames["action"]} ? 0 : 1; // abrupt state jump, ignores perception/contact'
    if slug in ('cross-portal','enter-room'): wrong='const personX = -50 + frame*6; // slides in from screen edge; no portal depth or occlusion'
    if slug in ('carry-prop','put-down','hand-over','catch-falling'): wrong='const propX = lerp(0, 400, frame/100); // independent movement, no contact/ownership state'
    if slug in ('giant-stomp','impact-body','recoil-shot','crash-branch'):wrong='const shake = Math.sin(frame*7)*18; // fake impact, no defined contact impulse or body reaction'
    if slug in ('steady-walk','first-step','panic-run'):wrong='const footWorldX = hipX + 30*Math.sin(frame*.3); // planted foot slides with root'
    if slug in ('sound-bridge','silence-payoff'):wrong='const audioGain = 1.0; // no knowledge of event timing, distance or dramatic priority'
    good=f'const pose = sampleAction("{name}", frame, recipes);\nconst {ch} = pose.channels.{ch};\nconst phase = pose.phase;\n// Connect {ch} to the appropriate rig/camera/audio property.\n// Extra collision/IK/occlusion constraints are mandatory when listed below.'
    meta=f'---\nid: {name}\ntitle: {r["utterance"]}\nkind: action_recipe\nstatus: PROPOSED_NOT_PRODUCTION_VERIFIED\ntags: {cat.lower()}, {slug.replace("-", ", ")}, acting, implementation, qa\nsource_ids: {src}\nrelated_ids: LRN-0001, LRN-0002, LRN-0004\napplies_to: 2D, AE, Remotion, storyboard\nupdated: 2026-11-19\n---\n'
    body=f'''{meta}
# {name} — {r['utterance']}

**Creative intention:** {r['intent']}

**Context dependency:** {r['ambiguity']} This timing is a *starting blocking proposal*, not a studio universal rule.

## Causal storyboard at 30 fps ({r['duration_frames']} frames, end-exclusive)

| Phase | Frames | What the audience must perceive |
|---|---:|---|
{phase_table}

## Character and asset engineering

- **Primary rig/controllers:** {r['rig']}.
- **Recommended system:** {configs[cat]['rig']}.
- **Named channel:** `{ch}`. The sample engine returns normalized 0–1 values, to be mapped to shot-specific units.
- **Object/space constraints:** preserve world contacts and attachment/occlusion where applicable; do not pretend ease curves solve collisions or IK.

## Camera and sound—chosen from story meaning

- **Camera objective:** {r['camera']}
- **Sound objective:** {r['audio']}
- **Why they belong together:** both direct attention to the event's cause and result; a sound may legitimately precede picture when its source is offscreen.

## Technical implementation (tested as data sample, not as a finished character rig)

JavaScript entry: `08_TOOLS/action_engine.mjs`; data: `12_ACTION_INTELLIGENCE/DATA/action_recipes.json`.

**Bad / known failure approach**

```js
{wrong}
```

**Better, event-addressable implementation**

```js
import {{ sampleAction }} from '../../08_TOOLS/action_engine.mjs';
// `recipes` is the parsed JSON array. `frame` is the absolute local scene frame.
{good}
```

The sampled value only describes timing and desired change. Actual end-effectors, colliders, mattes, transitions, and audio emitters must be connected to it and evaluated in a render.

## Defect-to-fix reasoning

- **Observed-risk / deliberately flawed design:** {r['failed_pattern']}.
- **Root cause hypothesis:** motion/effects applied without preserving the action's cause, geometry, and contact dependencies.
- **Repair:** {r['repair_strategy']}.

## Observable acceptance test

{''.join('- '+test+'\n' for test in r['qa_expected'])}- Verify frame-by-frame at phase boundaries and contacts; check camera axis and spatial sound perspective.
- If a render or listening test is absent, label status **UNVERIFIED_VISUAL_AND_AUDIO**, even if JS tests pass.

## Evidence status and scope

- `RESEARCH_SOURCE`: {src}; supporting **general principles**, not these particular invented shot timings.
- `PRODUCTION_PROPOSAL`: action breakdown, staging, sound decisions, code binding.
- `NOT_TESTED`: this specific recipe has not been individually rendered/approved unless listed in `12_ACTION_INTELLIGENCE/RESULTS/TEST_REPORT.md`.

## Where not to overapply

Do not mechanically insert identical anticipation or extra head-turn into every action. A surprise reaction, urgent protective reflex, premeditated effort, and offscreen warning legitimately have different timing and perception requirements.
'''
    (OUT/'RECIPES'/f'{name}_{slug}.md').write_text(body,encoding='utf8')
# human navigation
index=['# Lesson 05 — Searchable Action Recipe Index','', '**Status:** 42 production *proposals*, not 42 rendered validations.','', 'To search: `python 08_TOOLS/search_knowledge.py "catch egg hand contact" --expand --scope 12_ACTION_INTELLIGENCE`.','', 'Machine-readable registry: [`DATA/action_recipes.json`](DATA/action_recipes.json).','']
for category in configs:
    index+=['## '+category,'']
    for r in recipes:
        if r['category']==category:index.append(f'- [{r["id"]} — {r["utterance"]}](RECIPES/{r["id"]}_{r["slug"]}.md) · `{r["slug"]}` · {r["duration_frames"]} frames')
    index.append('')
(OUT/'INDEX.md').write_text('\n'.join(index)+'\n',encoding='utf8')
with (OUT/'DATA/action_recipes.csv').open('w',newline='',encoding='utf-8') as fp:
    fields=['id','category','slug','utterance','stimulus','perception','decision','anticipation','action','consequence','camera','audio','failed_pattern','repair_strategy','primary_channel','status']
    writer=csv.DictWriter(fp,fieldnames=fields);writer.writeheader()
    for r in recipes:writer.writerow({k:r[k] for k in fields})
print('Created',len(recipes),'action recipes + index + JSON + CSV')
