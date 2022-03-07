
# Train — A Python Sample Project

[![Tests](https://github.com/thunze/train/actions/workflows/tests.yml/badge.svg)](https://github.com/thunze/train/actions/workflows/tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/thunze/train/badge.svg?branch=dev&t=MaLMqA)](https://coveralls.io/github/thunze/train?branch=dev)
[![DeepSource](https://deepsource.io/gh/thunze/train.svg/?label=active+issues&show_trend=true&token=MANIVouBzNimIFTXsYQQJpau)](https://deepsource.io/gh/thunze/train/?ref=repository-badge)

## Features

- Dependency management using [Poetry](https://python-poetry.org/)
- GitHub action to run **tests** with coverage and upload the results to [Coveralls](https://coveralls.io/)
  - [pytest failure annotations](https://github.com/utgwkk/pytest-github-actions-annotate-failures) for GitHub
- GitHub action to build the application and create a new **release** whenever a version tag is pushed
  - Bundling of the application is done in a platform-independent manner using [PyInstaller](https://pyinstaller.readthedocs.io/)
- Integration of the [deepsource](https://deepsource.io/) static analysis platform
- [pre-commit](https://pre-commit.com/) hooks: [black](https://black.readthedocs.io/), [flake8](https://flake8.pycqa.org/), [mypy](https://mypy.readthedocs.io/), [isort](https://pycqa.github.io/isort/) and a few more
- Incorporation of best practices when accessing **static files** from Python using [importlib.resources](https://docs.python.org/3/library/importlib.html#module-importlib.resources)
- Some example code including tests
