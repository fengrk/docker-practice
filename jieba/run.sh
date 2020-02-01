#!/bin/bash

docker-compose up --scale jieba-test=3  -d
docker-compose logs -f


