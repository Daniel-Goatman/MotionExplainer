Use AnswerPanel as the raised surface that holds one visual answer, with the question bubble at the top right.

**Provide:** a `host` element, an optional `question` string and an optional accessible `label`. Put your content in the returned `body`; `top` takes the Ask bubble and `StoryControls`.

**Use** one panel per answer, 420px wide (it works down to 360px).

**Do**
- Sit every mark flush on the panel.

**Don't**
- Nest cards, boxes or bordered groups inside it.
- Give inner regions a background.
- Add a second panel for the same answer.
