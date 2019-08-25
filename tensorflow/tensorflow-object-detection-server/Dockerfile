from frkhit/docker-python:3.6

RUN apt-get update && \
   apt-get -y install python3-tk && \
   pip install flask requests tensorflow==1.14.0 pyxtools pymltools && \
   echo "/pylibs" | tee /usr/local/lib/python3.6/site-packages/pylibs.pth  && \
   cd / && curl -OL http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz && \
   tar -xzvf ssd_mobilenet_v2_coco_2018_03_29.tar.gz && mv ssd_mobilenet_v2_coco_2018_03_29 data && \
   rm ssd_mobilenet_v2_coco_2018_03_29.tar.gz && \
   cd / && curl -OL https://codeload.github.com/frkhit/ml_tools/zip/master && \
   unzip -qq master -d /pylibs && rm master && \
   mv /pylibs/ml_tools-master /pylibs/ml_tools && \
   rm -rf /var/lib/apt/lists/* && \
   rm -rf /root/.cache/pip/*

COPY server.py /app/server.py

