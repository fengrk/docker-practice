from tensorflow/tensorflow:1.4.0-py3

RUN apt-get update && \
   apt-get -y install python3-tk git protobuf-compiler && \
   git clone https://github.com/tensorflow/models /tensorflow/models && \
   echo "/tensorflow/models/research/" | tee /usr/local/lib/python3.5/dist-packages/research.pth  && \
   echo "/tensorflow/models/research/slim" | tee /usr/local/lib/python3.5/dist-packages/slim.pth && \
   cd /tensorflow/models/research && protoc object_detection/protos/*.proto --python_out=. && \
   pip install flask requests