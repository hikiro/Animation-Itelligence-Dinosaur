# Lesson 05 source-backed guidance vs. our own tests

**Source ledger:** `01_RESEARCH/00_SOURCE_LEDGER.md` IDs S45–S51. The sources were checked online on 2026-11-19. These are references for general practice; none certifies the 42 original timed recipes.

## Research-backed principles

- **Character acting is intentional and supported by weight and staging.** Disney Animation lists clear staging, anatomy, weight, anticipation and secondary action as animation practices. **Direct support:** S45.
- **Storyboarding and camera layout are connected to expression and timing.** Disney story and layout documentation links storyboard emotion and framing to the shot's cinematography and rough actor staging. **Direct support:** S46.
- **Puppet deformation is not rig-level balance.** Adobe documents pins and mesh deformation; Blender documents IK chains separately. We infer that a rigged character also needs contact anchors, hierarchy, and actual foot placement. **Direct support:** S47; inference explicitly ours.
- **Spatial path and timing function are independent dimensions.** Adobe speed graph and Remotion interpolation/spring affect how values evolve; neither source claims automatic physical correctness or meaning. **Direct support:** S48; rule extrapolated to our defect cases.
- **Audio is spotted against picture and story; cuts have rhythms.** Disney sound/editorial and Adobe Foley guidance support cue-sheet based collaboration. Sound emitter positions and story rationale are production decisions. **Direct support:** S49.
- **Simulation is art-directed, not an automatic substitute for performance.** Disney's technical animation emphasizes physically convincing, intentional response. **Direct support:** S50.
- **Use deterministic randomness for frame-addressable renders.** Remotion warns nondeterministic randomness causes inconsistent multi-thread rendering. **Direct support:** S51.

## Original lesson-05 synthesis (not sourced studio rules)

- Six-phase storyboard as a practical search and QA schema.
- Forty-two compact everyday-language action cards.
- Per-category proposed 3–4 second example blocking schedules at 30 fps.
- Event-driven audio/pose contracts, visual contact-check heuristics and failure-mode taxonomy.
- Three educational cartoon tests comparing deliberately faulty and improved action logic.

## Major evidence distinctions

| Evidence type | What is established | What remains unresolved |
|---|---|---|
| `SOURCE_REVIEW` | General professional animation concepts and tool capabilities | Whether this one animation looks good |
| `UNIT_TEST` | Recipe schema, monotonic parametric curves, frame lookups and data completeness | Correct body rig, depth, contact and emotional acting |
| `SCHEMATIC_RENDER` | A demonstrable short visualization was encoded; frame samples can be inspected | Whether production-scale art and movement pass director review |
| `PRODUCTION_RENDER` | Actual output from target rig and scene exists and can be inspected | Still needs independent QA and listening |
| `APPROVED` | All scene-specific quality gates documented and passed | New edits can regress it and must rerun checks |

Do not attribute hand-authored sample timing to Disney, Adobe, Blender or Remotion. Do not claim AE expressions were executed in After Effects unless an AEP and measured render are provided.
