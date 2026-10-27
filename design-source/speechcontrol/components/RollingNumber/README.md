Use RollingNumber for every figure that can change: digit columns spring to the new value (NumberFlow style), keyed by place value.

**Provide:** `value`, an optional `format(v) => string` (for signs, percentages or units such as "−7.6%"), and an optional `size` (`xl`, `lg`, or the default md).

**Controller:** `set(v)`.

**Use** `xl` for the single hero number, `lg` for a selected subject's total, and md inline with a caption-sized unit.

**Don't** tween through invented intermediate values, or let digits shift baseline mid-roll. Under reduced motion the new value appears at once.
