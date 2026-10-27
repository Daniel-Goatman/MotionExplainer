"""Speech provider registry. Add your provider here to make it selectable with --provider."""
from __future__ import annotations

import importlib

PROVIDERS = {
    "kokoro": ("speech.providers.kokoro", "KokoroProvider"),
    "command": ("speech.providers.command", "CommandProvider"),
    # "my-service": ("speech.providers.my_service", "MyServiceProvider"),
}


def load(name: str):
    if name not in PROVIDERS:
        raise SystemExit(f"Unknown speech provider '{name}'. Available: {', '.join(PROVIDERS)}")
    module, cls = PROVIDERS[name]
    return getattr(importlib.import_module(module), cls)
