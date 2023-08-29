FROM python:alpine
WORKDIR /data
COPY ./requirements.txt /data/
RUN pip3 install -r requirements.txt
COPY ./neural.py /data/
COPY ./generate.py /data/
COPY ./itemname.py /data/
COPY ./main.py /data/
CMD python3 main.py