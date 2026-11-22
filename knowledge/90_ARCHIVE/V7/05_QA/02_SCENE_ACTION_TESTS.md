# Action-completion tests by scene — ask what actually happened

**QA method:** for each test mark `VERIFIED` only with rendered evidence (shot frame range / actual output name); otherwise `UNVERIFIED` or `FAILED`. A script saying an action happened does not count.

| Scene | Test | Exact evidence required | Fail condition |
|---|---|---|---|
| S01 | Portal materializes on floor | Rim base/ground and foliar response sequential frames | Portal floats; glow overlay only |
| S01 | Person emerges from *inside* | Head partly inside aperture; lead foot outside and trail limb still inside; then all body outside | Person enters from screen edge or merely passes front of portal |
| S01 | Feet receive mass | Contact debug and actual knee/hip settling while sole stays planted | Skating/hovering/no weight transfer |
| S02 | Thud has consequence | Egg nest wobble follows intentional offscreen step | Egg rolls with no force |
| S02 | Egg catch | Egg leaves nest, travels, contacts hands, body absorbs momentum | Cut hides collision; egg attaches too early |
| S03 | Mother interprets | Mother scans empty nest then egg in human's hands | Angry before she notices egg |
| S03 | Roar-recoil order | Breath/roar visibly precedes human startled movement | Human recoils before stimulus |
| S04 | Why keep egg? | Human attempts to put egg down but mother too close; cradles protectively | Human inexplicably steals egg |
| S04 | Real run/pursuit | Feet grounded, actor faces left, mother closes x-distance | Gliding/backwards run; mother gap widens |
| S04 | Branch collision | Branch shown in route; human ducks; mother physically contacts, branch breaks | Branch appears only in fracture shot |
| S04 | Stumble | Foot catches root and torso pitches, recovers without losing egg | Random shake without obstruction |
| S05 | Crack and hatch | Shell fracture develops and baby emerges head then body | Instant baby sprite spawn |
| S05 | Mother stops for baby | Chirp heard/recognized before brake; body/tail decelerate | Hard freeze unrelated to baby |
| S06 | Baby ground transfer | Baby feet plant while hands still supporting, hands release afterward | Child hovers or falls |
| S06 | Reunion changes emotion | Snout/baby contact and mother softens, then human sees acceptance | Smile before reunion |
| S06 | Bond planted | Baby specifically turns/chirps toward human | Follower motivation missing |
| S07 | Human returns through portal | Body clears aperture into other dimension, portal remains open | Walks off left screen |
| S07 | Baby chooses | Sees human depart, mother distracted, baby turns and enters aperture | Teleports/ignores mother for no reason |
| S07 | Mother realizes | Mother sees absence then lunges toward portal | Already attacking before noticing |
| S08 | Both exit into apartment | Human and baby arrive by same portal plane with distinct ground contacts | Pop into center of room |
| S08 | Snout forces portal | Partial snout crossing with rim displacement and proper occlusion | Whole mother appears instantly |
| S08 | Comic payoff | Human reaction after he notices new pressure/eye; short readable final reveal | Sting/cut before viewer understands |

## Independent viewer questions

Watch without soundtrack. Ask a person unfamiliar with prompt: “Where did human come from? What caused egg to fall? What does mother believe? Why is he running with the egg? What stops chase? Why is mother affectionate? Why does child follow? Why is mother entering apartment?” If viewer interpretations differ materially from intended story, reopen story/shot design even if individual motion is smooth.

## What automated code can assist

Event ordering, portal crossing state sequences, distance-to-dinosaur metrics, foot stance velocity in world space, parent ownership count, frame count, absence of null/NaN transforms, encoded audio track presence, scene boundary time. These help diagnose failures; they do **not** replace watching the video.
