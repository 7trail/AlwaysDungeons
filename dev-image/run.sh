#!/bin/bash
set -e
pip3 install -r /data/AlwaysDungeons/requirements.txt
cp /data/.env /data/AlwaysDungeons/.env
cd /data/AlwaysDungeons
python3 main.py
