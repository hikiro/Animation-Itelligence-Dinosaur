# THE CORE LEARNING — Context is the director of camera, motion and sound

This is the most important transferable new material in V3. Camera, motion and sound should not be chosen independently. Their **shared reason for existing** is the viewer's changing understanding of the story.

## The contextual directing algorithm (CDA)

For each beat `b`, fill:

```
C = character goal + emotional state + current knowledge
T = trigger/event source (visible/offscreen/subjective)
A = actor action (eyes -> anticipation -> movement -> contact -> consequence)
V = viewer question or information gap
CAM = subject, POV, frame, axis, start/end, move/hold, reveal timing
SND = source, audience POV, distance/timbre, timing relative to T/A, priority
EDIT = cut/hold, eyeline and geography, sound bridge
TEST = what silent view proves + what SFX-only view proves + what full mix proves
```

Then ask in order: (1) Does action actually happen? (2) Can the camera prove it? (3) Does sound clarify or complicate it? (4) Does the combined effect make the intended emotion/readability stronger? If no, redesign. Do **not** solve an unsolved action with a sound effect or camera shake.

## Three viewpoints to distinguish

1. **Character POV:** what this person or dinosaur notices at this exact moment. They may be unaware of an offscreen mother or may hear a distant thud.
2. **Audience knowledge:** viewer may hear mother first, creating dramatic irony before human realizes danger; or viewer may know no more than human, creating surprise.
3. **Camera/audio narrator:** editorial system may withhold an image, use an offscreen footfall, switch to a reaction shot, or hold a visual longer to build comprehension.

An effective sequence may choose **audience knows more than human** (distant stomp, looming foot), then **human hears/thinks**, then **audience shares human fear** (close breath and narrowed soundscape). These transitions should be intentional, not accidental.

## Context matrix — concrete director decisions for the film

| Beat | Audience state | Character decision | Camera | Motion | Audio | What could go wrong |
|---|---|---|---|---|---|---|
| Portal opens | Where are we? | Human tests unknown world | Locked wide; hold horizon/ground/portal | Aperture opens, foliage responds, body begins INSIDE | Soft shimmering portal + stable forest bed | Fancy orbit hides impossible crossing |
| First step | Is it real? | Human trusts ground | Full-body/ground frame, no cut | Foot crosses plane, plants, COM shifts, trailing limb clears | Small threshold timbre changes then foot plant, no unrelated whoosh | Foot appears from left edge, sound fakes exit |
| Egg wobbles | Will it fall? | Human spots danger | Eyeline from human to egg, readable ledge | Nest shakes then egg begins controlled roll | Distant thud causes wobble; rolling sound tightens focus | Egg moves before cause, viewer doesn't see risk |
| Catch | Can he save it? | Human leaps to intercept | Hold hands/egg/ground in shot | Anticipation, reach, egg-hand contact, recovery step | Short tactile catch transient + rustle after contact | Insert cuts before catch or egg teleports |
| Mother approaches | What made thud? | Mother checks nest | Ground-scale reveal; mother's eyeline to egg | Heavy foot plant, head scans, gaze narrows | Offscreen foot thuds become closer, LF+mid texture | Roar before mother recognizes egg |
| Roar | Is he in danger? | Mother warns; human fears | Low angle mother then readable reaction, axis clear | Inhale, open jaw, full-body roar; human recoils AFTER | Rise of breath then roar, forest bed dips selectively | Human recoil pre-dates roar |
| Fleeing | Will he escape? | Human protects egg and escapes | Side tracking shows physical separation | Attempt to lower egg; mother too close; pivot; sprint | Breath/push-off and event-synced footfalls; score pulse | Human looks wrong way, dinosaur does not gain ground |
| Branch collision | Can he navigate? | Human ducks; mother plows | Establish branch ahead; hold crossing/impact | Duck under, branch bends/snaps on mother contact | Swish before branch, snap AT hit, leaves scatter after | No visible branch before impact |
| Shell crack | What changed? | Human listens and brakes | Tighten from motion to stillness; insert only AFTER decel begins | Eyes drop; whole body decels; shell cracks | Music retreats; tiny crack foreground; subjective narrowing | Music masks crack, instant frozen running pose |
| Baby appears | Is it alive? | Human reassesses; mother recognizes | Close detail then shared reaction | Shell displacement and baby emerge; dinosaur skid/tail lag | Chirp is small but focal, mother's heavy braking trails | Baby teleports in and mother stops without hearing |
| Reunion | Is mother safe? | Human gives baby back | Baby-level two-shot then held frame | Careful lowering, planted baby feet, mother nuzzles | Small footsteps, soft breath, delayed warm motif | “Cute” audio starts before characters understand |
| Baby follows | Will it stay? | Baby chooses human | Portal/nest geography wide, eye-trace to opening | Looks at distracted mother then portal, runs, crosses | Brief chirp, departing portal sound; mother alarm AFTER | Mother sees baby but inexplicably doesn't stop it |
| Apartment reveal | Did adventure end? | Human sees baby; mother pursues | Hold domestic reveal, push-in only at snout | Two actual portal exits; rim stretches under mother force | Apartment room tone vs forest, rising physical tension, sting at reveal | Snout appears without crossing/portal motion |

## The “attention budget” law (a project heuristic)

For each beat, allocate primary attention among **character performance**, **camera move**, **sonic event**, **text/graphics**, **environmental motion**. If all five are loud, none can lead. During first foot contact, actor geometry must dominate. During mother reveal, controlled camera angle + offscreen footfall can dominate while character stays comparatively still. During shell crack, reduce score and camera motion; let the tiny egg state change lead.

An implementation rule: assign one `PRIMARY` and up to two `SUPPORT` modalities on every shot card. Other modalities should maintain continuity without stealing focus. A deliberate exception is allowed but must be explained.

## Motivated vs unmotivated — rapid tests

**Motivated camera:** “We need to see that the first foot plants beyond the portal, so we lock the camera and include ground and opening.”

**Unmotivated camera:** “Let's zoom fast because scene starts slow.”

**Motivated sound:** “A distant step establishes the mother's approach before she enters frame; it also causes the egg to wobble.”

**Unmotivated sound:** “Add four trailer booms because dinosaurs are dramatic.”

**Motivated animation:** “Human recoils after roar, shifts balance and flees to protect the egg.”

**Unmotivated animation:** “Loop running cycle while x translates.”

**Motivated silence:** “The tiny shell crack interrupts the chase rhythm, so most music drops away while breath/crack remain.”

**Unmotivated silence:** “Delete all audio in emotional moment with no cue or bed continuity.”

## Audio-first, picture-first and simultaneous beats

A professional sequence may begin from **audio** (offscreen stomps leading picture), **motion** (human sees egg tipping, body reacts), or **camera/editorial withholding** (hold human reaction before showing its object). There is no universal order of stimulus in sound vs image. What matters is whether the causal information is intentionally revealed and intelligible.

Use three synchronization labels in cue sheet:
- `CONTACT_LOCKED`: on the actual rendered collision/foot plant frame (e.g. `egg_catch`).
- `LEAD_INTENTIONAL`: warning, anticipation, inhale, J-cut or subjective cue BEFORE picture event.
- `TAIL_CONTINUITY`: decay, debris, breath, ambience or L-cut AFTER/ACROSS edit.

## Feedback loop across departments

A camera edit changes what sounds near/far; sound can motivate a camera reveal; changing gait speed changes footfall timestamps; changing character staging can necessitate an eyeline recut. Therefore every significant change triggers a **dependency check**:

```
Story beat change -> script + shot cards + motion + camera + cues + QA
Contact timing change -> events + Foley + score sync + QA
Camera angle/cut change -> screen axis + scale + eye-trace + sonic perspective + QA
Visual asset/rig change -> silhouette + collision shapes + contacts + shadow/sounds + QA
Audio change -> story inference + listening perspective + editorial rhythm + QA
```

## Context review exercise for another chat

Before animating ANY unfamiliar scene, require a 7-column direction table:
`what audience knows | what actor knows | action and cause | visual framing | sound perspective/timing | edit consequence | silent/SFX-only proof`.
Reject a shot card missing actor knowledge or an event's consequence. This forces the agent to think as a director rather than merely applying an effects checklist.

## Failure demonstration

Bad beat: At 3.2 seconds a dinosaur sprite enters from right, camera shakes, roar plays, human instantly glides left, upbeat chase track starts.

Correct beat: Offscreen thud causes nest tremble → human's attention goes egg → mother physically enters, scans nest and notices egg held by human → mother narrows pupils, inhales and roars → sound moves from offscreen thud to near roar; human recoils, decides he cannot safely place egg, pivots and pushes off; side-tracking shot shows distance closing. Each component communicates the **same** cause-and-effect story.
