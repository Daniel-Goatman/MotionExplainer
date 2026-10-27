Use Loader as the working indicator: a 4×4 grid of round dots crossed by a soft wave whose direction slowly turns.

**Provide:** an optional present-tense `text` ("Measuring the disk…"), and optionally `n`, `pitch`, `radius` and `color`.

**Controller:** `start(text?)`, `text(t)` swaps the status and `stop()`. Calling `stop()` collapses the whole row: once the answer settles, no working text or glyph remains.

**Do** let the answer's own material take over from the loader as soon as there is a truthful first state.

**Don't**
- Crop the dots.
- Show progress counts ("12 of 12").
- Leave the loader visible after the answer settles.
