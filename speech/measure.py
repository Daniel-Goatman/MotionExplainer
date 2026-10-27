"""Measure narration clips and place cue anchors on the voiced audio. Provider-independent.

Usage: python3 -m speech.measure segments.json clip_dir timing.json

Each segment may carry "cues": {"key": "phrase in the sentence"}. ffmpeg silencedetect finds the voiced
spans of each clip; a cue's time is its character offset mapped across the voiced time with internal
pauses removed, so emphasis lands after a comma pause rather than inside it. Output per clip:
{"dur": seconds, "voiced": [[start, end], ...], "cues": {"key": seconds}}.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


def main() -> None:
    segs = json.loads(Path(sys.argv[1]).read_text())
    clips = Path(sys.argv[2])
    out = {}
    for s in segs:
        wav = clips / f"{s['id']}.wav"
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(wav)],
                                   capture_output=True, text=True, check=True).stdout)
        log = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(wav), "-af", "silencedetect=noise=-40dB:d=0.12", "-f", "null", "-"],
                             capture_output=True, text=True).stderr
        starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
        ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
        voiced, t = [], 0.0
        for a, b in zip(starts, ends + [dur] * (len(starts) - len(ends))):
            if a > t + 0.01:
                voiced.append((t, a))
            t = b
        if t < dur - 0.01:
            voiced.append((t, dur))
        voiced = voiced or [(0.0, dur)]
        total = sum(b - a for a, b in voiced)

        def at(frac: float) -> float:
            want = frac * total
            for a, b in voiced:
                if want <= b - a:
                    return a + want
                want -= b - a
            return voiced[-1][1]

        text = s["text"]
        cues = {}
        for k, phrase in s.get("cues", {}).items():
            if phrase not in text:
                raise SystemExit(f"Cue '{k}' phrase not found in {s['id']}: {phrase!r}")
            cues[k] = round(at(text.index(phrase) / len(text)), 3)
        out[s["id"]] = {"dur": round(dur, 3), "voiced": [[round(a, 3), round(b, 3)] for a, b in voiced], "cues": cues}
    Path(sys.argv[3]).write_text(json.dumps(out, indent=1))
    print(f"measured {len(out)} clips")


if __name__ == "__main__":
    main()
