#!/usr/bin/env bash
set -e
ORG="askiiart"
NAME="discord-always-dungeons"

# Apply patch for Docker
docker run -v .:/repo python /bin/bash -c "cd /repo && pip install -r requirements.txt && pip install pyinstaller && pyinstaller main.py && cd /repo/dist/main && chmod 777 /repo/dist/main/main"

# Build image
ID=$(docker build . -q)

# Could just do -t on the build, but this makes it easier to expand if needed.
docker tag ${ID} ${ORG}/${NAME}:latest
docker push ${ORG}/${NAME}:latest
