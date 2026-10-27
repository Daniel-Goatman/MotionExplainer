# Shared video production pipeline

## Workspace boundary
The root owns the pinned runtime, design-source/speechcontrol, src/design and reusable primitives, shared public assets, scripts and authoring guidance. The default src/index.ts entry point contains a blank composition only.

Each jobs/<job-id> owns its brief, original-source references, chapter plan, drawn references/storyboards, approvals, narration, timeline, scene implementation, public assets, renders, deliverables and verification records. Give each job its own index.ts or index.tsx and public directory. Never register a private job globally in the shared Root.

## Production sequence
1. Establish the job brief, audience, claims and source boundary, including uncertainties and illustrative data.
2. Draw one visual reference per chapter, then actual per-chapter storyboards with continuous bridges. Review and obtain approval before animation.
3. Set per-job voice and sound choices. Render and listen to a representative narrated sample; review explanation, movement and sound before expanding production.
4. Assemble from measured narration and a frame-based timeline. Schedule named-object emphasis and explanatory actions. Do not freeze frames where motion is still meaningful.
5. Review representative frames and actual passages, including technical sections and transition midpoints. Check source grounding, captions, audio, complete decode and final-player seeking. Record limitations honestly.
6. Save outputs and evidence inside the job. External publishing is a separate authorised action.

## Commands
From this workspace, use the installed runtime without fetching packages:

```sh
node scripts/video-job.mjs <job-id> studio
node scripts/video-job.mjs <job-id> compositions
node scripts/video-job.mjs <job-id> still <composition-id> check.png --frame=120
node scripts/video-job.mjs <job-id> render <composition-id> picture.mp4 --muted
```

Narration (one WAV per sentence, then cue timing measured on the voiced audio):

```sh
python3 -m speech.synthesize jobs/<job-id>/audio/segments.json jobs/<job-id>/public/audio/narration --provider kokoro --voice bm_daniel
python3 -m speech.measure jobs/<job-id>/audio/segments.json jobs/<job-id>/public/audio/narration jobs/<job-id>/src/timing.json
```

Providers live in speech/providers. Use `--provider command` with SPEECH_COMMAND for any local text-to-speech CLI, or copy speech/providers/template.py to add a hosted service. Scenes read only the WAV files and timing JSON, so changing provider never touches scene code.

The runner supplies that job’s entry point and public directory, and puts still/render filenames under its out directory. Audio assembly and delivery commands belong in the job brief. Existing local render scripts may use explicit paths; they must supply the same job-specific public directory.

Shared assets can be linked from a job’s public directory, with provenance. Job-specific media must stay in that job. Document any local presentation URL or compatibility symlink in the job’s output mapping.

Do not install or update dependencies to run these commands. Before any dependency change or package execution, verify the effective maturity gate. Scripts do not bypass it.
