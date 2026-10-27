Use CapacityBar as a slim 4px part-to-whole strip under a total ("812 GB used of 1,000"), split by category and linked to the main visual.

**Provide:** `items` as `[{value, tone?}]`, an optional `free` amount and an optional `onHover(i|null|-1)`. The free segment reports `-1`.

**Controller:** `highlight(i|null)`. The hovered segment thickens and the others fade.

**Don't** label segments inside the bar, or use it as the only visual when the parts matter. It supports a primary visual and doesn't replace one.
