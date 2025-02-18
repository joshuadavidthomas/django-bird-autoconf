# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project attempts to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
## [${version}]
### Added - for new features
### Changed - for changes in existing functionality
### Deprecated - for soon-to-be removed features
### Removed - for now removed features
### Fixed - for any bug fixes
### Security - in case of vulnerabilities
[${version}]: https://github.com/joshuadavidthomas/django-bird/releases/tag/v${version}
-->

## [Unreleased]

## [0.1.1]

### Changed

- Bumped the minimum version of django-bird to v0.16.2.
- Changed hook implementation to use new `pre_ready` hook, in order to setup project settings before any template scanning or other internal initialization happens in core library.

## [0.1.0]

### Added

- Added autoconfiguration of a project using django-bird, copied from the current implementation in the core library.

### New Contributors

- Josh Thomas <josh@joshthomas.dev> (maintainer)

[unreleased]: https://github.com/joshuadavidthomas/django-bird-autoconf/compare/v0.1.1...HEAD
[0.1.0]: https://github.com/joshuadavidthomas/django-bird-autoconf/releases/tag/v0.1.0
[0.1.1]: https://github.com/joshuadavidthomas/django-bird-autoconf/releases/tag/v0.1.1
