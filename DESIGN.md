# SpeechControl Visuals for video explainers

## Authority
The intended design system is **SpeechControl Visuals**, shared by Codex and Claude. The pinned reference is design-source/speechcontrol/; its README, tokens and component contracts are copied without modification. See docs/provenance.json for hashes. Update this snapshot deliberately; do not silently follow changes in another project.

src/design/tokens.ts imports that JSON directly. No second handwritten palette. Clear is the default; Warm is an explicit per-project choice. Both agents follow this document and the same tokens.

## Preserve the system
One dominant visual and one short conclusion at each beat; reveal detail progressively. Answer first, use sentence case and British spelling. Bold figures rather than prose. Use tabular system-sans numerals; never mono figures or invented count-up values.

Use canvas behind a raised answer surface, with no nested cards. Bubble is for callouts/controls and paper for illustrated objects. Categories keep their colour identity through every view. Use only as many hues as the information needs. Clear uses blue accent; Warm uses amber. No glows, gradients, drop shadows, neon or decorative icons. Free-dot texture belongs only in empty/free space. Geometry remains round; object illustrations retain real proportions.

Use the source type hierarchy, spacing, radii and motion roles. The source permits purposeful spring settling; do not carry forward the previous blanket no-bounce rule. It does not license arbitrary bounce or old ink/typing/wipe signatures.

## Adaptation to linear video
- Hover: authored focus beat with linked highlighting and a short exact-value caption. Do not draw a fake cursor by default.
- Click/drill-in: a scheduled morph, preserving identity and context. End with the overview where useful.
- Drag/scrubber: a controlled sweep through a meaningful ordered variable, with explicit settled values.
- RollingNumber: animate digit columns between real values, not fabricated intermediate facts. Preserve place-value alignment and tabular figures.
- SwapText: retain its short outgoing/incoming movement. Verify any blur in rendered frames before enabling it; avoid legible overlaps and blank gaps.
- DotField: coherent forms, dense dots, arcs and source travel timing; no ghost duplicates or premature destination outline.
- Ask: show the real question only when the brief calls for a question-led explainer. Do not invent chat chrome.
- Skip/replay, hover, focus and reduced-motion interaction remain player/interactive-preview concerns. Do not burn non-functional controls into an MP4. A reduced-motion export can be a separate option.

Convert CSS bezier values to frame-evaluated easing. Never run the source imperative DOM controllers, CSS transitions or timers as video animation. Preserve duration in seconds; scale spatial measurements for the canvas. The source's 420px sidebar layout is not a 16:9 video template. Validate adapted type, line weights and dot density at actual playback size before approval.

## Implementation boundary
Import tokens into reusable React primitives; compose each job’s own scenes from those primitives. The reference snapshot documents the interactive system; it is not a fully ported Remotion component library. Translate only the behaviours needed by the approved storyboard into deterministic frame-driven components. Keep domain-specific scenes and prototypes inside their job.

Render reference frames and transition midpoints to check clipping, hierarchy, alignment and motion. Use VIDEO-GENERATION.md for storyboarding, duration, continuity and review. Readiness and verification results belong in the selected job, never in this design authority.
