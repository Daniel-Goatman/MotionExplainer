"""The speech provider contract.

A provider turns one sentence of narration into one WAV file. Everything else in the pipeline
(scheduling, cue measurement, captions) only reads those WAV files, so any runtime that can
produce speech audio can be plugged in here.
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


class SpeechProvider:
    """Subclass this, set `name`, and implement `synthesize`."""

    name = "base"

    def __init__(self, voice: str | None = None, speed: float = 1.0, **options):
        self.voice = voice
        self.speed = speed
        self.options = options

    def synthesize(self, text: str, out_wav: Path, voice: str | None = None, speed: float | None = None) -> None:
        """Write `text` as speech to `out_wav` (any sample rate; mono preferred)."""
        raise NotImplementedError

    def close(self) -> None:
        """Release models or connections. Optional."""


def to_wav(src: Path, out_wav: Path) -> None:
    """Convert any audio file ffmpeg can read (mp3, ogg, m4a...) to a 24 kHz mono WAV."""
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is required to convert provider output to WAV")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-ac", "1", "-ar", "24000", str(out_wav)], check=True)
