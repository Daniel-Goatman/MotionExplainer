Use Timeline for moments spaced by real time, so that long gaps can be felt. Each moment is a small solid dot in its era's colour with a `halo`. Dots grow on hover and are largest when current.

**Provide:** `events` as `[{label, at, tone?}]` (where `at` is a number such as fractional years), an optional `ticks` as `[{label, at}]`, plus `value` and `onSelect(i)`.

**Controller:** `select(i)`.

**Don't** use hollow rings, list counts ("5 events"), or space moments evenly when the time between them matters.
