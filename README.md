# Animation Intelligence — Dinosaur

A versioned, evidence-aware knowledge repository for **translating ordinary human storytelling instructions into meaningful, testable animation**, including causal acting, story context, creature rigs, camera, sound, code, and visual QA.

**If you are a new ChatGPT chat or coding agent, [READ THE FULL HANDOVER FIRST](HANDOVER.md).** Then read [AGENTS.md](AGENTS.md) and the canonical [`knowledge/`](knowledge/) rules (if unpacked).

## What is backed up

- `knowledge/`: expanded **V8** browsable canonical knowledge with research, 90 *unverified* composable presets, rulebook, do/don'ts, creature-size adaptation, evidence gaps, logs, tools and V7 historical archive (when sync complete).
- `releases/`: historical release ZIPs and the full V8 portable archive; read [BACKUP_MANIFEST.md](BACKUP_MANIFEST.md) for what actually uploaded.
- `archives/`: editable original sample projects, reference images, and old source bundles where uploaded.
- `audits/`: concrete quality and story-logic defects; animation technical decode ≠ cinematic quality.
- `media/`: prototype example MP4s, explicitly not final film/benchmark.
- [`HANDOVER.md`](HANDOVER.md): exact decisions, states, goals, workflow, evidence and next steps.

The desired product is a **general-model-friendly animation directing framework**, not just a collection of expressions or indiscriminate presets. The user values detailed and searchable learning with citations, reproducible tests, realistic creature/size adaptations, and failure cases.

## Non-negotiable truth

As of the handover dated 2026-11-23, the approved **9-second / 270-frame DINO portal entrance** has **not passed production QA**; the planned 80-second *Wrong Exit* film is **not complete**. Existing examples are schematic tests.

## Search / validate (after cloning)

```bash
python knowledge/08_TOOLS/audit_repo.py
python knowledge/08_TOOLS/search_repo.py "portal crossing"
```

## Source and license notes

Preserved conversation-generated research and user-provided original archive. Sources from third parties are cited as research references; don't infer redistribution rights from inclusion. Do not upload credentials, private data, or copyrighted commercial footage without permission.
