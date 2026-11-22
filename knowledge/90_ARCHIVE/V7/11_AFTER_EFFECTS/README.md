# After Effects for story-first character animation — research track

**Status:** Source-grounded technical study, examples not executed in Adobe After Effects during this session. These docs teach which building blocks to use and when; they do not claim Adobe After Effects is installed or that any AEP was rendered.

## Navigation

1. `01_LAYERS_SOLIDS_MATTES_AND_PRECOMPS.md` — what each layer physically contributes, why a solid matters and when to precompose.
2. `02_KEYFRAMES_GRAPH_EDITOR_AND_RIGS.md` — hand-keyed posing and speed/spacing, layered 2D rigs, puppet tools.
3. `03_EXPRESSIONS_PLAIN_ENGLISH_DICTIONARY.md` — expression APIs, precise scope, situations and caveats.
4. `04_EXPRESSION_COOKBOOK.md` — small annotated AE property expressions, event-driven impact and delayed motion.
5. `05_CAMERAS_EFFECTS_AND_COMPOSITING.md` — tracking, 2.5D, masks, matte, distortion, motion blur, art accents.
6. `06_CONTEXT_DRIVEN_TECHNIQUE_SELECTOR.md` — avoid using a technique out of emotional/story context.
7. `07_2D_CHARACTER_SCENE_BLUEPRINT.md` — layer hierarchy for portal, actor, projectile/contact demo.
8. `08_VERIFICATION_AND_LIMITATIONS.md` — exact tests in a future AE session and factual boundaries.

## Conceptual rule

**Script/treatment → action contract → storyboard/animatic → timing/poses → layer architecture → keyframes + expressions + effects → rendered frames → visual+audio QA.**

AE expressions are JavaScript-based calculations attached to individual properties. `.jsx` scripting is a separate way to automate creating/manipulating project elements. A renderer such as Remotion can implement equivalent concepts but does not run AE expressions natively. Don't paste AE expressions into a web animation runtime unchanged.

Research provenance: Adobe Help [expression language](https://helpx.adobe.com/after-effects/desktop/work-with-expressions/expression-language-reference/expression-language-reference.html), [layers](https://helpx.adobe.com/after-effects/desktop/work-with-layers/create-layers/creating-layers.html), [Puppet](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animate-with-puppet-tools/animating-puppet-tools.html), [Graph Editor](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/speed-between-keyframes/speed.html).
