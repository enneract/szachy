#!/bin/bash
set -Eeuo pipefail

PACKAGE_PATH="$(dirname "$0")"
export PYTHONPATH="$PACKAGE_PATH"

python3 -m szachy
