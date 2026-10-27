"""Generate narration clips for a job: one WAV per sentence, plus durations.json.

Usage (from the repository root):
  python3 -m speech.synthesize jobs/<job>/audio/segments.json jobs/<job>/public/audio/narration \
      [--provider kokoro|command|...] [--voice NAME] [--speed 1.0] [--only ID ...]

segments.json is a list of {"id": "...", "text": "..."} (optional per-line "voice" and "speed").
Provider and voice can also come from SPEECH_PROVIDER and SPEECH_VOICE.
Existing clips are kept unless their text changed or --force is given.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from pathlib import Path

from speech.providers import load


def wav_seconds(path: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, check=True).stdout
    return float(out)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("segments")
    ap.add_argument("out_dir")
    ap.add_argument("--provider", default=os.environ.get("SPEECH_PROVIDER", "kokoro"))
    ap.add_argument("--voice", default=os.environ.get("SPEECH_VOICE"))
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--only", nargs="*", help="regenerate only these ids")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    segs = json.loads(Path(a.segments).read_text())
    out = Path(a.out_dir); out.mkdir(parents=True, exist_ok=True)
    manifest_path = out / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    provider = None
    durations = {}
    try:
        for s in segs:
            wav = out / f"{s['id']}.wav"
            key = hashlib.sha256(f"{a.provider}|{s.get('voice') or a.voice}|{s.get('speed', a.speed)}|{s['text']}".encode()).hexdigest()
            wanted = a.only is None or s["id"] in a.only
            if wav.exists() and ((manifest.get(s["id"]) == key and not a.force) or not wanted):
                durations[s["id"]] = round(wav_seconds(wav), 3)
                continue
            if provider is None:
                provider = load(a.provider)(voice=a.voice, speed=a.speed)
            provider.synthesize(s["text"], wav, voice=s.get("voice"), speed=s.get("speed"))
            manifest[s["id"]] = key
            durations[s["id"]] = round(wav_seconds(wav), 3)
            print(f"{s['id']}  {durations[s['id']]:.2f}s", flush=True)
    finally:
        if provider is not None:
            provider.close()
        manifest_path.write_text(json.dumps(manifest, indent=1))
    (out / "durations.json").write_text(json.dumps(durations, indent=1))
    print(f"{len(durations)} clips, {sum(durations.values()):.1f}s of narration")


if __name__ == "__main__":
    main()
