Use Legend for category names and values, linked to the visual: hovering a legend item highlights its marks, and the visual highlights the legend in return.

**Provide:** `items` as `[{label, value?, tone?, free?}]`, plus an optional `onHover(i|null)` and `onSelect(i)`.

**Controller:** `highlight(i|null)`.

**Values** take their category colour. Free space uses the free-dot colour.

**Don't** use a legend when the marks can be labelled directly, or list more than seven categories.
