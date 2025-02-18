from __future__ import annotations

from django_bird.plugins import pm


def test_plugin_is_installed():
    assert pm.has_plugin("autoconf")
