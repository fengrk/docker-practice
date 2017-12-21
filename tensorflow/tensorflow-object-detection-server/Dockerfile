from tensorflow/tensorflow:1.4.0-py3

RUN echo "/root/models/research/" | tee /usr/local/lib/python3.5/dist-packages/research.pth \
   && echo "/root/models/research/slim" | tee /usr/local/lib/python3.5/dist-packages/slim.pth \
   && pip install flask
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/' /etc/apt/sources.list \
    && apt-get update \
    &&  apt-get -y install python3-tk

RUN pip install requests 
