# Shared video workspace

Read VIDEO-GENERATION.md, DESIGN.md and PIPELINE.md, then the selected job’s brief. Use skills/video-explainer/SKILL.md; Codex and Claude resolve the same project-local skill.

- Keep sources, scripts, storyboards, approvals, timing, assets, audio choices, production status and outputs inside jobs/<job-id>. Shared files contain universal principles and reusable primitives only.
- Open only the selected job. Independent versions may share original research and the design system, but must not read, import or reuse another job’s creative work unless the user authorises it.
- Draw chapter references and actual per-chapter storyboards; obtain review before production. Prove a narrated motion sample before scaling up.
- Let sources and comprehension determine duration, within the agreed ceiling. Preserve facts, qualifications and illustrative labels.
- Use achievable, varied visual models, centred compositions, meaningful continuous transitions with no cuts, narration-cued emphasis, restrained purposeful motion, occasional draw-in takeaways and selective technical side bullets.
- SpeechControl Visuals is the visual authority. Import src/design/tokens.ts; use design-source/speechcontrol for reference contracts. Keep animation deterministic and frame-driven.
- Voice, music, ambience and sound effects are explicit per-job decisions, reviewed in a representative mix. No paid services or publication is implied.
- Generate narration through the swappable speech layer (`python3 -m speech.synthesize`, provider chosen per job) and measure cue timing with `python3 -m speech.measure`. Do not hard-wire a speech runtime into scenes.
- Preserve user and concurrent edits. Missing fonts/media must fail visibly. Verify actual frames, motion, playback and sound separately from build success.
- Retain the strict 12-day publication gate for every package and transitive version. Do not change dependencies or bypass installer enforcement without the required authority.
