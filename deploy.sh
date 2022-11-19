#!/bin/bash
set -xEeuo pipefail

PACKAGE="szachy.tar.gz"
HOST="redman.xyz"
DESTDIR="/home/enneract/szachy"

ssh "$HOST" systemctl --user stop szachy
ssh "$HOST" rm -r "$DESTDIR"
ssh "$HOST" mkdir "$DESTDIR"
tar -czf - -T <(git ls-tree -r --name-only HEAD) | ssh "$HOST" tar -C "$DESTDIR" -xzf -
ssh "$HOST" systemctl --user start szachy
