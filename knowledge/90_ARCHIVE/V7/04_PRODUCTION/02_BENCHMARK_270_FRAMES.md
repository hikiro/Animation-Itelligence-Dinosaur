# S01/A01 — 270-frame cinematic benchmark: physical emergence through portal

**Single continuous shot, frame indices 0–269, output 1080×1920 at 30fps.** Planning timing is an acceptance target, not a record of rendered work.

## Why this shot exists

Prove beyond ambiguity that the traveler originates INSIDE a portal and physically steps OUT, with correct material depth, planted-foot transfer, whole-body follow-through and deliberate audiovisual perspective. If the shot fails, the underlying animation system is not ready for the 80-second film.

## Camera and visual context

- Viewer question: “What is that doorway, and who is coming through it?”
- Dominant idea: **actual threshold crossing**; no camera trickery.
- Camera: side-on/light three-quarter 2.5D medium-wide or full shot, locked through full exit; portal left-middle, destination clearing center/right, world-ground line visible, warm forest with cyan portal accent.
- Ground baseline: set physically in project world coordinates and keep portal base, foot contact, shadows aligned. Example for screen-space blocking only: ground around y=1450, portal aperture height enough for puppet and x≈390; derive exact values from design sheet. These are **not verified rig coordinates**.
- Portal layers: `far background → portal back rim → aperture/interior showing origin space → crossing actor body mask (inside/outside state) → front rim in front when appropriate → foreground ferns`. Test with debug coloring before art.
- Actor never enters from x<0 or a screen edge. If actor starts hidden, it is hidden *by portal aperture geometry*, not because it is out of the canvas.
- Primary modality: character/threshold; supporting: portal illumination and restrained location sound. No music hit or camera shake that obscures the silhouette.

## Frame blocks and proof images

| Frame span | 30fps time | Intended poses/states | Camera/sound | Proof to capture |
|---|---|---|---|---|
| F000–047 | 0.00–1.60 | Portal opens from cyan seed, bottom grounded, nearby foliage flexes. Human totally internal/hidden. | Camera fixed; forest amb, portal opening sound ramps. | F000, F024, F047; empty visible exterior |
| F048–083 | 1.60–2.80 | Head appears within aperture, hand tests edge; head/eyes scan before torso. | Quiet breath/interior rustle, no offscreen entrance. | F048, F060, F083, front/back mask debug |
| F084–125 | 2.80–4.20 | Torso leans, leading knee/foot pass portal plane and leading foot PLANTS outside. COM starts over foot. | Contact event is read from ACTUAL foot plant, not guessed. | F084, knee crossing, 5 consecutive pre/contact/post frames |
| F126–191 | 4.20–6.40 | Pelvis crosses threshold; trailing leg detaches from inside support and clears; trailing foot plants outside. | Secondary fabric/portal shimmer and second foot plant. | Pelvis before/after threshold, trail foot clearing, F191 full exterior |
| F192–215 | 6.40–7.20 | Balance recovery, knee compression, chest/arm follow-through, breathing. | Space calms; portal remains open. | F192, F205, F215; support and shadow |
| F216–269 | 7.20–9.00 | Eyes move up toward giant fern, head follows, small delighted lean/gasp. | Ambient foliage and light curious sound; music optional/minimal. | F216, F240, F269; gaze order and expression |

**Critical sequence proof:** at least one image clearly shows human **partly inside and partly outside** the portal with appropriate rim occlusion; another shows both feet outside and full body cleared. Without both, fail.

## Actual event log format (do not fabricate frame numbers)

```json
{"event_id":"human_lead_plant","frame":null,"state":"PLANNED","world_x":null,"world_y":null,"source":"ground_contact_solver","sync_class":"CONTACT_LOCKED"}
{"event_id":"human_full_exit","frame":null,"state":"PLANNED","source":"portal_crossing_state","sync_class":"VISUAL_PROOF"}
{"event_id":"human_trail_plant","frame":null,"state":"PLANNED","world_x":null,"world_y":null,"sync_class":"CONTACT_LOCKED"}
```

Fill `frame` from actual finished animation data after rendering and inspecting. Do not invent exact contact frames because the planning intervals do not themselves specify them.

## Character pose plan and force

- **Head/eyes:** eyes inspect clearing before torso leads into danger.
- **Hand:** one hand braces/interacts with rim without physically grabbing an impossible energy surface unless portal design explains resistance.
- **Lead foot:** ankle/sole shifts from far-side hidden to outside visible, strikes ground, absorbs weight; world position stays nearly fixed during stance.
- **Pelvis/torso:** rotate and transfer over lead foot; do not move rigid puppet as one layer.
- **Trail foot:** moves from inside to outside; if occlusion absent, reveal will look like teleportation.
- **Final settle:** arms lag, shoulders relax, breath and curiosity micro-actions.

## Sound contexts

- `amb_forest`: continuous local outdoors with subtle direction; sounds persist throughout.
- `portal_open` (`LEAD_INTENTIONAL` for aperture growth): starts with visual activation, gains width/depth.
- `inside_rustle` (`CONTACT_LOCKED` or local) as body emerges from aperture.
- `foot_lead` and `foot_trail` (`CONTACT_LOCKED`) generated from ground contact solver.
- `human_breath` (`CHARACTER`) near settle; curiosity gasp after visual gaze change.
- `portal_bed`: remains while open; never sudden mute when full exit occurs.

## Review methods

1. Render *debug* mode showing portal plane, back/front rims, actor mask and foot anchor points.
2. Render visual-only normal mode; inspect sequential frames, not only at fixed 1-second samples.
3. Render sound pass. Play full 9 seconds on phone and headphones. Confirm foot sound event matches visible plant.
4. Measure foot velocity while stance true; flag world-space drift above design tolerance. Tolerance should be chosen after rig scale, not guessed universally.
5. Compare eye motion onset before head/body look, and confirm no facial/pose popping.
6. Confirm F000..F269 deterministic at arbitrary seek and no frame-to-frame scale shifts.
7. Record evidence in defect log; no pass on prompt text alone.

## Explicit rejection checklist

- [ ] Human comes from screen left instead of portal interior.
- [ ] Portal bottom floats above character ground line.
- [ ] Actor drawn entirely in front of rim during partial crossing.
- [ ] Body parts appear/disappear instantly instead of following threshold.
- [ ] Lead foot skates after contact, body center of mass never transfers.
- [ ] Camera crops the foot/rim or excessive zoom disguises crossing.
- [ ] Sound gives a false footfall or portal exit before visible action.
- [ ] Technical output missing, not seekable, absent audio, or unverified.

The checklist items above are **reject conditions**: a checked observation means failure. Don't reverse their meaning when marking QC.
