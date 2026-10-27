Use StoryControls on any authored playthrough longer than a loading moment: a round skip button and a round replay button.

**Provide:** `onSkip`, which jumps straight to the true settled state, and `onReplay`, which restarts from the question.

**Show** them from the first frame, in the panel's top row.

**Don't** make users wait through a story. Skip must leave no half-finished state behind: cancel every pending timer.
