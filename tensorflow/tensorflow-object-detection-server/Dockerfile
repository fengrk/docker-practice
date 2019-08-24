from tensorflow/tensorflow:1.4.0-py3

RUN apt-get update && \
   apt-get -y install python3-tk && \
   curl -OL curl -OL https://codeload.github.com/tensorflow/models/zip/master && \
   unzip -qq master -d /tensorflow && mv /tensorflow/models-master /tensorflow/models && rm -f /master && \
   echo "/tensorflow/models/research/" | tee /usr/local/lib/python3.5/dist-packages/research.pth  && \
   echo "/tensorflow/models/research/slim" | tee /usr/local/lib/python3.5/dist-packages/slim.pth && \
   cd / && curl -OL https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip && \
   unzip -qq protoc-3.2.0-linux-x86_64.zip -d protoc3 && \
   mv protoc3/bin/* /usr/local/bin/ && mv protoc3/include/* /usr/local/include/ && rm -rf protoc3/ && \
   cd /tensorflow/models/research && protoc object_detection/protos/*.proto --python_out=. && \
   pip install flask requests && \
   cd / && curl -OL http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz && \
   tar -xzvf ssd_mobilenet_v2_coco_2018_03_29.tar.gz && mv ssd_mobilenet_v2_coco_2018_03_29 data && \
   rm ssd_mobilenet_v2_coco_2018_03_29.tar.gz && \
   rm -rf /var/lib/apt/lists/* && \
   rm -rf /root/.cache/pip/*

