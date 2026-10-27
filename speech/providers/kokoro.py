"""Local Kokoro-82M narration via kokoro-mlx (Apple silicon).

Install separately (not a project dependency): `pip install kokoro-mlx`.
Model: set KOKORO_MODEL to a local model directory or a Hugging Face repo id
(default `mlx-community/Kokoro-82M-bf16`, downloaded on first use).
Voices: e.g. `bm_daniel`, `bf_emma`, `am_michael`, `af_heart`. Language defaults to British English.
"""
from __future__ import annotations

import os
from pathlib import Path

from .base import SpeechProvider


class KokoroProvider(SpeechProvider):
    name = "kokoro"

    def __init__(self, voice: str | None = None, speed: float = 1.0, **options):
        super().__init__(voice or "bm_daniel", speed, **options)
        try:
            from kokoro_mlx import KokoroTTS
        except ImportError as e:  # fail visibly with the fix
            raise RuntimeError("Kokoro provider needs kokoro-mlx: pip install kokoro-mlx (or choose another --provider)") from e
        model = os.environ.get("KOKORO_MODEL", "mlx-community/Kokoro-82M-bf16")
        self.language = options.get("language") or os.environ.get("KOKORO_LANGUAGE", "en-gb")
        self.tts = KokoroTTS.from_pretrained(model)

    def synthesize(self, text: str, out_wav: Path, voice: str | None = None, speed: float | None = None) -> None:
        from kokoro_mlx.playback import save_wav
        r = self.tts.generate(text, voice=voice or self.voice, speed=speed or self.speed, language=self.language)
        save_wav(r.audio, out_wav, r.sample_rate)
