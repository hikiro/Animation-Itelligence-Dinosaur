# Motion mechanics: keyframes, graph editor and joints

Sources: Adobe [speed graph](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/speed-between-keyframes/speed.html), [keyframe interpolation](https://helpx.adobe.com/uk/after-effects/desktop/animate-in-after-effects/animation-keyframes/keyframe-interpolation.html), [Puppet tools](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animate-with-puppet-tools/animating-puppet-tools.html), [time remapping](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/time-stretching-and-time-remapping/time-stretching-time-remapping.html).

## Timing is not spacing

- **Timing**: how many frames an action takes, when anticipation/contact/recovery occurs.
- **Spacing**: how far an object's position changes between consecutive frames, controlling perceived speed and acceleration.
- **Spatial path**: the curve in 2D/3D through which it moves. A curved *camera* path is not necessarily a curved *projectile* path.
- **Speed graph**: inspect velocity changes; abrupt spikes imply a snap, except when purposefully used as a stylized impact.
- **Value graph**: inspect property values and tangent behavior. Keyframe interpolation and spatial Bezier tangents must be reviewed independently.
- **Hold keyframes**: deliberate freezes and poses, e.g., graphic manga impact hold or shocked realization.
- **Roving spatial keyframes**: distribute travel timing when useful, but not a solution for contact timing.

## Contact-first animation contract

Before moving the camera or applying FX, lock exact event frames: start, notice, anticipate, push-off, release, travel, approach, touch, settle, recovery. For each contact, list surfaces and anchor points. Root and joint motion must satisfy the contact constraint. Do not animate both a hand and held prop with independent, unrelated position curves; attach it to the hand coordinate frame during `held` state.

## Rigging hierarchy (stylized human)

`ACTOR_ROOT` → `HIPS` → torso → neck → head → eyes; hips → thighs → shins → feet; torso → upper arms → forearms → hands. Layer-specific front/back order changes with blocking, not randomly. Add controllers `GAZE_TARGET`, `CONTACT_LEFT_FOOT`, `CONTACT_RIGHT_FOOT`, `HOLD_POINT`.

**Puppet vs segmented rig:** Puppet Pins bend a continuous mesh for soft motion; separated hinged layers preserve sharp paper-cut segments and limb silhouettes. Mix carefully, avoid stretching paper textures beyond their intended style.

## Three examples of the same gesture in different contexts

- **Curiosity:** eyes first; slow head turn; torso follows; shoulders relax; light ambient Foley; patient close shot.
- **Fear:** eyes dart; shoulders compress; tiny anticipatory pause; abrupt backward root shift; contact foot catches balance; environmental sound drops.
- **Comedy:** exaggerated hold, late recognition, sudden overreaction, inertial overshoot, end pose held long enough to register; strong but not excessive sound punctuation.

## QA

Scrub at 100% speed and 1-frame steps. Analyze foot contacts, joint intersections, silhouette, weight shifts, velocity discontinuities and object attachments. A smooth position path is not enough to certify believable body action.
