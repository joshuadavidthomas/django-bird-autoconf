from __future__ import annotations

from django_bird.plugins import pm


def test_plugin_is_installed():
    plugins = pm.get_plugins()
    assert any(plugin.__name__ == "django_bird_autoconf.plugin" for plugin in plugins)
