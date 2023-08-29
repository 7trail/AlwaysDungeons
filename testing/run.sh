#!/bin/bash
set -e
git clone https://github.com/7trail/AlwaysDungeons
pip3 install -r data/AlwaysDungeons/requirements
cp /data/.env /data/AlwaysDungeons/.env
cd /data/AlwaysDungeons
python3 main.py