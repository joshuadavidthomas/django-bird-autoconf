from __future__ import annotations

import logging
from pathlib import Path

import pytest
from django.conf import settings

pytest_plugins = []


def pytest_configure(config: pytest.Config) -> None:  # pyright: ignore [reportUnusedParameter]
    logging.disable(logging.CRITICAL)

    settings.configure(**TEST_SETTINGS)


TEST_SETTINGS = {
    "ALLOWED_HOSTS": ["*"],
    "DEBUG": False,
    "CACHES": {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    },
    "DATABASES": {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    },
    "DJANGO_BIRD": {
        # TODO: Remove once deprecated setting is removed
        "ENABLE_AUTO_CONFIG": False,
    },
    "EMAIL_BACKEND": "django.core.mail.backends.locmem.EmailBackend",
    "INSTALLED_APPS": [
        "django_bird",
        "django.contrib.staticfiles",
    ],
    "LOGGING_CONFIG": None,
    "PASSWORD_HASHERS": [
        "django.contrib.auth.hashers.MD5PasswordHasher",
    ],
    "SECRET_KEY": "not-a-secret",
    "STATIC_URL": "/static/",
    "STATICFILES_FINDERS": [
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    ],
    "TEMPLATES": [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [
                Path(__file__).parent / "templates",
            ],
            "OPTIONS": {
                "builtins": [
                    "django.template.defaulttags",
                ],
                "loaders": [
                    "django.template.loaders.filesystem.Loader",
                    "django.template.loaders.app_directories.Loader",
                ],
            },
        }
    ],
}
