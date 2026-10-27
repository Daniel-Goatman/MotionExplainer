Use ComparisonColumns to compare this period with a previous level: solid columns in `accent`, the previous value as a fine `ink` line exactly as wide as its column, and any increase as a dotted rose slice.

**Provide:** `items` as `[{label, value, previous?}]`, plus `unit`, `height`, `max` and `onHover(i|null)`.

**Behaviour:** on hover the column lifts 3px and brightens, its neighbours dim, and a tooltip gives the exact value and the difference.

**Pair** it with a separate summary such as a total or a jar. Don't stack a second chart that repeats the same data.

**Don't** let level lines overhang their columns, and don't use pill-shaped columns with numbers perched on top.
