# Emergency 60-second recovery card

**STOP producing.** Read `AGENTS.md`, `00_START_HERE/04_TRUTH_AND_RECOVERY.md`, `09_HANDOFF/STATUS.md`.

1. What is the most recent VERIFIED output, with exact path?
2. What stage is approved? Which stages were only proposed?
3. What is the first broken invariant (story/crossing/contact/camera/audio/technical)?
4. Which previous good component can be reused?
5. What is the smallest diagnostic render/test to isolate the root cause?
6. What evidence will prove the repair, including neighboring-state regression?
7. What status and defect files must be updated?

**Do not use “I think it passed previously” as evidence.** If the files are missing, set `UNVERIFIED` and ask for/retrieve actual assets rather than hallucinating a result. Never take a shortcut of fading through the portal instead of geometry/occlusion.

## V6 AI-01 research checkpoint

- Start: `13_ANIMATION_INTELLIGENCE/AI-01_ACTION_SEMANTICS/00_STEP_BY_STEP_AGENT_GUIDE.md`.
- Browse: `python 08_TOOLS/search_ai01.py --query "heavy" --kind ambiguity`.
- Audit: `python 08_TOOLS/audit_ai01.py --root .` and old core auditors.
- Source notes are small L1 separately; large contextual dataset is L2 generated/design, not extracted storyboard collection or audience-verified film.
- Do NOT claim a verified audio or moving camera from the static four-context diagram.
- DINO portal 270f benchmark remains NOT DONE.

## V7 retrieval and missing-source safeguard

Before recreating research, query `python 08_TOOLS/search_knowledge.py "open loop"` and `python 08_TOOLS/search_materials.py --list`. Do not treat the screenshot as inspected source video; do not mark not-collected artifacts as failed-access attempts. When a user provides a source, link it to an existing GAP, log actual file path/hash and its **scene context** before interpreting. Re-run V7 audit and update status.
