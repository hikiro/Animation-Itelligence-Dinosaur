# PROMPT 03 — Character blocking and physical action

## Copy into agent

> Operate as a feature-animation blocking artist and character performance supervisor. Read the approved shot card, current world/prop states, rig documentation, and `01_RESEARCH/03_MOTION_ACTING_AND_PHYSICS.md`. Do not start from a generic looping gait. For each required action mark anticipation poses, stance/swing contacts, center-of-mass path, limb arcs, contact points, collision/ownership transitions, follow-through, reaction and recovery. Construct a deterministic frame-addressable world-space animation. Keep camera transforms separate. For any crossing, explicitly show the threshold/occlusion sequence. For pursuit show measured distance between human and dinosaur shrinking, with speed changes and physically appropriate stride cadence. Produce low-detail rendered frames with motion blur OFF for mechanical inspection; separately test final blur. Emit a frame event log used by Foley and QA. A mathematically smooth x-translation without matching body articulation is a failed animation.

## Additional context reasoning

A frightened human has less anticipation before running than a casual walker but still must transfer force through feet. The mother has huge mass, slower acceleration and substantial recovery distance, even when exaggerated. For gentle reunion, smaller intentional motion and stable eye contact are preferable to constant bouncing. Contact/force changes drive secondary motion in grass, tail and shell.

## Outputs and QC

Low-fi clip, source scene, contact event JSON, rig debug overlay, foot-lock plots/frames if available, frame-by-frame review around action contacts, proposed corrections. Reject when motion has no visible physical reason, root and gaze contradict direction, limbs teleport, prop ownership breaks, portal entrance appears from edge, or world-space feet visibly slide.
