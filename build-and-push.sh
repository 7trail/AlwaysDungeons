#!/usr/bin/env bash
set -e
ORG="askiiart"
NAME="discord-always-dungeons"
ID=$(docker build . -q)

# Could just do -t on the build, but this makes it easier to expand if needed.
docker tag ${ID} ${ORG}/${NAME}:latest
docker push ${ORG}/${NAME}:latest
