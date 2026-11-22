# Sound, music and audio perspective — film/TV/animation rules adapted for mobile

**Evidence anchors:** S04/S05/S11/S12/S13/S14/S15/S19. **Most important new rule:** sound is a *storytelling perspective*, not a list of SFX attached to visuals. In animation, physical sound must be designed; silence/quiet and offscreen sounds are valid narrative choices.

## The seven questions before adding any sound

1. What is the physical source? If there is none, is it an intentionally subjective/non-diegetic signal?
2. What does the audience need to know or feel from this cue?
3. Who hears it: human, mother, baby, or an omniscient audience?
4. Where is the source relative to the camera/character (distance, direction, barrier, location size)?
5. Does it arrive **before**, **on**, or **after** the visible event, and why?
6. What must be quiet so this cue reads (masking, spectrum, spatial separation, dynamic level)?
7. What carries the acoustic space through the cut (ambience, early cue, decay, silence)?

## Sonic perspective (select deliberately per beat)

- **Objective/diegetic:** believable forest bed, mother footsteps from offscreen right approaching, rustle of paper-like grass. Supports location and physical continuity.
- **Subjective/point-of-audition:** human fear causes mother breath and heartbeat to become disproportionately present, or background to duck before a roar. Supports a character's inner experience; it is not literal physics. Signal the perspective change with visual acting and return gracefully.
- **Audience/editorial sound:** sound prelap/J-cut: low thud is heard while mother remains unseen, creating anticipation. Designed sting on apartment snout reveal is non-diegetic punctuation. These are acceptable if specified.

Sound can be **before image** (offscreen warning), **exactly with image** (foot contact), **after image** (branch debris settling), or **across cut** (forest sound bridges portal). Labelling every sound “sync to current frame” is incorrect.

## Sound layers and production stems

| Stem | Purpose | Examples | Risk |
|---|---|---|---|
| `AMB_FOREST` / `AMB_APARTMENT` | Acoustic location and continuity | Wind/insects/birds; indoor air hum | Beds abruptly restart at edits |
| `FOLEY_HUMAN` | Physicality of small character | Shoes on leaves, hand grip, fabric/paper rustle | Random evenly spaced steps |
| `FOLEY_DINO` | Mass, weight, directional movement | Foot impacts, contact grit, tail/foliage | Giant LF boom inaudible on phone |
| `FOLEY_PROP` | Clarify causal actions | Egg roll, catch, shell crack, baby contact | Sound says action happened but image doesn't |
| `SFX_DESIGNED` | World/portal/physical emphasis | Spectral portal energy, crack, branch break | Clichéd whooshes masking dialogue/action |
| `VOX_CHARACTER` | Meaning and emotion without dialogue | Surprise gasp, mother breath, baby chirp | Human-like speech where not needed |
| `MUSIC` | Emotion, motif and rhythm | Curiosity, threat, gentle reunion, comic sting | Wall-to-wall intensity; lack of contrast |
| `DIALOG_VO` (optional) | Narration only if specifically selected | Potential accessibility/story variant | Narration replaces visible event |

Maintain separate 48kHz WAV masters or suitable editable stem format; final mix may be stereo AAC. Project decisions, not universal requirement: name stems consistently and retain licensing provenance.

## Foley is grounded in contacts

Mark frame-level animation events before placing contact SFX. For example `human_left_foot_plant`, `egg_hand_contact`, `mother_foot_plant_03`, `egg_shell_split`, `baby_feet_on_ground`. Each event has a frame index, spatial location, material, force and perspective. Follow-through sound may continue after contact, and distant rumble may precede a visible footfall if the source is offscreen.

A heavy dinosaur step is a layered composite: contact transient (reads on phone), mid-frequency body/ground crunch, short low-frequency mass component, displaced foliage response, and decay. A baby step needs a distinct timbre and scale. A fully synthetic paper-cut film may use stylized timbres; coherence matters more than literal Foley realism.

## Design the film's sonic identities

**Portal:** soft high shimmering opening + lower resonant dimensional tone; spatial tension at rim; slight pitch/texture shift when a body crosses; acoustics change on other side. Avoid a repeated generic sci-fi whoosh for every portal micro-movement.

**Human:** small, close foot/cloth sounds; nervous inhale before pivot; catching breath after sprint; absence of speech helps silent comprehension.

**Mother:** distant rhythmic ground thuds preceding reveal, detailed foot/foliage at camera proximity, inhalation preceding roar, tail/neck movement after stop, softer breath at reunion. Roar occurs *after* she recognizes egg in human's hands.

**Egg/baby:** egg lightly rolling on nest, catch hand thump with shell rattle, brittle cracking, baby gasp/chirp; these close transient details become foreground at emotional reversal.

**Forest/apartment:** outdoor open/high diffusion vs small, comparatively dry indoor reflections; the transition through portal may lead sound from destination before the full visual crossing, but the effect must not imply the character teleported before it crosses.

## Music as narrative pressure, not a wallpaper

- **0–9 discovery:** sparse curious motif, give portal and footsteps sonic space.
- **9–19 rescue:** quietly tighten pulse only after egg risk is perceived; protect falling/catch details.
- **19–30 mother:** low harmonic suspense, drop under recognition; roar takes priority.
- **30–46 chase:** rhythmic energy rising with actual pursuit dynamics, not every beat emphasized by orchestral hits.
- **46–56 hatch:** music withdraws before crack so micro-sounds are heard; tentative warm motif only after hatch is recognized.
- **56–66 reunion:** warm return of motif after physical handoff and mother’s softened response; avoid cue arriving before emotion.
- **66–74 follower:** playful motif, a brief gap as the baby makes its decision.
- **74–80 reveal:** apartment stillness and baby's chirp, rising portal tension, punchline sting on snout reveal; cut/decay chosen deliberately.

Musical leitmotifs are optional; if used, define small melodic/rhythmic identities, original or appropriately licensed. Do not borrow protected film themes.

## Sonic transitions and perspective shifts

- **J-cut:** approaching mother step is audible before the shot reveals her. Viewer knows danger while human may not, producing dramatic irony or tension.
- **L-cut:** mother's exhale or branch debris can continue after picture cuts, preserving physical space and cause/effect.
- **Ambience bridge:** forest bed carries across close-ups to maintain place; apartment air replaces it gradually/at a motivated threshold.
- **Subjective narrowing:** when human hears shell crack, duck wider chase percussion and retain close brittle detail, perhaps lightly filtering the distant dinosaur for a short moment. Restore world audio after recognition.
- **Constructed silence:** intentional removal of score and some ambience can heighten hatch; absolute digital silence is not automatically the most natural or effective choice.

## Timing rules

- Frame 0 of rendered film is time 0. At 30fps, frame N starts at N/30 seconds; events should use frame indices as truth.
- Contact: sound transient should align to visible contact frame as closely as the format/medium permits (inspection required). Artfully anticipatory breath or pressure can lead the contact if source is clear.
- Heavy impacts may include low-frequency pre-rumble, an onset transient and delayed rustle/decay; document each component relative to the master contact.
- Do not derive a 2Hz footstep loop from a constant clock when gait speed changes; events must follow pose/contact state.
- Music can anticipate a narrative event if used deliberately, but should not accidentally spoil the baby reveal or scare the viewer before characters perceive danger.

## Mix and engineering checks

1. Target **YouTube web/phone** for this project, not a broadcast TV -23 LUFS specification by default; verify platform's most current specs at delivery.
2. Capture/edit at 48kHz where feasible; produce final codec/container consistent with YouTube's supported guidance.
3. Inspect integrated loudness, loudness range, sample/true peaks, clipping, phase coherence, mono sum and phone speaker performance. Do not invent a single mandatory LUFS value where the destination has not specified one.
4. Headphones: spatial coherence and transient detail; phone speaker: midrange impacts and clear baby chirps; quiet speakers: intelligible cause/effect.
5. Prevent masking with gain staging, arrangement, frequency balance, selective ducking, not automatic heavy compression of everything.
6. Verify actual MP4 soundtrack exists and is aligned; check with `ffprobe` and listen to export, not only stems.
7. Save the audio source/creator/license/permission and any required credit for each external sample.

## Audio quality review in four modes

A. **Foley/SFX without score:** Can a listener hear where and when objects touch and character mass changes? B. **Ambience/character only:** Is the location and emotional perspective coherent? C. **Music+full mix:** Does it lead feeling without overpowering story? D. **Blind audio-only:** Can listener roughly infer portal, footsteps, threat, crack, baby, reunion and room change? Do not require audio alone to tell every visual detail, but it should support essential beats.

## Corrective matrix

| Symptom | Diagnose | Repair |
|---|---|---|
| Mother roar feels random | Was recognition visible; is inhale/roar timed? | Fix motivation/pose before roar placement |
| Chase has no intensity | Is dinosaur closing distance? Is rhythm dynamic? | Correct pursuit physics; then increase cue urgency |
| Step sounds mechanical | Are loops fixed-time? | Generate step timestamps from contact states |
| Egg crack unheard | Spectral masking/music over event? | Pull back score/ambience, spotlight close crack |
| Portal feels flat | Does sound change as character crosses? | Modulate spectral/space cues tied to threshold |
| Audio jarring at cuts | Bed reset or perspective jump? | Add continuity bed, prelap/decay, re-evaluate listener POV |
| Huge impact absent on phone | LF-only design | Add short defined midrange transient and material response |
| Mix appears loud but lifeless | No dynamic contrast, all stems competing | Create quiet/peak structure and prioritize one focal cue |
