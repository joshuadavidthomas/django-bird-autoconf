from __future__ import annotations

from contextlib import suppress
from typing import Any
from typing import final

import django.template
from django.conf import settings

from django_bird import hookimpl
from django_bird.conf import AppSettings
from django_bird.conf import app_settings


@hookimpl
def pre_ready():
    configurator = AutoConfigurator(app_settings)
    configurator.autoconfigure()


DJANGO_BIRD_BUILTINS = "django_bird.templatetags.django_bird"
DJANGO_BIRD_FINDER = "django_bird.staticfiles.BirdAssetFinder"


@final
class AutoConfigurator:
    def __init__(self, app_settings: AppSettings) -> None:
        self.app_settings = app_settings
        self._configured = False

    def autoconfigure(self) -> None:
        self.configure_templates()
        self.configure_staticfiles()
        self._configured = True

    def configure_templates(self) -> None:
        template_config = None

        for config in settings.TEMPLATES:
            engine_name = config.get("NAME") or config["BACKEND"].split(".")[-2]
            if engine_name == "django":
                template_config = config
                break

        if template_config is None:
            return

        options = template_config.setdefault("OPTIONS", {})

        self.configure_builtins(options)

        # Force re-evaluation of settings.TEMPLATES because EngineHandler caches it.
        with suppress(AttributeError):  # pragma: no cover
            del django.template.engines.templates
            django.template.engines._engines = {}  # pyright: ignore[reportAttributeAccessIssue]

    def configure_builtins(self, options: dict[str, Any]) -> None:
        builtins = options.setdefault("builtins", [])

        builtins_already_configured = DJANGO_BIRD_BUILTINS in builtins

        if not builtins_already_configured:
            builtins.append(DJANGO_BIRD_BUILTINS)

    def configure_staticfiles(self) -> None:
        finders_already_configured = DJANGO_BIRD_FINDER in settings.STATICFILES_FINDERS

        if not finders_already_configured:
            settings.STATICFILES_FINDERS.append(DJANGO_BIRD_FINDER)
