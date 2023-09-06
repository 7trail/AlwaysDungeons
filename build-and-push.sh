#!/usr/bin/env bash
set -e
ORG="askiiart"
NAME="discord-always-dungeons"

# Apply patch for Docker
git apply docker.patch

# Build image
docker run -v .:/repo python /bin/sh -c "cd /repo && pip install -r requirements.txt && apt-get update && apt-get install binutils -y && pip install pyinstaller && pyinstaller main.py && cd /repo/dist/main && chmod -R 777 /repo/dist/main && tar cvfz /repo/AlwaysDungeons.tar.gz *"
ID=$(docker build . -q)

# Could just do -t on the build, but this makes it easier to expand if needed.
docker tag ${ID} ${ORG}/${NAME}:latest
docker push ${ORG}/${NAME}:latest
