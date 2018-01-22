from tensorflow/tensorflow:1.4.0-py3

RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/' /etc/apt/sources.list \
    && apt-get update \
    &&  apt-get -y install python3-tk

RUN pip install bitarray==0.8.1 boto3==1.4.8 botocore==1.5.29 captcha==0.2.1 certifi==2016.9.26 jieba==0.38 scikit-image==0.12.3 wheezy.captcha[Pillow]==0.1.44 chardet==3.0.4
RUN apt-get -y install libffi-dev && pip install cffi==1.5.2
