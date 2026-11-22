# Red-team review: how to find flaws even when a render looks polished

Reviewers must try to disprove completion, not merely list what seems impressive. Use scene direction and generated actual frames. These questions are intentionally hostile to superficial output but constructive in repair.

## The eight deception traps

1. **Semantic substitution:** Prompt says “steps through portal”; visual shows person passing a glowing circle. Check fractional containment/occlusion from inside to outside.
2. **Camera camouflage:** Camera zoom, flash, whip-pan or smoke hides the exact frame a catch/crossing should occur. Disable effects or render debug view.
3. **Motion blur camouflage:** Fast movement looks fluid but underlying poses/joints pop. Render without blur and inspect adjacent frames.
4. **Sound camouflage:** Footstep/impact audio suggests an event not visible in video. Mute and recheck physical cause.
5. **Style camouflage:** Beautiful paper texture hides incorrect knee pivots and detached arms. Overlay skeleton/rig debug.
6. **Montage camouflage:** Storyboard verbs are split across cuts so nothing visibly happens. Verify continuous actor/object trajectory.
7. **Label camouflage:** “COMING THROUGH”, “ROAR” or “RUN” is text that narrates an action the puppet failed to perform. Remove captions and retest.
8. **Metrics camouflage:** Encoder integrity, deterministic seek and passing unit tests are presented as “professional animation QC.” Separate mechanical health from story/acting judgement.

## Critical old-project regression list

From first DINO four-style audit: flat enters/incorrect portal crossing, style variants sharing identical choreography, huge per-frame jumps without appropriate blur, gait switches with foot slip, unconvincing pursuit, premature mother appearance, risky title/safe area, mechanical Foley timing. Reuse the old audit findings as *negative tests*; do not assume new film inherits exact old bugs until visual inspection.

## Structured inspection

For each A## shot fill:

```
INTENDED: [what viewer must learn, what actor visibly does]
ACTUAL: [observed frame/sample and audio]
CONTRADICTION: [exact difference; none if evidence matches]
WHY: [rig, blocking, world/camera, asset, editor, audio, story]
REPAIR: [minimum change capable of fixing cause]
REGRESSION: [what adjacent beats could break]
STATUS: [open/fixed/verified]
```

## Mandatory reviewer questions

- Is the actor oriented toward actual movement, or does camera translation fake movement?
- Do the dinosaur and human demonstrate different masses and inertia?
- Does new information arrive before reaction? If not, is the exception deliberate, like anticipatory sound?
- Does the camera show the evidence of the event, or mostly the aftermath?
- Has audio been designed from source/POV, or simply added to fill silence?
- Does the color/light/material obey location and scene motivation?
- Is the audience given enough time to recognize the baby and mother's emotional change?
- Does the follow action have a clear planted motive from the preceding scene?
- What is one failure a casual viewer may not notice but an animator must still repair?

## Escalation after two failed repair attempts

Stop changing random easing values. Isolate an 8–30-frame debug range, simplify to primitive shapes, visualize hinges/contacts/portal plane, test behavior without camera movement and blur, then reintroduce layers one by one. Fix source hierarchy or state logic if necessary. Document result and update status. If tool cannot render/inspect actual frames, report as BLOCKED and do not claim visual QC.
