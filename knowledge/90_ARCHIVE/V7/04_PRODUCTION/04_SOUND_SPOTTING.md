# Audio spotting and narrative cue design — planned event map

**This is NOT finished audio.** It is the instruction map that a sound designer uses with actual rendered contact-frame events. Approximate windows are planning regions. `CONTACT_LOCKED` events must be updated after animation export; `LEAD_INTENTIONAL` and `TAIL_CONTINUITY` have deliberately offset timing.

## Scene spotting map

| Scene/time | Intent | Cue and perspective | Sync class | Music function | Acceptance |
|---|---|---|---|---|---|
| S01/0–1.6 | World / door arrives | Forest bed under airy portal bloom; opening has near/far dimensional quality | VISUAL/LEAD | Very sparse, optional | Sound opens with aperture and does not drown viewer's sense of place |
| S01/1.6–6.4 | Person crosses | Interior breath, contact-linked near-side shoes, flexible rim reaction | CONTACT_LOCKED | Hold | Actual foot contacts coincide with floor sound |
| S01/6.4–9 | Wonder | Small breath + overhead foliage movement | VISUAL/TAIL | Curious motif can emerge | Head/eyes react before accent |
| S02/9–12 | Threat foreshadowed | Distant heavy step from east/right, loose nest leaves | LEAD_INTENTIONAL | Low tension not yet danger | Audience may hear mother before see her; egg wobble has physical cause |
| S02/12–19 | Egg rescue | Twig rattle, small egg roll, catch transient, shoe recovery, second heavier step | CONTACT_LOCKED / TAIL | Pull back during catch | Egg can be tracked with ears; catch on visible hands |
| S03/19–25 | Mother revealed | Weighted foot + debris; searching breath | CONTACT_LOCKED | Low restrained harmonic color | Foot sound scales with visible distance and size |
| S03/25–30 | Fear | Mother inhale then protective roar; human gasp follows | VISUAL/TAIL | Duck under roar | Roar follows egg recognition; human fear follows roar |
| S04/30–39 | Chase starts | Actual human foot contact/gait plus delayed heavier dinosaur contacts; breath | CONTACT_LOCKED | Rising pursuit pulse | Dinosaur closes distance and audio rhythm matches pace |
| S04/39–46 | Obstacles | Branch strike and fragments; root scrape + stumble recovery | CONTACT_LOCKED / TAIL | Small rhythm dislocation | Impact exactly when collision physically occurs |
| S05/46–49 | Focus shifts | Tiny shell crack, close human breath, spectral duck of environment | SUBJECTIVE / CONTACT | Score withdraws | Crack actually audible and causally interrupts running |
| S05/49–56 | Baby and mother braking | Small shell snaps/chirp, mother skid/drag with delayed tail movement | CONTACT_LOCKED / TAIL | Very restrained warm transition | Mother hears chirp before braking; shell opens visibly |
| S06/56–63 | Caregiving | Baby foot/hand transfer, little toddles, soft snout touch | CONTACT_LOCKED | Warm motif waits | Release and nuzzle match actual picture |
| S06/63–66 | Acceptance | Soft mother exhale, baby chirp toward human | VISUAL/TAIL | Warm motif responds to recognition | Motif does not announce emotional state before acting |
| S07/66–71 | Goodbye | Human feet, portal activation sustained, apartment acoustics begin to prelap on crossing | CONTACT_LOCKED/LEAD | Curious motif returns | Actor stays visible in correct crossing states |
| S07/71–74 | Follower | Tiny dash/chirp, mother breath/alarm after notices absence | CONTACT_LOCKED / TAIL | Playful then pause | Baby decision reads in muted view too |
| S08/74–76 | New room | Dry apartment room tone, contact on carpet and baby landing | CONTACT_LOCKED / BRIDGE | Sparse | Forest→room transition has plausible acoustic change |
| S08/76–80 | Comedy reveal | Baby chirp, portal tension, rim strain, close mother breath, sting | LEAD / CONTACT / TAIL | Precisely timed comic punctuation | Snout passes physically and sound doesn't spoil too early |

## Event and cue schema

Every cue should have at minimum:

```
cue_id, event_id, scene_id, shot_id,
source_asset, license/provenance,
anchor_frame (null while unrendered), start_frame/end_frame (null if pending),
sync_class (CONTACT_LOCKED/LEAD_INTENTIONAL/TAIL_CONTINUITY/SUBJECTIVE),
world_position, camera/listener POV, perceived_distance,
frequency_or_texture, track_stem, priority (PRIMARY/SUPPORT/BED),
audibility_test, verified_asset_file, status
```

Examples: `S01_FOOT_LEAD` resolves actual contact event at render time; `S02_MOTHER_OFFSCREEN_01` intentionally begins before mother shown; `S05_CRACK_01` anchors to first actual shell crack and requires score reduction. Don't fill the event file with guessed timestamps and claim it is synchronized.

## Director's sound attention budget

- When footsteps/portal crossing are the story event, they get foreground transient attention; forest bed supports.
- During mother reveal, a low advance then sudden close weight effect cues scale; mother's searching breath has space.
- During chase, footfalls and breath articulate pursuit; don't stack generic whooshes on every cut.
- At hatch, cut clutter: the soft crack and baby chirp should feel physically small but emotionally enormous.
- During reunion, score should enter after the change in attitude, not sell the moment prematurely.
- For apartment reveal, room tone change and baby chirp establish false safety; portal tension reveals danger before snout; a sting punctuates at payoff.

## Mix/export checklist

48kHz internal masters where possible; separate stems and metadata; original or cleared rights only; determine online target empirically and by current platform specs; avoid clipping/distortion and unmotivated compression; true-peak and loudness measurements; stereo and mono checks; on-device playback; audio-only review and actual MP4 spot check.
