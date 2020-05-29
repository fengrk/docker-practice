#!/bin/bash
echo -n ./lock.file.log

for i in $(seq 1 10); do
  SERVER_INDEX=$i docker-compose up -d --scale py-server=$i --no-recreate;
  # if not work, use command below
  # echo "SERVER_INDEX=${i}" > .env && SERVER_INDEX=$i docker-compose up -d --scale py-server=$i --no-recreate
done
