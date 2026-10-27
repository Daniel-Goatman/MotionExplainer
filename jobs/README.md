# Jobs

Each video lives in its own folder, `jobs/<job-id>/`, which is git-ignored by default. A job holds its brief, source references, storyboards, approvals, narration script, timing, scenes (`index.ts` + `src/`), `public/` assets and `out/` renders.

Minimal layout:

```
jobs/<job-id>/
  README.md            brief, audience, decisions, approvals, voice and sound choices
  research/            source material (or links to it)
  storyboard/          drawn chapter references and storyboards
  audio/segments.json  narration sentences with cue phrases
  index.ts             registerRoot(...) for this job only
  src/                 scenes and timeline
  public/              job assets (narration WAVs land in public/audio/...)
  out/                 stills, review renders and deliverables
```

Run a job with `node scripts/video-job.mjs <job-id> studio|render|still ...` (see PIPELINE.md).
