#!/usr/bin/env bash
set -e
# ORG and NAME aren't used unless push is enabled.
ORG="askiiart"
NAME="discord-always-dungeons"
PUSH="false"


# Apply patch for Docker
git apply docker.patch

# Build image
docker run -v .:/repo python /bin/sh -c "apt update && apt install -y rustc && cd /repo && pip install -r requirements.txt && apt-get update && apt-get install binutils -y && pip install pyinstaller && pyinstaller main.py && cd /repo/dist/main && chmod -R 777 /repo/dist/main && tar cvfz /repo/AlwaysDungeons.tar.gz *"
ID=$(docker build . -q)

# Could just do -t on the build, but this makes it easier to expand if needed.
if [ $ID == "true" && $PUSH="true" ]; then
    docker tag ${ID} ${ORG}/${NAME}:latest
    docker push ${ORG}/${NAME}:latest
else
    echo Docker image ID: $ID
fi