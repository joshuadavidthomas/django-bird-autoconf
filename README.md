# django-bird-autoconf

[![PyPI](https://img.shields.io/pypi/v/django-bird-autoconf)](https://pypi.org/project/django-bird-autoconf/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-bird-autoconf)
![Django Version](https://img.shields.io/badge/django-4.2%20%7C%205.0%20%7C%205.1%20%7C%205.2-%2344B78B?labelColor=%23092E20)
<!-- https://shields.io/badges -->
<!-- django-4.2 | 5.0 | 5.1 | 5.2-#44B78B -->
<!-- labelColor=%23092E20 -->

[django-bird](https://github.com/joshuadavidthomas/django-bird) plugin for autoconfiguring your Django project.

## Requirements

- Python 3.10, 3.11, 3.12, 3.13
- Django 4.2, 5.0, 5.1, 5.2
- django-bird >= 0.16.1

## Installation

1. Install the package from PyPI:

    ```bash
    python -m pip install django-bird-autoconf

    # or if you like the new hotness

    uv add django-bird-autoconf
    uv sync
    ```

2. The plugin should automatically be loaded by django-bird, no configuration required.

## Getting Started

After installation, django-bird-autoconf will automatically configure the necessary settings in your project needed for django-bird.

> [!NOTE]
> This plugin retains the same behavior as `settings.DJANGO_BIRD["ENABLE_AUTO_CONFIG"] = True` prior to v0.16.1. Please refer to the django-bird's [documentation](https://django-bird.readthedocs.io/configuration.html#manual-setup) on manual setup to see what it does.
