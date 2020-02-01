FROM python:3.7-buster

ADD apt_list /apt_list
RUN mv /apt_list /etc/apt/sources.list && \
    apt-get update && \
    pip3 install jieba grpcio grpcio-tools paddlepaddle-tiny==1.6.1 -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache/pip/*

ENV PYTHONUNBUFFERED 1
WORKDIR /app

