#!/bin/bash

docker-compose --compatibility  up -d
sleep 1
docker-compose logs -f




