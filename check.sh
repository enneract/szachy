#!/bin/bash
set -Eeuo pipefail

PACKAGE_PATH="$(dirname "$0")"
export PYTHONPATH="$PACKAGE_PATH"

flake8 --ignore=E501 "$PACKAGE_PATH/szachy"
mypy --strict --python-version=3.10 -p "szachy"
pytest "$PACKAGE_PATH/szachy"
