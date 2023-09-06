FROM python:slim-bookworm
WORKDIR /data
ADD AlwaysDungeons.tar.gz /data
CMD ["/data/main"]