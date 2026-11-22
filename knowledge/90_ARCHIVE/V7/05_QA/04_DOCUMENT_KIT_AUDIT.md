# Audit the handbook separately from auditing a film

## Document/package audit — what can be automated

Run `python 08_TOOLS/audit_kit.py` from pack root. It checks mandatory files, Markdown counts, blank content, relative Markdown links (including renamed files), canonical scene timing, shot ID and module coverage, source ledger presence, and evidence/status defaults. It is not a web link checker and does not render the film.

Review manually:
- Is the handoff readable by an agent with no prior conversation?
- Does README define entry path and status priority?
- Are creative “rules” distinguished from actual external standards?
- Does context coupling explain **why** camera/motion/sound are chosen together?
- Are audio timing types differentiated (contact, lead, tail), avoiding false blanket sync instruction?
- Is the portal benchmark a real staged exit rather than a summary?
- Do 8 story scenes and 24 shot cards cover causal chain?
- Are failures and recovery mechanism actionable rather than vague “check again”?
- Is status transparent about no newly rendered V3 scene?
- Are source URLs real and researched?

## Film audit — cannot be inferred from this pack

The pack is a plan. Visual performance, camera clarity and mix quality require actual source and rendered media in future. No success score or “passes professional QC” can be assigned to a film that has not been rendered and inspected.

## Evidence record format

`timestamp | check | file/path | tool/method | observed result | classification | outstanding defects`. Use the exact command and path; never say a test passed if the command was only suggested.
