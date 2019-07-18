FROM tensorflow/tensorflow:1.12.0-gpu-py3

RUN pip install bert-serving-server && \
    mkdir -p /app && cd /app && \
    curl https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip -o chinese.zip && \
    unzpip chinese.zip && \
    rm /root/.cache/pip -R && \
    rm chinese.zip

WORKDIR /app

