# Video generation guide

This is the shared authoring guide for this workspace. It governs creative process; DESIGN.md governs SpeechControl Visuals; package and permission rules remain in force.

## What a successful explainer does
Teach the material with visual reasoning. A chapter structure is useful, but every chapter must earn its visual form. A palette applied to repetitive lists is not a design system in action. Motion must reveal relationships, causality, quantity, state or evidence. Ask: what can the viewer understand by seeing this that the caption alone does not show?

Choose an executable art vocabulary: clean SVG geometry, proportionate object drawings, documents, data marks, masks, cropping and camera movement. Do not promise cinematic 3D, photorealism or elaborate artwork that the pipeline cannot produce reliably. Prototype the hardest visual in the storyboard and simplify it if it fails.

## Timing and information
Let the source and the learning task determine duration. No equal-length chapters, fixed number of caption beats or arbitrary short-video target. Preserve necessary explanation, qualifications and useful examples; do not discard information just to shorten the video. The default ceiling is 20 minutes unless the brief sets another; anything shorter is acceptable if it explains the material properly. If necessary coverage exceeds the ceiling, propose a series or scope decision rather than silently omitting it.

Use provisional timing ranges during storyboarding, based on reading, observing and understanding. Fix timing only after the explanation and any narration are settled. Avoid long holds after an idea has already landed. Silent video needs enough time to read and then look at the visual.

## Mandatory design sequence
1. **Source and chapter plan.** Identify audience/job, necessary claims, source references, uncertainty and chapter outcomes. Separate facts, reported status, proposals and illustrative examples.
2. **One visual reference per chapter.** Draw a representative frame showing that chapter's visual approach at useful fidelity. Explain what it teaches, why that representation fits, and the limited primitives needed to build it. Review the references as a contact sheet for repetition and feasibility before expanding them.
3. **A storyboard per chapter.** Draw the actual key states, including the revealing intermediate state. Show the required text at realistic scale. For every transition, specify the retained object, its change, camera path/mask if any, focus, and destination. Include the bridge to the next chapter. A text outline or JSON scene list alone is not a storyboard.
4. **Review and revise the boards.** Check explanatory value, fidelity, legibility, continuity, repetition and feasibility. Show references and storyboards to the user. Stop at the storyboard checkpoint until the user approves or directs changes. Record approval in the job brief before production.
5. **After storyboard approval, animate a representative passage.** Choose one that proves the hardest explanatory movement and chapter bridge, not the easiest title. Review actual motion before building the rest.
6. **Assemble and verify.** Use the approved storyboard and source-linked script; retime to real comprehension/narration needs. Check both visual design and technical output. Export only after those distinct checks pass.

## Composition and continuity
Use visual plus text when they complement each other; visual-only when the relationship is self-evident; text-only when a precise distinction deserves the stage. Keep the text concise without relying on it to do all the explaining. Change the visual structure when the information changes, not just the labels.

No hard cuts between states or chapters. Compose continuous transitions using elements from state A: a document becomes its extracted record, a row expands into a detail view, a transaction aligns with an invoice, a room pulls back into a project overview. Keep an anchor visible while other content changes. Specify zoom origin/destination and what remains spatially stable. Avoid replacing an entire scene with a fade, wipe or effect unrelated to the content.

Use source-system easing, coherent travel, selective emphasis, masks, zoom and purposeful morphs. Effects must explain or direct attention, never disguise a missing idea. Preserve object identity and truthful quantities. Do not animate facts through invented values. Any illustrative quantities, documents or statuses must be clearly labelled, never presented as real project records.

## Review gates
**Reference review:** are the chapters visually distinct where their concepts differ? Could these drawings actually be implemented well? Is the chosen visual more informative than a list?

**Storyboard review:** do the drawn states teach cause and effect? Can the viewer follow the same object across changes? Is every state/chapter bridge continuous? Are needed qualifications visible? Are examples explicitly illustrative? Does text fit at real playback size?

**Motion review:** inspect entry, intermediate, reversal/exception and settled frames; check actual passage playback. Verify coherent paths, rhythm, reading time and no unwanted resets/cuts. Do not approve a transition from its endpoints alone.

**Technical review:** source accuracy, fonts/assets, frame count, audio/caption sync, deterministic timing, decode, clipping and final playback. Technical success does not establish communication or design quality. A repetitive contact sheet is a redesign finding even when every frame is readable.

## Shared system and audio
SpeechControl Visuals is the visual authority. Preserve the source's identity and component finish while adapting layouts and interactions to video. Do not constrain every chapter to the same panel, circle sequence or numbered list.

Music and SFX are off unless requested and separately auditioned. Narration is a project choice, not a reason to postpone useful storyboard work. No paid service or external publication is implied.

## Deliverable contract
Keep the references, drawn boards, transition notes, source map, timing rationale and review record inside the selected job. Mark readiness accurately: outline, references, storyboard awaiting review, motion prototype, rough cut, or verified final. Never call a written outline a visual storyboard, or a technically valid render an approved design.

## Narration-led motion and sound revision
Motion must continue to explain the subject during the spoken passage, not occur only at transitions. Plan a cue track alongside narration: named object, spoken phrase, emphasis, connection/action and release. Raise or selectively scale the active object, highlight its relevant field, reduce competing emphasis, and carry a pulse along the relationship when attention transfers. Keep restrained ambient motion where appropriate, without moving everything uniformly or distracting from reading. Use source easing; no default glow or shadow.

Measure narration phrases to anchor the cues. Rewrite fast lists into deliberate spoken beats when the viewer needs time to see each object. Review a narrated motion sample with actual sound before scaling the treatment across the film. A still storyboard and a successful decode do not establish engaging motion or good sound.

Do not use generated broadband/brown/pink noise as a substitute for a musical ambience bed, or unreviewed synthetic clicks as finished sound effects. Soundtrack character must be chosen and auditioned in a representative mix. Keep a clean narration stem.

Do not freeze all frames after the transition as a rendering shortcut. Any frame-reuse optimisation must preserve the entire motion/cue timeline.

## Composition, emphasis and technical support
Default to a centred film composition: centre chapter kickers and headings, headline takeaways, major visual groups, and labels/status pills beneath their objects. Align numerical comparisons around the centre of the frame. Use left alignment inside authentic documents or tables only where that aids reading; do not let the whole frame inherit a document-page layout.

Use occasional large highlighted key phrases with an eased draw-in reveal or drawn underline. Time them to the spoken takeaway and let them remain long enough to read. Do not turn every sentence into kinetic typography or cover the main diagram.

For technical or easily confused sections, provide two to four concise supporting bullets beside the main visual. Reveal or emphasise the relevant point with the narration and retain the short list as an orientation aid. Reserve space explicitly, resize/recentre the visual smoothly, and check for collisions. Bullets support visual reasoning; they do not replace it.

Record narration engine, voice, sound effects, music and ambience choices in the job brief. Respect the latest per-job direction, including silence where requested. Keep stems separable, audit the actual mix by listening, and retain asset licences and attribution.

## Job independence
Use the selected job’s original research, brief and approval record. Another version’s script, storyboard, timing, art, audio choices and rendered examples are creative work, not shared pipeline inputs. Share only generic runtime, design primitives and production tooling unless the user explicitly requests reuse. Keep all project names, approvals, selected assets, output paths and production status out of this guide and the shared skill.
