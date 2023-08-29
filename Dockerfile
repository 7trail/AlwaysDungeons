FROM python:latest
WORKDIR /data
COPY ./requirements.txt /data/
RUN pip3 install -r /data/requirements.txt
COPY ./*.py /data/
CMD python3 main.py