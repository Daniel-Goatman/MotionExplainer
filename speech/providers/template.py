"""Template for a hosted speech service (for example ElevenLabs or OpenAI text-to-speech).

Copy this file, rename the class and `name`, implement `synthesize`, then register it in
speech/providers/__init__.py. Nothing here calls a network service: wiring an API, its
credentials and its costs is your decision.

Guidelines:
- Read credentials from environment variables; never commit them.
- Return one file per sentence. If the service returns MP3/OGG, save it and call `to_wav`.
- Keep the voice and model fixed for a whole film so the narration stays consistent.
"""
from __future__ import annotations

from pathlib import Path

from .base import SpeechProvider, to_wav  # noqa: F401  (to_wav is useful for non-WAV responses)


class HostedSpeechProvider(SpeechProvider):
    name = "hosted-template"

    def __init__(self, voice: str | None = None, speed: float = 1.0, **options):
        super().__init__(voice, speed, **options)
        # e.g. self.api_key = os.environ["YOUR_SERVICE_API_KEY"]; create your client here.
        raise NotImplementedError("Copy speech/providers/template.py and implement your service")

    def synthesize(self, text: str, out_wav: Path, voice: str | None = None, speed: float | None = None) -> None:
        # 1. Send `text` with `voice or self.voice` to your service.
        # 2. Write the returned audio to a temporary file.
        # 3. to_wav(temp_file, out_wav)
        raise NotImplementedError
