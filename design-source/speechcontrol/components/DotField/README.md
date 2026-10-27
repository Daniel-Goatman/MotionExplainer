Use DotField for dense dot material that forms a shape, such as a device screen, a capacity mass or a map.

**Provide:** `width`, `height`, `pitch` (2.5–5px) and `radius` (1–1.5px), a `shape(u, v) => 0..1` mask in unit coordinates, and a `color`.

**Controller:** `set(shape, color?)`. The field reveals upward on first draw.

**Use** it when density describes something. When morphing between shapes, move the same dots: material becomes the answer and is never replaced.

**Don't** scatter random dots, use chunky low-resolution dots, or lay decorative residue along edges.
