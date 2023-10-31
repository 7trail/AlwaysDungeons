FROM python:slim-bookworm
WORKDIR /data
RUN apt update && apt install -y rust-all
ADD AlwaysDungeons.tar.gz /data
CMD ["/data/main"]