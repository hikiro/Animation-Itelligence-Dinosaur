# AE expressions: what code means in normal creative language

**Scope:** These are property expressions (AE JavaScript engine); they output a property's value at each evaluation time. They are not After Effects project-creation scripts, and they do not create full narratives. See [Adobe expression reference](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html), [expression basics](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-basics/expression-basics.html), [examples](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-examples/expression-examples.html), [controls](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-controls/expression-controls.html).

| Method/operator | What code actually does | Describe it to a noncoder | Good context / risk |
|---|---|---|---|
| `time` | Current comp time in seconds | “Use the current playback moment” | Procedural rotation; not a hit trigger by itself |
| `value` | Pre-expression property value | “Start with the pose I already keyframed” | Preserve animation and add minor response |
| `wiggle(freq,amp)` | Procedural spatial/value fluctuation around base | “Make it tremble at a chosen frequency and distance” | Ambient tremor, small post-hit shake; no collision timing, no intent |
| `ease(t,t0,t1,a,b)` | Smooth interpolation between numbers/vectors | “Accelerate then settle through an interval” | Smooth reaction envelopes; easing can harm intentional sharp contacts |
| `linear(t,t0,t1,a,b)` | Linear interpolation | “Move at an even rate in this interval” | Meter values, progress, carefully chosen sections of travel |
| `easeIn`, `easeOut` | Asymmetric easing variants | “Start gentle/finish fast” or “start fast/finish gentle” | Use with planned pose timing; check direction carefully |
| `loopOut("cycle")` | Repeat keyed motion pattern | “Repeat this walk or background cycle” | Requires a properly animated base cycle; does not fix foot sliding |
| `loopOut("pingpong")` | Reverse and repeat keyframed cycle | “Oscillate back and forth” | Pendulum-like effects, avoid repeating one-off impacts |
| `valueAtTime(t)` | Sample property at another timeline time | “Follow the leader a moment later” | Tail/head follow-through; may introduce lag and intersections |
| `velocityAtTime(t)` | Sample rate of property change | “Use how fast the thing was moving” | Inertial settle/overshoot; keyframe continuity and units matter |
| `smooth(width,samples)` | Smooth samples of property over time | “Filter jitter in a noisy control” | May erase an intended snap/contact; not a gait fix |
| `posterizeTime(fps)` | Reduce evaluation cadence | “Make this procedural animation step like stop motion” | Paper-cut jerk rhythm; not the final composition frame rate |
| `seedRandom(seed,true)` | Make pseudorandom values repeatable | “Give each particle a consistent personal variation” | Consistency; usually pair with `random()` |
| `random(min,max)` | Sample pseudorandom value | “Make different elements slightly varied” | Seed for stable variation; avoid uncontrolled changing contact |
| `Math.sin`, `Math.cos` | Smooth periodic functions | “Create a rhythmic oscillation” | Breath/bob/tail oscillation; not every action should loop |
| `Math.exp` | Exponential growth/decay | “Let a shock fade away quickly” | Decreasing impact shake, settle, ambience modulation |
| `Math.atan2(y,x)` | Angle to a 2D vector | “Make an object point along its movement direction” | Directional streaks; local-axis/coordinate checks |
| `toComp(point)` | Convert local point to comp-space coordinates | “Find the hand's actual screen position” | Attach egg effect/flash in compositing coordinates |
| `fromComp(point)` | Convert comp-space to local coordinates | “Turn a screen contact location into this layer's coordinates” | Correct parenting and occlusion |
| `length(a,b)` | Distance between points | “How far apart are the characters?” | Proximity cue, camera framing; not enough to infer awareness |
| `sourceRectAtTime()` | Bounds of source/text | “Fit a caption box to text rather than oversizing it” | Responsive title/caption cards; verify anchor positions |
| `thisComp.layer("...")` | Reference another named layer | “Drive this motion from the character's controller” | Rigs and coordinated effects; exact layer names are required |
| `effect("Name")("Slider")` | Read control value | “Expose an artist-friendly knob” | Controls for impact strength/decay, camera shake amplitude |
| `marker.nearestKey(time)` | Find nearest marker | “Time an effect to its declared story beat” | Must validate marker name and whether next/previous event applies |
| `clamp(value,min,max)` | Bound output | “Prevent effect intensity from exceeding safe limits” | Opacity and distortion; AE engine/version check |

## Key conceptual traps

- Expressions do **not** automatically infer a shot's emotional meaning. A random wiggle may communicate fear, comedy, machinery, or a bad render depending on context.
- A single property expression cannot physically react the whole character unless the rig is wired to share an event/control and each relevant layer participates.
- Property expressions cannot be used interchangeably with `.jsx` ExtendScript creation scripts. AE JavaScript expressions and JSX scripting have different execution contexts and capabilities.
- Coordinate conversion matters. Comparing a hand's local `Position` with a projectile in comp space is generally wrong until transformed to a common space.
- Technical snippets in this kit are **illustrative and not executed inside AE**. Test against installed AE version and real property dimensionality before use.
