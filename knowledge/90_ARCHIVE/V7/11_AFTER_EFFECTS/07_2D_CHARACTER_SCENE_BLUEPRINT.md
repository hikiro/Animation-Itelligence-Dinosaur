# Reconstructable 2D scene architecture for animation agents

## Comp hierarchy for a fictional non-graphic projectile impact demonstration

`MASTER_VERTICAL_1080x1920_30` (final edit / safe-area overlays)

- `CAMERA_RIG` null, 2D or AE camera linked to a separate camera controller for 2.5D
- `WORLD_FAR` precomp (sky, far scenery)
- `WORLD_MID` precomp (architecture, distant figures)
- `WORLD_ACTION` precomp:
  - `SHOOTER_ROOT` null → hips, torso, arm/hand and expression layers
  - `SOURCE_PROP` layer attached to correct hand point during start and recoil
  - `PROJECTILE_PATH` shape/path and `PROJECTILE_BODY` independent visual
  - `PROJECTILE_TRAIL` streak/particles, governed by traveled path
  - `CONTACT_TARGET` null at a specific location on receiver
  - `RECEIVER_ROOT` null → hips, torso, legs, arms, head, face
  - `IMPACT_CTRL` null with time, intensity, damping sliders
  - `CONTACT_RING` / graphic flash / debris on separate selective effect layers
  - `SHADOW_RECEIVER`, `SHADOW_SHOOTER` registered to ground plane
- `WORLD_FORE` precomp (foreground occluders and environmental objects)
- `CAPTIONS_SAFE` titles and brand separate from camera-induced blur
- `AUDIO` multitrack stems (not flattened-only)

## Event/state table (illustrative, not exact final timings)

| Event | State | Must be visible | Technical dependency |
|---|---|---|---|
| EV-01 | `ready` | Actor prepares, stable pose, eye direction | Rig pose and blocking |
| EV-02 | `fired` | Visible cause + shooter whole-body recoil | Limb joints + grounded feet |
| EV-03 | `in-flight` | Continuously mapped projectile progress | Path/position, motion blur, trail follows object |
| EV-04 | `approach` | Target is in known relation to travel direction | Editing geography and frame match |
| EV-05 | `contact` | Object and target occupy same contact location/time | Coordinate conversion, body silhouette, effect anchoring |
| EV-06 | `force-transfer` | Receiving character's posture and balance respond | Actor rig, hips, planted/swing foot, follow-through |
| EV-07 | `after` | Character settles/falls, sound decays, consequence persists | Stateful pose/prop continuity |

**Critical:** This scene is a teaching case for **visual intelligibility**, not an instruction to design, build, or operate real weapons. Avoid mechanical instruction or graphic injury. Animation may intentionally exaggerate travel and impact for artistic purposes.

## Dino portal variant

Swap `PROJECTILE_BODY` for `HUMAN_ROOT`, replace `CONTACT_TARGET` with `PORTAL_THRESHOLD`, establish front/back rim/matte, anchor ground contact. Never infer portal crossing from proximity: render visibility stages partly inside → straddling threshold → fully outside.
