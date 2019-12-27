FROM docker.elastic.co/elasticsearch/elasticsearch:7.5.1

RUN yes | bin/elasticsearch-plugin install ingest-attachment && \
    yes | bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.5.1/elasticsearch-analysis-ik-7.5.1.zip

