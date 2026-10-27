Use CarouselNav to step through a sequence. Position dots stretch into a pill on the current item, and round arrows sit beside them, with an optional "all side by side" overview button.

**Provide:** `count`, `index` (-1 means the overview), `overview` (boolean) and `onChange(i)`.

**Controller:** `set(i)`.

**Behaviour:** previous and next always move exactly one step. Previous from the overview goes to the last item, and next from the overview goes to the first. An expanded detail stays expanded across steps.

**Don't** use a long list when a carousel would do, or add a filmstrip that repeats the visual.
