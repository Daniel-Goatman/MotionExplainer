Use AreaTiles for part-to-whole in flat category tiles sized by area, with free space as dotted empty floor and drill-in on parts that have children.

**Provide:** `items` as `[{label, value, tone?, parts?: [{label, value}]}]`, plus `total`, `unit`, `width` and `height`, and the callbacks `onHover(i|null|-1)`, `onOpen(i)`, `onClose(i)` and `onHoverPart(i, j)`.

**Controller:** `open(i)`, `close()` and `highlight(i)`. Pair it with `ReturnLink` and wire Esc to `close()`.

**Behaviour**
- On hover, the tile lifts and brightens and the others dim. Drive the caption and the CapacityBar from `onHover`.
- Opening a tile grows it from its place and splits it into stepped shades of its colour.
- Closing merges the parts and shrinks the tile home while the others return: a mirror of opening.
- A round **+** marks the tiles that open.

**Don't** add textures to tiles, add more than seven categories, or label the tiles with instructions.
