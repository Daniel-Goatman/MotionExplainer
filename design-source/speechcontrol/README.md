# SpeechControl Visuals

The design system for visual answers. This directory is the source of truth. Preview every component locally by serving the repo root and opening `Design/preview.html`. Tokens live in `tokens.json` (compiled to `tokens.css`), components in `components/` (`bundle.js`, `bundle.css`, and a `README.md` plus `preview.html` per component).

Visual answers in the SpeechControl sidebar. One bold, dominant visual carries the answer, with a single short sentence beside it. Everything else is revealed by interaction: hover gives exact values and explanations, and a click opens the deeper layer. The identity (colour, type, geometry, motion and how controls feel) is fixed here. Layout and the interaction design stay free for each answer, so build them from the components and rules below rather than from a template.

## Fixed and free

| Fixed by this system | Free for each answer |
| --- | --- |
| Tokens: colour roles, the type scale, spacing, radii, easing and duration | What the visual is: columns, area tiles, a field of dots, devices, a map, a timeline |
| Component finish: round controls, tooltips, rolling digits, text swaps, loader | How parts are sized, shaped, positioned and stacked |
| Interaction contract: hover is light, click is heavy, drag owns selection | Which behaviours are combined (a drill-in carousel whose item count follows the selection is fine) |
| Composition rules: one hero visual, one sentence, no containers | The order in which information is revealed, and how many levels deep it goes |

Never restyle a component to make it fit. Compose components, or draw new marks with the tokens.

## Content fundamentals

- **Answer first.** Open with the conclusion in plain words: "Documents, Photos and Xcode take **524 GB**, almost two thirds of what's used." Never describe the visual ("This chart shows…").
- **One sentence at rest, one sentence on hover.** At rest the caption summarises the whole answer. On hover it explains the item: what it is, its exact value and its share ("Photos Library · **168 GB** · 16.8% of the disk"). Two lines at most.
- **Bold the figures, not the words.** Figures go in `ink` at weight 500. Everything else in the sentence is `ink-soft`.
- **Units stay with their numbers.** Write "812 GB used of 1,000" and "−7.6%", with a thin space before units only where the font needs it. Use thousands separators and a true minus sign (−).
- **No metadata or process text in the result.** Leave out counts of readings, date ranges that are already visible, labels such as "energy_report" or "1 particle = 1 kWh", coordinates, and instructions like "click to open" or "drag to explore". Show that something can be opened with an affordance (a round **+**), not with words.
- **Working text exists only while working.** Write it in the present tense with an ellipsis ("Measuring the disk…", "Scoring places…"), then remove the whole row once the answer settles.
- **Sentence case everywhere.** British spelling ("colour"). No emoji, no exclamation marks.
- **The question stays visible.** It sits in the Ask bubble at the top right, exactly as asked.

## Visual foundations

### Colour

- **Surfaces.** The sidebar is `canvas`. The answer lives on `raised`, and nothing inside it gets another background: no cards and no boxes. The only extra surfaces are `bubble` (the question, tooltips and resting round buttons) and `paper` (illustrated objects such as device screens).
- **Text.** Use `ink` for figures and selected labels, `ink-soft` for sentences and captions, and `ink-mute` for axis and kicker labels only. On a category fill or on `paper`, use `on-tone`.
- **Categories.** Use `blue`, `teal`, `lavender`, `amber`, `rose`, `slate` and `olive`, in that order, as **flat fills** with `on-tone` labels. A category keeps its colour everywhere in an answer: field, legend dot, legend value, tooltip and drag knob. Parts inside a category are stepped shades of the parent (100%, 78% and 56% of it mixed toward `canvas`), never new hues.
- **Restraint.** Use as many categories as the comparison needs and no more. A single-subject answer uses one `accent` hue. A two-way comparison uses `teal` for less or saved and `rose` for more. Never cycle hues by index for decoration.
- **Texture.** The only texture is `free-dot`, on empty or free space. Never pattern a data fill.
- **Themes.** Clear is the theme for answers: cool charcoal with a `blue` accent. Warm (the warmer Living Scene tones: cream `paper`, warm ink, an `amber` accent) is parked: it stays in the tokens, but answers don't use it for now.
- **Never use** glows, gradients, drop shadows, neon, or washed-out pale fills. `halo` is the only shadow token, and it is a solid ring in the panel colour.

### Type

- Use the system sans (`--font-sans`) only. Never use serifs, and never use mono for figures.
- Set the hero number in `figure-xl` (at most one per answer), a selected subject's name in `figure-lg`, and inline headline figures in `figure-md` next to a `body`-sized unit sentence.
- Use `lede` for a conclusion that leads with words, and `body` for captions. `label` is for legends, tile names and status text, `data` for axis and mark labels and tooltips, and `kicker` for one uppercase micro-label per view.
- Every figure uses tabular numerals and changes through `RollingNumber`. Never animate a fact through invented intermediate values: the roll moves digits, and it does not count up.

### Geometry

- **Round language.** Use circles for dots, knobs, playheads and timeline points, and pills for tooltips and the return link. Never use square handles or switches. Timeline points are solid dots in their era colour with a `halo`, never hollow rings.
- **Radii.** Columns use `radius-mark` on top and 3px at the base. Tiles and small devices use `radius-tile`, a containing scene `radius-scene`, and the panel `radius-panel`.
- **Hairlines.** Baselines, rails and axes are 1px `line`, and level markers are 2px `ink` at 60%. A marker is exactly as wide as its mark, with no overhang. Where it falls inside a mark, cut it in the panel colour.
- **Illustrations use real proportions.** Phones are about 9:19.5 and a laptop lid about 1.54:1. A notch or island is drawn at its true fraction of the device, with a minimum size so it stays visible. Check every drawing by rendering it at real size: if two states claim to differ, they must look different.
- **Dot material.** Dot fields need real resolution: a pitch of 2.5 to 5px and a radius of 1 to 1.5px. A dot field must be dense enough to read as a form, never as a few chunky icons.
- **Nothing leaves its bounds.** Hover never changes the size of a container: reserve space for any text that can change.

### Layout and density

- The answer panel is 420px wide by default (it works down to 360px). It may grow to 720px when the visual genuinely needs it, such as a map, a network or a dense comparison; it never grows just to fit more text. The inset is 22px on the sides and top and 20px at the bottom.
- From top to bottom, an answer runs: Ask bubble, then the working row (removed once settled), then the headline figure or lede, then **the visual (most of the height)**, then one caption, then an optional legend or navigation row.
- Show the overview first and let interaction reveal the depth. Sequences end on, or can switch to, an overview showing every step side by side.
- A summary sits apart from its parts, like a jar beside the months or a total beside the tiles.
- Prefer a carousel with expandable detail over a long list. An expanded detail stays expanded as you step.
- Never stack two charts that show the same thing. Never add a control that doesn't change what you understand: a scrubber needs a meaningful ordered variable, and a threshold slider is almost never right.

### Motion

Motion explains change: things move from where they were to where they now mean something.

- **Loading becomes the result.** The material of the working state (grains, dots, a measuring fill) turns into the answer. It is never thrown away and replaced.
- **Travel follows arcs.** Use `ease-travel` and `dur-travel`, stagger grains by 45ms, and move a form as one coherent group with a shared curve. Don't split a form into ghosts, and don't draw a destination outline before the form arrives.
- **Springs settle things.** Use `ease-spring` for digits, presses and dots growing, and `ease-morph` for layout and shape changes.
- **Reverse is as good as forward.** A drill-out mirrors the drill-in. An interrupted transition picks up from the element's current position; it never resets or queues.
- **Stories are optional.** Any authored playthrough shows `StoryControls` (skip and replay) from the first frame, and skip goes to the true settled state.
- **Waves ease in and out.** Ambient motion such as a wave or a pulse fades its amplitude in and out and moves continuously in time, never in steps. It stops once the answer settles.
- **Respect `prefers-reduced-motion`.** Jump to the settled state, with no travel and no rolls.

### Interaction states

| Input | What happens | Duration |
| --- | --- | --- |
| Hover a mark | The mark lifts 3px or scales to 1.015 and brightens; the others dim to 55%; its legend item and bar segment respond (linked highlighting); the caption explains it instantly | `dur-hover` |
| Leave | The summary caption returns | `dur-swap` |
| Click | A heavy change: drill in, morph, carousel step, replay of one segment | `dur-morph` |
| Drag | Owns the selection. Pressing clears hover, and hover stays off until the pointer genuinely moves again (more than 3px) | — |
| Keyboard | ← and → step, Enter opens, Esc returns to the overview; focus is shown with `focus` | — |

Hover must never trigger a heavy morph, flash during fast sweeps, wait behind another transition, or blank the text.

## Iconography

There is no icon font and no logo. The few glyphs are inline 12px SVGs with a 1.8 stroke, round caps and joins, and `currentColor`: chevrons, skip, replay, plus and overview. They always sit inside a round button. Never use emoji or icons as decoration, and never use mascots, faces or characters.

## Components

| Component | Use it for |
| --- | --- |
| `AnswerPanel` | The raised surface every answer sits on |
| `Ask` | The user's question, top right |
| `Loader` | The working indicator: a 4×4 dot grid crossed by a soft wave |
| `StoryControls` | Round skip and replay buttons for authored playthroughs |
| `RollingNumber` | Every changing figure |
| `SwapText` | Every changing sentence or label |
| `Tooltip` | Exact values on hover |
| `Legend` | Category names and values, linked to the visual |
| `CapacityBar` | Slim part-to-whole strip under a total |
| `AreaTiles` | Part-to-whole in flat tiles, with drill-in |
| `ComparisonColumns` | This period against a previous level |
| `Scrubber` | Selecting along a meaningful ordered variable |
| `Timeline` | Moments spaced by real time |
| `CarouselNav` | Stepping through a sequence, plus an overview |
| `ReturnLink` | The quiet way back from a drill-in |
| `DotField` | Dense dot material for illustrated forms |

Every component is a function, `Visuals.<Name>(host, props)`, that renders into `host` and returns a controller (`set`, `select`, `open`, `close`, `destroy`). Each one's README lists what the caller provides.

## Primitives and patterns

Under the components sit `primitives/` and `patterns/` (see `primitives/README.md`):
- marks: tile, column, bar, dot, ring, label, free space, line and area;
- stackable behaviours: hover, select, drill, enter and step;
- layout helpers, a state store with derived values, and `Grains` dot material that gathers, waves and travels on arcs;
- `scene` for the answer's order, `draw` for custom forms, and `filterStyles`, which removes off-token colours and fonts and snaps sizes, radii and timings to tokens.

Use them when an answer needs a form or interaction no component has. The same layer is also available as declarative elements (`<v-stage>`, `<v-mark>`, `<v-columns>`, `<v-area-tiles>`, `<v-timeline>`, `<v-scrubber>`, `<v-carousel>`, `<v-figure>`, `<v-caption>`, `<v-return>`, `<v-grains>`), which the answer frame builds at every streamed stage without generated script; see `primitives/README.md`. Patterns rebuild components from these pieces with the same API: AreaTiles is rebuilt so far and is pixel-identical to the authored component (`node Tools/design-baseline.mjs diff`). The Canvas answer frame inlines all of this through `python3 Tools/design-into-canvas.py`.
