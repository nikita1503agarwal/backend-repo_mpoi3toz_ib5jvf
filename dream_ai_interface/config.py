"""Config module for Dream.AI

This module centralizes API keys for various AI providers. Keys are loaded from
environment variables when available, otherwise set to empty strings so the
application can run without immediate configuration.

Providers covered:
- OpenAI: OPENAI_API_KEY
- DeepSeek: DEEPSEEK_API_KEY
- Vidqu: VIDQU_API_KEY
- Kling: KLING_API_KEY
- Pika: PIKA_API_KEY
- Runway: RUNWAY_API_KEY

Usage:
    from dream_ai_interface.config import api_keys
    key = api_keys["openai"]
"""
from __future__ import annotations

import os
from typing import Dict

# Map env var names to public-facing provider keys
_ENV_TO_PROVIDER = {
    "OPENAI_API_KEY": "openai",
    "DEEPSEEK_API_KEY": "deepseek",
    "VIDQU_API_KEY": "vidqu",
    "KLING_API_KEY": "kling",
    "PIKA_API_KEY": "pika",
    "RUNWAY_API_KEY": "runway",
}


def _load_api_keys() -> Dict[str, str]:
    keys: Dict[str, str] = {}
    for env_name, provider in _ENV_TO_PROVIDER.items():
        keys[provider] = os.getenv(env_name, "")
    return keys


api_keys: Dict[str, str] = _load_api_keys()


__all__ = ["api_keys"]
