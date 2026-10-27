Use Tooltip as the pill readout of exact values on hover. It sits above the hovered mark and slides between marks rather than jumping.

**Provide:** a positioned `host` (the visual's container). Call `show(html, x, y)` with coordinates in host space, and `hide()`.

**Content:** name · **value** · difference or share, e.g. "Jun · **230** kWh · −21 vs 251". Use `v-up` and `v-down` spans for direction.

**Don't** put instructions, links or more than one line in a tooltip, or let it leave the host.
