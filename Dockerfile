FROM python:3.11-slim-bookworm
WORKDIR /data
ADD AlwaysDungeons.tar.gz /data
CMD ["/data/main"]