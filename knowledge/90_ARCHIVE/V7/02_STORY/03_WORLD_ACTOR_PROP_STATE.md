# World geography, scale, awareness and prop/portal states

## Coordinate convention

World X increases east/right, Y is vertical or ground height depending on implementation; choose one convention and declare it in code. **Do not mix pixel canvas Y-down with physical Y-up silently.** The 2D projection should clearly establish a ground plane, plus background/foreground Z bands.

```
WEST / screen-left                                                EAST / screen-right
[Open portal] ---- [forest ground] ---- [branch, root] ---- [egg nest ledge] ---- [mother entry]
                                          human flees WEST <---- mother pursues WEST
```

Use a rough world map before choosing camera crops. Screen-left west direction is the **initial chase convention**, not a mandate that every camera POV face west. Reversals require deliberate camera re-establishment.

## Visual scale contracts

- Human adult height is the baseline 1.0 actor unit; baby significantly smaller, mother several times taller. The precise multiplier requires design sheet and must remain consistent in world space.
- Portal is tall/wide enough for full human crossing, grounded, with an aperture that supports body passage. The rim may stretch only where story establishes elasticity.
- Nest height, egg diameter and human hand size must make a two-handed catch physically possible. The egg must plausibly contain a small hatchling without drastic teleporting changes.
- Mother cannot pass fully through a human-sized portal without substantial purposeful deformation or opening enlargement; end only with snout and eye partially through, preserving cliffhanger.

## Character knowledge state by scene

| Scene | Human knows | Mother knows | Baby knows / state | Audience knows |
|---|---|---|---|---|
| 01 | Unfamiliar prehistoric environment | Offscreen with nest and egg | Inside egg | Human truly crossed into prehistoric space |
| 02 | Egg in danger, he rescued it | Not yet aware of removal | Egg state | Remote footsteps may mean unseen creature |
| 03 | Dinosaur thinks him a threat | Nest empty, human holds egg; assumes danger | Egg state | Misinterpretation clearly visible |
| 04 | Must protect egg while fleeing | Needs to recover egg | Shell intact until late chase | Both motivations simultaneous |
| 05 | Egg is hatching | Recognizes chirp as baby | Emerging | Threat can be resolved |
| 06 | Mother is grateful/not attacking | Baby safe; human helped | Human is safe/familiar | Reunion resolves conflict |
| 07 | Returning home, unaware baby chose to follow | Briefly distracted, then learns of departure | Chooses human | Viewer anticipates new trouble |
| 08 | Home, discovers baby follower | Pursuing through aperture | Delighted follower | Snout reveal is consequence, not random monster |

## Egg / baby ownership states

`nest → rolling on ledge → free falling → held_in_both_hands → cradled_at_chest → cracking_in_hands → baby_supported_by_hands → baby_feet_on_ground → baby_free → baby_with_mother → baby_crosses_portal → baby_in_apartment`.

A single authoritative state owner controls parent transform and physics. At contact, add parent attachment; at release, remove after support established. A cut must not silently change ownership.

## Portal state machine

`closed → opening → open_passable → HUMAN_PARTIAL_EXIT → HUMAN_FULL_EXIT → open_idle → HUMAN_RETURN_PARTIAL → HUMAN_FULL_RETURN → BABY_PARTIAL_ENTRY → BABY_FULL_ENTRY → MOTHER_SNOUT_PARTIAL_ENTRY → cliffhanger`.

Portal aperture is a spatial **threshold** with inside/outside half spaces, front/rear layering, and light/sound continuity. Crossing events should be recorded. A sprite passing left of the portal is never interpreted as crossing the portal simply because its x-coordinate crossed portal.x.

## Sound state across locations

Forest ambience persistent through scenes 1–7; offscreen mother becomes nearer from 2 to 4; chase narrows to close breathing in 5; restored warmth in 6; portal sound bridges 7→8; apartment ambience changes to smaller interior acoustics in 8. Character breath/feet events persist across cuts only when physically motivated.

## Shot transition invariant card

At end of every shot document `world time, human position/facing/foot stance, mother position/facing/gait state, baby position/state, egg ownership, portal state, sound bed, camera side/axis, next viewer attention`. The next shot must begin from that state or show a justified ellipsis/match.
