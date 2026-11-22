# Evidence, version, licensing and testing limitations

**No AE runtime present in this research task; code snippets are not executed AE expressions.** Verify installed AE version, expression engine setting, layer names, UI effects, coordinate systems and required assets before claiming real AE compatibility.

## Smallest AE validation project

1. Make comp `TEST_EXPR_1080x1920_30`, 60–150 frames.
2. Create two solid/shape layers and one null with named slider controls.
3. Confirm code pasted into the **correct property** (Position, Rotation, Opacity, Scale).
4. Verify no error triangle; scrub beginning, event, 1 frame before/after, decaying tail.
5. Confirm deterministic frame seeking: visiting frame 30 after frame 100 has the same values as frame 30 in sequential play.
6. Confirm dimensionality: 2D Position `[x,y]` vs 3D `[x,y,z]`, Scale percentages, Rotation degrees, Opacity 0–100.
7. Render a short lossless/visually high-quality reference. Compare contact, pose, silhouette, blur, tracking and sound.
8. Record AE version, renderer, plugin version, source URL, screenshot, exported render and verdict in lesson/log.

## Failure checklist

- Bad layer property name; missing slider; wrong keyframe dimensions; references target property from same expression incorrectly; sourceRect bounds and anchor mismatch.
- `loopOut` has no real starting cycle; `posterizeTime` freezes a non-keyframed property; `wiggle` loops or jumps in unintended context.
- Track matte front/back occlusion inverted; mask doesn't move with portal; precompose/collapse transformations changed depth or effects order.
- Blurred footage misses the underlying contact frame; wave/distortion hides object; camera shake looks like a bug.
- Audio not aligned to visual event; effect accents masked by music; stereo location contradicts shot geography.

## External dependencies and ethics

Don't claim third-party scripts/plugins are installed or properly licensed. Adobe effects/plugins evolve; validate official current docs. Keep the source ledger, link the specific claim, distinguish sourced facts from directorial preference. Descriptions of fictional projectile impacts are safe to illustrate without operational weapon information, gore, or instructions about injury.
