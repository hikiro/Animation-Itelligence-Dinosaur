# Camera, effects and compositing for legible storytelling

Sources: Adobe [cameras](https://helpx.adobe.com/after-effects/desktop/work-with-layers/camera-layer/cameras-lights-points-interest.html), [motion blur](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/assorted-animation-tools/assorted-animation-tools.html), [displacement/distort](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/distort-effects.html), [effects list](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/effects-and-animation-presets/effect-list.html), [Turbulent Noise](https://helpx.adobe.com/after-effects/desktop/apply-effects-and-animation-presets/list-of-effects/noise-grain-effects.html).

## Camera decision chain

1. What exactly must viewer notice or infer?
2. Whose perspective: objective, character subjective, omniscient/explanatory?
3. What is current spatial relationship and screen direction?
4. Choose shot size/angle/lens-like perspective that makes that relationship clear.
5. Choose whether camera is locked, follows, pushes in, tracks alongside, or reframes **for a dramatic reason**.
6. Plan camera acceleration/deceleration and shot transition before adding motion blur.
7. Reinspect eye-trace, cut on action, axis continuity and spectator comprehension.

## AE implementation choices

- **2D fake camera:** Parent flat background/foreground to a root null and animate that null. Good for small pans/zoom graphics; parallax needs independent depth-specific motion.
- **Real AE camera with 3D layers:** Place flat cards at different Z depths; use camera position/point of interest and optional depth of field for 2.5D. This changes scale/occlusion with perspective. Avoid arbitrary zoom that makes projected body scale inconsistent.
- **Tracking insert:** Separate shot precomp isolates target and projectile while preserving geography through entry/exit frame matches. Camera tracking might be visually more legible than an impossible continuous whip-pan.
- **Motion blur:** Enabled per moving layer and comp; shutter angle and shutter phase alter blur character. Motion blur does not correct actual path discontinuities.
- **Graphically stylized speed lines:** Shape-layer Trim Paths/Repeaters following a consistent direction field, not random full-screen scratches.
- **Water/wake distortion:** Use layered ripples/particles and modest displacement for a scene underwater; if a dry scene uses water-like tearing, explicitly mark it a metaphorical effect.
- **Impact bloom/glow/flash:** Attach to actual contact frame and collision point. Flash is one brief controlled event, not substitute for deforming/deflecting a body.
- **Turbulent Displace/Displacement Map:** Can warp heat/water/energy or material response. Use a separate control solid/noise map if needed. Do not warp character silhouette until it loses anatomy.

## Camera vs character motion conflicts

- Fast camera push plus fast projectile motion may create excessive total screen velocity. One movement should dominate at a time.
- Shot insert changes audience frame of reference. Include at least one orientation cue (departure vector, target location, left/right geography) to make impact location legible.
- Camera shake should be minimized during the exact contact frame so the viewer actually sees the hit; if used, it may peak immediately after contact and decay.
- A dramatic slow-motion insert requires editorial time mapping. If returning to real-time, mark transition with action/audio beat.
- Whole-composition scale changes can invalidate 9:16 safe areas and clip impact graphics; inspect on mobile preview.

## Stylization choices are not physics claims

Cinema may intentionally hold a projectile, curve the camera around it, use impossible perspective, or slow time. Be explicit: `stylized-camera`, `stylized-time`, `stylized-trail`, `physically-plausible-motion`. No ambiguity about what path or force the character is actually following.
