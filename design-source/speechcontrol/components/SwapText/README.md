Use SwapText for every sentence or label that changes: the old text lifts away with a short blur, and the new text arrives from below.

**Provide:** an initial `html`. Use `block` to render a div, and `className` (usually `v-caption`).

**Controller:** `set(html, {instant})`. The latest call always wins and changes never queue.

**Use** `instant: true` for hover explanations, which must be readable within `dur-hover`, and the animated swap for state changes.

**Don't** let old and new text overlap legibly, or blank the text while a transition plays.
