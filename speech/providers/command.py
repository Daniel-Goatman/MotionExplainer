"""Run any text-to-speech command line you already have.

Set SPEECH_COMMAND to a command template. Placeholders:
  {text_file}  path to a UTF-8 file containing the sentence
  {out}        path the command must write audio to (any format ffmpeg can read)
  {voice}      the voice name passed with --voice
  {speed}      the speed passed with --speed

Examples:
  SPEECH_COMMAND='say -v Samantha -f {text_file} -o {out}.aiff'   (macOS; the .aiff suffix is detected)
  SPEECH_COMMAND='piper --model en_GB-alan-medium.onnx --output_file {out} < {text_file}'
"""
from __future__ import annotations

import os
import shlex
import subprocess
import tempfile
from pathlib import Path

from .base import SpeechProvider, to_wav


class CommandProvider(SpeechProvider):
    name = "command"

    def __init__(self, voice: str | None = None, speed: float = 1.0, **options):
        super().__init__(voice, speed, **options)
        self.template = options.get("command") or os.environ.get("SPEECH_COMMAND")
        if not self.template:
            raise RuntimeError("Set SPEECH_COMMAND (see speech/providers/command.py) to use the command provider")

    def synthesize(self, text: str, out_wav: Path, voice: str | None = None, speed: float | None = None) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            text_file = Path(tmp) / "line.txt"
            text_file.write_text(text, encoding="utf-8")
            raw = Path(tmp) / "speech"
            cmd = self.template.format(text_file=shlex.quote(str(text_file)), out=shlex.quote(str(raw)),
                                       voice=shlex.quote(voice or self.voice or ""), speed=speed or self.speed)
            subprocess.run(cmd, shell=True, check=True)
            produced = [p for p in Path(tmp).iterdir() if p.name.startswith("speech")]
            if not produced:
                raise RuntimeError(f"SPEECH_COMMAND wrote no audio for: {text[:60]}")
            to_wav(produced[0], out_wav)
