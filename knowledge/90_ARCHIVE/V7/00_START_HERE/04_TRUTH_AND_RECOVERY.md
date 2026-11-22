# Anti-hallucination, context-loss and drift recovery protocol

## Core idea

A **plausible description is not a verified artifact**. Tool output does not imply visual quality. Source code does not imply that generated motion was watched. A preview screenshot does not prove smooth movement. A claimed audio file does not prove that the final MP4 contains sound.

## Evidence classes

- `VERIFIED_RENDER`: exact existing artifact path + its media probe + sampled frames/audio playback evidence + date and method.
- `VERIFIED_SOURCE`: opened exact file/version and inspected relevant lines/functions.
- `RESEARCH_SOURCE`: webpage/report that was opened and whose claim is listed in the source ledger.
- `PROPOSAL`: creative or technical plan; not yet implemented.
- `UNVERIFIED`: potentially true, lacking evidence.
- `BLOCKED`: dependency unavailable or failed.

## Resumption after a long pause / new chat

1. Open only **actual** project directory and `09_HANDOFF/STATUS.md`.
2. List files with real paths. Inspect recent modification timestamps and sizes; verify hashes if `manifest.json` is present.
3. Cross-check claimed phase against named evidence in status. Where paths do not exist, downgrade to `UNVERIFIED`.
4. Inspect last approved render and latest defect log. When render isn't available, **do not assume it passed**.
5. Reconstruct character states at end of last shot (positions, headings, held objects, portal aperture, sound/ambience state).
6. Run smallest deterministic reproducible check; note exact command and exit code.
7. Create a two-column `KNOWN / UNKNOWN` record and choose the next small action.
8. Continue only after confirming locked decisions and current scene.

## Drift detectors — halt if any occur

- More than one scene is being built without verifying the previous shot's decisive physical action.
- User requested portal emergence, but shot design gives a person appearing from screen edge.
- Sound is selected because it feels cinematic without a source, perspective or narrative role.
- Camera zoom/shake hides missing actor movement or unreadable contacts.
- New character/prop or plot twist is introduced without updating story state and approval.
- Assistant says “done/verified/fixed” while producing only text or code, no rendering evidence.
- Claimed tool/library behavior is not checked against its installed version or documented source.
- Old assets are relabeled as newly generated material.
- Sound/voice/music is copied from an external source without license/ownership check.

## Recovery script the agent must perform

```text
HALT GENERATION.
A. Quote current project goal and locked beat from project files.
B. State last VERIFIED phase and list existing artifacts with exact paths.
C. Compare intended event vs observed result; if no render exists say "not inspected".
D. Identify first violated invariant and probable origin.
E. Select minimum reversible change that restores the invariant.
F. Render a tiny test span or debug-only view; inspect concrete evidence.
G. Update defects and status; resume one phase only.
```

## Repeated failure decision tree

```text
Portal exit looks wrong?
├─ Is first visible human pixel INSIDE portal aperture? No → change initial actor state.
├─ Does portal mask correctly occlude trailing body? No → fix depth and composite order.
├─ Does first foot land on world-space ground? No → fix foot IK/contact/root path.
├─ Does root move independent from camera? No → separate spaces.
└─ Are crossing, plant, and clearance all visible? No → retime/block poses.
```

```text
Sound feels wrong?
├─ Is there a story-relevant sonic source or explicitly subjective cue? No → remove/justify.
├─ Did the event actually occur? No → fix animation rather than audio.
├─ Is perspective correct for camera/POV? No → revise filtering, distance and stereo position.
├─ Does cue start at expected preview/contact frame? No → derive from event map.
├─ Are ambience and music masking the focal event? Yes → prioritize mix, duck/space.
└─ Does change still work on phone and mono? No → revise frequency balance/width.
```

## Error budget and final transparency

Use `BLOCKER`, `MAJOR`, `MINOR`, `SUGGESTION`. Blocker: story action absent, impossible portal, corrupt render, missing essential asset. Major: ambiguous motivation, repeated foot slide, serious continuity/sound problem. Minor: polish without effect on comprehension. Any blocker or unresolved major prevents approval. State incomplete work honestly.

## Context packing when token-limited

Instead of pasting the full chat, transmit only the following source-of-truth items: 1) project constitution; 2) scene and locked beat; 3) approved shot/cue card; 4) actual assets with paths; 5) open defects; 6) last tested command/results; 7) next action. Do not transfer hidden reasoning or fabricated test outcomes.
