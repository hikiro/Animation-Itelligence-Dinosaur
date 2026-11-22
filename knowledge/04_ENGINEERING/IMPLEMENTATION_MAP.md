# From normal-language direction to technology-specific implementation

| Human request | Story/context decision | Rig/scene channels | AE | Remotion/JS | QA |
|---|---|---|---|---|---|
| "Eyes notice first" | Target must be perceivable and attention precedes intent | eye target → head → torso | Separate face/head layers and parent chains, keyframe target | interpolate gaze/head rotation with distinct delays | Gaze starts only after event trigger |
| "Feet don't slide" | Stance foot in world coordinates | world root, hip, IK target, stance-state | Puppet/controller/null rigs or external rig solver | world contact lock plus inverse local transform | foot drift across stance |
| "He catches it" | Show hand-object contact, then change ownership | hand IK, prop transform and attachment state | parenting / expressions / track mattes with explicit handoff | deterministic state and transforms | no prop teleport, grasp frame visible |
| "Massive creature stops" | Braking inertia, body and appendage follow-through | root acceleration, contact, spine/head/tail offset | graph editor, FK rotations, constraints | piecewise time curves and dependent channel delays | body stops after support; tail later |
| "Through the portal" | physically cross depth threshold | front/back layer order and aperture mask | track matte, precomp, layered rig | clipping mask/scene graph or depth test | inside / straddle / outside evidence |
| "Make it cinematic" | Identify audience information goal first | camera path, lens/framing, lighting, edit | 2.5D camera + null rig, graph curves | animated world/camera transforms | motivation and continuity |
| "Heavy sound" | material, source/room, listener distance | contact emitter ID, spatial parameters | event-driven layers via audio edits | timeline event cues / external mix | waveform transient matches actual contact |

## Engineering rules
- Rig solved before effects. Contact constraints precede cosmetic shake.
- Camera transforms are separate from world coordinates and body pose.
- No single property expression can implement story logic, depth-aware portal crossing or collision by itself.
- Deterministic seeking: frame `f` must produce the same scene regardless of previous calls unless simulation is explicitly baked.
- Never port AE expression semantics to JS without checking units, color, coordinate conventions, time/frame and layer-parenting behavior.
- Source docs: SRC-005–SRC-009, archived V7 After Effects materials. These rows are proposed techniques (L2), not AE-render-tested code.
