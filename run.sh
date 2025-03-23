#!/bin/bash
#
docker stop $(docker ps -aq)
docker container rm -f $(docker container ls -aq)
docker volume rm -f $(docker volume ls -q)
docker rm $(docker ps -a -q)
docker-compose up --build -d
