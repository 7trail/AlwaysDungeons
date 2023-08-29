#!/bin/bash
set -e
cd /data
git clone https://github.com/7trail/AlwaysDungeons
cd /data/AlwaysDungeons
pip3 install -r requirements
cp /data/.env /data/AlwaysDungeons/.env
python3 main.py