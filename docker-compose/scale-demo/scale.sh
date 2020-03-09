#!/bin/bash

for i in $(seq 1 10);
  do SERVER_INDEX=$i docker-compose up -d --scale py-server=$i --no-recreate;
done
