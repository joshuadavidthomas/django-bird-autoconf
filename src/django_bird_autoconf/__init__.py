from __future__ import annotations

from importlib.metadata import version

try:
    __version__ = version("django_bird_autoconf")
except ImportError:
    __version__ = "0.0.0"
