FROM researchdeezer/spleeter:3.7-5stems

# 2stems
RUN mkdir -p /model/2stems && \
    wget -O /tmp/2stems.tar.gz https://github.com/deezer/spleeter/releases/download/v1.4.0/2stems.tar.gz && \
    tar -xvzf /tmp/2stems.tar.gz -C /model/2stems/ && \
    touch /model/2stems/.probe && \
    rm -f /tmp/*.tar.gz


# 4stems
RUN mkdir -p /model/4stems && \
    wget -O /tmp/4stems.tar.gz https://github.com/deezer/spleeter/releases/download/v1.4.0/4stems.tar.gz && \
    tar -xvzf /tmp/4stems.tar.gz -C /model/4stems/ && \
    touch /model/4stems/.probe && \
    rm -f /tmp/*.tar.gz

# install grpc
RUN apt-get update && \
    pip3 install jieba grpcio grpcio-tools && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache/pip/*
