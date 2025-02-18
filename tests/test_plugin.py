from __future__ import annotations

import pytest
from django.conf import settings
from django.test import override_settings

from django_bird.conf import app_settings
from django_bird.plugins import pm
from django_bird_autoconf.plugin import DJANGO_BIRD_BUILTINS
from django_bird_autoconf.plugin import DJANGO_BIRD_FINDER
from django_bird_autoconf.plugin import AutoConfigurator


def test_plugin_is_installed():
    plugins = pm.get_plugins()
    pm.load_setuptools_entrypoints("bird")
    assert any(plugin.__name__ == "django_bird_autoconf.plugin" for plugin in plugins)


class TestAutoConfigurator:
    @pytest.fixture(autouse=True)
    def unregister_plugin(self):
        print(f"{pm.get_plugins()=}")
        assert any(
            plugin.__name__ == "django_bird_autoconf.plugin"
            for plugin in pm.get_plugins()
        )
        plugins = pm.list_name_plugin()
        for plugin in plugins:
            print(f"{plugin=}")
        print(f"{pm.is_registered('autoconf')=}")
        pm.unregister(name="autoconf")
        print(f"{pm.is_registered('autoconf')=}")
        plugins = pm.list_name_plugin()
        for plugin in plugins:
            print(f"{plugin=}")

    @pytest.fixture
    def configurator(self):
        return AutoConfigurator(app_settings)

    def test_autoconfigure(self, configurator):
        template_options = settings.TEMPLATES[0].get("OPTIONS", {})

        assert DJANGO_BIRD_BUILTINS not in template_options.get("builtins", [])
        assert DJANGO_BIRD_FINDER not in settings.STATICFILES_FINDERS

        configurator.autoconfigure()

        assert DJANGO_BIRD_BUILTINS in template_options.get("builtins", [])
        assert DJANGO_BIRD_FINDER in settings.STATICFILES_FINDERS

    @override_settings(
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.jinja2.Jinja2",
            }
        ],
    )
    def test_non_django_template_engine(self, configurator):
        template_options = settings.TEMPLATES[0].get("OPTIONS", {})

        configurator.configure_templates()

        assert DJANGO_BIRD_BUILTINS not in template_options.get("builtins", [])

    def test_configure_builtins(self, configurator):
        template_options = settings.TEMPLATES[0].get("OPTIONS", {})

        assert DJANGO_BIRD_BUILTINS not in template_options.get("builtins", [])

        configurator.configure_builtins(template_options)

        assert DJANGO_BIRD_BUILTINS in template_options.get("builtins", [])

    def test_configure_staticfiles(self, configurator):
        assert DJANGO_BIRD_FINDER not in settings.STATICFILES_FINDERS

        configurator.configure_staticfiles()

        assert DJANGO_BIRD_FINDER in settings.STATICFILES_FINDERS

    def test_configured(self, configurator):
        assert configurator._configured is False

        configurator.autoconfigure()

        assert configurator._configured is True

    # @override_settings(
    #     **{
    #         "STATICFILES_FINDERS": [
    #             "django.contrib.staticfiles.finders.FileSystemFinder",
    #             "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    #         ],
    #         "TEMPLATES": [
    #             {
    #                 "BACKEND": "django.template.backends.django.DjangoTemplates",
    #                 "DIRS": [],
    #                 "APP_DIRS": True,
    #                 "OPTIONS": {
    #                     "context_processors": [
    #                         "django.template.context_processors.request",
    #                         "django.contrib.auth.context_processors.auth",
    #                         "django.contrib.messages.context_processors.messages",
    #                     ],
    #                 },
    #             },
    #         ],
    #     }
    # )
    # def test_startproject_settings(self, configurator, example_template):
    #     configurator.autoconfigure()
    #
    #     template_options = settings.TEMPLATES[0]["OPTIONS"]
    #
    #     assert DJANGO_BIRD_BUILTINS in template_options["builtins"]
    #     assert DJANGO_BIRD_FINDER in settings.STATICFILES_FINDERS
    #
    #     with pytest.raises(TemplateDoesNotExist, match=example_template.base.name):
    #         Template(example_template.content).render(Context({}))
