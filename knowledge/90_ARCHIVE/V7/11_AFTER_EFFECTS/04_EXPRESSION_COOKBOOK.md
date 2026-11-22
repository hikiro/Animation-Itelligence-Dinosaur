# After Effects expression cookbook — code, normal-language translation, context, QA

**Status:** Examples drafted from Adobe's documented JavaScript-based expression API. They have not been executed or rendered in After Effects in this session. Paste into the specified property, use the exact control/layer names, and validate in a small AE test project before production. Code may require minor adjustment for property dimensions/version.

## E01: Background breathing — subtle living atmosphere

**Expression property:** `Position` on a 2D background foliage layer.

```javascript
var phase = index * 0.9;
var dx = 3 * Math.sin(time * 0.8 + phase);
var dy = 2 * Math.sin(time * 1.15 + phase);
value + [dx, dy];
```

**Plain language:** “Let background plants drift a few pixels out of phase with one another, slowly enough that viewers focus on the character.” `index` differs by layer, so clones don't all pulse together. **Do not** use as a replacement for leaf-specific pivoting or wind response.

## E02: Procedural shake after a registered event

**Setup:** Add a null `IMPACT_CTRL`, add Slider Controls renamed exactly `Hit Time`, `Shake Amplitude`, `Shake Frequency`, `Shake Decay`. Keyframe the `Hit Time` manually as a chosen global timestamp, or enter it on the slider. Put the following on a **2D camera-rig null's Position**, not every character joint.

```javascript
var c = thisComp.layer("IMPACT_CTRL");
var hit = c.effect("Hit Time")("Slider");
var amp = c.effect("Shake Amplitude")("Slider");
var freq = c.effect("Shake Frequency")("Slider");
var decay = c.effect("Shake Decay")("Slider");
var dt = time - hit;
var delta = [0,0];
if (dt >= 0 && dt < 0.45) {
  var envelope = amp * Math.exp(-decay * dt);
  delta = [envelope * Math.sin(2*Math.PI*freq*dt),
           envelope * 0.30 * Math.sin(2*Math.PI*freq*dt + 1.0)];
}
value + delta;
```

**Plain language:** “At the chosen hit frame, nudge the view sharply, then let the shake decay within roughly half a second.” **Limits:** Single hit trigger only; this does not create character recoil, contact or grounded physics. Distinguish an intentionally shaky POV from objectively still camera. If you need several hits, use markers/events or multiple controls. Avoid overusing screen shakes and repetitive flash patterns.

## E03: Head follows torso with delay, but preserve hand-crafted head acting

**Expression property:** `Rotation` of 2D `HEAD` layer. The head's existing keyframes are the primary acting; lag adds *small* secondary response.

```javascript
var torso = thisComp.layer("TORSO").transform.rotation;
var lag = 0.07;
var follow = (torso.valueAtTime(time - lag) - torso.value) * 0.18;
value + follow;
```

**Plain language:** “If the torso turns suddenly, the head momentarily trails, but the animator's deliberate gaze/pose remains primary.” **Pitfall:** This is just approximate lag, not an anatomical solver. Avoid double-counting parent rotation if head is already parented; verify with actual joint setup.

## E04: Impact compression in animated scale (2D)

**Setup:** `IMPACT_CTRL` with `Hit Time` slider. Expression goes on a 2D graphic's Scale; for character acting, prefer keyframed **pose** compression, using this only for a minor material accent.

```javascript
var t0 = thisComp.layer("IMPACT_CTRL").effect("Hit Time")("Slider");
var dt = time - t0;
var s = 0;
if (dt >= 0 && dt < 0.25) {
  s = 9 * Math.sin(2*Math.PI*9*dt) * Math.exp(-15*dt);
}
[value[0] + s, value[1] - 0.5*s];
```

**Plain language:** “Squash briefly, rebound, and settle.” **Pitfall:** Add on the appropriate layer/control, not a full articulated character rig without considering limb constraints.

## E05: Animated accent intensity at a contact frame

**Expression property:** `Opacity` of a short-lived impact accent layer. Setup `IMPACT_CTRL/Hit Time`.

```javascript
var hit = thisComp.layer("IMPACT_CTRL").effect("Hit Time")("Slider");
var dt = time - hit;
var out = 0;
if (dt >= 0 && dt <= 0.12) {
  out = easeOut(dt, 0, 0.12, 60, 0);
}
out;
```

**Plain language:** “A brief contact highlight appears at the exact impact and fades rapidly.” **Safety:** Not a repeating strobe; check target device, accessibility and that silhouette stays readable. If `easeOut` or output semantics are problematic in your AE environment, replace with tested keyframes.

## E06: Artist-controlled follow through on jaw/tail (keyframe-first)

**Expression property:** `Rotation` of the tail tip or jaw. Assumes joint rotation contains meaningful keyframes.

```javascript
var driver = thisComp.layer("TORSO_CTRL").transform.rotation;
var lag = 0.09;
var k = 0.22;
value + (driver.valueAtTime(time - lag) - driver.value) * k;
```

**Plain language:** “Let the far joint respond a fraction after the main motion.” **Important:** On the **same** property this can be interpreted in surprising ways because it samples pre-expression/keyframed values; for robust rigs drive the extra from a separate upstream control, and test for feedback/parenting artifacts. This is a **design sketch**, not a verified final rig solution.

## E07: Maintain consistent per-layer noise (not random every frame)

**Expression property:** `Rotation` of independent decorative leaves.

```javascript
seedRandom(index, true);
var offset = random(-6, 6);
value + offset + 2*Math.sin(time*0.7 + index);
```

**Plain language:** “Every leaf gets its own stable resting angle and subtle movement.” **Not for:** a hand actually grabbing an object or foot colliding with ground.

## E08: Repeat a fully designed cycle

**Expression property:** A keyed `Rotation`/`Position` property with at least two intentional keyframes.

```javascript
loopOut("cycle");
```

**Plain language:** “Repeat the already-drawn run loop.” **Watch out:** repeating a 12-frame run does not create world-space movement or lock feet against the ground. Synchronize root distance with gait cycle and contact frames.

## E09: Manga impact stepped cadence

**Expression property:** Keyframed decorative effect position or rotation (not whole master composition).

```javascript
posterizeTime(12);
value;
```

**Plain language:** “Sample a moving graphic only 12 times per second so it feels graphic/held.” **Note:** Works only if the property has actual underlying movement. The final 30-fps render still contains frames, but the graphic moves on twos/threes. Do not use on contact tracking that requires precise updates every frame.

## E10: Responsive caption box sizing

**Expression property:** `Rectangle Path > Size` inside a shape layer named `CAPTION_BOX`; text layer `CAPTION_TEXT` exists in the comp.

```javascript
var r = thisComp.layer("CAPTION_TEXT").sourceRectAtTime(time, false);
[r.width + 44, r.height + 26];
```

**Plain language:** “Make the background fit the actual words, with breathing space, rather than showing a huge empty rectangle.” **Note:** Centering/positioning need separate rig/anchor expressions or manual layout. Check single-line and multiline captions, safe area and reading time.

## E11: Follow a moving target through a comp-space conversion

**Expression property:** Position of an unparented 2D ring/flash layer `CONTACT_RING`; uses `CONTACT_TARGET` layer's anchor point.

```javascript
var p = thisComp.layer("CONTACT_TARGET");
p.toComp(p.anchorPoint);
```

**Plain language:** “Place the effect at the collision point's on-screen coordinates.” **Important:** `toComp(anchorPoint)` asks for the current screen position of the target layer's anchor point, and a 2D effect position needs 2D output. If layers are parented or 3D, transform to the correct destination space and test. This is not hit-detection logic.

## Expression versus effect versus authored action

- **Expression:** calculates property value (`wiggle`, easing, event envelope, follow-through).
- **Layer/effect:** represents a visual mechanism (solid, mask, displacement, shape, matte, glow, blur).
- **Rig/keyframes:** performs *meaningful anatomy* (recoil, stagger, fall, contact, pointing).
- **Editing/camera:** changes audience viewpoint and rhythm.
- **Sound:** communicates location, distance, material, emotion and contact.
- **QA:** determines whether the viewer actually understood the story action.

**Priority rule:** If a key action isn't readable, first fix staging and causal key poses. Do not try to solve it by increasing `wiggle` or adding a flash.
