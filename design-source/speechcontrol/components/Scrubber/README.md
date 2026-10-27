Use Scrubber to select along a meaningful ordered variable, such as months or years. It has a round knob with a halo, round stops, and a filled span up to the selection.

**Provide:** `stops` (labels), a starting `value`, and the callbacks `onChange(i)`, `onDragStart()` and `onDragEnd()`.

**Behaviour**
- While dragging, the knob follows the pointer exactly.
- On release, the knob springs onto the nearest stop.
- Dragging owns the selection: clear any hover in `onDragStart`, and ignore hover until the pointer genuinely moves again.
- Arrow keys step through the stops.

**Don't** add a scrubber when hover already gives the information, use it for thresholds, or let the knob sit outside its track.
