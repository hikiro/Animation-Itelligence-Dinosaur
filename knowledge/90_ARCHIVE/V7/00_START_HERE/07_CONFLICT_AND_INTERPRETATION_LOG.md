# Conflicts, trade-offs, and decisions

Keep a row even after resolved. When uncertain, present the options rather than silently choosing.

| ID | Statement A | Statement B | Current resolution | Evidence / QA |
|---|---|---|---|---|
| CONFLICT-001 | “Bullet follows a curved trajectory” | Grounded, fast projectile motion usually reads near-straight over short distances | Distinguish **actual path** from camera motion, speed ramp, stylized trail. Default literal physical path = direct; stylized curve only when explicit stylization is intended | Check continuous path and intended realism |
| CONFLICT-002 | “Hit = intense shake” | Whole-body acting must maintain understandable balance and grounded contact | Shake accent is subordinate to contact/pose and force; avoid whole-comp random jitter. Use decay only after actual impact | Inspect pre-hit, contact and recovery frames |
| CONFLICT-003 | “Camera zooms to projectile then out to victim” | Editing geography and travel time may make the shot unreadable | Establish start and target locations, cut to planned insert/tracking if necessary, match screen direction back to target. Do not assume literal single-camera zoom is always best | Silent-read spatial test |
| CONFLICT-004 | “Character falls slowly” | Physical reaction should show initial force and gravity | Separate fast impact/compression, destabilization, **stylized** temporal dilation, then continued fall and landing; avoid weightless float | Whole-body path and timing review |
| CONFLICT-005 | “Expressions do the animation” | Expressions compute property values; not story logic or a rig | Choose hand-authored key poses, links, physical constraints, then use expressions for secondary procedural behavior | Rig + contact tests |
| CONFLICT-006 | “Use After Effects resources” | V3 Dino production renderer was previously tool-agnostic; exact AE app not available in this environment | AE becomes a **reference implementation learning track**, not a claim the DINO film already uses AE or that expression samples ran in AE | Toolchain state; label snippets not AE-tested |
| CONFLICT-007 | High-energy manga flashes and impact | Platform photosensitivity / legibility | Prefer a controlled, non-strobing contrast accent rather than repetitive flashing. QA for readability and photosensitivity risk | Review full render at target speed |

**Decision owner:** Explicit user direction outranks this project file. All new conflicts require a new ID, date, affected scene, alternatives, chosen approach, and re-test. The last `status` and actual render remain the source of truth.

## V5 interpretation conflicts

- `CONFLICT-V5-01` **Source research vs invented universal rules:** Disney/Adobe/Remotion documents support acting and tools, not our fixed phase length. Treat 30fps timing tables as illustrative proposals until tested in narrative context.
- `CONFLICT-V5-02` **Schematic good portal vs approved portal benchmark:** Teaching comparator visually conveys inside→outside, but does not implement target-grade foot IK, true depth or 270-frame staging. The old failure remains open in production.
- `CONFLICT-V5-03` **Event-aligned sound vs foreshadowing:** Offscreen dinosaur steps are valid earlier-than-reveal sounds if the diegetic source event happens earlier. Contact Foley must still match its real event; label J-cuts and perspective.
- `CONFLICT-V5-04` **Stylized curve vs believable physics:** Default to physically coherent object path and optional camera/graphics styling; record intentional physical deviation separately. No implicit bullet-curving effect merely because 'cinematic' was requested.


## V6 conflicts and interpretations — 2026-11-19

- **CONFLICT-008 (OPEN): Dataset size vs real source evidence.** User wants a large research dataset; 6k+ rows are feasible with synthetic context expansion, but that is not 6k+ independently observed production samples. RESOLUTION: explicitly separate L1 source observations from L2 designed/generated rows, report both counts and prioritize real paired artifacts.
- **CONFLICT-009 (OPEN): Polysemous modifiers.** “Heavy,” “sharp,” “hold,” “cut,” “close” attach to different targets and cannot safely select effects by token. RESOLUTION: use syntactic attachment, source of sound, actor belief and audience objective; test alternate readings.
- **CONFLICT-010 (OPEN): Threat/comedy/wonder styles vs same world physics.** Emotional direction may alter editing/acting/audio but should not accidentally change object contact and screen geography. RESOLUTION: lock shared contact event; compare context variants experimentally.

## V7 interpretation conflict — 2026-11-19

- **CONFLICT-011 (RESOLVED AS CONTEXTUAL POLICY):** Short-form framework with repeated open loops and CTA vs meaningful emotional pacing and honest story completion. **Decision:** preserve exact screenshot as `REF-STORY-0001` and apply conditionally. In DINO fiction, honor action clarity, emotional payoff and one intentional cliffhanger; do not force a promotional CTA or two loops at fixed intervals. In factual Shorts, hook/lead/body/open-loop may be tested for engagement provided claims remain accurate and loops pay off. **Status:** proposal; not audience validated. **Related:** GOAL-019, AI-01.
- **CONFLICT-012 (RESOLVED AS PROVENANCE RULE):** Large dataset and attractive source references vs direct-source inspection. **Decision:** user screenshot is observed; original video, attribution and claims of “perfect” structure unverified. Never invent creator strategy, soundtrack or measured performance. **Related:** GAP-001, GAP-002, GAP-009.
